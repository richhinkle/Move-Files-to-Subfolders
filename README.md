# Move Files to Subfolders

This Python script organizes files in a directory by creating a subfolder for each file and moving the file into it.

## How to Use

1.  Place the `makedirectory.py` script into the directory containing the files you want to organize.
2.  Run the script from your terminal:
    ```bash
    python makedirectory.py
    ```

## Example

If you have a directory with the following files:

```
- my_document.txt
- another_file.pdf
- image.jpg
- makedirectory.py
```

After running the script, the directory structure will be:

```
- my_document/
  - my_document.txt
- another_file/
  - another_file.pdf
- image/
  - image.jpg
- makedirectory.py
```
