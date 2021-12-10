# Plan

Eventual goal is to have a single function `process` that will run all the steps for any number of files

## Processing Steps for a single files
### 1. Read Data from Disk
- [ ] read progress data
- [ ] read names data

### 2. Determine name of the current course

- [ ] use `os.path` to get file name
- [ ] define `course_name_to_code()` to generate course code

### 3. Clean the names column
- [ ] define `clean_names_column()` to fix errors with names column

### 4. Prepare to filter data with addition of new column
- [ ] define `add_track_info(progress_df,names_df)`to add new column with track information

### 5. Add new column to determine enrolment
- [ ] define `add_enrollment_info(progress_df,course_name)`
- [ ] define `tag_enrollment(course_code,track)` as a helper to above step

### 6. Filter the progress data based on new column
- [ ] define `filter_names(progress_df)`

### 7. Define a single function to combine all steps above
- [ ] define `process()`