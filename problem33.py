for i in range(10, 100):
    for j in range(10, 100):
        # i/j < 1
        if i >= j:
            continue
        if len(set(list(str(i) + str(j)))) == 3 and not(i % 10 == 0 and j % 10 == 0):


            i_set = set(list(str(i)))
            j_set = set(list(str(j)))

            if len(i_set) == 2 and len(j_set) == 2:


                i2 = int(list((i_set - j_set))[0])
                j2 = int(list((j_set - i_set))[0])



                if j2 > 0 and i/j == i2/j2:
                    print(f"candidate: {i}/{j}", end="")
                    print(f" -> {i2}/{j2}")