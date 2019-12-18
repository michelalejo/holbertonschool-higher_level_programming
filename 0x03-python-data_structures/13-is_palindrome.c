#include "lists.h"
/**
 * is_palindrome - Funtion that checks if a singly linked list is a palindrome
 * @head: Head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *poli;
	int i = 0, j = 0;
	int buf[4096];


	if (!head)
		return (0);
	poli = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (i = 0; poli; poli = poli->next, i++)
		buf[i] = poli->n;
	for (j = 0, i--; i > j; i--, j++)
	{
		if (buf[j] == buf[i])
			;
		else
			return (0);
	}
	return (1);
}
