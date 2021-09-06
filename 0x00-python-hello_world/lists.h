#include "lists.h"

/**
 * check_cycl - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
listint_t *fast = list, *slow = list;
if (list != NULL)
{
while (fast && fast->next)
{
fast = fast->next->next;
slow = slow->next;
if (slow == fast)
{
fast = list;
while (slow != fast)
{
slow = slow->next;
fast = fast->next;
}
return (1);
}
}
}
return (0);
}
