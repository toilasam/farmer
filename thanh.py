class TheLoai:
    def __init__(self, ma, ten, mo_ta, do_tuoi_gioi_han, tu_khoa):
        self.ma = ma
        self.ten = ten
        self.mo_ta = mo_ta
        self.do_tuoi_gioi_han = do_tuoi_gioi_han
        self.tu_khoa = tu_khoa

    def hien_thi(self):
        print(f"Thể loại: {self.ten} (Mã: {self.ma})")
        print(f"Mô tả: {self.mo_ta}")
        print(f"Độ tuổi giới hạn: {self.do_tuoi_gioi_han}+")
        print(f"Từ khóa: {', '.join(self.tu_khoa)}")
        print("-" * 50)

danh_sach_the_loai = []

def tao_the_loai(ma, ten, mo_ta, do_tuoi_gioi_han, tu_khoa):
    if not isinstance(ma, str) or len(ma) < 3:
        print("Lỗi: Mã thể loại phải là chuỗi và có độ dài tối thiểu 3 ký tự!")
        return

    if not ten:
        print("Lỗi: Tên thể loại không được để trống!")
        return

    if not isinstance(do_tuoi_gioi_han, int) or not (16 <= do_tuoi_gioi_han <= 100):
        print("Lỗi: Độ tuổi giới hạn phải là số nguyên từ 16 đến 100!")
        return

    if len(mo_ta) < 10:
        print("Lỗi: Mô tả phải chứa ít nhất 10 ký tự!")
        return

    if not isinstance(tu_khoa, list) or len(tu_khoa) == 0:
        print("Lỗi: Từ khóa phải là danh sách không rỗng!")
        return

    the_loai_moi = TheLoai(ma, ten, mo_ta, do_tuoi_gioi_han, tu_khoa)
    danh_sach_the_loai.append(the_loai_moi)
    print(f"Thêm mới thể loại '{ten}' thành công!")

def hien_thi_cac_the_loai():
    if len(danh_sach_the_loai) == 0:
        print("Thư viện hiện chưa có thể loại nào.")
    else:
        print("\nDanh sách các thể loại trong thư viện:")
        print("-" * 50)
        for the_loai in danh_sach_the_loai:
            the_loai.hien_thi()

def tim_kiem_the_loai(ma):
    for the_loai in danh_sach_the_loai:
        if the_loai.ma == ma:
            print("\nKết quả tìm kiếm:")
            the_loai.hien_thi()
            return
    print(f"Không tìm thấy thể loại với mã '{ma}'.")

def cap_nhat_mo_ta(ma, mo_ta_moi):
    for the_loai in danh_sach_the_loai:
        if the_loai.ma == ma:
            if len(mo_ta_moi) < 10:
                print("Lỗi: Mô tả phải chứa ít nhất 10 ký tự!")
            else:
                the_loai.mo_ta = mo_ta_moi
                print(f"Mô tả thể loại '{the_loai.ten}' đã được cập nhật!")
            return
    print(f"Không tìm thấy thể loại với mã '{ma}'.")

def xoa_the_loai(ma):
    for the_loai in danh_sach_the_loai:
        if the_loai.ma == ma:
            danh_sach_the_loai.remove(the_loai)
            print(f"Đã xóa thể loại với mã '{ma}'.")
            return
    print(f"Không tìm thấy thể loại với mã '{ma}'.")

def loc_the_loai_theo_do_tuoi(do_tuoi_gioi_han):
    print(f"\nDanh sách các thể loại cho độ tuổi giới hạn từ {do_tuoi_gioi_han}+ trở lên:")
    print("-" * 50)
    dem = 0
    for the_loai in danh_sach_the_loai:
        if the_loai.do_tuoi_gioi_han >= do_tuoi_gioi_han:
            the_loai.hien_thi()
            dem += 1
    if dem == 0:
        print(f"Không tìm thấy thể loại nào với độ tuổi giới hạn từ {do_tuoi_gioi_han}+ trở lên.")

def loc_the_loai_theo_tu_khoa(tu_khoa):
    print(f"\nDanh sách các thể loại chứa từ khóa '{tu_khoa}':")
    print("-" * 50)
    dem = 0
    for the_loai in danh_sach_the_loai:
        if tu_khoa in the_loai.tu_khoa:
            the_loai.hien_thi()
            dem += 1
    if dem == 0:
        print(f"Không tìm thấy thể loại nào chứa từ khóa '{tu_khoa}'.")


def menu_quan_ly():
    while True:
        print("\n--- Quản Lý Thư Viện ---")
        print("1. Thêm thể loại mới")
        print("2. Hiển thị tất cả các thể loại")
        print("3. Tìm kiếm thể loại theo mã")
        print("4. Cập nhật mô tả thể loại theo mã")
        print("5. Xóa thể loại theo mã")
        print("6. Lọc thể loại theo độ tuổi giới hạn")
        print("7. Lọc thể loại theo từ khóa")
        print("8. Thoát chương trình")
        
        lua_chon = input("Nhập lựa chọn của bạn (1-8): ")

        if lua_chon == "1":
            ma = input("Nhập mã thể loại: ")
            ten = input("Nhập tên thể loại: ")
            mo_ta = input("Nhập mô tả thể loại: ")
            do_tuoi_gioi_han = int(input("Nhập độ tuổi giới hạn: "))
            tu_khoa = input("Nhập danh sách từ khóa (phân cách bằng dấu phẩy): ").split(',')
            tu_khoa = [tk.strip() for tk in tu_khoa]
            tao_the_loai(ma, ten, mo_ta, do_tuoi_gioi_han, tu_khoa)

        elif lua_chon == "2":
            hien_thi_cac_the_loai()

        elif lua_chon == "3":
            ma = input("Nhập mã thể loại cần tìm: ")
            tim_kiem_the_loai(ma)

        elif lua_chon == "4":
            ma = input("Nhập mã thể loại cần cập nhật: ")
            mo_ta_moi = input("Nhập mô tả mới: ")
            cap_nhat_mo_ta(ma, mo_ta_moi)

        elif lua_chon == "5":
            ma = input("Nhập mã thể loại cần xóa: ")
            xoa_the_loai(ma)

        elif lua_chon == "6":
            do_tuoi_gioi_han = int(input("Nhập độ tuổi giới hạn để lọc: "))
            loc_the_loai_theo_do_tuoi(do_tuoi_gioi_han)

        elif lua_chon == "7":
            tu_khoa = input("Nhập từ khóa để lọc: ")
            loc_the_loai_theo_tu_khoa(tu_khoa)

        elif lua_chon == "8":
            print("Thoát chương trình. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

