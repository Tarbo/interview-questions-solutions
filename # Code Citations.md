# Code Citations

## License: unknown
https://github.com/jeremypruitt/learnings/tree/efc495f53b0c07a2c39ac541fc9bf12e662e421f/leetcode/334-IncreasingTripletSubsequence.md

```
Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
```

