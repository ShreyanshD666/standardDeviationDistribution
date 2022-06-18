import pandas as pd
import statistics as st

df = pd.read_csv("StudentsPerformance.csv")
data = df["math score"].to_list()

mean = sum(data) / len(data)
stdDeviation = st.stdev(data)
median = st.median(data)
mode = st.mode(data)

first_std_deviation_start, first_std_deviation_end = mean-stdDeviation, mean+stdDeviation
second_std_deviation_start, second_std_deviation_end = mean-(2*stdDeviation), mean+(2*stdDeviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*stdDeviation), mean+(3*stdDeviation)

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

print("The mean of this data is:", mean)
print("The median of this data is:", median)
print("The mode of this data is:", mode)
print("the standard deviation of this data is:", stdDeviation)
print("{}% of math scores (data) lies within 1 standard deviation:", (len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of math scored (data) lies within 2 standard deviations:", (len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of math scores (data) lies within 3 standard deviations:", (len(list_of_data_within_3_std_deviation)*100.0/len(data)))
