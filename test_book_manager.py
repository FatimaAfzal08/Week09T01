import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        # Add setup for test books here
                # Add setup for test books here
        self.book1 = {'isbn':0000,'title':'Book One', 'author':'Author A'}
        self.book1 = {'isbn':0002,''title':'Book One', 'author':'Author A'}
        

    # Implement test methods here
    def test_add_and_list_books(self):
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)
        self.assertEqual(self.manager.list_book(),[self.book1,self.book2])
        
    def test_remove_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(0000)
        self.assertEqual(self.manager.list_book(),[])

    def test_remove_nonexistent_book(self):
        self.manager.add_book(self.book1)
        self.manager.remove_book(0003)
        self.assertEqual(self.manager.list_book(),[self.book1])
        

if __name__ == '__main__':
    unittest.main()
