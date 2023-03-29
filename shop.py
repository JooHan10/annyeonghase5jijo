from class_ import *


class Seller():
    def __init__(self, name):
        super().__init__(name)
    # 김훈희 무기상 공격 or 스킬 강화
    # 김동우 음식점 음식 먹으면 체력 회복 #체력회복, 버프
    # 최양임 잡화 상인 물약 #물약(전투중 사용가능), 적 디버프 물약, 경험치 물약
        pass

    def buy_item(self, itemnumber, price): #캐릭터에 들어가야할듯?
        
        if self.money >= price:
            self.money -= price
            inventory[0].append()
        else: 
            print("돈이 모자랍니다.")
        pass
    # 상점에서 아이템을 선택하면, buy_item(self, player, money)을 실행 
    # 플레이어 돈 감소, 아이템 지급


    
#############################################################################################
class Item(): 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Weapon(): #무기상
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
        print("어떤 아이템을 구매하시겠습니까? 고기")
        buy_item = int(input("0. :"))
        pass


class Expendables(): #잡화상인
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        print("어떤 아이템을 구매하시겠습니까?")
        buy_item = int(input("1. :"))
        pass



inventory = [[],[]] 
weapon = []
food = []
expendable = []
    # inventory = [[장비 아이템 리스트],[소모품 리스트]] 
    # 1.장비 2.소모품 3.돌아가기
    # 1. inventory[0] 2. inventory[1] 3. 돌아가기

    # 상점 공통
    # self.buy_item(itemnumber)
    #

    # 무기점 weapon = [{name:무기1, stat:power, amount:1},
    #                 {name:무기2, stat:power, amount:1},
    #                 {name:무기3, stat:power, amount:1},
    #                 {name:무기4, stat:power, amount:1}
    #                ] or 아이템을 각각 클래스화 해서 아이템.hp
    # 1. a무기(가격) 2.b무기(가격) 3.c무기(가격) 4.d무기(가격) 5.f무기(가격)   => 무기 1번만 먼저 만들어서 되는지 확인
    #


    # 음식점 food = [음식1, 음식2, 음식3, 음식4 ...]
    # 1. 음식1(hp,mp회복) 2.음식2(mp) 3.음식3(max_hp) 4.음식4(강화버프 등등)    => 버프, 디버프류, 연막탄은 다른거 다 만들고 나중에 추가)
    # 바로 그 자리에서 효과 적용
    # eat_food(음식1) => p_character.hp = p_character.max_hp //

    # 잡화점 expendable = [hp물약, mp물약, 연막탄 ...]
    # use
    # 1. hp물약 2.mp물약 3.연막탄(도망=>마을 인벤 던전 선택창) 4.힘 물약(이번 전투 힘 증가)    => 버프, 디버프류, 연막탄은 다른거 다 만들고 나중에 추가)

