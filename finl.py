import os.path
import os
import sys
import csv
import openpyxl
import getpass
import time
import numpy as np
import pandas as pd



def load_user_data(data_csv):  # 返還讀取內容
    if(os.path.isfile(data_csv)):
        # print("讀取到文件<userdata.csv>")
        us_data = pd.read_csv("userdata.csv", sep=' ',
                              encoding='utf-8', engine='python', header=None)
        data = np.array(us_data)

    else:
        # print("<<沒有用戶資料檔 將創造用戶資料文件>>")
        us_data = open(data_csv, "w+", encoding='utf-8', newline='')
        # print("已創造文件<userdata.csv>")
        writer = csv.writer(us_data, delimiter=' ')
        data = []
        data.append([0, "admin", "admin"])
        for line in range(0, 1000):
            data.append([10001+line, "nu", "np"])
            writer.writerow([10000+line, "nu", "np"])

        us_data.close()
    return data

#==============================================================================================================================================
def data_update(data_csv, new_data):
    us_data = open(data_csv, "w+", encoding='utf-8', newline='')
    writer = csv.writer(us_data, delimiter=' ')

    for line in range(0, len(new_data)):
        writer.writerow(
            [new_data[line][0], new_data[line][1], new_data[line][2]])
    us_data.close()

#==============================================================================================================================================
def old_user():  # 使用者登入
    print("登入賬號.")
    user_num = int(input("賬號號碼 : "))
    user_name = input("賬號名稱 : ")
    user_password = getpass.getpass("賬號密碼 : ")
    return user_num, user_name, user_password

#==============================================================================================================================================
def new_user():  # 新的使用者
    print("感謝你註冊會員,請輸入新的賬號名稱.")
    user_name = input("賬號名稱 : ")
    user_a_password = input("使用者密碼 : ")
    user_b_password = input("確認密碼 : ")

    while user_a_password != user_b_password:
        print("兩次輸入的密碼不同! 請重新輸入")
        user_a_password = input("賬號密碼 : ")
        user_b_password = input("確認密碼 : ")

    return user_name, user_a_password

#==============================================================================================================================================
def quickly_select_user_data(data):
    for select in range(1, len(data)):
        if data[select][1] == 'nu':
            return select
        # print(select[0][1])
    return 'full'

#==============================================================================================================================================
def align_data():  # 資料對齊
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)

#==============================================================================================================================================
def SpecialOffers():  # 顯示特價商品

    df = pd.read_excel("商品資料庫.xlsx",
                       #  sheet_name="工作表1",
                       usecols=["商品名稱", "特價", "特價後價格"])

    special_offers = df[df["特價"] == 1]
    special_offers = special_offers.drop(columns=["特價"])  # 刪除特價欄位

    print("特價商品列表:")
    print(special_offers)

def add_product():
    df = pd.read_excel("商品資料庫.xlsx")
    product_name = input("請輸入商品名稱： ")
    product_price = input("請輸入商品價格：")
    special_offer = int(input("該商品是否特價（1表示是，0表示否）："))
    if special_offer == 1:
        discounted_price = float(input("請輸入特價後價格： "))
    else:
        discounted_price = 0

    new_row = {"商品名稱": product_name, "價格": product_price,
               "特價": special_offer, "特價後價格": discounted_price}

    df.loc[len(df)] = new_row  # 將資料加入工作表

    # 保存資料
    df.to_excel("商品資料庫.xlsx", index=False)
    print("商品列表:")
    print(df)

#==============================================================================================================================================
def remove_product():
    df = pd.read_excel("商品資料庫.xlsx")
    product_name = input("請輸入要下架的商品名稱：")

    # 找對應的行
    index_to_remove = df[df["商品名稱"] == product_name].index

    # 刪除對應的行
    df.drop(index_to_remove, inplace=True)

    # 保存修改後的資料
    df.to_excel("商品資料庫.xlsx", index=False)
    print("商品列表:")
    print(df)

