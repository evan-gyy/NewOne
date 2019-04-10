import random

def transstr(lsn):
    lsnstr = lsn.replace('\t', ':')
    countls = lsnstr.split('\n')
    return countls

def trans(lsn):
    lsnstr = ''.join(lsn).replace('\t', ':')
    countls = lsnstr.split('\n')
    return countls

def randchance(classes, key2):
    answer = input("\n>> 请输入类别字母（输入i获取答案）：")
    allchances = random.randint(2, 999999999)
    i = 1
    while i < allchances:
        if answer == 'i':
            print(f"\n>> 答案: {classes}类\n")
            return
        if answer == key2:
            print('\n>> 答对啦！\n')
            return
        chances = allchances - i
        print(f'\n>> 错啦！你还有{chances}次机会嘿嘿\n')
        i = i + 1
        answer = input("\n>> 请输入类别字母（输入i获取答案）：")
    print(f"\n>> 机会用完啦！公布答案: {classes}类\n")

countop = open('count.txt', 'r')
counttr = countop.read()
# method 1

# method 2

clean = counttr.replace('_', '')
all = transstr(clean)
# it's a big big list

assets, liability, equity, cost, profit_loss = counttr.split('_')
# they are strings

assets = trans(assets)
liability = trans(liability)
equity = trans(equity)
cost = trans(cost)
profit_loss = trans(profit_loss)

try:
    while True:
        print('\n\n会计科目分为五类：a.资产类 b.负债类 c.所有者权益类 d.成本类 e.损益类')
        print('\n以下会计科目属于哪一类？\n')
        elements = random.choice(all)
        print(f'\t{elements}')

        if elements in assets:
            randchance('资产', 'a')
        elif elements in liability:
            randchance('负债', 'b')
        elif elements in equity:
            randchance('所有者权益', 'c')
        elif elements in cost:
            randchance('成本', 'd')
        elif elements in profit_loss:
            randchance('损益', 'e')

        input('   再来一题：Enter\n   溜了溜了：Ctrl+C')

except KeyboardInterrupt:
    print("\n\n   Wish you a good mark!\n")

countop.close()
