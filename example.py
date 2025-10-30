"""
Example script demonstrating A/B testing framework for Nykaa
"""

import sys
sys.path.append('src')

from ab_testing import ABTestAnalyzer
from utils.data_loader import DataLoader
from utils.visualizer import ABTestVisualizer


def main():
    """Run a simple A/B test analysis example."""
    
    print("=" * 70)
    print("A/B TESTING FRAMEWORK FOR NYKAA - EXAMPLE")
    print("=" * 70)
    print()
    
    # Generate sample data
    print("1. Generating sample e-commerce data...")
    loader = DataLoader()
    data = loader.generate_ecommerce_data(n_users=3000, random_seed=42)
    print(f"   Generated {len(data)} user records")
    print()
    
    # Initialize analyzer
    print("2. Running A/B test analysis...")
    analyzer = ABTestAnalyzer(data, control_group='A', treatment_group='B')
    
    # Run analysis
    results = analyzer.run_ab_test(alpha=0.05)
    print()
    
    # Display results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()
    
    print("CONVERSION RATES:")
    print(f"  Control (A):    {results['conversion_rates']['control']:.2%}")
    print(f"  Treatment (B):  {results['conversion_rates']['treatment']:.2%}")
    print(f"  Lift:           {results['conversion_rates']['lift']:+.2%}")
    print()
    
    print("SAMPLE SIZES:")
    print(f"  Control (A):    {results['sample_sizes']['control']:,}")
    print(f"  Treatment (B):  {results['sample_sizes']['treatment']:,}")
    print()
    
    print("STATISTICAL TEST:")
    print(f"  Z-Statistic:    {results['z_statistic']:.4f}")
    print(f"  P-Value:        {results['p_value']:.4f}")
    print(f"  Significant:    {'Yes ✓' if results['is_significant'] else 'No ✗'} (α = {results['alpha']})")
    print()
    
    print("EFFECT SIZE & POWER:")
    print(f"  Cohen's h:      {results['effect_size']:.4f}")
    print(f"  Power:          {results['power']:.2%}")
    print()
    
    print("CONFIDENCE INTERVALS (95%):")
    print(f"  Control:        [{results['control_ci'][0]:.4f}, {results['control_ci'][1]:.4f}]")
    print(f"  Treatment:      [{results['treatment_ci'][0]:.4f}, {results['treatment_ci'][1]:.4f}]")
    print()
    
    print("=" * 70)
    print()
    
    # Segment analysis
    print("3. Running segment analysis by device...")
    segment_results = analyzer.segment_analysis('device')
    print()
    print(segment_results.to_string(index=False))
    print()
    
    # Sample size calculation
    print("4. Calculating required sample size for future experiments...")
    required_size = analyzer.calculate_sample_size(
        baseline_rate=0.12,
        mde=0.10,
        alpha=0.05,
        power=0.8
    )
    print(f"   Required sample size per group: {required_size:,}")
    print(f"   Total required sample size: {required_size * 2:,}")
    print()
    
    print("=" * 70)
    print("Analysis complete! Check the notebooks folder for detailed examples.")
    print("=" * 70)


if __name__ == "__main__":
    main()
