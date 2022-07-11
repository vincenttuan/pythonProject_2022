# *不定數量參數
def getScoreSummary(*score):
    print(score, type(score))
    len_value = len(score)  # 個數
    sum_value = sum(score)  # 總和
    avg_value = sum_value / len_value  # 平均
    return len_value, sum_value, avg_value


if __name__ == '__main__':
    lenValue, sumValue, avgValue = getScoreSummary(100, 90, 80, 70, 60)
    print('個數: %d 總和: %d 平均: %.1f' % (lenValue, sumValue, avgValue))
