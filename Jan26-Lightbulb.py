class Lightbulb:
    def __init__(self, wattage: int, is_led: bool, brand: str, is_on: bool = False, brightness: int = 0):
        self.wattage = wattage
        self.is_led = is_led
        self.brand = brand
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_string(self):
        print(f'Brand is {self.brand}. Wattage is {self.wattage}.')

    def set_brightness(self, level):
        assert 0 <= level <= 10, 'Level outside bounds'
        self.brightness = level


my_lightbulb = Lightbulb(6, True, 'Phillips')
my_lightbulb.to_string()
