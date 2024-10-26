import prettytable as pt

# 显示座位
def show_ticket(row_num, seating):
    tb = pt.PrettyTable()  # 创建一个表格
    # 设置标题（表头部分）
    tb.field_names = ['行号', '座位数1', '座位数2', '座位数3', '座位数4', '座位数5', '座位数6']
    # 遍历所有显示座位状态
    for i in range(row_num):
        lst = [f'第{i + 1}行'] + seating[i]  # 使用当前座位状态
        tb.add_row(lst)
    print(tb)


# 订票
def order_ticket(seating, row, column):
    row_index = int(row) - 1  # 转换为0基索引
    column_index = int(column) - 1  # 转换为0基索引

    if seating[row_index][column_index] == '有票':
        seating[row_index][column_index] = '已售'  # 更新座位状态
        print("订票成功！")
    elif seating[row_index][column_index] == '已售':
        print('抱歉，你选择的桌位已被选购')
    else:
        print('无效的座位选择')


if __name__ == '__main__':
    row_num = 6
    # 初始化座位状态
    seating = [['有票'] * 6 for _ in range(row_num)]

    while True:
        show_ticket(row_num, seating)  # 显示当前座位状态
        # 开始售票
        choose_num = input('请输入您选择的座位：如4,3表示第4排第三列，退出请输入\'exit\'：')
        if choose_num == 'exit':
            break
        try:
            row, column = choose_num.split(',')  # 系列解包赋值
            order_ticket(seating, row, column)  # 处理订票
        except (ValueError, IndexError):
            print('输入格式不正确，请输入有效的行和列，如4,3')

# import prettytable as pt
#
#
# # 初始化座位图
# def initialize_seating(row_num):
#     return [['有票'] * 6 for _ in range(row_num)]
#
#
# # 显示座位图
# def show_ticket(seating):
#     tb = pt.PrettyTable()  # 创建一个表格
#     tb.field_names = ['行号', '座位数1', '座位数2', '座位数3', '座位数4', '座位数5', '座位数6']
#
#     for i, row in enumerate(seating):
#         tb.add_row([f'第{i + 1}行'] + row)
#     print(tb)
#
#
# # 订票
# def order_ticket(seating, row, column):
#     row_index = int(row) - 1  # 转换为0基索引
#     column_index = int(column) - 1  # 转换为0基索引
#
#     if seating[row_index][column_index] == '有票':
#         seating[row_index][column_index] = '已售'
#         print("订票成功！")
#     else:
#         print("抱歉，该座位已被售出。")
#
#
# if __name__ == '__main__':
#     row_num = 6
#     seating = initialize_seating(row_num)
#
#     while True:
#         show_ticket(seating)  # 显示当前座位图
#
#         # 开始售票
#         choose_num = input('请输入您选择的座位：如4,3表示第4排第三列（输入exit退出）：')
#         if choose_num.lower() == 'exit':
#             break
#         row, column = choose_num.split(',')  # 拆包赋值
#         order_ticket(seating, row, column)  # 处理订票


