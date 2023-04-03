import random
import os  # os.system('cls')
import time
from tqdm import tqdm

print('Now Loading...', '\n')
for i in tqdm(range(100)):  # tqdm 첫 번째 인자에 순회가능한 객체 전달
    time.sleep(0.01)

# 캐릭터부모 클래스
# 캐릭터 공통 스탯: 체력, 공격력, 회피력, 체력재생력


class Character:
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        self.name = name

        # 소모용
        self.hp = hp  # 체력
        self.mp = mp  # 마나
        self.eng = eng  # 기력

        # 고정스탯
        self.atk = atk  # 공격력
        self.int_ = int_  # 지능/주문력
        self.def_ = def_  # 방어력
        self.agi = agi  # 민첩/회피율
        self.vit = vit  # 체력재생력
        self.rst = rst  # 기력재생력
        self.rem = rem  # 마나재생력
        Character.skills = []
        self.level = level
        self.exp = exp
        # 레벨

    # 레벨시스템

    def character_level(self):
        self.exp += 50
        if self.exp % 100 == 0:
            self.level += 1
            self.hp += self.hp*0.1
            self.atk += self.atk*0.1
            self.def_ += self.def_*0.1

        # 공격함수

    def attack(self, target):
        while True:
            print("어떤 공격을 할까?")
            for i, skill in enumerate(self.skills):
                print(f"{i+1}: {skill.__name__}")  # 스킬 번호와 이름 출력
            try:
                choice = int(input()) - 1  # 스킬 번호 입력 받기 (인덱스는 0부터 시작하므로 1을 뺌)
                if 0 <= choice < len(self.skills):
                    selected_skill = self.skills[choice]  # 선택한 스킬의 함수 객체 가져오기
                    selected_skill(target)  # 선택한 스킬 사용하기
                    break  # 올바른 스킬을 선택했으므로 루프를 빠져나감
                else:
                    print("얘! 숫자 읽을줄 모르니?")
            except ValueError:
                print("오타 검지검지~")

# 캐릭터 종류============================================================================
# 체육쌤 (꼴초) - 흙, 불속성


