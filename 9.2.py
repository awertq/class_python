class Show:
    self.hey = ""
    self.robot = ""

    def show_name(self):
        print(self.hey)
        print(self.robot)

list_ = Show
list.hey = "a"
list.robot = "a"
list.show_name()
