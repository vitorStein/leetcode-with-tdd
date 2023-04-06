from problems.solution_724 import Solution 

def test_when_array_has_many_values():
    array = [1,7,3,6,5,6]
    assert Solution().pivotIndex(array) == 3

def test_when_array_has_no_pivot():
    array = [1,2,3]
    assert Solution().pivotIndex(array) == -1

def test_when_array_has_no_pivot_2():
    array = [2,1,-1]
    assert Solution().pivotIndex(array) == 0