class PEteacher(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)

        self.skills = [self.call_of_dust, self.cigarett_fire]

    def status(self):
        current_status = {
            '이름': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp)
        }
        for key, value in current_status.items():
            print(key, value, sep=':')

    # 먼지나게 맞아볼래

    def call_of_dust(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk  # 수치조정으로 밸런스
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄

        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        if target.name == ElecMonster:  # 변수명 수정
            damage += self.atk*0.2
        elif target.name == WindMonster:
            damage -= self.atk*0.2
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

            # 담배빵

    def cigarett_fire(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk*0.4  # 수치조정으로 밸런스
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄

        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        if target.name == WindMonster:   # 변수명 수정
            damage += self.atk*0.2
        elif target.name == WaterMonster:    # 변수명 수정
            damage -= self.atk*0.2
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 흙속성 - 먼지나게 맞자
        # 불속성 - 라이터로 지지기

        # 캐릭터 종류============================================================================
        # 몸짱 공익 - 노멀
        # 자가회복 - 벌크업!! 2. 일반공격 - 몸통박치기
        # 기력소모


class AgentP(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)

        self.skills = [self.thatbam, self.body_crash, self.mashjeong]

    def status(self):
        current_status = {
            '이름': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp),
            'ENG': self.eng
        }
        for key, value in current_status.items():
            print(key, value, sep=':')

    # 딱밤(댓뱀)
    def thatbam(self, target):
        damage = self.atk*0.5  # 수치조정으로 밸런스조정
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
# 몸통박치기

    def body_crash(self, target):
        if self.eng <= 0:
            print('기력이 없어서 일반공격으로')
            return
        damage = self.hp*0.15  # 수치조정으로 밸런스조정
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        self.eng -= 100
        print('100 기력사용!')
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 마시쩡

    def mashjeong(self, target):
        if self.eng <= 0:
            print('기력이 없어서 일반공격으로')
            return
        self.eng -= 70
        print('70 기력사용!')
        effect = self.eng*0.3
        self.hp += effect
        self.eng += self.rst
        print(f'이기적인녀석 자신의 체력을 {effect}만큼 회복했다!')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 캐릭터 종류============================================================================
        # 바리스타 - 물 속성


class Barista(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)
        self.skills = [self.all_heal, self.final_cleaning]

    def status(self):
        current_status = {
            '이름': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp)
        }
        for key, value in current_status.items():
            print(key, value, sep=':')

        # 전체회복 - hp 기준 20% 회복  - > 카페인 충전
    def all_heal(self, target):

        print(f'커피로 카페인을 충전하여 모두가 체력의 20%만큼 회복했다!')
        buff = self.hp*0.2
        for i in character:
            i.hp += 30
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {buff}만큼 체력을 회복했다.')
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 일반공격: 마감청소 ㅠㅠㅠ; 공익 몸통박치기와 로직동일, 수치만 바꿨기에 후에 검토할것!!
    def final_cleaning(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk*1.3  # 몸통박치기에서 체력계수 없애고 공격력계수로 수정했음
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄

        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 캐릭터 종류============================================================================
        # 지식채널 유튜버 - 노멀, 기력소모


class KnowledgeYoutuber(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)

        self.skills = [self.i_know_how_to_kill_you,
                       self.do_you_how_to_learn_fight]

    def status(self):
        current_status = {
            '이름': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp),
            'ENG': self.eng,

        }
        for key, value in current_status.items():
            print(key, value, sep=':')

        # 일반스킬 - 난 아프게 때리는 법도 알아~(기댓값높은랜덤데미지)

    def i_know_how_to_kill_you(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = random.randint(
            int(self.atk*0.8), int(self.atk*1.6))  # 수치조정으로 밸런스
        damage -= target.def_*0.15  # 방어력상쇄량0.3->0.15로 수정해서 혹시 원펀맨 된건 아닌지 체크

        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 자가버프 - 셀프 공격력이 올라간다.싸움잘하는법 배울짜람?~ 기력 소모값 추가요망 수정수정수정수정

    def do_you_how_to_learn_fight(self, target):
        if self.eng <= 0:
            print('기력이 없어서 일반공격으로')
            return
        # 버프걸고 아프게 때렸을때, 기력+2턴소모+상대로부터한턴 맞는 코스트소모를했으므로 단순히 두턴의 기댓값인2.4계수보다 비슷하면서 무조건적으로 높아야 리턴이 성립한다,(1+(1.2)*(0.8~1.6))정도면 적정하다 생각
        effect = self.atk*0.2
        self.hp += effect
        self.eng += self.rst
        print(f'체력을 {effect}만큼 회복했다!')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

        # 캐릭터 종류============================================================================
        # 담임쌤 - 노멀, 기력소모


class Teacher(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)

        self.skills = [self.chalk_throw, self.buff]

    def status(self):
        current_status = {
            '이름': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp),
            'ENG': self.eng
        }
        for key, value in current_status.items():
            print(key, value, sep=':')
        # 자가버프 - 회피력 높인다.

    def buff(self, target):
        if self.eng <= 0:
            print('기력이 없어서 일반공격으로')
            return
        effect = self.atk*0.2
        self.hp += effect
        self.eng += self.rst
        print(f'체력을 {effect}만큼 회복했다!')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        # 일반스킬 - 분필던지기

    def chalk_throw(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk*1.3  # 몸통박치기에서 체력계수 없애고 공격력계수로 수정했음
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄

        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            # 몸통박치기에서 체력계수 없애고 공격력계수로 수정했음
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')

  # 캐릭터 종류============================================================================
        # 잘생긴 좀도둑 - 바람 속성


class HandsomeThief(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)
        # 밸런스를 위해 추가함
        self.skills = [self.thief_normal_attack,
                       self.betrayed_team, self.smileguy]

    def status(self):
        current_status = {
            '이름': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp),
            'ENG': self.eng
        }
        for key, value in current_status.items():
            print(key, value, sep=':')

        # 좀도둑 평타
    def thief_normal_attack(self, target):
        if random.random() < target.agi:
            return
        damage = self.atk  # 랜덤으로 치명타 적용
        damage -= target.def_*0.2  # 방어력으로 물리공격 상쇄
        if target.name == FireMonster:  # 상성 추뎀
            damage += self.atk*0.2
        elif target.name == SoilMonster:
            damage -= self.atk*0.2
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{damage} 푹!')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        self.eng += self.rst
        print(f'{self.name}은(는) {self.rst}만큼 기력을 회복했다.')
        if target.hp <= 0:
            print(f'톡 쳤더니 죽어버린 {target.name} 코이츠 wwwww')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*0.2
            print(f'{self.name}은(는) {self.rst*0.2}만큼 기력을 회복했다.')

    # 일반스킬 - 몬스터 하나를 없애고.. 팀 전체 디버프 -> 뒤통수치기

    def betrayed_team(self, target):
        if self.eng <= 0:
            print('기력 부족하여 하찮은 일반공격으로 대체합니다')
            return
        damage = 100000  # 처형이기때문에 무조건 높은값
        target.hp -= damage
        debuff = self.atk*0.1
        for i in character:
            i.def_ -= debuff
        self.eng -= 1000
        print('모든 기력사용!')
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        self.eng += self.rst*0.5
        print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*0.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.')

    # 마법스킬 - 상대 몬스터에게 전체방어력 저하 -> 난 너희들 마음도 다 훔쳐~~
    def smileguy(self, target):
        if self.eng <= 0:
            print('기력 부족하여 하찮은 일반공격으로 대체합니다')
            return
        debuff = self.atk*0.1
        damage = self.atk*0.3
        if target.name == FireMonster:  # 상성 추뎀
            damage += self.atk*0.2
        elif target.name == SoilMonster:
            damage -= self.atk*0.2
        for i in character:
            i.hp -= damage
        self.eng -= 30
        print('30 기력사용!')
        print(f'모든 몬스터에게 {damage}피해를 주고 {debuff}만큼의 방어력을 깎았다.')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        self.eng += self.rst*0.5
        print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.eng += self.rst*0.5
            print(f'{self.name}은(는) {self.rst*1.5}만큼 기력을 회복했다.')

        # 캐릭터 종류
        # 교통경찰 - 전기   # 지능사용  # MP소모


