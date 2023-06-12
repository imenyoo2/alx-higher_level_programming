#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    int len, i = 0, check = 1;
    listint_t *buffer;
    int *arr;

    if (head == NULL || *head == NULL)
    {
        return 0;
    }
    buffer = *head;
    len = len_list(head);
    arr = (int *) malloc(sizeof(int) * len / 2);
    if (arr == NULL)
    {
        return (0);
    }
    
    while (buffer != NULL)
    {
        if (i < len / 2)
        {
            arr[i] = buffer->n;
            buffer = buffer->next;
            i++;
        }
        else
        {
            if (arr[len/2 - 1 - (i - len/2)] != buffer->n)
            {
                check = 0;
                break;
            }
            buffer = buffer->next;
            i++;
        }
    }
    free(arr);
    return (check);
}
