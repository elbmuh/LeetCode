## 2023.08.12 Sat
## 1342. 숫자를 0으로 줄이기 위해 몇 단계가 필요한지의 개수를 세기

class Solution:
    def numberOfSteps(self, num: int) -> int:
        # num == 홀수 -> 1을 빼라
        # num == 짝수 -> 2로 나눠라
        result = 0
        cnt = 0

        while (num > 0) :
            if (num == 1) :
                cnt += 1
                break
            ## num == 1 일 때 멈추지 않으면,
            ## 2개의 if 문에 각각 들어가서 cnt 값이 중복된다. 

            if (num % 2 == 1) :
                num = num - 1
                # print("-1 -> ", end='')
                # print(num)
                cnt += 1

            if (num % 2 == 0) :
                cnt += 1

            result = num / 2
            # print("/2 -> ", end='')
            # print(result)
            num = result
        
        return cnt
        # 마지막 스텝 : 1 - 1 = 0 (cnt += 1)
