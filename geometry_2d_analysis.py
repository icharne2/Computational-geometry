import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"x= {self.x} y= {self.y}")


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_line(self):
        if self.b == 0:
            print(f"Równanie linii: y= {round(self.a, 3)} * x")
        elif self.b < 0:
            print(f"Równanie linii: y= {round(self.a, 3)} * x {self.b}")
        else:
            print(f"Równanie linii: y= {round(self.a, 3)} * x + {self.b}")


def create_point_from_user_input():
    x = float(input("Podaj współrzędną x punktu: "))
    y = float(input("Podaj współrzędną y punktu: "))

    return Point(x, y)


def create_line_from_user_input():
    a = float(input("Podaj wartość współczynnika kierunkowego a: "))
    b = float(input("Podaj wartość wyrazu wolnego b:  "))

    return Line(a, b)


def create_line(point1, point2):
    a = (point1.y - point2.y) / (point1.x - point2.x)
    b = point1.y - (a * point1.x)

    return Line(a, b)


def plot_line(point1, point2):
    plt.plot([point1.x, point2.x], [point1.y, point2.y], '-')
    plt.xlabel('Współrzędna X')
    plt.ylabel('Współrzędna Y')
    plt.title('Równanie linii')
    plt.show()


def lineage_affiliation(point, line):
    if point.y == ((line.a * point.x) + line.b):
        return True
    else:
        return False


def which_side(point, line):
    result = point.y - (line.a * point.x + line.b)

    if result > 0:
        print("Punkt leży po lewej stronie prostej")
    elif result < 0:
        print("Punkt leży po prawej stronie prostej")
    else:
        print("Punkt leży na prostej")


def show_lineage_affiliatio(point, line):
    x_values = np.array([point.x - 5, point.x + 5])
    y_values = line.a * x_values + line.b

    plt.plot(x_values, y_values, '-')
    plt.scatter(point.x, point.y, color='red', label='Punkt', marker='x')
    plt.xlabel('Współrzędna X')
    plt.ylabel('Współrzędna Y')
    plt.title('Przynależność punktu do linii')
    plt.legend()
    plt.show()


def plot_line_segment(point_start, point_end, ptr):
    plt.scatter(ptr.x, ptr.y, color='red', label='Punkt', marker='x')
    plt.plot([point_start.x, point_end.x], [point_start.y, point_end.y], marker='o')
    plt.xlabel('Współrzędna X')
    plt.ylabel('Współrzędna Y')
    plt.title('Rysowanie odcinka')
    plt.legend()
    plt.show()


def point_in_line_segment(point, segment_start, segment_end):
    # Czy współrzędne punktu są pomiędzy współrzędnymi punktów odcinka
    x_min = min(segment_start.x, segment_end.x)
    x_max = max(segment_start.x, segment_end.x)
    y_min = min(segment_start.y, segment_end.y)
    y_max = max(segment_start.y, segment_end.y)

    if x_min <= point.x <= x_max and y_min <= point.y <= y_max:
        # Orientację punktu względem odcinka
        orientation = (point.x - segment_start.x) * (segment_end.y - segment_start.y) - (point.y - segment_start.y) * (
                segment_end.x - segment_start.x)
        # Ze wzoru: (y-y1)(x2-x1)-(y2-y1)(x-x1)=0

        if orientation == 0:
            print("Punkt leży na odcinku")
        elif orientation < 0:
            print("Punkt leży po lewej stronie odcinka")
        elif orientation > 0:
            print("Punkt leży po prawej stronie odcinka")
        else:
            print("Punkt nie leży na odcinku")
    else:
        print("Punkt nie leży na odcinku")

    # Translacja o wektor


def translate(pkt_line_start, pkt_line_end, vector):
    pkt_line_start.x += vector.x
    pkt_line_start.y += vector.y

    pkt_line_end.x += vector.x
    pkt_line_end.y += vector.y

    return create_line(pkt_line_start, pkt_line_end)


def reflect_point(point, line):
    m = line.a  # współczynnik kierunkowy prostej

    x_prime = ((1 - m ** 2) * point.x + 2 * m * point.y - 2 * m * line.b) / (1 + m ** 2)
    y_prime = (2 * m * point.x + (m ** 2 - 1) * point.y + 2 * line.b) / (1 + m ** 2)

    reflected_point = Point(x_prime, y_prime)
    return reflected_point


def show(point, point2, line):
    x_values = np.array([point.x - 5, point.x + 5])
    y_values = line.a * x_values + line.b

    plt.plot(x_values, y_values, '-')
    plt.scatter(point.x, point.y, color='red', label='Punkt pierwotny', marker='x')
    plt.scatter(point2.x, point2.y, color='blue', label='Punkt odbity', marker='o')
    plt.xlabel('Współrzędna X')
    plt.ylabel('Współrzędna Y')
    plt.title('Odbicie punktu wzgledem linii')
    plt.legend()
    plt.show()


def main():
    print("Menu Lab_01:")
    print("1. Wyznaczenie równania prostej, do której należy dana linia.")
    print("2. Sprawdzenie przynależności punktu do prostej.")
    print("3. Sprawdzenie przynależności punktu do linii (odcinka).")
    print("4. Określenie położenia punktu względem prostej (prawo/lewo).")
    print("5. Dokonanie translacji linii o podany wektor.")
    print("6. Dokonanie odbicia danego punktu względem linii.")

    option = input("Wybierz opcje: ")
    if option == "1":
        point_a = create_point_from_user_input()
        point_b = create_point_from_user_input()

        line_1 = create_line(point_a, point_b)
        line_1.print_line()

        plot_line(point_a, point_b)

    elif option == "2":
        point = create_point_from_user_input()
        line = create_line_from_user_input()

        if lineage_affiliation(point, line):
            print("Punkt nalezy do linii :>")
        else:
            print("Punkt nie należy do linii :<")

        show_lineage_affiliatio(point, line)
    elif option == "3":
        # Aby sprawdzić, czy punkt należy do odcinka linii musimy mieć dwa punkty,
        # które ograniczają linie

        print("Dla odcinka:")
        point_start = create_point_from_user_input()
        point_end = create_point_from_user_input()

        print("Punkt dla którego sprawdzamy, czy należy na odcinku")
        ptr = create_point_from_user_input()

        point_in_line_segment(ptr, point_start, point_end)
        plot_line_segment(point_start, point_end, ptr)

    elif option == "4":
        point = create_point_from_user_input()
        line = create_line_from_user_input()

        which_side(point, line)
        show_lineage_affiliatio(point, line)
    elif option == "5":
        # Tworzenie linii
        point_start = create_point_from_user_input()
        point_end = create_point_from_user_input()
        line = create_line(point_start, point_end)

        print("Linia przed translacja.")
        line.print_line()
        plot_line(point_start, point_end)

        print("Wsporzedne wektora na podstawie, ktorego wykonujemy translacje")
        ptr = create_point_from_user_input()

        # Translacja
        line = translate(point_start, point_end, ptr)

        print("Linia po translacji.")
        line.print_line()
        plot_line(point_start, point_end)

    elif option == "6":
        print("Linia względem którem dokonujemy odbicia")
        line = create_line_from_user_input()

        print("Punkt, który odbijamy")
        ptr = create_point_from_user_input()
        ptr2 = reflect_point(ptr, line)

        show(ptr, ptr2, line)

    else:
        print("Nieprawiodłowy wybór :<")


if __name__ == "__main__":
    main()
