#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - will add to sorted list
 * @head: head of the list
 * @number: number to be added
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head, *temp = NULL, *tm;

	temp = malloc(sizeof(listint_t));

	if (temp == NULL)
	{
		return (NULL);
	}

	temp->n = number;
	temp->next = NULL;

	if (h == NULL || h->n > number)
	{
		temp->next = h;
		*head = temp;
		return (temp);
	}

	while (h->next != NULL && h->next->n < number)
	{
		h = h->next;
	}

	tm = h->next;
	h->next = temp;
	temp->next = tm;

	return (temp);
}
