"""
Visualization utilities for A/B testing results
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Dict, List, Optional


class ABTestVisualizer:
    """
    Visualization tools for A/B test results.
    """
    
    def __init__(self, style: str = 'seaborn-v0_8-darkgrid'):
        """
        Initialize visualizer with a specific style.
        
        Args:
            style: Matplotlib style to use
        """
        try:
            plt.style.use(style)
        except:
            plt.style.use('default')
        sns.set_palette("husl")
    
    def plot_conversion_rates(self, results: Dict, save_path: Optional[str] = None):
        """
        Plot conversion rates comparison.
        
        Args:
            results: Results dictionary from ABTestAnalyzer.run_ab_test()
            save_path: Optional path to save the figure
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        groups = ['Control', 'Treatment']
        rates = [
            results['conversion_rates']['control'],
            results['conversion_rates']['treatment']
        ]
        
        colors = ['#3498db', '#e74c3c']
        bars = ax.bar(groups, rates, color=colors, alpha=0.7, edgecolor='black')
        
        # Add value labels on bars
        for i, (bar, rate) in enumerate(zip(bars, rates)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{rate:.2%}',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        # Add confidence intervals
        ci_control = results['control_ci']
        ci_treatment = results['treatment_ci']
        
        ax.errorbar([0, 1], rates,
                   yerr=[[rates[0] - ci_control[0], rates[1] - ci_treatment[0]],
                         [ci_control[1] - rates[0], ci_treatment[1] - rates[1]]],
                   fmt='none', color='black', capsize=5, capthick=2)
        
        ax.set_ylabel('Conversion Rate', fontsize=12)
        ax.set_title('A/B Test: Conversion Rate Comparison', fontsize=14, fontweight='bold')
        ax.set_ylim(0, max(rates) * 1.3)
        
        # Add significance indicator
        if results['is_significant']:
            ax.text(0.5, max(rates) * 1.15, '***Statistically Significant***',
                   ha='center', fontsize=12, color='green', fontweight='bold')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_sample_sizes(self, results: Dict, save_path: Optional[str] = None):
        """
        Plot sample size comparison.
        
        Args:
            results: Results dictionary from ABTestAnalyzer.run_ab_test()
            save_path: Optional path to save the figure
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        groups = ['Control', 'Treatment']
        sizes = [
            results['sample_sizes']['control'],
            results['sample_sizes']['treatment']
        ]
        
        colors = ['#3498db', '#e74c3c']
        bars = ax.bar(groups, sizes, color=colors, alpha=0.7, edgecolor='black')
        
        # Add value labels on bars
        for bar, size in zip(bars, sizes):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{size:,}',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        ax.set_ylabel('Sample Size', fontsize=12)
        ax.set_title('A/B Test: Sample Size Distribution', fontsize=14, fontweight='bold')
        ax.set_ylim(0, max(sizes) * 1.2)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_funnel_analysis(self, data: pd.DataFrame, stages: List[str],
                           group_col: str = 'group', save_path: Optional[str] = None):
        """
        Plot funnel analysis for both groups.
        
        Args:
            data: DataFrame with user data
            stages: List of stage column names in order
            group_col: Column name for group assignment
            save_path: Optional path to save the figure
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        groups = data[group_col].unique()
        x = np.arange(len(stages))
        width = 0.35
        
        for i, group in enumerate(groups):
            group_data = data[data[group_col] == group]
            stage_rates = [group_data[stage].mean() for stage in stages]
            
            offset = width * (i - 0.5)
            bars = ax.bar(x + offset, stage_rates, width, 
                         label=f'Group {group}', alpha=0.7)
            
            # Add value labels
            for bar, rate in zip(bars, stage_rates):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{rate:.1%}',
                       ha='center', va='bottom', fontsize=9)
        
        ax.set_ylabel('Conversion Rate', fontsize=12)
        ax.set_title('Funnel Analysis by Group', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(stages)
        ax.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_cumulative_results(self, data: pd.DataFrame, 
                              date_col: str = 'date',
                              group_col: str = 'group',
                              conversion_col: str = 'converted',
                              save_path: Optional[str] = None):
        """
        Plot cumulative conversion rates over time.
        
        Args:
            data: DataFrame with temporal data
            date_col: Column name for date
            group_col: Column name for group
            conversion_col: Column name for conversion indicator
            save_path: Optional path to save the figure
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        data_sorted = data.sort_values(date_col)
        
        for group in data_sorted[group_col].unique():
            group_data = data_sorted[data_sorted[group_col] == group]
            cumulative_rate = group_data[conversion_col].expanding().mean()
            
            ax.plot(range(len(cumulative_rate)), cumulative_rate,
                   label=f'Group {group}', linewidth=2)
        
        ax.set_xlabel('Number of Observations', fontsize=12)
        ax.set_ylabel('Cumulative Conversion Rate', fontsize=12)
        ax.set_title('Cumulative Conversion Rate Over Time', 
                    fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_segment_analysis(self, segment_results: pd.DataFrame,
                            save_path: Optional[str] = None):
        """
        Plot segment-wise A/B test results.
        
        Args:
            segment_results: DataFrame from ABTestAnalyzer.segment_analysis()
            save_path: Optional path to save the figure
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        segments = segment_results['segment']
        x = np.arange(len(segments))
        width = 0.35
        
        # Plot conversion rates
        ax1.bar(x - width/2, segment_results['control_rate'], width,
               label='Control', alpha=0.7, color='#3498db')
        ax1.bar(x + width/2, segment_results['treatment_rate'], width,
               label='Treatment', alpha=0.7, color='#e74c3c')
        
        ax1.set_ylabel('Conversion Rate', fontsize=12)
        ax1.set_title('Conversion Rates by Segment', fontsize=14, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(segments, rotation=45, ha='right')
        ax1.legend()
        
        # Plot lift
        colors = ['green' if sig else 'gray' 
                 for sig in segment_results['is_significant']]
        bars = ax2.bar(segments, segment_results['lift'] * 100, 
                      color=colors, alpha=0.7)
        
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax2.set_ylabel('Lift (%)', fontsize=12)
        ax2.set_title('Lift by Segment', fontsize=14, fontweight='bold')
        ax2.set_xticklabels(segments, rotation=45, ha='right')
        
        # Add value labels
        for bar, lift in zip(bars, segment_results['lift'] * 100):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{lift:.1f}%',
                    ha='center', va='bottom' if height > 0 else 'top',
                    fontsize=9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def create_summary_report(self, results: Dict, save_path: Optional[str] = None):
        """
        Create a comprehensive visual summary report.
        
        Args:
            results: Results dictionary from ABTestAnalyzer.run_ab_test()
            save_path: Optional path to save the figure
        """
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
        
        # Conversion rates
        ax1 = fig.add_subplot(gs[0, 0])
        groups = ['Control', 'Treatment']
        rates = [
            results['conversion_rates']['control'],
            results['conversion_rates']['treatment']
        ]
        colors = ['#3498db', '#e74c3c']
        bars = ax1.bar(groups, rates, color=colors, alpha=0.7, edgecolor='black')
        
        for bar, rate in zip(bars, rates):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{rate:.2%}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        ax1.set_ylabel('Conversion Rate')
        ax1.set_title('Conversion Rates', fontweight='bold')
        
        # Sample sizes
        ax2 = fig.add_subplot(gs[0, 1])
        sizes = [
            results['sample_sizes']['control'],
            results['sample_sizes']['treatment']
        ]
        ax2.bar(groups, sizes, color=colors, alpha=0.7, edgecolor='black')
        
        for i, size in enumerate(sizes):
            ax2.text(i, size, f'{size:,}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        ax2.set_ylabel('Sample Size')
        ax2.set_title('Sample Sizes', fontweight='bold')
        
        # Statistical summary (text)
        ax3 = fig.add_subplot(gs[1, :])
        ax3.axis('off')
        
        summary_text = f"""
        Statistical Test Results:
        
        Lift: {results['conversion_rates']['lift']:.2%}
        Z-Statistic: {results['z_statistic']:.4f}
        P-Value: {results['p_value']:.4f}
        Significance Level (α): {results['alpha']}
        Is Significant: {'Yes' if results['is_significant'] else 'No'}
        Effect Size (Cohen\'s h): {results['effect_size']:.4f}
        Statistical Power: {results['power']:.2%}
        
        Control CI: [{results['control_ci'][0]:.4f}, {results['control_ci'][1]:.4f}]
        Treatment CI: [{results['treatment_ci'][0]:.4f}, {results['treatment_ci'][1]:.4f}]
        """
        
        ax3.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=12, family='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
        
        # Effect size visualization
        ax4 = fig.add_subplot(gs[2, 0])
        effect_size = results['effect_size']
        effect_categories = ['Small\n(0.2)', 'Medium\n(0.5)', 'Large\n(0.8)']
        thresholds = [0.2, 0.5, 0.8]
        
        colors_effect = ['green' if abs(effect_size) >= t else 'lightgray' 
                        for t in thresholds]
        ax4.barh(effect_categories, thresholds, color=colors_effect, alpha=0.7)
        ax4.axvline(x=abs(effect_size), color='red', linestyle='--', 
                   linewidth=2, label=f'Actual: {abs(effect_size):.3f}')
        
        ax4.set_xlabel('Effect Size')
        ax4.set_title('Effect Size Interpretation', fontweight='bold')
        ax4.legend()
        
        # Power analysis
        ax5 = fig.add_subplot(gs[2, 1])
        power_value = results['power']
        
        categories = ['Achieved\nPower', 'Target\nPower\n(0.8)']
        values = [power_value, 0.8]
        colors_power = ['green' if power_value >= 0.8 else 'orange', 'lightblue']
        
        bars = ax5.bar(categories, values, color=colors_power, alpha=0.7, edgecolor='black')
        
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax5.text(bar.get_x() + bar.get_width()/2., height,
                    f'{value:.2%}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        ax5.set_ylabel('Statistical Power')
        ax5.set_title('Statistical Power Analysis', fontweight='bold')
        ax5.set_ylim(0, 1.1)
        
        plt.suptitle('A/B Test Summary Report - Nykaa', 
                    fontsize=16, fontweight='bold', y=0.98)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
