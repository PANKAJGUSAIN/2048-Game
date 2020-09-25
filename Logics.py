import random

#start function
def start_game():
    mat =[]
    for _ in range(4):
        mat.append([0]*4)
    return mat

#adding '2' randomly
def add_new_2(mat):

    r = random.randint(0,3)
    c = random.randint(0,3)

    while(mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2