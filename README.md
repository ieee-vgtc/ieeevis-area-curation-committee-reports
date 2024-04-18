# ieeevis-area-curation-committee-reports

## Installation

Install [quarto](https://quarto.org/docs/get-started/) to generate the final document.


Install an Anaconda distribution, either:
- [Miniforge3](https://conda-forge.org/miniforge/) (recommended),
- [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), or
- [Anaconda](https://docs.anaconda.com/free/anaconda/install/) if you wish.

Once installed, you can create a virtual environment to avoid breaking your applications:


``` shell
conda create -n acc python=3.10
conda activate acc
conda install jupyterlab pandas matplotlib plotly scipy scikit-learn
```

Connect to the 2023 directory and use quarto to generate the report.

The file "Analysis 2023.ipynb" is a JupyterLab notebook. To edit it, run:
 
``` shell
jupyter lab Analysis\ 2023.ipynb
```

The notebook file should be displayed on your browser, but it has no attached image or computed cells. You need to run the whole notebook using the menu item "Kernel->Restart Kernel and Run All Cells..." to update the visualizations and computed results. It takes a few minutes to finish running.

Then, save the file using the "File -> Save Notebook" menu item. You can then generate the report in htnm format using the following command:


``` shell
quarto preview Analysis\ 2023.ipynb 
```

Quarto will generate the Analysis\ 2023.html file and show it in browser.

Don't try to commit and push the notebook to github.com, it is too large. You need to strip it from all the generated cells first using the "Kernel -> Restart Kernel and Clear Outputs of All Cells..." menu item. Then, save the file again (Ctrl-S), and you can commit and push the file.

If you try to commit the big file, you are in trouble since github.com will not let you do anything since the file is too big. The simplest way out is to rename the local repo, clone the original repo, copy the modified stripped files to the clean repo, and commit/push.

### Added quatro file and report from 2022 
- Steven Drucker


### Raw data for report kept in seperate folder:
- ieee-vgtc/ieeevis-area-chair-committee-data 
