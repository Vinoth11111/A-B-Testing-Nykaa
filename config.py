"""
Configuration file for A/B Testing Framework
Customize these settings for your experiments
"""

# Statistical Test Configuration
STATISTICAL_CONFIG = {
    # Default significance level (alpha)
    'alpha': 0.05,
    
    # Default statistical power for sample size calculations
    'power': 0.80,
    
    # Default minimum detectable effect (as proportion, e.g., 0.10 = 10%)
    'mde': 0.10,
    
    # Confidence level for confidence intervals
    'confidence_level': 0.95,
    
    # Number of simulations for Bayesian analysis
    'bayesian_simulations': 100000,
}

# Data Configuration
DATA_CONFIG = {
    # Default group names
    'control_group': 'A',
    'treatment_group': 'B',
    
    # Default conversion column name
    'conversion_column': 'converted',
    
    # Default group column name
    'group_column': 'group',
    
    # Default data directory
    'data_directory': 'data/',
}

# Visualization Configuration
VISUALIZATION_CONFIG = {
    # Default matplotlib style
    'style': 'seaborn-v0_8-darkgrid',
    
    # Default figure size (width, height)
    'figsize': (12, 6),
    
    # Default DPI for saved figures
    'dpi': 300,
    
    # Color scheme
    'colors': {
        'control': '#3498db',      # Blue
        'treatment': '#e74c3c',    # Red
        'positive': '#27ae60',     # Green
        'negative': '#e67e22',     # Orange
    },
    
    # Default save directory for plots
    'output_directory': 'output/',
}

# E-commerce Specific Configuration (for Nykaa)
ECOMMERCE_CONFIG = {
    # Funnel stages in order
    'funnel_stages': [
        'viewed_product',
        'added_to_cart',
        'initiated_checkout',
        'completed_purchase'
    ],
    
    # Common segments to analyze
    'segments': [
        'device',
        'user_type',
        'age_group',
        'category',
    ],
    
    # Device types
    'device_types': ['Mobile', 'Desktop', 'Tablet'],
    
    # User types
    'user_types': ['New', 'Returning'],
    
    # Age groups
    'age_groups': ['18-24', '25-34', '35-44', '45+'],
}

# Reporting Configuration
REPORTING_CONFIG = {
    # Include these metrics in reports by default
    'default_metrics': [
        'conversion_rate',
        'sample_size',
        'z_statistic',
        'p_value',
        'effect_size',
        'confidence_interval',
        'statistical_power',
    ],
    
    # Report format
    'format': 'detailed',  # 'detailed' or 'summary'
    
    # Decimal places for rounding
    'decimal_places': 4,
}

# Experiment Tracking
EXPERIMENT_CONFIG = {
    # Experiment metadata to track
    'metadata_fields': [
        'experiment_name',
        'start_date',
        'end_date',
        'hypothesis',
        'success_metric',
        'sample_size_per_group',
    ],
    
    # Auto-save results
    'auto_save': True,
    
    # Results directory
    'results_directory': 'results/',
}

# Advanced Settings
ADVANCED_CONFIG = {
    # Enable multiple testing correction
    'multiple_testing_correction': False,
    
    # Correction method ('bonferroni', 'benjamini-hochberg')
    'correction_method': 'bonferroni',
    
    # Enable sequential testing
    'sequential_testing': False,
    
    # Minimum runtime for experiments (in days)
    'minimum_runtime_days': 7,
    
    # Maximum runtime for experiments (in days)
    'maximum_runtime_days': 30,
}

# Thresholds
THRESHOLDS = {
    # Effect size thresholds (Cohen's h)
    'effect_size': {
        'small': 0.2,
        'medium': 0.5,
        'large': 0.8,
    },
    
    # Sample size warnings
    'min_sample_size_per_group': 100,
    'recommended_sample_size_per_group': 1000,
    
    # Conversion rate boundaries
    'min_conversion_rate': 0.001,  # 0.1%
    'max_conversion_rate': 0.999,  # 99.9%
}
