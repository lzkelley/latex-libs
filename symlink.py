"""Create symlinks from local files to appropriate library folders in user directory.

Usage:
    In the latex-libs root directory, run:
    $ python symlink.py

Functions
---------
-   main            - API Function executed by running this script.
-   getFiles        - Find files in target directory, construct symlink names.
-   create_symlink  - Unlink an existing symbolic-link if it exists, create symlink.

"""
import os
import shutil
import warnings

from pathlib import Path

DIRS = [
    ["./styles/", "/Users/lzkelley/Library/texmf/tex/latex/local/"],
    ["./biblio/", "/Users/lzkelley/Library/texmf/bibtex/bst/"],
    # ["./templates/", "/Users/lzkelley/Library/TeXShop/Templates/"]
]

VERBOSE = True
TEST = False
COPY_INSTEAD_OF_SYMLINK = False
CREATE_DIRS = True


def main():
    # Iterate over directories
    for (din, dout) in DIRS:
        # Get input and output (symlink) file names
        fin, fout = getFiles(din, dout)
    
        # Create links
        for infile, outfile in zip(fin, fout):
            path = Path(outfile).expanduser()
            if CREATE_DIRS:
                print(f"Creating directory: '{path.parent}'")
                path.parent.mkdir(parents=True, exist_ok=True)

            if not path.parent.is_dir():
                raise RuntimeError(f"path does not exist!  '{path.parent}' !")
                
            create_symlink(infile, outfile)

    return

    # Create links for all these files
    createLinks(yesFiles)
    # Tell user about any files NOT linked
    otherFiles = nonLinks(yesFiles)
    return


def getFiles(din, dout):
    if VERBOSE:
        print("Dir: '{}'".format(din))
    fin = []
    fout = []
    # Iterate over files in directory
    temp = os.listdir(din)
    for tt in temp:
        # Filter out hidden and emacs-backup files
        if not tt.startswith(".") and not tt.endswith("~"):
            # Append input-filename
            f_in = os.path.join(din, tt)
            f_in = os.path.abspath(f_in)
            fin.append(f_in)
            # Create output-filename
            t_dir, t_fil = os.path.split(tt)
            f_out = os.path.join(dout, t_fil)
            # Append
            f_out = os.path.abspath(f_out)
            fout.append(f_out)
            if VERBOSE: print("\t'{}' ---> '{}'".format(f_in, f_out))

    return fin, fout


def create_symlink(src, dest):
    if os.path.islink(dest):
        try:
            if VERBOSE: print("> unlink '{}'".format(dest))
            if not TEST: os.unlink(dest)
        except Exception as err:
            warnings.warn(str(err))

        try:
            if VERBOSE: print("> delete '{}'".format(dest))
            if not TEST: os.remove(dest)
        except Exception as err:
            warnings.warn(str(err))


    if COPY_INSTEAD_OF_SYMLINK:
        if VERBOSE: print(">\tcopy '{}' ---> '{}'.".format(src, dest))
        if not TEST: shutil.copyfile(src, dest)
    else:
        if VERBOSE: print(">\tsymlink '{}' ---> '{}'.".format(src, dest))
        if not TEST: os.symlink(src, dest)
    return


    
if __name__ == "__main__": 
    main()
