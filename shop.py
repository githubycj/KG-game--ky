def shop1():
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
            import KG游戏
            KG = KG游戏
            print(KG)
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
            import KG游戏
            KG = KG游戏
            print(KG)
    elif a == "tui":
        import KG游戏
        KG = KG游戏
        print(KG)
    else:
        print("请输入正确的选择")
        import KG游戏
        KG = KG游戏
        print(KG)
