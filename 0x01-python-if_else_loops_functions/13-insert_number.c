#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted linked list.
 *
 * @head: Pointer to the head of the linked list.
 * @number: Value to be inserted into the new node.
 *
 * Return: Address of the new node or NULL if memory allocation fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;

        /* Allocate memory for the new node */
        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);

        /* Initialize the value of the new node */
        new->n = number;

        /* Insert the new node at the beginning if the list is empty or the new value is smaller */
        if (node == NULL || node->n >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        /* Traverse the list to find the correct position for the new node */
        while (node && node->next && node->next->n < number)
                node = node->next;

        /* Insert the new node into the sorted linked list */
        new->next = node->next;
        node->next = new;

        return (new);
}
