ELEMENT_TYPE_LABEL = 0
ELEMENT_TYPE_BUTTON = 1

class Label:
    def __init__(self, text: str, id: int = -1):
        self.id = id
        self.element_type = ELEMENT_TYPE_LABEL
        self.text = text

class Button:
    def __init__(self, text: str, hookFunction: any = None, id: int = -1):
        self.id = id
        self.element_type = ELEMENT_TYPE_BUTTON
        self.text = text
        self.hookFunction = hookFunction

class ConsoleUI:
    def __init__(self, screen):
        self.buffer = screen
        # index: int, text: str, element_type: int, fun: any
        self.screen_map = []
        self.next_index = 0
    def add_label(self, label: Label):
        label.id = self.next_index
        self.next_index += 1
        self.screen_map.append([label.id, label.text, label.element_type, None])
        return label
    def add_button(self, button: Button):
        button.id = self.next_index
        self.next_index += 1
        self.screen_map.append([button.id, button.text, button.element_type, button.hookFunction])
        return button
    def remove_element(self, index: int):
        for element in self.screen_map:
            if element[0] == index:
                self.screen_map.remove(element)
    def render_element(self, element: list):
       if element[2] == ELEMENT_TYPE_LABEL:
           self.buffer.addstr(element[0], 0, element[1])
       elif element[2] == ELEMENT_TYPE_BUTTON:
           # Add colors here
           self.buffer.addstr(element[0], 0, f"[{element[1]}]")
    def render(self):
        self.buffer.nodelay(True)
        for element in self.screen_map:
            self.render_element(element)
        self.buffer.refresh()