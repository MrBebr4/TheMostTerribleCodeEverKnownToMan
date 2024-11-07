times_num = int(input())
start_time = 3
for i in range(1, times_num + 1):
    for j in range(start_time, 0, -1):
        print(f"До старта {j} секунд(ы)")
    start_time = start_time + 1
    print(f"Старт {i}!!!")
