"""
Data loading and generation utilities
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional


class DataLoader:
    """
    Utility class for loading and generating A/B test data.
    """
    
    @staticmethod
    def generate_sample_data(n_control: int = 1000, n_treatment: int = 1000,
                           control_rate: float = 0.10, treatment_rate: float = 0.12,
                           random_seed: Optional[int] = 42) -> pd.DataFrame:
        """
        Generate sample A/B test data.
        
        Args:
            n_control: Number of users in control group
            n_treatment: Number of users in treatment group
            control_rate: Conversion rate for control group
            treatment_rate: Conversion rate for treatment group
            random_seed: Random seed for reproducibility
            
        Returns:
            DataFrame with sample A/B test data
        """
        if random_seed is not None:
            np.random.seed(random_seed)
        
        # Generate control group
        control_data = pd.DataFrame({
            'user_id': [f'C_{i:06d}' for i in range(n_control)],
            'group': 'A',
            'converted': np.random.binomial(1, control_rate, n_control)
        })
        
        # Generate treatment group
        treatment_data = pd.DataFrame({
            'user_id': [f'T_{i:06d}' for i in range(n_treatment)],
            'group': 'B',
            'converted': np.random.binomial(1, treatment_rate, n_treatment)
        })
        
        # Combine data
        data = pd.concat([control_data, treatment_data], ignore_index=True)
        
        # Add timestamps
        start_date = datetime.now() - timedelta(days=30)
        data['timestamp'] = [
            start_date + timedelta(
                seconds=np.random.randint(0, 30*24*60*60)
            ) for _ in range(len(data))
        ]
        
        return data.sort_values('timestamp').reset_index(drop=True)
    
    @staticmethod
    def generate_ecommerce_data(n_users: int = 2000,
                               random_seed: Optional[int] = 42) -> pd.DataFrame:
        """
        Generate sample e-commerce A/B test data for Nykaa.
        
        Args:
            n_users: Total number of users
            random_seed: Random seed for reproducibility
            
        Returns:
            DataFrame with e-commerce funnel data
        """
        if random_seed is not None:
            np.random.seed(random_seed)
        
        # Split users into groups
        groups = np.random.choice(['A', 'B'], size=n_users)
        
        data = pd.DataFrame({
            'user_id': [f'U_{i:06d}' for i in range(n_users)],
            'group': groups
        })
        
        # Add user segments
        data['device'] = np.random.choice(
            ['Mobile', 'Desktop', 'Tablet'],
            size=n_users,
            p=[0.6, 0.35, 0.05]
        )
        
        data['user_type'] = np.random.choice(
            ['New', 'Returning'],
            size=n_users,
            p=[0.4, 0.6]
        )
        
        data['age_group'] = np.random.choice(
            ['18-24', '25-34', '35-44', '45+'],
            size=n_users,
            p=[0.3, 0.4, 0.2, 0.1]
        )
        
        # Funnel stages with different rates for A/B groups
        # Control group (A) - baseline rates
        control_rates = {
            'viewed_product': 0.8,
            'added_to_cart': 0.4,
            'initiated_checkout': 0.25,
            'completed_purchase': 0.12
        }
        
        # Treatment group (B) - improved rates
        treatment_rates = {
            'viewed_product': 0.82,
            'added_to_cart': 0.45,
            'initiated_checkout': 0.28,
            'completed_purchase': 0.15
        }
        
        # Generate funnel data
        for stage in control_rates.keys():
            data[stage] = 0
            
            # Control group
            control_mask = data['group'] == 'A'
            if stage == 'viewed_product':
                data.loc[control_mask, stage] = np.random.binomial(
                    1, control_rates[stage], control_mask.sum()
                )
            else:
                prev_stage = list(control_rates.keys())[
                    list(control_rates.keys()).index(stage) - 1
                ]
                data.loc[control_mask, stage] = (
                    data.loc[control_mask, prev_stage] & 
                    np.random.binomial(
                        1, control_rates[stage] / control_rates[prev_stage],
                        control_mask.sum()
                    )
                )
            
            # Treatment group
            treatment_mask = data['group'] == 'B'
            if stage == 'viewed_product':
                data.loc[treatment_mask, stage] = np.random.binomial(
                    1, treatment_rates[stage], treatment_mask.sum()
                )
            else:
                prev_stage = list(treatment_rates.keys())[
                    list(treatment_rates.keys()).index(stage) - 1
                ]
                data.loc[treatment_mask, stage] = (
                    data.loc[treatment_mask, prev_stage] & 
                    np.random.binomial(
                        1, treatment_rates[stage] / treatment_rates[prev_stage],
                        treatment_mask.sum()
                    )
                )
        
        # Add revenue for purchases
        data['revenue'] = 0.0
        purchased = data['completed_purchase'] == 1
        data.loc[purchased, 'revenue'] = np.random.gamma(
            shape=2, scale=500, size=purchased.sum()
        )
        
        # Add timestamps
        start_date = datetime.now() - timedelta(days=30)
        data['date'] = [
            start_date + timedelta(days=np.random.randint(0, 30))
            for _ in range(n_users)
        ]
        
        # Primary conversion metric
        data['converted'] = data['completed_purchase']
        
        return data
    
    @staticmethod
    def load_from_csv(file_path: str) -> pd.DataFrame:
        """
        Load A/B test data from CSV file.
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            DataFrame with loaded data
        """
        return pd.read_csv(file_path)
    
    @staticmethod
    def save_to_csv(data: pd.DataFrame, file_path: str):
        """
        Save A/B test data to CSV file.
        
        Args:
            data: DataFrame to save
            file_path: Path to save CSV file
        """
        data.to_csv(file_path, index=False)
