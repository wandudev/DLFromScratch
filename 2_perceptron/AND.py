def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

'''
퍼셉트론의 매개변수 값을 정하는 것 -> 인간
인간이 학습 데이터를 보며 매개변수 값을 생각하는 것.
기계학습: 이 매개변수 값 정하는 작업을 컴퓨터가 자동으로 하도록 함
학습: 적절한 매개변수 값을 정하는 작업
사람: 퍼셉트론의 구조(모델)을 고민하고 컴퓨터에 학습할 데이터를 주는 역할을 함
'''