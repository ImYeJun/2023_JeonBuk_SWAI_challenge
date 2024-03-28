import random

print("국가의 정보를 입력하시오.")
city_num, population = map(int,input().split())

country = [[]]

for i in range(1,city_num + 1):
    city = []
    
    for j in range(1,population + 1):
        city.append(input().split(","))
    
    country.append(city)

print("도시간의 경로를 입력하시오.")
node = int(input())

INF = 1001

graph = [[] for _ in range(city_num + 1)]
distance = [INF for _ in range(city_num + 1)]
passed = [False for _ in range(city_num + 1)]
way = [[] for _ in range(city_num + 1)]

#그래프 작성
for i in range(node):
    start,end,value = map(int,input().split())
    graph[start].append((end,value))

print("시작 지점을 입력하시오.")
start_point = int(input())

show_process = input("과정을 보시겠습니까? (Y/N):")

#시작 지점
passed[start_point] = True
distance[start_point] = 0

for node in graph[start_point]:
    distance[node[0]] = node[1]
    way[node[0]].append(start_point)
    way[node[0]].append(node[0])

#테이블 작성
for i in range(1, city_num):
    minimum = INF
    index = 0

    #최소지점 계산
    for j,value in enumerate(distance):
        if value < minimum and not(passed[j]):
            minimum = value
            index = j

    passed[index] = True

    if show_process == "Y":
        print() 
        print(f"(현재 지정 지점)\n{index}")
        print(f"(현재 지나간 지점)\n{passed}")
        print(f"(현재 지점 까지 최소거리)\n{distance}")
        print(f"(현재 까지 지나간 경로)\n{way}")
    
    #거리 계산
    for node in graph[index]:
        way_start = way[index]
        way_para = way_start + [node[0]]
        para = distance[index] + node[1]

        if para < distance[node[0]]:
            distance[node[0]] = para
            way[node[0]] = way_para

#최고 거리 게산
max = 0
for i in distance:
    if i != INF and i > max:
        max = i

print()

mini_para = distance.copy()
shortest = []

for z in range(city_num):
    minimum = INF
    index = 0
    
    for i,value in enumerate(mini_para):
        if value < minimum:
            index = i
            minimum = value
    
    shortest.append(index)
    mini_para[index] = INF

print()
print("----위험도 순위----")
print()
print(f"시작지역 : {start_point}번지역")
print()

for i,key in enumerate(shortest[1:]):
    print(f"{i+1}순위 : {key}번 지역")
    print(f"{start_point}지역에서 {key}지역 까지의 최소 거리 : {distance[key]}")
    print("최소 거리 경로")
    
    print(f"{way[key][0]}",end = "")
    for j in way[key][1:]:
        print(f"  -->  {j}",end = "")
    
    print()
    print()

dangerous_city = country[shortest[1]]

# --------------------------- 한 도시의 사람들의 진단정보를 구하는 프로그램 ----------------------------- #

