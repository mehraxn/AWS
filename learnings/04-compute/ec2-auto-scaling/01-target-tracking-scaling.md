# AWS Target Tracking Scaling Policy 

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Title

**AWS Target Tracking Scaling Policy**

---

## Simple Definition

A **Target Tracking Scaling Policy** is an AWS Auto Scaling policy that automatically adds or removes capacity to keep a chosen metric close to a target value.

For example, you can tell AWS to keep average CPU utilization around **50%**.

AWS then adjusts capacity for you.

---

## Core Idea in Plain English

Think of target tracking like a **thermostat**.

You do not manually turn the heating on and off every few minutes.
You simply choose the temperature you want, and the thermostat keeps the room close to that target.

Target tracking works the same way.

You choose:

* a metric, such as CPU utilization
* a target value, such as 50%

AWS then automatically:

* scales **out** when the metric rises above the target
* scales **in** when the metric drops below the target

This makes it one of the easiest scaling methods to understand and use.

---

## Main Use Cases

### 1. Scaling web applications with changing traffic

Web applications often have traffic that goes up and down during the day.

A target tracking policy helps the application stay responsive by automatically adding more capacity when load increases and reducing capacity when traffic becomes quiet.

### 2. Managing EC2 Auto Scaling groups automatically

Many companies run applications on EC2 instances inside an Auto Scaling group.

Target tracking is useful here because it helps maintain stable performance without requiring the team to manually define many thresholds.

### 3. Scaling Amazon ECS services

Container-based applications running on Amazon ECS may need more tasks when demand increases.

Target tracking can automatically increase or decrease the number of running tasks based on metrics such as CPU or memory utilization.

### 4. Handling workloads with unpredictable demand

Some systems do not follow a fixed schedule.

Instead of guessing when to add capacity, target tracking reacts to real-time demand, which makes it useful for dynamic workloads.

### 5. Balancing performance and cost

A business wants strong performance during busy times but does not want to overpay during quiet periods.

Target tracking helps achieve both goals by scaling capacity up only when needed and scaling down when demand falls.

### 6. Reducing operational effort

Teams that want a simpler and more automatic scaling setup often choose target tracking.

It reduces the need to manually manage many alarm thresholds and scaling actions.

---

## Key Features

### 1. Automatic scaling around a target metric

The main feature is that AWS tries to keep a selected metric close to the value you set.

Instead of manually defining many rules, you define the target and AWS handles the response.

### 2. Simple configuration

Target tracking is easier to configure than more manual scaling methods such as step scaling.

This simplicity is one reason it is often tested in beginner AWS exams.

### 3. AWS manages the CloudWatch alarms

You do not usually need to create and manage the scaling alarms yourself.

AWS creates and manages the required CloudWatch alarms in the background.

### 4. Supports scale-out and scale-in

The policy can both:

* add capacity when demand increases
* remove capacity when demand decreases

This helps maintain performance while also controlling cost.

### 5. Works well with common utilization metrics

It is commonly used with metrics such as:

* average CPU utilization
* average memory utilization for some services
* request count per target

These metrics are useful because they reflect actual workload pressure.

### 6. Designed to maintain steady performance

Target tracking is meant to keep performance stable by reacting when the metric moves away from the target.

It is not about keeping a fixed number of instances. It is about keeping a metric near the desired level.

### 7. Usually scales in more carefully than it scales out

AWS is generally more careful when reducing capacity, because removing resources too quickly can hurt application availability or cause performance issues.

This is an important practical point and also a useful exam concept.

---

## How It Works

### 1. You choose a metric

This is the metric AWS will watch.

Common examples include:

* average CPU utilization
* request count per target
* ECS service average CPU usage
* ECS service average memory usage

### 2. You choose a target value

This is the level AWS tries to maintain.

Examples:

* keep CPU around 50%
* keep request count per target near a selected number

### 3. AWS monitors the metric through CloudWatch

Amazon CloudWatch provides the metric data.

Target tracking continuously checks whether the metric is above or below the target.

### 4. AWS adjusts capacity automatically

* If the metric is **above** the target, AWS adds capacity.
* If the metric is **below** the target, AWS removes capacity.

### 5. AWS keeps correcting over time

