# Christiaan Dageforde EVC Data Engineer Assessment

## Data Wrangling
This is a script for pulling data from Vendor Y's API and merging it with a csv containing Vendor X's data. The code cleans & forces consistency across the joined data and writes to a csv in the `Data` folder.

### Executing Python code
At the command line, navigate to project directory and enter the following command with DB credentials as arguments in the order specified below: 
`python DataWrangling.py "DB USERNAME" "DB HOST" "DB PASSWORD" "DB NAME" "DB PORT"`

### Next Steps
1. Revise code to be more flexible, secure and overall more pythonic by wrapping code blocks in functions
2. Fill out data cleansing functions
3. Fix database schema errors

## Data Engineer Concepts
1. Before ingesting data into a preexisting reporting structure, my ultimate concern is around maintaining data quality. I would ask whether data from different sources are structured differently. Is there missing data? Is it valuable to me to leave this as missing data, or do I want to come up with a strategy for imputing values in a way that doesn't affect the data's accuracy or usefulness?
2. To build a consensus with the team around changes to a data process, I would start by gathering data on the pipeline in its current state, for example, by generating some kind of statistics report around pipeline performance speed. Then I would bring this to the team while we are planning an upcoming sprint and present my findings and propose my changes. I would ask for feedback in the moment, while also leaving time for teammates to consider my proposal and offer feedback outside of the meeting. Ultimately, I would set a clear date and time for feedback to be due, after which time I would assess whether or not there was a consensus to move ahead with my proposed changes. If I feel like I am missing valuable input from specific members of the team, I would be sure to reach out to them directly.
3. When cleaning data or taking general measures to ensure data quality, I consider accuracy, completeness, reliability, and relevance. One important issue is considering the quality of missing data. Is it valuable to leave this data as "missing"? Or should I find a way to impute the missing data in a way that doesn affect the quality of the data? From there, I also consider the relevance of the data I'm cleaning. Are there any columns or large swaths of data that is irrelevant to our analysis or project that we can get rid of? After I ask these questions, my focus is on exploratory data analysis and taking measures to enforce consistency across the data. 