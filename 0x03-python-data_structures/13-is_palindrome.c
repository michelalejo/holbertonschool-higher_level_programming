#include "lists.h"
/**
 * is_palindrome - Funtion that checks if a singly linked list is a palindrome.
 * @head: Head.
 * Return: 1 or 0.
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, buf[1024];
	listint_t *pal = *head;

	if (!head)
		return (0);

	if (!*head || (*head)->next == NULL)
		return (1);

	for (i = 0; pal; pal = pal->next, i++)
		buf[i] = pal->n;

	for (j = 0, i--; i > j; i--, j++)
	{
		if (buf[j] == buf[i])
			;
		else
			return (0);
	}
	return (1);
}
