import pandas as pd
from datetime import datetime
import panel as pn
import matplotlib.pyplot as plt
pn.extension()

# class Book_loan_requests:
#     def __init__(self, request_ID, customer_ID, loan_start_date, loan_end_date, return_date, book_ID, quantity):
#         self.request_ID = request_ID
#         self.customer_ID = customer_ID
#         self.loan_start_date = loan_start_date
#         self.loan_end_date = loan_end_date
#         self.return_date = return_date
#         self.book_ID = book_ID
#         self.quantity = quantity

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
    def update_requests(cls):
        print('Câp nhật')
        df = cls.load_request()
        while True:
            request_id_ud = input('Nhập mã sách muốn cập nhật: ')
            if request_id_ud in list(df['Request_ID']):
                break
            else:
                print('Mã mượn sách không tồn tại.')
        print(f'Nhập thông tin cho mã đơn {request_id_ud}')
        customer_id_ud = input('Nhâp mã khách hàng: ')
        loan_start_date_ud = input('Nhập ngày mượn sách: ')
        loan_end_date_ud = input('Nhập ngày phải trả sách: ')
        book_id_ud = input('Nhập mã sách: ')
        while True:
            quantity_ud = input('Nhập số lượng sách mượn: ')
            try:
                quantity_ud = int(quantity_ud)
                if quantity_ud < 0:
                    print('Số lượng phải lớn hơn 0.')
                else:
                    break
            except ValueError:
                print('Số lượng phải là số nguyên: ')

        df.loc[df['Request_ID'] == request_id_ud, ['Customer_ID', 'Loan_start_date', 'Loan_end_date', 'Book_ID', 'Quantity']] = customer_id_ud, loan_start_date_ud, loan_end_date_ud, book_id_ud, quantity_ud

        cls.confirm_change()

    @classmethod
    def show_requests(cls):
        df = cls.load_request()
        df50  = df.tail(50)
        print(df50)

    @classmethod    
    def search_requests(cls):
        print('Tìm kiếm')
        info_search = input('Nhập mã đơn hoặc mã khách hàng: ')
        df = cls.load_request()
        dfrq = df[df['Request_ID'] == info_search]
        dfc = df[df['Customer_ID'] == info_search]
        df = pd.concat([dfrq, dfc], axis=0)
        return df

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

    @classmethod
    def show_late_loans(cls):                 # hiển thị phiếu quá hạn
        print('Các đơn sách bị quá hạn:')
        print(cls.check_loans())

    @classmethod
    def update_returned(cls):                          # cập nhật phiếu đã trả
        print('Trả sách')
        date = datetime.today().strftime("%m/%d/%Y")
        df = cls.load_request()
        lr_ID = input('Nhập mã phiếu muốn trả: ')
        df.loc[df['Request_ID'] == lr_ID, 'Return_date'] =  date
        cls.confirm_change(cls, df)
        

    @classmethod                  #"%m/%d/%Y"                
    def statistic(cls):
        print('Chức năng thống kê.')                  
        df = cls.load_request()

        df['Loan_start_date'] = pd.to_datetime(df['Loan_start_date'], format="%m/%d/%Y", errors='coerce')

        total_request = df['Request_ID'].count()
        print(f'Tổng số đơn mượn sách: {total_request}')
        total_book = df['Quantity'].sum()
        print(f'Tổng số sách được mượn: {total_book}')
        
        df_group = df.groupby('Loan_start_date').size()

        plt.figure(figsize=(10, 6))
        plt.plot(df_group.index, df_group, marker='o', linestyle='-', color='b')

        plt.title('Số đơn mượn sách', fontsize=16)
        plt.xlabel('Ngày', fontsize=12)
        plt.ylabel('Số lượng', fontsize=12)
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()



    @classmethod
    def backup(cls): 
        file_path_backup = "book_loan_requests_backup.xlsx"
        df = cls.load_request()
        while True:
            confirm = input('Xác nhận (y/n): ').lower()
            if confirm == 'y':
                df.to_excel(file_path_backup, index = False)
                print('Thao tác thành công.')
                break
            elif confirm == 'n':
                print('Đã huỷ thao tác.')
                break
            else: print('Lựa chọn không hợp lệ. Chọn lại.')      

                               

    def confirm_change(cls, df):
        while True:
            confirm = input('Xác nhận (y/n): ').lower()
            if confirm == 'y':
                cls.save_request(df), print('Thao tác thành công.')
                break
            elif confirm == 'n':
                print('Đã huỷ thao tác.')
                break
            else: print('Lựa chọn không hợp lệ. Chọn lại.')  

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
    #      return s

    def get_infor():
        date_format = "%m/%d/%Y"
        print('Nhập thông tin:')
        while True:
            request_ID = input('Nhập mã mượn sách (7 ký tự): ')
            if len(request_ID) == 7 and ' ' not in request_ID:
                break
            else:
                print('Mã phải gồm 7 kí tự và không chứa khoảng trắng.')
        while True:
            customer_ID = input('Nhập mã khách hàng: ')
            if len(customer_ID) == 7 and ' ' not in customer_ID:
                break
            else:
                print('Mã phải gồm 7 kí tự và không chứa khoảng trắng.')   
        while True:
            book_ID = input('Nhập mã sách: ')
            if len(book_ID) == 7 and ' ' not in book_ID:
                break
            else:
                print('Mã phải gồm 7 kí tự và không chứa khoảng trắng.')

        while True:
            loan_start_date = input('Nhập ngày mượn sách định dang (mm/dd/yyyy): ')
            try:
                datetime.strptime(loan_start_date, date_format)
                break
            except ValueError:
                print('Nhập sai định dạng nhập lại')

        while True:  
            loan_end_date = input('Nhập ngày hẹn trả sách định dang (mm/dd/yyyy): ')
            try:
                datetime.strptime(loan_end_date, date_format)
                break
            except ValueError:
                print('Sai định dạng mời nhập lại.')

        return_date = ''
        while True:
            quantity = input('Nhập số lượng sách mượn: ')
            try:
                qu = int(quantity)
                if quantity < 0:
                    print('Số lượng phải lớn hơn 0.')
                else:
                    break
            except ValueError:
                print('Số lượng phải là số nguyên: ')

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
        
    @classmethod
    def choose_action(cls):
        while True:
            print(''' 
                1: Tạo phiếu mượn       6: Trả sách
                2: Tìm kiếm             7: Thống kê
                3: Cập nhật             8: Phiếu quá hạn
                4: Hiển thị             9: Sao lưu
                5: Xoá phiếu mượn       0: Quay lại
    ''')
    # 2
        
            action = input("Thao tác muốn thực hiện (0-9): ")
            if action == '1':
                cls.add_new_requests()
            elif action == '2':    
                print(cls.search_requests())
            elif action == '3':    
                cls.update_requests()
            elif action == '4':     
                print('Hien thi')
                cls.show_requests()
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
                print('Thao tác sai.')
