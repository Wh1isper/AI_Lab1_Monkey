class State():
    def __init__(self, monkey='A', box='B', banana='C'):
        self._monkey = monkey
        self._box = box
        self._banana = banana
        self._monkey_on_box = False
        self._path = []

    def print_current_state(self):
        print('Monkey at {}.'.format(self._monkey, end=', '))
        print('Box at {}.'.format(self._box, end=', '))
        print('Banana at {}.'.format(self._banana))

    def monkey_goto(self, v):
        self._path.append("Monkey from {} go to {}.".format(self._monkey, v))
        self._monkey = v

    def monkey_push_box_to(self, w):
        if self._monkey != self._box:
            raise Exception("Input error, monkey must go to {} first.".format(w))
        self._path.append("Monkey push box from {} to {}.".format(self._box, w))
        self._box = w
        self._monkey = w

    def climb_box(self):
        if self._monkey != self._box:
            raise Exception("Invalid call, the monkey must be in the same position as the box.")
        if self._monkey_on_box:
            raise Exception("Invalid call, the monkey is already in box.")
        self._path.append("Monkey climb onto the box.")
        self._monkey_on_box = True

    def grasp(self):
        if not self._monkey_on_box:
            raise Exception('Invalid call, the monkey has not yet climbed the box, try "state().climb_box()"')
        self._path.append("Monkey got the banana!")

    def print_cur_path(self):
        for s in self._path:
            print(s)

    def cur_step(self):
        return len(self._path)

    def cur_state(self):
        return {
            "monkey": self._monkey,
            "banana": self._banana,
            "box": self._box,
            "monkey_on_box": self._monkey_on_box
        }

    def box_in_position(self):
        return self._box == self._banana

    def monkey_in_box_position(self):
        return self._monkey == self._box

    def monkey_on_box(self):
        return self._monkey_on_box

    def __getitem__(self, item):
        return self.cur_state()[item]

    def __len__(self):
        return self.cur_step()
