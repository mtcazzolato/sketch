# Sketch-GUI

## Source files

The source code of Sketch-GUI is organized into four main modules:

 - **Main** screen for data loading and selection.  
 - **Similarity Search and Tuple Correlation**  
 - **Association Rules with Lift Correlation**  
 - **Analysis of Variance (ANOVA)**  

The file extensions refer to:

 - *file.py* and *file.tcl* files: Files used to edit the user interface and functionalities. In case the user wants to customize the tool, we recommend using the PAGE GUI generator ([available here](http://page.sourceforge.net/))  
 - *file_support.py*: Files to control the user interface and call the modules of Sketch  

Folder **sketch_modules** has the python scripts implementing the main modules of Sketch-GUI.

## Requirements

File *requirements.txt* lists the python libraries required to run Sketch-GUI.

## Running the tool

On Linux (via terminal) and on Windows (via shell), type:

> *python main.py*

