grade = int(input("성적을 입력하시오: "))
# 정수형으로 성적 입력

if grade<70 and grade>=0: # 음수 입력 시 오류 발생.
	print("F 입니다.")
elif grade<75: # 70 이상 75 미만, 70 이상 조건은 앞서 처리됨.
	print("C 입니다.")
elif grade<80:
	print("C+ 입니다.")
elif grade<85:
	print("B 입니다.")
elif grade<90:
	print("B+ 입니다.")
elif grade<95:
	print("A 입니다.")
elif grade<=100:
	print("A+ 입니다.")
else: # 0 ~ 100 외의 값 입력 시
	print("입력 값이 올바르지 않습니다.")
