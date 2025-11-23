"""
Command Line Interface for Library Inventory Manager
Main entry point for the application.
"""

import sys
import os

# IMPORTANT: Add project root to Python path
# This allows Python to find the library_manager module
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

import logging
from library_manager.inventory import LibraryInventory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('library_manager.log'),
        logging.StreamHandler()
    ]
)

class LibraryCLI:
    """Command Line Interface for Library Management System."""
    
    def __init__(self):
        """Initialize the CLI with library inventory."""
        try:
            self.inventory = LibraryInventory()
            logging.info("CLI initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing CLI: {e}")
            sys.exit(1)
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("📚 LIBRARY INVENTORY MANAGER 📚")
        print("="*50)
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        print("="*50)
    
    def get_valid_input(self, prompt, input_type=str, allow_empty=False):
        """
        Get validated input from user.
        
        Args:
            prompt (str): Input prompt message
            input_type (type): Expected input type
            allow_empty (bool): Whether to allow empty input
            
        Returns:
            Validated input value
        """
        while True:
            try:
                user_input = input(prompt).strip()
                
                if not user_input and not allow_empty:
                    print("❌ Input cannot be empty. Please try again.")
                    continue
                
                if user_input == "" and allow_empty:
                    return None
                
                if input_type == int:
                    return int(user_input)
                
                return user_input
            
            except ValueError:
                print(f"❌ Invalid input. Please enter a valid {input_type.__name__}.")
            except KeyboardInterrupt:
                print("\n\n⚠️  Operation cancelled by user.")
                return None
    
    def add_book(self):
        """Add a new book to the inventory."""
        try:
            print("\n--- ADD NEW BOOK ---")
            
            title = self.get_valid_input("Enter book title: ")
            if not title:
                return
            
            author = self.get_valid_input("Enter author name: ")
            if not author:
                return
            
            isbn = self.get_valid_input("Enter ISBN: ")
            if not isbn:
                return
            
            if self.inventory.add_book(title, author, isbn):
                print(f"✅ Book '{title}' added successfully!")
            else:
                print(f"❌ Book with ISBN {isbn} already exists!")
        
        except Exception as e:
            logging.error(f"Error in add_book: {e}")
            print(f"❌ An error occurred: {e}")
    
    def issue_book(self):
        """Issue a book from the inventory."""
        try:
            print("\n--- ISSUE BOOK ---")
            
            isbn = self.get_valid_input("Enter ISBN of the book to issue: ")
            if not isbn:
                return
            
            book = self.inventory.search_by_isbn(isbn)
            
            if not book:
                print(f"❌ No book found with ISBN: {isbn}")
                return
            
            if book.is_available():
                if self.inventory.issue_book(isbn):
                    print(f"✅ Book '{book.title}' issued successfully!")
                else:
                    print("❌ Failed to issue the book.")
            else:
                print(f"❌ Book '{book.title}' is already issued!")
        
        except Exception as e:
            logging.error(f"Error in issue_book: {e}")
            print(f"❌ An error occurred: {e}")
    
    def return_book(self):
        """Return a book to the inventory."""
        try:
            print("\n--- RETURN BOOK ---")
            
            isbn = self.get_valid_input("Enter ISBN of the book to return: ")
            if not isbn:
                return
            
            book = self.inventory.search_by_isbn(isbn)
            
            if not book:
                print(f"❌ No book found with ISBN: {isbn}")
                return
            
            if not book.is_available():
                if self.inventory.return_book(isbn):
                    print(f"✅ Book '{book.title}' returned successfully!")
                else:
                    print("❌ Failed to return the book.")
            else:
                print(f"❌ Book '{book.title}' was not issued!")
        
        except Exception as e:
            logging.error(f"Error in return_book: {e}")
            print(f"❌ An error occurred: {e}")
    
    def view_all_books(self):
        """Display all books in the inventory."""
        try:
            print("\n--- ALL BOOKS IN INVENTORY ---")
            books = self.inventory.display_all()
            
            if not books:
                print("📭 No books in the inventory.")
                return
            
            for i, book in enumerate(books, 1):
                status_icon = "✅" if book.is_available() else "🔴"
                print(f"\n{i}. {status_icon}")
                print(book)
                print("-" * 40)
        
        except Exception as e:
            logging.error(f"Error in view_all_books: {e}")
            print(f"❌ An error occurred: {e}")
    
    def search_book(self):
        """Search for books in the inventory."""
        try:
            print("\n--- SEARCH BOOK ---")
            print("1. Search by Title")
            print("2. Search by ISBN")
            
            choice = self.get_valid_input("Enter your choice (1-2): ", int)
            
            if choice == 1:
                title = self.get_valid_input("Enter title to search: ")
                if not title:
                    return
                
                results = self.inventory.search_by_title(title)
                
                if results:
                    print(f"\n✅ Found {len(results)} book(s):")
                    for i, book in enumerate(results, 1):
                        status_icon = "✅" if book.is_available() else "🔴"
                        print(f"\n{i}. {status_icon}")
                        print(book)
                        print("-" * 40)
                else:
                    print(f"❌ No books found with title containing '{title}'")
            
            elif choice == 2:
                isbn = self.get_valid_input("Enter ISBN to search: ")
                if not isbn:
                    return
                
                book = self.inventory.search_by_isbn(isbn)
                
                if book:
                    status_icon = "✅" if book.is_available() else "🔴"
                    print(f"\n✅ Book found: {status_icon}")
                    print(book)
                else:
                    print(f"❌ No book found with ISBN: {isbn}")
            
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        except Exception as e:
            logging.error(f"Error in search_book: {e}")
            print(f"❌ An error occurred: {e}")
    
    def run(self):
        """Main loop for the CLI application."""
        print("\n🎉 Welcome to Library Inventory Manager! 🎉")
        logging.info("Application started")
        
        while True:
            try:
                self.display_menu()
                choice = self.get_valid_input("Enter your choice (1-6): ", int)
                
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.issue_book()
                elif choice == 3:
                    self.return_book()
                elif choice == 4:
                    self.view_all_books()
                elif choice == 5:
                    self.search_book()
                elif choice == 6:
                    print("\n👋 Thank you for using Library Inventory Manager!")
                    print("📚 Happy Reading! 📚\n")
                    logging.info("Application closed by user")
                    break
                else:
                    print("❌ Invalid choice! Please enter a number between 1 and 6.")
            
            except KeyboardInterrupt:
                print("\n\n⚠️  Application interrupted by user.")
                logging.warning("Application interrupted")
                break
            except Exception as e:
                logging.error(f"Unexpected error in main loop: {e}")
                print(f"❌ An unexpected error occurred: {e}")


def main():
    """Entry point for the application."""
    try:
        cli = LibraryCLI()
        cli.run()
    except Exception as e:
        logging.critical(f"Critical error: {e}")
        print(f"❌ Critical error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()