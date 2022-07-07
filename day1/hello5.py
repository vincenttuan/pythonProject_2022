# 變數的應用
symbol = '2330'  # 股票代號
name = '台積電'   # 股票名稱
price = 410      # 價格
shares = 3000    # 買進股數
fee = 0.003      # 手續費
# 計算買入成本 + 手續費
total = shares * price
total = total + (total * fee)
print("買入成本:%.1f" % total)
# total 經過 format 格式化之後會變成字串
print("買入成本:%s" % format(total, ","))
print("%s %s 買入成本:%s" % (symbol, name, format(total, ",")))
