# 讀寫一個檔案
# 1. 開啟檔案, 2. 讀寫入資料
# r+: opens the file for both reading and writing
# w+: opens for writing (and thus truncates the file) and reading
# r: reading
# w:writing
try:
    f = open('demo.txt', 'r+', encoding="UTF-8")
    print(f.readlines())
    try:
        f.write("\nPython AI")
    except Exception as e:
        print('資料寫入失敗!', e)
    finally:
        print('關閉檔案')
        f.close()
except FileNotFoundError as fnf:
    print('檔案找不到:', fnf)

