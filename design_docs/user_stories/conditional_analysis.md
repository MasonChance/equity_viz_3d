# Condidtional Analysis, Searching for Meaning

As an Analyst interested in discovering possible correlations between one or more data points and the expected future price of a given equity over various time-periods: 

I would like to be able to set specific conditions and parameters and evaluate the occurences over time. 

I would like to be able to control the time-periods considered (using historical data) and whether or not it is a fixed time frame or a randomized sample of fixed periods over the life of the equity under consideration.

**Examples:**
*example 1:*

``` when D/E is less than 1 and SMA200 is 3% above price at start of period, what is the average change over a 6 month period?

test from <start date> to <end date>
test 30 periods of 6 months randomly from life of equity and plot on scatter chart or in 3D viewer. 

```

*example 2:*

``` If average price over last 3 months is above current price, AND current price is less than EPS, what is the average percent change over the subsequent 3 months in a random sample of 100 3month periods over the life of the equity

```

*example 3:*

``` plot all points over the last year, where price was 2% greater than the SMA50 color the points blue.

plot all points in 10 random years over the life of the stock where above condition was true and color the points orange
```
