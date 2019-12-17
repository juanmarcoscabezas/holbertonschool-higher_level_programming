#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * Description: Thid function checks is a linked list is a palindrome
 * @head: Head of the singly linked list
 * Return: 0 if it is not palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *end, *start;
	int len = 0, first = 0, last = 0;

	if (!head || !*head)
		return (0);
	end = *head;
	start = *head;

	while (end->next)
	{
		end = end->next;
		start = start->next;
		len++;
	}
	end = *head;
	start = *head;
	while (first < len)
	{
		last = first;
		end = start;
		while (last < len && end->next)
		{
			printf("EN WHILE\n");
			end = end->next;
			last++;
		}
		printf("%d - %d\n", start->n, end->n);
		if (start->n != end->n)
			return (0);
		printf("ANTES\n");
		start = start->next;
		printf("DESPUES");
		first++;
		len--;
	}
	return (1);
}
