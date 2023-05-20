#include "lists.h"
#include<stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly
 * linked list
 * @head: double pointer to head of the linked list
 * @number: data for the new node in the linked list
 * 
 * Return: pointer to the new node, or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node, *tmp;

    if (head == NULL)
        return (NULL);

    node = malloc(sizeof(listint_t));
    if (node == NULL)
        return (NULL);
    node->n = number;
    node->next = NULL;
    if (*head == NULL)
    {
        *head = node;
        return (node);
    }

    tmp = *head;
    while (tmp->next != NULL && tmp->next->n < number)
    {
        tmp = tmp->next;
    }
    node->next = tmp->next;
    tmp->next = node;
    return (node);
}
