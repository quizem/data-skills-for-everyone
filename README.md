# Working with CSV in Python

## Introduction

Welcome to this tutorial series. This tutorial covers essentials data manipulation skills you can apply when working with CSVs. CSV is a very common file format for carrying data around. Because of its versatility, beginner lessons in data analytics begin with this data file format. As we go through the tutorial, we will address the specific case of a problem described below and our goal is to use Python programming to handle it.

## Problem:

A teacher who runs a training program using courses on a third-party platform is interested in obtaining some custom reporting on the learning progress of his learners.

However, the learning platform only provides very basic reporting. For example, at any time you can see the percentage that each learner has gone into the course. So, if you want to see a week-by-week progression, you will have to download the CSV progress report on a weekly basis and find a way to keep track of each learner.

This is the basic motivation for the problems we will tackle in this series. However, a couple of other problems show up once we download the report, which is in csv. 

 

In the videos that follow, we will tackle several problems including:

- Normalizing information in a given column, i.e., fix the column so the information is uniform.
- Filtering out information in a csv based on information in another csv
- Adding new information based on some calculation
- Create a single excel workbook that get aggregates information from several CSV
- Update an existing excel workbook with new information from a CSV file
- Write code that can produce all the above steps to any number of csv files
- Write code that can to a certain degree automate the processes outlined above

 

## Part 1 – Initial Setup

This section covers the initial setup for the series. It outlines a nice for case for dealing with CSV data files.



## Part 2 – Normalizing the Name Column

This section covers some initial data cleaning that must be performed on the CSV file. The raw file has 4 columns: `name`,  `started_at`, `completed_at`, `percent_complete`. The name column needs some work. Some records contain emails instead of full names. We want to replace the emails with their corresponding full names from a reference file which contains both information.



## Part 3 – Filtering Records based on the Name Column

This section demonstrates how to filter data in a CSV based on information on information in another CSV file. The CSV file we download from the learning platform is such that it contains the names of all the people on the platform whose emails match our company’s domain. This means, whether a person is enrolled in a course or not, as long as their emails match that of our company’s account, their names will appear on the progress report for any course we download. This is not desirable. We wish to use some means to eliminate the names of all people who according to our records are not taking the course.

 

## Disclaimer:

The names of the courses used in the video series are names of actual course you may find on real leaning platforms. In most of the videos, the example courses are based real courses on [Codecademy](https://www.codecademy.com/). However, the names of people, emails and other pieces of information are all fake and were added for the sake of this tutorial.