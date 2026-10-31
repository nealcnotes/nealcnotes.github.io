---
title: "Pandas Indexing Primer"
categories: 
  - "old-comics"
tags: 
  - "pandas"
---



![a castle from which a panda escapes](/assets/images/escape.jpg "Escape the Pandas Indexing Jungle")
![first make a dataframe of random numbers with labels](/assets/images/randnum.jpg)


*An early try at programming-with-cartoons, in the spirit of [\_why's Poignant Guide](https://poignant.guide/). Current work is at [home](/).*


```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 4),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 8, 2)))
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.871237</td>
      <td>-1.083014</td>
      <td>-1.475604</td>
      <td>-0.752170</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-2.706205</td>
      <td>0.329963</td>
      <td>0.392216</td>
      <td>-2.409230</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.468933</td>
      <td>-0.869137</td>
      <td>-0.228810</td>
      <td>0.244244</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.594944</td>
      <td>0.586175</td>
      <td>0.777512</td>
      <td>0.302765</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.919059</td>
      <td>-0.033826</td>
      <td>-0.517170</td>
      <td>0.952174</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.516535</td>
      <td>-0.311024</td>
      <td>-0.237281</td>
      <td>0.986209</td>
    </tr>
  </tbody>
</table>
</div>



![the basic indexing goes by labeled columns, like a python dictionary](/assets/images/randnum_01.jpg)


```python
df1[2]  # column labelled 2, like a python dictionary
```




    0    -1.083014
    2     0.329963
    4    -0.869137
    6     0.586175
    8    -0.033826
    10   -0.311024
    Name: 2, dtype: float64



<img src="/assets/images/randnum_02.jpg" alt="use .iloc for position based indexing" style="height: 200px;"/>


```python
df1.iloc[2]  # row in second position of dataframe
```




    0   -0.468933
    2   -0.869137
    4   -0.228810
    6    0.244244
    Name: 4, dtype: float64




```python
df1.iloc[2,3] # third entry of the above row
```




    0.24424384065382918



<img src="/assets/images/randnum_03.jpg" alt="use .loc for label based indexing" style="height: 200px;"/>


```python
df1.loc[2]  # row labelled 2
```




    0   -2.706205
    2    0.329963
    4    0.392216
    6   -2.409230
    Name: 2, dtype: float64



<img src="/assets/images/randnum_04.jpg" alt="which also slices" style="height: 200px;"/>


```python
df1.iloc[2:4,2:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>-0.228810</td>
      <td>0.244244</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.777512</td>
      <td>0.302765</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.loc[2:4,2:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0.329963</td>
      <td>0.392216</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.869137</td>
      <td>-0.228810</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_06.jpg" alt="can send a callable function" style="height: 200px;"/>
The function takes in the dataframe and returns something that .loc can index on


```python
df1.loc[lambda df_parameter: df_parameter[2]>0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-2.706205</td>
      <td>0.329963</td>
      <td>0.392216</td>
      <td>-2.409230</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.594944</td>
      <td>0.586175</td>
      <td>0.777512</td>
      <td>0.302765</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_05.jpg" alt="filter with a Boolean" style="height: 200px;"/>



```python
df1.loc[df1[2]>0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-2.706205</td>
      <td>0.329963</td>
      <td>0.392216</td>
      <td>-2.409230</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.594944</td>
      <td>0.586175</td>
      <td>0.777512</td>
      <td>0.302765</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_07.jpg" alt="dig a little deeper with Booleans" style="height: 200px;"/>



```python
df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)

```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.AAA <= 6
```




    0     True
    1     True
    2     True
    3    False
    Name: AAA, dtype: bool




```python
df[(df.AAA <= 6)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]},
    index=["foo", "bar", "boo", "kar"],
)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>foo</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>boo</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>kar</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_08.jpg" alt="Labels" style="height: 200px;"/>



```python
df["bar":"kar"]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>boo</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>kar</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc["bar":"kar"]  # Label
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>boo</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>kar</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Generic

df[0:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>foo</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>boo</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>




```python
datadict = {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
datadict
```




    {'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]}




```python
df2 = pd.DataFrame(data=datadict, index=[1, 2, 3, 4])  # Note index starts at 1.
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.iloc[1:3]  # Position-oriented
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc[1:3]  # Label-oriented
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[1:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_10.jpg" alt="Grouping" style="height: 300px;"/>



```python
df = pd.DataFrame(
    {"AAA": [1, 1, 1, 2, 2, 2, 3, 3], "BBB": [2, 1, 3, 4, 5, 1, 2, 3]}
)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_11.jpg" alt="idxmin" style="height: 200px;"/>



```python
# Method 1 : idxmin() to get the index of the minimums
df.loc[df.groupby("AAA")["BBB"].idxmin()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_13.jpg" alt="print groups trick" style="height: 200px;"/>



```python
df.groupby("AAA").apply(lambda a: a[:]) # https://stackoverflow.com/a/62803666
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
    </tr>
    <tr>
      <th>AAA</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">1</th>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2</th>
      <th>3</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>6</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



<img src="/assets/images/randnum_12.jpg" alt="sort first" style="height: 200px;"/>



```python
# Method 2 : sort then take first of each
df.sort_values(by="BBB").groupby("AAA", as_index=False).first()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by="BBB")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by="BBB").groupby("AAA",as_index=False).apply(lambda a: a[:])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">0</th>
      <th>1</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">1</th>
      <th>5</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>6</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>30</td>
      <td>-30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>40</td>
      <td>-50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[(df["BBB"] < 15) & (df["CCC"] >= -10)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[(df["BBB"] < 15) | (df["CCC"] >= -10)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>BBB</th>
      <th>CCC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>10</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>20</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>





These examples are taken from the main Pandas website and cookbook: 
- [https://pandas.pydata.org/docs/user_guide/indexing.html](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [https://pandas.pydata.org/docs/user_guide/cookbook.html](https://pandas.pydata.org/docs/user_guide/cookbook.html)


Get the jupyter notebook here: 
[Pandas Indexing Notebook](/assets/notebooks/pandasindexing.ipynb)



