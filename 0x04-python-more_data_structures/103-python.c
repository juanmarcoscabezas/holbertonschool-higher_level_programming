#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints a python list
 * Description: This function prints a python list
 * @p: PyObject
 * Return:
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *element = p;

	list = (PyListObject *) p;
	int size = (((PyVarObject *)(p))->ob_size);
	int i;
	const char *name = NULL;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int) list->allocated);
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		name = (((PyObject *)(element))->ob_type)->tp_name;
		printf("Element %d: %s\n", i, name);
		if (strcmp(name, "bytes") == 0)
			print_python_bytes(element);
	}
}

/**
 * print_python_bytes - Prints python bytes
 * Description: This function prints python bytes
 * @p: PyObject
 * Return:
 */
void print_python_bytes(PyObject *p)
{
	int size = (((PyVarObject *)(p))->ob_size);
	int counter = 0, limit = 10;
	char *string = NULL;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		string = PyBytes_AsString(p);
		printf("size: %d\n", size);
		printf("trying string: %s\n", string);
		if (size < limit)
			limit = size;
		printf("first %d bytes:", limit + 1);
		for (counter = 0; counter < limit; counter++)
		{
			printf(" %02x", string[counter]);
		}
		printf("\n");
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}
