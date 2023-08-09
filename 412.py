## 2023.08.09 Wed
## 412. 피즈 버즈 (나눗셈 게임)
### 정수 **n**이 주어지면, 문자열 **answer**(_1-indexed_) 을 반환하라.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 3의 배수 -> Fizz 출력
        # 5의 배수 -> Buzz 출력
        # 3과 5의 공배수 -> FizzBuzz 출력

        fizzBuzz = []

        '''
        for i in range(2) :
            i += 1
            fizzBuzz.append(str(i))
        '''

        for i in range(n) :
            i += 1
            if ((i % 3 != 0) and (i % 5 != 0) and (i % 15 != 0)) :
                fizzBuzz.append(str(i))
                continue
            
            if (i % 15 == 0) :
                fizzBuzz.append("FizzBuzz")
                continue

            if (i % 3 == 0) : 
                fizzBuzz.append("Fizz")
                continue

            if (i % 5 == 0) :
                fizzBuzz.append("Buzz")
                continue
            
        return fizzBuzz
