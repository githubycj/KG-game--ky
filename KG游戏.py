# xiugou游戏,制作者YCJ
import time
import random

print("欢迎来到KG游戏")
name = input("请输入你的昵称:")
namex = open("./data/user/name.txt", "w")
namex.write(name)
namex.close()
print("欢迎,", name)
print("======KG游戏======")
print("1<开始游戏>2<保存存档>3<退出游戏>4<打开商店>5<插件-mod> |实验玩法-联机>>>| 6<创建联机房间>7<加入联机房间>")
xuanze = input("做出你的选择:")
if xuanze == "1":
    print("加载中...")
    time.sleep(2)
    print("加载成功,正在进入!")
    print("[", name, "]", "|你的血量为[100]|你的攻击力为100~150(武器加成不算入)")
    xue = 100
    bossxue = 300
    time.sleep(1)
    print("前方出现目标!")
    print("|目标名称:boss|血量:300|攻击力:10~40之间|")
    while True:
        bossgong = random.randint(10, 40)
        namegong = random.randint(100, 150)
        print("boss对你发起了进攻")
        xue = xue - bossgong
        if xue <= 0:
            print("你失败了")
            print("-程序将在5秒后自动退出-")
            time.sleep(5)
        else:
            print("你的血量剩余为", xue)
            print("boss的血量剩余为", bossxue)
            namefan = input("按下a即可反击")
            if namefan == "a":
                print("正在反击...")
                jiacheng = open("./data/game/cundang.txt", "r")
                jiacheng1 = jiacheng.read()
                jiacheng = open("./data/game/cundang1.txt", "r")
                jiacheng2 = jiacheng.read()
                if jiacheng1 == "1":
                    print("正在使用烈火大刀...")
                    namegong = namegong + 50
                    print("你使用烈火大刀对boss造成伤害", namegong)
                    bossxue = bossxue - namegong
                    if bossxue <= 0:
                        print("你获胜了!!!")
                        print("-程序将在10秒后自动退出-")
                        print("本次收益10金币")
                        shouyi = open("./data/game/jinbi.txt", "r")
                        sy = shouyi.read()
                        sy = int(sy)
                        shouyi.close()
                        shi = 10
                        sy = sy + shi
                        sy2 = str(sy)
                        shouyi1 = open("./data/game/jinbi.txt", "w")
                        shouyi1.write(sy2)
                        shouyi1.close()
                        time.sleep(10)
                        break
                elif jiacheng2 == "1":
                    print("正在使用普通大刀...")
                    namegong = namegong + 10
                    print("你使用普通大刀对boss造成伤害", namegong)
                    bossxue = bossxue - namegong
                    if bossxue <= 0:
                        print("你获胜了!!!")
                        print("-程序将在10秒后自动退出-")
                        print("本次收益10金币")
                        shouyi = open("./data/game/jinbi.txt", "r")
                        sy = shouyi.read()
                        sy = int(sy)
                        shouyi.close()
                        shi = 10
                        sy = sy + shi
                        sy2 = str(sy)
                        shouyi1 = open("./data/game/jinbi.txt", "w")
                        shouyi1.write(sy2)
                        shouyi1.close()
                        time.sleep(10)
                        break
                else:
                    print("你对boss造成伤害", namegong)
                    bossxue = bossxue - namegong
                    if bossxue <= 0:
                        print("你获胜了!!!")
                        print("-程序将在10秒后自动退出-")
                        print("本次收益10金币")
                        shouyi = open("./data/game/jinbi.txt", "r")
                        sy = shouyi.read()
                        sy = int(sy)
                        shouyi.close()
                        shi = 10
                        sy = sy + shi
                        sy2 = str(sy)
                        shouyi1 = open("./data/game/jinbi.txt", "w")
                        shouyi1.write(sy2)
                        shouyi1.close()
                        time.sleep(10)
                        break
            else:
                print("你选择不攻击")
                time.sleep(1)
elif xuanze == "2":
    print("保存中...")
    time.sleep(3)
    print("保存成功!")
elif xuanze == "3":
    exit()
