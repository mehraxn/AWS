#!/usr/bin/env python3
"""Apply the source-verified, allowlisted terminology corrections for AWS-006."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

QUICK_FILES = [
    "14-ai-ml-analytics-and-other-services/README.md",
    "14-ai-ml-analytics-and-other-services/analytics/amazon-athena/01-overview.md",
    "14-ai-ml-analytics-and-other-services/analytics/amazon-quicksight/01-overview.md",
    "14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/01-overview.md",
    "15-comparisons-and-decision-guides/analytics/01-emr-vs-redshift.md",
    "docs/service-index.md",
]

HEALTH_FILES = [
    "12-billing-pricing-and-support/aws-health-dashboard/01-overview.md",
    "12-billing-pricing-and-support/aws-support/02-support-plans.md",
]

SAGEMAKER_FILES = [
    "12-billing-pricing-and-support/aws-savings-plans/02-study-guide.md",
    "14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/amazon-rekognition/01-overview.md",
    "14-ai-ml-analytics-and-other-services/internet-of-things/aws-iot-greengrass/01-overview.md",
]


def replace(relative: str, pairs: list[tuple[str, str]]) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in pairs:
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8", newline="\n")


def main() -> None:
    for relative in QUICK_FILES:
        replace(relative, [("Amazon QuickSight", "Amazon Quick Sight"), ("Amazon Quicksight", "Amazon Quick Sight")])
    for relative in HEALTH_FILES:
        replace(relative, [("AWS Personal Health Dashboard", "AWS Health Dashboard"), ("Personal Health Dashboard", "AWS Health Dashboard")])
    for relative in SAGEMAKER_FILES:
        replace(relative, [("Amazon SageMaker", "Amazon SageMaker AI")])


if __name__ == "__main__":
    main()
