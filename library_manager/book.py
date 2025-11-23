"""
Book Class Module
Handles individual book objects with their attributes and operations.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Book:
    """
    Represents a book in the library inventory.
    
    Attributes:
        title (str): Title of the book
        author (str): Author of the book
        isbn (str): Unique ISBN number
        status (str): Current status - 'available' or 'issued'
    """
    
    def __init__(self, title, author, isbn, status="available"):
        """
        Initialize a Book object.
        
        Args:
            title (str): Book title
            author (str): Book author
            isbn (str): Book ISBN
            status (str): Book status (default: 'available')
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
        logging.info(f"Book created: {self.title} by {self.author}")
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Formatted book information
        """
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"Status: {self.status}")
    
    def to_dict(self):
        """
        Convert book object to dictionary for JSON serialization.
        
        Returns:
            dict: Book data as dictionary
        """
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'status': self.status
        }
    
    def issue(self):
        """
        Issue the book if available.
        
        Returns:
            bool: True if issued successfully, False otherwise
        """
        if self.status == "available":
            self.status = "issued"
            logging.info(f"✅ Book issued: {self.title} (ISBN: {self.isbn})")
            print(f"📖 '{self.title}' status changed to: ISSUED")
            return True
        else:
            logging.warning(f"⚠️  Book already issued: {self.title} (ISBN: {self.isbn})")
            return False
    
    def return_book(self):
        """
        Return the book if it was issued.
        
        Returns:
            bool: True if returned successfully, False otherwise
        """
        if self.status == "issued":
            self.status = "available"
            logging.info(f"✅ Book returned: {self.title} (ISBN: {self.isbn})")
            print(f"📖 '{self.title}' status changed to: AVAILABLE")
            return True
        else:
            logging.warning(f"⚠️  Book was not issued: {self.title} (ISBN: {self.isbn})")
            return False
    
    def is_available(self):
        """
        Check if the book is available.
        
        Returns:
            bool: True if available, False otherwise
        """
        return self.status == "available"