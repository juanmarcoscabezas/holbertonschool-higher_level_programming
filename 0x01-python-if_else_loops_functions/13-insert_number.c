#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Head of the linked list
 * @number: Number to inser into @head
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *actual_node = *head;

	listint_t *new_node;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (new_node->n < actual_node->n)
	{
		new_node->next = actual_node;
		*head = new_node;
		return (new_node);
	}
		
	while (actual_node)
	{
		if (new_node->n < actual_node->n)
		{
			new_node->next = actual_node->next;
			actual_node->next = new_node;
			new_node->n = actual_node->n;
			actual_node->n = number;
			return (actual_node);
		}
		if (actual_node->next == NULL)
		{
			actual_node->next = new_node;
			break;
		}
		actual_node = actual_node->next;
	}
	return (new_node);
}
