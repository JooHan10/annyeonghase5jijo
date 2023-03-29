from class_ import *
from monster_ import *
from shop import *
import time
import sys
import random

while True:
    # 1. 스파르타 던전에 입장합니다
    print("-----------------------------------------")
    print("        스파르타 던전에 입장합니다.        ")
    print("-----------------------------------------")
    print("\n-----------------------------------------")
    player_name = input("사용하실 플레이어 이름을 입력해 주세요.     ")
    print("-----------------------------------------")
    print("직업을 선택하세요.")
    player_select = int(input("1.미친 구름 / 2.그네 / 3.유늬 / 4.민 / 5.좐     "))
    print("-----------------------------------------")


    crazy_cloud = CrazyCloud(player_name)
    geu_ne = GeuNe(player_name)
    uni = Uni(player_name)
    m_i_n = Min(player_name)
    ijh = Ijh(player_name)

    # Characters = {}
    # Characters['uni'] = Character(player_name(uni??????))
    # hp, mp, power, magic_pow

    # 몬스터들 리스트 입니다. 랜덤으로 호출할 때 사용할 겁니다.
    jy_manager = JYManager("지영매니저님")
    ky_manager = KCManager("기철매니저님")
    yh_boss_manager = YHBossManager("영환매니저님")
    ch_tuter = CHTuter("창호튜터님")
    mc_tuter = MCTuter("민철튜터님")
    god_bk = GodBK("갓규")
    


    def random_monster():
        names = random.choice([jy_manager, ky_manager, yh_boss_manager, ch_tuter, mc_tuter, god_bk])
        return names

    monsters = random_monster()

    # monsters = random.choice([jy_manager, ky_manager, yh_boss_manager, ch_tuter, mc_tuter, god_bk])
    # 배틀종료시 if 몬스터 hp가 0: 일때 random으로 다시 몬스터에 할당해주세요

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

    # print("짹짹쨱")
    # print("짹짹쨱")
    # print("짹짹쨱")
    # print(f"게더1: {player_name}용사님 어서 오시죠! 제발 게더 타운에 나타난 몬스터를 무찔러 주세요!")
    # print("게더2: 몬스터들이 주는 과제때문에 미치겠어요!")
    # print("게더3: (멀리서) 그만해~ 이러다..... 다... 죽어~~....")
    # time.sleep(1)
    # print("-----------------------------------------")
    # print("게더 타운을 위해 던전에 입장할까요???")
    enter_or_run = int(input("1.던전 입장 / 2.빤쓰런     "))
    print("-----------------------------------------")
    if enter_or_run == 1:
        enter_or_run_tf = 1

    elif enter_or_run == 2:
        print("..........................................")
        print("빤쓰런 합니다..............🏃‍♂️")
        sys.exit()

    
    while enter_or_run_tf == 1:
        if p_character.hp != 0:
            print("던전에 들어갑니다!\n")
            # time.sleep(0.5)
            # print("^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print(" ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("^   ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print(" ^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^\n")
            # time.sleep(0.5)
            # print(" ^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("^   ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print(" ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^\n")
            # time.sleep(0.5)
            # print("^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print(" ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("^   ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^")
            # print("^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^  ^^^\n")
            # time.sleep(0.5)
            print("모험을 계속할까요? 마을로 갈까요?")
            hunt_or_town = int(input("1.모험 / 2.마을     "))
            if hunt_or_town == 1:
                # time.sleep(0.2)
                # print("!\n")
                # time.sleep(0.5)
                # print("!\n")
                # time.sleep(0.5)
                # print("!\n")
                # time.sleep(0.5)
                print(f"{monsters.name}(이)가 나타났다!\n")
                print("싸울까요??")
                time.sleep(0.5)
                fight_or_run = int(input("1.Yes / 2.No     "))
                print("")
                time.sleep(0.2)
                if fight_or_run == 1:
                    time.sleep(1)
                    print("----------------------------------------- \n")
                    p_character.show_status()
                    monsters.show_status()
                    print("----------------------------------------- \n")
                    time.sleep(1)
                    if p_character.speed >= monsters.speed:
                        first_attack = 1
                    elif p_character.speed < monsters.speed:
                        first_attack = 2

                        # 몬스터 스킬
                        #1. 발제 (매니저 몬스터 공통 스킬)
                        #2. 감시 (카메라 끄면 찾아오기)
                        #3. 전화 (지각하면 깨워주기)
                        #4. DM (TIL 재촉하기)
                        #5. 찐한 관리 / 면담

                    while True:
                        if first_attack == 1:
                            print("플레이어가 더 빠릅니다 어떤 공격을 할까요??")
                            time.sleep(0.5)
                            attack_input1 = int(
                                input("1.몸통박치기 / 2.카메라 끄기!     ")
                            )
                            print("")
                            if attack_input1 == 1:
                                time.sleep(0.5)
                                p_character.attack_cam_off(monsters)
                                if monsters.hp != 0:
                                    time.sleep(0.5)
                                    monsters.attack_homework(p_character)
                                    if p_character.hp != 0 and monsters.hp != 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        print("-----------------------------------------")
                                    elif p_character.hp == 0 or monsters.hp == 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        monsters.cure()
                                        time.sleep(0.5)
                                        print("----------------------------------------- \n")
                                        time.sleep(0.5)
                                        monsters = random_monster()
                                        break
                                elif p_character.hp == 0 or monsters.hp == 0:
                                    time.sleep(0.5)
                                    p_character.show_status()
                                    monsters.show_status()
                                    monsters.cure()
                                    time.sleep(0.5)
                                    print("배틀 종료! \n")
                                    print("----------------------------------------- \n")
                                    time.sleep(0.5)
                                    monsters = random_monster()
                                    break
                            elif attack_input1 == 2:
                                time.sleep(0.5)
                                p_character.attack_til(monsters)
                                if monsters.hp != 0:
                                    time.sleep(0.5)
                                    monsters.attack_homework(p_character)
                                    if p_character.hp != 0 and monsters.hp != 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        print("-----------------------------------------")
                                    elif p_character.hp == 0 or monsters.hp == 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        monsters.cure()
                                        time.sleep(0.5)
                                        print("-----------------------------------------\n")
                                        time.sleep(0.5)
                                        monsters = random_monster()
                                        break
                                elif p_character.hp == 0 or monsters.hp == 0:
                                    time.sleep(0.5)
                                    p_character.show_status()
                                    monsters.show_status()
                                    monsters.cure()
                                    time.sleep(0.5)
                                    print("배틀 종료! \n")
                                    print("-----------------------------------------\n")
                                    time.sleep(0.5)
                                    monsters = random_monster()
                                    break

                        elif first_attack == 2:
                            print("몬스터가 더 빠릅니다. 후공으로 어떤 공격을 할까요??")
                            time.sleep(0.5)
                            attack_input2 = int(
                                input(f"1.몸통박치기 / 2.카메라끄기!     ")
                            )
                            print("")
                            if attack_input2 == 1:
                                time.sleep(0.5)
                                monsters.attack_homework(p_character)
                                if p_character.hp != 0:
                                    time.sleep(0.5)
                                    p_character.attack_cam_off(monsters)
                                    if monsters.hp != 0 and p_character.hp != 0:
                                        time.sleep(0.5)
                                        monsters.show_status()
                                        p_character.show_status()
                                        print("-----------------------------------------")
                                    elif p_character.hp == 0 or monsters.hp == 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        monsters.cure()
                                        time.sleep(0.5)
                                        print("-----------------------------------------\n")
                                        time.sleep(0.5)
                                        monsters = random_monster()
                                        break
                                elif p_character.hp == 0 or monsters.hp == 0:
                                    time.sleep(0.5)
                                    p_character.show_status()
                                    monsters.show_status()
                                    monsters.cure()
                                    time.sleep(0.5)
                                    print("배틀 종료! \n")
                                    print("-----------------------------------------\n")
                                    time.sleep(0.5)
                                    monsters = random_monster()
                                    break
                            elif attack_input2 == 2:
                                time.sleep(0.5)
                                monsters.attack_homework(p_character)
                                if p_character.hp != 0:
                                    time.sleep(0.5)
                                    p_character.attack_til(monsters)
                                    if monsters.hp != 0 and p_character.hp != 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        print("-----------------------------------------")
                                    elif p_character.hp == 0 or monsters.hp == 0:
                                        time.sleep(0.5)
                                        p_character.show_status()
                                        monsters.show_status()
                                        monsters.cure()
                                        print("-----------------------------------------\n")
                                        time.sleep(0.5)
                                        monsters = random_monster()
                                        break
                                elif p_character.hp == 0 or monsters.hp == 0:
                                    time.sleep(0.5)
                                    p_character.show_status()
                                    monsters.show_status()
                                    monsters.cure()
                                    time.sleep(0.5)
                                    print("배틀 종료!\n")
                                    print("-----------------------------------------\n")
                                    time.sleep(0.5)
                                    monsters = random_monster()
                                    break
                elif fight_or_run == 2:
                    time.sleep(0.5)
                    print(".........................................")
                    print(".........................................")
                    print(".................................도망쳤습니다!\n")
                    time.sleep(2)
                    monsters.random_monster()

            elif hunt_or_town == 2: 
                print("마을에 왔습니다! 이제 쉽시다!.")

        elif p_character.hp == 0:
            print("체력을 소진하여 마을에 왔습니다! !.")
            break
        
        
        elif p_character.level > 7: #갓범규 클리어시 무조건 레벨업으로 클리어메시지
            print("스파르타 던전을 클리어하셨습니다.")
            sys.exit()


    # 빤쓰런


    # 2. 1 대 다수의 싸움 방식입니다
    # 3. 각 스테이지의 몬스터와 싸워 이기면 다음 스테이지로 갈 수 있고, 마을에 방문할 수 있습니다
    # 4. 마을에서 각종 아이템을 얻을 수 있습니다
    # 5. 다음 층으로 갈수록 몬스터가 강해집니다
    # 6. 스테이지7의 몬스터와 싸워 이기면 게임이 종료됩니다
    # ===========================================================================
    # 1.마을   2.인벤토리    3.던전
    # 마을 => 1.무기점 2.음식점 3.잡화 4.돌아가기
    # 인벤토리 => 1.장비 2.소비아이템 3. 돌아가기

    # 던전 => 전투 시작 전투함수를 따로 짜서 level값에 따라 등장 몬스터 변경 ex) level 3이하 ~~~// 4~6 // 7일때 갓범규 소환
    # if monster.hp > 0 and player.hp > 0:
    # 무엇을 할까? input
    # (1.캠끄기  2.지각하기 3.TIL안내기) => 기본공격이 3개는 너무 많음(이것도 랜덤으로?). 4.개인스킬 5.사용아이템 6.턴넘기기(디버깅용)
    # 전투 종료시마다 마을 인벤토리 던전 중에 어디로 갈지 선택

    # 1, 4레벨에 몬스터 1마리 / 2,5레벨에 몬스터 2마리 / 3,6 레벨에 몬스터 3마리

    # 7레벨에 갓범규 대표님과의 전투 승리시 엔딩 스토리 출력

    # ============================================================================
