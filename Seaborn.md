# Seaborn Tutorial 

>**IMPORTANT**
> Que: What is Probability Density of Data?
> Ans: The Probability Density of Data refers to the likelihood of a certain value or range of values occurring within a dataset.
> It is mathematical function that describes the distribution of the data and can be used to make prediction 
> and to understand the underlying patterns and relationship within the dataset. 

>**Note** 
> Python notebook containing all plots with various parameter can be obtain from [here]



---
## Setup
Install the [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/) in your editor or notebook by using following commands 
```python
pip install seaborn      # to install in termianl 
pip install matplotlib      
!pip install seaborn     # to install in notebook
!pip install matplotlib
conda install seaborn    # to install in conda env 
conda install matplotlib
```
# Plots 
## Distribution Plots
### Joint Plot
Joint Plot is a combination of scatter plot and a histogram or kernel density estimate (KDE) plot to display the distribution of one variable along the x-axis and the distribution of another variable on y-axis.
It allows to visualize the relationship between two variables.
### KDE Plot
Kernel Density Estimation is a graphical representation of the probability density function of a continuous random variable. 
It uses a smoothed line to show how often different values appear in the dataset.
It is a non-parametric method(it does not make any assumptions about the underlying distribution of data.)
### Pair Plot
Also known as Scatter plot matrix.
A pair plot is used to visualize the relationship between multiple variables in a dataset.
It uses a grid of subplots, where each subplot shows a scatter plot of two variables. 
Pair plot is often used to explore the relationship in a dataset.
### Rug Plot
Rug plot shows the distribution of a single numeric variable. 
A set of vertical lines is plotted for each observation in the dataset, with x-axis representing the variable of interest and the y-axis representing a value of 0 or 1.
The resulting plot allows you to see the density of observations at different values of the variable.
It's called rug-plot because it looks like a carpet or a rug.
### Styling
Style and customization can be done using various function and options like you can change the color palette of a plot, adjust the size and font of the axis labels, or add a title to the plot, scale and provide context to the plot, various plotting function and Faceting(split data across multiple subplots).
## Categorial Plots
### Bar Plot
In Bar Plot bars can represent different categories or groups, and the height of the bar plot can represent a numerical value or count. 
In Seaborn the `barplot()` function can plot a bar char of the y-axis variable against the x-axis variable.
### Count Plot
Count Plot shows the number of occurrences of each category in a dataset. 
It used to visualize the distribution of categorical data.
The x-axis represents the categories and the y-axis represents the count of data points in each category. 
### Box Plot
### Violin Plot
Violin Plot is similar to the box plot, but instead of a box it plots the data as kernel density estimate(KDE). 
The violin plot shows the probability density of the data at different values. 
It has a marker to indicate the median of the data and the width of violin indicates the frequency of the data points.
### Strip Plot
It displays the individual data points as dots or points on a single line. 
It is used to show the distribution of a single variable and often used in combination with other types of plots to provide additional information.
### Swarm Plot
### Palettes
A palette refers to a set of colors that can be used to create visualizations.
`sns.color_palette()` function can be used to create custom palettes.
Different palettes that can be used to create different types of plots, such as categorical plots, sequential plots, and diverging plots
## Matrix Plot
### Heat Maps
Heat maps uses color to show the density of distribution of data, where the values are represented by colors.
It is a 2-dimensional representation of data.
The data can be passed as a matrix or a data-frame, with each row and column representing a variable in the data, and the values of the cells representing the measurements or observations.  


### Cluster Map
Cluster Map group the similar data points together and separated dissimilar data points. 
In Cluster Map the rows and columns of the data are rearranged to group of similar data points together and to make patterns in the data more visible.
### Pair Grid
Pair Grid allows to plot multiple plots together in a grid format. 
### Facet Grid
### Regression Plot


