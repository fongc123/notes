---
title:
- Cost Calculation for Scraping Modules on AWS
author:
- Fong Chenananporn
theme:
- Copenhagen
fontsize: 10pt
---
# Hosting Options

Options explored:

+ AWS Lightsail (*current*)
+ AWS API Gateway
+ AWS Lambda
+ AWS EC2

# Calculation Assumptions

The following assumptions were made to calculate costs.

+ maximum usage per month
+ **6GB** memory per module
+ 1 month = 2,628,000 seconds

The **number of articles or profiles per month** is derived first to obtain the **price per article or profile per month**.

The prices per article or profile are shown in $10^{-4}$ USD per month.


# AWS Lightsail

An easy-to-use, low-cost, and pre-configured cloud service. 

+ great for small businesses
+ testing environments
+ relevant features: virtual server and container

AWS Lightsail services will be billed at a fixed rate per month.

|       Feature [^1]        | Price | Linkedin | Glassdoor | Reuters |
|:--------------------:|:-------------:|:--------------------:|:---------------------:|:-------:|
| Virtual Server |   39.24    |       5.97        |       23.89        | 0.60 |
|   Container    |   156.99   |       23.89       |       95.58        | 2.39 |

[^1]: 8GB memory to meet scraper requirements.

# AWS Lambda

A serverless, event-driven cloud service that allows code to be run from any application without any server management.

AWS Lambda services will be billed based on the number of requests sent. However, AWS Lambda has a restriction of 900 seconds per function call.

| Usage [^2] | Price [^3] | Linkedin | Glassdoor | Reuters |
| :-----: | :-------------: | :--------: | :---------: | :-------: |
| 100%  | 256.13        | 38.98    | 155.94    | 3.90    |
| 50%   | 124.73        | 37.97    | 151.88    | 3.80        |

[^2]: Utilization per month (%).
[^3]: Free tier prices.

# AWS Elastic Compute Cloud (EC2)

The broadest and deepest compute platform with many instance choices to match user needs.

AWS EC2 comes with different payment plans to suit needs.

+ EC2 Instance Savings Plans (plan 1)
+ On-Demand (plan 2)

The EC2 Instance Savings Plan will be billed at a fixed rate, while the On-Demand plan will only be billed based on usage.

|   Plan   | Price | Linkedin | Glassdoor | Reuters |
|:--------:|:-----:|:--------:|:---------:|:-------:|
|    1     | 38.98 |   5.93   |   23.73   |  0.59   |
| 2 (100%) | 61.90 |   9.42   |   37.69   |  0.94   |
| 2 (62%)  | 38.41 |   9.43   |   37.72   |  0.94   |
| 2 (10%)  | 6.19  |   9.42   |   37.69   | 0.94        |

# Summary

![AWS Hosting Costs](midas-analytics-aws-costs-graph.png){width=75%}

Consider a virtual server on AWS Lightsail *or* AWS EC2 with the Instance Savings Plan.