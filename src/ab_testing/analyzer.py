"""
A/B Test Analyzer
Provides comprehensive analysis for A/B testing experiments
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional
from .statistical_tests import StatisticalTests


class ABTestAnalyzer:
    """
    A comprehensive A/B test analyzer for Nykaa experiments.
    
    This class provides methods to analyze A/B test results including
    conversion rate analysis, statistical significance testing, and
    effect size calculations.
    """
    
    def __init__(self, data: pd.DataFrame, control_group: str = 'A', 
                 treatment_group: str = 'B'):
        """
        Initialize the A/B Test Analyzer.
        
        Args:
            data: DataFrame containing test data with 'group' and 'converted' columns
            control_group: Name of the control group (default: 'A')
            treatment_group: Name of the treatment group (default: 'B')
        """
        self.data = data
        self.control_group = control_group
        self.treatment_group = treatment_group
        self.stats = StatisticalTests()
        
    def get_conversion_rates(self) -> Dict[str, float]:
        """
        Calculate conversion rates for each group.
        
        Returns:
            Dictionary with conversion rates for control and treatment groups
        """
        control_data = self.data[self.data['group'] == self.control_group]
        treatment_data = self.data[self.data['group'] == self.treatment_group]
        
        control_rate = control_data['converted'].mean()
        treatment_rate = treatment_data['converted'].mean()
        
        return {
            'control': control_rate,
            'treatment': treatment_rate,
            'lift': (treatment_rate - control_rate) / control_rate if control_rate > 0 else 0
        }
    
    def get_sample_sizes(self) -> Dict[str, int]:
        """
        Get sample sizes for each group.
        
        Returns:
            Dictionary with sample sizes for control and treatment groups
        """
        control_data = self.data[self.data['group'] == self.control_group]
        treatment_data = self.data[self.data['group'] == self.treatment_group]
        
        return {
            'control': len(control_data),
            'treatment': len(treatment_data),
            'total': len(self.data)
        }
    
    def run_ab_test(self, alpha: float = 0.05) -> Dict:
        """
        Run complete A/B test analysis.
        
        Args:
            alpha: Significance level (default: 0.05)
            
        Returns:
            Dictionary containing comprehensive test results
        """
        control_data = self.data[self.data['group'] == self.control_group]
        treatment_data = self.data[self.data['group'] == self.treatment_group]
        
        control_conversions = control_data['converted'].sum()
        treatment_conversions = treatment_data['converted'].sum()
        control_size = len(control_data)
        treatment_size = len(treatment_data)
        
        # Run z-test
        z_stat, p_value = self.stats.two_proportion_z_test(
            control_conversions, control_size,
            treatment_conversions, treatment_size
        )
        
        # Calculate confidence intervals
        control_ci = self.stats.confidence_interval(
            control_conversions, control_size, alpha
        )
        treatment_ci = self.stats.confidence_interval(
            treatment_conversions, treatment_size, alpha
        )
        
        # Calculate effect size
        effect_size = self.stats.cohens_h(
            control_conversions / control_size,
            treatment_conversions / treatment_size
        )
        
        conversion_rates = self.get_conversion_rates()
        
        return {
            'conversion_rates': conversion_rates,
            'sample_sizes': self.get_sample_sizes(),
            'z_statistic': z_stat,
            'p_value': p_value,
            'is_significant': p_value < alpha,
            'alpha': alpha,
            'control_ci': control_ci,
            'treatment_ci': treatment_ci,
            'effect_size': effect_size,
            'power': self._calculate_statistical_power(
                control_conversions / control_size,
                treatment_conversions / treatment_size,
                control_size, treatment_size, alpha
            )
        }
    
    def _calculate_statistical_power(self, p1: float, p2: float, 
                                     n1: int, n2: int, alpha: float) -> float:
        """
        Calculate statistical power of the test.
        
        Args:
            p1: Control group conversion rate
            p2: Treatment group conversion rate
            n1: Control group sample size
            n2: Treatment group sample size
            alpha: Significance level
            
        Returns:
            Statistical power
        """
        from scipy import stats
        
        pooled_p = (p1 * n1 + p2 * n2) / (n1 + n2)
        se_pooled = np.sqrt(pooled_p * (1 - pooled_p) * (1/n1 + 1/n2))
        se_alternative = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
        
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = (abs(p2 - p1) - z_alpha * se_pooled) / se_alternative
        
        power = stats.norm.cdf(z_beta)
        return power
    
    def calculate_sample_size(self, baseline_rate: float, mde: float,
                            alpha: float = 0.05, power: float = 0.8) -> int:
        """
        Calculate required sample size per group.
        
        Args:
            baseline_rate: Baseline conversion rate
            mde: Minimum detectable effect (as decimal, e.g., 0.05 for 5%)
            alpha: Significance level
            power: Desired statistical power
            
        Returns:
            Required sample size per group
        """
        from scipy import stats
        
        p1 = baseline_rate
        p2 = baseline_rate * (1 + mde)
        
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)
        
        pooled_p = (p1 + p2) / 2
        
        n = (z_alpha * np.sqrt(2 * pooled_p * (1 - pooled_p)) + 
             z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))**2 / (p2 - p1)**2
        
        return int(np.ceil(n))
    
    def segment_analysis(self, segment_column: str) -> pd.DataFrame:
        """
        Perform A/B test analysis for different segments.
        
        Args:
            segment_column: Column name to segment by
            
        Returns:
            DataFrame with results for each segment
        """
        results = []
        
        for segment in self.data[segment_column].unique():
            segment_data = self.data[self.data[segment_column] == segment]
            analyzer = ABTestAnalyzer(segment_data, self.control_group, 
                                     self.treatment_group)
            segment_results = analyzer.run_ab_test()
            
            results.append({
                'segment': segment,
                'control_rate': segment_results['conversion_rates']['control'],
                'treatment_rate': segment_results['conversion_rates']['treatment'],
                'lift': segment_results['conversion_rates']['lift'],
                'p_value': segment_results['p_value'],
                'is_significant': segment_results['is_significant'],
                'control_n': segment_results['sample_sizes']['control'],
                'treatment_n': segment_results['sample_sizes']['treatment']
            })
        
        return pd.DataFrame(results)
