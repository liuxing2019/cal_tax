def main():
    # 月总收入
    print("月薪：")
    month_salary = int(input())
    print("年终奖（12个月月薪外的全部收入）：")
    awards = int(input())
    # 深圳为例，养老8%，医疗2%，失业0.3%
    print("月社保扣除（自行计算）：")
    social_security = int(input())
    # 基数*比例
    print("月个人公积金（自行计算）：")
    housing_fund = int(input())
    # 租房的话每个月抵扣1500
    print("月附加扣除额（个税app自行申报）：")
    add_deduct = int(input())

    # 每月累计应纳税额
    month_amount = []
    for i in range(12):
        month_amount.append((i + 1) * (month_salary - social_security - housing_fund - add_deduct - 5000))
    month_amount.append(round((awards + month_amount[-1]), 2))

    # print("年应纳税额：")
    # year_amount = month_salary * 12 + awards - 12 * (social_security + housing_fund + add_deduct) - 60000
    year_amount = month_amount[-1]

    print("\n=============")
    print("年税前收入：")
    print(12*month_salary+awards)

    print("年总个税：")
    year_tax = cal_tax(year_amount)
    print(year_tax)

    print("年到账收入：")
    print(12*month_salary+awards-year_tax-12*social_security-12*housing_fund)

    print("年公积金收入：")
    print(12*housing_fund*2)

    # 每月个税，默认年终奖在年末单独扣税
    month_tax = []
    for i in month_amount:
        tmp = 0
        for j in month_tax:
            tmp = tmp + j
        month_tax.append(round((cal_tax(i) - tmp), 2))
    for i in range(len(month_tax)):
        if i == len(month_tax) - 1:
            print("年终奖扣税：%s" % month_tax[i])
        else:
            print("%s月个税：%s" % (i + 1, month_tax[i]))
    print("===================")


# 2019新个税法
def cal_tax(year_amount):
    if year_amount <= 36000:
        tax = 0.03 * year_amount
    elif year_amount <= 144000:
        tax = 0.1 * year_amount - 2520
    elif year_amount <= 300000:
        tax = 0.2 * year_amount - 16920
    elif year_amount <= 420000:
        tax = 0.25 * year_amount - 31920
    elif year_amount <= 660000:
        tax = 0.3 * year_amount - 52920
    elif year_amount <= 960000:
        tax = 0.35 * year_amount - 85920
    else:
        tax = 0.45 * year_amount - 181920
    return round(tax, 2)


if __name__ == '__main__':
    while True:
        main()
