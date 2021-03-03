# Παραδείγματα με wxPython 

* <https://www.youtube.com/user/Johnnyboycurtis/videos>

1. Εγκατάσταση miniconda από το <https://docs.conda.io/en/latest/miniconda.html>

2. Δημιουργία virtual environment, ενεργοποίηση virtual environment, εγκατάσταση modules 

    ```
    $ conda create -n myenv python=3.8
    $ conda activate myenv
    $ conda install -c anaconda wxpython
    ```

3. Εκτέλεση κώδικα

    ```
    $ python 01_hello.py
    ```

4. Απενεργοποίηση virtual environment

    ```
    $ conda deactivate
    ```