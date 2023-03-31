import random

#캐릭터 & 몬스터 부모클래스
class BaseCharacter:
    def __init__(self, name):
        self.level = 1
        self.name = name
        self.max_hp = random.randrange(40, 51)
        self.hp = self.max_hp
        self.power = random.randrange(10, 16)
        self.max_mp = random.randrange(40, 51)
        self.mp = self.max_mp
        self.magic_power = random.randrange(10, 16)
        self.experience = 0
        self.money = 0
        self.items = {}

    def cure(self):
        self.hp = self.max_hp
        self.mp = self.max_mp

#############################################################################################

#캐릭터들 부모클래스
class Character(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        pass
    
    # 전투 승리 보상
    def reward(self, other):
        if self.level <= 5:
            print(f"{other.name}(이)가 쓰러졌습니다!")
            if other.money == 0:
                print(f'운이 지지리도 없으시네요! 💰{other.money}머니 획득!\t{self.money-other.money} → {self.money}')
            else:    
                self.money += other.money
                print(f'{self.name}의 돈이 💰{other.money}만큼 올랐습니다!\t{self.money-other.money} → {self.money}')
            self.experience += other.experience
            print(f'{self.name}의 경험치가 🎁{other.experience}만큼 올랐습니다!!\t{self.experience-other.experience} → {self.experience}')
        else:
            print(f"{other.name}(이)가 쓰러졌습니다!")
            self.money += other.money
            print(f'{self.name}의 돈이 💰{other.money}만큼 올랐습니다!\t{self.money-other.money} → {self.money}')
            self.experience += other.experience
            print(f'{self.name}의 경험치가 🎁{other.experience}만큼 올랐습니다!!\t{self.experience-other.experience} → {self.experience}')
    
    
    # TIL 제출 안 하기
    def attack_til(self, other):
        if other.hp != 0:
            other.hp = max(other.hp - self.power, 0)
            print(f"{self.name}의 T.I.L 미제출! {other.name}에게 {self.power}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                self.reward(other)

    # 카메라 끄고 잠수 타기
    def attack_cam_off(self, other):
        if other.hp != 0:
            damage = random.randint(int(self.power), int(self.power*1.1))
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 카메라 끄기!📷 {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                self.reward(other)

    # 지각하기         
    def attack_late(self, other):
        if other.hp != 0:
            damage = random.randint(int(self.power*0.9), int(self.power*1.2))
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 지각! {other.name}에게 정신적 충격! {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                self.reward(other)
    
    #캐릭터 레벨업
    def level_up(self):
        if self.experience >= 500*self.level:
            self.level += 1
            self.max_hp = random.randrange(40, 51)*self.level
            self.hp = self.max_hp
            self.experience -= 500*(self.level-1)
            print(f"레벨이 올랐습니다!\t{self.level - 1} → {self.level} ")

    

    # 아이템 구매
    # 상점에서 아이템을 선택하면, buy_item(self, player, money)을 실행 
    # 플레이어 돈 감소, 아이템 지급
    # other에 무기객체 부여
    def buy_item(self, other): # 아이템 구매
        self.item_name = other.item_name
        
        if self.money < other.price:
            print('금액이 모자랍니다.')
        else:
            self.money -= other.price
            self.power += other.power
            if other.item_name in self.items.keys():
                self.items[other.item_name] += 1  # 이미 있는 아이템이면 수량 추가
            else:
                self.items[other.item_name] = 1  # 새 아이템이면 딕셔너리에 추가
        print(f"{self.name}님의 {other.item_name} 구매가 완료되었습니다! 인벤토리를 여시겠습니까?")
        inven_show = int(input("1.YES / 2.NO    "))
        if inven_show == 1:
            for item_name, self.items[other.item_name] in self.items.items(): # self.items 딕셔너리에 item()로 (키, 값) 형태로 보기
                print("["+item_name, str(self.items[other.item_name])+"개]")
        elif inven_show == 2:
            pass

    # def show_items(self):        
    #     for item_name, quantity in self.items.items(): # self.items 딕셔너리에 item()로 (키, 값) 형태로 보기
    #         print(item_name, str(quantity)+"개")
         
    
    #mp, power, magic_power, speed, experience, level, money
    def show_status(self):
        print(f"{self.name}의 상태: (HP) {self.hp}/{self.max_hp} (MP) {self.mp}/{self.max_mp}")

#############################################################################################

class CrazyCloud(Character):
    def __init__(self, name):
        super().__init__(name)

    def character_skill(self, other):
        if self.mp < 16:
            print(f"💫mp가 부족해 {self.name}의 💫공격이 실패했습니다!")
        else:
            self.mp -= 16
            if other.hp != 0:
                damage = random.randint(self.magic_power, self.level*70)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 줌 강의 마이크 안끄기! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
                print("-----------------------------------------")
                if other.hp == 0:
                    self.reward(other)
        #개인스킬

class GeuNe(Character):
    def __init__(self, name):
        super().__init__(name)
        
    def character_skill(self, other):
        if self.mp < 16:
            print(f"💫mp가 부족해 {self.name}의 💫공격이 실패했습니다!")
        else:
            self.mp -= 16
            if other.hp != 0:
                damage = random.randint(self.magic_power, self.magic_power*2)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 윈드밀! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
                print("-----------------------------------------")
                if other.hp == 0:
                    self.reward(other)
            #개인스킬

class Uni(Character):
    def __init__(self, name):
        super().__init__(name)

    def character_skill(self, other):
        if self.mp < 16:
            print(f"💫mp가 부족해 {self.name}의 💫공격이 실패했습니다!")
        else:
            self.mp -= 16
            if other.hp != 0:
                damage = random.randint(self.magic_power, self.magic_power + 17)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 생츄어리 {other.name}에게 {self.power}의 데미지를 입혔습니다. \n")
                print("-----------------------------------------")
                if other.hp == 0:
                    self.reward(other)
            #개인스킬

class Min(Character):
    def __init__(self, name):
        super().__init__(name)
       
    def character_skill(self, other):
        if self.mp < 16:
            print(f"💫mp가 부족해 {self.name}의 💫공격이 실패했습니다!")
        else:
            self.mp -= 16
            if other.hp != 0:
                damage = random.randint(self.magic_power, self.magic_power + 2)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 블리자드! {other.name}에게 {self.power}의 데미지를 입혔습니다. \n")
                print("-----------------------------------------")
                if other.hp == 0:
                    self.reward(other)
        #개인스킬
        
class Ijh(Character):
    def __init__(self, name):
        super().__init__(name)

    def character_skill(self, other):
        if self.mp < 16:
            print(f"💫mp가 부족해 {self.name}의 💫공격이 실패했습니다!")
        else:
            self.mp -= 16
            if other.hp != 0:
                damage = self.magic_power + (self.level * 100)
                other.hp = max(other.hp - damage, 0)
                print(f"{self.name}의 광선검! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
                print("-----------------------------------------")
                if other.hp == 0:
                    self.reward(other)
        #개인스킬

#############################################################################################

 
