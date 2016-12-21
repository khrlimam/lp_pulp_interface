import pulp
from NoSolutionException import NoSolutionException


class Solver:
    def __init__(self, problem_name, what_to_do):
        self.problem_name = problem_name
        self.__prob__ = pulp.LpProblem(self.problem_name, what_to_do)

    def constraints(self, list=None, *fks):
        if list is not None:
            fks = list
        for val in fks:
            self.__prob__ += val

    def objective(self, ft):
        self.__prob__ += ft

    def any_solution(self):
        result = self.__prob__.solve()
        try:
            assert result == pulp.LpStatusOptimal
        except AssertionError:
            raise NoSolutionException("Tidak ada solusi!")
