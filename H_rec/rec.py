from math import log
from design_patterns.decorator.timer_function import timer
from crack.C_queue.stack import MyStack
from decimal import Decimal

def fibunacci(n, li):
    print(n, li)
    if n < len(li):
        return li[n]
    else:
        res = fibunacci(n-1, li) + fibunacci(n-2, li)
        li.append(res)
        return res


def step_combinations(n):
    combinations = 0
    for step_size in range(1,4):
        new_element = n - step_size
        
        if new_element == 0:
            combinations += 1
        elif new_element > 0:
            combinations += step_combinations(new_element)
    return combinations



grid = [
    [0,1,0,0,1],
    [0,0,1,1,1],
    [0,0,0,0,0]
]

def robot_in_a_grid(grid, x, y):
    print(x,y)

    if y == len(grid) - 1 and x == len(grid[y]) - 1:
        return ([(x,y)], 1)
    else:
        fields = []
        if y < len(grid) - 1:
            fields.append((x, y+1))
        if x < len(grid[y]) - 1:
            fields.append((x+1, y))
        
        optimal_path = ([(0,0)],100000000)

        for field in fields:
            if grid[y][x] == 0:
                next_path = robot_in_a_grid(grid, field[0],  field[1])
                print(next_path)
                if next_path[1] < optimal_path[1]:
                    optimal_path = next_path
                    return ([(x,y)] + optimal_path[0], optimal_path[1]+1)




def magic_index(arr, start):
    middle_index = int(len(arr)/2)
    middle = arr[middle_index]
    if middle == start + middle_index:
        return (True, middle)
    else:
        if middle > middle_index + start:
            return magic_index(arr[:middle_index], start)
        else:
            return magic_index(arr[middle_index+1:], start+middle_index+1)



def subsets(dataset):
    result = []
    datalist = list(dataset)

    for x in range(0, len(datalist)):
        for y in range(x, len(datalist)):
            if x == y:
                result.append([datalist[x]])
            else:
                result.append([datalist[x],datalist[y]])
                if (y-x) > 1:
                    result.append(datalist[x:y+1])
    return result + [[]]

@timer
def multiply_simple(x,y):
    return multiply(x,y)

def multiply(x,y):
    if y > 1:
        x += multiply(x, y-1)
    return x


@timer
def mulitply_bit(x,y):
    exp = log(y,2)
    multiplicated_with_exp = x << int(exp)
    remainder = y - (2**int(exp))
    return multiplicated_with_exp + multiply(x, remainder)



def towers_of_hanoi(n):
    keys = ['a','b','c'] 
    towers = { element:MyStack(n+1) for element in keys }
    for element in range(1,n+1):
        towers['a'].push(element)
    
    def solve(n, from_rod, to_rod, aux_rod):
        if n == 1:
            temp = towers[from_rod].pop()
            towers[to_rod].push(temp)
        else:
            solve(n-1, from_rod ,aux_rod, to_rod)
            temp = towers[from_rod].pop()
            towers[to_rod].push(temp)
            solve(n-1, aux_rod, to_rod, from_rod)

    solve(n, 'a', 'b', 'c')

    print([str(towers[e]) for e in towers])


def permutations(st):
    final_permutations = []
    st_list = list(st)

    if len(st_list) == 1:
        return [st_list]
    else:
        for index, character in enumerate(st_list):

            new_list = st_list.copy()
            new_list.pop(index)
            new_permutations = permutations("".join(new_list))
            for new_permutation in new_permutations:
                final_permutations.append([character]+new_permutation)
        return final_permutations

def permutations_with_dups(st):
    st_list = list(st)
    st_set = set(st_list)
    st_list = list(st_set)
    print(st_list)
    return permutations("".join(st_list))

@timer
def parens(n):

    if n == 1:
        return ["()"]
    else:
        final_combinations = []
        new_combinations = parens(n-1)
        for new_combination in new_combinations:
            new_creations = ["()"+new_combination, new_combination+"()", "("+new_combination+")"]
            for new_creation in new_creations:
                if new_creation not in final_combinations:
                    final_combinations.append(new_creation)
        return final_combinations

def paint_fill(screen, new_color, r, c):
    paint_fill_worker(screen, new_color, screen[r][c], r, c)

