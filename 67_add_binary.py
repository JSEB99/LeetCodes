class Solution:
    def addBinary(self, a: str, b: str) -> str:
        reverse_a,reverse_b = a[::-1],b[::-1]
        sum_of_binary = []
        added_num = 0
        # las volteo pa sumar de derecha a izquierda
        length_a = len(reverse_a)
        length_b = len(reverse_b)
        # igualo las cadenas
        if length_a>=length_b:
            while length_b!=length_a:
                reverse_b+="0"
                length_b = len(reverse_b)
        elif length_b>=length_a:
            while length_a!=length_b:
                reverse_a+="0"
                length_a = len(reverse_a)
        for number in range(len(reverse_a)):
            # 1 + 1 = 10
            if (int(reverse_a[number])+int(reverse_b[number])==2):
                if added_num == 1:
                    # 1 + 1 + 1 = 11
                    if (int(reverse_a[number])+int(reverse_b[number])+added_num == 3):
                        sum_of_binary.append('1')
                        added_num = 1
                else:
                    # 1 + 1 = 10
                    sum_of_binary.append('0')
                    added_num = 1
            elif (int(reverse_a[number])+int(reverse_b[number])==1):
                if added_num == 1:
                    # 1 + 1 = 10
                    if (int(reverse_a[number])+int(reverse_b[number])+added_num == 2):
                        sum_of_binary.append('0')
                        added_num = 1
                else:
                    # 1 + 0 = 1
                    sum_of_binary.append('1')
                    added_num = 0
            elif (int(reverse_a[number])+int(reverse_b[number])==0):
                if added_num == 1:
                    # 1 + 0 = 1
                    if (int(reverse_a[number])+int(reverse_b[number])+added_num == 1):
                        sum_of_binary.append('1')
                        added_num = 0
                else:
                    # 0
                    sum_of_binary.append('0')
        # si existe acarreo
        if added_num == 1:
            sum_of_binary.append('1')
        # conversión en cadena
        binary_sum = "".join(sum_of_binary[::-1])
        print(binary_sum)
        
example = Solution()
example.addBinary("1111","1111")