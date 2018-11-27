#include <bits/stdc++.h>
using namespace std;

class every_jiedian{
	public:
		string name;
		float weight;
		string bianma;
};

void BianMa(every_jiedian);

int main(){
	int number;
	cout << "请输入变量的数目";
	cin >> number;
	cout << "你的选择数量是 : " << number << endl;
	
	every_jiedian sum[number], copy[number]; // 在之后对于copy进行操作 
	for (int i = 1; i <= number ; i++){
		cout << "第" << i << "个节点的名称 & 权重" ;
		cin >> sum[i-1].name >> sum[i-1].weight;
		
		copy[i-1].name = sum[i-1].name;
		copy[i-1].weight = sum[i-1].weight;		
		copy[i-1].bianma = "";  
	} // 依次录入数据 
	
	while(1){
	int	first_site, second_site;
	float first_data = 0,second_data = 0;
	second_site = -1;
	
	
		first_site = 0;
	 	first_data = copy[0].weight;
	 	for (int i = 1; i <= number ; i++){
	 		if (first_data > copy[i-1].weight){
	 			cout << "更新最小数值 从  " << first_data << "   到   " << copy[i-1].weight  << endl;  
	 			first_data = copy[i-1].weight;
	 			first_site = i-1;
	 		}
	 	}
		 cout << "最小" << first_data << " " << first_site << endl;  // right
		  
		  for (int i = 0; i < number; i++){
		  	if(i != first_site){
		  		second_data = copy[i].weight;
		  		cout << "设置second_data " << second_data << endl;
				  break;  
		  	}
		  }
	 	
	 	for (int i = 0; i < number; i++){
	 		if(copy[i].weight < second_data && copy[i].weight > first_data){
	 			second_data = copy[i].weight;
	 			second_site = i;
	 			cout << "设置 次小" << endl;
	 		}
	 	}
	 	
	 	cout << "最小\t" << first_data << "  " << first_site+1 << endl;
	 	cout << "次小\t" <<second_data << "  " << second_site+1 << endl; // right
	 	
	 	
	 	
	 	// 将first second分别设置为当前第一小，和第二小的元素 
	 	float bothdata ;
		bothdata = first_data + second_data; //权值相加
		float temp_bothdata;
		temp_bothdata = bothdata * 1;  // 将操作以后的数设置为负数 
		
		copy[first_site].bianma = " 0" + copy[first_site].bianma;
		copy[second_site].bianma = " 1" + copy[second_site].bianma;
		
	 	copy[first_site].weight = temp_bothdata;
		copy[second_site].weight = temp_bothdata;
		//将两个操纵位置的数值设置为对应数值的相反数
		//经过验证相同的相反数不可能出现
		//所以用相反数的形式可以判断是否操作过。
		
		// 对于编码区域进行操作 
		cout << "将二者合并 数值为\t" << bothdata << endl;  
	 
	 	for(int i = 0; i < number ; i++){
	 		cout << "当前编码  ";
	 		cout << copy[i].name  << "\t";
		 	cout << copy[i].weight << "\t";
		 	cout << copy[i].bianma << endl;
	 	}
		int agr, K = 0;
		agr = copy[0].weight;
		for(int i = 0; i < number ; i++){
			if(agr != copy[i].weight){
				cout << "不满足条件，继续进行循环" << endl;
				K = 1;
				break; 
			}
		}
	 	
	 	if(K == 0){
	 		cout << "满足条件,编码完成"  << endl; 
	 	}
	}
}




