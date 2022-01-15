from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        
        
        '''
            Explanation:
                - Two things to understand
                    1. Between characters, there is a difference of one
                    2. There can be rotation in the alphabets (as seen in the case of "zab")

                - We will form a dictionary to help with the grouping.
                    - Key will be the difference between characters and value will be the strings with the distance same as the difference
                        - For distance = 1 going in the positive direction, key = "11"
                        - For distance = 1 going in the reversed direction, key = "-1-1"
                    - Concept of rotation (abc), c + 2
                        - (Length of string + index of c + how much are we moving) % length of string
                        - (3 + 2 + 2) % 3 = 1. Index 1 which is b
        '''