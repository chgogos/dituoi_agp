# Cython examples

Κώδικας από το <https://medium.com/easyread/run-python-code-hundreds-of-times-faster-716f4da20669>

* Κώδικας σε python [example_py.py](./example_py.py)
* Κώδικας σε cython [example_cy.pyx](./example_cy.pyx)
* [setup.py](./setup.py)

Δημιουργία του object file
```
$ python setup.py build_ext --inplace
```

* Κλήση κώδικα cython [call_cython_code_example_cy](./call_cython_code_example_cy) 
* Χρονομέτρηση κώδικα [timing_code.py](./timing_code.py)