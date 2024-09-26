import pandas as pd
from datetime import datetime

class Book_loan_requests:
    def __init__(self, request_ID, customer_ID, loan_start_date, loan_end_date, return_date, book_ID, quantity):
        self.request_ID = request_ID
        self.customer_ID = customer_ID
        self.loan_start_date = loan_start_date
        self.loan_end_date = loan_end_date
        self.return_date = return_date
        self.book_ID = book_ID
        self.quantity = quantity

class Request_manager:
    file_path = 'book_loan_requests.xlsx'
    
    @classmethod
    def load_request(cls):
        try:
            return pd.read_excel(cls.file_path)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Request_ID','Customer_ID','Loan_start_date','Loan_end_date','Return_Date','Book_ID','Quantity'])
    @classmethod
    def save_request(cls, df):
        df.to_excel(cls.file_path, index = False)

    @classmethod    
    def add_new_requests(cls):
        print('Nhập thông tin:')
        request_ID = input('Nhập mã mượn sách: ')
        customer_ID = input('Nhap mã khách hàng: ')
        loan_start_date = input('Nhâp ngày mượn sách: ')
        loan_end_date = input('Nhâp ngày hẹn trả sách: ')
        #return_date = input('Nhập ngày trả sách: ')
        return_date = ''
        book_ID = input('Nhập mã sách: ')
        quantity = int(input('Nhập số lượng: '))

        new_request_data = {
        'Request_ID' : request_ID,
        'Customer_ID': customer_ID,
        'Loan_start_date': loan_start_date,
        'Loan_end_date': loan_end_date,
        'Return_Date' : return_date,
        'Book_ID' : book_ID,
        'Quantity' : quantity
        }

        # cls.add_new_requests(new_request_data)
        df = cls.load_request()
        df = pd.concat([df,pd.DataFrame([new_request_data])], ignore_index=True)
        cls.confirm_change(cls,df)

    @classmethod
    def update_requests(cls):
        df = 1
        cls.confirm_change()
        print('Cập nhật thông tin')
        

    @classmethod
    def show_requests():
        print('Hien thi')

    @classmethod    
    def search_requests(cls):
        print('Tìm kiếm')
        info_search = input('Nhập thông tin cần tìm: ')
        df = cls.load_request()

    @classmethod
    def del_requests(cls):
        print('Xoá phiếu mượn sách')
        ID_del_request = input('Nhập vào mã mượn sách: ')
        df = cls.load_request()
        if ID_del_request in df['Request_ID'].values:
            df = df[df['Request_ID'] != ID_del_request]
            cls.confirm_change(cls, df)
        else:
            print('Mã phiếu mượn không tồn tại.')
            
    @classmethod
    def check_loans(cls):
        today = datetime.now()
        df = cls.load_request()
        df['Loan_end_date'] = pd.to_datetime(df['Loan_end_date'], errors = 'coerce')

        late_loans = df[df['Loan_end_date'] < today]
        return late_loans
    
    @classmethod
    def notifications_late_loans(cls, late_loans):   # thông báo phiếu quá bạn
        if not late_loans.empty:
            print('Có đơn sách quá hạn.')
        else:
            print('Have a nice day.')

    def show_late_loans(late_loans):            # hiển thị phiếu quá hạn
        print('Các đơn sách bị quá hạn:')
        print(late_loans)

    def update_returned():                      # cập nhật phiếu đã trả
        pass

    def statistic():                            # thống kê
        pass    

# sao lưu


    def confirm_change(cls, df):
        confirm = input('Xác nhận (y/n): ').lower()
        if confirm == 'y':
            cls.save_request(df), print('Thực hiện thành công.')
        elif confirm == 'n':
                print('Đã huỷ thao tác.')
        else: print('Lựa chọn không hợp lệ.')    
        

    @classmethod
    def choose_action(cls):
        # request_manager = Request_manager()
        action = input("Nhập hành động (add, update, show, search, delete): ")
        if action == 'add':         #1
            cls.add_new_requests()  
        elif action == 'delete':    #2 
            cls.del_requests()
        elif action == 'update':    #3
            pass
        elif action == 'show':      #4
            pass
        elif action == 'search':    #5
            pass
        
