#include "lists.h"

/**
 * insert_node - inserts a node into a sorted list
 * @head: head of the list
 * @number: node value
 *
 * Return: node created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t)), *prev = NULL, *current = *head;

	if (node == NULL || head == NULL)
		return (free(node), NULL);
	node->n = number, node->next = NULL;
	if (*head == NULL)
		return (*head = node, node);
	while (current != NULL && current->n < number)
		prev = current, current = prev->next;
	if (current == NULL)
		prev->next = node;
	else if (current->n >= number)
		(prev == NULL ? (*head = node) : (prev->next = node)), node->next = current;
	return (node);
}
