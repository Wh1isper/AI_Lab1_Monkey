from State import State

MAX_STEP = 150

def recur_solotion(state):
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

    recur_solotion(State(monkey="赵家",box="钱家",banana="孙家"))