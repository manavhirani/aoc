class Solution:
    def __init__(self):
        pass
    
    def is_possible(self, eq: str) -> int | bool:
        value, nums = eq.split(':')
        value = int(value)
        nums = list(nums.split())
        # print(f"Finding if {nums=} can evalute to {value=}")
        # Get operator combinations in increasing orders as a map
        n = len(nums) # Get n - 1 combos, therefore 2^(n-1)
        
        # Binary mask for the operators, 0 = +, 1 = *
        ops = [list(f'{combo:0{n-1}b}') for combo in range(2**(n-1))]
        
        # Now create an expression that foes through the nums and ops
        symbol = {'0':'+', '1':'*', '':''}
        for op in ops:
            expr = '('*n + ' '.join([' '.join([n+')', symbol[o]]) for n, o in zip(nums, op + [''])])
            # print(f'Evaluating {expr} = {eval(expr)}')
            if eval(expr) == value:
                return value
        
        return False
    
    def is_possible_concat(self, eq: str) -> int | bool:
        # print(f'\nIs Possible Concat {eq=}')
        value, nums = eq.split(':')
        nums = list(nums.split())
        # print(f"Finding if {nums=} can evalute to {value=}")
        # Get operator combinations in increasing orders as a map
        
        def ceval(numst) -> str:
            n = len(numst) # Get n - 1 combos, therefore 2^(n-1)
            if n == 1:
                return numst
            # Binary mask for the operators, 0 = +, 1 = *
            ops = [list(f'{combo:0{n-1}b}') for combo in range(2**(n-1))]
            # Now create an expression that foes through the numst and ops
            symbol = {'0':'+', '1':'*', '':''}
            evals = []
            for op in ops:
                expr = '('*n + ' '.join([' '.join([n+')', symbol[o]]) for n, o in zip(numst, op + [''])])
                # print(f'Evaluating {expr} = {eval(expr)}')
                evals.append(str(eval(expr)))
            return evals
        
        for i in range(1, len(nums)):
            left = nums[:i]  
            # print(f"{nums[:i]=}")
            left_evals = ceval(nums[:i])
            print(f"Left evals = {left_evals}")
            for le in left_evals:
                temp = [str(le) + nums[i]] + nums[i+1:]
                print(f"Doing a {str(le)} || {nums[i:]}, using {left_evals}")
                print(temp)
                # print(f"Evaluating {temp=}")
                ctemp = ceval(temp)
                print(ctemp)
                # print(f"{ctemp=}")
                if value in ceval(temp):
                    print("HIT")
                    return int(value)
       
        return False
    
    def callibarate(self, inp: str) -> int:
        total = 0
        equations = inp.splitlines()
        for eq in equations:
            print(f"Solving for {eq=}")
            if (value := self.is_possible(eq)) != False:
                print("Found a value!")
                total += value
        print(f'{total=}')
        return total
    
    def concatenate_callibarate(self, inp: str) -> int:
        total = 0
        equations = inp.splitlines()[:10]
        for eq in equations:
            print()
            print(eq)
            # print(f"\n\nSolving for {eq=}")
            if (value := self.is_possible(eq)) != False:
                # print("Found a value!")
                total += value
            elif (value := self.is_possible_concat(eq)) != False:
                print("Found a value!")
                total += value

        print(f'{total=}')
        return total

if __name__ == '__main__':
    s = Solution()
    
    # test = open('test.in').read()
    # result = s.callibarate(test)
    # assert result == 3749
    
    # final = open('input.in').read()
    # result = s.callibarate(final)
    # print(result)
    
    test = open('test.in').read()
    result = s.concatenate_callibarate(test)
    assert result == 11387
    
    final = open('input.in').read()
    result = s.concatenate_callibarate(final)
    print(result)