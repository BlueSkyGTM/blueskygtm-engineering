# Exercises — Time Series Fundamentals

## Exercises

1. **Implement additive decomposition on a synthetic weekly outbound email volume series.** Generate 104 weeks of data with a linear upward trend, a 52-week seasonal pattern, and Gaussian noise. Run `seasonal_decompose` with `model='additive'`, then print the trend, seasonal, and residual values for the first 5 weeks. Verify your output by confirming that the three components sum back to the original observed values for those 5 weeks.

2. **Generate a random walk of 200 points and run the Augmented Dickey-Fuller test on it.** Print the ADF statistic, p-value, and critical values at the 1%, 5%, and 10% significance levels. Then generate a second series of 200 independent draws from a standard normal distribution and run the same test. Print both sets of results side by side and state which series is stationary at α = 0.05.

3. **Build a feature matrix from 365 days of synthetic daily demo bookings data.** Without using any pre-built feature engineering library, implement lag features at lags 1, 7, 14, and 28, and rolling window statistics (mean and standard deviation) with window sizes of 7 and 30 days. Print the resulting DataFrame's first 35 rows so you can observe how NaN values propagate at the beginning of the series and how each feature column aligns temporally.

4. **Apply first-order differencing to achieve stationarity.** Generate a 200-point series with a deterministic linear trend plus seasonal noise — a series that is clearly non-stationary. Compute the ADF p-value on the original series. Then apply first-order differencing, compute the ADF p-value on the differenced series, and print both p-values. Confirm the differenced series passes the stationarity threshold at α = 0.05.

5. **Design and build a lag-depth optimization pipeline that selects features based on autocorrelation significance.** Given any time series as input, compute the autocorrelation function up to 40 lags, identify every lag where ACF exceeds the 95% confidence band, and generate lag features only for those statistically significant lags. Run the pipeline on a 3-year weekly series of CRM opportunity creation