def paint_fill_worker(screen, new_color, old_color, r, c):
    screen[r][c] = new_color
    surrounding_coordinates = [[r-1, c-1], [r-1, c], [r-1, c+1], [r, c+1], [r, c-1], [r+1, c-1], [r+1, c], [r+1, c+1]]
    surrounding_coordinates = [coordinate for coordinate in surrounding_coordinates if coordinate[0] >= 0 and coordinate[0] < len(screen) and coordinate[1] >= 0 and coordinate[1] < len(screen[0])]
    for coordinate in surrounding_coordinates:
        if screen[coordinate[0]][coordinate[1]] == old_color:
            paint_fill_worker(screen, new_color, old_color, coordinate[0], coordinate[1])

@timer
def comb_of_cents(n):
    return comb_of_cents_worker(n)

def comb_of_cents_worker(n):
    solutions = []
    possibilities = [25, 10, 5]
    for possibility in possibilities:
        if possibility == n:
            solutions.append([n])
        else:
            if n - possibility >= 0:
                new_possibilities = []
                new_n = n - possibility
                new_possibilities = comb_of_cents_worker(new_n)
                for new_possibility in new_possibilities:
                    solutions.append([possibility] + new_possibility)
    return solutions


@timer
def comb_of_cents_dynamic(n):
    return comb_of_cents_worker_dynamic(n, {})

def comb_of_cents_worker_dynamic(n, solution_map):

    solutions = []
    possibilities = [25, 10, 5]
    for possibility in possibilities:
        if possibility == n:
            solutions.append([n])
        else:
            if n - possibility >= 0:
                new_possibilities = []
                new_n = n - possibility
                if new_n in solution_map:
                    new_possibilities = solution_map[new_n]
                else:
                    new_possibilities = comb_of_cents_worker_dynamic(new_n, solution_map)
                    solution_map[new_n] = new_possibilities
                for new_possibility in new_possibilities:
                    solutions.append([possibility] + new_possibility)
    return solutions

def tower_setup():
    class Box:
        def __init__(self, width, height, depth):
                super().__init__()
                self.width = width
                self.height = height
                self.depth = depth
        def __str__(self):
                return "width: "+str(self.width)+" height: "+str(self.height)+" depth: "+str(self.depth)
    boxes = [
                Box(1,1,1),
                Box(1,2,1),
                Box(2,2,2),
                Box(3,3,3),
                Box(4,4,4)
            ]
    
    return create_tower(boxes)


def create_tower(boxes):
    sorted_boxes = sorted(boxes, key=lambda box: box.height)
    stack = [box for i, box in enumerate(sorted_boxes) if sorted_boxes[i].width > sorted_boxes[i-1].width and sorted_boxes[i].depth > sorted_boxes[i-1].depth and i > 0]
    # for i in range(0, len(sorted_boxes) - 1):
    #     print(i)
    #     if not sorted_boxes[i].width < sorted_boxes[i+1].width and not sorted_boxes[i].depth < sorted_boxes[i+1].depth:
    #         sorted_boxes.pop(i)
    #         i -= 1
    return stack

if __name__ == "__main__":
    # print(">>>", fibunacci(5, [0,1]))
    # print("final: ", step_combinations(4))
    # print(">>>", robot_in_a_grid(grid, 0,0))
    # print(magic_index([-10,1,20,30,40,50,60], 0))
    # print(magic_index([-10,-5,-1,0,1,2,3,7,10], 0))
    # print(subsets({1,2,3,4}))
    # print(multiply_simple(2,900))
    # print(mulitply_bit(2,900))
    # towers_of_hanoi(10)
    # print(permutations("abcde"))
    # print(permutations("abcdeee"))
    # print(sorted(permutations("abcde")) == sorted(permutations_with_dups("abcdeee")))
    # print(parens(10))

    # screen = [
    #     [0,0,1,1,1],
    #     [0,1,0,0,0],
    #     [0,1,1,1,1],
    #     [0,1,1,1,0],
    #     [0,0,1,1,0],
    #     [0,0,0,0,0],
    # ]


    # paint_fill(screen, 5, 3, 3)
    # print(screen)
    # comb_of_cents(150)
    # comb_of_cents_dynamic(150)
    print([str(e) for e in tower_setup()])

