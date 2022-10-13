#for the whole reserviour we have to get the confidence interval from the data provided
#to calculate confidence interval we have to import scipy.stats
import scipy.stats as st
import math
#mean is generated from previous code 
x_bar = 0.492287 
s = 0.353569 
n = 122
print("mean: %.2f. Standard deviation: %.2f. size: %d." % (x_bar, s, n))
# Z_score must be calculated to get confidence interval  
z_score = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score)
#calculating confidence interval
std_err = s / math.sqrt(n)
print("standard error: %.2f" % std_err)
#Then calculate the amrgin of error
mrg_err = z_score * std_err 
("printMargin of error: %.2f" % mrg_err)
#lower and upper bound needs to get calculated for confidence interval
ci_low = x_bar - mrg_err
ci_upp = x_bar + mrg_err
print("Confidence Interval of the mean: %.2f to %.2f" % (ci_low, ci_upp))