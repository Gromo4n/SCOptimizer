class Combinations:
    def __init__(self):
        pass

    def combination_with_repetition_optimized(self, n, k, index):
        """
        Оптимизированная версия для сочетаний с повторениями по индексу
    
        Args:
            n: количество элементов (0 до n-1)
            k: размер сочетания
            index: порядковый номер (0 до C(n+k-1, k)-1)
    
        Returns:
            list: сочетание в виде списка
         """
        # Предвычисляем биномиальные коэффициенты
        max_val = n + k
        binom = [[0] * (max_val + 1) for _ in range(max_val + 1)]
    
        for i in range(max_val + 1):
            binom[i][0] = 1
            for j in range(1, i + 1):
                binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
    
        result = []
        x = index
        a = n
        b = k
    
        for i in range(k):
            for j in range(a):
                # Количество сочетаний при выборе элемента j
                count = binom[a - j + b - 2][b - 1] if b > 1 else 1
            
                if x < count:
                    result.append(j)
                    a = n - j
                    b -= 1
                    break
                else:
                    x -= count
    
        return result