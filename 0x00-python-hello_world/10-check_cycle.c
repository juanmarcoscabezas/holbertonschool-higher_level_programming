#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: List to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (!list)
		return (0);

	while (tortoise && hare)
	{
		tortoise = tortoise->next;
		hare = (hare->next)->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
