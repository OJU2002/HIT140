#As per question 4 we have to calculate the hypothesis to know that artifical dam are responsible for the increase in mercury level or not
import pandas as pd
import scipy.stats as st
#we have to read csv into a DataFrame
df = pd.read_csv("Assessment.csv")
# To get hypothesis split DataFrame into two subsets: 
# df1: no functional dam present, all natural flowage
# df2: at some man made flowage  in the drainage area
df1 = df[df["Dam"] == 1]
df2 = df[df["Dam"] == 0]


# Applicable columns should be selected for each dataframe 
sample1 = df1["Mercury"].to_numpy()
sample2 = df2["Mercury"].to_numpy()


# should print the values in samples
print("Sample 1: ", sample1)
print("Sample 2: ", sample2)


#should calulate two basic statistics for two sample 
print("\n Computing basic statistics of samples ...")

#statistics for sample 1:
x_bar1 = st.tmean(sample1)
s1 = st.tstd(sample1)
n1 = len(sample1)
print("\t Statistics of sample 1: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1, s1, n1))


#statistics of sample 2:
x_bar2 = st.tmean(sample2)
s2 = st.tstd(sample2)
n2 = len(sample2)
print("\t Statistics of sample 2: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2, s2, n2))


#have to perform two-sample t-test
#For null hypothesis: mean of sample 1 = mean of sample 2
# For alternative hypothesis: mean of sample 1 is greater than mean of sample 2 (one-sided test)
# we have to notice that for argument equal_var=False, which assumes that two sample do not have equal variance
t_stats, p_val = st.ttest_ind_from_stats(x_bar1, s1, n1, x_bar2, s2, n2, equal_var=False, alternative='greater')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.2f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.4f" % p_val)

print("\n Conclusion:")
if p_val < 0.4:
    print("\t We reject the null hypothesis.")
else:
    print("\t We accept the null hypothesis.")