AWS keeps making adjustments so the metric stays close to the selected target.

This is why target tracking is easier than manually writing many threshold-based rules.

---

## Why It Is Important for the Exam

Target tracking scaling policy is important for the AWS Certified Cloud Practitioner exam because it represents the **simplest and most automatic dynamic scaling method**.

You should remember these points:

* **Target tracking = easy dynamic scaling**
* **AWS manages the alarms**
* **You set the target, AWS handles the scaling**
* **It helps balance performance and cost**

In many exam questions, target tracking is the correct answer when the scenario says:

* traffic changes automatically
* the company wants less manual work
* the system should maintain performance
* the company wants a simple scaling solution

---

## Related AWS Services and Differences

### 1. Target Tracking vs Step Scaling

**Target tracking** is simpler.

You choose a metric and a target value, and AWS decides how to scale.

**Step scaling** is more manual.

You define exact thresholds and the exact actions to take at each threshold.

Example of step scaling:

* if CPU is above 60%, add 1 instance
* if CPU is above 80%, add 3 instances

**Exam tip:**
If the question asks for the **simpler**, **more automatic**, or **lower-effort** solution, target tracking is usually the better answer.

### 2. Target Tracking vs Simple Scaling

**Simple scaling** is older and more basic.

It uses a CloudWatch alarm and one scaling adjustment, often with cooldown periods.

**Target tracking** is more intelligent and more automated, so it is generally preferred in modern AWS scenarios.

### 3. Target Tracking vs Scheduled Scaling

**Scheduled scaling** is used when demand is predictable by time.

Example:

* add capacity every day at 9 AM

**Target tracking** is used when demand changes in real time.

Example:

* add capacity when CPU rises above the desired level

### 4. Target Tracking and CloudWatch

CloudWatch provides the metrics used for scaling.

With target tracking, AWS automatically creates and manages the CloudWatch alarms needed for the policy.

### 5. Related AWS Services

* **Amazon EC2 Auto Scaling** – scales EC2 instances in an Auto Scaling group
* **Amazon ECS Service Auto Scaling** – scales ECS tasks
* **Application Auto Scaling** – scales supported AWS services such as ECS, DynamoDB, Aurora replicas, and more
* **Amazon CloudWatch** – provides the monitoring metrics used by the scaling policy

---

## Common Exam Traps

### Trap 1. Confusing target tracking with step scaling

This is one of the most common mistakes.

If the question gives exact rules such as:

* above 60%, add 1 instance
* above 80%, add 2 more instances

that is **step scaling**, not target tracking.

**Why this trap appears:**
Both are dynamic scaling methods, so students often mix them up.

### Trap 2. Forgetting that AWS manages the alarms

In target tracking, AWS usually creates and manages the CloudWatch alarms for you.

**Why this matters in the exam:**
If the question asks for the solution with the **least manual effort**, this is a strong clue for target tracking.

### Trap 3. Thinking target tracking keeps a fixed number of instances

That is incorrect.

Target tracking does not try to keep a fixed number of resources.
It tries to keep a **metric** near a target value.

The number of instances or tasks may change many times.

### Trap 4. Mixing target tracking with scheduled scaling

If demand happens at known times, scheduled scaling may be a better fit.

If demand changes according to real usage, target tracking is usually more appropriate.

**Exam clue:**

* predictable time-based demand → scheduled scaling
* unpredictable live demand → target tracking

### Trap 5. Choosing a poor metric

The metric used for target tracking should actually reflect workload demand.

For exam questions, common good examples are:

* CPU utilization
* request count per target
* ECS CPU or memory utilization

If the metric does not reflect real load, scaling may not behave well.

### Trap 6. Thinking target tracking is manual threshold tuning

The idea of target tracking is that you do **not** define lots of detailed threshold rules yourself.

You provide the target, and AWS does the adjustment work.

This makes it more automatic than step scaling.

---

## Easy Real-World Example

A company runs an online store on Amazon EC2.

On normal days, traffic is low. During promotions, traffic rises quickly.

The company wants the website to stay fast, but it also wants to avoid paying for too many servers when traffic is low.

So the company creates a target tracking scaling policy with:

* **Metric:** average CPU utilization
* **Target:** 50%

What happens:

