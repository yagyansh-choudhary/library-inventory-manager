# 📚 Library Inventory Manager

A comprehensive command-line based library management system built with Python, demonstrating Object-Oriented Programming principles, robust file handling, and user-friendly CLI interface.

## 🎯 Project Overview

This project is a library inventory management system that allows library staff to:
- Track book status (available/issued)
- Add new books to the catalog
- Issue and return books
- Search books by title or ISBN
- Maintain persistent records using JSON storage

## ✨ Features

- **📖 Book Management**: Add, issue, and return books with ease
- **🔍 Smart Search**: Search by title (partial match) or ISBN (exact match)
- **💾 Persistent Storage**: All data saved in JSON format
- **🛡️ Error Handling**: Comprehensive exception handling and logging
- **📊 Logging System**: Track all operations with Python's logging module
- **🎨 User-Friendly CLI**: Interactive menu-driven interface
- **✅ Input Validation**: Robust input validation for all operations
- **🧪 Unit Tests**: Comprehensive test coverage using unittest

## 📁 Project Structure

```
library-inventory-manager-yourname/
│
├── library_manager/          # Main package directory
│   ├── __init__.py           # Package initialization
│   ├── book.py               # Book class definition
│   └── inventory.py          # LibraryInventory class
│
├── cli/                      # Command line interface
│   └── main.py               # CLI application entry point
│
├── data/                     # Data storage directory
│   └── books.json            # JSON file for book data (auto-generated)
│
├── tests/                    # Unit tests directory
│   ├── __init__.py
│   └── test_book.py          # Tests for Book class
│
├── README.md                 # Project documentation (this file)
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── library_manager.log      # Application log file (auto-generated)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/library-inventory-manager-yourname.git
cd library-inventory-manager
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python cli/main.py
```

## 💻 Usage

### Main Menu Options

When you run the application, you'll see the following menu:

```
📚 LIBRARY INVENTORY MANAGER 📚
==================================================
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit
==================================================
```

### 1️⃣ Add Book
- Enter book title, author name, and ISBN
- System validates that ISBN is unique
- Book is automatically marked as "available"

### 2️⃣ Issue Book
- Enter ISBN of the book to issue
- System checks if book exists and is available
- Updates book status to "issued"

### 3️⃣ Return Book
- Enter ISBN of the book to return
- System checks if book was previously issued
- Updates book status to "available"

### 4️⃣ View All Books
- Displays all books in the inventory
- Shows title, author, ISBN, and status
- Visual indicators: ✅ (available) 🔴 (issued)

### 5️⃣ Search Book
- **Search by Title**: Partial match, case-insensitive
- **Search by ISBN**: Exact match
- Returns matching books with full details

### 6️⃣ Exit
- Safely closes the application
- All data is automatically saved

## 🎓 OOP Principles Applied

### Encapsulation
- Private methods (e.g., `_ensure_data_directory()`)
- Attributes protected within classes
- Clean public interfaces

### Inheritance
- Extensible class structure
- Ready for future enhancements (e.g., specialized book types)

### Magic Methods
- `__init__()`: Constructor for object initialization
- `__str__()`: Human-readable string representation
- Custom methods: `to_dict()`, `is_available()`

## 🛠️ Technical Details

### File Handling
- **JSON Storage**: Uses `json` module for serialization
- **Path Management**: `pathlib.Path` for cross-platform compatibility
- **Error Handling**: Try-except blocks for file operations
- **Auto-creation**: Data directory created automatically if missing

### Exception Handling
- File I/O exceptions (IOError, FileNotFoundError)
- JSON parsing errors (JSONDecodeError)
- User input validation
- Graceful error messages

### Logging
- Log levels: INFO, WARNING, ERROR, CRITICAL
- Dual output: Console and file (`library_manager.log`)
- Timestamp and level information in each log entry
- Tracks all major operations and errors

## 🧪 Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_book

# Run with verbose output
python -m unittest tests.test_book -v
```

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:
- No external dependencies required (uses Python standard library)
- pathlib (built-in)
- json (built-in)
- logging (built-in)
- unittest (built-in)

## 🔒 Data Persistence

- Books are stored in `data/books.json`
- JSON format for human-readable storage
- Automatic save after every modification
- Load on application startup

**Example JSON structure:**
```json
[
    {
        "title": "Python Programming",
        "author": "John Doe",
        "isbn": "978-0-123456-78-9",
        "status": "available"
    },
    {
        "title": "Data Structures",
        "author": "Jane Smith",
        "isbn": "978-1-234567-89-0",
        "status": "issued"
    }
]
```

## 🤝 Contributing

This is an academic project. If you'd like to suggest improvements:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 Learning Outcomes

This project demonstrates:
- ✅ Class-based design with attributes and methods
- ✅ OOP principles: encapsulation, inheritance, magic methods
- ✅ File I/O with JSON and pathlib
- ✅ Exception handling with try-except-finally
- ✅ Modular code with reusable functions
- ✅ CLI development with input validation
- ✅ Python logging module implementation
- ✅ Unit testing with unittest framework
- ✅ Project packaging and documentation

## 📧 Contact

**Developer**: Yagyansh Singh Ahlawat  
**Email**: 2501010120@krmu.edu.in 
**GitHub**: [yagyansh-choudhary](https://github.com/yagyansh-choudhary)

**Course**: Programming for Problem Solving using Python  
**Institution**: K.R MANGALAM UNIVERSITY

## 📄 License

This project is created for educational purposes as part of a programming course assignment.

## 🙏 Acknowledgments

- Course Instructor: jyoti.yadav@krmangalam.edu.in
- Python Documentation
- Stack Overflow Community

---

**Note**: This project follows PEP 8 style guidelines and best practices for Python development.

Made with ❤️ for learning Python programming!
