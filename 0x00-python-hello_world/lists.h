#ifndef LISTS_H_
#define LISTS_H_


#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */
int check_cycle(listint_t *list);

#endif /*LISTS_H_*/
