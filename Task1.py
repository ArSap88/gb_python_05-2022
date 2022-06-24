from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def color_change(self):
        i = 0
        while i < 3:
            print('Current color is: ', TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1
