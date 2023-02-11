from webapp.state_dir.abc_state import State


class SleepState(State):
    def feed_cat(self):
        self._cat.description = 'Кот спит'

    def play_with_the_cat(self):
        self._cat.change_state('not_sleep')
        self._cat.level_happy -= 5
        self._cat.description = 'Вы разбудили кота ему это не очень понравилось'

    def put_the_cat_to_sleep(self):
        self._cat.description = 'Дальше только об стену'
