typedef int ElemType;
struct BiTNode{
	ElemType data;
	struct BiTNode * lchild, * rchild; 
};


void CreateBiTree(BiTNode * T){
	ElemType ch;
	scanf("%d", &ch);getchar();
	if (ch == 0)
		*T = NULL;
	else{
		*T = (BiTree) malloc (sizeof(BiTNode));
		(*T)->data = ch;
		CreateBiTree(&(*T)->lchild);
		CreratBiTree(&(*T)->rchild);
	}
} 
