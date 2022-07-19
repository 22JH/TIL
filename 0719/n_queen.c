#include <stdio.h>
#include <stdlib.h>

int *arr;

int abs(int num)
{
	if (num > 0)
		return (num);
	else
		return (-num);
}

void ft_print_queen(int T)
{
	for(int i = 1; i <= T; i++)
		printf("%d\n", arr[i]);
	exit (0);
}
int ft_prom_queen(int col)
{
	int i;
	
	i = 0;
	while (++i < col)
		if (arr[i] == arr[col] || abs(arr[col] - arr[i]) == abs(col - i))
			return(0);
	return (1);
}

void ft_queen(int col, int T)
{
	int row;

	if (ft_prom_queen(col))
	{
		if (col == T)
			ft_print_queen(T);
		else
		{
			for (row = 1; row <= T; row++) 
			{
				arr[col + 1] = row;
				ft_queen(col + 1, T);
			}
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	arr = (int*)malloc(sizeof(int) * (T + 1));
	for (int i = 0; i <= T; i++)
		arr[i] = 0;

	ft_queen(0, T);
}