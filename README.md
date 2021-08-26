# Hej och välkommen till din första pythonkurs!

## Smidigt tips för nya conda environments med jupyter notebook

För att automatiskt registrera ett ny environment för att använda med notebooks kan man installera ett paket i sitt 'base' environment. 
Detta behöver du bara göra en gång! 

#### Installera notebook och nb_conda_kernels i din base environment. Detta behöver du endast göra en gång.

	
	conda activate base

	conda install -c conda-forge notebook nb_conda_kernels

#### Nästa gång du vill skapa ett nytt conda environment

Skapa ditt environment och installera python och ipykernel. Välj själv namn istället för NEW_ENV. Eftersom vi installerar ipykernel så kommer nb_conda_kernels automatiskt registrera det


	conda create --name NEW_ENV python=3.9 ipykernel

#### Alternativ 1: Använda ditt nya environment med jupyter notebooks i webbläsaren
Du kan nu prova att starta en notebook server från ditt base conda environment med:

    jupyter notebook

Om du skapar en ny notebook så kommer du kunna välja en kernel med namnet Python [conda env: NEW_ENV]

#### Altenativ 2: Skapa en notebook i VSCode

1. I VSCode, skapa en ny notebook med ctrl + shift + p
2. Sök på 'Jupyter: Create New Blank Notebook' och välj det
3. I övre högra hörnet finns en knapp för att välja kernel. Tryck på den och sök på din NEW_ENV


## Kurslitteratur

Vi kommer använda många olika resurser för att lära oss om python, men vi kommer till stor del att använda oss av Jake VanderPlas *A whirlwind tour of python* och *Python data science handbook*. 
Båda böckerna är gratis och tillgängliga på författarens github både som text och som jupyter notebooks. För att ta till sig materialet rekommenderar vi starkt att ni kör all kod själva när ni läser!

Länkar till böckerna:
- [WIP](https://jakevdp.github.io/WhirlwindTourOfPython/) 
- [PDS handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)


// era kursledare Isabella Gagner och Alexander Hagelborn
