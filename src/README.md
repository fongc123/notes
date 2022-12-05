# COMP4462 Final Project
This repository contains the code and data sources of the two dashboards for the COMP4462 final project of Group 3. The source code for all visualizations except the Sankey diagram, which is in Observable, can be found here.

The interactive dashboard was implemented in Tableau, while the static dashboard was implemented in Tableau and JavaScript. Data preprocessing was done with Python and Excel.

All charts in the interactive dashboard update based on selected states in the dot map. The static dashboard contains not only the JavaScript counterparts of the interactive dashboard charts but also more sophisticated data visualizations.

## Usage
The interactive and static dashboards can be viewed [here](https://public.tableau.com/app/profile/arun3771/viz/COMP4462_Finalproduct_16702290006430/InteractiveDashboard?publish=yes) on Tableau Public.

Alternatively, the dashboards can be viewed locally with the following steps.
1. Open the `COMP4462_Finalproduct.twb` file.
2. Click **Cancel** when the "Extract Not Found" window appears.
3. In the "Dashboard Unavailable" window, click **Locate File**.
4. In the pop-up window, navigate to the `/Data` directory and open the `governor_shooting_merged_v2.csv` file.
5. Repeat the previous step until there are no more missing file requests.
6. In the "Extract Not Found" window, select the **Regenerate the extract** option.
7. Save the extract file (a `.hyper` file) locally.

In step 4, Tableau should ask for input four times.

### Sankey Diagram
The source code for the Sankey diagram can be accessed from this [link](https://observablehq.com/@hagrawalaa/sankey) on Observable. If the chart does not appear initially, click the **Run all**.

## Dataset
This project primarily focuses on fatal police shootings in the United States between 2015 to 2022. Additional datasets, such as state governors, state party affiliation, and state population, were used to explore relationships between shooting incidents and other factors.
- [Fatal Force Database](https://github.com/washingtonpost/data-police-shootings)
- [US Governor Dataset](https://www.kaggle.com/datasets/brandonconrady/us-governor-dataset)
- [State-Level Estimates of Household Firearm Ownership](https://www.rand.org/pubs/tools/TL354.html)
- [List of state abbreviations](https://worldpopulationreview.com/states/state-abbreviations)

All original and processed data files can be found under the `/Data` directory.