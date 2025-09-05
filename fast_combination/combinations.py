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

        self.total_count = self.binom[n + k - 1][k]
        
        print(self.binom)

    def get_combination(self, index):
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
    
    def get_combinations_range(self, start_index, end_index):
        """
        Получить диапазон сочетаний от start_index до end_index-1
        
        Args:
            start_index: начальный индекс (включительно)
            end_index: конечный индекс (исключительно)
        
        Returns:
            list: список сочетаний
        """
        # Проверка корректности индексов
        if start_index < 0:
            raise ValueError(f"start_index не может быть отрицательным: {start_index}")
        if end_index > self.total_count:
            raise ValueError(f"end_index превышает общее количество: {end_index} > {self.total_count}")
        if start_index >= end_index:
            raise ValueError(f"start_index должен быть меньше end_index: {start_index} >= {end_index}")
        
        results = []
        for index in range(start_index, end_index):
            results.append(self.get_combination(index))
        
        return results



    def get_combinations_range_generator(self, start_index, end_index):
        """
        Генератор для диапазона сочетаний (экономит память)
        
        Args:
            start_index: начальный индекс (включительно)
            end_index: конечный индекс (исключительно)
        
        Yields:
            list: очередное сочетание
        """
        if start_index < 0:
            raise ValueError(f"start_index не может быть отрицательным: {start_index}")
        if end_index > self.total_count:
            raise ValueError(f"end_index превышает общее количество: {end_index} > {self.total_count}")
        if start_index >= end_index:
            raise ValueError(f"start_index должен быть меньше end_index: {start_index} >= {end_index}")
        
        for index in range(start_index, end_index):
            yield self.get_combination(index)