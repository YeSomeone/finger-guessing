import random

# 出拳
while True:
    options = ['石头', '剪刀', '布']
    computer_choice = random.choice(options)
    user_choice = input('玩家请出拳(石头，剪刀或布)：\n')
    while user_choice not in options:
        user_choice = input('输入有误，请重新出拳：\n')

    # 亮拳
    print('————亮拳————')
    print('电脑出拳：',computer_choice)
    print('玩家出拳：',user_choice)

    # 胜负结果
    print('————结果————')
    user_win = [['石头', '布'], ['剪刀', '石头'], ['布', '剪刀']]
    if computer_choice == user_choice:
        print('平局！')
    elif [computer_choice, user_choice] in user_win:
        print('恭喜你取得胜利！')
    else:
        print('电脑取得了胜利，再接再励啊！')
    go_on = input('还要继续游戏吗？输入Y继续,输入其他结束游戏：\n')
    if go_on != 'Y':
        break
