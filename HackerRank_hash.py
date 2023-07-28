try:
    def stringtointegers(container: list)->list:
        container_integers = []
        for stringnumber in container:
            container_integers.append(int(stringnumber))
        return container_integers

    n = int(input("n: "))
    container = input().split()
    if len(container) != n:
        raise ValueError("Incorrect number of elements")
    else:
        correct_container = stringtointegers(container)
        
except ValueError:
    print("intente nuevamente...\n")
    container = input().split()
    correct_container = stringtointegers(container)
finally:
    print(hash(tuple(correct_container)))



    