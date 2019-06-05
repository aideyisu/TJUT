#include<stdio.h>

//快速幂 a*b(mod m)=((a mod m)*(b mod m))mod m
long long quickpower(long long x,long long y,int n){
	long long ans,cnt;
	ans=1;
	cnt=x;
	while(y){
		if(y&1){
			ans=(ans%n)*(cnt%n)%n;
		}
		cnt=(cnt%n)*(cnt%n)%n;
		y>>=1;
	}
	return ans;
}

//扩展欧几里德
int Exgcd(int a,int b,int &x,int &y){
	if(b==0){
		x=1,y=0;
	//	printf("a=%d b=%d x=%d y=%d\n",a,b,x,y);
		return a;
	}
	int q=Exgcd(b,a%b,x,y);
	int t1,t2;
	t1=x;
	t2=y;
	x=t2;
	y=t1-(a/b)*t2;
	//printf("t1=%d t2=%d a=%d b=%d x=%d y=%d\n",t1,t2,a,b,x,y);
	return q;
		
}

//gcd
int gcd(int a,int b){
	int r;
	while(1){
		r=a%b;
		if(r==0){
			break;
		}
		else{
			a=b;
			b=r;
		}
	}
	return b;
	}

//寻找互素的数(最小互质数） 
int coprime(int x){
	for(int i=2;i<x;i++){
		if(gcd(i,x)==1)
		return i;
	}
}

//加密
int encrypt(int m,int e,int n) {
	int c;
	c=quickpower(m,e,n);
	return c;	
}

//解密
int decode(int c,int d,int n){
	int m;
	m=quickpower(c,d,n);
	return m;
} 
int main(){
	int p,q,n,fai_n,e,d,x,y;
	printf("欢迎使用本次RSA加密！\n");
	printf("请输入两个大素数：\n");
	scanf("%d %d",&p,&q);
	n=p*q;
	fai_n=(p-1)*(q-1);
	e=coprime(fai_n);
	Exgcd(e,fai_n,x,y);
	d=(x+fai_n)%n;
	printf("0->退出         1->加密        2->解密     （请输入0或1或2）\n");
	while(1){
	int flag;
	scanf("%d",&flag);
	if(flag==0){
		printf("感谢使用本产品\n");
		break;
	}
	if(flag==1){
		printf("请以ASCII形式输入明文：\n");
		int m;
		scanf("%d",&m);
		printf("密文： c=%d\n",encrypt(m,e,n));
	}
	if(flag==2){
		printf("请以ASCII形式输入密文：\n");
		int c;
		scanf("%d",&c);
		printf("明文： m=%d\n",decode(c,d,n));
	}
	else{
		printf("非法输入，请输入 0或1或2\n");
	}
}
	return 0;
} 
