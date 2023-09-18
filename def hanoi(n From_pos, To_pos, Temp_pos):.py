def hanoi(n, From_pos, To_pos, Temp_pos):
    if n == 1:
        print(From_pos, "->", To_pos)
        return
    hanoi(n-1, From_pos, Temp_pos, To_pos)
    print(From_pos, "->", To_pos)
    hanoi(n-1, To_pos, Temp_pos, From_pos)

print("n=3")
hanoi(3,1,3,2)