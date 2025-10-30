"""
A/B Testing Framework for Nykaa
A comprehensive framework for conducting and analyzing A/B tests
"""

__version__ = "1.0.0"
__author__ = "VINOTH KUMAR V"

from .analyzer import ABTestAnalyzer
from .statistical_tests import StatisticalTests

__all__ = ['ABTestAnalyzer', 'StatisticalTests']
