#include <stdio.h>
#include <conio.h>

int visited[7] = {0, 0, 0, 0, 0, 0, 0};
int A[7][7] = {
    {0, 1, 1, 1, 0, 0, 0},
    {1, 0, 1, 0, 0, 0, 0},
    {1, 1, 0, 1, 1, 0, 0},
    {1, 0, 1, 0, 1, 0, 0},
    {0, 0, 1, 1, 0, 1, 1},
    {0, 0, 0, 0, 1, 0, 0},
    {0, 0, 0, 0, 1, 0, 0}
};

void DFS(int i)
{
    int j;
    printf("%d ", i);
    visited[i] = 1;
    for (j = 0; j < 7; j++)
    {
        if (A[i][j] == 1 && visited[j] == 0)
        {
            DFS(j);
        }
    }
}

void main()
{
    clrscr();
    printf("The DFS is: ");
    DFS(0);
    getch();
}