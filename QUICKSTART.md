# Quick Start Guide - A/B Testing for Nykaa

This guide will help you get started with the A/B Testing framework in 5 minutes.

## Installation

```bash
# Clone the repository
git clone https://github.com/Vinoth11111/A-B-Testing-Nykaa.git
cd A-B-Testing-Nykaa

# Install dependencies
pip install -r requirements.txt
```

## Running Your First Test

### 1. Run the Example Script

```bash
python example.py
```

This will demonstrate a complete A/B test analysis with sample data.

### 2. Use in Your Python Script

```python
import sys
sys.path.append('src')

from ab_testing import ABTestAnalyzer
from utils.data_loader import DataLoader
from utils.visualizer import ABTestVisualizer

# Generate sample data
loader = DataLoader()
data = loader.generate_ecommerce_data(n_users=3000)

# Run analysis
analyzer = ABTestAnalyzer(data, control_group='A', treatment_group='B')
results = analyzer.run_ab_test()

# Print results
print(f"Control: {results['conversion_rates']['control']:.2%}")
print(f"Treatment: {results['conversion_rates']['treatment']:.2%}")
print(f"Lift: {results['conversion_rates']['lift']:.2%}")
print(f"P-value: {results['p_value']:.4f}")
print(f"Significant: {results['is_significant']}")

# Create visualization
visualizer = ABTestVisualizer()
visualizer.create_summary_report(results, save_path='ab_test_report.png')
```

### 3. Explore Jupyter Notebook

```bash
jupyter notebook notebooks/ab_test_analysis.ipynb
```

This notebook contains detailed examples with explanations.

## Working with Your Own Data

### Load CSV Data

```python
import pandas as pd

# Your data should have at least 'group' and 'converted' columns
data = pd.read_csv('your_data.csv')

# Run analysis
analyzer = ABTestAnalyzer(data)
results = analyzer.run_ab_test()
```

### Required Data Format

Your CSV should contain:
- `group`: Group identifier (e.g., 'A', 'B' or 'control', 'treatment')
- `converted`: Binary conversion indicator (0 or 1)

Optional columns for advanced analysis:
- `user_id`: Unique user identifier
- `device`: Device type (Mobile, Desktop, etc.)
- `user_type`: User segment (New, Returning, etc.)
- `revenue`: Revenue per conversion

Example:
```csv
user_id,group,converted,device,revenue
U001,A,1,Mobile,1299
U002,B,0,Desktop,0
U003,A,1,Mobile,2499
```

## Common Use Cases

### 1. Calculate Required Sample Size

```python
analyzer = ABTestAnalyzer(data)
required_size = analyzer.calculate_sample_size(
    baseline_rate=0.10,  # 10% baseline conversion
    mde=0.15,            # Want to detect 15% improvement
    alpha=0.05,          # 5% significance level
    power=0.8            # 80% power
)
print(f"Need {required_size} users per group")
```

### 2. Segment Analysis

```python
# Analyze by device type
device_results = analyzer.segment_analysis('device')
print(device_results)

# Visualize
visualizer.plot_segment_analysis(device_results)
```

### 3. Create Visualizations

```python
visualizer = ABTestVisualizer()

# Individual plots
visualizer.plot_conversion_rates(results)
visualizer.plot_sample_sizes(results)

# Comprehensive report
visualizer.create_summary_report(results, save_path='report.png')
```

## Running Tests

```bash
cd tests
python test_ab_testing.py
```

All tests should pass with "OK" message.

## Next Steps

1. Read the comprehensive [README.md](README.md) for detailed documentation
2. Explore the [Jupyter notebook](notebooks/ab_test_analysis.ipynb) for in-depth examples
3. Check the source code in `src/` for implementation details
4. Customize the framework for your specific needs

## Getting Help

- Check the example.py for working code
- Review test cases in tests/test_ab_testing.py
- Read docstrings in the source code
- Open an issue on GitHub

## Key Features to Remember

✅ Statistical significance testing (z-test)
✅ Effect size calculation (Cohen's h)
✅ Confidence intervals
✅ Statistical power analysis
✅ Sample size calculation
✅ Segment analysis
✅ Bayesian A/B testing
✅ Comprehensive visualizations

Happy Testing! 🎯
