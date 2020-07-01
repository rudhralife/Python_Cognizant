# Python_Cognizant
from itertools import permutations, combinations

class Eight_Queen:
    N = 8
    x = range(1, N + 1)


master_list = []
for item in permutations(range(1, N + 1)):
    y = item
    new_list = []
    for x_value, y_value in zip(x, y):
        new_list.append((x_value, y_value))
    master_list.append(new_list)


def IsDiagonal(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    gradient = (y2 - y1) / (x2 - x1)
    if gradient == -1 or gradient == 1:
        return(True)
    else:
        return(False)


solutions = []
for possible_solution in master_list:
    diagonal_clash_list = []
    for piece1, piece2 in combinations(possible_solution, 2):
        diagonal_clash_list.append(IsDiagonal(piece1, piece2))

    if True not in diagonal_clash_list:
        solutions.append(possible_solution)


solutions = [set(solution) for solution in solutions]
list = solutions[0]
final_list = sorted(list,key=lambda seq: seq[0])
# print(final_list)
final_sol = []
for col in final_list:
    x_value,y_value = col
    final_sol.append(y_value)
print(final_sol)

def main():
    obj=Eight_Queen()

if __name__=="__main__":
    main()
