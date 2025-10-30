"""
Statistical Tests Module
Provides statistical test functions for A/B testing
"""

import numpy as np
from scipy import stats
from typing import Tuple, Dict


class StatisticalTests:
    """
    Collection of statistical tests for A/B testing.
    """
    
    @staticmethod
    def two_proportion_z_test(conversions_a: int, size_a: int,
                             conversions_b: int, size_b: int) -> Tuple[float, float]:
        """
        Perform two-proportion z-test.
        
        Args:
            conversions_a: Number of conversions in group A
            size_a: Sample size of group A
            conversions_b: Number of conversions in group B
            size_b: Sample size of group B
            
        Returns:
            Tuple of (z-statistic, p-value)
        """
        p_a = conversions_a / size_a
        p_b = conversions_b / size_b
        
        # Pooled proportion
        p_pooled = (conversions_a + conversions_b) / (size_a + size_b)
        
        # Standard error
        se = np.sqrt(p_pooled * (1 - p_pooled) * (1/size_a + 1/size_b))
        
        # Z-statistic
        z_stat = (p_b - p_a) / se if se > 0 else 0
        
        # Two-tailed p-value
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        return z_stat, p_value
    
    @staticmethod
    def chi_square_test(conversions_a: int, size_a: int,
                       conversions_b: int, size_b: int) -> Tuple[float, float]:
        """
        Perform chi-square test for independence.
        
        Args:
            conversions_a: Number of conversions in group A
            size_a: Sample size of group A
            conversions_b: Number of conversions in group B
            size_b: Sample size of group B
            
        Returns:
            Tuple of (chi-square statistic, p-value)
        """
        # Contingency table
        observed = np.array([
            [conversions_a, size_a - conversions_a],
            [conversions_b, size_b - conversions_b]
        ])
        
        chi2, p_value, dof, expected = stats.chi2_contingency(observed)
        
        return chi2, p_value
    
    @staticmethod
    def confidence_interval(conversions: int, size: int, 
                          alpha: float = 0.05) -> Tuple[float, float]:
        """
        Calculate confidence interval for a proportion.
        
        Args:
            conversions: Number of conversions
            size: Sample size
            alpha: Significance level (default: 0.05)
            
        Returns:
            Tuple of (lower_bound, upper_bound)
        """
        p = conversions / size
        z = stats.norm.ppf(1 - alpha/2)
        se = np.sqrt(p * (1 - p) / size)
        
        lower = p - z * se
        upper = p + z * se
        
        return max(0, lower), min(1, upper)
    
    @staticmethod
    def cohens_h(p1: float, p2: float) -> float:
        """
        Calculate Cohen's h effect size for proportions.
        
        Args:
            p1: Proportion in group 1
            p2: Proportion in group 2
            
        Returns:
            Cohen's h effect size
        """
        phi1 = 2 * np.arcsin(np.sqrt(p1))
        phi2 = 2 * np.arcsin(np.sqrt(p2))
        
        return phi2 - phi1
    
    @staticmethod
    def bayesian_ab_test(conversions_a: int, size_a: int,
                        conversions_b: int, size_b: int,
                        n_simulations: int = 100000) -> Dict:
        """
        Perform Bayesian A/B test using Beta distribution.
        
        Args:
            conversions_a: Number of conversions in group A
            size_a: Sample size of group A
            conversions_b: Number of conversions in group B
            size_b: Sample size of group B
            n_simulations: Number of Monte Carlo simulations
            
        Returns:
            Dictionary with Bayesian test results
        """
        # Beta priors (uniform prior: alpha=1, beta=1)
        alpha_a = 1 + conversions_a
        beta_a = 1 + size_a - conversions_a
        
        alpha_b = 1 + conversions_b
        beta_b = 1 + size_b - conversions_b
        
        # Sample from posterior distributions
        samples_a = np.random.beta(alpha_a, beta_a, n_simulations)
        samples_b = np.random.beta(alpha_b, beta_b, n_simulations)
        
        # Probability that B is better than A
        prob_b_better = (samples_b > samples_a).mean()
        
        # Expected loss
        expected_loss_a = np.maximum(samples_b - samples_a, 0).mean()
        expected_loss_b = np.maximum(samples_a - samples_b, 0).mean()
        
        return {
            'prob_b_better': prob_b_better,
            'prob_a_better': 1 - prob_b_better,
            'expected_loss_a': expected_loss_a,
            'expected_loss_b': expected_loss_b,
            'posterior_mean_a': samples_a.mean(),
            'posterior_mean_b': samples_b.mean()
        }