#==============================================================================================================================================
def edit_product(product_name):
    # 找到欲修改商品
    df = pd.read_excel("商品資料庫.xlsx")
    print(df)
    index_to_edit = df[df["商品名稱"] == product_name].index

    if len(index_to_edit) == 0:
        print("找不到該商品，請確認輸入之產品名稱是否正確")
        return
    # 印出商品目前資料
    print(df.loc[index_to_edit])

    change = input("欲修改項目：1.名稱 2.價格 3.特價狀態 4.特價價格：")
    if change == "1":
        new_product_name = input("請輸入新的商品名稱: ")
        df.loc[index_to_edit, "商品名稱"] = new_product_name
    elif change == "2":
        new_product_price = input("請輸入新的商品價格")
        df.loc[index_to_edit, "價格"] = new_product_price
    elif change == "3":
        new_special_offer = int(input("該商品是否特價（1表示是，0表示否）: "))
        df.loc[index_to_edit, "特價"] = new_special_offer
    elif change == "4":
        new_discounted_price = float(input("請輸入新的特價後價格： "))
        df.loc[index_to_edit, "特價後價格"] = new_discounted_price

    df.to_excel("商品資料庫.xlsx", index=False)
    print(df)

#==============================================================================================================================================
def popular_products():
    df = pd.read_excel("商品資料庫.xlsx")
    popular_products=df.nlargest(5, "銷售數量")

    print("熱賣商品列表:")
    print(popular_products)

#==============================================================================================================================================
def return_product(id_no):
    df = pd.read_excel("商品資料庫.xlsx")
    # print(df.loc[1])
    return df.loc[id_no]

#==============================================================================================================================================
def product_data_print():
    df = pd.read_excel("商品資料庫.xlsx")
    print("商品列表:")
    print(df)

#==============================================================================================================================================
def add_new_shopping_item():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "商品資料庫"
    print("已創造文件<商品資料庫.xlsx>")
    # 保存資料
    sheet['A1'] = '商品名稱'
    sheet['B1'] = '價格'
    sheet['C1'] = '商品簡介'
    sheet['D1'] = '特價'
    sheet['E1'] = '折數'
    sheet['F1'] = '特價後價格'
    sheet['G1'] = '銷售數量'

    wb.save("./商品資料庫.xlsx")
    # print(sheet)

#==============================================================================================================================================
def add_item():
    df = pd.read_excel("商品資料庫.xlsx")
    new_row = {}

    new_row[0] = {"商品名稱": '可口可樂', "價格": 10, "特價": 1, "特價後價格": 7}
    new_row[1] = {"商品名稱": '百世可樂', "價格": 10, "特價": 0, "特價後價格": 10}
    new_row[2] = {"商品名稱": '快樂薯片', "價格": 10, "特價": 0, "特價後價格": 10}
    new_row[3] = {"商品名稱": '幸運薯片', "價格": 10, "特價": 1, "特價後價格": 10}
    new_row[4] = {"商品名稱": '不粘強力膠', "價格": 10, "特價": 0, "特價後價格": 10}
    new_row[5] = {"商品名稱": '蘋果西打', "價格": 10, "特價": 0, "特價後價格": 10}
    new_row[6] = {"商品名稱": '黑松沙士', "價格": 10, "特價": 1, "特價後價格": 10}
    new_row[7] = {"商品名稱": '鱈魚香絲', "價格": 10, "特價": 0, "特價後價格": 10}
    new_row[8] = {"商品名稱": '橘子芬達', "價格": 10, "特價": 0, "特價後價格": 10}
    new_row[9] = {"商品名稱": '七喜', "價格": 10, "特價": 0, "特價後價格": 10}

    for i in range(0, 10):
        df.loc[len(df)] = new_row[i]
    df.to_excel("商品資料庫.xlsx", index=False)
#==============================================================================================================================================
def add_provisional_shop_data():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "provisional_shop"
    # print("已創造文件<provisional_shop.xlsx>")
    # 保存資料
    sheet['A1'] = '用戶ID'
    sheet['B1'] = '商品名稱'
    sheet['C1'] = '價格'
    sheet['D1'] = '購買數量'
    sheet['E1'] = '購買時間'

    wb.save("./provisional_shop.xlsx")
    # print(sheet)

#==============================================================================================================================================
def add_cart_data(user_id):  # 使用者id 購物id 購物數量
    df = pd.read_excel("商品資料庫.xlsx")
    shop_data = pd.read_excel("provisional_shop.xlsx")
    localtime = time.strftime("%Y-%m-%d", time.localtime())  # time
    # data = {'用戶ID','商品名稱','價格','購買數量','購買時間'}

    product_name = input("商品名稱:")
    shop_count = int(input("商品數量:"))

    find_data_df = df[df["商品名稱"] == product_name].index
    find_data_shop = shop_data[shop_data["商品名稱"] == product_name].index

    A = df.loc[find_data_df].values

    if len(find_data_df) == 0:
        print("找不到該商品，請確認輸入之產品名稱是否正確")
        return

    if len(find_data_shop) == 0:
        shop_data.loc[len(shop_data)] = {
            '用戶ID': user_id, '商品名稱': A[0][0], '價格': A[0][1], '購買數量': shop_count, '購買時間': localtime}

    else:
        shop_data.loc[find_data_shop,"購買數量"] += shop_count
        shop_data.loc[find_data_shop,"購買時間"] = localtime

    print("已加入商品")
    shop_data.to_excel("provisional_shop.xlsx", index=False)

