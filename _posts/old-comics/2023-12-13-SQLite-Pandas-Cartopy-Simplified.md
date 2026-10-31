---
title: "SQLite and Pandas quick intro"
categories: 
  - "old-comics"
tags: 
  - "pandas"
  - "sql"
---



![alt text](/assets/images/routemap.png "SQLite and Pandas quick intro")

*An early try at programming-with-cartoons, in the spirit of [\_why's Poignant Guide](https://poignant.guide/). Current work is at [home](/).*

Download the flights database here: [flights.db](/assets/notebooks/flights.db)


![alt text](/assets/images/pandas_sqlite1_01.jpg "Quick Intro")


```python
import pandas as pd
import sqlite3
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
pd.set_option("max_colwidth", 10)
pd.set_option("display.max_rows", 5)


con = sqlite3.connect("flights.db")
airdf = pd.read_sql_query("select * from airports;", con)
airdf
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
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>city</th>
      <th>country</th>
      <th>code</th>
      <th>icao</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>altitude</th>
      <th>offset</th>
      <th>dst</th>
      <th>timezone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>Goroka</td>
      <td>Goroka</td>
      <td>Papua ...</td>
      <td>GKA</td>
      <td>AYGA</td>
      <td>-6.081689</td>
      <td>145.39...</td>
      <td>5282</td>
      <td>10</td>
      <td>U</td>
      <td>Pacifi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>Madang</td>
      <td>Madang</td>
      <td>Papua ...</td>
      <td>MAG</td>
      <td>AYMD</td>
      <td>-5.207083</td>
      <td>145.7887</td>
      <td>20</td>
      <td>10</td>
      <td>U</td>
      <td>Pacifi...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8105</th>
      <td>8105</td>
      <td>9540</td>
      <td>Deer H...</td>
      <td>Deer H...</td>
      <td>United...</td>
      <td>DHB</td>
      <td>\N</td>
      <td>48.618397</td>
      <td>-123.0...</td>
      <td>0</td>
      <td>-8</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>8106</th>
      <td>8106</td>
      <td>9541</td>
      <td>San Di...</td>
      <td>San Diego</td>
      <td>United...</td>
      <td>OLT</td>
      <td>\N</td>
      <td>32.7552</td>
      <td>-117.1995</td>
      <td>0</td>
      <td>-8</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
  </tbody>
</table>
<p>8107 rows × 13 columns</p>
</div>



![alt text](/assets/images/pandas_sqlite1_02.jpg "Filtering in SQL")


```python
candf = pd.read_sql_query("select * from airports where country = 'Canada';", con);
candf
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
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>city</th>
      <th>country</th>
      <th>code</th>
      <th>icao</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>altitude</th>
      <th>offset</th>
      <th>dst</th>
      <th>timezone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>21</td>
      <td>Sault ...</td>
      <td>Sault ...</td>
      <td>Canada</td>
      <td>YAM</td>
      <td>CYAM</td>
      <td>46.485001</td>
      <td>-84.50...</td>
      <td>630</td>
      <td>-5</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>22</td>
      <td>Winnip...</td>
      <td>Winnipeg</td>
      <td>Canada</td>
      <td>YAV</td>
      <td>CYAV</td>
      <td>50.056389</td>
      <td>-97.0325</td>
      <td>760</td>
      <td>-6</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>433</th>
      <td>8103</td>
      <td>9538</td>
      <td>Port M...</td>
      <td>Port M...</td>
      <td>Canada</td>
      <td>YMP</td>
      <td>\N</td>
      <td>50.575556</td>
      <td>-127.0...</td>
      <td>225</td>
      <td>-8</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>434</th>
      <td>8104</td>
      <td>9539</td>
      <td>Sulliv...</td>
      <td>Sulliv...</td>
      <td>Canada</td>
      <td>YTG</td>
      <td>\N</td>
      <td>50.883333</td>
      <td>-126.8...</td>
      <td>0</td>
      <td>-8</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
  </tbody>
</table>
<p>435 rows × 13 columns</p>
</div>



![alt text](/assets/images/pandas_sqlite1_03.jpg)


```python
airdf.loc[airdf.country == "Canada"]
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
      <th>index</th>
      <th>id</th>
      <th>name</th>
      <th>city</th>
      <th>country</th>
      <th>code</th>
      <th>icao</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>altitude</th>
      <th>offset</th>
      <th>dst</th>
      <th>timezone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>21</td>
      <td>Sault ...</td>
      <td>Sault ...</td>
      <td>Canada</td>
      <td>YAM</td>
      <td>CYAM</td>
      <td>46.485001</td>
      <td>-84.50...</td>
      <td>630</td>
      <td>-5</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>22</td>
      <td>Winnip...</td>
      <td>Winnipeg</td>
      <td>Canada</td>
      <td>YAV</td>
      <td>CYAV</td>
      <td>50.056389</td>
      <td>-97.0325</td>
      <td>760</td>
      <td>-6</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8103</th>
      <td>8103</td>
      <td>9538</td>
      <td>Port M...</td>
      <td>Port M...</td>
      <td>Canada</td>
      <td>YMP</td>
      <td>\N</td>
      <td>50.575556</td>
      <td>-127.0...</td>
      <td>225</td>
      <td>-8</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
    <tr>
      <th>8104</th>
      <td>8104</td>
      <td>9539</td>
      <td>Sulliv...</td>
      <td>Sulliv...</td>
      <td>Canada</td>
      <td>YTG</td>
      <td>\N</td>
      <td>50.883333</td>
      <td>-126.8...</td>
      <td>0</td>
      <td>-8</td>
      <td>A</td>
      <td>Americ...</td>
    </tr>
  </tbody>
</table>
<p>435 rows × 13 columns</p>
</div>



![alt text](/assets/images/pandas_sqlite1_04.jpg)


```python
routes = pd.read_sql_query("""
select sa.code as sacode, da.code as dacode, cast(sa.longitude as float) as source_lon,
    cast(sa.latitude as float) as source_lat,
    cast(da.longitude as float) as dest_lon,
    cast(da.latitude as float) as dest_lat
from routes
    inner join airports sa on sa.id = routes.source_id
    inner join airports da on da.id = routes.dest_id;
""",con)
routes
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
      <th>sacode</th>
      <th>dacode</th>
      <th>source_lon</th>
      <th>source_lat</th>
      <th>dest_lon</th>
      <th>dest_lat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AER</td>
      <td>KZN</td>
      <td>39.956589</td>
      <td>43.449928</td>
      <td>49.278728</td>
      <td>55.606186</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ASF</td>
      <td>KZN</td>
      <td>48.006278</td>
      <td>46.283333</td>
      <td>49.278728</td>
      <td>55.606186</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>67200</th>
      <td>FRU</td>
      <td>OSS</td>
      <td>74.477556</td>
      <td>43.061306</td>
      <td>72.793269</td>
      <td>40.608989</td>
    </tr>
    <tr>
      <th>67201</th>
      <td>OSS</td>
      <td>FRU</td>
      <td>72.793269</td>
      <td>40.608989</td>
      <td>74.477556</td>
      <td>43.061306</td>
    </tr>
  </tbody>
</table>
<p>67202 rows × 6 columns</p>
</div>



![alt text](/assets/images/pandas_sqlite2.jpg)


```python
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

for name, row in routes[:3000].iterrows():
    distcolor = "blue" if abs(row["source_lon"] - row["dest_lon"]) < 30  else "red"
    plt.plot([row.source_lon, row.dest_lon], [row.source_lat, row.dest_lat],
             color=distcolor, linewidth=1,
             transform=ccrs.Geodetic(),)
plt.show()
```


    
![Route Map](/assets/images/routemap.png)


<details class="comic-transcript inline-block">
  <summary class="button m1-4 md:p-4 md:text-center font-bold cursor-pointer">read the transcript!</summary>
  <h3>bubble 1: Panda says sqlite3.connect is how we connect Python's built-in SQLite3 to a standard sqlite3 file.</h3>

  <h3>bubble 2: Seal says And we can run SQL queries with just the read_sql_query line</h3>


  <h3>bubble 3: Seal says we can filter with SQL where clauses, and Panda
  replies Or with pandas boolean indexing</h3>

  <h3>bubble 4: Panda says we get a dataframe from a few joins.</h3>

  <h3>bubble 5: Seal says and then make a cool Cartopy map from python</h3>
</details>

Read more details here: [https://www.dataquest.io/blog/python-pandas-databases](https://www.dataquest.io/blog/python-pandas-databases)

Get the jupyter notebook here: 
[SQLite and Pandas Jupyter Notebook](/assets/notebooks/airsqlite.ipynb)



```python

```
