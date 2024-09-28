books = []

def display_books():
    if not books:
        print("Không có sách trong danh sách.")
    else:
        for book in books:
            print(f"Mã: {book['Mã']}, Tác giả: {book['Tác giả']}, Tiêu đề: {book['Tiêu đề']}, Thể loại: {book['Thể loại']}, Số bản sao: {book['Số bản sao']}")
    print()

def add_book():
    ma = input("Nhập mã sách: ")
    tac_gia = input("Nhập tên tác giả: ")
    tieu_de = input("Nhập tiêu đề sách: ")
    the_loai = input("Nhập thể loại sách: ")
    so_ban_sao = input("Nhập số bản sao: ")
   

    if not ma or not tac_gia or not tieu_de or not the_loai or not so_ban_sao.isdigit():
        print("Dữ liệu không hợp lệ, vui lòng nhập lại.")
        return

    books.append({"Mã": ma, "Tác giả": tac_gia, "Tiêu đề": tieu_de, "Thể loại": the_loai, "Số bản sao": int(so_ban_sao)})
    print("Sách đã được thêm thành công!\n")

def update_book():
    ma = input("Nhập mã sách muốn cập nhật: ")
    for book in books:
        if book['Mã'] == ma:
            print("Sách hiện tại:", book)
            if input("Xác nhận cập nhật (Y/N)? ").upper() == 'Y':
                book['Tác giả'] = input("Nhập tên tác giả mới: ")
                book['Tiêu đề'] = input("Nhập tiêu đề mới: ")
                book['Thể loại'] = input("Nhập thể loại mới: ")
                book['Số bản sao'] = int(input("Nhập số bản sao mới: "))
                print("Cập nhật thành công!\n")
            return
    print("Không tìm thấy sách với mã này.\n")

def delete_book():
    ma = input("Nhập mã sách muốn xóa: ")
    for book in books:
        if book['Mã'] == ma:
            if input("Xác nhận xóa (Y/N)? ").upper() == 'Y':
                books.remove(book)
                print("Sách đã bị xóa.\n")
            return
    print("Không tìm thấy sách với mã này.\n")

def search_books():
    keyword = input("Nhập từ khóa tìm kiếm (mã/tác giả/tiêu đề/thể loại): ")
    found_books = [book for book in books if keyword in book['Mã'] or keyword in book['Tác giả'] or keyword in book['Tiêu đề'] or keyword in book['Thể loại']]
    
    if found_books:
        for book in found_books:
            print(f"Mã: {book['Mã']}, Tác giả: {book['Tác giả']}, Tiêu đề: {book['Tiêu đề']}, Thể loại: {book['Thể loại']}, Số bản sao: {book['Số bản sao']}")
    else:
        print("Không tìm thấy sách nào.\n")

def menu():
    while True:
        print("1. Hiển thị danh sách sách")
        print("2. Tìm kiếm sách")
        print("3. Thêm sách")
        print("4. Cập nhật sách")
        print("5. Xóa sách")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")
        if choice == '1':
            display_books()
        elif choice == '2':
            search_books()
        elif choice == '3':
            add_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            if input("Xác nhận thoát (Y/N)? ").upper() == 'Y':
                print("Đã thoát chương trình.")
                break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")


