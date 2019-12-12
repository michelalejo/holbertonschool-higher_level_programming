#include "lists.h"
/**
 * insert_node - Adds new node to a listint_t list.
 * @number: New node.
 * @head: First.
 * Return: New address or null.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p, *q, *h;
	unsigned int i = 0;

	if (head == NULL)
		return (0);
	p = malloc(sizeof(listint_t));
	if (p == NULL)
	{free(p);
		return (NULL);}
	if (*head == NULL)
	{p->n = number;
		p->next = NULL;
		*head = p;
		return (p);}
	h = *head;
	p->n = number;
	for (; p->n > h->n && h != NULL; q = h,
		     h = h->next, i++)
	{
		if (h->next == NULL)
			break;}
	if (h->next != NULL)
	{
		if (i != 0)
		{
			q->next = p;
			p->next = h;}
		else
		{
			p->next = *head;
			*head = p;
		}
	}
	else
	{
		h->next = p;
		p->next = NULL;
	}
	return (p);
}
