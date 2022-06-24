import Task1
import Task2
import Task3
import Task4
import Task5

print('Task 1:')
TrafficLight = Task1.TrafficLight()
TrafficLight.color_change()
print('End of Task 1.\n\nTask 2:')

asphalt_needed = Task2.Road()
print(f'Amount of asphalt needed is: {asphalt_needed.RoadMass(25, 5) / 1000} tons')
print('End of Task 2.\n\nTask 3:')

worker_data = Task3.Position('Arman', 'Sapinskiy', 'Cook', wage=300000, bonus=10500)
print(f'Mr/Mrs {worker_data.get_full_name()} '
      f'works as {worker_data.position} '
      f'and earns {worker_data.get_total_income()} per month')
print('End of Task 3.\n\nTask 4:')

police = Task4.PoliceCar(speed=70, color='Police', name='Ford Police Interceptor', is_police=True)
sport_car = Task4.SportCar(speed=120, color='Yellow', name='McLaren F1', is_police=False)
work_car = Task4.WorkCar(speed=59, color='White', name='Ford Transit', is_police=False)
town_car = Task4.TownCar(speed=59, color='Gray', name='Ravon R3', is_police=False)
print(f'{police.stop()}\n{sport_car.turn("left")}\n{work_car.show_speed()}\n{town_car.show_speed()}')
print('End of Task 4.\n\nTask 5:')

pen = Task5.Pen()
pencil = Task5.Pencil()
handle = Task5.Handle()
print(f'{pen.draw()}\n{pencil.draw()}\n{handle.draw()}\nEnd of Task 5')
