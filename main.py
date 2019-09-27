from State import State

MAX_STEP = 150


def recur_solotion(state):
    # 猴子拿香蕉4步走：
    # 1. 去箱子（箱子没就位）
    # 2. 搬箱子到香蕉（猴子就位）
    # 3. 站上箱子（箱子就位 猴子就位）
    # 4. 拿到香蕉
    # 然后我们反着看这个过程，就是这个函数的书写顺序了
    # 这个函数将从4到1检查某件事是否可行，满足需求则做
    if len(state) > MAX_STEP:
        print("Can't reach")
        exit(-1)

    if state.monkey_on_box():
        state.grasp()
        state.print_cur_path()
        exit(0)

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
    # 你不输入的话，猴子箱子香蕉就在一起啦！
    recur_solotion(State(monkey=monkey, box=box, banana=banana))
