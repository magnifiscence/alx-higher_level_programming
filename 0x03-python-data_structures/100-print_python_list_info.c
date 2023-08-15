#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - prints python list info
 * @p: python
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	int size, j, alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*} Allocated = %d\n", alloc);

	for (j = 0; i < size; i++)
	{
		printf("Element %d: ", j);

		obj = PyList_Getltemp(p, i);
		printf("%s\n", py_type(obj)->tp_name);
	}
}
