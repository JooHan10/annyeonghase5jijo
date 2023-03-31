from class_ import *
# from main import *
import random


# 몬스터들 부모 클래스
class Monster(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.power = 6

    def show_status(self):
        print(f"{self.name}의 상태: (HP) {self.hp}/{self.max_hp}")
    
    # 발제
    def attack_homework(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 발제 공격!📜 너의 주말은 없다! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")
    
    # 감시
    def attack_cam(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 감시 공격! 캠을 끌 수 없어!📸 {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")
                
    # 전화
    def attack_call(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 전화 공격!📞 늦잠은 안 돼지! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")
    
    # DM
    def attack_dm(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 DM 공격! 재촉은 내 전문! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")

    # 찐한 관리 / 면담
    def attack_interview(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 면담 공격! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")

    def attack_or_skill(self, other):
        select = random.choice([self.attack_homework, self.attack_cam, self.attack_call, self.attack_dm, self.attack_interview])
        select(other)


# 잡몹
class ErrorMon(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.power = 4
        self.max_hp = random.randint(10, 14)
        self.hp = self.max_hp
            
    # 에러
    def attack_jjob(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 에러 공격! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")

#어? 하는 팀원
class TrollTeammate(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.power = 4
        self.max_hp = random.randint(10, 14)
        self.hp = self.max_hp

    # 웅성웅성대기
    def attack_jjob(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 웅성웅성 공격! 무슨 일이 일어난거지! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")

#르탄이
class Rtani(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.power = 4
        self.max_hp = random.randint(10, 14)
        self.hp = self.max_hp

    # 귀여움
    def attack_jjob(self, other):
        if other.hp != 0:
            damage = random.randint(self.power - 2, self.power + 2)
            other.hp = max(other.hp - damage, 0)
            print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다. \n")
            print("-----------------------------------------")
            if other.hp == 0:
                print(f"{other.name}(이)가 쓰러졌습니다! {self.name}의 승리!")
        
# 지영 매니저님
class JYManager(Monster): # 1-3 Lv
    def __init__(self, name):
        super().__init__(name)
        self.power = 8
        self.max_hp = random.randrange(40, 51)
        self.hp = self.max_hp
        self.experience = 500
        self.money = random.choice([0, 100])

# 기철 매니저님
class KCManager(Monster): # 1-3 Lv
    def __init__(self, name):
        super().__init__(name)
        self.power = 8
        self.max_hp = random.randrange(40, 51)
        self.hp = self.max_hp
        self.experience = 500
        self.money = random.choice([0, 100])

# 영환 매니저님
class YHBossManager(Monster): # 1-3 Lv
    def __init__(self, name):
        super().__init__(name)
        self.power = 12
        self.max_hp = random.randrange(40, 51)
        self.hp = self.max_hp
        self.experience = 500
        self.money = 200

# 창호 튜터님
class CHTuter(Monster): # 4-5 Lv
    def __init__(self, name):
        super().__init__(name)
        self.power = 40
        self.max_hp = random.randrange(70, 81)
        self.hp = self.max_hp
        self.experience = 1000
        self.money = 2000
        
# 민철 튜터님 
class MCTuter(Monster): # 4-5 Lv
    def __init__(self, name):
        super().__init__(name)
        self.power = 40
        self.max_hp = random.randrange(70, 81)
        self.hp = self.max_hp
        self.experience = 1000
        self.money = 2000

# 갓범규님
class GodBK(Monster): # 6 Lv
    def __init__(self, name):
        super().__init__(name)
        self.power = 50
        self.max_hp = 1000
        self.hp = self.max_hp
        self.experience = 100000
        self.money = 10000

        #스킬 자체회복 - 물약 코드스니펫 딸깍
        #