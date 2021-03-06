"""
The :mod:`sklearn.tree` module includes decision tree-based models for
classification and regression.
"""

from .tree import DecisionTreeClassifier

from .tree import DecisionTreeRegressor
from .tree import ExtraTreeClassifier
from .tree import ExtraTreeRegressor
from .export import export_graphviz
from .export import feature_importance
from .export import uplift_adaboost


__all__ = ["DecisionTreeClassifier", "DecisionTreeRegressor",
           "ExtraTreeClassifier", "ExtraTreeRegressor", "export_graphviz","feature_importance"]
