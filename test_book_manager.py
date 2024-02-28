import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        # Add setup for test books here
                # Add setup for test books here
        self.book1 = {'isbn':1234,'title':'Book One', 'author':'Author A'}
        self.book2 = {'isbn':1345,'title':'Book One', 'author':'Author A'}
        

    # Implement test methods here
    def test_add_and_list_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(self.manager.list_books(),[self.book1,self.book2])
        
    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(1234)
        self.assertEqual(self.manager.list_books(),[])

    def test_remove_nonexistent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(1254)
        self.assertEqual(self.manager.list_books(),[self.book1])
        

if __name__ == '__main__':
    unittest.main()
