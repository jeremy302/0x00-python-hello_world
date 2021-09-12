#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks is a list is a palindrome
 * @head: head of the list
 *
 * Return: 1 if the list is a palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int nums_[100000], *nums = NULL, i = 0, len = 0;

	if (head == NULL || *head == NULL || head[0]->next == NULL)
		return (head != NULL);
	current = *head;
	while (current)
		++len, current = current->next;
	if (len / 2 <= 100000)
		nums = nums_;
	else
		nums = malloc(sizeof(int) * (len / 2));
	current = *head;
	for (i = 0; i < len / 2; ++i)
		nums[i] = current->n, current = current->next;
	if (len % 2)
		current = current->next;
	for (--i; i >= 0; --i, current = current->next)
		if (current->n != nums[i])
			return (free(nums == nums_ ? NULL : nums), 0);
	return (free(nums == nums_ ? NULL : nums), 1);
}
