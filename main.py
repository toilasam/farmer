
from books import *
from book_loan_requests import Request_manager
from categories import *
from customers import *
from publishers import *
from confirm import confirm_exit

class_library = {
    "1": 'books',
    "2": 'requests',
    "3": 'categories',
    "4": 'customers',
    "5": 'publishers'
}

if __name__ == "__main__":
    while True:
        print('-------------Chương Trình Quản Lý Thư Viện------------')
        Request_manager.notifications_late_loans(Request_manager.check_loans())
        print(''' 
            1: Books          4: Customers
            2: Requests       5: Publishers
            3: Categories  ''')
        user_input = input("Nhập mã đối tượng muốn tương tác ('q' để thoát): ").strip().lower()
        if user_input == 'q':
            confirm_exit()
            
        elif user_input in class_library or user_input in list(class_library.values()): 
            if user_input == '1' or user_input == 'books': 
                print('Books')
                Book_manager.choose_action()
            elif user_input == '2' or user_input == 'requests':
                print('Requests')
                Request_manager.choose_action()
            elif user_input == '3': 
                pass
            elif user_input == '4':
                pass
            elif user_input == '5':
                Publishers.menu()
                pass
        else:
            print("Đối tượng không tồn tại. Vui lòng chọn lại.")