#==============================================================================================================================================
def remove_cart_data():  # 使用者id 購物id 購物數量
    shop_id = input("商品名稱:")
    shop_data = pd.read_excel("provisional_shop.xlsx")
    localtime = time.strftime("%Y-%m-%d", time.localtime())  # time
    # data = {'用戶ID','商品名稱','價格','購買數量','購買時間'}

    find_data_in = shop_data[shop_data["商品名稱"] == shop_id].index

    if len(find_data_in) == 0:
        print("找不到該商品!")

    else:
        shop_data.drop(find_data_in, inplace=True)
        print("已刪除商品!")
    shop_data.to_excel("provisional_shop.xlsx", index=False)

#==============================================================================================================================================
def edit_cart_data():  # 使用者id 購物id 購物數量
    # df = return_product(id_no)
    shop_id = input("商品名稱:")
    shop_count = int(input("商品數量:"))
    shop_data = pd.read_excel("provisional_shop.xlsx")
    localtime = time.strftime("%Y-%m-%d", time.localtime())  # time
    # data = {'用戶ID','商品名稱','價格','購買數量','購買時間'}

    find_data_in = shop_data[shop_data["商品名稱"] == shop_id].index

    if len(find_data_in) == 0:
        print("找不到該商品!")

    else:
        shop_data.loc[find_data_in, "購買數量"] = shop_count
        shop_data.loc[find_data_in, "購買時間"] = localtime
        print("已修改商品數量!")
    shop_data.to_excel("provisional_shop.xlsx", index=False)

#==============================================================================================================================================
def show_cart_data():
    shop_data = pd.read_excel("provisional_shop.xlsx")
    total = 0
    # for line in range(0,len(shop_data)):
    #     total += shop_data.loc[line][2]*shop_data.loc[line][3]
    print(shop_data)
    # print("Total : " + str(total))
#==============================================================================================================================================
def delivery_order_save():
    shop_data = pd.read_excel("provisional_shop.xlsx")
    order_data = pd.read_excel("delivery_order.xlsx")

    A6 = input("優惠卷代碼:")
    
    if A6 == '111':
        A6 = 0.9
    else:
        A6 = 1
    df=pd.read_excel("商品資料庫.xlsx")
    for line in range(0,len(shop_data)):
        A1 = shop_data.loc[line][0]
        A2 = shop_data.loc[line][1]
        A3 = shop_data.loc[line][2] * A6
        A4 = shop_data.loc[line][3]
        A5 = shop_data.loc[line][4]

        new_row = {'用戶ID': A1, '商品名稱': A2, '價格': A3, '購買數量': A4, '購買時間': A5}
        order_data.loc[len(order_data)] = new_row
        
        find_data_df=df[df["商品名稱"]==A2].index.tolist()#將索引轉為列表
        
        df.loc[find_data_df,"銷售數量"]+=A4 #更新銷售數量
        
    order_data.to_excel("delivery_order.xlsx", index=False)
    
    print("已結賬!")
    df.to_excel("商品資料庫.xlsx",index=False)

#==============================================================================================================================================

if __name__ == '__main__':  # 主程序開始執行
    align_data()
    us_ = 'userdata.csv'  # 資料夾名稱
    user_d = load_user_data(us_)  # 取得文件內容並存取**
    ac_in = False

    print("歡迎來到購物城,請先登入(1)或註冊(2):結束(3)")
    user_choose = input("選擇:")
