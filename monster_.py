from class_ import *
# from main import *
import random


# 몬스터들 부모 클래스
class Monster(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)

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
class JYManager(Monster):
    def __init__(self, name):
        super().__init__(name)
# 기철 매니저님
class KCManager(Monster):
    def __init__(self, name):
        super().__init__(name)
# 영환 매니저님
class YHBossManager(Monster):
    def __init__(self, name):
        super().__init__(name)
# 창호 튜터님
class CHTuter(Monster):
    def __init__(self, name):
        super().__init__(name)
# 민철 튜터님 
class MCTuter(Monster):
    def __init__(self, name):
        super().__init__(name)
# 갓범규님
class GodBK(Monster):
    def __init__(self, name):
        super().__init__(name)

