# A/B Testing Framework for Nykaa

A comprehensive Python-based A/B testing framework designed for e-commerce experimentation, specifically tailored for Nykaa, a well-known beauty and wellness brand.

## 🎯 Overview

This repository provides a complete toolkit for conducting, analyzing, and visualizing A/B tests in an e-commerce environment. It includes statistical analysis tools, visualization utilities, and sample notebooks to help you make data-driven decisions.

## 📋 Features

- **Statistical Analysis**
  - Two-proportion z-test
  - Chi-square test for independence
  - Confidence interval calculation
  - Bayesian A/B testing
  - Effect size calculation (Cohen's h)
  - Statistical power analysis

- **Visualization Tools**
  - Conversion rate comparisons
  - Sample size distributions
  - Funnel analysis
  - Cumulative results over time
  - Segment analysis visualizations
  - Comprehensive summary reports

- **Data Generation**
  - Sample A/B test data generator
  - E-commerce funnel data generator
  - CSV import/export utilities

- **Advanced Analysis**
  - Segment-level analysis (device, user type, demographics)
  - Sample size calculation
  - Multi-metric evaluation
  - Revenue impact analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Vinoth11111/A-B-Testing-Nykaa.git
cd A-B-Testing-Nykaa
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start

Run the example script to see the framework in action:

```bash
python example.py
```

This will:
- Generate sample e-commerce data
- Run a complete A/B test analysis
- Display detailed results
- Perform segment analysis
- Calculate sample sizes for future experiments

## 📊 Usage

### Basic A/B Test Analysis

```python
from ab_testing import ABTestAnalyzer
from utils.data_loader import DataLoader

# Load or generate data
loader = DataLoader()
data = loader.generate_ecommerce_data(n_users=5000)

# Initialize analyzer
analyzer = ABTestAnalyzer(data, control_group='A', treatment_group='B')

# Run analysis
results = analyzer.run_ab_test(alpha=0.05)

# Display results
print(f"Control Rate: {results['conversion_rates']['control']:.2%}")
print(f"Treatment Rate: {results['conversion_rates']['treatment']:.2%}")
print(f"Lift: {results['conversion_rates']['lift']:.2%}")
print(f"P-Value: {results['p_value']:.4f}")
print(f"Is Significant: {results['is_significant']}")
```

### Visualization

```python
from utils.visualizer import ABTestVisualizer

visualizer = ABTestVisualizer()

# Plot conversion rates
visualizer.plot_conversion_rates(results)

# Create comprehensive summary report
visualizer.create_summary_report(results, save_path='report.png')
```

### Segment Analysis

```python
# Analyze by device type
device_results = analyzer.segment_analysis('device')

# Visualize segment results
visualizer.plot_segment_analysis(device_results)
```

### Sample Size Calculation

```python
# Calculate required sample size
required_size = analyzer.calculate_sample_size(
    baseline_rate=0.12,      # 12% baseline conversion rate
    mde=0.10,                # 10% minimum detectable effect
    alpha=0.05,              # 5% significance level
    power=0.8                # 80% statistical power
)

print(f"Required sample size per group: {required_size}")
```

## 📁 Project Structure

```
A-B-Testing-Nykaa/
├── src/
│   ├── ab_testing/
│   │   ├── __init__.py
│   │   ├── analyzer.py           # Main A/B test analyzer
│   │   └── statistical_tests.py  # Statistical test functions
│   └── utils/
│       ├── __init__.py
│       ├── data_loader.py        # Data loading and generation
│       └── visualizer.py         # Visualization utilities
├── notebooks/
│   └── ab_test_analysis.ipynb    # Comprehensive analysis notebook
├── tests/
│   └── test_ab_testing.py        # Unit tests
├── data/                         # Data directory (gitignored)
├── example.py                    # Example usage script
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── LICENSE                       # MIT License
```

## 📓 Notebooks

The `notebooks` directory contains Jupyter notebooks with detailed examples:

- **ab_test_analysis.ipynb**: Complete walkthrough of A/B testing analysis including:
  - Data generation and loading
  - Statistical analysis
  - Visualization techniques
  - Segment analysis
  - Power analysis and sample size calculation

To run the notebooks:

```bash
jupyter notebook notebooks/ab_test_analysis.ipynb
```

## 🧪 Testing

Run the test suite to ensure everything is working correctly:

```bash
cd tests
python test_ab_testing.py
```

## 📈 Example Analyses for Nykaa

This framework can be used for various A/B testing scenarios at Nykaa:

1. **Website Design Changes**
   - Test new product page layouts
   - Evaluate checkout flow modifications
   - Compare CTA button designs

2. **Pricing Experiments**
   - Test discount strategies
   - Evaluate bundle offers
   - Compare free shipping thresholds

3. **Personalization**
   - Test product recommendations
   - Evaluate email campaign variations
   - Compare search result rankings

4. **Mobile vs Desktop**
   - Analyze performance across devices
   - Test mobile-specific features
   - Evaluate responsive design changes

## 📊 Statistical Methods

The framework implements industry-standard statistical methods:

- **Frequentist Approach**: Z-test for proportions with confidence intervals
- **Bayesian Approach**: Beta-Binomial model for probabilistic inference
- **Effect Size**: Cohen's h for practical significance
- **Power Analysis**: Calculate and verify statistical power
- **Multiple Testing**: Support for segment analysis with appropriate corrections

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**VINOTH KUMAR V**

## 🙏 Acknowledgments

- Built for Nykaa e-commerce experimentation
- Inspired by best practices in A/B testing from leading tech companies
- Statistical methods based on academic research in experimental design

## 📚 References

- Kohavi, R., Tang, D., & Xu, Y. (2020). Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing
- VanderPlas, J. (2016). Python Data Science Handbook
- SciPy Statistical Functions Documentation

---

**Note**: This framework is designed for educational and professional use. Always ensure proper statistical rigor and business context when making decisions based on A/B test results.