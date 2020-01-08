def test_get_century():
    year_to_test = [1701, 19, 1700, 2011, 1200, 403]
    for y in year_to_test:
        century = get_century(y)
        print(f"Année{y} siècle {century}")

    print('- ' * 30)
    year_to_test_with_result = [
        (1701,18), 
        (19,1), 
        (1700,17), 
        (2011,21), 
        (1200,12), 
        (403,5)
    ]
    
    for testy in year_to_test_with_result:
        century = get_century(testy[0])
        if century == testy[1]:
            print(f"Année{testy[0]} siècle {century} : PASSED")
        else:
            print(f"Année{testy[0]} siècle {century} expected {testy[1]} : FAILED")
            raise Exception(F"TEST FAILED with{testy[0]}")


def get_century(date):
    if date > 100:
        century = date % 100
        if century == 0:
            century_birth = date // 100
        else:
            century_birth = date // 100 + 1
    else:
        century_birth = 1
    return century_birth


test_get_century()
