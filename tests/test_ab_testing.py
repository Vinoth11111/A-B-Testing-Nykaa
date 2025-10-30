"""
Unit tests for A/B testing framework
"""

import unittest
import sys
sys.path.append('../src')

import pandas as pd
import numpy as np
from ab_testing import ABTestAnalyzer, StatisticalTests
from utils.data_loader import DataLoader


class TestStatisticalTests(unittest.TestCase):
    """Test cases for StatisticalTests class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.stats = StatisticalTests()
    
    def test_two_proportion_z_test(self):
        """Test two-proportion z-test calculation."""
        z_stat, p_value = self.stats.two_proportion_z_test(
            conversions_a=100, size_a=1000,
            conversions_b=120, size_b=1000
        )
        
        self.assertIsInstance(z_stat, float)
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(p_value, 0)
        self.assertLessEqual(p_value, 1)
    
    def test_chi_square_test(self):
        """Test chi-square test calculation."""
        chi2, p_value = self.stats.chi_square_test(
            conversions_a=100, size_a=1000,
            conversions_b=120, size_b=1000
        )
        
        self.assertIsInstance(chi2, float)
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(chi2, 0)
        self.assertGreaterEqual(p_value, 0)
        self.assertLessEqual(p_value, 1)
    
    def test_confidence_interval(self):
        """Test confidence interval calculation."""
        lower, upper = self.stats.confidence_interval(
            conversions=100, size=1000, alpha=0.05
        )
        
        self.assertIsInstance(lower, float)
        self.assertIsInstance(upper, float)
        self.assertLess(lower, upper)
        self.assertGreaterEqual(lower, 0)
        self.assertLessEqual(upper, 1)
    
    def test_cohens_h(self):
        """Test Cohen's h effect size calculation."""
        h = self.stats.cohens_h(p1=0.1, p2=0.12)
        
        self.assertIsInstance(h, float)


class TestABTestAnalyzer(unittest.TestCase):
    """Test cases for ABTestAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Generate sample data
        loader = DataLoader()
        self.data = loader.generate_sample_data(
            n_control=1000, n_treatment=1000,
            control_rate=0.10, treatment_rate=0.12,
            random_seed=42
        )
        self.analyzer = ABTestAnalyzer(self.data)
    
    def test_initialization(self):
        """Test analyzer initialization."""
        self.assertIsInstance(self.analyzer.data, pd.DataFrame)
        self.assertEqual(self.analyzer.control_group, 'A')
        self.assertEqual(self.analyzer.treatment_group, 'B')
    
    def test_get_conversion_rates(self):
        """Test conversion rate calculation."""
        rates = self.analyzer.get_conversion_rates()
        
        self.assertIn('control', rates)
        self.assertIn('treatment', rates)
        self.assertIn('lift', rates)
        
        self.assertGreaterEqual(rates['control'], 0)
        self.assertLessEqual(rates['control'], 1)
        self.assertGreaterEqual(rates['treatment'], 0)
        self.assertLessEqual(rates['treatment'], 1)
    
    def test_get_sample_sizes(self):
        """Test sample size calculation."""
        sizes = self.analyzer.get_sample_sizes()
        
        self.assertIn('control', sizes)
        self.assertIn('treatment', sizes)
        self.assertIn('total', sizes)
        
        self.assertEqual(sizes['total'], sizes['control'] + sizes['treatment'])
    
    def test_run_ab_test(self):
        """Test complete A/B test analysis."""
        results = self.analyzer.run_ab_test(alpha=0.05)
        
        # Check all expected keys are present
        expected_keys = [
            'conversion_rates', 'sample_sizes', 'z_statistic', 'p_value',
            'is_significant', 'alpha', 'control_ci', 'treatment_ci',
            'effect_size', 'power'
        ]
        
        for key in expected_keys:
            self.assertIn(key, results)
        
        # Check value types and ranges
        self.assertIn(results['is_significant'], [True, False])
        self.assertEqual(results['alpha'], 0.05)
        self.assertGreaterEqual(results['p_value'], 0)
        self.assertLessEqual(results['p_value'], 1)
        self.assertGreaterEqual(results['power'], 0)
        self.assertLessEqual(results['power'], 1)
    
    def test_calculate_sample_size(self):
        """Test sample size calculation."""
        required_size = self.analyzer.calculate_sample_size(
            baseline_rate=0.10,
            mde=0.20,
            alpha=0.05,
            power=0.8
        )
        
        self.assertIsInstance(required_size, int)
        self.assertGreater(required_size, 0)


class TestDataLoader(unittest.TestCase):
    """Test cases for DataLoader class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.loader = DataLoader()
    
    def test_generate_sample_data(self):
        """Test sample data generation."""
        data = self.loader.generate_sample_data(
            n_control=500, n_treatment=500,
            control_rate=0.1, treatment_rate=0.12,
            random_seed=42
        )
        
        self.assertEqual(len(data), 1000)
        self.assertIn('group', data.columns)
        self.assertIn('converted', data.columns)
        self.assertIn('user_id', data.columns)
        
        # Check group distribution
        self.assertEqual(data[data['group'] == 'A'].shape[0], 500)
        self.assertEqual(data[data['group'] == 'B'].shape[0], 500)
    
    def test_generate_ecommerce_data(self):
        """Test e-commerce data generation."""
        data = self.loader.generate_ecommerce_data(n_users=1000, random_seed=42)
        
        self.assertEqual(len(data), 1000)
        
        # Check required columns
        required_cols = [
            'user_id', 'group', 'device', 'user_type', 'age_group',
            'viewed_product', 'added_to_cart', 'initiated_checkout',
            'completed_purchase', 'revenue', 'converted'
        ]
        
        for col in required_cols:
            self.assertIn(col, data.columns)


if __name__ == '__main__':
    unittest.main()
