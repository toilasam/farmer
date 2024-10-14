class Publishers:
    Publishers = []

    @classmethod
    def hien_thi_danh_sach(cls):
        if len(cls.Publishers) == 0:
            print("Danh sách nhà xuất bản trống.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SDT':<10}")
            print("-" * 95)
            for nxb in cls.Publishers:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    @classmethod
    def tim_kiem_theo_ma(cls):
        ma = input("Mời bạn nhập mã nhà xuất bản để tìm: ").lower()
        ket_qua = [nxb for nxb in cls.Publishers if ma in nxb['ma'].lower()]

        if len(ket_qua) == 0:
            print("Không tìm thấy nhà xuất bản nào với mã này.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SĐT':<10}")
            print("-" * 95)
            for nxb in ket_qua:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    @classmethod
    def tim_kiem_theo_ten(cls):
        ten = input("Mời bạn nhập tên nhà xuất bản để tìm: ").lower()
        ket_qua = [nxb for nxb in cls.Publishers if ten in nxb['ten'].lower()]

        if len(ket_qua) == 0:
            print("Không tìm thấy nhà xuất bản nào với tên này.")
        else:
            print(f"{'Mã':<5}{'Tên':<20}{'Địa chỉ':<30}{'Email':<30}{'SĐT':<10}")
            print("-" * 95)
            for nxb in ket_qua:
                print(f"{nxb['ma']:<5}{nxb['ten']:<20}{nxb['dia_chi']:<30}{nxb['email']:<30}{nxb['sdt']:<10}")

    @classmethod
    def them_moi(cls):
        ma = input("Nhập mã nhà xuất bản: ")
        ten = input("Nhập tên nhà xuất bản: ")
        dia_chi = input("Nhập địa chỉ: ")
        email = input("Nhập Email: ")
        sdt = input("Nhập số điện thoại: ")
        # Thêm thông tin mới vào danh sách Publishers
        cls.Publishers.append({'ma': ma, 'ten': ten, 'dia_chi': dia_chi, 'email': email, 'sdt': sdt})
        print("Cập nhật thông tin Nhà Xuất Bản thành công.")

    @classmethod
    def xoa(cls):
        ma = input("Nhập mã nhà xuất bản cần xóa: ")
        for nxb in cls.Publishers:
            if nxb['ma'] == ma:
                cls.Publishers.remove(nxb)
                print("Xóa nhà xuất bản thành công.")
                return
        print("Không tìm thấy nhà xuất bản có mã này!")

    @classmethod
    def sap_xep_theo_ten(cls):
        cls.Publishers.sort(key=lambda x: x['ten'])
        print("Danh sách đã được sắp xếp theo tên Nhà Xuất Bản (A-Z).")
        cls.hien_thi_danh_sach()

    @classmethod
    def dem_so_luong(cls):
        print(f"Tổng số Nhà Xuất Bản hiện có: {len(cls.Publishers)}")

    @classmethod
    def cap_nhat(cls):
        ma = input("Nhập mã nhà xuất bản cần cập nhật: ")
        for nxb in cls.Publishers:
            if nxb['ma'] == ma:
                print(f"Đang cập nhật thông tin cho Nhà Xuất Bản {nxb['ten']}")
                nxb['ten'] = input("Nhập tên nhà xuất bản mới: ") or nxb['ten']
                nxb['dia_chi'] = input("Nhập địa chỉ mới: ") or nxb['dia_chi']
                nxb['email'] = input("Nhập email mới: ") or nxb['email']
                nxb['sdt'] = input("Nhập số điện thoại mới: ") or nxb['sdt']
                print("Cập nhật thông tin Nhà Xuất Bản thành công.")
                return
        print("Không tìm thấy nhà xuất bản có mã này!")

    @classmethod
    def dao_nguoc_danh_sach(cls):
        if len(cls.Publishers) == 0:
            print("Danh sách nhà xuất bản trống, không đảo ngược.")
        else:
            cls.Publishers.reverse()
            print("Danh sách nhà xuất bản đã được đảo ngược.")
            cls.hien_thi_danh_sach()

        @classmethod
    def loc_theo_ma(cls):
        ma = input("Mời bạn nhập mã nhà xuất bản để lọc: ").lower()
11':
                    if cls.confirm_action("Bạn có chắc chăn muốn thoát hay không: "):
                        print("Thoát menu.")
                    break
                case _:
                    print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

