from random import randint

from webapp.state_dir.abc_state import State


class NotSleepState(State):
    def feed_cat(self):
        self._cat.level_satiety += 15
        if self._cat.level_satiety > 100:
            self._cat.level_happy -= 30
            self._cat.description = 'Кот перекормлен'
        else:
            self._cat.level_happy += 5
            self._cat.description = 'Кот покормлен'

    def play_with_the_cat(self):
        if self._cat.level_satiety > 30:
            if randint(1, 3) == 2:
                self._cat.level_happy = 0
                self._cat.level_satiety -= 10
                self._cat.description = 'кот дурканул и пришёл в ярость'
            else:
                self._cat.level_happy += 15
                self._cat.level_satiety -= 10
                self._cat.description = 'вы поиграли с котом'
        else:
            self._cat.level_happy += 15
            self._cat.level_satiety -= 10
            self._cat.description = 'вы поиграли с котом'

    def put_the_cat_to_sleep(self):
        self._cat.change_state('sleep')