* if CPU goes above 50%, AWS launches more EC2 instances
* if CPU goes below 50%, AWS removes some instances

Result:

* good performance during busy periods
* lower cost during quiet periods
* minimal manual effort

---

## AWS Exam Keywords for This Service

These are words and phrases that may appear in the exam and should make you think of **Target Tracking Scaling Policy**:

* target value
* keep metric near target
* automatic dynamic scaling
* scale out automatically
* scale in automatically
* maintain CPU at 50%
* request count per target
* simplest scaling option
* highly automated scaling
* low operational effort
* AWS manages alarms
* CloudWatch metrics
* maintain performance
* respond to changing demand
* thermostat model
* balance cost and performance

### Strong clue phrases in exam questions

If you see phrases like these, target tracking is often the right answer:

* “keep CPU utilization around 50%”
* “automatically maintain a metric near a target”
* “reduce manual scaling effort”
* “simplest dynamic scaling method”
* “AWS should automatically create and manage alarms”
* “application traffic changes throughout the day”

---

## Auto Scaling Group Design Supplement

An Auto Scaling group uses a launch template and maintains **minimum**, **desired**, and **maximum** capacity. Scaling out adds instances; scaling in removes them. Target tracking follows a target, step scaling responds by alarm severity, scheduled scaling anticipates known timing, and predictive scaling can forecast recurring demand. Instance warmup prevents new instances from distorting metrics.

Spread the group across AZs and attach an ELB target group. EC2 or load-balancer health checks can trigger replacement. Auto Scaling supplies capacity; ELB routes traffic; multi-AZ deployment improves availability. None alone guarantees application fault tolerance, especially with local state.

Choose a metric proportional to per-instance load and test scale-in. Minimum capacity improves readiness but costs more; aggressive scale-in risks disruption; launch time affects spike response.

### Knowledge Check

1. What is the current target size? **Desired capacity.**
2. What policy suits a known weekday peak? **Scheduled scaling.**
3. Does an ASG alone make stateful software fault tolerant? **No.**

## Official References

- [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)
- [Health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html)

Official references checked: 2026-07-22.

## Final Summary

A Target Tracking Scaling Policy is an AWS Auto Scaling policy that automatically adds or removes capacity to keep a selected metric close to a target value.

It is one of the easiest and most automatic scaling methods in AWS.

You choose:

* the metric
* the target value

AWS then handles the scaling adjustments for you.

For the exam, remember that target tracking is best when you want:

* automatic scaling
* less manual configuration
* steady performance
* cost efficiency

---

## Short Exam Answer

A Target Tracking Scaling Policy automatically adds or removes capacity to keep a selected metric, such as CPU utilization, near a target value. It is a simple and highly automated dynamic scaling method in AWS.

---

## Memory Trick

**Target Tracking = Thermostat Scaling**

A thermostat keeps room temperature near a chosen target.

Target tracking keeps CPU, requests, or another metric near a chosen target.

So remember:

**Set the target, let AWS adjust.**

---

## If I Were an Examiner...

If I were writing an AWS exam question about Target Tracking Scaling Policy, I would test these ideas:

### 1. Do you know it is the simplest dynamic scaling option?

I may describe a company that wants automatic scaling with minimal setup and see whether you choose target tracking.

### 2. Do you know the difference between target tracking and step scaling?

I may give choices that include exact thresholds and see whether you can recognize that those belong to step scaling instead.

### 3. Do you know that AWS manages the alarms?

I may ask for the option that reduces operational effort and does not require manually configuring many CloudWatch alarms.

### 4. Do you know it works by maintaining a metric, not a fixed capacity?

I may try to confuse you by making it sound like the policy keeps the same number of instances all the time.

### 5. Do you know when scheduled scaling is better?

I may compare predictable daily traffic with unpredictable live traffic and check whether you choose the right scaling method.

### 6. Do you recognize exam clue words?

I may include phrases like:

* maintain CPU around 50%
* automatically keep a metric near target
* simple dynamic scaling
* least administrative effort

These are strong clues pointing to **Target Tracking Scaling Policy**.

---

## One-Line Exam Memory

**Target Tracking Scaling Policy = set a target metric, and AWS automatically adjusts capacity to stay near it.**
