Nykaa A/B Test: Impact of Shipping Fee Increase on Revenue Per User
1. Project Overview
This project is an end-to-end A/B testing simulation designed to evaluate a potential business change for the e-commerce platform, Nykaa.

The core objective is to determine if increasing the minimum order value for free shipping from ₹299 to ₹399 would be a profitable decision. This project demonstrates a data-driven approach, moving from problem identification and hypothesis formulation to data simulation, rigorous statistical analysis, and a final, actionable business recommendation.

2. The Business Problem & Hypothesis
Problem Identification

Before designing the test, I conducted domain research to identify high-impact business questions relevant to Nykaa. Potential areas of investigation included:

The impact of the Nykaa Affiliated Program (NAP) on sales.

The effect of sitewide offers on overall sales vs. individual product sales.

The effectiveness of "limited edition" products on sales volume.

The relationship between premium customers and order frequency.

From this, I selected a high-stakes, common e-commerce problem: optimizing shipping fee thresholds.

Hypothesis Formulation

The experiment tests the following hypothesis:

Null Hypothesis (H 
0
​	
 ): Increasing the minimum shipping fee from ₹299 to ₹399 will have no significant effect on the Revenue Per User (RPU).

Alternative Hypothesis (H 
a
​	
 ): Increasing the minimum shipping fee from ₹299 to ₹399 will have a significant effect on the Revenue Per User (RPU).

3. Methodology & Metrics
Experiment Design

To test this hypothesis, a controlled experiment was simulated with 100,000 users, randomly split into two groups:

Group A (Control): Users who see the original free shipping threshold (₹299).

Group B (Treatment): Users who see the new, higher shipping threshold (₹399).

Key Metrics

To ensure a complete picture of business impact, I selected both a primary success metric and a critical guardrail metric.

Main Metric: Revenue Per User (RPU)

Why: This is the primary success metric. It measures the total revenue generated divided by the total number of users in the experiment. It directly answers the business question: "Will this change make us more money per user?"

Test Used: Welch's t-test. This was chosen over the standard Student's t-test because the Shapiro-Wilk test confirmed the data was not normally distributed, and it does not assume equal variances between the two groups (which is a safer assumption).

Guardrail Metric: Conversion Rate (CR)

Why: This metric is monitored to ensure the change doesn't unacceptably harm user behavior. A significant drop in conversions (users completing a purchase) could wipe out any gains from a higher RPU.

Test Used: Chi-squared test (for categorical data) and a Bayesian Beta distribution analysis to determine the probability of one group being better than the other.

Secondary Metric: Average Order Value (AOV)

Why: This measures the average revenue only from users who converted. It helps explain why the RPU changed.

4. Key Findings & Results
The analysis revealed a clear and statistically significant story.

Finding 1: Conversion Rate (Guardrail Metric) Dropped Significantly

The Chi-squared test yielded a p-value of 0.024.

Since p<0.05, we reject the null hypothesis for conversion.

This indicates a statistically significant drop in conversions for the treatment group. Users were clearly deterred by the higher shipping fee.

The Bayesian analysis confirmed this, showing a 99.33% probability that the control group's conversion rate was better than the treatment group's.

Finding 2: Revenue Per User (Main Metric) Did NOT Increase

The Welch's t-test for RPU yielded a p-value of 0.647.

Since p>0.05, we fail to reject the null hypothesis.

This means there is no statistically significant difference in RPU between the two groups.

The 95% confidence interval for the difference in RPU was [-₹1.59, +₹1.17]. Since this interval contains 0, it confirms our finding that there is no statistically significant gain or loss.

Results Summary

| Metric | Test Used | Control Group (A) | Treatment Group (B) | p-value | Finding (at $\alpha=0.05$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Conversion Rate (Guardrail)** | Chi-squared | 3.01% | 2.80% | **0.024** | **Statistically Significant Drop** |
| **Revenue Per User (Main)** | Welch's t-test | ₹16.48 | ₹17.07 | 0.647 | **No Significant Difference** |
| **Avg. Order Value (AOV)** | - | ₹547.41 | ₹610.19 | - | Treatment AOV is higher* |

The AOV for the treatment group did increase, suggesting users who did convert were spending more to meet the new threshold. However, this gain was completely offset by the number of users who abandoned their carts, as seen by the drop in conversion.

5. Conclusion & Business Recommendation
Conclusion

The experiment was a success. It provided a clear answer to the business question.

While the higher shipping fee did successfully nudge converting users to spend more (a higher AOV), this positive effect was canceled out by the significant number of users who were deterred from purchasing at all (a lower CR).

The net result is no statistically significant change in our main metric, Revenue Per User, and a negative impact on user conversion.

Recommendation: DO NOT LAUNCH 🛑

I recommend that Nykaa DOES NOT implement the change to increase the free shipping threshold from ₹299 to ₹399.

The data clearly shows that this change would fail to increase overall revenue and would actively harm the user experience by causing fewer users to convert, leading to customer frustration for no business gain.
