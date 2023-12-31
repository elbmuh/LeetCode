## 2023.08.09 Wed
## 1672. 가장 부유한 고객의 자산
### **accounts[i][j]** 란, i번째 고객이 j번째 은행에 가지고 있는 금액이다. accounts 정수 **m x n**그리드가 제공된다. 
### 이때, 가장 부유한 고객이 가진 부를 반환한다.
### 고객의 재산은 모든 은행 계좌에 있는 금액이고, 가장 부유한 고객은 최대의 부를 가진 고객이다.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        '''
        # case 1, 2 : Web surfing
        # case 1 : 
        # return sum(max(accounts, key=sum))

        # case 2 :
        # accounts[i][j]
        
        max_wealth = 0

        for i in accounts:
            # index 0, 1, 2 ..번째 리스트 안에 있는 요소들의 총합 구하기 
            max_wealth = max(max_wealth, sum(i))
            
        return max_wealth
        '''

        # case 3 :
        wealth_list = []
        for i in accounts :
            wealth_list.append(sum(i))

        return max(wealth_list)
