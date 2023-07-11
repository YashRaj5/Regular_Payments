# Databricks notebook source
# MAGIC %md
# MAGIC *Using signal processing theory and Fourier transforms, we extract regular payment informations from a large dataset of card transactions data. Although it is easy to eye ball regularity in payments when looking at specific transactions, doing so at scale across billions of card transactions requires a scientific (and programmatic) approach to a business problem. In this solution accelerator, we demonstrate a novel approach to consumer analytics by combining core mathematical concepts with engineering best practices and state of the art optimizations techniques to better model customers' behaviors and provide millions of customers with personalized insights. With 40% of americans struggling to come up with $400 for an unexpected expense ([source](https://www.cnbc.com/2019/07/20/heres-why-so-many-americans-cant-handle-a-400-unexpected-expense.html)), such a framework could be used to suggest financial goals and provide customers with recommended actions to better spread regular payments over billing cycles, minimize periods of financial vulnerability and better plan for unexpected events.*

# COMMAND ----------

# MAGIC %md
# MAGIC <img src ="https://raw.githubusercontent.com/databricks-industry-solutions/reg-reporting/main/images/reference_architecture.png">

# COMMAND ----------

# MAGIC %md
# MAGIC # The Theory
# MAGIC Before delving into the actual solution, let's get back to our physics fundamentals. In this notebook, we will explore signal processing theory as it may apply to retail banking and card transaction data. Let's select an hypothetical user for a subscription service we know would exhibit strong seasonality (such as Netflix). Easy to eye ball on a graph, such a payment regularity would be difficult to programmatically extract from billions of card transactions, especially when the regularity of payments may not be of exact match (bank holidays or missed payments).

# COMMAND ----------