def get_diagnostic_information(city):
    for info in city:
        
        # -------------------- 기본 정보 가져오기 -------------------- #
        
        name = info[0]
        gender = info[1]
        height = float(info[2])
        weight = float(info[3])

        print('-----------------------------------------------------------------')
        print(f'이름: {name}')
        print(f'성별: {gender}')
        print(f'키: {height}')
        print(f'몸무게: {weight}')
        print()

        # -------------------- BMI 계산 -------------------- #

        height /= 100 # BMI 수치 계산을 위해 키 단위를 미터로 변환

        bmi = weight / (height * height) # BMI 계산식
        bmi_condition = ''

        if bmi < 18.5:
            bmi_condition = '저체중'

        elif bmi < 23:
            bmi_condition = '정상'

        elif bmi < 25:
            bmi_condition = '과체중'

        elif bmi < 30:
            bmi_condition = '경도 비만(1단계 비만)'

        elif bmi < 35:
            bmi_condition = '중도 비만(2단계 비만)'

        else:
            bmi_condition = '고도 비만(3단계 비만)'

        print(f'{name}님의 BMI 수치는 {bmi:.3f}(으)로 {bmi_condition}입니다.')

        # ------------------------------ 체지방 계산 ------------------------------ #

        height *= 100 # 체지방 계산을 위해 키 단위를 센치미터로 변환

        # ---------- 제지방량 계산
        lean_body_mass = 0 # 제지방량

        if gender == 'Male':
            lean_body_mass = (weight * 1.1) - (128 * (weight**2 / height**2)) # 남자 제지방량 계산식
        else:   
            lean_body_mass = (weight * 1.07) - (128 * (weight**2 / height**2)) # 여자 제지방량 계산식

        # ---------- 체지방량, 체지방률 계산
        body_fat_mass = weight - lean_body_mass # 체지방량
        body_fat_percentage = body_fat_mass * 100 / weight # 체지방률
        body_fat_condition = ''

        # ---------- 성별에 따른 체지방률 기준에 따라 분류
        if gender == 'Male':
            if body_fat_percentage < 8:
                body_fat_condition = '표준이하'

            elif body_fat_percentage < 20:
                body_fat_condition = '표준'

            elif body_fat_percentage < 25:
                body_fat_condition = '경도비만'

            else:
                body_fat_condition = '고도비만'

        else:
            if body_fat_percentage < 21:
                body_fat_condition = '표준이하'

            elif body_fat_percentage < 33:
                body_fat_condition = '표준'

            elif body_fat_percentage < 39:
                body_fat_condition = '경도비만'

            else:
                body_fat_condition = '고도비만'   

        print(f'{name}님의 체지방량은 {body_fat_mass:.3f}kg 입니다.')
        print(f'{name}님의 체지방률은 {body_fat_percentage:.3f}%이므로 {body_fat_condition}입니다.')
        print()

        # ------------------------- 체지방률에 따라 추천하는 관리법 ------------------------- #

        random_var1 = random.randrange(1, 3)
        random_var2 = random.randrange(1, 3)
        random_var3 = random.randrange(1, 3)

        # ----- 비만
        if body_fat_condition == '경도비만' or body_fat_condition == '고도비만':
            print(f'[당신의 체지방률은 {body_fat_condition} 이므로 체지방량을 건강하게 줄이는 식습관과 운동 루틴을 형성해야 합니다.]\n')

            if random_var1 == 1:
                print('추천 식습관: 영양가 있는 음식을 조금씩 자주 천천히 먹기 \n')
            elif random_var1 == 2:
                print('추천 식습관: 동물성 지방보다 올리브유,아몬드,아보카도 등의 불포화 지방 섭취하기 \n')
            elif random_var1 == 3:
                print('추천 식습관: 닭가슴살,돼지안심,콩,저지방우유 등의 저지방 고단백질 음식 섭취하기 \n')

        # ----- 표준
        elif body_fat_condition == '표준':
            print(f'[당신의 체지방률은 {body_fat_condition} 이므로 체지방량을 건강하게 유지하는 식습관과 운동 루틴을 형성해야 합니다.]\n')

            if random_var2 == 1:
                print('추천 식습관: 아침식사는 꼭 챙겨먹기\n')
            elif random_var2 == 2:
                print('추천 식습관: 천천히 식사하기\n')
            elif random_var2 == 3:
                print('추천 식습관: 자기 전에 단 음식 먹지 않기\n')

        # ----- 표준이하
        elif body_fat_condition == '표준이하':
            print(f'[당신의 체지방율은 {body_fat_condition} 이므로 체지방량을 건강하게 늘리는 식습관과 운동 루틴을 형성해야 합니다.]\n')

            if random_var3 == 1:
                print('추천 식습관: 고기,생선,계란,견과류 등의 고단백질 섭취하기\n')
            elif random_var3 == 2:
                print('추천 식습관: 적절하게 칼로리 섭취량 증가시키기\n')
            elif random_var3 == 3:
                print('추천 식습관: 곡물,채소,과일 등의 고탄수화물 식품 섭취하기')
        

stop = input(f"아무키를 눌러서 {shortest[1]} 지역 주민의 진단표 확인")
get_diagnostic_information(dangerous_city)


#---------------------자가 운동 루틴 제작 프로그램---------------------

