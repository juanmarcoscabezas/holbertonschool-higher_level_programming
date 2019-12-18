#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * Description: Thid function checks is a linked list is a palindrome
 * @head: Head of the singly linked list
 * Return: 0 if it is not palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int array[5000];
	int len = 0, start = 0, end = 0;

	if (!head || !*head)
		return (1);
	node = *head;

	while (node)
	{
		array[len] = node->n;
		node = node->next;
		len++;
	}
	end = len - 1;
	while (start < end)
	{
		if (array[start] != array[end])
			return (0);
		start++;
		end--;
	}
	return (1);
}
