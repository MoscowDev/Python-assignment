#
import statistics

values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]
mean_value = statistics.mean(values)
median_value = statistics.median(values)
mode_value = statistics.mode(values)
 
print("The mean is: " + str(mean_value))
print("The median is: " + str(median_value))
print("The mode is: " + str(mode_value))
