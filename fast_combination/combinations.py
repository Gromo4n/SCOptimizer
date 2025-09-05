class Combinations:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.max_val = n + k
        self.binom = [[0] * (self.max_val + 1) for _ in range(self.max_val + 1)]
        
        for i in range(self.max_val + 1):
            self.binom[i][0] = 1
            for j in range(1, i + 1):
                self.binom[i][j] = self.binom[i-1][j-1] + self.binom[i-1][j]
        
        print(self.binom)

    def combination_with_repetition_optimized(self, index):
        """
        Оптимизированная версия для сочетаний с повторениями по индексу
    
        Args:
            index: порядковый номер (0 до C(n+k-1, k)-1)
    
        Returns:
            list: сочетание в виде списка
         """
    
    
        result = []
        x = index
        a = self.n
        b = self.k
    
        for i in range(self.k):
            for j in range(a):
                # Количество сочетаний при выборе элемента j
                count = self.binom[a - j + b - 2][b - 1] if b > 1 else 1
            
                if x < count:
                    result.append(j)
                    a = self.n - j
                    b -= 1
                    break
                else:
                    x -= count
    
        return result