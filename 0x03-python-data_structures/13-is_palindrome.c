#include "lists.h"
/**
 * is_palindrome - Funtion that checks if a singly linked list is a palindrome
 * @head: Head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, *buf, buffer = 1024, n = 1;
	listint_t *poli;

	buf = malloc(sizeof(int) * buffer * n);
	if (!buf)
		return (0);

	if (!head)
		return (0);
	poli = *head;
	if (!*head || (*head)->next == NULL)
		return (1);

	for (i = 0; poli; poli = poli->next, i++)
	{
		if (i % 1000 == 0)
		{
			n++;
			buf = realloc(buf, sizeof(int) * buffer * n);
		}
		buf[i] = poli->n;
	}
	for (j = 0, i--; i > j; i--, j++)
	{
		if (buf[j] != buf[i])
			return (0);
	}
	return (1);
}
