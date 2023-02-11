from webapp.state_dir.abc_state import State


class Dead(State):
    def feed_cat(self):
        self._cat.description = 'Кот умер'

    def play_with_the_cat(self):
        self._cat.description = 'Кот умер'

    def put_the_cat_to_sleep(self):
        self._cat.description = 'Кот умер'
