import pandas as pd
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
    def load_request(cls):
        try:
            return pd.read_excel(cls.file_path)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Request_ID','Customer_ID','Loan_start_date','Loan_end_date','Return_Date','Book_ID','Quantity'])
    def save_request(cls, df):
        df.to_excel(cls.file_path, index = False)
        
    def add_new_requests(cls, new_request_data):
        df = cls.load_request()
        df = pd.concat([df,pd.DataFrame([new_request_data])], ignore_index=True)
        cls.save_request(df)
        print('Tạo phiếu mượn sách thành công.')

    @classmethod
    def update_requests():
        print('Thay doi')

    @classmethod
    def show_requests():
        print('Hien thi')

    @classmethod    
    def seach_requests():
        print('Tim Kiem')
        
    @classmethod
    def del_requests():
        print('Xoa')

    def choose_action():
        request_manager = Request_manager()
        action = input("Nhập hành động (add, update, show, search, delete): ")
        if action == 'add':
            print('Nhập thông tin:')
            request_ID = input('Nhập mã mượn sách: ')
            customer_ID = input('Nhap mã khách hàng: ')
            loan_start_date = input('Nhâp ngày mượn sách: ')
            loan_end_date = input('Nhâp ngày hẹn trả sách: ')
            return_date = input('Nhập ngày trả sách: ')
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
        request_manager.add_new_requests(new_request_data)
        if action == 'delete':
            request_manager.del_requests()