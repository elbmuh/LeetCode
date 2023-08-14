
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
