# mmt01-grading-system

TITLE: "Proposal of A New Grading Scale under Remote Learning in The Philippine Science High School System"
AUTHORS: ANONYMOUS
COURSE: MMT01 - Mathematical Modelling
DATE: October 7, 2020

This is a project for the paper mentioned in order to provide simulation analysis for a new grading system as referenced to the citation Kulick, G., & Wright, R. (2008). The Impact of Grading on the Curve: A Simulation Analysis. International Journal for the Scholarship of Teaching and Learning, 2(2). https://doi.org/10.20429/ijsotl.2008.020205. The python files are used to create the data and the text files are the randomized outputs that are provided for n = 1,000,000 different situations for each simulation iteration. 

The algorithm for simulation we produced relies on a few assumptions in order to optimize the program: (1) the floor grade c is a random integer between 35 and 45, inclusive, in order to make way for the decision that would be provided by the teacher, (2) the number of formative assessments is set between 8 and 16, while the number of alternative assessments is set between 1 and 8, (3) the grading system is perfectly consistent with each subject, meaning that there are no biases between teachers. This has been an efficient method to start developing an exam system, which involves randomizing variables in order to create data sets through simulation analysis.

This is a randomizer written in Python 3.7 would test this for a grading system in an entire level in the PSHSS, in this case we have selected a theoretical Grade 9 curriculum with 5 subjects with the same number of units and a theoretical Grade 10 curriculum with 10 subjects with different number of units
