"""첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다."""

people=int(input())

for i in range(people):
    p_array=list(map(int,input().split()))
    avg_num=sum(p_array[1:])/p_array[0]
    k=0 # if 밖이 아니라 for 밖으로 들어간다.           
    for p in p_array[1:]:
        if p>avg_num:
            k+=1
    q=k/p_array[0]*100
    print(f'{q:.3f}%') # f표기법
            
        
    
