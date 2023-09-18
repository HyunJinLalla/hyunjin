def hanoi(n, From_pos, To_pos, Temp_pos):    
    if n == 1:
        print(From_pos, "->", To_pos)
        return
    hanoi(n-1, From_pos, Temp_pos, To_pos)
    print(From_pos, "->", To_pos)
    hanoi(n-1, Temp_pos, To_pos, From_pos)

def print_hanoi_steps(num_discs):
    print("Solving the Tower of Hanoi with", num_discs, "disc(s):")
    hanoi(num_discs, 1, 3, 2)

print_hanoi_steps(3)
print("\n")