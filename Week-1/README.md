# Week-0: Warp Up


## TODO

In this week, we will cover some fundamental tools for Machine Learning:

- *Pandas*: for data manipulation in python
- *Scipy*: Statistical analysis
- *Matplotlib*: Data visualization

And
- Flask: for generating custom APIs.

## 1) *Pandas*

The course materials which are used for this section are adapted from [Data Camp](https://learn.datacamp.com/skill-tracks/data-manipulation-with-python).

### 1.1) *Course-1: Data Manipulation with Pandas*

In this section, some basic and even advance commands and syntaxes of pandas will be reviwed.

Pandas is butil on Numpy and Matplotlib. Rectangular data(Tabular data) is the most common way to represenet data.

In pandas, recatngular data is shown in **DataFrame** objects.

#### 1.1.1) Exploring a DataFrame: **.head()**
If we want to quickly explore whats going on in a particular dataset we must use:

```
df.head()
```
#### 1.1.2) Exploring a DataFrame: **.info()**
The info method displays the names of the columns, the data types they contain, and whether they have any missing values.

```
df.info()
```
#### 1.1.3) Exploring a DataFrame: **.describe()**
The describe method computes some summary statistics for numerical columns. like mean and median. "count" is the number of non-missing values in each column.

```
df.describe()
```

DataFrames consist of three different components, accessible using attributes. 

#### 1.1.4) Components of a DataFrame: **.value**
The values attribute, as you might expect, contains the data values in a 2-dimensional Numpy array.

```
df.values
```
#### 1.1.5) Components of a DataFrame:**.columns** and **.index**
The other two components of a DataFrame are labels for columns and rows. The columns attribute contains column names, and the index attribute contains row numbers or row names. Be careful, since row labels are stored in dot-index, not in dot-rows.

```
df.columns
df.index
```

Now we'll cover the two simplest and possibly most important ways to find interestin parts of the DataFrame.

#### 1.1.6) **Sorting**

```
dogs.sort_values("weight_kg", ascending=False)
dogs.sort_values(["weight_kg", "height_cm"])
```

#### 1.1.7) **Subsetting columns**
We may want to zoom in on just one column. We can do this using the DataFrame, followed by sqaure brackets with a column name inside.

```
dogs.["name"]
dogs.[["name", "height_cm"]]
```
#### 1.1.8) **Subsetting rows**
There are several ways to subset rows. The most common way to do this is by creating a logical condition to filter against.

```
dogs[dogs["height_cm"] > 50]
dogs[dogs["date_of_birth"] > "2015-01-01"]
dogs[(dogs["breed"] == "Labrador") & (dogs["color"] == "Brown")]
```

#### 1.1.9) Subsetting using **.isin()**
If you want to filter on multiple values of a categorical variable, the easiest way is to use the isin method.

```
is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]
```
#### 1.1.10) Adding a new column
Creating and adding new columns can go by many names, including mutating a DataFrame, transforming a DataFrame and a feature engineering.
```
dogs["height_m"] = dogs["height_cm"] / 100
```

## 2) *Flask*

This part is taught by Patrick Smyth in [Creating Web APIs with Python and Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask). Two basic (Hello world) web APIs are implemented in `api/`.

To run them, you need [Flask](https://flask.palletsprojects.com) installed, then enter these commands in your terminal or cmd:

```
$ cd path/to/your/dir
$ python api.py
```

Then, follow the link above, http://127.0.0.1:5000/, using your web browser to see the running application.