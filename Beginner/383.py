## 2023.08.14 Mon
## 383. 랜섬 노트
### 두 문자열 ransomNote 와 magazine 이 주어졌을 때,
### 만약 ransomNote 가 magazine 으로부터 그 문자들을 사용하 구성될 수 있을 때, true 값을 반환하고 그렇지 않다면 false 값을 반환하라.
### magazine 에 있는 각 문자는 ransomNote에서 오직 한 번만 사용될 수 있다.

# ======= case 01 =======
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_maz = dict()
        for s in magazine : 
            dict_maz[s] = dict_maz.get(s, 0) + 1
        
        for s in ransomNote : 
            if s not in dict_maz : 
                return False
            if dict_maz[s] == 0 : 
                return False
            
            dict_maz[s] -= 1
        
        return True




# ======= case02 =======
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ran = collections.Counter(ransomNote)
        dict_maz = collections.Counter(magazine)

        for key, value in dict_ran.items() : 
            if key not in dict_maz or value > dict_maz[key] : 
                return False
        
        return True




# ======= case 03 =======
class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    dict_ran = colletions.Counter(ransomNote)
    dict_maz = colletions.Counter(magazine)

    for key, value in dict_ran.items():
      if key not in dict_maz or value > dict_maz[key]:
        return False

    return True




# ======= case 04 ======= (출처 : 호놀률루 / 매일을 꿈틀대는 법)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## ransomNote : 여기에서 글자들을 추출한다.
        ## magazine : 추출한 글자들을 자신이 원하는 단어 형태로 만든다.
        global num

        ransomNote_list = list(ransomNote)
        magazine_list = list(magazine)

        if len(ransomNote_list) > len(magazine_list) :
            return False
        else : 
            for i in range(0, len(ransomNote_list)) : 
                for j in range(0, len(magazine_list)) : 
                    num = 1

                    if ransomNote_list[i] == magazine_list[j] : 
                        num -= 1
                        magazine_list.pop(j)
                        break

                if num == 1 :
                    break

        if num == 1 :
            return False
        
        else : 
            return True
