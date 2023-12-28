import random  # 导图随机模块
class system:  # 创建类：system，代表银行系统
    def __init__(self):  # 定义初始化方法，构造全局变量
        self.id_card = None  # 身份证号码
        self.password = None  # 密码
        self.card_num = None  # 卡号
        self.userdata = []  # 用户信息为一个空列表
        self.token = False # 登录状态
        self.money = 0

    def sign_up(self):
        """
        定义方法：注册，sign_up
        :return:
        """
        print("----------欢迎访问浦发银行系统！本系统由薛永华设计！----------")
        print("下面进入注册页面")
        name = input("请输入你的姓名：")  # 输入姓名
        address = input("请输入你的地址：")  # 输入地址
        self.id_card = input("请输入你的身份证：")  # 输入身份证号码
        self.password = input("请输入你的密码：")  # 输入密码
        password2 = input("请再次输入你的密码：")  # 再次输入密码
        if self.password != password2:  # 如果第一次输入的密码和第二次输入的密码不相同
            print("两次密码不同，请重新输入")  # 系统提示请重新输入密码，完成两次密码的校验
            self.password = input("请输入你的密码：")
            password2 = input("请再次输入你的密码：")
        self.card_num = random.randint(6210000000000000000,6230000000000000000)  # 卡号是用random模块的randint方法随机生成的
        print(f"恭喜您，注册成功，您的卡号为：{self.card_num}") # 系统提示卡号注册成功，并输出卡号
        self.userdata.append({
            "姓名":name,
            "地址":address,
            "身份证":self.id_card,
            "密码":self.password,
            "卡号":self.card_num,
        })  # 把用户信息以字典的形式存储到本地
        f = open('Mysql.txt','a+',encoding='utf-8')  # 用a+格式，使用utf-8编码，创建Mysql.txt文件
        f.write(f"{self.userdata}")  # 写入用户数据

    def login(self):
        """
        定义方法：登录，login
        :return:
        """
        if self.card_num == '' and self.password == '':  # 登录的时候系统要判断用户是否注册，卡号和密码是否等于空值
            raise TypeError("你还没有注册，请先进行注册")  # 系统报错，提示没有注册也就不能进行登录，登录时为了用户数据安全得设置登录次数
        print("下面进入登录页面")
        index = 0
        while index <= 5:  # 登录时为了用户数据安全，设置登录次数小于等于5次
            index += 1  # 每登录一次，记录就增加一次
            login_card_num = int(input("请输入你的卡号："))  # 加int 是因为系统生成的卡号是整数形式，而不是字符串形式
            login_password = input("请输入你的密码：")
            if self.card_num == login_card_num and self.password == login_password:  # 如果登录时卡号密码输入正确，就登录系统
                print("登录成功")
                self.token = True  # 登录成功，修改登录状态为有效，并结束循环
                break
            else:
                print(f"登录失败，密码输入错误，请重新输入。提示：还剩{5 - index}次登录机会")  # 否则，让用户继续登录
                if index == 5:
                    print("你的账户已被封禁，请明天在尝试。")  # 如果登录次数等于5次，就提示账户已被封禁，并结束循环
                    break
        print("欢迎进入浦发银行主页")  # 要是第一次卡号和密码就输入正确，就直接进入系统

    def query(self):
        """
        定义方法：查询余额，query
        :return:
        """
        if self.token == False:  # 如果登录状态无效，系统就会报错提示用户还没有登录，也就不能查询余额
            raise TypeError("你还没有登录，请先登录")
        print("下面进入查询页面")
        query_password = input("请输入你的密码：")  # 查询余额，输入密码
        if self.password == query_password:  # 如果输入的密码与注册时的密码相同
            print(f"查询中-----你的余额为：{self.money}元")
        else:
            print("查询失败！")

    def saving(self):
        """
        定义方法：存款，saving
        :return:
        """
        if self.token == False:  # 如果登录状态无效，系统就会报错提示用户还没有登录，也就不能进行存款
            raise TypeError("你还没有登录，请先登录")
        print("下面进入存款页面")
        saving_money = int(input("请输入你的存款金额："))  # 加int 是因为系统上用户的余额要加上存款的余额，系统上的余额是整数类型
        saving_password = input("请输入你的密码：")
        if self.password == saving_password:  # 如果输入的密码与注册时的密码相同
            self.money += saving_money  # 系统余额+存款金额
            print(f"存款成功！你的余额为:{self.money}元")
        else:
            print("存款失败！")

    def get_money(self):
        """
        定义方法：取款，get_money
        :return:
        """
        if self.token == False:  # 如果登录的状态是无效的，系统就会报错提示用户还没有登录，也就不能进行取款
            raise TypeError("你还没有登录，请先登录")
        print("下面进入取款页面")
        get_money = int(input("请输入你的取款金额："))
        get_password = input("请输入你的密码：")
        if self.password == get_password:  # 如果输入的密码与注册时的密码相同
            self.money -= get_money  # 系统余额-存款金额
            print(f"取款成功！你的余额为：{self.money}元")
        else:
            print("取款失败！")

    def find(self):
        """
        定义方法：找回密码，find
        :return:
        """
        print("----------下面进入找回密码页面----------")
        find_id_card = input("请输入你的身份证号码：")
        find_card_num = int(input("请输入你的卡号："))
        if self.id_card == find_id_card and self.card_num == find_card_num:  # 如果用户输入的身份证号和卡号同时与注册时相同
            find_password = input("请输入你的新密码：")  # 设置新密码
            self.password = find_password  # 系统上的密码就变更为用户新设置的密码
            print(f"你的新密码为{self.password}")
        else:
            print("你的身份信息有误，请重新输入")

银行系统 = system()
银行系统.sign_up()
银行系统.login()
银行系统.query()
银行系统.saving()
银行系统.get_money()
银行系统.find()
