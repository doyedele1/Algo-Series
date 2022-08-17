# Create a hash map of the number and the resulting steps. {1: 0, 5: 5, 16: 4, 8: 3, 4: 2, 2: 1}
# Store the resulting steps in an array
# Pop the resulting steps from the end of the array and store the numbers as key of the hash map and increasing steps as value of the hash map
# Return the value of the key passed which is the input number

class CollatzConjecture:
    def solution(n):
        cache = { 1: 0 } # n: steps
        start = n # 5
        steps = [] # [5, 16, 8, 4, 2]

        while start != 1:
            if start in cache: break

            steps.append(start)

            if (start % 2 == 0): start //= 2

            else: start = (3 * start) + 1
        # print steps ==> [5, 16, 8, 4, 2]

        totalSteps = cache.get(start, 0) + 1
        # print totalSteps ==> 1

        while steps:
            curr = steps.pop()
            cache[curr] = totalSteps
            totalSteps += 1
        # print cache => {1: 0, 2: 1, 4: 2, 8: 3, 16: 4, 5: 5}

        return cache[n]

# print(CollatzConjecture.solution(100))