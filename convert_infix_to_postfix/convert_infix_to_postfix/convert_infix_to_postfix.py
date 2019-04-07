infix=[]                                    #입력받은 식을 중위표기식으로 변경하고 저장하는 리스트
postfix=[]                                  #중위표기식을 후위표기식으로 변경하고 저장하는 리스트
stack=[]                                    #스택을 구현하는 리스트
full_oper=['(',')','+','-','*','/']         #연산자 리스트  
oper=['+','-','*','/']
in_put=input("식을 입력하시오 : ")
tmp=''                                      #와일드변수
def level(i):                               #연산자들의 레벨을 지정하는 함수
    if(i=='('):
        return 0
    elif (i == '+','-'):
        return 1
    elif(i == '*','/'):
        return 2
    elif (i==')'):
        return 3

for i in range(len(in_put)):                #입력받은 문자열을 수식으로 변경하는 알고리즘
    if in_put[i] not in full_oper:          #연산자가 아닐경우
        tmp = tmp + in_put[i]               #문자를 tmp에 저장해 자리수를 마추고
    else:
        if tmp !='':
            infix.append(int(tmp))          #자리수를 마춘 문자를 정수로 변경하면서 리스트에 넣음
            tmp=''                          #다음 문자를 받기위해 초기화
        infix.append(in_put[i])             #연산자를 리스트에 넣음
if tmp !='':
    infix.append(int(tmp))                  #마지막 문자를 정수로 변경하면서 넣음
tmp=''                                  
for i in range(len(infix)):                 #후위표기식 변경 알고리즘
    if infix[i] not in full_oper:
        posfix.append(infix[i])             #연산자가 아닐경우 리스트에 넣음
    elif infix[i] in oper:              
        tmp = level(infix[i])               #차례의 연산자의 레벨을 체크
        while len(stack) > 0:               #스택이 차있을 경우
            v=len(stack)
            top = stack[v-1]                #top를 체크하고
            if level(top)<tmp:              #top의 레벨보다 입력된 연산자의 레벨이 높은경우
                break                       #반복종료  
            posfix.append(stack.pop())      #연산자의 레벨이 낮은경우 스택에서 꺼내며 후위표기식에 넣음
        stack.append(infix[i])              #레벨에 높을때 연산자 스택에 넣음
    elif infix[i] == '(':                    #괄호 구현
        stack.append(infix[i])
    elif infix[i] == ')' :
        while True:
            c = stack.pop()
            if c =='(':
                break
            posfix.append(c)


 
while len(stack)>0:                         #스택에 남은 연산자 pop
    posfix.append(stack.pop())

if '(' in posfix:                           #출력하기 전 후위 연산에서 괄호를 제거
    posfix.remove('(')
if ')' in posfix:
    posfix.remove(')')

print(infix)                                #입력받은 중위표기법 수식
print(posfix)                               #변경된 후위표기법 수식


#이 코드는 Visual Studio 2017 community 에서 작성함
#참고사이트 https://docs.python.org/ko/3/library/index.html
#참고사이트 https://docs.python.org/ko/3/tutorial/datastructures.html#using-lists-as-stacks
#참고도서 어서와 파이썬은 처음이지! , c언어로 쉽게 풀어쓴 자료구조 생능출판
