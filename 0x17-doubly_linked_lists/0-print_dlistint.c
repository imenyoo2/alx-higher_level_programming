#include "lists.h"


size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *buffer = h;

	while (buffer)
	{
		printf("%d\n", buffer->n);
		buffer = buffer->next;
		count++;
	}
	return (count);
}