def self_exercise():
    print("---자가 운동 루틴 제작 프로그램---")
    print("팔, 다리, 복근, 가슴, 등, 체중 관리")
    exercise_area = input("보기에서 원하는 운동 부위을 입력하세요\n입력:")

    if exercise_area == "팔":
        difficulty = int(input("운동 난이도를 입력해주세요(1~5)"))

        if 1 <= difficulty <= 5:
            Round = int(input("운동 레벨을 입력해 주세요(1~30) 만약 어제 해당 부위를 운동 했다면 0을 입력하고 쉬거나 다른 부위를 운동하세요"))

            if 1 <= Round <= 30:
                Difficulty_before = int(input("자신이 느낀 전 날에 한 운동에 대한 난이도를 입력해 주세요(1~5) 만약 운동 첫 날이라면 3을 입력하세요"))

                if Difficulty_before == 1:
                    Round += 4
                    print("다음 운동 때 다다음 레벨을 운동하세요")

                elif Difficulty_before == 2:
                    Round += 2
                    print("다음 운동 때 다음 레벨을 운동하세요")
                
                elif Difficulty_before == 3:
                    pass
                    print("다음 운동 때 지금과 같은 레벨을 운동하세요")

                elif Difficulty_before == 4:
                    Round -= 2
                    print("다음 운동 때 이전 레벨을 운동하세요")
                
                elif Difficulty_before == 5:
                    Round -= 4
                    print("다음 운동 때 전전 레벨을 운동하세요")

                if 1 <= Difficulty_before <= 5:
                    print("운동 한 개 후 30초 휴식해 주세요",
                        f"\n팔 들어올리기 {10*difficulty+Round-1}초",
                        f"\n옆으로 팔 올리기 {10*difficulty+Round-1}초",
                        f"\n트리셉스 체어 딥 {3*difficulty+Round//3}개",
                        f"\n시계 방향으로 팔 돌리기 {10*difficulty+Round-1}초",
                        f"\n시계 반대 방향으로 팔 돌리기 {10*difficulty+Round-1}초",
                        f"\n다이아몬드 푸시업 {2*difficulty+Round//5}개",
                        f"\n점핑잭 {10*difficulty+Round-1}초",
                        f"\n가슴모아 들어올리기 {5*difficulty+Round//2}초",
                        f"\n다리 역기 컬 왼쪽 {2*difficulty+Round//5}개",
                        f"\n다리 역기 컬 오른쪽 {2*difficulty+Round//5}개",
                        f"\n사선 플랭크 {3*difficulty+Round//3}개",
                        f"\n펀치 {10*difficulty+Round-1}초",
                        f"\n팔굽혀펴기 {3*difficulty+Round//3}개",
                        f"\n자벌레 {2*difficulty+Round//5}개",
                        f"\n벽 푸시업 {4*difficulty+Round//3}",
                        f"\n삼두근 스트레칭 왼쪽 {10*difficulty+Round-1}초",
                        f"\n삼두근 스트레칭 오른쪽 {10*difficulty+Round-1}초",
                        f"\n스탠딩 이두근 스트레칭 왼쪽 {10*difficulty+Round-1}초",
                        f"\n스탠딩 이두근 스트레칭 오른쪽 {10*difficulty+Round-1}초")

                else:
                    print("범위를 벗어났습니다")

            elif Round == 0:
                print("종료")
            
            else:
                print("범위를 벗어났습니다")
        else:
            print("범위를 벗어났습니다")

    elif exercise_area == "다리":
        difficulty = int(input("운동 난이도를 입력해주세요(1~5)"))

        if 1 <= difficulty <= 5:
            Round = int(input("운동 레벨을 입력해 주세요(1~30) 만약 어제 해당 부위를 운동 했다면 0을 입력하고 쉬거나 다른 부위를 운동하세요"))

            if 1 <= Round <= 30:
                Difficulty_before = int(input("자신이 느낀 전 날에 한 운동에 대한 난이도를 입력해 주세요(1~5) 만약 운동 첫 날이라면 3을 입력하세요"))

                if Difficulty_before == 1:
                    Round += 4
                    print("다음 운동 때 다다음 레벨을 운동하세요")

                elif Difficulty_before == 2:
                    Round += 2
                    print("다음 운동 때 다음 레벨을 운동하세요")
                
                elif Difficulty_before == 3:
                    pass
                    print("다음 운동 때 지금과 같은 레벨을 운동하세요")

                elif Difficulty_before == 4:
                    Round -= 2
                    print("다음 운동 때 이전 레벨을 운동하세요")
                
                elif Difficulty_before == 5:
                    Round -= 4
                    print("다음 운동 때 전전 레벨을 운동하세요")

                if 1 <= Difficulty_before <= 5:
                    print("운동 한 개 후 30초 휴식해 주세요",
                        f"\n좌우 뛰기 {10*difficulty+Round-1}초",
                        f"\n스쿼트 {4*difficulty+Round//3}개",
                        f"\n스쿼트 {4*difficulty+Round//3}개",
                        f"\n옆으로 누워 다리 올리기 왼쪽 {4*difficulty+Round//3}개",
                        f"\n옆으로 누워 다리 올리기 오른쪽 {4*difficulty+Round//3}개",
                        f"\n옆으로 누워 다리 올리기 왼쪽 {4*difficulty+Round//3}개",
                        f"\n옆으로 누워 다리 올리기 오른쪽 {4*difficulty+Round//3}개",
                        f"\n뒤 런지 {4*difficulty+Round//3}개",
                        f"\n뒤 런지 {4*difficulty+Round//3}개",
                        f"\n동키 킥 왼쪽 {5*difficulty+Round//2}개",
                        f"\n동키 킥 오른쪽 {5*difficulty+Round//2}개",
                        f"\n동키 킥 왼쪽 {5*difficulty+Round//2}개",
                        f"\n동키 킥 오른쪽 {5*difficulty+Round//2}개",
                        f"\n벽으로 하는 왼쪽 쿼드 스트레칭 {10*difficulty+Round-1}초",
                        f"\n벽으로 하는 오른쪽 쿼드 스트레칭 {10*difficulty+Round-1}초",
                        f"\n무릅을 가슴으로 스트레칭 왼쪽 {10*difficulty+Round-1}초",
                        f"\n무릅을 가슴으로 스트레칭 오른쪽 {10*difficulty+Round-1}초",
                        f"\n벽 종아리 들기 {4*difficulty+Round//3}개",
                        f"\n벽 종아리 들기 {4*difficulty+Round//3}개",
                        f"\n벽으로 하는 스모 스쿼트 종아리 올리기 {4*difficulty+Round//3}개",
                        f"\n벽으로 하는 스모 스쿼트 종아리 올리기 {4*difficulty+Round//3}개",
                        f"\n종아리 스트레칭 왼쪽 {10*difficulty+Round-1}초",
                        f"\n종아리 스트레칭 오른쪽 {10*difficulty+Round-1}초")

                else:
                    print("범위를 벗어났습니다")

            elif Round == 0:
                print("종료")
            
            else:
                print("범위를 벗어났습니다")
        else:
            print("범위를 벗어났습니다")

    elif exercise_area == "복근":
        difficulty = int(input("운동 난이도를 입력해주세요(1~5)"))

        if 1 <= difficulty <= 5:
            Round = int(input("운동 레벨을 입력해 주세요(1~30) 만약 어제 해당 부위를 운동 했다면 0을 입력하고 쉬거나 다른 부위를 운동하세요"))

            if 1 <= Round <= 30:
                Difficulty_before = int(input("자신이 느낀 전 날에 한 운동에 대한 난이도를 입력해 주세요(1~5) 만약 운동 첫 날이라면 3을 입력하세요"))

                if Difficulty_before == 1:
                    Round += 4
                    print("다음 운동 때 다다음 레벨을 운동하세요")

                elif Difficulty_before == 2:
                    Round += 2
                    print("다음 운동 때 다음 레벨을 운동하세요")
                
                elif Difficulty_before == 3:
                    pass
                    print("다음 운동 때 지금과 같은 레벨을 운동하세요")

                elif Difficulty_before == 4:
                    Round -= 2
                    print("다음 운동 때 이전 레벨을 운동하세요")
                
                elif Difficulty_before == 5:
                    Round -= 4
                    print("다음 운동 때 전전 레벨을 운동하세요")

                if 1 <= Difficulty_before <= 5:
                    print("운동 한 개 후 30초 휴식해 주세요",
                        f"\n점핑잭 {10*difficulty+Round-1}초",
                        f"\n복부 크런치 {5*difficulty+Round//3}개",
                        f"\n러시안 트위스트 {6*difficulty+Round//2}개",
                        f"\n마운틴 클라이머 {5*difficulty+Round//3}개",
                        f"\n발 뒤꿈치 터치 {6*difficulty+Round//2}개",
                        f"\n다리 들어올리기 {5*difficulty+Round//3}개",
                        f"\n플랭크 {10*difficulty+Round-1}초",
                        f"\n복부 크런치 {4*difficulty+Round//5}개",
                        f"\n러시안 트위스트 {10*difficulty+Round//2}개",
                        f"\n마운틴 클라이머 {4*difficulty+Round//3}개",
                        f"\n발 뒤꿈치 터치 {6*difficulty+Round//2}개",
                        f"\n다리 들어올리기 {4*difficulty+Round//3}개",
                        f"\n플랭크 {10*difficulty+Round-1}초",
                        f"\n코브라 스트레칭 {10*difficulty+Round-1}초",
                        f"\n척추 허리 트위스트 스트레칭 왼쪽 {10*difficulty+Round-1}초",
                        f"\n척추 허리 트위스트 스트레칭 오른쪽 {10*difficulty+Round-1}초")

                else:
                    print("범위를 벗어났습니다")

            elif Round == 0:
                print("종료")
            
            else:
                print("범위를 벗어났습니다")
        else:
            print("범위를 벗어났습니다")

    elif exercise_area == "가슴":
        difficulty = int(input("운동 난이도를 입력해주세요(1~5)"))

        if 1 <= difficulty <= 5:
            Round = int(input("운동 레벨을 입력해 주세요(1~30) 만약 어제 해당 부위를 운동 했다면 0을 입력하고 쉬거나 다른 부위를 운동하세요"))

            if 1 <= Round <= 30:
                Difficulty_before = int(input("자신이 느낀 전 날에 한 운동에 대한 난이도를 입력해 주세요(1~5) 만약 운동 첫 날이라면 3을 입력하세요"))

                if Difficulty_before == 1:
                    Round += 4
                    print("다음 운동 때 다다음 레벨을 운동하세요")

                elif Difficulty_before == 2:
                    Round += 2
                    print("다음 운동 때 다음 레벨을 운동하세요")
                
                elif Difficulty_before == 3:
                    pass
                    print("다음 운동 때 지금과 같은 레벨을 운동하세요")

                elif Difficulty_before == 4:
                    Round -= 2
                    print("다음 운동 때 이전 레벨을 운동하세요")
                
                elif Difficulty_before == 5:
                    Round -= 4
                    print("다음 운동 때 전전 레벨을 운동하세요")

                if 1 <= Difficulty_before <= 5:
                    print("운동 한 개 후 30초 휴식해 주세요",
                        f"\n점핑잭 {10*difficulty+Round-1}초",
                        f"\n인클라인 푸시업 {2*difficulty+Round//5}개",
                        f"\n팔굽혀펴기 {1*difficulty+Round//10}개",
                        f"\n팔 벌려 푸시업 {1*difficulty+Round//10}개",
                        f"\n트리셉스 체어 딥 {2*difficulty+Round//5}개",
                        f"\n팔 벌려 푸시업 {1*difficulty+Round//10}개",
                        f"\n인클라인 푸시업 {1*difficulty+Round//10}개",
                        f"\n트리셉스 체어 딥 {1*difficulty+Round//10}개",
                        f"\n무릅굽혀 푸시업 {1*difficulty+Round//10}개",
                        f"\n코브라 스트레칭 {10*difficulty+Round//2}초",
                        f"\n가슴 스트레칭 {10*difficulty+Round//2}초")

                else:
                    print("범위를 벗어났습니다")

            elif Round == 0:
                print("종료")
            
            else:
                print("범위를 벗어났습니다")
        else:
            print("범위를 벗어났습니다")

    elif exercise_area == "등":
        difficulty = int(input("운동 난이도를 입력해주세요(1~5)"))

        if 1 <= difficulty <= 5:
            Round = int(input("운동 레벨을 입력해 주세요(1~30) 만약 어제 해당 부위를 운동 했다면 0을 입력하고 쉬거나 다른 부위를 운동하세요"))

            if 1 <= Round <= 30:
                Difficulty_before = int(input("자신이 느낀 전 날에 한 운동에 대한 난이도를 입력해 주세요(1~5) 만약 운동 첫 날이라면 3을 입력하세요"))

                if Difficulty_before == 1:
                    Round += 4
                    print("다음 운동 때 다다음 레벨을 운동하세요")

                elif Difficulty_before == 2:
                    Round += 2
                    print("다음 운동 때 다음 레벨을 운동하세요")
                
                elif Difficulty_before == 3:
                    pass
                    print("다음 운동 때 지금과 같은 레벨을 운동하세요")

                elif Difficulty_before == 4:
                    Round -= 2
                    print("다음 운동 때 이전 레벨을 운동하세요")
                
                elif Difficulty_before == 5:
                    Round -= 4
                    print("다음 운동 때 전전 레벨을 운동하세요")

                if 1 <= Difficulty_before <= 5:
                    print("운동 한 개 후 30초 휴식해 주세요",
                        f"\n점핑잭 {10*difficulty+Round-1}초",
                        f"\n팔 들어올리기 {5*difficulty+Round//3}초",
                        f"\n롬보이드 풀 {5*difficulty+Round//3}개",
                        f"\n옆으로 팔 올리기 {5*difficulty+Round//3}초",
                        f"\n무릅굽혀 푸시업 {5*difficulty+Round//5}개",
                        f"\n옆으로 누워 바닥 스트레칭 왼쪽 {10*difficulty+Round-1}초",
                        f"\n옆으로 누워 바닥 스트레칭 오른쪽 {10*difficulty+Round-1}초",
                        f"\n암 시저스 {10*difficulty+Round-1}초",
                        f"\n롬보이드 풀 {4*difficulty+Round//5}개",
                        f"\n옆으로 팔 올리기 {5*difficulty+Round//2}초",
                        f"\n무릅굽혀 푸시업 {4*difficulty+Round//5}개",
                        f"\n고양이 소 포즈 {10*difficulty+Round-1}초",
                        f"\n엎드려 삼두근 팔굽혀펴기 {5*difficulty+Round//5}개",
                        f"\n리클라인 롬보이드 스퀴즈 {4*difficulty+Round//5}개",
                        f"\n엎드려 삼두근 팔굽혀펴기 {5*difficulty+Round//5}",
                        f"\n리클라인 롬보이드 스퀴즈 {4*difficulty+Round//5}개",
                        f"\n어린이 포즈 {10*difficulty+Round-1}초")

                else:
                    print("범위를 벗어났습니다")

            elif Round == 0:
                print("종료")
            
            else:
                print("범위를 벗어났습니다")
        else:
            print("범위를 벗어났습니다")

    elif exercise_area == "체중 관리":
        difficulty = int(input("운동 난이도를 입력해주세요(1~5)"))

        if 1 <= difficulty <= 5:
            Round = int(input("운동 레벨을 입력해 주세요(1~30) 만약 어제 해당 부위를 운동 했다면 0을 입력하고 쉬거나 다른 부위를 운동하세요"))

            if 1 <= Round <= 30:
                Difficulty_before = int(input("자신이 느낀 전 날에 한 운동에 대한 난이도를 입력해 주세요(1~5) 만약 운동 첫 날이라면 3을 입력하세요"))

                if Difficulty_before == 1:
                    Round += 4
                    print("다음 운동 때 다다음 레벨을 운동하세요")

                elif Difficulty_before == 2:
                    Round += 2
                    print("다음 운동 때 다음 레벨을 운동하세요")
                
                elif Difficulty_before == 3:
                    pass
                    print("다음 운동 때 지금과 같은 레벨을 운동하세요")

                elif Difficulty_before == 4:
                    Round -= 2
                    print("다음 운동 때 이전 레벨을 운동하세요")
                
                elif Difficulty_before == 5:
                    Round -= 4
                    print("다음 운동 때 전전 레벨을 운동하세요")

                if 1 <= Difficulty_before <= 5:
                    print("운동 한 개 후 30초 휴식해 주세요",
                        f"\n스모 스쿼트 {15*difficulty+Round-1}초",
                        f"\n플랭크 잭 {15*difficulty+Round-1}초",
                        f"\n무릎굽혀 푸시업 {15*difficulty+Round-1}초개",
                        f"\n슈퍼맨 {15*difficulty+Round-1}초",
                        f"\n플러터 발차기 {15*difficulty+Round-1}초",
                        f"\n플랭크 다리 올리기 {15*difficulty+Round-1}초",
                        f"\n불가사리 크런치 {15*difficulty+Round-1}초")

                else:
                    print("범위를 벗어났습니다")

            elif Round == 0:
                print("종료")
            
            else:
                print("범위를 벗어났습니다")
        else:
            print("범위를 벗어났습니다")

    else:
        print("존재하지 않는 부위입니다.")

self_exercise()

abc = input("아무키나 입력하면 꺼짐니다.")