import random

#캐릭터 & 몬스터 부모클래스
class BaseCharacter:
    def __init__(self, name):
        self.name = name
        self.max_hp = random.randrange(40, 51)
        self.hp = self.max_hp
        self.power = random.randrange(10, 16)
        self.max_mp = random.randrange(40, 51)
        self.mp = self.max_mp 
        self.magic_power = random.randrange(10, 16)
        self.speed = random.randrange(6, 9)
        self.experience = 0
        self.level = 1
        self.money = 0

    def cure(self):
        self.hp = self.max_hp
        self.mp = self.max_mp

#############################################################################################

#캐릭터들 부모클래스
class Character(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        pass
    # def __init__(self, name, hp, power, speed, experience):
    #     super().__init__(name, hp, power, speed, experience)
    #     self.max_mp = random.randrange(40, 51)
    #     self.mp = self.max_mp
    #     self.magic_power = random.randrange(40, 51)
    #     self.level = 1
    #     self.money = 0

    
    # TIL 제출 안 하기
    def attack_til(self, other):
        if other.hp != 0:
            other.hp = max(other.hp - self.power, 0)
            print(f"{self.name}의 T.I.L 미제출! {other.name}에게 {self.power}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
                self.money += 500
                print(f'{self.name}의 돈이 {self.money}가 되었습니다!')
                self.experience += 500
                print(f'{self.name}의 경험치가 {self.experience}가 되었습니다!')
                    

    # 카메라 끄고 잠수 타기
    def attack_cam_off(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 카메라 끄기! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
                self.money += 500
                print(f'{self.name}의 돈이 {self.money}가 되었습니다!')
                self.experience += 500
                print(f'{self.name}의 경험치가 {self.experience}가 되었습니다!')

    # 지각하기         
    def attack_late(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 지각! {other.name}에게 정신적 충격! {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다!")
                self.money += 500
                print(f'{self.name}의 돈이 {self.money}가 되었습니다!')
                self.experience += 500
                print(f'{self.name}의 경험치가 {self.experience}가 되었습니다!')
    
    #캐릭터 레벨업
    def level_up(self):
        if self.experience >= 500*self.level:
            self.experience -= 500*self.level
            self.level += 1
            print(f"레벨이 올랐습니다!\t{self.level - 1} → {self.level} ")

    # 아이템 구매
    # 상점에서 아이템을 선택하면, buy_item(self, player, money)을 실행 
    # 플레이어 돈 감소, 아이템 지급
    def buy_item(self, money, price, itemnumber):
        if self.money < price:
            print("f'{self.price - self.money}'금액이 모자랍니다")
        else:
            self.money -= price
   
    def give_item(self, itemnumber):
            pass
    
    #mp, power, magic_power, speed, experience, level, money
    def show_status(self):
        print(f"{self.name}의 상태: (HP) {self.hp}/{self.max_hp} (MP) {self.mp}/{self.max_mp}")

#############################################################################################

class CrazyCloud(Character): # 각각 디폴트값을 주는 것 말고 한번에 각각 클래스에 디폴트를 줄 수 없을까? > 시도해본 것 > 부모클래스에 디폴트 값을 주니 오버라이딩하면서 값을 가져오지 못함...
    def __init__(self, name):
        super().__init__(name)
        self.power = 500
        self.hp = 1
        self.speed = 1
        #개인스킬

class GeuNe(Character):
    def __init__(self, name):
        super().__init__(name)
        
        #개인스킬

class Uni(Character):
    def __init__(self, name):
        super().__init__(name)
        
        #개인스킬

class Min(Character):
    def __init__(self, name):
        super().__init__(name)
       
        #개인스킬
        
class Ijh(Character):
    def __init__(self, name):
        super().__init__(name)
       
        #개인스킬

#############################################################################################

 