elif xuanze == "4":
    # 商店系统请勿更改代码,制作者:YCJ
    print("欢迎光临")
    jinbiliang = open("./data/game/jinbi.txt", "r")
    i = jinbiliang.read()
    print("您的金币总量为:", i)
    print("请问您要买什么?")
    print("1{烈火大刀-100金币-伤害增加50},2{普通大刀-50金币-伤害增加10},tui[退出商店]")
    a = input("做出你的选择")
    if a == "1":
        b = open("./data/game/jinbi.txt", "r")
        s = b.read()
        s = int(s)
        manei = 100
        b.close()
        if s >= manei:
            print("购买中")
            s1 = s - manei
            f = open("./data/game/jinbi.txt", "w")
            s1 = str(s1)
            f.write(s1)
            f.close()
            print("购买成功")
            e = open("./data/game/cundang.txt", "w")
            e.write("1")
            e.close()
        else:
            print("你的金币不足,可以通过打boss获得")
    elif a == "2":
        b = open("./data/game/jinbi.txt", "r")
        s = b.read()
        s = int(s)
        manei1 = 50
        b.close()
        if s >= manei1:
            print("购买中")
            s1 = s - manei1
            f = open("./data/game/jinbi.txt", "w")
            s1 = str(s1)
            f.write(s1)
            f.close()
            print("购买成功")
            e = open("./data/game/cundang1.txt", "w")
            e.write("1")
            e.close()
        else:
            print("你的金币不足,可以通过打boss获得")
    elif a == "tui":
        exit()
    else:
        print("请输入正确的选择")
elif xuanze == "5":
    print("本插件为默认插件可以进行修改")
elif xuanze == "6":
    try:
        import socket

        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 协议

        duan = int(input("自定义房间号(1024~65535)[纯整数!]:"))
        sk.bind(('127.0.0.1', int(duan)))
        # 监听联机请求
        sk.listen(8)  # 半连接池
        print("开房成功!等待玩家进入,房间号为[", duan, "]")
        # 取出联机请求,开始联机
        conn, addr = sk.accept()
        print(conn, "加入了联机房间")
        print("对方ip+端口", addr)
        print("现在属于聊天房间,开始游戏请等待对面发送一条消息...")
        while True:
            # 数据传输
            data = conn.recv(1024)
            data = data.decode('utf-8')
            print("对面发来的消息:", data)
            mydata = input("给对面发送的消息(输入/play即可开始游戏)(输入/ban踢出玩家):")
            if mydata == "/play":
                conn.send('/playx'.encode('utf-8'))
                print("游戏开始")
                while True:
                    woxue = 100
                    print("你的血量为", woxue, "攻击力为[10~50]")
                    xgong = input("按下a即可向对面攻击:")
                    if xgong == "a":
                        sk.send("/bg".encode('utf-8'))
                        xg = random.randint(10, 50)
                        print("你对对面造成", xg, "点攻击")
                        duixue = "你剩余血量", woxue - xg
                        duixue = str(duixue)
                        sk.send(duixue.encode('utf-8'))
                        data = conn.recv(1024)
                        dxue = data.decode('utf-8')
                        if dxue == "/si":
                            print("你胜利了!")
                            break
                        else:
                            data = conn.recv(1024)
                            dxue = data.decode('utf-8')
                            print(dxue)
                            dxue = int(dxue)
                            dxue = dxue[5:7]
                            woxue1 = woxue - dxue
                            if woxue1 <= 0:
                                print("你失败了")
                                sk.send("/si".encode('utf-8'))
                                break
            elif mydata == "/ban":
                conn.close()  # ban玩家
            else:
                conn.send(mydata.encode('utf-8'))  # 发送消息
    except ValueError:
        print("出现错误!")
elif xuanze == "7":
    import socket

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 协议
    # 创建连接
    duan1 = input("请输入房间号:")
    sk.connect(('127.0.0.1', int(duan1)))
    while True:
        neirong = input("输入你要发送的内容:")
        sk.send(neirong.encode('utf-8'))
        print("等待对方回复...")
        data = sk.recv(1024)
        print("对方发来的消息:", data.decode('utf-8'))
        if data == "/playx":
            print("游戏开始")
            print("你的血量为[100]攻击力为[10~50]")
        else:
            neirong = input("输入你要发送的内容:")
            sk.send(neirong.encode('utf-8'))
            print("等待对方回复...")
            print("对方发来的消息:", data.decode('utf-8'))
else:
    print("请输入正确的选择:)")
