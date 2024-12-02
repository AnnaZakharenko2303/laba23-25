"без паттерна"
import random
import math

def main():
    points = []
    
    while True:
        print("\nМеню:")
        print("1) Генерация случайных точек")
        print("2) Ввод точек вручную")
        print("3) Найти ближайшие точки")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            num_points = int(input("Введите количество случайных точек: "))
            points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(num_points)]
            print(f"Сгенерированные точки: {points}")

        elif choice == '2':
            user_input = input("Введите точки в формате (x1,y1),(x2,y2): ")
            user_input = user_input.strip().split('),(')
            points = [tuple(map(float, p.strip('()').split(','))) for p in user_input]
            print(f"Введенные точки: {points}")

        elif choice == '3':
            if not points:
                print("Ошибка: Необходимо сначала ввести или сгенерировать точки.")
                continue
            
            results = []
            for i in range(len(points)):
                nearest_point = None
                min_distance = float('inf')
                for j in range(len(points)):
                    if i != j:
                        dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                        if dist < min_distance:
                            min_distance = dist
                            nearest_point = points[j]
                results.append((points[i], nearest_point))
            
            for point, nearest in results:
                print(f"Точка {point} ближайшая точка {nearest}")

        elif choice == '0':
            break

# Пример использования
if __name__ == "__main__":
    main()
