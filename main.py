from State import State

MAX_STEP = 150


def recur_solotion(state):
    '''
    利用产生式系统解决问题。
    （1）定义综合数据库（M, B, Box, On, H）
    其中：
    M: 猴子的位置
    B: 香蕉的位置
    Box: 箱子的位置
    On = 0: 猴子在地板上
    On = 1: 猴子在箱子上
    H = 0: 猴子没有抓到香蕉
    H = 1: 猴子抓到了香蕉
    （2） 初始状态：（a, c, b, 0, 0）
    （3） 结束状态：（c, c, c, 1, 1）
    （4） 规则集：
    r1: IF(x, y, z, 0, 0)
    THEN(w, y, z, 0, 0)（猴子移动xw）
    r2: IF(x, y, x, 0, 0)
    THEN(z, y, z, 0, 0)（猴子推箱子xz）
    r3: IF(x, y, x, 0, 0)
    THEN(x, y, x, 1, 0)（猴子爬箱子）
    r4: IF(x, y, x, 1, 0)
    THEN(x, y, x, 0, 0)（猴子下箱子）
    r5: IF(x, x, x, 1, 0)
    THEN(x, x, x, 1, 1)（猴子抓香蕉）
    其中， x, y, z, w
    为变量。
    解答：设猴子位置为A，箱子位置为B，香蕉位置在C
    根据具体问题可将规则具体为：
    r1: IF(a, c, b, 0, 0)
    THEN(b, c, b, 0, 0)
    r2: IF(b, c, b, 0, 0)
    THEN(c, c, c, 0, 0)
    r3: IF(b, c, b, 0, 0)
    THEN(b, c, b, 1, 0)
    r3: IF(c, c, c, 0, 0)
    THEN(c, c, c, 1, 0)
    r4: IF(b, c, b, 1, 0)
    THEN(b, c, b, 0, 0)
    r5: IF(c, c, c, 1, 0)
    THEN(c, c, c, 1, 1)
    在已知事实下，r1r2r3r5, 可得到香蕉
    '''

    if len(state) > MAX_STEP:
        print("Can't reach")
        exit(-1)

    if state.monkey_on_box():
        if state.box_in_position():
            state.grasp()
            print("----------Solution----------")
            state.print_cur_path()
            print("----------Solution----------", end='')
            exit(0)
        else:
            state.climb_down_box()
            recur_solotion(state)

    if state.box_in_position():
        if state.monkey_in_box_position():
            if not state.monkey_on_box():
                state.climb_box()
                recur_solotion(state)
            else:
                recur_solotion(state)
        else:
            state.monkey_goto(state["box"])
            recur_solotion(state)
    else:
        if state.monkey_in_box_position():
            state.monkey_push_box_to(state["banana"])
            recur_solotion(state)
        else:
            state.monkey_goto(state["box"])
            recur_solotion(state)


if __name__ == '__main__':
    monkey = input("猴子猴子在哪里？")
    box = input("箱子箱子在哪里？")
    banana = input("香蕉香蕉在哪里？")
    on_box = False
    if monkey == box:
        on_box = input("猴子在箱子上吗？(有输入则视作在箱子上)")
        if on_box != '':
            on_box = True
        else:
            on_box = False
    if monkey != '' and box != '' and banana != '':
        state = State(monkey=monkey, box=box, banana=banana, on_box=on_box)
    else:
        print("有空输入，不算数哦")
        print("只好听我的，猴子在A，香蕉在B，箱子在C")
        state = State()
    print(state)
    recur_solotion(state)