#============================================================================================================================================== 賬號登入 in
    while True:
        # shop_data = {'用戶ID','商品名稱','價格','購買數量','購買時間'}
        shop_data = {}
        if user_choose != '1' and user_choose != '2' and user_choose != '3':
            user_choose = input("輸入有誤\n請輸入數字: 1 2 3:")
            continue

        if user_choose == '3':
            print('感謝你使用購物網路!')
            sys.exit(0) 
    
        elif user_choose == '1':
            user_data_check = old_user()
            find_user = False
            # print(user_data_check[0])
            # print(user_data_check[1])
            # print(user_data_check[2])
            if(user_data_check[0] == 0 and user_data_check[1] == 'admin' and user_data_check[2] == 'admin'):
                find_user = True
                print('進入管理員模式')
    
            if find_user == False:     # user_data_check = id_no username password
                if(user_d[user_data_check[0]-10000][1] == user_data_check[1] and user_d[user_data_check[0]-10000][2] == user_data_check[2]):
                    print(user_data_check[1]+'歡迎回來!')
                    find_user = True
                else:
                    print('沒有找到 ID:'+user_data_check[0] + 'User:' + user_data_check[1]+'的使用者')
                    print('請重新選擇!')
            
        else:
            user_data_check = new_user()
            select_ = quickly_select_user_data(user_d)
    
            if select_ != 'full':
                print("已新增用戶:", user_data_check[0])
                print("賬號ID:", 10000+select_)
                user_d[select_][1] = user_data_check[0]
                user_d[select_][2] = user_data_check[1]
            data_update(us_, user_d)
#==============================================================================================================================================
        if os.path.isfile("商品資料庫.xlsx"):
            df = pd.read_excel("商品資料庫.xlsx")
        else:
            add_new_shopping_item()
            add_item()
            df = pd.read_excel("商品資料庫.xlsx")
        product_data_print()
        add_provisional_shop_data()
#==============================================================================================================================================
        print("選擇服務: 1.商品 2.購物車 3.結賬 4.登出 5.結束程序")
        login_user_choose = input("選擇:")

        while True:
          # login_user_choose = '0' #防bug
            if login_user_choose != '1' and login_user_choose != '2' and login_user_choose != '3' and login_user_choose != '4' and login_user_choose != '5':
                login_user_choose = input("輸入有誤\n請輸入數字 1 2 3 4 5:")
                continue
#==============================================================================================================================================商品
            if login_user_choose == '1':
                while True:
                    print("選擇服務: 1.顯示商品內容 2.顯示熱賣內容 3.顯示特價內容 4.返回上一層")
                    login_user_choose = input("選擇:")
                    if login_user_choose != '1' and login_user_choose != '2' and login_user_choose != '3' and login_user_choose != '4':
                        login_user_choose = input("輸入有誤\n請輸入數字 1 2 3 4:")
                        continue
      
                    if login_user_choose == '1':
                        product_data_print()
                    elif login_user_choose == '2':
                        popular_products()
                    elif login_user_choose == '3':
                        SpecialOffers()
                    elif login_user_choose == '4':
                        print("選擇服務: 1.商品 2.購物車 3.結賬 4.登出 5.結束程序")
                        login_user_choose = input("選擇:")
                        break
#==============================================================================================================================================購物車
            elif login_user_choose == '2':
                while True:
                    print("選擇服務: 1.加入商品 2.刪除商品 3.修改商品數量 4.顯示購物車 5.返回上一層")
                    login_user_choose = input("選擇:")
      
                    if login_user_choose != '1' and login_user_choose != '2' and login_user_choose != '3' and login_user_choose != '4' and login_user_choose != '5':
                        login_user_choose = input("輸入有誤\n請輸入數字 1 2 3 4 5:")
                        continue
      
                    if login_user_choose == '1':
                        shop_data = add_cart_data(user_data_check[0])

                    elif login_user_choose == '2':
                        remove_cart_data()

                    elif login_user_choose == '3':
                        edit_cart_data()

                    elif login_user_choose == '4':
                        show_cart_data()

                    elif login_user_choose == '5':
                        print("選擇服務: 1.商品 2.購物車 3.結賬 4.登出 5.結束程序")
                        login_user_choose = input("選擇:")
                        break
#==============================================================================================================================================結賬
            elif login_user_choose == '3':
                delivery_order_save()
                add_provisional_shop_data()
                print("選擇服務: 1.商品 2.購物車 3.結賬 4.登出 5.結束程序")
                login_user_choose = input("選擇:")
#==============================================================================================================================================登出
            elif login_user_choose == '4':
                add_provisional_shop_data()
                find_user = 0
                print("歡迎來到購物城,請先登入(1)或註冊(2):結束(3)")
                user_choose = input("選擇:")
#==============================================================================================================================================結束
            elif login_user_choose == '5':
                print('感謝你使用購物網路!')
                sys.exit(0) 








