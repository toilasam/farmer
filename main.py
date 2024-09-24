
from books import Books
from book_loan_requests import Book_loan_requests, Request_manager
from categories import Categories
from customers import Customers
from publishers import Publishers

class_library = {
    "1": Books,
    "2": Book_loan_requests,
    "3": Categories,
    "4": Customers,
    "5": Publishers
}

if __name__ == "__main__":
    while True:
        print('-----------Chương Trình Quản Lý Thư Viện------------')
        print(''' 
            1: Books          4: Customers
            2: Requests       5: Publishers
            3: Categories  ''')
        user_input = input("Nhập mã đối tượng muốn tương tác ('exit' để thoát): ")
        if user_input == 'exit':
            print("Bye")
            break

        if user_input in class_library:
            if user_input == '1': #### ví dụ nhập 1 để tương tác với đối tượng sách:
                print('Books')
                pass
            if user_input == '2':#### ví dụ nhập 2 để tương tác với đối tượng phiếu mượn sách:
                print('Requests')
                Request_manager.choose_action()
            ##### mọi người điền tiếp ÌF để tương tác với phần bài của mọi người dưới đây ####

        else:
            print("Đối tượng không tồn tại. Vui lòng thử lại.")

    print('Thoát chương trình.')
