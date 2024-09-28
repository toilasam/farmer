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
        new_request_data = cls.get_infor()
        df = cls.load_request()
        df = pd.concat([df,pd.DataFrame([new_request_data])], ignore_index=True)
        cls.confirm_change(cls,df)

    @classmethod
    def update_requests():
        # df = 1
        # cls.confirm_change()
        # print('Cập nhật thông tin')
        print('Câp nhật')
        
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

    def show_late_loans():                 # hiển thị phiếu quá hạn
        print('Các đơn sách bị quá hạn:')
        # print(late_loans)

    def update_returned():                           # cập nhật phiếu đã trả
        print('Trả sách')
        

    def statistic():                                  # thống kê
        print('Chức năng thông kê.')    
        pass    

    def backup():
        print('Sao lưu')                        # sao lưu   

    # @classmethod
    # def check_date(cls):
    #     date_format = "%Y-%m-%d"
    #     while True:  
    #         s = input()
    #         try:
    #             datetime.strptime(s, date_format)
    #             break
    #         except ValueError:
    #             print('Sai định dạng mời nhập lại.')
    #         return s

    def get_infor():
        date_format = "%Y-%m-%d"
        print('Nhập thông tin:')
        while True:
            request_ID = input('Nhập mã mượn sách (7 ký tự): ')
            if len(request_ID) == 7 and ' ' not in request_ID:
                break
            else:
                print('Mã phải gồm 7 kí tự và không chứ khoảng trắng.')
        while True:
            customer_ID = input('Nhập mã khách hàng: ')
            if len(customer_ID) == 7 and ' ' not in customer_ID:
                break
            else:
                print('Mã phải gồm 7 kí tự và không chứ khoảng trắng.')   
        while True:
            book_ID = input('Nhập mã sách: ')
            if len(book_ID) == 7 and ' ' not in book_ID:
                break
            else:
                print('Mã phải gồm 7 kí tự và không chứ khoảng trắng.')

        while True:
            loan_start_date = input('Nhập ngày mượn sách định dang (yyyy-mm-dd): ')
            try:
                datetime.strptime(loan_start_date, date_format)
                break
            except ValueError:
                print('Nhập sai định dạng nhập lại')

        while True:  
            loan_end_date = input('Nhập ngày hẹn trả sách định dang (yyyy-mm-dd): ')
            try:
                datetime.strptime(loan_end_date, date_format)
                break
            except ValueError:
                print('Sai định dạng mời nhập lại.')

        return_date = ''
        while True:
            quantity = input('Nhập số lượng: ')
            try:
                quantity = int(quantity)
                break
            except ValueError:
                print('Nhập số nguyên. ')

        new_request_data = {
        'Request_ID' : request_ID,
        'Customer_ID': customer_ID,
        'Loan_start_date': loan_start_date,
        'Loan_end_date': loan_end_date,
        'Return_Date' : return_date,
        'Book_ID' : book_ID,
        'Quantity' : quantity
        }
        
        return new_request_data

#################################
      
#################################

    def confirm_change(cls, df):
        confirm = input('Xác nhận (y/n): ').lower()
        if confirm == 'y':
            cls.save_request(df), print('Thực hiện thành công.')
        elif confirm == 'n':
                print('Đã huỷ thao tác.')
        else: print('Lựa chọn không hợp lệ.')    
        
    @classmethod
    def choose_action(cls):
        while True:
            print(''' 
                1: Tạo phiếu mượn       6: Trả sách
                2: Tìm kiếm             7: Thống kê
                3: Cập nhật             8: Phiếu quá hạn
                4: Hiển thị             9: Sao lưu
                5: xoá phiếu mượn       0: Quay lại
    ''')
        
            action = input("Thao tác muốn thực hiện (0-9): ")
            if action == '1':
                cls.add_new_requests()
            elif action == '2':    
                cls.search_requests()
            elif action == '3':    
                print("Cập nhật")
            elif action == '4':     
                cls.load_request()
            elif action == '5':    
                cls.del_requests()
            elif action == '6':    
                cls.update_returned()
            elif action == '7':    
                cls.statistic()
            elif action == '8':    
                cls.show_late_loans()
            elif action == '9':    
                cls.backup()
            elif action == '0':
                break
            else:
                print('Thao tác không đúng.')
