

# 예외처리 활용하기   try 예외가 발생할 문장. except 예외 종류  예외가 발생하면 실행할 문장. else  예외가 발생하지 않을 때 실행할 문장


# 예제1
#정상적인 경우
print('정상적인 경우')
no1 = int(input("숫자 1개 입력하세요: "))
print(no1)

print("\n")
#숫자 입력 예외 처리를 적용한 경우
print("예외 발생 경우")
try:
  no2 = int(input('숫자 1개 입력하세요:'))
except :
  print('숫자 입력하세요.')


#예외일 경우와 아닐 경우 한꺼번에 지정하기
try:
  no2 = int(input('숫자 1개 입력하세요:'))
except:
  print('숫자 입력하세요.')
else:
  print("입력하신 숫자는 %s 압니다" %no2)