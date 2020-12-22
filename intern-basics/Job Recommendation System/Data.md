# Data

For the Job Recommendation System model we consider the data from the [Kaggle](https://www.kaggle.com/c/job-recommendation).

The dataset consist of many files in different formats, but we only consider the following files
* apps.tsv
* jobs.tsv
* test_users.tsv
* user_history.tsv
* users.tsv

In order to understand the content of the data files, you need to understand the structure of this contest.

In outline, we give you data on users, job postings, and job applications that users have made to job postings. In total, the applications span 13 weeks. 
We have split the applications into 7 groups, each group representing a 13-day window. Each 13-day window is split into two parts:
The first 9 days are the training period, and the last 4 days are the test period. All the other details on window split per user you can find in the
[Kaggle](https://www.kaggle.com/c/job-recommendation/data) site.

## File Formats
Each of the files is in .tsv (tab-seperated value) format. This means that each line in a .tsv file consists of several fields, which are separated by tabs.
To accommodate this file format, fields composed of text have been changed in the following ways to escape tabs, newlines, and carriage returns.

1. Tabs have been replaced by '\t'
2. Newlines have been replaced by '\n'
3. Carriage returns have been replaced by '\r'
4. Backslashes have been replaced by '&#92;\\'

## Files

**users.tsv** contains information about the users. Each row of this file describes a user. The *UserID* column contains a user's unique id number,
the *WindowID* column contains which of the 7 windows the user is assigned to, and the *Split* column tells whether the user is in the Train group or
the Test group. The remaining columns contain *demographic and professional information* about the users.

