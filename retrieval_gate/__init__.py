"""A small lexical retriever that has to pass its own evaluation before it is trusted."""
from .index import build_index, load_index
from .search import search_report
from .evaluate import evaluate

__all__ = ["build_index", "load_index", "search_report", "evaluate"]
