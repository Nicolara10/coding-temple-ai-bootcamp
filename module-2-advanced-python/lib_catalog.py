
# Library Catalog
# Module 2: Advanced Python & Data Handling
 
 
class Book:
    """Represents a single physical book."""
 
    def __init__(self, title, author, year):
        # Validate year before saving anything
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")
 
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False   # every book starts on the shelf
 
    def check_out(self):
        """Check out the book. Returns True if it worked."""
        if self.checked_out:
            return False           # someone already has it
        self.checked_out = True
        return True
 
    def return_book(self):
        """Return the book. Returns True if it worked."""
        if not self.checked_out:
            return False           # it wasn't checked out
        self.checked_out = False
        return True
 
    def __repr__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"'{self.title}' by {self.author} ({self.year}) [{status}]"
 
 
class EBook(Book):
    """An ebook. Many people can borrow it at the same time."""
 
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)   # run Book's setup (and validation)
        self.file_size_mb = file_size_mb
        self.checkout_count = 0                 # how many people have it right now
 
    def check_out(self):
        """Ebooks never run out, so checking out always works."""
        self.checkout_count += 1
        return True
 
    def return_book(self):
        """Return one copy. Returns True if it worked."""
        if self.checkout_count == 0:
            return False
        self.checkout_count -= 1
        return True
 
    def __repr__(self):
        return (f"'{self.title}' by {self.author} ({self.year}) "
                f"[EBook, {self.file_size_mb} MB, {self.checkout_count} checked out]")
 
 
class Catalog:
    """Manages a collection of books."""
 
    def __init__(self):
        self.books = []
 
    def add_book(self, book):
        """Add a Book or EBook to the catalog."""
        self.books.append(book)
 
    def search_by_author(self, author):
        """Return all books by this author (not case sensitive)."""
        return [b for b in self.books if b.author.lower() == author.lower()]
 
    def search_by_title(self, keyword):
        """Return books whose title contains the keyword (not case sensitive)."""
        return [b for b in self.books if keyword.lower() in b.title.lower()]
 
    def get_available(self):
        """Return all books that can be checked out right now."""
        return [b for b in self.books if not b.checked_out]
 
    def summary(self):
        """Print an overview of the catalog."""
        available = len(self.get_available())
        print(f"\nCatalog Summary: {available}/{len(self.books)} available")
        for book in self.books:
            print(f"  {book}")
 
 
# ============================================================
# Test code from the assignment
# ============================================================
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))
 
# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"
 
# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")
 
catalog.summary()
 
 