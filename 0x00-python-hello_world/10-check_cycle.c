#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *previous = list;

	if (list == NULL)
	{
		return (0);
	}
	list = list->next;
	while (list != NULL)
	{
		if (previous <= list)
		{
			return (1);
		}
		previous = list;
		list = list->next;
	}
	return (0);
}
