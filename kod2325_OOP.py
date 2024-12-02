"с помощью ООП"
import random
import math
from typing import List, Tuple

# Интерфейс стратегии
class NearestPointStrategy:
    def find_nearest_points(self, points: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        raise NotImplementedError("This method should be overridden.")

# Конкретная стратегия для евклидова расстояния
class EuclideanNearestPointStrategy(NearestPointStrategy):
    def find_nearest_points(self, points: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        result = []
        for i, point in enumerate(points):
            nearest_point = None
            min_distance = float('inf')
            for j, other_point in enumerate(points):
                if i != j:
                    dist = self.distance(point, other_point)
                    if dist < min_distance:
                        min_distance = dist
                        nearest_point = other_point
            result.append((point, nearest_point))
        return result

    def distance(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """Вычисление евклидова расстояния между двумя точками."""
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Конкретная стратегия для манхэттенского расстояния
class ManhattanNearestPointStrategy(NearestPointStrategy):
    def find_nearest_points(self, points: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        result = []
        for i, point in enumerate(points):
            nearest_point = None
            min_distance = float('inf')
            for j, other_point in enumerate(points):
                if i != j:
                    dist = self.distance(point, other_point)
                    if dist < min_distance:
                        min_distance = dist
                        nearest_point = other_point
            result.append((point, nearest_point))
        return result

    def distance(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """Вычисление манхэттенского расстояния между двумя точками."""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Контекст для работы со стратегиями
class PointFinder:
    def __init__(self, strategy: NearestPointStrategy) -> None:
        self.strategy = strategy

    def find_nearest_points(self, points: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        return self.strategy.find_nearest_points(points)

def generate_random_points(n: int) -> List[Tuple[float, float]]:
    """Генерация случайных точек."""
    return [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(n)]

def input_points() -> List[Tuple[float, float]]:
    """Ввод точек вручную."""
    points = input("Введите точки в формате (x1,y1), (x2,y2), ... : ")
    points = points.strip().split('), (')
    points = [tuple(map(float, point.strip('()').split(','))) for point in points]
    return points

def main_menu():
    """Главное меню приложения."""
    while True:
        print("\nМеню:")
        print("1) Генерация случайных точек")
        print("2) Ввод точек вручную")
        print("3) Найти ближайшие точки (евклидово расстояние)")
        print("4) Найти ближайшие точки (манхэттенское расстояние)")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            num_points = int(input("Введите количество случайных точек: "))
            points = generate_random_points(num_points)
            print(f"Сгенерированные точки: {points}")

        elif choice == '2':
            manual_points = input_points()
            print(f"Введенные точки: {manual_points}")

        elif choice == '3':
            if 'points' not in locals() and 'manual_points' not in locals():
                print("Ошибка: Необходимо сначала ввести или сгенерировать точки.")
                continue
            
            current_points = manual_points if 'manual_points' in locals() else points
            
            # Используем стратегию для нахождения ближайших точек по евклидово расстоянию
            strategy = EuclideanNearestPointStrategy()
            finder = PointFinder(strategy)
            results = finder.find_nearest_points(current_points)
            
            for point, nearest in results:
                print(f"Точка {point} ближайшая точка {nearest}")

        elif choice == '4':
            if 'points' not in locals() and 'manual_points' not in locals():
                print("Ошибка: Необходимо сначала ввести или сгенерировать точки.")
                continue
            
            current_points = manual_points if 'manual_points' in locals() else points
            
            # Используем стратегию для нахождения ближайших точек по манхэттенскому расстоянию
            strategy = ManhattanNearestPointStrategy()
            finder = PointFinder(strategy)
            results = finder.find_nearest_points(current_points)
            
            for point, nearest in results:
                print(f"Точка {point} ближайшая точка {nearest}")

        elif choice == '0':
            print("Завершение работы программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
