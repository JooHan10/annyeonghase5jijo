from class_ import *
from monster_ import *
from shop import *
import time
import sys
import random

player_name = input("사용하실 플레이어 이름을 입력해 주세요.     ")
print("직업을 선택하세요.")
player_select = int(input("1.미친 구름 / 2.그네 / 3.유늬 / 4.민 / 5.좐     "))

crazy_cloud = CrazyCloud(player_name)
geu_ne = GeuNe(player_name)
uni = Uni(player_name)
m_i_n = Min(player_name)
ijh = Ijh(player_name)

if player_select == 1:
    p_character = crazy_cloud
elif player_select == 2:
    p_character = geu_ne
elif player_select == 3:
    p_character = uni
elif player_select == 4:
    p_character = m_i_n
elif player_select == 5:
    p_character = ijh
    
# 몬스터들 리스트 입니다. 랜덤으로 호출할 때 사용할 겁니다.

# 잡몹
errormon = ErrorMon("에러몬")
uhteamate = TrollTeammate("어? 하는 팀원")
rtani = Rtani("르탄이")

# 매니저몬
jy_manager = JYManager("지영매니저님")
kc_manager = KCManager("기철매니저님")
yh_boss_manager = YHBossManager("영환매니저님")

# 튜터몬
ch_tuter = CHTuter("창호튜터님")
mc_tuter = MCTuter("민철튜터님")

# 보스
god_bk = GodBK("갓규")

# 아이템    
knife = Knife()
old_cam = OldCam()
keyboard = Keyboard()

# 던전 => 전투 시작 전투함수를 따로 짜서 level값에 따라 등장 몬스터 변경 ex) level 3이하 ~~~// 4~6 // 7일때 갓범규 소환
# if monster.hp > 0 and player.hp > 0:
# 무엇을 할까? input
# (1.캠끄기  2.지각하기 3.TIL안내기) => 기본공격이 3개는 너무 많음(이것도 랜덤으로?). 4.개인스킬 5.사용아이템 6.턴넘기기(디버깅용)
# 전투 종료시마다 마을 인벤토리 던전 중에 어디로 갈지 선택

# 1, 4레벨에 몬스터 1마리 / 2,5레벨에 몬스터 2마리 / 3 레벨에 몬스터 3마리

# 6 레벨에 갓범규 대표님과의 전투 승리시 엔딩 스토리 출력

manager_mon = None


def random_manager_monster():
    if p_character.level <= 3:
        manager_monsters_names = random.choice([jy_manager, kc_manager, yh_boss_manager])
    elif p_character.level <= 5:
        manager_monsters_names = random.choice([ch_tuter, mc_tuter])
    else:
        manager_monsters_names = god_bk
    return manager_monsters_names

def random_jjob_monster():
    if p_character.level <= 5:
        jjob_monsters_names = random.sample([errormon, uhteamate, rtani], 2)
        return jjob_monsters_names
    else:
        jjob_monsters_names = random.sample([errormon, uhteamate, rtani], 0)

# monsters 변수 안에 [random 값1, random 값2, random 값3] 들어있음.
manager_mon = random_manager_monster()
jjob_monsters = random_jjob_monster()

# manager_mon = manager_mon
if p_character.level <= 5:
    jjob_mon1 = jjob_monsters[0]
    jjob_mon2 = jjob_monsters[1]


# print(manager_mon.name, jjob_mon1.name, jjob_mon2.name)
# monsters = random.choice([jy_manager, ky_manager, yh_boss_manager, ch_tuter, mc_tuter, god_bk])
# 배틀종료시 if 몬스터 hp가 0: 일때 random으로 다시 몬스터f에 할당해주세요



# 전투당 적정 공격 횟수?
# 

# 레벨별로 적정 전투 횟수?
# 1-3 Lv : 
# 4-5 Lv : 5-6번?
# 레벨별로 경험치가 다른데 괜찮을지? > 몬스터가 주는 경험치량을 늘려서 해결해보죠
# 

# 캐릭터 회복 기능이 없음..
# > 마을로 가면 회복? Yes ok

# 몬스터가 hp !=0 일 동안 전투
# 


enter_or_run = int(input("1.마을 입장 / 2. 게임 종료     "))
if enter_or_run == 1:
    enter_or_run_tf = 1

elif enter_or_run == 2:
    print("빤쓰런 합니다 🏃‍♂️~~~")
    sys.exit()

