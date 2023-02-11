from webapp.state_dir.Not_sleep_state import NotSleepState
from webapp.state_dir.abc_state import State
from webapp.state_dir.dead import Dead
from webapp.state_dir.state_sleep import SleepState


class Cat:
    __state: State

    def __init__(self, name, age, level_happy, level_satiety, state_name):
        self.cat_name = name
        self.cat_age = age
        self.level_happy = level_happy
        self.level_satiety = level_satiety
        self.description = ''
        self.__state = self.change_state(state_name)
        self.__state.set_cat(self)

    def change_state(self, state):
        match state:
            case "sleep":
                self.__state = SleepState()
                self.__state.set_cat(self)
                return SleepState()
            case "not_sleep":
                self.__state = NotSleepState()
                self.__state.set_cat(self)
                return NotSleepState()
            case "dead":
                self.__state = Dead()
                self.__state.set_cat(self)
                return Dead()

    def feed_cat(self):
        self.__state.feed_cat()

    def play_with_the_cat(self):
        self.__state.play_with_the_cat()

    def put_the_cat_to_sleep(self):
        self.__state.put_the_cat_to_sleep()
