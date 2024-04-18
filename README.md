# ieeevis-area-curation-committee-reports

## Installation

Install [quarto](https://quarto.org/docs/get-started/) to generate the final document.


Install an Anaconda distribution, either:
- [Miniforge3](https://conda-forge.org/miniforge/) (recommended),
- [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), or
- [Anaconda](https://docs.anaconda.com/free/anaconda/install/) if you wish.

Once installed, you can create a virtual environment to avoid breaking your applications:


``` sh
conda create -n acc python=3.10
conda activate acc
conda install jupyterlab pandas matplotlib plotly scipy scikit-learn
```

Connect to the 2023 directory and use quarto to generate the report.

``` shell
quarto preview Analysis\ 2023.ipynb 
```

Quarto will generate the Analysis\ 2023.html file and show it in browser.

You can also open the .ipynb file as a JupyterLab notebook to edit it.

### Added quatro file and report from 2022 
- Steven Drucker


### Raw data for report kept in seperate folder:
- ieee-vgtc/ieeevis-area-chair-committee-data 
