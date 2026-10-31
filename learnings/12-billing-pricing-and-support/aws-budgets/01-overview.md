# AWS Budgets

## Simple definition

AWS Budgets is an AWS cost management service that helps you set spending, usage, or commitment targets and alerts you when you are close to, or over, those targets.

---

## Core idea in plain English

Think of AWS Budgets as a financial guardrail for your AWS account.

You decide how much you want to spend, how much of a service you want to use, or how efficiently you want to use Reserved Instances or Savings Plans. AWS Budgets then tracks your actual and forecasted progress against that target and warns you before things go too far.

In some cases, it can also trigger automatic actions to help control costs.

---

## Main use cases

### 1. Setting a monthly cloud spending limit

A company can create a monthly cost budget to make sure its AWS bill stays within a planned amount. This is one of the most common uses of AWS Budgets.

### 2. Getting alerts before costs become too high

Teams can configure alerts at thresholds such as 80%, 90%, and 100% of the budget. This helps them react before the bill becomes a problem.

### 3. Tracking service usage against a target

AWS Budgets can monitor usage-based values, not just money. For example, a team may want to track a specific amount of service usage and be warned when it approaches the limit.

### 4. Monitoring Reserved Instance utilization and coverage

Organizations using Reserved Instances can check whether they are fully benefiting from their commitments. This helps avoid underusing purchased reservations.

### 5. Monitoring Savings Plans utilization and coverage

Teams can also track how well their Savings Plans are being used. This helps them understand whether their committed discounts are being applied effectively.

### 6. Supporting team-level cost governance

Budgets can be filtered by account, service, region, or tag. This helps different teams or departments stay within their own cost targets.

### 7. Automating cost-control actions

AWS Budgets can be linked to budget actions. This allows certain responses to happen automatically when a threshold is reached, helping enforce spending rules.

---

## Key features

### 1. Cost budgets

These budgets track AWS spending in money terms. They are used when you want to control how much you spend over a given time period.

### 2. Usage budgets

These budgets track service usage instead of cost. They are useful when you want to monitor consumption levels rather than billing amounts.

### 3. Reserved Instance budgets

AWS Budgets can track Reserved Instance utilization and coverage. This helps organizations measure whether their RI purchases are being used efficiently.

### 4. Savings Plans budgets

AWS Budgets can also track Savings Plans utilization and coverage. This is useful for making sure long-term discount commitments are providing value.

### 5. Actual and forecasted alerts

AWS Budgets can notify you based on current values and predicted end-of-period values. This is important because it is not limited to past spending only.

### 6. Budget actions

You can configure automated responses when thresholds are crossed. This makes AWS Budgets more than just a notification tool.

### 7. Flexible filtering

Budgets can be filtered by dimensions such as account, service, tag, or region. This makes it easier to monitor costs for specific business units or workloads.

### 8. Recurring or custom budget periods

You can create budgets for recurring time periods such as monthly, quarterly, or annually, or define custom time ranges depending on the use case.

### 9. Threshold-based notifications

You can set multiple alert levels for the same budget. This gives teams early warning before reaching the final limit.

---

## How it works

### 1. Create a budget

You create a budget in AWS Billing and Cost Management.

### 2. Choose what to track

You select whether the budget is for cost, usage, Reserved Instances, or Savings Plans.

### 3. Set a target amount or goal

You define the threshold you want AWS to compare against.

### 4. Add alert thresholds

You choose values such as 80%, 90%, and 100%.

### 5. AWS tracks actual and forecasted values

AWS compares live and predicted values against your target.

### 6. Notifications are sent when thresholds are reached

AWS Budgets can alert the right people when a threshold is crossed.

### 7. Optional actions can be triggered

If configured, AWS Budgets can apply budget actions to help control spending.

---

## Why it is important for the exam

AWS Budgets is important for the AWS Certified Cloud Practitioner exam because it is one of the main AWS services for cost control and governance.

You should remember that:

### 1. It helps control costs

AWS Budgets is used to set limits and monitor whether you are staying within them.

### 2. It supports forecasted alerts

It can warn you before the billing period ends if AWS predicts that you will exceed the budget.

### 3. It is for financial governance, not performance monitoring

AWS Budgets is about spending and usage targets, not CPU, memory, logs, or application health.

### 4. It is different from analysis-focused tools

It is often confused with Cost Explorer, but AWS Budgets focuses on limits, alerts, and governance.

