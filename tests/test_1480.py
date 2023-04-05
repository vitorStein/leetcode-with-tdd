from problems.solution_1480 import Solution 

def test_when_array_has_one_value():
    array = [1]
    assert Solution().runningSum(array) == [1]

def test_when_array_has_many_values():
    array = [1,2,3,4]
    assert Solution().runningSum(array) == [1,3,6,10]