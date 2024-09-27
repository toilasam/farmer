from datetime import datetime

class DocGia:
    def __init__(self, ma, ten, email, sdt, ngay_dang_ki=None):
        self.ma = ma 
        self.ten = ten 
        self.email = email 
        self.sdt = sdt 
        if ngay_dang_ki is None:
            self.ngay_dang_ki = datetime.now()
        else:
            self.ngay_dang_ki = ngay_dang_ki

    def hien_thi_thong_tin(self):
        print(f"Mã độc giả: {self.ma}")
        print(f"Tên độc giả: {self.ten}")
        print(f"Email: {self.email}")
        print(f"Số điện thoại: {self.sdt}")
        print(f"Ngày đăng ký: {self.ngay_dang_ki.strftime('%Y-%m-%d')}")

    def them_doc_gia(self, ds_doc_gia, doc_gia):
        ds_doc_gia.append(doc_gia)
        print(f"Đã thêm độc giả: {doc_gia.ten}")

    def tim_kiem_doc_gia(self, ds_doc_gia, ma=None, ten=None):
        ket_qua = []
        for doc_gia in ds_doc_gia: 
            if (ma and doc_gia.ma == ma) or (ten and doc_gia.ten.lower() == ten.lower()):
                ket_qua.append(doc_gia)
        return ket_qua 

    def hien_thi_danh_sach_doc_gia(self, ds_doc_gia):
        for doc_gia in ds_doc_gia:
            doc_gia.hien_thi_thong_tin()

    def cap_nhat_doc_gia(self, doc_gia, ten=None, email=None, ma=None):
        if ten:
            doc_gia.ten = ten 
        if email:
            doc_gia.email = email 
        if ma:
            doc_gia.ma = ma 
        print(f"Đã cập nhật thông tin độc giả: {doc_gia.ten}")

    def chon_chuc_nang(self, ds_doc_gia):  # Thêm tham số ds_doc_gia
        menu = {
            1: 'hien_thi_thong_tin',
            2: 'them_doc_gia',
            3: 'tim_kiem_doc_gia',
            4: 'hien_thi_danh_sach_doc_gia',
            5: 'cap_nhat_doc_gia'
        }
        while True:
            print("\nChọn một chức năng:")
            for key, value in menu.items():
                print(f"{key}. {value.replace('_', ' ').capitalize()}")

            lua_chon = int(input("Nhập lựa chọn của bạn: "))

            if lua_chon in menu:
                # Gọi phương thức tương ứng từ đối tượng và truyền ds_doc_gia vào
                if lua_chon in [2, 3, 4, 5]:
                    if lua_chon == 2:  # Thêm độc giả
                        ma = input("Nhập mã độc giả: ")
                        ten = input("Nhập tên độc giả: ")
                        email = input("Nhập email: ")
                        sdt = input("Nhập số điện thoại: ")
                        doc_gia_moi = DocGia(ma, ten, email, sdt)
                        self.them_doc_gia(ds_doc_gia, doc_gia_moi)
                    elif lua_chon == 3:  # Tìm kiếm độc giả
                        ma = input("Nhập mã độc giả (hoặc để trống để tìm theo tên): ")
                        ten = input("Nhập tên độc giả (hoặc để trống để tìm theo mã): ")
                        ket_qua = self.tim_kiem_doc_gia(ds_doc_gia, ma=ma, ten=ten)
                        for doc_gia in ket_qua:
                            doc_gia.hien_thi_thong_tin()
                    elif lua_chon == 4:  # Hiện thị danh sách độc giả
                        self.hien_thi_danh_sach_doc_gia(ds_doc_gia)
                    elif lua_chon == 5:  # Cập nhật độc giả
                        ma = input("Nhập mã độc giả cần cập nhật: ")
                        doc_gia = self.tim_kiem_doc_gia(ds_doc_gia, ma=ma)
                        if doc_gia:
                            doc_gia = doc_gia[0]
                            ten = input("Nhập tên mới (để trống nếu không muốn thay đổi): ")
                            email = input("Nhập email mới (để trống nếu không muốn thay đổi): ")
                            self.cap_nhat_doc_gia(doc_gia, ten=ten, email=email)
                        else:
                            print("Không tìm thấy độc giả.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Đảm bảo thêm điều kiện này
if __name__ == "__main__":
    ds_doc_gia = []  # Khởi tạo danh sách độc giả
    doc_gia = DocGia(ma='001', ten='John Doe', email='john@example.com', sdt='123456789')
    ds_doc_gia.append(doc_gia)  # Thêm độc giả vào danh sách
    doc_gia.chon_chuc_nang(ds_doc_gia)  # Gọi phương thức chọn chức năng từ đối tượng 

