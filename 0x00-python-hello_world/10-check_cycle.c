#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle
 * @list: A pointer to the head of the linked list
 *
 * This function determines whether a linked list has a cycle or not.
 * It uses Floyd's Tortoise and Hare algorithm to detect a cycle by having
 * two pointers traverse the list at different speeds.
 *
 * @list: A pointer to the head of the linked list to be checked.
 *
 * Return: 1 if a cycle is detected, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;  /* Tortoise pointer */
        listint_t *fast = list;  /* Hare pointer */

        /* Check if the list is empty */
        if (!list)
                return (0);

        /* Traverse the list with two pointers (Tortoise and Hare) */
        while (slow && fast && fast->next)
                {
                        slow = slow->next;         /* Move the Tortoise one step at a time */
                        fast = fast->next->next;   /* Move the Hare two steps at a time */
                        /* If the Tortoise and Hare meet, a cycle is detected */
                        if (slow == fast)
                                return (1);
                }
        /* If the loop completes without detecting a cycle, return 0 */
        return (0);
}
