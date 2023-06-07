#include "lists.h"

/**
 * insert_node - insert a new node with n = number to listint_t
 * @head: head of the list
 * @number: n value of new node
 * Return: address of new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *buffer = *head;

	listint_t *new = (listint_t *) malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (buffer == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (number < buffer->n)
	{
		new->next = buffer;
		*head = new;
		return (new);
	}
	while (buffer != NULL)
	{
		if (number >= buffer->n &&
				(buffer->next == NULL || number <= buffer->next->n))
		{
			new->next = buffer->next;
			buffer->next = new;
			break;
		}
		buffer = buffer->next;
	}
	return (new);
}
