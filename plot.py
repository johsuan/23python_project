import matplotlib.pyplot as plt
import pandas as pd


#購買日期折線圖
df=pd.read_excel("delivery_order.xlsx")
purchase_time=df["購買時間"]
purchase_count=df.shape[0]
plt.plot(purchase_time,range(1,purchase_count+1),"bo-")

plt.title("購買時間走勢圖",fontsize=24,loc="center")
plt.xlabel("日期",fontsize=10)
plt.ylabel("購買筆數",fontsize=10)
plt.show()
#plt.savefig()
'''
#購買數量長條圖
df=pd.read_excel("商品資料庫.xlsx")
product_names=df["商品名稱"]
sales_quantities= df["銷售數量“]
plt.bar(product_names,sales_quentities)
plt.xlabel("商品名稱")
plt.ylabel("銷售數量")
plt.title("各項商品銷售數量統計圖")
                     
plt.xticks(rotation=45)
plt.figure(figsize=(12,6))

plt.show()                     
'''
