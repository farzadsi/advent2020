class Play:

    def __init__(self, input_list):
        self.game_memroy = {number: i+1 for i, number in enumerate(input_list[:-1])}
        self.new_memory = [input_list[-1], len(input_list)]
        # self.last_num = input_list[-1]
        self.last_state = 1 # 1 first time, 0 repeat
        self.turn = len(input_list)

    def next_turn(self):
        self.turn += 1
        if self.new_memory[0] in self.game_memroy.keys():
            age = self.new_memory[1] - self.game_memroy[self.new_memory[0]]
            self.game_memroy.update({self.new_memory[0]: self.new_memory[1]})
            self.new_memory = [age, self.turn]
            return age
        else:
            self.game_memroy.update({self.new_memory[0]: self.new_memory[1]})
            self.new_memory = [0, self.turn]
            return 0

new_play = Play([11, 0, 1, 10, 5, 19])

while True:
    new_play.next_turn()
    if new_play.turn == 30000000:
        print('the word spoken was', new_play.new_memory[0])
        break

print('happy happy')

