class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return round(mean(salary), ndigits = 5)
