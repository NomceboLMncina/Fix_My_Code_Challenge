#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - Prints all the integers in a doubly linked list
 *
 * @h: Pointer to the first node of the list
 *
 * Return: The number of nodes printed
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t n;

    n = 0;
    while (h)
    {
        printf("%d\n", h->n);
        h = h->next;
        n++;
    }
    return (n);
}
