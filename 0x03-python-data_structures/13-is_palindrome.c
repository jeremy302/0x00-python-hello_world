#include "lists.h"

/**
 * is_palindrome - checks is a list is a palindrome
 * @head: head of the list
 *
 * Return: 1 if the list is a palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int *nums = NULL, i = 0, len = 0;

	if (head == NULL || *head == NULL || head[0]->next == NULL)
		return (head != NULL);
	current = *head;
	while (current)
		len++, current = current->next;
	nums = malloc(sizeof(int) * len);
	current = *head;
	while (current)
		nums[i++] = current->n, current = current->next;
	for (i = 0; i < (len / 2) + (len % 2); i++)
		if (nums[i] != nums[len - i - 1])
			return (free(nums), 0);
	return (free(nums), 1);
}
