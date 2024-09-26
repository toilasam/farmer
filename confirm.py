
def confirm_exit():
    confirm = input('Bạn muốn thoát chương trình (y/n): ').lower()
    if confirm == 'y':
        exit()
    elif confirm == 'n':
        print('Trở lại chương trình')
    else:
        print('Lựa chọn không hợp lệ.')