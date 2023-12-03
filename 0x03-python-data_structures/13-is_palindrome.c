#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if list is palindrome
 * @head: the head or start of the list
 * Return: returns 1 if palidrome and 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *h = *head, *tail = *head;
	int *arr = NULL, size = 0, i = 0, len = 0;

	if (!h)
		return (1);

	if (!tail->next)
		return (1);

	while (tail)
	{
		tail = tail->next;
		size++;
	}
	arr = malloc(sizeof(int) * size);
	tail = *head;
	while (tail)
	{
		arr[i] = tail->n;
		tail = tail->next;
		i++;
	}
	len = size - 1;
	while (h)
	{
		if (h->n != arr[len])
		{
			free(arr);
			return (0);
		}
		if (len == size / 2 && h->n == arr[len])
		{
			free(arr);
			return (1);
		}
		h = h->next;
		len--;
	}
	free(arr);
	return (1);
}
