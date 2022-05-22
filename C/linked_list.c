
#include <stdio.h>
#include <stdlib.h>

typedef struct n
{
  int   x;
  char  y;
  struct n * next;
}           node;

int main()
{
  //Linked list oluşturma eleman ekleme ve listede gezme
  int i = 1;
  node * root;
  root = (node *)malloc(sizeof(node));
  root -> x = 10;
  root -> next = (node *) malloc (sizeof(node));
  root -> next -> x = 20;
  root -> next -> next = (node *) malloc (sizeof(node));
  root -> next -> next -> x = 30;
  root -> next -> next -> next = (node *) malloc (sizeof(node));
  root -> next -> next -> next -> x = 40;
  root -> next -> next -> next -> next = (node *) malloc (sizeof(node));
  root -> next -> next -> next -> next -> x = 50;
  root -> next -> next -> next -> next -> next = (node *) malloc (sizeof(node));
  node * iter;
  iter = root;
  while (iter -> x != '\0')
  {
    printf("%d:%d\n",i ,iter ->x);
    iter = iter -> next;
    i++; 
  }
}