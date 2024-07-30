num = 456789    # Baby-gin 확인할 6자리 수
c=[0]*12    # 개수 누적 리스트  # 가장 큰 정수는 9인데 12개의 배열을 생성하는 이유는 혹시 모르니까...

for i in range(6):
    c[num%10]+=1    # num을 리스트로 지정하지 않았기 때문에 이런 식으로 일의 자리 숫자부터 확인을 해준다.
    num //= 10

i=0
tri=run=0

while i<10:
    if c[i]>=3: # triplete 조사 후 데이터 삭제
        c[i]-=3
        tri+=1
        continue
    if c[i]>=1 and c[i+1]>=1 and c[i+2]>=1:
        c[i]-=1
        c[i+1]-=1
        c[i+2]=-1
        run+=1
        continue
    i+=1

if run + tri == 2:
    print("Baby Gin!")
else:
    print("Lose")