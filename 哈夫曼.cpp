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
	cout << "�������������Ŀ";
	cin >> number;
	cout << "���ѡ�������� : " << number << endl;
	
	every_jiedian sum[number], copy[number]; // ��֮�����copy���в��� 
	for (int i = 1; i <= number ; i++){
		cout << "��" << i << "���ڵ������ & Ȩ��" ;
		cin >> sum[i-1].name >> sum[i-1].weight;
		
		copy[i-1].name = sum[i-1].name;
		copy[i-1].weight = sum[i-1].weight;		
		copy[i-1].bianma = "";  
	} // ����¼������ 
	
	while(1){
	int	first_site, second_site;
	float first_data = 0,second_data = 0;
	second_site = -1;
	
	
		first_site = 0;
	 	first_data = copy[0].weight;
	 	for (int i = 1; i <= number ; i++){
	 		if (first_data > copy[i-1].weight){
	 			cout << "������С��ֵ ��  " << first_data << "   ��   " << copy[i-1].weight  << endl;  
	 			first_data = copy[i-1].weight;
	 			first_site = i-1;
	 		}
	 	}
		 cout << "��С" << first_data << " " << first_site << endl;  // right
		  
		  for (int i = 0; i < number; i++){
		  	if(i != first_site){
		  		second_data = copy[i].weight;
		  		cout << "����second_data " << second_data << endl;
				  break;  
		  	}
		  }
	 	
	 	for (int i = 0; i < number; i++){
	 		if(copy[i].weight < second_data && copy[i].weight > first_data){
	 			second_data = copy[i].weight;
	 			second_site = i;
	 			cout << "���� ��С" << endl;
	 		}
	 	}
	 	
	 	cout << "��С\t" << first_data << "  " << first_site+1 << endl;
	 	cout << "��С\t" <<second_data << "  " << second_site+1 << endl; // right
	 	
	 	
	 	
	 	// ��first second�ֱ�����Ϊ��ǰ��һС���͵ڶ�С��Ԫ�� 
	 	float bothdata ;
		bothdata = first_data + second_data; //Ȩֵ���
		float temp_bothdata;
		temp_bothdata = bothdata * 1;  // �������Ժ��������Ϊ���� 
		
		copy[first_site].bianma = " 0" + copy[first_site].bianma;
		copy[second_site].bianma = " 1" + copy[second_site].bianma;
		
	 	copy[first_site].weight = temp_bothdata;
		copy[second_site].weight = temp_bothdata;
		//����������λ�õ���ֵ����Ϊ��Ӧ��ֵ���෴��
		//������֤��ͬ���෴�������ܳ���
		//�������෴������ʽ�����ж��Ƿ��������
		
		// ���ڱ���������в��� 
		cout << "�����ߺϲ� ��ֵΪ\t" << bothdata << endl;  
	 
	 	for(int i = 0; i < number ; i++){
	 		cout << "��ǰ����  ";
	 		cout << copy[i].name  << "\t";
		 	cout << copy[i].weight << "\t";
		 	cout << copy[i].bianma << endl;
	 	}
		int agr, K = 0;
		agr = copy[0].weight;
		for(int i = 0; i < number ; i++){
			if(agr != copy[i].weight){
				cout << "��������������������ѭ��" << endl;
				K = 1;
				break; 
			}
		}
	 	
	 	if(K == 0){
	 		cout << "��������,�������"  << endl; 
	 	}
	}
}




