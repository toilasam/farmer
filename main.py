
from books import Books, Book_manager
from book_loan_requests import Book_loan_requests, Request_manager
from categories import Categories
from customers import Customers
from publishers import Publishers

class_library = {
    "books": Books,
    "requests": Book_loan_requests,
    "categories": Categories,
    "customers": Customers,
    "publishers": Publishers
}
book_manager = Book_manager()

if __name__ == "__main__":
    while True:
        user_input = input("Nhập tên đối tượng muốn tương tác (hoặc 'exit' để thoát): ")
        if user_input == 'exit':
            print("Bye")
            break

        if user_input in class_library:
            if user_input == 'books':
                Book_manager.choose_action()
            if user_input == 'requests':
                Request_manager.choose_action()
        else:
            print("Đối tượng không tồn tại. Vui lòng thử lại.")
    print('Thoát chương trình.')
