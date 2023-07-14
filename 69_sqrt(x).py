class Solution:
    def mySqrt(self, x: int) -> int:
        """Raíz Cuadrada por Método Babilónico"""
        temporal_x = 0
        temporal_y = 0
        if x == 0:
            return 0
        elif x == 1:
            return 1
        # Buscamos potencia cercana a resultado
        for number in range(x):
            print(number)
            if (number*number)==x:
                sqrt_of_x = number
                return sqrt_of_x
            elif (number*number)>x:
                temporal_x = number
                break
        # Buscamos el rango alto y bajo del número
        temporal_y = temporal_x - 1
        print(temporal_x,temporal_y)
        potencia_x = temporal_x * temporal_x
        potencia_y = temporal_y * temporal_y
        # Averiguamos cual es el más cercano
        x_cercania = abs(x-potencia_x)
        y_cercania = abs(x-potencia_y)
        # Aplicamos fórmula con el más cercano
        if x_cercania<y_cercania:
            sqrt_of_x = (x+potencia_x)/(temporal_x*2)
        elif y_cercania<x_cercania:
            sqrt_of_x = (x+potencia_y)/(temporal_y*2)
        else:
            sqrt_of_x = (x+potencia_x)/(temporal_x*2)
        
        return int(sqrt_of_x)
    
example = Solution()
ans = example.mySqrt(2)
print(ans)

