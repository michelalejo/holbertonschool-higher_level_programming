#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Funtion to know if the ir a cycle in a linked list.
 * @list: Struct / list to be checked.
 * Return: 0 - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *y = list;

	while (x != NULL && y != NULL && x->next != NULL)
	{
		x = x->next->next, y = y->next;
		if (x == y)
			return (1);
	}
	return (0);
}