### 5. It can support automation

Budget actions make it more powerful than a simple email notification service.

---

## Related AWS services and differences

### AWS Budgets vs Cost Explorer

**AWS Budgets:** Sets targets, tracks progress against them, and sends alerts or actions.

**Cost Explorer:** Helps analyze and visualize historical cost and usage data.

### AWS Budgets vs AWS Cost and Usage Report (CUR)

**AWS Budgets:** Good for alerts, thresholds, and ongoing cost control.

**CUR:** Provides detailed raw billing and usage data for advanced reporting and analysis.

### AWS Budgets vs AWS Pricing Calculator

**AWS Budgets:** Tracks real AWS costs and usage after or during actual usage.

**AWS Pricing Calculator:** Estimates expected cost before deployment.

### AWS Budgets vs Amazon CloudWatch

**AWS Budgets:** Monitors billing-related targets such as cost, usage, RI coverage, and Savings Plans utilization.

**Amazon CloudWatch:** Monitors operational metrics such as CPU, memory, logs, alarms, and application performance.

---

## Common exam traps

### Trap 1. Thinking AWS Budgets only looks at past spending

This is incorrect because AWS Budgets can also generate alerts based on forecasted spending. In the exam, if the question mentions predicting that costs will exceed a target before the month ends, AWS Budgets is a strong answer.

### Trap 2. Confusing AWS Budgets with Cost Explorer

This is a very common trap. Cost Explorer is mainly for analysis and visualization, while AWS Budgets is for setting thresholds, receiving alerts, and applying governance.

### Trap 3. Thinking AWS Budgets monitors CPU, memory, or application health

That is normally the role of Amazon CloudWatch. If the exam asks about operational metrics, logs, or infrastructure performance, AWS Budgets is not the right choice.

### Trap 4. Assuming AWS Budgets is only for cost budgets

AWS Budgets can also track usage budgets, Reserved Instance utilization and coverage, and Savings Plans utilization and coverage. The exam may test whether you know it is broader than just spending alerts.

### Trap 5. Thinking budgets can only send notifications

AWS Budgets can also be connected to budget actions. This means the service can support automated responses, not just warnings.

### Trap 6. Confusing AWS Budgets with AWS Pricing Calculator

The Pricing Calculator is used before deployment to estimate cost. AWS Budgets is used to monitor actual and forecasted usage or spending after services are in use.

### Trap 7. Confusing AWS Budgets with CUR

The Cost and Usage Report is meant for detailed billing data export and deep reporting. AWS Budgets is designed for simpler control, thresholds, and alerts.

---

## AWS exam keywords for AWS Budgets

These are common words and phrases that may appear in AWS exam questions about AWS Budgets:

* Budget
* Cost budget
* Usage budget
* Budget threshold
* Forecasted cost
* Actual cost
* Alert
* Notification
* Budget action
* Spending limit
* Monthly limit
* Cost control
* Cost governance
* Billing alert
* Reserved Instance utilization
* Reserved Instance coverage
* Savings Plans utilization
* Savings Plans coverage
* AWS Billing and Cost Management
* Track against target
* Threshold reached
* Forecasted to exceed budget
* Filter by service
* Filter by tag
* Filter by account
* Filter by region

---

## Easy real-world example

A startup wants to keep its AWS bill under **$200 per month**.

It creates an AWS Budget with:

### 1. A monthly cost budget of $200

This sets the spending target.

### 2. Alerts at 80%, 90%, and 100%

These thresholds warn the team before the full budget is exceeded.

### 3. Notifications sent to the finance lead and cloud administrator

This ensures the right people know when spending is rising.

### 4. An optional budget action

If configured, this can help apply an automatic cost-control response.

---

## Final summary

AWS Budgets is a cost control and governance service. It helps you define targets for AWS spending, usage, Reserved Instances, and Savings Plans. It compares actual and forecasted values against those targets, sends alerts when thresholds are reached, and can trigger budget actions.

For the exam, remember it as the AWS service for **budget limits, alerts, forecast-based warnings, and cost governance**.

---

## Short exam answer

AWS Budgets is an AWS cost management service that lets you set custom budgets for cost, usage, Reserved Instances, and Savings Plans, then receive alerts or trigger actions when thresholds are reached.

---

## Memory trick

**Budgets = boundaries for your bill.**

If **Cost Explorer** is the dashboard, **AWS Budgets** is the alarm system.
