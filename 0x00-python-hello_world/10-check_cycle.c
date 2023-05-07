#include"lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to a node in the list (probably head)
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		tmp = list->next;
		while (tmp != NULL)
		{
			if (tmp == list)
				return (1);
			tmp = tmp->next;
		}
		list = list->next;
	}
	return (0);
}
