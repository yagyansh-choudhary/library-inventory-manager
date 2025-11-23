"""
Library Manager Package
A simple library inventory management system.
"""

__version__ = "1.0.0"
__author__ = "Yagyansh Singh Ahlawat"
__email__ = "2501010120@krmu.edu.in"

from library_manager.book import Book
from library_manager.inventory import LibraryInventory

__all__ = ['Book', 'LibraryInventory']