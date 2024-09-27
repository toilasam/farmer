from books import *
from book_loan_requests import Request_manager

from publishers import *
from confirm import confirm_exit
from Doc_gia import *


class_library = {
    "1": 'books',
    "2": 'requests',
    "3": 'categories',
    "4": 'customers',
    "5": 'publishers'
}

if __name__ == "__main__":
    ds_doc_gia = []  # Khởi tạo danh sách độc giả
    # Bạn có thể khởi tạo một số độc giả mẫu nếu cần
    doc_gia1 = DocGia(ma='001', ten='John Doe', email='john@example.com', sdt='123456789')
    ds_doc_gia.append(doc_gia1)


    while True:
        print('-------------Chương Trình Quản Lý Thư Viện------------')
        Request_manager.notifications_late_loans(Request_manager.check_loans())
        print(''' 
            1: Sách             4: Độc giả
            2: Phiếu mượn       5: Nhà xuất bản
            3: Thể loại  ''')
        user_input = input("Nhập mã đối tượng muốn tương tác ('q' để thoát): ").strip().lower()
        if user_input == 'q':
            confirm_exit()
            
        elif user_input in class_library: # or user_input in list(class_library.values()): 
            if user_input == '1' or user_input == 'books': 
                print('Sách')
                Book_manager.choose_action()
            elif user_input == '2' or user_input == 'requests':
                print('Phiếu mượn')
                Request_manager.choose_action()
            elif user_input == '3': 
                cate.menu_quan_ly()
                # pass
            elif user_input == '4':
                doc_gia = DocGia(ma='001', ten='John Doe', email='john@example.com', sdt='123456789')
                doc_gia.chon_chuc_nang(ds_doc_gia)  # Gọi phương thức từ đối tượng và truyền ds_doc_gia
            elif user_input == '5':
                Publishers.menu()
        else:
            print("Đối tượng không tồn tại. Vui lòng chọn lại.")

