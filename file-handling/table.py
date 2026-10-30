def generate_table(n):

    table = ""

    for i in range(1, 11):
    
        table = table + f"{n} x {i} = {n * i}\n"
    f = open(f"tables/table_of_{n}.txt", "w")
    f.write(table)
    f.close()

for i in range (2,222):
    generate_table(i)
    