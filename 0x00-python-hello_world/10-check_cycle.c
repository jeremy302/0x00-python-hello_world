#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if there is a cycle in the list
 * @list: a linked list
 *
 * Return: 1 if there is a cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list == NULL ? NULL : list->next,  *tortoise = list;

	while (hare != NULL && hare != tortoise)
	{
		hare = hare->next;
		tortoise = hare == tortoise ? tortoise : tortoise->next;
		hare = hare == tortoise || hare == NULL ? hare : hare->next;
	}
	return (hare != NULL);
}
