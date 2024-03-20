#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a,
 * palindrome.
 * @head: double points to head of the list.
 *
 * Return: 1 if given list is a palindrome. 0 if otherwise.
 */
int is_palindrome(listint_t **head)
{
	int palindr[10000];
	int a, n = 0;
	listint_t *traverse;

	if (head == NULL)
		return (0);

	/* copy numbers from linked list to palindr */
	traverse = *head;
	while (traverse)
	{
		palindr[n++] = traverse->n;
		traverse = traverse->next;
	}

	/* checks if palindr is a palindrome */
	for (a = 0; a < n / 2; a++)
	{
		if (palindr[a] != palindr[n - a - 1])
			return (0);
	}
	return (1);
}
