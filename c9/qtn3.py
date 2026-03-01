def generate(n):
    table=""
    for i in range(1,11):
        table=f"{n} X {i} = {n*i}"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)
    print('Tables generated successfully')

for n in range(2,21):
    generate(n)