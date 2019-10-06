class State():
    def __init__(self, monkey='A', box='B', banana='C', on_box=False):
        '''
        :param monkey:monkey position
        :param box: box position
        :param banana: banana position
        :param on_box: monkey on the box or not(If true, monkey must be in the same position as the box.)
        '''
        self._monkey = monkey
        self._box = box
        self._banana = banana
        if on_box:
            if self._monkey == self._box:
                self._monkey_on_box = on_box
            else:
                raise Exception("Init error, the monkey must be in the same position as the box.")
        else:
            self._monkey_on_box = on_box
        # Record strings according to the solution
        self._path = []

    def __getitem__(self, item):
        return self.cur_state()[item]

    def __len__(self):
        return self.cur_step()

    def __str__(self):
        str1 = 'Monkey at {}. Box at {}. Banana at {}. '.format(self._monkey, self._box, self._banana)
        if self._monkey_on_box:
            str2 = 'Monkey is on the box.'
        else:
            str2 = ''
        return str1 + str2

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
            raise Exception("Invalid call, the monkey is already on box.")
        self._path.append("Monkey climb onto the box.")
        self._monkey_on_box = True

    def climb_down_box(self):
        if not self._monkey_on_box:
            raise Exception("Invalid call, the monkey is not on box.")
        self._path.append("Monkey climb dowm the box.")
        self._monkey_on_box = False

    def grasp(self):
        if not self._monkey_on_box:
            raise Exception('Invalid call, the monkey has not yet climbed the box, try "state().climb_box()"')
        self._path.append("GRASP! Monkey got the banana!")

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
