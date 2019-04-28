# coding:utf-8
'''
汉诺塔问题介绍：
在印度，有这么一个古老的传说：在世界中心贝拿勒斯（在印度北部）的圣庙里，一块黄铜板上插着三根宝石针。
印度教的主神梵天在创造世界的时候，在其中一根针上从下到上地穿好了由大到小的64片金片，这就是所谓的汉诺塔。
不论白天黑夜，总有一个僧侣在按照下面的法则移动这些金片，一次只移动一片，不管在哪根针上，小片必在大片上面。
当所有的金片都从梵天穿好的那根针上移到另外一概针上时，世界就将在一声霹雳中消灭，梵塔、庙宇和众生都将同归于尽。

我们首先利用数学上的数列知识来看看F(n=1)=1,F(n=2)=3,F(n=3)=7,F(n=4)=15……F(n)=2F(n-1)+1; 
我们使用数学归纳法可以得出通项式：F(n)=2^n-1。当n为64时F(n=64)=18446744073709551615。 
我们假设移动一次圆盘为一秒，那么一年为31536000秒。那么18446744073709551615/31536000约等于584942417355天，换算成年为5845.54亿年。 
目前太阳寿命约为50亿年，太阳的完整寿命大约100亿年。所以我们整个人类文明都等不到移动完整圆盘的那一天。

'''

def hanoi(n, A, B, C):
    if n == 1:
        move(A, C)
    else:
        hanoi(n-1, A, C, B)
        move(A, C)
        hanoi(n-1, B, A, C)


def move(A, C):
    print ("move:"+A+"-->"+C)

if __name__ == "__main__":
    print "移动汉诺塔的步骤："
    hanoi(3, 'a', 'b', 'c')


'''

//非递归算法（还没仔细看）
int hanota(int num) {
	int max_times;
	int i,k,j;
	int flag;
	int s1,s2,s3,s=0;
	//记录每个盘子位置
	int site[100]={0};
	//判断输入的盘子个数是奇数还是偶数
	if(num%2 == 0)
		flag=1;
	else
		flag=0;
	//求出需要搬动盘子的最大值
	max_times=poww(2, num)-1;
	//根据规律搬动盘子
	for (i=1; i <= max_times; i++){
		//根据规律求出当前步数需要挪动那个盘子
		for(j=num-1; j>=0; j--){
			int temp;
			temp=poww(2,j);
			if(i%temp == 0 && i >= temp )
				break;
		}
		//printf("*****k=%d********\n", j+1);
		k=j+1;
		//根据规律挪动盘子
		if(flag){
			if(k%2 != 0){
				printf("move1 %d from %d to %d \n", k,site[k],(site[k]+1)%3);
				printff(k,site[k],(site[k]+1)%3);
				s=(s+1)%3;
				site[k]=(site[k]+1)%3;
			}
			else{
				printf("move2 %d from %d to %d \n",k,site[k],abs((site[k]-1+3)%3));
				printff(k,site[k],abs((site[k]-1+3)%3));
				s=abs((s-1+3)%3);
				site[k]=abs((site[k]-1+3)%3);
			}
			
		}
		else{
			if(k%2 == 0){
				printf("move3 %d from %d to %d \n", k,site[k],(site[k]+1)%3);
				printff(k,site[k],(site[k]+1)%3);
				s=(s+1)%3;
				site[k]=(site[k]+1)%3;
			}
			else{
				printf("move4 %d from %d to %d \n",k,site[k],abs((site[k]-1+3)%3));
				printff(k,site[k],abs((site[k]-1+3)%3));
				s=abs((s-1+3)%3);
				site[k]=abs((site[k]-1+3)%3);
			}
		
		}
	}

}
	
int main () {
	hanota(6);
	printf("count =%d\n", count);
	return 0;
}

'''