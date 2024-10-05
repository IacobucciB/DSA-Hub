#include <stdio.h>

struct LinkedListLNode
{
	int data;
	struct LLNode *next;
};
typedef struct LinkedListLNode LLNode;

LLNode* insertAtBegginning(int n, LLNode* L)
{
	LLNode *aux;
	aux = (LLNode *)malloc(sizeof(LLNode));
	
	aux->data = n;
	
	aux->next = L;
	return aux;
}

LLNode* insertAtEnd(int n, LLNode** L)
{
	LLNode *newNode;
	newNode = (LLNode *)malloc(sizeof(LLNode));
	newNode->data = n;
	newNode->sig = NULL;
	
	LLNode *act;
	act = *L;
	if(*L == NULL)
	{
		*L = newNode;
	}
	else
	{
		while(act->next != NULL)
		{
			act = act->next;
		}
		act->next = newNode;
	}
}

int main(void)
{
    printf("Hello World o7");
    return 0;
}