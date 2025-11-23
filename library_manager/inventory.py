"""
Library Inventory Manager Module
Manages the collection of books in the library.
"""

import json
import logging
import os
from pathlib import Path

# Get the directory where inventory.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the project root (parent of library_manager)
project_root = os.path.dirname(current_dir)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class LibraryInventory:
    """
    Manages the library's book inventory with persistent storage.
    
    Attributes:
        books (list): List of Book objects
        data_file (Path): Path to JSON data file
    """
    
    def __init__(self, data_file=None):
        """
        Initialize the library inventory.
        
        Args:
            data_file (str): Path to JSON file for data persistence
        """
        self.books = []
        
        # Set default data file path relative to project root
        if data_file is None:
            data_dir = os.path.join(project_root, 'data')
            data_file = os.path.join(data_dir, 'books.json')
        
        self.data_file = Path(data_file)
        self._ensure_data_directory()
        self.load_from_file()
        logging.info("Library Inventory initialized")
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist."""
        try:
            # Create parent directory if it doesn't exist
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            logging.info(f"Data directory ensured: {self.data_file.parent}")
            
            # If file doesn't exist, create an empty one
            if not self.data_file.exists():
                with open(self.data_file, 'w', encoding='utf-8') as f:
                    json.dump([], f)
                logging.info(f"Created new data file: {self.data_file}")
                
        except PermissionError as e:
            logging.error(f"Permission denied creating directory: {e}")
            print(f"⚠️  Warning: Cannot create data directory. Using current directory.")
            # Fallback to current directory
            self.data_file = Path("books.json")
        except Exception as e:
            logging.error(f"Error creating data directory: {e}")
            print(f"⚠️  Warning: Error creating directory: {e}")
            self.data_file = Path("books.json")
    
    def add_book(self, title, author, isbn, status="available"):
        """
        Add a new book to the inventory.
        
        Args:
            title (str): Book title
            author (str): Book author
            isbn (str): Book ISBN
            status (str): Book status
            
        Returns:
            bool: True if added successfully, False if ISBN already exists
        """
        try:
            # Import here to avoid circular import
            from library_manager.book import Book
            
            # Check if ISBN already exists
            if self.search_by_isbn(isbn):
                logging.warning(f"Book with ISBN {isbn} already exists")
                return False
            
            book = Book(title, author, isbn, status)
            self.books.append(book)
            
            # Save immediately after adding
            if self.save_to_file():
                logging.info(f"Book added and saved successfully: {title}")
                return True
            else:
                logging.error(f"Book added but failed to save: {title}")
                return False
                
        except Exception as e:
            logging.error(f"Error adding book: {e}")
            return False
    
    def search_by_title(self, title):
        """
        Search books by title (case-insensitive, partial match).
        
        Args:
            title (str): Title to search for
            
        Returns:
            list: List of matching Book objects
        """
        try:
            results = [book for book in self.books 
                      if title.lower() in book.title.lower()]
            logging.info(f"Search by title '{title}': {len(results)} results found")
            return results
        except Exception as e:
            logging.error(f"Error searching by title: {e}")
            return []
    
    def search_by_isbn(self, isbn):
        """
        Search book by ISBN (exact match).
        
        Args:
            isbn (str): ISBN to search for
            
        Returns:
            Book: Book object if found, None otherwise
        """
        try:
            for book in self.books:
                if book.isbn == isbn:
                    logging.info(f"Book found with ISBN: {isbn}")
                    return book
            logging.info(f"No book found with ISBN: {isbn}")
            return None
        except Exception as e:
            logging.error(f"Error searching by ISBN: {e}")
            return None
    
    def display_all(self):
        """
        Display all books in the inventory.
        
        Returns:
            list: List of all Book objects
        """
        try:
            if not self.books:
                logging.info("No books in inventory")
            else:
                logging.info(f"Displaying {len(self.books)} books")
            return self.books
        except Exception as e:
            logging.error(f"Error displaying books: {e}")
            return []
    
    def save_to_file(self):
        """
        Save the current inventory to JSON file.
        
        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            # Ensure directory exists
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert books to dictionary format
            books_data = [book.to_dict() for book in self.books]
            
            # Write to file with proper encoding
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(books_data, f, indent=4, ensure_ascii=False)
            
            logging.info(f"✅ Inventory saved successfully to {self.data_file}")
            print(f"💾 Data saved to: {self.data_file}")
            return True
            
        except PermissionError as e:
            logging.error(f"❌ Permission denied writing to file: {e}")
            print(f"❌ Cannot save: Permission denied for {self.data_file}")
            return False
            
        except IOError as e:
            logging.error(f"❌ IO Error saving to file: {e}")
            print(f"❌ Cannot save: IO Error - {e}")
            return False
            
        except Exception as e:
            logging.error(f"❌ Error saving to file: {e}")
            print(f"❌ Cannot save: {e}")
            return False
            
        finally:
            logging.info("Save operation completed")
    
    def load_from_file(self):
        """Load inventory from JSON file."""
        try:
            if not self.data_file.exists():
                logging.warning(f"Data file not found: {self.data_file}. Starting with empty inventory.")
                print(f"ℹ️  No existing data file. Starting fresh.")
                return
            
            with open(self.data_file, 'r', encoding='utf-8') as f:
                books_data = json.load(f)
            
            # Import here to avoid circular import
            from library_manager.book import Book
            
            self.books = []
            for book_dict in books_data:
                book = Book(
                    book_dict['title'],
                    book_dict['author'],
                    book_dict['isbn'],
                    book_dict.get('status', 'available')
                )
                self.books.append(book)
            
            logging.info(f"✅ Loaded {len(self.books)} books from {self.data_file}")
            print(f"📚 Loaded {len(self.books)} books from storage")
        
        except json.JSONDecodeError as e:
            logging.error(f"❌ JSON decode error: {e}. Starting with empty inventory.")
            print(f"⚠️  Data file corrupted. Starting with empty inventory.")
            self.books = []
            
        except PermissionError as e:
            logging.error(f"❌ Permission denied reading file: {e}")
            print(f"❌ Cannot read data file: Permission denied")
            self.books = []
            
        except IOError as e:
            logging.error(f"❌ IO Error loading file: {e}")
            print(f"❌ Cannot read data file: IO Error")
            self.books = []
            
        except Exception as e:
            logging.error(f"❌ Error loading from file: {e}")
            print(f"❌ Error loading data: {e}")
            self.books = []
            
        finally:
            logging.info("Load operation completed")
    
    def issue_book(self, isbn):
        """
        Issue a book by ISBN.
        
        Args:
            isbn (str): ISBN of the book to issue
            
        Returns:
            bool: True if issued successfully, False otherwise
        """
        try:
            book = self.search_by_isbn(isbn)
            if book:
                if book.issue():
                    if self.save_to_file():
                        return True
                    else:
                        # Rollback status if save failed
                        book.status = "available"
                        return False
                else:
                    return False
            else:
                logging.warning(f"Book with ISBN {isbn} not found")
                return False
        except Exception as e:
            logging.error(f"Error issuing book: {e}")
            return False
    
    def return_book(self, isbn):
        """
        Return a book by ISBN.
        
        Args:
            isbn (str): ISBN of the book to return
            
        Returns:
            bool: True if returned successfully, False otherwise
        """
        try:
            book = self.search_by_isbn(isbn)
            if book:
                if book.return_book():
                    if self.save_to_file():
                        return True
                    else:
                        # Rollback status if save failed
                        book.status = "issued"
                        return False
                else:
                    return False
            else:
                logging.warning(f"Book with ISBN {isbn} not found")
                return False
        except Exception as e:
            logging.error(f"Error returning book: {e}")
            return False