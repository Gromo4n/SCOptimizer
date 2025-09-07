class Combinations:
    def __init__(self, n, k):
        if k < 0 or n < 0 or k > n:
            raise ValueError("Invalid parameters: n and k must be non-negative, and k <= n")
        self.n = n
        self.k = k
        self.binom = [[0] * (k + 1) for _ in range(n + k)]
        
        # Вычисление биномиальных коэффициентов
        for i in range(n + k):
            self.binom[i][0] = 1
            for j in range(1, min(i + 1, k + 1)):
                self.binom[i][j] = self.binom[i-1][j-1] + (self.binom[i-1][j] if j <= i-1 else 0)
        
        self.total_count = self.binom[n + k - 1][k]
        print(f"Total combinations: {self.total_count}")  # Отладочная информация

    def get_combination(self, index):
        if index >= self.total_count:
            raise ValueError(f"Index {index} exceeds total number of combinations {self.total_count}")
        
        result = []
        x = index
        n = self.n
        k = self.k
        
        for i in range(k):
            j = 0
            while True:
                # Количество комбинаций, начинающихся с j на текущей позиции
                count = self.binom[n - j + k - i - 1 - 1][k - i - 1] if k - i - 1 > 0 else 1
                if x < count or j >= n - 1:
                    result.append(j)
                    break
                x -= count
                j += 1
                if j >= n:
                    raise ValueError(f"Generated element {j} exceeds valid range [0, {n-1}]")
        
        return result

    def get_combinations_range_generator(self, start_index, end_index):
        if start_index < 0 or end_index > self.total_count or start_index > end_index:
            raise ValueError(f"Invalid range: ensure 0 <= start_index ({start_index}) <= end_index ({end_index}) <= total_count ({self.total_count})")
        
        current = self.get_combination(start_index) if start_index > 0 else [0] * self.k
        yield current[:]
        
        for _ in range(start_index + 1, end_index):
            current = self._next_combination(current)
            yield current[:]

    def _next_combination(self, current):
        result = current[:]
        i = self.k - 1
        while i >= 0 and result[i] >= self.n - 1:
            i -= 1
        if i < 0:
            return result
        result[i] += 1
        for j in range(i + 1, self.k):
            result[j] = result[i]  # Для сочетаний с повторениями следующий элемент равен текущему
        return result