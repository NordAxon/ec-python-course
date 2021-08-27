# Hej och välkommen till din första pythonkurs!

## TIPS: conda environments med jupyter notebook

För att automatiskt registrera ett ny environment för att använda med notebooks kan man installera ett paket i sitt 'base' environment. 
Detta behöver du bara göra en gång! 

#### 1. Installera `notebook` och `nb_conda_kernels` i din base environment. Detta behöver du endast göra en gång.
	
	conda activate base

	conda install -c conda-forge notebook nb_conda_kernels

#### 2. Nästa gång du vill skapa ett nytt conda environment

Skapa ditt environment och installera `python` och `ipykernel`. __Välj själv namn istället för NEW_ENV__. Eftersom vi installerar `ipykernel` så kommer `nb_conda_kernels` automatiskt att registrera det

	conda create --name NEW_ENV python=3.9 ipykernel

#### 3. När du har aktiverat din NYA environment

__FÖRSTA GÅNGEN__ du aktiverar din miljö ska du inte glömma att installera alla requirements. Se till att du står i samma mapp (folder) som din `requirements.txt` fil finns, och har din environment aktiverad. Du aktiverar den med

	conda activate NEW_ENV

När du har aktiverat din environment så kan du dubbelkolla att din `requirements.txt` fil finns i mappen genom att titta på listan som dyker upp när du kör

	ls
eller 

	dir

När du ser att din `requirements.txt`-fil finns så kör du

	pip install -r requirements.txt

#### 4. Alternativ 1: Använda ditt nya environment med jupyter notebooks i webbläsaren
Du kan nu prova att starta en notebook server från ditt base conda environment med:

    jupyter notebook

Om du skapar en ny notebook så kommer du kunna välja en kernel med namnet Python [conda env: NEW_ENV]

#### 4. Altenativ 2: Skapa en notebook i VSCode

1. I VSCode, skapa en ny notebook med ctrl + shift + p
2. Sök på 'Jupyter: Create New Blank Notebook' och välj det
3. I övre högra hörnet finns en knapp för att välja kernel. Tryck på den och sök på din NEW_ENV

## TIPS: git + kursens repo = sant

Om du vill kunna ladda ner de senaste ändringarna i kursens GitHub repo, men bara får en massa erorrs, följ dessa steg:

#### 1. git status
För att se vilka filer som din git klagar på, gör detta kommando
	
	git status

Titta speciellt på filerna som dyker upp under rubriken __changes not staged for commit__. De kommer att dyka upp med röd text.

Om det är ändringar som du inte vill spara, gå till steg 2. Om du har ändringar du vill spara, gå vidare till steg 3.

#### 2. git revert

I den röda texten specificeras vägen till de filer som du ska återställa (alltså det som du inte vill spara). Du återställer genom att köra

	git revert path-to-file

för varje path-to-file som synts i rött. Om du provar att göra `git status` igen så ska inga filer finnas kvar under __changes not staged for commit.__

Då kan du gå vidare till att dra ner det senaste i repot genom

	git pull

#### 3. git add och git commit

I den röda texten specificeras vägen till de filer som du vill spara ändringarna i. Du sparar genom att köra
	
	git add path-to-file

för varje path-to-file som synts i rött. Om du provar att göra `git status` igen så ska dessa filer dyka upp som gröna istället.

När du inte har några filer kvar under __changes not staged for commit__ så kan du gå vidare till att dra ner det senaste i repot genom

	git pull


## Kurslitteratur

Vi kommer använda många olika resurser för att lära oss om python, men vi kommer till stor del att använda oss av Jake VanderPlas *A whirlwind tour of python* och *Python data science handbook*. 
Båda böckerna är gratis och tillgängliga på författarens github både som text och som jupyter notebooks. För att ta till sig materialet rekommenderar vi starkt att ni kör all kod själva när ni läser!

Länkar till böckerna:
- [WIP](https://jakevdp.github.io/WhirlwindTourOfPython/) 
- [PDS handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)


// era kursledare Isabella Gagner och Alexander Hagelborn



