#include "lists.h"
/**
 * is_palindrome - test if a LL is also a palindrome
 * @head: begining of list
 * Return: 1 for yes, 0 for no or fail
 */
int is_palindrome(listint_t **head)
{
	listint_t *pal;
	int i = 0, j = 0;
	int arr[1024];


	if (!head)
		return (0);
	pal = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (; pal; pal = pal->next, i++)
		buf[i] = pal->n;
	for (i--; i > j; i--, j++)
	{
		if (buf[j] == buf[i])
			;
		else
			return (0);
	}
	return (1);
}
