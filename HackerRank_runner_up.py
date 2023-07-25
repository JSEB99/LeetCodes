if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    def max_number(arr):
        highest_score = -100
        lista_temp = []
        for number in arr:
            lista_temp.append(number)
            if number>highest_score:
                highest_score = number
        return highest_score,lista_temp
    
    def runner_up_score(highest_score,number_list):
        minimun_number = -100
        for number in number_list:
            if (number>minimun_number) and (number<highest_score):
                minimun_number = number
        return minimun_number
    
    numero_mayor,lista_numeros = max_number(arr)
    print(runner_up_score(numero_mayor,lista_numeros))
    