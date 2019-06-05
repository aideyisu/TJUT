#include<stdio.h>

//������ a*b(mod m)=((a mod m)*(b mod m))mod m
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

//��չŷ�����
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

//Ѱ�һ��ص���(��С�������� 
int coprime(int x){
	for(int i=2;i<x;i++){
		if(gcd(i,x)==1)
		return i;
	}
}

//����
int encrypt(int m,int e,int n) {
	int c;
	c=quickpower(m,e,n);
	return c;	
}

//����
int decode(int c,int d,int n){
	int m;
	m=quickpower(c,d,n);
	return m;
} 
int main(){
	int p,q,n,fai_n,e,d,x,y;
	printf("��ӭʹ�ñ���RSA���ܣ�\n");
	printf("������������������\n");
	scanf("%d %d",&p,&q);
	n=p*q;
	fai_n=(p-1)*(q-1);
	e=coprime(fai_n);
	Exgcd(e,fai_n,x,y);
	d=(x+fai_n)%n;
	printf("0->�˳�         1->����        2->����     ��������0��1��2��\n");
	while(1){
	int flag;
	scanf("%d",&flag);
	if(flag==0){
		printf("��лʹ�ñ���Ʒ\n");
		break;
	}
	if(flag==1){
		printf("����ASCII��ʽ�������ģ�\n");
		int m;
		scanf("%d",&m);
		printf("���ģ� c=%d\n",encrypt(m,e,n));
	}
	if(flag==2){
		printf("����ASCII��ʽ�������ģ�\n");
		int c;
		scanf("%d",&c);
		printf("���ģ� m=%d\n",decode(c,d,n));
	}
	else{
		printf("�Ƿ����룬������ 0��1��2\n");
	}
}
	return 0;
} 
