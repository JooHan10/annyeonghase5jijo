from class_ import *


class Seller():
    def __init__(self, name):
        super().__init__(name)
    # 김훈희 무기상 공격 or 스킬 강화
    # 김동우 음식점 음식 먹으면 체력 회복 #체력회복, 버프
    # 최양임 잡화 상인 물약 #물약(전투중 사용가능), 적 디버프 물약, 경험치 물약
        pass

    def buy_item(self, itemname, price): #캐릭터에 들어가야할듯?
        
        if self.money >= price:
            self.money -= price
            inventory[0].append()
        else: 
            print("머니가 부족합니다.")
        pass
    # 상점에서 아이템을 선택하면, buy_item(self, player, money)을 실행 
    # 플레이어 돈 감소, 아이템 지급

#############################################################################################

class Item(): 
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price       
        
    # 아이템 >> 아이템 등급제로 할 것인지? > 인벤토리 구현(쉽지 않음)

    # 1. 능력치만 올려주는 아이템 → 장착?
    # 2. 특정기능이 있는 아이템(디버프 혹은 데미지)
    # 3. 소모품? 1회성 아이템 → 물약
    # 4. 몬스터 죽이면 → 경험치 & 재화

class Weapon(): #무기상
    def __init__(self, name, price, power):
        self.name = "키보드"
        self.price = 500
        self.power = 10
    
        print("어떤 아이템을 구매하시겠습니까? 고기")
        buy_item = int(input("0. :"))
        pass
    "💸"

    def old_cam(self, other):
        # self.weapon_power = 50{}
        other.money = (other.money - self.price)
        other.power = other.power + self.power



class Expendables(): #잡화상인
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    # def 
    #     print("어떤 아이템을 구매하시겠습니까?")
    #     buy_item = int(input("1. :"))
    #     pass

class Oldcam(Weapon):
    def __init__(self, name):
        pass

####################################################################################################

class Inventory():
    def __init__(self):
        self.items = {} # 빈 딕셔너리 생성
    
    # 몬스터 죽으면 나오는 아이템 추가할때 사용
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity # 이미 있는 아이템이면 수량 추가
        else:
            self.items[item_name] = quantity # 새 아이템이면 딕셔너리에 추가
    
    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity # 수량 빼기
                if self.items[item_name] == 0:
                    del self.items[item_name] # 수량이 0이면 딕셔너리에서 아이템 삭제
            else:
                print("삭제하려는 숫자가 아이템의 수보다 많습니다.")
        else:
            print("인벤토리에 아에템 음슴")

my_inventory = Inventory() # 인벤토리 생성
my_inventory.add_item("apple", 3) # "apple" 3개 추가
my_inventory.add_item("banana", 5) # "banana" 5개 추가
print(my_inventory.items) # {'apple': 3, 'banana': 5}

my_inventory.remove_item("apple", 1) # "apple" 1개 제거
print(my_inventory.items) # {'apple': 2, 'banana': 5}

my_inventory.remove_item("banana", 10) # "banana" 10개 제거 (인벤토리에 5개만 있음)
# 출력: "Not enough items to remove."



####################################################################################################

inventory = [[{"name": "검", "power": 5, "price": 100}, {"name": "총", "power": 10, "price": 250}, {"name": "키보드", "power": 15, "price": 500}],
             [{"name":"hp물약", "price":50},{"name":"mp물약", "price":50}]]

# 이름값은 출력하는 용도로 사용됨
item_name = inventory[0][0]["name"] 
# power, price값은 수치 계산에 사용됨
inventory[0][0]["power"]
inventory[0][0]["price"]

weapon = [{"name": "마우스", "power": 5, "price": 100},
          {"name": "키보드", "power": 10, "price": 250},
          {"name": "칼", "power": 15, "price": 500}]
weapon[0]["name"] 
weapon[0]["power"] 

food = [{"name": "고기", "price": 100}]
expendable = [{"name":"hp물약", "price":50}]



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