while enter_or_run_tf == 1:
    if p_character.level <= 6:
        if p_character.hp != 0:
            print("마을에 들어갑니다!\n")

            print("던전에 입장할까요?")
            hunt_or_town = int(input("1.Yes / 2.No     "))
            if hunt_or_town == 1: # 던전
                def status_all(): # 상태 보여주기
                    time.sleep(0.5)
                    p_character.show_status()
                    manager_mon.show_status()
                    if p_character.level <= 6:
                        jjob_mon1.show_status()
                        jjob_mon2.show_status()
                    
                def battle(): # 전투
                    global manager_mon
                    if p_character.hp != 0 and manager_mon.hp != 0:
                        status_all()

                        print("-----------------------------------------")
                    elif p_character.hp == 0 or manager_mon.hp == 0:
                        time.sleep(0.5)
                        p_character.level_up()
                        status_all()
                        time.sleep(0.5)
                        print("배틀 종료! \n")
                        print("-----------------------------------------\n")
                        time.sleep(0.5)
                        

                def after_attack(): #몬스터 공격
                    if manager_mon.hp != 0:
                        time.sleep(0.5)
                        manager_mon.attack_or_skill(p_character)
                        if p_character.level <= 6:
                            jjob_mon1.attack_jjob(p_character)
                            jjob_mon2.attack_jjob(p_character)
                        battle()
                    else:
                        battle()

                def mon_appear():
                    if p_character.level <= 5:
                        print(f"{manager_mon.name}(이)가 {jjob_mon1.name}, {jjob_mon2.name}와(과) 함께 나타났다!")
                    else:
                        print("게더에 어두운 기운이 느껴진다.....")
                        print(f"{manager_mon.name}가 등장했다!!!!!")

                mon_appear()
                print("싸울까요??")
                time.sleep(0.5)
                fight_or_run = int(input("1.Yes / 2.No     "))
                print("")
                time.sleep(0.2)
                if fight_or_run == 1:
                    status_all()
                    time.sleep(1)                
                    
                    while manager_mon.hp != 0 and p_character.hp !=0:                       
                        print("어떤 공격을 할까요??")
                        attack_input1 = int(input("1.카메라 끄기! / 2. T.I.L 미제출! / 3. 지각 / 4. 스킬     "))
                        print("")
                        if attack_input1 == 1:
                            time.sleep(0.5)
                            p_character.attack_cam_off(manager_mon)
                            after_attack()

                        elif attack_input1 == 2:
                            time.sleep(0.5)
                            p_character.attack_til(manager_mon)
                            after_attack()
                            
                        elif attack_input1 == 3:
                            time.sleep(0.5)
                            p_character.attack_late(manager_mon)
                            after_attack()
                            
                        elif attack_input1 == 4:
                            time.sleep(0.5)
                            p_character.character_skill(manager_mon)
                            after_attack()
                            
                        else:
                            print("잘못된 입력입니다.")
                            continue

                    if p_character.level <= 6:
                        manager_mon = random_manager_monster()
                        manager_mon.cure()    
                    if p_character.level <= 5:
                        jjob_mon1.cure()
                        jjob_mon2.cure()   
                        
                elif fight_or_run == 2:
                    time.sleep(0.5)
                    print("도망쳤습니다!\n")
                    time.sleep(2)
                    manager_mon = random_manager_monster()
                else:
                    print("잘못된 입력입니다.")
                    continue

            elif hunt_or_town == 2: # 마을
                print("마을에 왔습니다! 상점을 이용하시겠습니까?")
                service_select = int(input("1.아이템상점 / 2.휴식하기 / 3.무기상점     "))
                if service_select == 1:
                    print("아이템상점에 들어왔습니다! 어떤 아이템을 구매하시겠습니까?")
                    print(f"현재 보유하신 {p_character.name}님의 머니는 {p_character.money}입니다!")
                    item_select = int(input("1.검(450) / 2.낡은 캠(2500) / 3.키보드(10000)     "))
                    if item_select == 1:
                        p_character.buy_item(knife)
                    elif item_select == 2:
                        p_character.buy_item(old_cam)
                    elif item_select == 3:
                        p_character.buy_item(keyboard)
                elif service_select == 2: 
                    print("적절한 휴식은 필수.\nhp와 mp가 max로 회복되었습니다!")
                    p_character.cure()
                elif service_select == 3:                    
                    print("무기상점은 공사중입니다...\n연락주시면 바로 오겠습니다. -🚒내배캠119🚨")
                    continue
                else:
                    print("잘못된 입력입니다.")
                    continue
                    
        elif p_character.hp == 0:
            print("체력을 소진하였습니다! !.")
            p_character.cure()
            continue
    
    elif god_bk.hp == 0: #갓범규 클리어시 무조건 레벨업으로 클리어메시지
        print("스파르타 던전을 클리어하셨습니다!🎊")
        sys.exit()

