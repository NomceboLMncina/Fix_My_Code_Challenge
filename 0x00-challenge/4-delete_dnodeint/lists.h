#ifndef _LISTS_H_
#define _LISTS_H_

#include <stddef.h>

/**
 * struct dlistint_s - Doubly linked list node
 * @n: Integer data
 * @prev: Points to the previous node
 * @next: Points to the next node
 *
 * Description: Represents a node in a doubly linked list.
 */
typedef struct dlistint_s
{
    int n;                    /**< Integer data */
    struct dlistint_s *prev;  /**< Points to the previous node */
    struct dlistint_s *next;  /**< Points to the next node */
} dlistint_t;

/**
 * print_dlistint - Prints all elements of a doubly linked list
 * @h: Head of the list
 * 
 * Return: Number of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h);

/**
 * add_dnodeint_end - Adds a new node at the end of the list
 * @head: Pointer to the head of the list
 * @n: Integer data for the new node
 * 
 * Return: Pointer to the new node, or NULL on failure
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);

/**
 * delete_dnodeint_at_index - Deletes the node at a given index
 * @head: Pointer to the head of the list
 * @index: Index of the node to delete
 * 
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index);

/**
 * free_dlistint - Frees all nodes in the list
 * @head: Head of the list
 */
void free_dlistint(dlistint_t *head);

#endif
