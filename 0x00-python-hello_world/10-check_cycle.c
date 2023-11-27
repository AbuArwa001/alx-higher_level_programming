#include "lists.h"


/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *ptr1 =  list, *ptr2 = list;

    while (ptr2 != NULL && ptr2->next !=  NULL)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;
        if (ptr1 == ptr2)
        {
            return (1);
        }

    }
    return (0);
}
