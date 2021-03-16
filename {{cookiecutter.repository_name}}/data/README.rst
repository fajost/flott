This directory contains all data files used in the process.

The ``test`` subdirectory should usually contain sampled subsets of the actual data to allow test cases to run quickly on data. In our case, we have added the same file as the data is similar size. If you use DVC, this comes at no additional memory requirement.

Note: please make sure to manage the data via DVC and **do not** check-in data files into Git directly. You can delete
the ``.gitignore`` file in this folder, after removing the example files.