class TraffiselfPolice(Character):
    def __init__(self, name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp):
        super().__init__(name, hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp)
        self.skills = [self.wand_attack, self.taser_gun]

    def status(self):
        current_status = {
            '이름self': self.name,
            'Lv.': self.level,
            '경험치': self.exp,
            'HP': round(self.hp),
            'MP': self.mp
        }
        for key, value in current_status.items():
            print(key, value, sep=':')

        # 일반스킬 : 지팡이 때리기기

    def wand_attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk  # 수치조정으로 밸런스
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 대충 좀비울음소리')
        target.hp -= damage
        print(f'{target.name}에게 {damage}피해')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem*1.5}만큼 마나를 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}녀석 {damage}맞고 죽음')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.mp += self.rem
            print(f'{self.name}은(는) {self.rem*1.5}만큼 마나를 회복했다.')

    # 마법스킬 : 테이저건 -> 정상수 특효약  #int_ 지능/주문력 계수 활용해서 스킬짜기 so special!!
    def taser_gun(self, target):
        if self.mp <= 0:
            print('마나가 부족하여 하찮은 일반공격으로 대체합니다')
            return
        if random.random() < target.agi:
            return
        damage = self.int_*0.8
        if target.name == WaterMonster:   # 변수명 수정
            damage += self.atk*0.2
        elif target.name == SoilMonster:    # 변수명 수정
            damage -= self.atk*0.2
        damage -= target.rep*0.2  # 마법저항력으로 마법공격 상쇄
        self.mp -= 30
        print('30마나 사용')
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 오소이')
        target.hp -= damage
        print(f'{target.name}은 {damage}피해를 입었지만 테이져건을 견뎠다')
        self.hp += self.vit*0.2
        print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
        self.mp += self.rem
        print(f'{self.name}은(는) {self.rem}만큼 마나를 회복했다.')
        if target.hp <= 0:
            print(f'{target.name}, 제겐 유용한 단백질원이죠')
            self.hp += self.vit*0.2
            print(f'{self.name}은(는) {self.vit*0.2}만큼 체력을 회복했다.')
            self.mp += self.rem*0.2
            print(f'{self.name}은(는) {self.rem*0.2}만큼 마나를 회복했다.')


