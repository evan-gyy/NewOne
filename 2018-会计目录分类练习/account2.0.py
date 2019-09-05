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
    allchances = random.randint(2, 4)
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


account = """库存现金	存放在出纳保管的现款
银行存款	存放在企业银行的款项
其他货币资金	银行汇票、本票、信用卡、信用证存款
交易性金融资产	短期的债券、股票、基金投资的公允价值
应收票据	销售商品收到的商业汇票
应收账款	销售商品或提供的劳务尚未收取的款项
预付账款	按合同规定预付给供货单位的款项
应收股利	应收取的现金股利或利润
应收利息  应收取交易性和可供出售金融资产及持有到期投资(债券等)的利息
其他应收款  指各种应收及暂付款项（如职工借款、押金等）
材料采购	指采用计划成本核算材料而购入材料的实际采购成本
在途物资	采用实际成本核算材料，货款已付尚未验收入库的在途材料的采购成本
原材料	用于制造产品而存放在金库的材料
材料成本差异	材料计划成本与实际采购成本的差额
库存商品	存放在仓库的商品（产成品）
发出商品	未满足收入确认条件而发出的商品实际成本
委托加工物资	委托外单位加工材料的实际成本
周转材料	指包装物、低值易耗品及建筑业的钢模板、木模板、脚手架等的实际成本
固定资产	使用年限在一年以上，单位价值较高机器设备、房屋等
累计折旧（贷） 指固定资产累计的损耗价值（抵减固定资产价值）
在建工程	正在建造或安装的固定资产的支出
工程物资	为在建工程准备的各种物资
固定资产清理	核算固定资产报废时转出价值及清理费用
无形资产	没有实物形态的长期资产（如商标权、专利权等）
累计摊销（贷） 对使用寿命有限的无形资产计提摊销_
短期借款	偿还期在一年内（含一年）的借款
交易性金融负债  发行短期债券、基金应承担的债务
应付票据	购买材料及商品开出的商业汇票
应付账款	购买材料、商品等尚未支付经供应单位的款项
预收账款	按合同规定向购货单位预收的款项
应付职工薪酬  应付而未付的职工工资、福利费、社保费、住房公积金等
应交税费	应交而未交给税务局的各种税费
应付股利	应付未付给投资者的现金股利和利润
应付利息	应付未付投资者的债券利息及长期借款利息
其他应付款  指各项应付、暂收的款项（如暂收押金等）
长期借款	指偿还期在一年以上的借款
应付债券	指发行债券的企业应付而未付的本金和利息_
实收资本	实际收到投资者投入的资本金（注册资本)
资本公积	超过注册资本那部份的投资金额
盈余公积	按净利润提取的公共积累
本年利润	按本年度实现的利润或亏损额
利润分配	历年积累下来待分配的利润_
生产成本	生产产品耗用的材料,工人工资,生产车间费用
制造费用	无法直接计入产品成本的生产车间费用(如车间管理人员工资、车间折旧费、耗用的物料等）
劳务成本	指对外提供劳务（修理等）发生的成本
研发支出	为研究和研发资产发生的支出_
主营业务收入	企业销售主要商品的收入
其他业务收入	指销售材料、出租财产租金收入等
投资收益	指购买股票、债券、基金等投资取得的收入
营业外收入	与生产经营无直接关系的各种收入。（台出售无形资产收益，处置固定资产净收益等）
主营业务成本	销售主要商品的实际成本
其他业务成本	指其他业务收入发生的成本
营业税金及附加	指营业税、城建税、教育费附加、消费税等
销售费用	为销售商品而发生的运输费、广告费、展览费等
管理费用	厂部行政办公室的管理人员工资、折旧费、差旅费、水电费、业务接待费、办公费等
财务费用	指短期借款利息支出、汇兑手续费等
资产减值损失	计提各项资产减值准备所形成的损失
营业外支出	与生产经营无关的支出（如固定资产盘亏、处置固定资产净损失，出售无形资产损失，自然灾害损失）
所得税费用	按利润总额计提的所得税款
"""
# method 2

clean = account.replace('_', '')
all = transstr(clean)
# it's a big big list

assets, liability, equity, cost, profit_loss = account.split('_')
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
