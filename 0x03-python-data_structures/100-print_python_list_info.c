#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info -  Prints the info of a python list
 * @p: Python object
 * @Return:
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), i;
	PyListObject *obj = (PyListObject *) p;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int) obj->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, (char *) item->ob_type->tp_name);
	}
}
