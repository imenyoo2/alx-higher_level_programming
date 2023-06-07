#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *previous = list;

	if (list == NULL)
	{
		return (0);
	}
	while (list != NULL)
	{
		list = list->next;
		if (previous == NULL)
		{
			return (0);
		}
		if (previous < list)
		{
			return (1);
		}
		previous = list;
	}
	return (0);
}