# 좀비부모 클래스============================================================================


class Monster:
    def __init__(self, name, hp, atk, def_, rep, agi):
        self.name = name

        # 소모용
        self.hp = hp  # 체력

        # 고정스탯
        self.atk = atk  # 공격력
        self.def_ = def_  # 방어력
        self.rep = rep  # 마법저항력력
        self.agi = agi  # 민첩/회피율


class WaterMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, PEteacher):  # 체육선생님(불속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0


# 불좀 FireMonster
class FireMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, HandsomeThief):  # 잘생긴좀도둑(바람속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 바람좀 WindMonster
class WindMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, PEteacher):  # 체육선생님(흙속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 흙좀 SoilMonster
class SoilMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, TraffiselfPolice):  # 교통경찰(전기속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 전기좀 ElecMonster
class ElecMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.3  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, Barista):  # 바리스타(물속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 가스좀(돌연변이) GasMonster
class GasMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.5  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 해양쓰레기(돌연변이) OTM(OceanTrashMonster)
class OTM(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        damage -= target.def_*0.1  # 방어력으로 물리공격 상쇄
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 방사능(돌연변이)  NukeMonster
class NukeMonster(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 보스 1    Boss1(흙속성)
class Boss1(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, TraffiselfPolice):  # 교통경찰(전기속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 보스 2    Boss2 (물속성)
class Boss2(Monster):
    def __init__(self, name, hp, atk, def_, rep, agi):
        super().__init__(name, hp, atk, def_, rep, agi)

    def attack(self, target):
        if random.random() < target.agi:  # 회피
            return
        damage = self.atk
        if damage < 0:  # 뎀지가 0이 안될시에 공격이 안됨
            damage = 0
            print(f'{target.name} : 느려')
        if isinstance(target, PEteacher):  # 체육선생님(불속성)인 경우
            target.hp -= self.atk * 1.2
        else:
            target.hp -= self.atk
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def status_check(self):
        if self.hp > 0:
            print(f"{self.name}의 hp가 {self.hp}만큼 남았습니다.")
        else:
            self.hp = 0
            print(f"{self.name}은(는) 죽었습니다.")


# 체력,마나,기력,공격력,지능/주문력,방어력,민첩/회피율/체력재생력,기력재생력,마나재생력
# hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp
# 캐릭터 생성
character = [PEteacher('술을 마시지 못하지만 항상 얼굴이 빨갛게 달아올라 술고래로 오해받는 체육선생님', 700, 0, 0, 170, 0, 200, 0.15, 30, 0, 0, 1, 0),
             AgentP('구청에서 메이플거래하다가 사기당하고 전재산 날려먹은 공익근무요원', 1200,
                    0, 200, 150, 0, 180, 0.1, 20, 10, 200, 1, 0),
             Barista('낮에는 바리스타, 밤에는 발이STAR인 커피를 잘 못만드는 바리스타',
                     780, 0, 0, 150, 0, 150, 0.1, 30, 0, 0, 1, 0),
             KnowledgeYoutuber('평소에 공부를 하지 않았지만 인터넷에서 줏어들은 정보로만 채널을 운영하는 지식유튜버',
                               630, 0, 180, 150, 0, 140, 0.12, 25, 10, 0, 1, 0),
             Teacher('학교가 너무 가기싫어서 일도 대충하는 이세계학교의 담임선생님', 650,
                     0, 150, 150, 0, 150, 0.35, 20, 10, 0, 1, 0),
             HandsomeThief('얼굴이 정말 잘생겼지만 손버릇이 좋지않아 여자들에게 퇴짜를 맞는 좀도둑',
                           500, 0, 200, 150, 0, 120, 0.3, 20, 10, 100, 1, 0)
             ]
# hp, atk, def_, rep, agi
# 좀비 생성
zombie = [WindMonster("토네이도좀비", 1000, 100, 50, 100, 0.2),
          FireMonster("불쏘시개좀비", 1500, 130, 50, 100, 0.05),
          WaterMonster("물귀신 좀비", 1700, 150, 100, 100, 0.05),
          ElecMonster("피카츄라이츄 좀비", 1600, 170, 50, 100, 0.05),
          Boss1('보스1', 2500, 250, 100, 100, 0.02),
          GasMonster('가스좀비', 1500, 130, 100, 100, 0.2),
          SoilMonster("흙흙좀비", 1400, 170, 0, 100, 0),
          OTM('해양쓰레기좀비', 2000, 230, 100, 0, 0.1),
          NukeMonster('방사능좀비', 3300, 180, 100, 100, 0.1),
          Boss2('보스2', 3000, 270, 0, 0, 0)
          ]


# 상태체크
def check(a):
    if a.hp > 0:
        a.status()
    else:
        a.hp = 0
        print(f"{a.name}은(는) 죽음..")


def levelup(a):
    if a.hp > 0:
        a.character_level()


# 좀비가 싸울 대상 선택, 인자로 character 들어감.
# 좀비가 싸울 대상은 hp가 가장 큰 캐릭터!

def zombie_attack(a):
    max_hp = a[0].hp  # 첫번째 캐릭터의  hp를 맥스값으로 적용함
    target = a[0]
    for i in a:
        if max_hp < i.hp:
            target = i
    return target


# 싸움장면 (반복되서 함수로 만듦)(잘했삼)(멋있삼)(오졌삼)(바지적삼)
# 4대 1전투
def fight1(a):
    while (character[0].hp > 0 or character[1].hp > 0 or character[2].hp > 0 or character[3].hp > 0) and a.hp > 0:
        for player in character:
            if player.hp > 0 and a.hp > 0:
                player.attack(a)
            else:
                pass
        a.status_check()
        if a.hp > 0:
            a.attack(zombie_attack(character))
        time.sleep(2)
        for i in character:
            check(i)

            
#5대 1전투
def fight2(a):
    while (character[0].hp > 0 or character[1].hp > 0 or character[2].hp > 0 or character[3].hp > 0 or character[4].hp > 0) and a.hp > 0:
        for player in character:
            if player.hp > 0 and a.hp > 0:
                player.attack(a)
            else:
                pass
        a.status_check()
        if a.hp > 0:
            a.attack(zombie_attack(character))
        time.sleep(2)
        for i in character:
            check(i)


def battle():
    # 스토리랑 전투장면
    print('\n', '좀비아포칼립스 세상이 들이닥쳤는데 좀비들이 5원소 속성을 가지지만 받는 피해에만 상성을 가질때 인간이 5원소공격을 하는 건에 대하여', '\n')
    time.sleep(1)
    print('뉴스 특보입니다. 좀비가 출현했습니다. 당장 항구로 대피하십시오.', '\n')
    time.sleep(2)
    print('좀비를 피해 급히 학교 옥상으로 대피한 6명의 사람들', '살기 위해서는 늦지 않게 항구에 도착해야한다.',
          '6명 모두는 갈 수 없는 상황. 2명은 가지 못한다.', '누구를 버릴 것인가', sep='\n')

    while True:
        print('첫번째로 버릴 사람은?', f'0: {character[0].name}', f'1: {character[1].name}', f'2: {character[2].name}',
              f'3: {character[3].name}', f'4: {character[4].name}', f'5: {character[5].name}', sep='\n')
        x = int(input(
            "당신의 선택은? :"))
        print('두번째로 버릴 사람은?', f'0: {character[0].name}', f'1: {character[1].name}', f'2: {character[2].name}',
              f'3: {character[3].name}', f'4: {character[4].name}', f'5: {character[5].name}', sep='\n')
        y = int(input(
            "당신의 선택은? :"))

        if x == y:
            print("다시 입력하세요.")
        elif x > y:
            del character[x]
            del character[y]
            break
        else:
            del character[x]
            del character[y-1]
            break

    # 전투장면
    while True:
        # os.system('cls')

        wind = zombie[0]  # 바람좀비
        fire = zombie[1]  # 불좀비
        water = zombie[2]  # 물좀비
        elec = zombie[3]  # 전기좀비
        boss1 = zombie[4]  # 보스좀비
        gas = zombie[5]  # 가스좀비
        soil = zombie[6]  # 흙좀비
        otm = zombie[7]  # 해양쓰레기좀비
        nuke = zombie[8]  # 방사능좀비
        boss2 = zombie[9]  # 보스좀비

        print("이제 준비는 끝났다. 출..ㅂ..ㅏ..",
              "어? 좀비가 옥상까지 기어올라왔다. 싸워서 이 곳을 탈출하자", '\n', sep='\n')

        # 스테이지1(바람)
        fight1(wind)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in range(4):
            levelup(character[i])
            check(character[i])
        time.sleep(5)

        os.system('cls')
        # 스테이지2(불)
        print("휴.. 무사히 옥상 밖으로 나왔다. 배가 너무 고픈데..?",
              "급한데로 학교급식실에서 먹을 것을 찾아봐야겠다.", "좀비와 싸워이겨서 먹을 것을 쟁취하자", '\n', sep='\n')
        fight1(fire)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in range(4):
            levelup(character[i])
            check(character[i])
        time.sleep(5)

        os.system('cls')
        # 스테이지3 (물)
        print("좀비들을 다 물리쳤다.", "급식실에서 몇 가지 음식과 음료를 찾았고 우린 허기를 채웠다.",
              "더욱 강력해졌다!! 이제 이 학교를 벗어나 항구로 향해야한다.",
              "그러기 위해선 먼저 좀비가 가득한 학교운동장을 지나가야한다.", '\n', sep='\n')
        fight1(water)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in range(4):
            levelup(character[i])
            check(character[i])
        time.sleep(5)

        os.system('cls')
        # 스테이지4(전기)
        print("학교 운동장에서 벗어났다.", "재정비를 할 시간이다. 저기 마트가 있다!",
              "마트 안에는 무기로 쓸 만한 물건과 충분한 식료품이 있다.", "좀비와의 전투를 시작하자.", sep='\n')
        fight1(elec)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in range(4):
            levelup(character[i])
            check(character[i])
        time.sleep(5)

        os.system('cls')
        # 스테이지5 (보스1 출현)
        print("이제 배도 차고 무기도 충분히 채웠다.", "뉴스방송에는 계속 항구로 오라는 메세지...",
              "항구로 가야만 살 수 있다.", "항구로 가기 위해 차를 얻어야겠다. 마침 중고차 시장이 눈에 보인다.",
              "이곳에도 좀비가 가득하다. 싸워서 차를 얻자!!!", '\n', sep='\n')
        fight1(boss1)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", sep='\n')
            break
        print('='*100, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in range(4):
            levelup(character[i])
            check(character[i])
        time.sleep(5)

        os.system('cls')
        # 스테이지6 (가스)
        print("힘겨운 싸움 끝에 자동차를 얻었다.", "어? 근데 범상치 않은 교통경찰이 우리를 향해 다가온다???",
              "전직 마법사였던 교통경찰.. 그와 함께한다면 항구까지 가기 더 수월할거다.", "그럼 이제 출~~바...ㄹ.... ㅇㅔ??",
              "기름이 없다...", "기름을 얻으러 주유소로 가자", '\n', sep='\n')

# hp, mp, eng, atk, int_, def_, agi, vit, rem, rst, level, exp
        # 교통경찰추가!!
        character.append(TraffiselfPolice('이세계 마법사였지만 마법세계에서 퇴출을 당하고 마법부에 쫓기고 있는 교통경찰',
                                          700, 150, 0, 120, 200, 150, 0.15, 20, 120, 0, 3, 0))

        fight2(gas)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0 and character[4].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in character:
            levelup(i)
            check(i)
        time.sleep(5)

        os.system('cls')
        # 스테이지7(흙)
        print("이제 기름까지 채웠겠다. 정말로 출발하자.",
              "아닛.. 고속도로에는 온통 버려진 차로 가득하다.", "이 길로는 갈 수 없다. 산길로 가자.", '\n', sep='\n')
        time.sleep(2)
        print("시간이 얼마나 흘렀을까...", "벌써 해가 졌다. 야영을 하기로 했다.",
              "그런데.. 저 멀리 좀비가...", '\n', sep='\n')
        fight2(soil)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0 and character[4].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in character:
            levelup(i)
            check(i)
        time.sleep(5)

        os.system('cls')
        # 스테이지8(해양쓰레기)
        print("산을 벗어났다.", "이곳은 쓰레기 해변으로 유명한 곳.. 조금만 더 가면 목적지다.",
              "쓰레기 사이로.. 좀비가!!", '\n', sep='\n')
        fight2(otm)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0 and character[4].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', '\n', sep='\n')
        for i in character:
            levelup(i)
            check(i)
        time.sleep(5)

        os.system('cls')
        # 스테이지9(방사능)
        print("이제 정말 거의 다 왔다. 부두다!!!",
              "기쁨도 잠시.. 이곳을 지키는 방사능 범벅 좀비...!!", '\n', sep='\n')
        fight2(nuke)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0 and character[4].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        print('='*70, '좀비와의 전투에서 승리했습니다! 보상:  레벨업, 스킬업', sep='\n')
        for i in character:
            levelup(i)
            check(i)
        time.sleep(5)

        os.system('cls')
        # 스테이지10(보스2)
        print("부두를 벗어나고 항구에 도착했다!!!",
              "배가 곧 출항할 것 같다. 눈 앞에 아주 강해보이는 존재.. 보스좀비다!!", "보스를 해치우고 살아남자!!", '\n', sep='\n')
        fight2(boss2)
        if character[0].hp <= 0 and character[1].hp <= 0 and character[2].hp <= 0 and character[3].hp <= 0 and character[4].hp <= 0:
            print("게임종료..", "이쉽게도 당신은 생존하지 못했습니다..", '\n', sep='\n')
            break
        break


battle()
print('='*50, ' '*50, ' '*50, sep='\n')
survivors = 0
for player in character:
    if player.hp > 0:
        survivors += 1
print(f'그렇게 {survivors}명밖에 남지 않은 생존자들은 어디로 향할것인가, 과연 그 곳에는 또 어떤 위험이 도사리고 있을까.', '좀비아포칼립스 세상이 들이닥쳤는데데 좀비들이 5원소 속성을 가지지만 받는피해만 상성을 가질때 인간이 5원소공격을 하는 건에 대하여', '-THE END-', sep='\n'
      )
