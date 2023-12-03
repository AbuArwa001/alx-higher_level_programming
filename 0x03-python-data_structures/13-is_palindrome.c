#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: the head or start of the list
 * Return: returns 1 if palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next, *temp;

	if (!slow || !slow->next)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;

		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast)
		slow = slow->next;

	while (prev && slow)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	temp = NULL;
	while (head && *head)
	{
		next = (*head)->next;
		(*head)->next = temp;
		temp = *head;
		*head = next;
	}

	/* *head now points to the new head of the list after reversing */
	*head = temp;

	return (1);
}
