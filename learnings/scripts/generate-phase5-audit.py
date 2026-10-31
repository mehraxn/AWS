"""Generate Recovery Phase 5 certification-audit artifacts from canonical notes.

This is an audit-only generator. It reads, but never writes, numbered learning
directories. Official baseline data was transcribed and paraphrased from the AWS
exam guides checked on 2026-07-21.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "certification-audit"
CHECKED = "2026-07-21"
CPP_GUIDE = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html"
CPP_TECH = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-technologies-concepts.html"
CPP_SCOPE = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html"
CPP_OUT = "https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-out-of-scope-services.html"
SAA_GUIDE = "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html"
SAA_SCOPE = "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html"
SAA_OUT = "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html"
CPP_BADGE = "2EA44F"
SAA_BADGE = "0969DA"

CATEGORIES = [f"{i:02d}-" for i in range(1, 17)]

CPP_DOMAINS = {
    "1": ("Cloud Concepts", "24%"),
    "2": ("Security and Compliance", "30%"),
    "3": ("Cloud Technology and Services", "34%"),
    "4": ("Billing, Pricing, and Support", "12%"),
}
SAA_DOMAINS = {
    "1": ("Design Secure Architectures", "30%"),
    "2": ("Design Resilient Architectures", "26%"),
    "3": ("Design High-Performing Architectures", "24%"),
    "4": ("Design Cost-Optimized Architectures", "20%"),
}

# task id, title, expected category, paraphrased knowledge statements, paraphrased skills
CPP_TASKS = [
    ("1.1", "Define the AWS Cloud and its value proposition", "01-cloud-fundamentals", ["AWS Cloud value proposition", "cloud economics", "global reach and agility"], ["Explain cloud benefits", "Match cloud benefits to business needs"]),
    ("1.2", "Identify AWS Cloud design principles", "13-architecture-and-design-patterns", ["Well-Architected pillars", "design for failure", "elasticity and automation"], ["Recognize appropriate cloud design principles"]),
    ("1.3", "Understand migration benefits and strategies", "11-migration-and-hybrid-cloud", ["AWS Cloud migration benefits", "migration strategies", "AWS Cloud Adoption Framework"], ["Identify migration approaches", "Recognize migration assistance resources"]),
    ("1.4", "Understand cloud economics", "12-billing-pricing-and-support", ["fixed versus variable cost", "rightsizing", "economies of scale", "licensing strategy"], ["Compare on-premises and cloud costs", "Identify cost optimization practices"]),
    ("2.1", "Understand the Shared Responsibility Model", "01-cloud-fundamentals", ["AWS responsibilities", "customer responsibilities", "responsibility changes by service model"], ["Assign security tasks for EC2, RDS, and Lambda"]),
    ("2.2", "Understand security, governance, and compliance", "09-security-and-compliance", ["compliance concepts", "encryption", "logging and auditing", "governance services"], ["Identify AWS Artifact and compliance resources", "Choose monitoring and auditing services"]),
    ("2.3", "Understand access management", "03-identity-governance-and-organizations", ["least privilege", "root user protection", "IAM identities and policies", "federation and cross-account access"], ["Apply MFA and access-key practices", "Select users, groups, roles, policies, and Identity Center"]),
    ("2.4", "Identify security resources and capabilities", "09-security-and-compliance", ["AWS security services", "security guidance", "Trusted Advisor security checks"], ["Recognize threat detection and protection services", "Locate AWS security assistance"]),
    ("3.1", "Define deployment and operation methods", "10-monitoring-management-and-deployment", ["Management Console, CLI, SDK, and API access", "cloud, hybrid, and on-premises deployment", "infrastructure as code"], ["Select an AWS interaction method", "Recognize deployment models"]),
    ("3.2", "Understand AWS global infrastructure", "02-global-infrastructure", ["Regions", "Availability Zones", "edge locations", "high availability and multi-Region use"], ["Select Regions and Availability Zones", "Recognize edge-service benefits"]),
    ("3.3", "Identify AWS compute services", "04-compute", ["EC2 instance families", "containers", "serverless compute", "Auto Scaling and load balancing"], ["Select a compute option", "Recognize scaling and load-balancing use cases"]),
    ("3.4", "Identify AWS database services", "06-databases", ["relational databases", "NoSQL databases", "caching", "database migration"], ["Select a database category", "Recognize managed database benefits"]),
    ("3.5", "Identify AWS network services", "07-networking-and-content-delivery", ["VPC components", "security groups and network ACLs", "Route 53", "VPN and Direct Connect"], ["Recognize public, private, and hybrid connectivity", "Select basic network controls"]),
    ("3.6", "Identify AWS storage services", "05-storage", ["object, block, and file storage", "S3 storage classes", "EBS and instance store", "EFS and FSx", "Storage Gateway and Backup"], ["Select a storage type", "Recognize lifecycle and backup options"]),
    ("3.7", "Identify AI, ML, and analytics services", "14-ai-ml-analytics-and-other-services", ["AI and ML service purposes", "analytics service purposes", "data ingestion and visualization"], ["Recognize common AI/ML and analytics use cases"]),
    ("3.8", "Identify other in-scope service categories", "14-ai-ml-analytics-and-other-services", ["application integration", "business applications", "developer tools", "end-user computing", "frontend and IoT services"], ["Recognize services by category and business use"]),
    ("4.1", "Compare AWS pricing models", "12-billing-pricing-and-support", ["On-Demand, Reserved, Spot, and Savings Plans", "storage pricing drivers", "data transfer pricing"], ["Choose a purchasing model", "Identify major cost drivers"]),
    ("4.2", "Understand billing and cost-management resources", "12-billing-pricing-and-support", ["Budgets", "Cost Explorer", "Cost and Usage Reports", "Organizations and cost allocation tags"], ["Select cost tools", "Recognize consolidated billing and tagging"]),
    ("4.3", "Identify AWS support resources", "12-billing-pricing-and-support", ["AWS Support plans", "AWS re:Post and documentation", "Trusted Advisor and AWS Health", "Partners, Marketplace, and Professional Services"], ["Select a support resource", "Recognize support-plan differences"]),
]

SAA_TASKS = [
    ("1.1", "Design secure access to AWS resources", "03-identity-governance-and-organizations", ["multi-account access", "federation and IAM Identity Center", "least privilege", "resource and identity policies", "SCPs and Control Tower"], ["Design root and MFA controls", "Design cross-account and federated access", "Apply least privilege"]),
    ("1.2", "Design secure workloads and applications", "09-security-and-compliance", ["credential management", "secure endpoints", "network segmentation", "edge protection", "threat detection"], ["Design VPC security boundaries", "Select WAF, Shield, firewall, and detection controls", "Secure hybrid connectivity"]),
    ("1.3", "Determine data security controls", "09-security-and-compliance", ["data classification", "encryption at rest and in transit", "key and certificate management", "retention and recovery", "compliance controls"], ["Design KMS and TLS usage", "Design backup, replication, lifecycle, and key rotation"]),
    ("2.1", "Design scalable and loosely coupled architectures", "13-architecture-and-design-patterns", ["stateless and microservice design", "event-driven architecture", "messaging and workflows", "caching", "horizontal scaling"], ["Design multi-tier and serverless systems", "Select queues, topics, events, and workflows", "Select load balancing and containers"]),
    ("2.2", "Design highly available and fault-tolerant architectures", "13-architecture-and-design-patterns", ["failure domains", "Multi-AZ and Multi-Region", "disaster recovery strategies", "durability and failover", "service quotas and observability"], ["Remove single points of failure", "Design recovery and failover", "Select resilient data and compute patterns"]),
    ("3.1", "Determine high-performing storage solutions", "05-storage", ["object, block, and file characteristics", "storage performance", "access patterns", "hybrid storage", "data lifecycle"], ["Select S3, EBS, EFS, FSx, and instance storage", "Match throughput, IOPS, latency, and durability requirements"]),
    ("3.2", "Design high-performing and elastic compute", "04-compute", ["compute selection", "instance families and sizing", "Auto Scaling", "load balancing", "containers and serverless"], ["Select compute for workload characteristics", "Design elastic capacity", "Choose scaling metrics and policies"]),
    ("3.3", "Determine high-performing database solutions", "06-databases", ["relational and nonrelational selection", "read scaling", "caching", "serverless databases", "database migration"], ["Choose database engines", "Design replicas, caches, and partitions", "Match consistency and performance needs"]),
    ("3.4", "Determine high-performing network architectures", "07-networking-and-content-delivery", ["VPC design", "hybrid connectivity", "DNS and routing", "edge delivery", "network performance"], ["Design subnets and routing", "Choose VPN, Direct Connect, Transit Gateway, and peering", "Select CloudFront or Global Accelerator"]),
    ("3.5", "Determine high-performing data ingestion and transformation", "14-ai-ml-analytics-and-other-services", ["streaming and batch ingestion", "data transformation", "data lakes and warehouses", "analytics stores", "transfer services"], ["Select Kinesis, Firehose, Glue, EMR, and Redshift", "Design ingestion for volume, velocity, and format"]),
    ("4.1", "Design cost-optimized storage", "05-storage", ["storage classes", "lifecycle policies", "retention", "access patterns", "backup cost"], ["Choose cost-effective storage", "Automate tiering and expiration", "Balance retrieval and durability needs"]),
    ("4.2", "Design cost-optimized compute", "04-compute", ["purchasing options", "rightsizing", "elasticity", "serverless and containers", "license considerations"], ["Choose On-Demand, Spot, Reserved Instances, or Savings Plans", "Reduce idle capacity", "Match compute model to demand"]),
    ("4.3", "Design cost-optimized databases", "06-databases", ["engine and licensing costs", "capacity models", "read scaling", "retention and backup", "managed service trade-offs"], ["Select cost-effective database", "Right-size and scale database capacity", "Balance operational and service cost"]),
    ("4.4", "Design cost-optimized networks", "07-networking-and-content-delivery", ["data transfer charges", "NAT and endpoint costs", "hybrid connectivity costs", "content delivery", "network topology"], ["Reduce cross-AZ and internet transfer cost", "Choose endpoints and gateways", "Balance managed connectivity cost and operations"]),
]

CPP_SERVICES = "Amazon Athena|Amazon EMR|AWS Glue|Amazon Kinesis|Amazon OpenSearch Service|Amazon QuickSight|Amazon Redshift|Amazon EventBridge|Amazon SNS|Amazon SQS|AWS Step Functions|Amazon Connect|Amazon SES|AWS Budgets|AWS Cost and Usage Reports|AWS Cost Explorer|AWS Marketplace|AWS Batch|Amazon EC2|AWS Elastic Beanstalk|Amazon Lightsail|AWS Outposts|Amazon ECR|Amazon ECS|Amazon EKS|AWS Support|Amazon Aurora|Amazon DocumentDB|Amazon DynamoDB|Amazon ElastiCache|Amazon Neptune|Amazon RDS|AWS CLI|AWS CodeBuild|AWS CodePipeline|AWS X-Ray|Amazon AppStream 2.0|Amazon WorkSpaces|Amazon WorkSpaces Secure Browser|AWS Amplify|AWS AppSync|AWS IoT Core|Amazon Comprehend|Amazon Kendra|Amazon Lex|Amazon Polly|Amazon Q|Amazon Rekognition|Amazon SageMaker AI|Amazon Textract|Amazon Transcribe|Amazon Translate|AWS Auto Scaling|AWS CloudFormation|AWS CloudTrail|Amazon CloudWatch|AWS Compute Optimizer|AWS Config|AWS Control Tower|AWS Health Dashboard|AWS License Manager|AWS Management Console|AWS Organizations|AWS Service Catalog|Service Quotas|AWS Systems Manager|AWS Trusted Advisor|AWS Well-Architected Tool|AWS Application Discovery Service|AWS Application Migration Service|AWS Database Migration Service|Migration Evaluator|AWS Migration Hub|AWS Schema Conversion Tool|AWS Snow Family|Amazon API Gateway|Amazon CloudFront|AWS Direct Connect|AWS Global Accelerator|AWS PrivateLink|Amazon Route 53|AWS Transit Gateway|Amazon VPC|AWS VPN|AWS Site-to-Site VPN|AWS Client VPN|AWS Artifact|AWS Audit Manager|AWS Certificate Manager|AWS CloudHSM|Amazon Cognito|Amazon Detective|AWS Directory Service|AWS Firewall Manager|Amazon GuardDuty|AWS IAM|AWS IAM Identity Center|Amazon Inspector|AWS KMS|Amazon Macie|AWS Resource Access Manager|AWS Secrets Manager|AWS Security Hub|AWS Shield|AWS WAF|AWS Fargate|AWS Lambda|AWS Backup|Amazon EBS|Amazon EFS|AWS Elastic Disaster Recovery|Amazon FSx|Amazon S3|Amazon S3 Glacier|AWS Storage Gateway".split("|")
SAA_SERVICES = "Amazon Athena|AWS Data Exchange|Amazon Data Firehose|Amazon EMR|AWS Glue|Amazon Kinesis|AWS Lake Formation|Amazon MSK|Amazon OpenSearch Service|Amazon Quick|Amazon Redshift|Amazon AppFlow|AWS AppSync|Amazon EventBridge|Amazon MQ|Amazon SNS|Amazon SQS|AWS Step Functions|AWS Budgets|AWS Cost and Usage Report|AWS Cost Explorer|Savings Plans|AWS Batch|Amazon EC2|Amazon EC2 Auto Scaling|AWS Elastic Beanstalk|AWS Outposts|AWS Serverless Application Repository|VMware Cloud on AWS|AWS Wavelength|Amazon ECR|Amazon ECS|Amazon ECS Anywhere|Amazon EKS|Amazon EKS Anywhere|Amazon EKS Distro|Amazon Aurora|Amazon Aurora Serverless|Amazon DocumentDB|Amazon DynamoDB|Amazon ElastiCache|Amazon Keyspaces|Amazon Neptune|Amazon RDS|Amazon Redshift|AWS X-Ray|AWS Amplify|Amazon API Gateway|AWS Device Farm|Amazon Comprehend|Amazon Kendra|Amazon Lex|Amazon Polly|Amazon Rekognition|Amazon SageMaker AI|Amazon Textract|Amazon Transcribe|Amazon Translate|AWS Auto Scaling|AWS CLI|AWS CloudFormation|AWS CloudTrail|Amazon CloudWatch|AWS Compute Optimizer|AWS Config|AWS Control Tower|AWS Health Dashboard|AWS License Manager|Amazon Managed Grafana|Amazon Managed Service for Prometheus|AWS Management Console|AWS Organizations|AWS Service Catalog|AWS Systems Manager|AWS Trusted Advisor|AWS Well-Architected Tool|Amazon Elastic Transcoder|Amazon Kinesis Video Streams|AWS Application Migration Service|AWS DataSync|AWS DMS|AWS Snow Family|AWS Transfer Family|AWS Client VPN|Amazon CloudFront|AWS Direct Connect|Elastic Load Balancing|AWS Global Accelerator|AWS PrivateLink|Amazon Route 53|AWS Site-to-Site VPN|AWS Transit Gateway|Amazon VPC|AWS Artifact|AWS Audit Manager|AWS Certificate Manager|AWS CloudHSM|Amazon Cognito|Amazon Detective|AWS Directory Service|AWS Firewall Manager|Amazon GuardDuty|AWS IAM Identity Center|Amazon Inspector|AWS KMS|Amazon Macie|AWS Network Firewall|AWS Resource Access Manager|AWS Secrets Manager|AWS Security Hub|AWS Shield|AWS WAF|AWS IAM|AWS Fargate|AWS Lambda|AWS Backup|Amazon EBS|Amazon EFS|Amazon FSx|Amazon S3|Amazon S3 Glacier|AWS Storage Gateway".split("|")
CPP_OUT_SERVICES = "Amazon AppFlow|AWS Clean Rooms|AWS Data Exchange|Amazon DataZone|Amazon MSK|Amazon Timestream for LiveAnalytics|AWS AppFabric|Amazon Simple Workflow Service|Amazon WorkDocs|Amazon WorkMail|AWS App Runner|AWS Copilot|AWS Wavelength|AWS Application Cost Profiler|Amazon DevPay|AWS Activate|AWS IQ|AWS Managed Services|AWS Billing Conductor|Amazon Keyspaces|Amazon MemoryDB for Redis OSS|AWS AppConfig|AWS Application Composer|AWS CodeArtifact|AWS CodeDeploy|Amazon CodeGuru|AWS CloudShell|AWS Device Farm|Amazon GameLift|Amazon Lumberyard|AWS IoT Device Defender|AWS IoT Greengrass|Amazon Monitron|Amazon Fraud Detector|Amazon Lookout for Metrics|Amazon Mechanical Turk|AWS Panorama|Amazon Personalize|AWS Chatbot|Amazon Data Lifecycle Manager|Amazon Elastic Transcoder|AWS Launch Wizard|AWS Elemental Appliances and Software|AWS Elemental MediaConnect|AWS Elemental MediaConvert|AWS Elemental MediaLive|AWS Elemental MediaPackage|AWS Elemental MediaStore|AWS Elemental MediaTailor|Amazon Interactive Video Service|AWS Migration Hub Refactor Spaces|AWS Transfer Family|AWS Cloud Map|AWS Network Access Analyzer|AWS Ground Station|Amazon VPC Lattice|Amazon Cloud Directory|AWS Network Firewall|AWS RoboMaker|Amazon FSx for Lustre".split("|")
SAA_OUT_SERVICES = "Amazon MWAA|Amazon Sumerian|Amazon Managed Blockchain|Amazon Lightsail|Amazon RDS on VMware|AWS CDK|AWS CloudShell|AWS CodeArtifact|AWS CodeBuild|AWS CodeCommit|AWS CodeDeploy|Amazon Corretto|AWS Fault Injection Simulator|AWS Tools and SDKs|Amazon Location Service|Amazon GameLift|All IoT services|Apache MXNet on AWS|Amazon Augmented AI|AWS DeepComposer|AWS Deep Learning AMIs|AWS Deep Learning Containers|Amazon DevOps Guru|Amazon Elastic Inference|Amazon HealthLake|AWS Inferentia|Amazon Personalize|PyTorch on AWS|Amazon SageMaker Canvas|Amazon SageMaker Ground Truth|TensorFlow on AWS|AWS Console Mobile Application|AWS Distro for OpenTelemetry|AWS Elemental Appliances and Software|AWS Elemental MediaConnect|AWS Elemental MediaConvert|AWS Elemental MediaLive|AWS Elemental MediaPackage|AWS Elemental MediaTailor|Amazon Interactive Video Service|Migration Evaluator|AWS Cloud Map|Amazon Braket|AWS Ground Station".split("|")

CONCEPTS = [
    ("Cloud value proposition", "core", "foundation"), ("AWS Shared Responsibility Model", "core", "foundation"),
    ("AWS global infrastructure", "core", "foundation"), ("AWS Well-Architected Framework", "core", "architecture"),
    ("AWS Cloud Adoption Framework", "core", "supporting"), ("migration strategies", "core", "architecture"),
    ("high availability", "core", "architecture"), ("fault tolerance", "supporting", "architecture"),
    ("elasticity and scalability", "core", "architecture"), ("disaster recovery", "supporting", "architecture"),
    ("least privilege", "core", "architecture"), ("federation and cross-account access", "supporting", "architecture"),
    ("encryption at rest and in transit", "core", "architecture"), ("multi-account governance", "supporting", "architecture"),
    ("infrastructure as code", "awareness", "architecture"), ("stateless architecture", "awareness", "architecture"),
    ("event-driven architecture", "awareness", "architecture"), ("decoupling", "core", "architecture"),
    ("caching", "awareness", "architecture"), ("load balancing", "core", "architecture"),
    ("Auto Scaling", "core", "architecture"), ("Multi-AZ design", "awareness", "architecture"),
    ("Multi-Region design", "awareness", "architecture"), ("RTO and RPO", "awareness", "architecture"),
    ("object block and file storage", "core", "architecture"), ("relational versus NoSQL", "core", "architecture"),
    ("VPC segmentation and routing", "core", "architecture"), ("hybrid connectivity", "awareness", "architecture"),
    ("monitoring logging and auditing", "core", "architecture"), ("rightsizing", "core", "architecture"),
    ("pricing models", "core", "architecture"), ("data transfer costs", "core", "architecture"),
    ("AWS Support resources", "core", "not-applicable"), ("service quotas", "awareness", "architecture"),
    ("streaming and batch ingestion", "awareness", "architecture"), ("backup and lifecycle", "core", "architecture"),
    ("AWS APIs", "awareness", "supporting"), ("AWS SDKs", "awareness", "supporting"),
    ("AWS Management Console and AWS CLI", "core", "supporting"), ("AWS compliance", "core", "architecture"),
    ("EC2 purchasing options", "core", "architecture"), ("AWS Partner Network", "awareness", "not-applicable"),
    ("AWS Pricing Calculator", "core", "supporting"), ("AWS Professional Services", "awareness", "not-applicable"),
    ("AWS re:Post", "awareness", "not-applicable"), ("AWS Prescriptive Guidance", "awareness", "supporting"),
    ("AWS Security Blog", "awareness", "supporting"), ("AWS Support Center and plans", "core", "not-applicable"),
    ("AWS Knowledge Center", "awareness", "supporting"), ("AWS Solutions Architects", "awareness", "supporting"),
    ("cloud migration and data transfer", "core", "architecture"), ("management and governance", "core", "architecture"),
]

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def lesson_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if any(p.relative_to(ROOT).as_posix().startswith(x) for x in CATEGORIES))

FILES = lesson_files()
TEXT = {p: p.read_text(encoding="utf-8", errors="replace") for p in FILES}

def headings(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M)]

def terms_for(phrase: str) -> list[str]:
    stop = {"aws", "amazon", "and", "the", "for", "with", "design", "understand", "identify", "determine", "secure", "high", "cloud"}
    return [w for w in norm(phrase).split() if w not in stop and len(w) > 2]

def evidence(query: str, expected: str = "") -> tuple[list[str], list[str], int]:
    q = terms_for(query)
    scored = []
    for p, body in TEXT.items():
        rel = p.relative_to(ROOT).as_posix()
        low = norm(body)
        score = sum(1 for w in q if w in low)
        if expected and rel.startswith(expected): score += 1
        if score:
            scored.append((score, len(body), rel, body))
    scored.sort(key=lambda x: (-x[0], -x[1], x[2]))
    picked = scored[:3]
    paths, hs = [], []
    for score, _, rel, body in picked:
        if score < max(1, min(2, len(q))): continue
        paths.append(rel)
        bh = headings(body)
        hit = next((h for h in bh if any(w in norm(h) for w in q)), bh[0] if bh else "(no heading)")
        hs.append(hit)
    strength = sum(x[0] for x in picked[:2])
    return paths, hs, strength

def depth(body: str, cert: str) -> str:
    n = len(re.findall(r"\b\w+\b", body))
    low = norm(body)
    arch = sum(k in low for k in ["trade off", "multi az", "multi region", "fault toler", "scalab", "architecture", "failover", "rto", "rpo", "scenario"])
    basic = sum(k in low for k in ["overview", "use case", "benefit", "pricing", "security", "what is"])
    if n < 35: return "mention-only"
    if cert == "saa":
        if arch >= 5 and n >= 700: return "scenario-ready"
        if arch >= 3 and n >= 400: return "architecture-and-design"
        if arch >= 1 and n >= 180: return "intermediate"
        return "awareness" if n >= 100 else "mention-only"
    if basic >= 4 and n >= 350: return "fundamental"
    if basic >= 2 and n >= 150: return "awareness"
    return "mention-only"

def yn(body: str, words: list[str]) -> str:
    low = norm(body)
    return "yes" if any(norm(x) in low for x in words) else "no"

def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (OUT / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader(); w.writerows(rows)

def title_for(p: Path, body: str) -> str:
    hs = headings(body)
    return re.sub(r"[*_`]", "", hs[0]) if hs else p.stem.replace("-", " ").title()

def inventory() -> list[dict]:
    rows = []
    for p in FILES:
        body = TEXT[p]; rel = p.relative_to(ROOT).as_posix(); low = norm(body); hs = headings(body)
        cpp = CPP_BADGE.lower() in body.lower(); saa = SAA_BADGE.lower() in body.lower()
        cppd, saad = depth(body, "cpp"), depth(body, "saa")
        words = len(re.findall(r"\b\w+\b", body))
        quality = "too-shallow" if words < 120 else "partial" if words < 400 else "adequate" if words < 900 else "strong"
        refs = re.findall(r"https?://[^\s)>]+", body)
        official = [u for u in refs if "aws.amazon.com" in u or "amazon.com" in u]
        services = [s for s in sorted(set(CPP_SERVICES + SAA_SERVICES)) if norm(s) in low]
        concepts = [c for c, _, _ in CONCEPTS if all(w in low for w in terms_for(c)[:2])]
        terminology = "review-required" if any(x in low for x in ["personal health dashboard", "amazon quicksight", "sagemaker studio", "elastic transcoder", "codecommit"]) else "current-or-no-issue-detected"
        rows.append({
            "canonical_path": rel, "title": title_for(p, body), "main_category": rel.split("/")[0],
            "services_mentioned": "; ".join(services[:12]), "concepts_covered": "; ".join(concepts[:12]),
            "current_cpp_badge": str(cpp).lower(), "current_saa_badge": str(saa).lower(),
            "actual_cpp_depth": cppd, "actual_saa_depth": saad,
            "architecture_scenarios": yn(body,["scenario","architecture","multi-AZ","multi-Region"]),
            "comparisons": yn(body,["comparison"," versus "," vs ","trade-off"]),
            "pricing_content": yn(body,["pricing","cost","On-Demand","Savings Plans"]),
            "security_content": yn(body,["security","encryption","IAM","least privilege"]),
            "resilience_content": yn(body,["resilience","high availability","fault tolerance","backup","failover"]),
            "official_references": "; ".join(official), "last_verified": CHECKED if official else "not-stated",
            "content_quality": quality, "terminology_status": terminology,
            "fact_review_required": "yes" if terminology == "review-required" or not official else "no",
            "navigation_status": "listed-in-category-readme" if p.name != "README.md" and (p.parent/"README.md").exists() else "category-index" if p.name == "README.md" else "missing-local-index",
            "notes": f"Body inspected; {words} words; {len(hs)} headings. Automated evidence inventory requires human confirmation before implementation."
        })
    return rows

def requirement_rows(tasks, domains, cert):
    rows=[]
    for task_id,title,cat,knowledge,skills in tasks:
        domain=task_id.split('.')[0]; dname,weight=domains[domain]; idx=0
        for typ, reqs in [("knowledge",knowledge),("skill",skills)]:
            for req in reqs:
                idx+=1; paths,hs,strength=evidence(req,cat)
                if not paths: status="missing"; cur="none"
                elif strength <= 3: status="mention-only"; cur="mention-only"
                else:
                    best=TEXT[ROOT/paths[0]]; cur=depth(best,cert)
                    if cert=="saa" and cur not in ("architecture-and-design","scenario-ready"): status="wrong-depth"
                    elif cert=="cpp" and cur in ("mention-only",): status="partial"
                    else: status="partial" if strength < 8 else "complete"
                required="architecture-and-design" if cert=="saa" else "fundamental"
                priority="P0" if status=="missing" and task_id in (["2.1","2.3","3.2"] if cert=="cpp" else ["1.1","1.2","1.3","2.1","2.2"]) else "P1" if status in ("missing","wrong-depth") else "P2" if status in ("partial","mention-only") else "P3"
                action="no-action" if status=="complete" else "expand-existing-lesson" if paths else "create-new-lesson"
                target=paths[0] if paths else f"{cat}/manual-review.md"
                common={"domain_id":domain,"domain_name":dname,"domain_weight":weight,"task_id":task_id,"task_title":title,
                    "requirement_id":f"{cert.upper()}-{task_id}-{idx:02d}","knowledge_or_skill":req,"requirement_type":typ,
                    "canonical_paths":"; ".join(paths),"evidence_headings":"; ".join(hs),"coverage_status":status,"current_depth":cur,
                    "required_depth":required,"priority":priority,"recommended_action":action,"target_path":target,
                    "notes":"Evidence chosen from lesson bodies, not names or badges; verify during implementation."}
                if cert=="cpp":
                    common.update({"missing_elements":"Full beginner explanation and exam-context reasoning" if status!="complete" else "none"})
                else:
                    common.update({"missing_architecture_elements":"Decision criteria, integration, failure behavior, and scenario application" if status!="complete" else "none",
                                   "missing_tradeoffs":"Cost, performance, security, resilience, and operational trade-offs" if status!="complete" else "none"})
                rows.append(common)
    return rows

def service_rows(inv):
    combined=sorted(set(CPP_SERVICES+SAA_SERVICES+CPP_OUT_SERVICES+SAA_OUT_SERVICES))
    rows=[]
    for s in combined:
        paths,_,strength=evidence(s)
        cpp=s in CPP_SERVICES; saa=s in SAA_SERVICES
        cpp_out=s in CPP_OUT_SERVICES; saa_out=s in SAA_OUT_SERVICES
        status="out-of-scope" if not cpp and not saa and (cpp_out or saa_out) else "missing" if not paths else "mention-only" if strength<4 else "partial"
        if paths and any(depth(TEXT[ROOT/p],"saa") in ("architecture-and-design","scenario-ready") for p in paths) and (not saa or any(depth(TEXT[ROOT/p],"cpp") in ("awareness","fundamental") for p in paths)): status="complete"
        critical={"Amazon EC2","Amazon S3","Amazon RDS","Amazon VPC","AWS IAM","AWS Lambda","Amazon DynamoDB","Elastic Load Balancing","EC2 Auto Scaling"}
        high={"Amazon EBS","Amazon EFS","Amazon Aurora","Amazon Route 53","Amazon CloudFront","Amazon SQS","Amazon SNS","AWS KMS","Amazon CloudWatch","AWS CloudTrail"}
        importance="out-of-scope" if status=="out-of-scope" else "critical-core" if s in critical else "high" if s in high else "important-supporting" if cpp and saa else "awareness"
        rec=("CPP;" if cpp else "")+("SAA" if saa else "")
        rows.append({"official_service_name":s,"official_category":"See official in-scope service list","cpp_listed":str(cpp).lower(),"saa_listed":str(saa).lower(),
            "cpp_expected_depth":"fundamental" if importance in ("critical-core","high") and cpp else "awareness" if cpp else "not-applicable",
            "saa_expected_depth":"architecture-and-design" if saa and importance in ("critical-core","high") else "awareness" if saa else "not-applicable",
            "canonical_location":paths[0] if paths else "missing","existing_files":"; ".join(paths),"coverage_status":status,
            "current_badges":"inspect inventory","recommended_badges":rec,"importance":importance,"terminology_status":"current official list wording",
            "action_required":"retain/label supplementary" if status=="out-of-scope" and paths else "none" if status in ("complete","out-of-scope") else "audit/expand or create at target",
            "target_path":paths[0] if paths else "manual-review","notes":f"CPP out-of-scope={str(cpp_out).lower()}; SAA out-of-scope={str(saa_out).lower()}. Official lists checked {CHECKED}; lists are non-exhaustive and subject to change."})
    return rows

BACKLOG = [
 ("P0","missing-topic","both","Cloud foundations","Shared responsibility","responsibility allocation","Shared Responsibility Model","01-cloud-fundamentals/README.md","01-cloud-fundamentals/01-shared-responsibility-model.md","create-new-lesson","fundamental","architecture-and-design","Overview; service-model responsibility shifts; EC2/RDS/Lambda scenarios","EC2; RDS; Lambda","none","CPP and SAA exam guides","M","Batch 1"),
 ("P0","missing-topic","CPP","Cloud Concepts","Task 1.1","cloud value proposition","Cloud benefits","01-cloud-fundamentals/README.md","01-cloud-fundamentals/02-cloud-concepts-and-benefits.md","create-new-lesson","fundamental","awareness","Benefits; economics; agility; elasticity; global reach; scenarios","AWS Cloud","none","CPP exam guide","M","Batch 1"),
 ("P0","partial-topic","both","Cloud Technology / Resilience","Global infrastructure","Regions and AZs","Global infrastructure fundamentals","02-global-infrastructure/README.md","02-global-infrastructure/01-regions-availability-zones-and-edge.md","create-new-lesson","fundamental","architecture-and-design","Regions; AZs; edge; service scope; HA; selection trade-offs","Regions; AZs; CloudFront","AWS-002","CPP and SAA exam guides","M","Batch 1"),
 ("P0","wrong-certification-depth","both","Security","Access management","IAM fundamentals and design","IAM","03-identity-governance-and-organizations/aws-iam/01-overview.md","03-identity-governance-and-organizations/aws-iam/01-overview.md","expand-existing-lesson","fundamental","architecture-and-design","Root; MFA; users/groups/roles; policies; federation; cross-account; least privilege","IAM; Identity Center; STS","none","CPP and SAA exam guides; IAM docs","L","Batch 1"),
 ("P0","missing-saa-architecture","both","Cloud Concepts / Resilience","Well-Architected","six pillars and design reasoning","Well-Architected foundations","13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md","13-architecture-and-design-patterns/aws-well-architected-framework/01-overview.md","expand-existing-lesson","fundamental","architecture-and-design","Six pillars; trade-offs; review process; scenarios","Well-Architected Tool","AWS-002","Exam guides; Well-Architected docs","M","Batch 1"),
 ("P1","outdated-terminology","both","Multiple","Terminology","current service and support names","Critical terminology corrections","manual-review","manual-review","correct-terminology","awareness","architecture-and-design","Apply terminology audit findings only after source verification","Amazon Quick; SageMaker AI; AWS Health","none","Official service pages","M","Batch 1"),
 ("P0","missing-topic","both","Compute","Compute selection","EC2 foundations and design","Amazon EC2","04-compute/amazon-ec2/01-overview.md","04-compute/amazon-ec2/01-overview.md","expand-existing-lesson","fundamental","scenario-ready","Families; sizing; lifecycle; storage/network; HA; security; cost; selection","EC2; EBS; ELB; Auto Scaling","AWS-003; AWS-004","EC2 docs; exam guides","L","Batch 2"),
 ("P1","missing-saa-architecture","SAA","Resilience/Performance","Elastic compute","load balancing selection","Elastic Load Balancing","04-compute/README.md","04-compute/elastic-load-balancing/01-overview.md","create-new-lesson","awareness","scenario-ready","ALB/NLB/GWLB; health; cross-zone; TLS; HA; cost","ELB; EC2; Auto Scaling","AWS-007","ELB docs","L","Batch 2"),
 ("P1","partial-topic","both","Compute","Elastic compute","scaling policies and metrics","EC2 Auto Scaling","04-compute/ec2-auto-scaling/01-target-tracking-scaling.md","04-compute/ec2-auto-scaling/01-target-tracking-scaling.md","expand-existing-lesson","fundamental","scenario-ready","Target tracking; step; scheduled; health; capacity; trade-offs","EC2; ELB; CloudWatch","AWS-008","Auto Scaling docs","L","Batch 2"),
 ("P1","wrong-certification-depth","both","Compute","Compute selection","serverless design","AWS Lambda","04-compute/aws-lambda/01-overview.md","04-compute/aws-lambda/01-overview.md","expand-existing-lesson","fundamental","scenario-ready","Invocation; scaling; limits concept; integrations; security; failure; cost","Lambda; API Gateway; SQS; EventBridge","none","Lambda docs","L","Batch 2"),
 ("P1","missing-topic","both","Compute","Containers","container service selection","Containers","04-compute/README.md","04-compute/containers/01-ecs-eks-and-fargate.md","create-new-lesson","awareness","architecture-and-design","ECS/EKS/Fargate; EC2 launch; selection; scaling; operations; cost","ECS; EKS; ECR; Fargate","none","Container service docs","L","Batch 2"),
 ("P0","wrong-certification-depth","both","Storage","Storage selection","object storage design","Amazon S3","05-storage/amazon-s3/01-overview.md","05-storage/amazon-s3/01-overview.md","expand-existing-lesson","fundamental","scenario-ready","Durability; availability; security; versioning; replication; events; performance; cost","S3; KMS; CloudFront","none","S3 docs","L","Batch 2"),
 ("P1","partial-topic","both","Storage","Storage selection","block storage performance","Amazon EBS","05-storage/amazon-ebs/01-overview.md","05-storage/amazon-ebs/01-overview.md","expand-existing-lesson","fundamental","architecture-and-design","Volume types; IOPS/throughput; snapshots; encryption; AZ scope; cost","EBS; EC2","AWS-007","EBS docs","M","Batch 2"),
 ("P2","partial-topic","both","Storage","Storage selection","ephemeral block storage","EC2 instance store","05-storage/ec2-instance-store/01-overview.md","05-storage/ec2-instance-store/01-overview.md","expand-existing-lesson","fundamental","architecture-and-design","Ephemeral behavior; performance; failure; suitable data; EBS comparison","EC2; EBS","AWS-007","EC2 storage docs","S","Batch 2"),
 ("P1","wrong-certification-depth","both","Storage","Storage selection","shared file storage","Amazon EFS","05-storage/amazon-efs/01-overview.md","05-storage/amazon-efs/01-overview.md","expand-existing-lesson","fundamental","architecture-and-design","Regional design; mount targets; performance; lifecycle; security; cost","EFS; EC2; Lambda","none","EFS docs","M","Batch 2"),
 ("P2","partial-topic","both","Storage","Storage selection","managed file systems","Amazon FSx","05-storage/amazon-fsx-for-lustre/01-overview.md","05-storage/amazon-fsx/01-family-and-selection.md","create-comparison-guide","awareness","architecture-and-design","FSx families; protocols; performance; HA; integration; selection","FSx; S3; EFS","none","FSx docs","M","Batch 2"),
 ("P2","partial-topic","both","Storage","Hybrid storage","gateway modes","AWS Storage Gateway","05-storage/aws-storage-gateway/01-overview.md","05-storage/aws-storage-gateway/01-overview.md","expand-existing-lesson","fundamental","architecture-and-design","File/Volume/Tape; cache; recovery; connectivity; selection; cost","Storage Gateway; S3; EBS","none","Storage Gateway docs","M","Batch 2"),
 ("P1","missing-topic","both","Storage/Resilience","Backup","centralized backup and restore","AWS Backup","05-storage/README.md","05-storage/aws-backup/01-overview.md","create-new-lesson","fundamental","architecture-and-design","Plans; vaults; policies; cross-account/Region; restore; cost","AWS Backup; Organizations; KMS","none","AWS Backup docs","M","Batch 2"),
 ("P2","missing-comparison","both","Compute/Storage","Selection","core selection trade-offs","Compute and storage comparisons","15-comparisons-and-decision-guides/README.md","15-comparisons-and-decision-guides/compute-and-storage/01-core-selection-guide.md","create-comparison-guide","fundamental","scenario-ready","EC2/Lambda/containers and S3/EBS/EFS/instance-store decision tables","Core compute and storage","AWS-007; AWS-009; AWS-010; AWS-012","Official service docs","L","Batch 2"),
 ("P0","missing-topic","both","Networking","Network design","VPC foundations","Amazon VPC","07-networking-and-content-delivery/amazon-vpc/README.md","07-networking-and-content-delivery/amazon-vpc/01-overview.md","create-new-lesson","fundamental","scenario-ready","CIDR; subnets; routes; IGW; NAT; controls; endpoints; HA; cost","VPC","AWS-003","VPC docs","L","Batch 3"),
 ("P1","partial-topic","SAA","Networking","Network design","subnets routes gateways","VPC routing","07-networking-and-content-delivery/amazon-vpc/README.md","07-networking-and-content-delivery/amazon-vpc/09-subnets-route-tables-and-internet-gateways.md","create-new-lesson","awareness","scenario-ready","Public/private; route evaluation; IGW; egress; AZ design","VPC; NAT Gateway","AWS-020","VPC docs","L","Batch 3"),
 ("P1","wrong-certification-depth","both","Networking","Network security","stateful and stateless controls","Security groups versus NACLs","07-networking-and-content-delivery/amazon-vpc/02-security-groups.md","15-comparisons-and-decision-guides/networking/03-security-groups-vs-network-acls.md","create-comparison-guide","fundamental","scenario-ready","State; rule evaluation; scopes; return traffic; scenarios","VPC","AWS-020","VPC security docs","M","Batch 3"),
 ("P1","partial-topic","SAA","Networking","Private connectivity","endpoint selection","VPC endpoints and PrivateLink","07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md","07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md","expand-existing-lesson","awareness","scenario-ready","Gateway/interface endpoints; endpoint services; DNS; security; cost","PrivateLink; S3; DynamoDB","AWS-020","PrivateLink docs","M","Batch 3"),
 ("P1","partial-topic","SAA","Networking","Hybrid/network topology","connectivity selection","Hybrid and multi-VPC connectivity","15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md","15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md","expand-existing-lesson","awareness","scenario-ready","Peering; TGW; VPN; DX; topology; routing; HA; cost","Transit Gateway; Direct Connect; VPN; peering","AWS-020","Networking docs","L","Batch 3"),
 ("P1","partial-topic","both","Networking","DNS and edge","routing and delivery decisions","Route 53 and CloudFront","07-networking-and-content-delivery/amazon-route-53/01-overview.md","15-comparisons-and-decision-guides/networking/04-dns-edge-and-global-routing.md","create-comparison-guide","fundamental","scenario-ready","DNS policies; health; CDN; Global Accelerator; selection; failure","Route 53; CloudFront; Global Accelerator","none","Official networking docs","L","Batch 3"),
 ("P0","missing-topic","both","Databases","Database selection","managed relational database","Amazon RDS","06-databases/README.md","06-databases/amazon-rds/01-overview.md","create-new-lesson","fundamental","scenario-ready","Engines; Multi-AZ; replicas; backups; security; scaling; cost","RDS","none","RDS docs","L","Batch 4"),
 ("P1","partial-topic","both","Databases","Database selection","Aurora architecture","Amazon Aurora","06-databases/amazon-aurora/01-overview.md","06-databases/amazon-aurora/01-overview.md","expand-existing-lesson","fundamental","scenario-ready","Cluster storage; replicas; failover; global/serverless; cost","Aurora; RDS","AWS-026","Aurora docs","L","Batch 4"),
 ("P0","missing-topic","both","Databases","Database selection","NoSQL design","Amazon DynamoDB","06-databases/README.md","06-databases/amazon-dynamodb/01-overview.md","create-new-lesson","fundamental","scenario-ready","Keys; capacity; indexes; consistency; global tables; streams; DAX; cost","DynamoDB","none","DynamoDB docs","L","Batch 4"),
 ("P1","wrong-certification-depth","both","Databases","Caching","cache selection and failure","Amazon ElastiCache","06-databases/amazon-elasticache/01-overview.md","06-databases/amazon-elasticache/01-overview.md","expand-existing-lesson","awareness","scenario-ready","Cache patterns; engines; HA; eviction; consistency; cost","ElastiCache; RDS; DynamoDB","none","ElastiCache docs","M","Batch 4"),
 ("P1","missing-comparison","SAA","Databases","Database selection","database decision trade-offs","Database selection guide","15-comparisons-and-decision-guides/README.md","15-comparisons-and-decision-guides/databases/01-database-selection-guide.md","create-comparison-guide","awareness","scenario-ready","RDS/Aurora/DynamoDB/ElastiCache; data model; scaling; HA; cost","Core databases","AWS-026; AWS-027; AWS-028; AWS-029","Database docs","L","Batch 4"),
 ("P1","partial-topic","both","Application Integration","Decoupling","queue and pub-sub selection","SQS and SNS","08-serverless-and-application-integration/amazon-sqs/01-overview.md","15-comparisons-and-decision-guides/application-integration/01-sqs-vs-sns-vs-eventbridge.md","create-comparison-guide","fundamental","scenario-ready","Queue/topic/event bus; delivery; ordering; retries; fanout; cost","SQS; SNS; EventBridge","none","Integration docs","L","Batch 5"),
 ("P1","missing-topic","both","Application Integration","Events","event routing","Amazon EventBridge","08-serverless-and-application-integration/README.md","08-serverless-and-application-integration/amazon-eventbridge/01-overview.md","create-new-lesson","awareness","scenario-ready","Buses; rules; targets; schemas; delivery; archive/replay; security","EventBridge","none","EventBridge docs","M","Batch 5"),
 ("P1","missing-topic","both","Application Integration","Workflows","orchestration","AWS Step Functions","08-serverless-and-application-integration/README.md","08-serverless-and-application-integration/aws-step-functions/01-overview.md","create-new-lesson","awareness","scenario-ready","Workflow types; states; retries; errors; integration; cost","Step Functions; Lambda","none","Step Functions docs","M","Batch 5"),
 ("P1","partial-topic","both","Serverless","API design","managed APIs","Amazon API Gateway","08-serverless-and-application-integration/amazon-api-gateway/01-overview.md","08-serverless-and-application-integration/amazon-api-gateway/01-overview.md","expand-existing-lesson","awareness","scenario-ready","API types; auth; integration; throttling; caching; HA; cost","API Gateway; Lambda; Cognito","AWS-010","API Gateway docs","M","Batch 5"),
 ("P0","missing-saa-architecture","SAA","Security","Data protection","encryption and key design","Data protection architecture","09-security-and-compliance/aws-kms/01-overview.md","13-architecture-and-design-patterns/security/01-data-protection-patterns.md","create-architecture-pattern","awareness","scenario-ready","KMS; TLS; ACM; secrets; rotation; envelope encryption; scenarios","KMS; ACM; Secrets Manager","AWS-004","Security docs","L","Batch 6"),
 ("P1","partial-topic","both","Security","Threat detection","security service selection","Security services","09-security-and-compliance/README.md","15-comparisons-and-decision-guides/security/01-security-service-selection.md","create-comparison-guide","awareness","architecture-and-design","GuardDuty/Inspector/Macie/Security Hub/Detective/Config; scopes; response","Security services","none","Security docs","L","Batch 6"),
 ("P1","missing-comparison","both","Operations","Monitoring and audit","observability service selection","CloudWatch CloudTrail Config","10-monitoring-management-and-deployment/README.md","15-comparisons-and-decision-guides/operations/01-cloudwatch-vs-cloudtrail-vs-config.md","create-comparison-guide","fundamental","scenario-ready","Metrics/logs/traces/API history/config; alarms; compliance; scenarios","CloudWatch; CloudTrail; Config; X-Ray","none","Operations docs","L","Batch 6"),
 ("P1","partial-topic","SAA","Security","Governance","multi-account guardrails","Organizations and Control Tower","03-identity-governance-and-organizations/aws-organizations/01-overview.md","13-architecture-and-design-patterns/security/02-multi-account-governance.md","create-architecture-pattern","awareness","scenario-ready","OUs; SCPs; account factory; identity; logs; guardrails; trade-offs","Organizations; Control Tower; Identity Center","AWS-004","Governance docs","L","Batch 6"),
 ("P2","partial-topic","both","Operations","Management","operations management selection","AWS Systems Manager","10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md","10-monitoring-management-and-deployment/aws-systems-manager/01-overview.md","expand-existing-lesson","awareness","architecture-and-design","Inventory; patch; automation; parameters; session; hybrid; security","Systems Manager","none","Systems Manager docs","M","Batch 6"),
 ("P1","missing-saa-architecture","SAA","Resilience","High availability","multi-tier HA design","Highly available web application","13-architecture-and-design-patterns/README.md","13-architecture-and-design-patterns/01-highly-available-web-applications.md","create-architecture-pattern","awareness","scenario-ready","Multi-AZ tiers; ELB/ASG; data failover; DNS; observability; trade-offs","EC2; ELB; RDS; Route 53","Batches 2-4","Architecture docs","L","Batch 7"),
 ("P0","missing-topic","SAA","Resilience","Disaster recovery","DR strategies and selection","Disaster recovery","13-architecture-and-design-patterns/README.md","13-architecture-and-design-patterns/02-disaster-recovery-strategies.md","create-architecture-pattern","awareness","scenario-ready","Backup/restore; pilot light; warm standby; active-active; RTO/RPO; cost","Backup; Route 53; S3; databases","AWS-018","DR guidance","L","Batch 7"),
 ("P1","missing-saa-architecture","SAA","Resilience","Event-driven","decoupled failure handling","Event-driven resilience","13-architecture-and-design-patterns/README.md","13-architecture-and-design-patterns/03-event-driven-and-decoupled-systems.md","create-architecture-pattern","awareness","scenario-ready","Queues; retries; DLQs; idempotency; orchestration/choreography; observability","SQS; SNS; EventBridge; Step Functions","Batch 5","Architecture docs","L","Batch 7"),
 ("P1","missing-saa-architecture","SAA","Resilience","Serverless","serverless application design","Serverless architecture","13-architecture-and-design-patterns/README.md","13-architecture-and-design-patterns/04-serverless-application-patterns.md","create-architecture-pattern","awareness","scenario-ready","API; compute; data; events; security; failure; scaling; cost","API Gateway; Lambda; DynamoDB","Batch 5","Serverless docs","L","Batch 7"),
 ("P1","partial-topic","CPP","Billing","Pricing models","purchase options","AWS pricing fundamentals","12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md","12-billing-pricing-and-support/aws-billing-and-cost-management/02-study-guide.md","expand-existing-lesson","fundamental","architecture-and-design","On-Demand; RI; Savings Plans; Spot; storage; transfer; scenarios","Billing; EC2; Savings Plans","none","Pricing pages","L","Batch 8"),
 ("P1","fact-review-required","CPP","Support","Support resources","current support plans and features","AWS Support","12-billing-pricing-and-support/aws-support/02-support-plans.md","12-billing-pricing-and-support/aws-support/02-support-plans.md","correct-fact","fundamental","awareness","Plan names; features; response-time source links; account assistance","Support; Trusted Advisor; Health","AWS-006","Official Support pages","M","Batch 8"),
 ("P2","partial-topic","both","Cost optimization","Cost tools","tool selection","Cost management tools","12-billing-pricing-and-support/README.md","15-comparisons-and-decision-guides/cost/01-cost-management-tool-selection.md","create-comparison-guide","fundamental","architecture-and-design","Budgets/Explorer/CUR/Calculator/tags; proactive/reactive; scenarios","Cost tools","none","Billing docs","M","Batch 8"),
 ("P2","fact-review-required","both","Pricing","Data transfer","current cost principles","Data transfer costs","12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md","12-billing-pricing-and-support/aws-billing-and-cost-management/03-data-transfer-costs.md","correct-fact","fundamental","architecture-and-design","Cost directions; AZ/Region/edge/NAT; checked date; no stale exact prices","Networking; billing","none","Current pricing pages","M","Batch 8"),
 ("P2","missing-topic","both","Analytics","Data ingestion","streaming service selection","Analytics ingestion","14-ai-ml-analytics-and-other-services/analytics/README.md","14-ai-ml-analytics-and-other-services/analytics/01-kinesis-and-data-firehose.md","create-new-lesson","awareness","architecture-and-design","Streams/Firehose; batch vs stream; destinations; scaling; cost","Kinesis; Data Firehose; S3; Redshift","none","Analytics docs","M","Batch 9"),
 ("P2","partial-topic","both","Analytics","Analytics selection","analytics decision guide","Analytics services","14-ai-ml-analytics-and-other-services/analytics/README.md","15-comparisons-and-decision-guides/analytics/02-analytics-service-selection.md","create-comparison-guide","awareness","architecture-and-design","Athena/EMR/Glue/Redshift/OpenSearch/Quick; use cases; trade-offs","Analytics services","AWS-047","Analytics docs","L","Batch 9"),
 ("P3","missing-topic","CPP","AI/ML","Service recognition","AI/ML recognition summary","AI and ML services","14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/README.md","14-ai-ml-analytics-and-other-services/artificial-intelligence-and-machine-learning/01-service-recognition-guide.md","create-cpp-summary","awareness","awareness","Purpose and recognition; no implementation depth; current names","AI/ML services","AWS-006","AI service docs","M","Batch 9"),
 ("P1","missing-scenario","CPP","All","Exam scenarios","CPP scenario reasoning","CPP exam preparation","16-exam-preparation/README.md","16-exam-preparation/01-cpp-scenario-reasoning.md","create-cpp-summary","fundamental","not-applicable","Domain-linked scenarios; distractor reasoning; no leaked questions","Cross-domain","Batches 1-9","Exam guide","L","Batch 10"),
 ("P1","missing-scenario","SAA","All","Architecture scenarios","SAA scenario reasoning","SAA exam preparation","16-exam-preparation/README.md","16-exam-preparation/02-saa-architecture-scenario-reasoning.md","create-saa-scenarios","awareness","scenario-ready","Requirements; constraints; eliminate options; trade-offs; domain links","Cross-domain","Batches 1-9","Exam guide","L","Batch 10"),
 ("P2","incorrect-badge","both","All","Scope labeling","badge corrections from audit","Certification badges","docs/certification-audit/BADGE-ACCURACY-AUDIT.csv","manual-review","correct-badges","fundamental","architecture-and-design","Apply only evidence-supported badge changes and preserve depth distinctions","All audited lessons","Batches 1-9","Exam guides and scope lists","M","Batch 10"),
 ("P2","broken-navigation","both","All","Navigation","indexes after implementation","Repository navigation","README.md","manual-review","improve-navigation","fundamental","architecture-and-design","Update category READMEs, service index, repository map, and validate links","All","Batches 1-10","Repository policies","M","Batch 10"),
]

def make_backlog():
    rows=[]
    for i,item in enumerate(BACKLOG,1):
        pr,gap,cert,dom,task,req,topic,current,target,action,cppd,saad,sections,related,deps,sources,effort,batch=item
        rows.append({"backlog_id":f"AWS-{i:03d}","priority":pr,"gap_type":gap,"certification":cert,"official_domain":dom,"official_task":task,
          "official_requirement":req,"topic":topic,"current_paths":current,"target_path":target,"recommended_action":action,
          "required_cpp_depth":cppd,"required_saa_depth":saad,"required_sections":sections,"related_services":related,
          "dependencies":deps,"official_sources_required":sources,"estimated_effort":effort,"batch":batch,
          "acceptance_criteria":f"Target provides {sections.lower()}; cites current official AWS sources; matches {cppd} CPP and {saad} SAA depth where applicable; filename and links validate.",
          "status":"not-started","notes":
          ("Manual review is required because this is a cross-repository correction whose exact lesson targets must be selected from the corresponding audit before edits begin; Phase 5 performs no implementation."
           if target == "manual-review" else "Phase 5 planning only; no lesson implementation performed.")})
    return rows

def md_table(headers, rows):
    esc=lambda x:str(x).replace("|","\\|").replace("\n"," ")
    return "| "+" | ".join(headers)+" |\n|"+"|".join(["---"]*len(headers))+"|\n"+"\n".join("| "+" | ".join(esc(x) for x in r)+" |" for r in rows)+"\n"

def baseline(cert,tasks,domains,services,out_services,guide,scope,out_scope):
    name="AWS Certified Cloud Practitioner" if cert=="CPP" else "AWS Certified Solutions Architect - Associate"
    code="CLF-C02" if cert=="CPP" else "SAA-C03"
    out=[f"# {cert} Official Baseline", "", f"- Certification: **{name}**", f"- Current exam code verified: **{code}**", f"- Checked: **{CHECKED}**", f"- [Official exam guide]({guide})", f"- [Official in-scope services]({scope})", "", "AWS states that its service and feature lists are non-exhaustive and subject to change. This baseline maps the published guide as checked; it does not guarantee future exam coverage.", "", "## Candidate and Required Depth", ""]
    out.append("The target learner needs broad cloud literacy, service recognition, basic security, pricing, and support reasoning." if cert=="CPP" else "The target learner needs at least one year of hands-on design experience. Coverage requires architecture decisions, integrations, security, resilience, performance, scalability, cost optimization, and explicit trade-offs; a definition alone is insufficient.")
    out += ["", "## Domains", "", md_table(["Domain","Name","Weight"],[(d,n,w) for d,(n,w) in domains.items()]), "## Tasks, Knowledge, and Skills", ""]
    for tid,title,cat,knowledge,skills in tasks:
        out += [f"### Task {tid}: {title}", "", f"Expected repository category: `{cat}/`", "", "Knowledge statements (paraphrased):", ""] + [f"- {x}" for x in knowledge] + ["", "Skill statements (paraphrased):", ""] + [f"- {x}" for x in skills] + [""]
    out += ["## Technologies and Concepts", "", ", ".join(c for c,_,_ in CONCEPTS), "", "## Listed In-Scope Services", "", ", ".join(services), "", "## Listed Out-of-Scope Services", ""]
    out += [f"[Official out-of-scope list]({out_scope}): " + ", ".join(out_services), "", "Out-of-scope lists are also non-exhaustive. Existing notes on these services are retained as supplementary or historical material rather than deleted.", ""]
    out += ["## Source and Copyright Note", "", "Statements above are concise paraphrases for mapping; consult the linked AWS guide for authoritative wording. No completeness beyond the checked guide version is claimed.",""]
    return "\n".join(out)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    inv=inventory(); cpp=requirement_rows(CPP_TASKS,CPP_DOMAINS,"cpp"); saa=requirement_rows(SAA_TASKS,SAA_DOMAINS,"saa"); services=service_rows(inv); backlog=make_backlog()
    inv_fields="canonical_path,title,main_category,services_mentioned,concepts_covered,current_cpp_badge,current_saa_badge,actual_cpp_depth,actual_saa_depth,architecture_scenarios,comparisons,pricing_content,security_content,resilience_content,official_references,last_verified,content_quality,terminology_status,fact_review_required,navigation_status,notes".split(',')
    write_csv("CANONICAL-CONTENT-INVENTORY.csv",inv_fields,inv)
    cpp_fields="domain_id,domain_name,domain_weight,task_id,task_title,requirement_id,knowledge_or_skill,requirement_type,canonical_paths,evidence_headings,coverage_status,current_depth,required_depth,missing_elements,priority,recommended_action,target_path,notes".split(',')
    saa_fields="domain_id,domain_name,domain_weight,task_id,task_title,requirement_id,knowledge_or_skill,requirement_type,canonical_paths,evidence_headings,coverage_status,current_depth,required_depth,missing_architecture_elements,missing_tradeoffs,priority,recommended_action,target_path,notes".split(',')
    write_csv("CPP-TASK-STATEMENT-MAP.csv",cpp_fields,cpp); write_csv("SAA-TASK-MAP.csv",saa_fields,saa)
    svc_fields="official_service_name,official_category,cpp_listed,saa_listed,cpp_expected_depth,saa_expected_depth,canonical_location,existing_files,coverage_status,current_badges,recommended_badges,importance,terminology_status,action_required,target_path,notes".split(',')
    write_csv("SERVICE-SCOPE-MATRIX.csv",svc_fields,services)
    concept_rows=[]
    for c,cr,sr in CONCEPTS:
        paths,_,strength=evidence(c); status="missing" if not paths else "mention-only" if strength<4 else "partial" if strength<8 else "complete"
        concept_rows.append({"concept":c,"cpp_relevance":cr,"saa_relevance":sr,"official_source_section":"Technologies/concepts and task statements","canonical_paths":"; ".join(paths),"coverage_status":status,"cpp_depth":depth(TEXT[ROOT/paths[0]],"cpp") if paths else "none","saa_depth":depth(TEXT[ROOT/paths[0]],"saa") if paths else "none","missing_elements":"Correct-depth explanation and scenarios" if status!="complete" else "none","priority":"P1" if status=="missing" else "P2" if status!="complete" else "P3","recommended_action":"create-new-lesson" if not paths else "expand-existing-lesson","target_path":paths[0] if paths else "manual-review","notes":"Paraphrased official concept mapping."})
    write_csv("TECHNOLOGIES-AND-CONCEPTS-MATRIX.csv","concept,cpp_relevance,saa_relevance,official_source_section,canonical_paths,coverage_status,cpp_depth,saa_depth,missing_elements,priority,recommended_action,target_path,notes".split(','),concept_rows)
    badge=[]
    for r in inv:
        rec_cpp=r["actual_cpp_depth"] in ("awareness","fundamental","intermediate") and r["main_category"]!="16-exam-preparation"
        rec_saa=r["actual_saa_depth"] in ("architecture-and-design","scenario-ready")
        action="none" if (str(rec_cpp).lower()==r["current_cpp_badge"] and str(rec_saa).lower()==r["current_saa_badge"]) else "correct-badges-after-manual-scope-review"
        badge.append({"canonical_path":r["canonical_path"],"current_cpp_badge":r["current_cpp_badge"],"current_saa_badge":r["current_saa_badge"],"recommended_cpp_badge":str(rec_cpp).lower(),"recommended_saa_badge":str(rec_saa).lower(),"evidence":f"Body depth: CPP {r['actual_cpp_depth']}; SAA {r['actual_saa_depth']}","confidence":"medium" if action!="none" else "high","action_required":action,"notes":"Depth recommendation is not an official-scope decision; confirm against service matrix before editing."})
    write_csv("BADGE-ACCURACY-AUDIT.csv","canonical_path,current_cpp_badge,current_saa_badge,recommended_cpp_badge,recommended_saa_badge,evidence,confidence,action_required,notes".split(','),badge)
    outscope=[]
    for r in inv:
        rel=r['canonical_path']; topic=r['title']; in_scope=any(norm(s) in norm(r['services_mentioned']) for s in set(CPP_SERVICES+SAA_SERVICES))
        role="core-certification-content" if in_scope else "supplementary-reference" if not rel.startswith("16-") else "important-supporting-content"
        outscope.append({"canonical_path":rel,"topic":topic,"cpp_scope":"mapped-or-supporting" if in_scope else "not-explicitly-mapped","saa_scope":"mapped-or-supporting" if in_scope else "not-explicitly-mapped","current_depth":f"CPP {r['actual_cpp_depth']}; SAA {r['actual_saa_depth']}","recommended_role":role,"recommended_action":"retain; review scope labeling","reason":"Official lists are non-exhaustive; absence is not a deletion rationale.","notes":"Category README files are navigation artifacts."})
    write_csv("OUT-OF-SCOPE-AND-SUPPLEMENTARY-AUDIT.csv","canonical_path,topic,cpp_scope,saa_scope,current_depth,recommended_role,recommended_action,reason,notes".split(','),outscope)
    back_fields="backlog_id,priority,gap_type,certification,official_domain,official_task,official_requirement,topic,current_paths,target_path,recommended_action,required_cpp_depth,required_saa_depth,required_sections,related_services,dependencies,official_sources_required,estimated_effort,batch,acceptance_criteria,status,notes".split(',')
    write_csv("PHASE-6-CONTENT-BACKLOG.csv",back_fields,backlog)

    (OUT/"CPP-OFFICIAL-BASELINE.md").write_text(baseline("CPP",CPP_TASKS,CPP_DOMAINS,CPP_SERVICES,CPP_OUT_SERVICES,CPP_GUIDE,CPP_SCOPE,CPP_OUT),encoding="utf-8")
    (OUT/"SAA-OFFICIAL-BASELINE.md").write_text(baseline("SAA",SAA_TASKS,SAA_DOMAINS,SAA_SERVICES,SAA_OUT_SERVICES,SAA_GUIDE,SAA_SCOPE,SAA_OUT),encoding="utf-8")

    topics=["Cloud concepts","Shared Responsibility Model","AWS global infrastructure","IAM","AWS Organizations","Amazon EC2","EC2 purchasing options","Elastic Load Balancing","EC2 Auto Scaling","AWS Lambda","Containers","Amazon S3","Amazon EBS","EC2 instance store","Amazon EFS","Amazon FSx","AWS Backup","Amazon RDS","Amazon Aurora","Amazon DynamoDB","Amazon ElastiCache","Amazon VPC","Subnets","Route tables","Internet gateways","NAT gateways","Security groups","Network ACLs","VPC endpoints","AWS PrivateLink","VPC peering","AWS Transit Gateway","AWS Direct Connect","AWS VPN","Amazon Route 53","Amazon CloudFront","Amazon API Gateway","Amazon SQS","Amazon SNS","Amazon EventBridge","AWS Step Functions","AWS KMS","AWS Secrets Manager","Amazon CloudWatch","AWS CloudTrail","AWS Config","AWS Systems Manager","AWS CloudFormation","Migration services","Disaster recovery","AWS Well-Architected Framework","Billing","Pricing","AWS Support"]
    drows=[]
    for t in topics:
        paths,_,_=evidence(t); cd=depth(TEXT[ROOT/paths[0]],"cpp") if paths else "none"; sd=depth(TEXT[ROOT/paths[0]],"saa") if paths else "none"
        drows.append((t,cd,"fundamental",sd,"architecture-and-design","Missing correct-depth decisions/scenarios" if sd not in ("architecture-and-design","scenario-ready") else "Verify task-level completeness","Expand existing or create mapped backlog lesson"))
    (OUT/"CPP-SAA-DEPTH-MATRIX.md").write_text("# CPP and SAA Depth Matrix\n\nDepth is based on lesson bodies. A service mention does not count as coverage.\n\n"+md_table(["Topic","Existing CPP depth","Required CPP depth","Existing SAA depth","Required SAA depth","Main gap","Action"],drows),encoding="utf-8")

    status_counts=lambda rows:Counter(r['coverage_status'] for r in rows)
    def dashboard(cert,rows,domains):
        lines=[f"# {cert.upper()} Coverage Dashboard","",f"Audit date: **{CHECKED}**. Scores are evidence metrics, not guaranteed exam-readiness scores.","", "Scoring: complete 1.0, partial 0.5, mention-only 0.1, wrong-depth 0.25, missing 0.0; outdated is capped at 0.25.",""]
        table=[]
        scorevals={"complete":1,"partial":.5,"mention-only":.1,"wrong-depth":.25,"missing":0,"outdated":.25}
        for d,(name,w) in domains.items():
            rr=[r for r in rows if r['domain_id']==d]; c=Counter(r['coverage_status'] for r in rr); score=sum(scorevals.get(r['coverage_status'],0) for r in rr)/len(rr)*100
            table.append((name,w,c['complete'],c['partial']+c['mention-only']+c['wrong-depth'],c['missing'],f"{score:.1f}%"))
        lines += [md_table(["Domain","Weight","Complete","Partial","Missing","Evidence-based score" if cert=="cpp" else "Architecture-depth score"],table)]
        sc=status_counts(rows); taskstate={}
        for tid in sorted(set(r['task_id'] for r in rows)):
            vals=[r['coverage_status'] for r in rows if r['task_id']==tid]
            taskstate[tid]="missing" if all(x=="missing" for x in vals) else "complete" if all(x=="complete" for x in vals) else "partial"
        depths=Counter(r['actual_cpp_depth' if cert=="cpp" else 'actual_saa_depth'] for r in inv)
        p0=sum(r['priority']=="P0" and r['certification'] in (cert.upper(),"both") for r in backlog); p1=sum(r['priority']=="P1" and r['certification'] in (cert.upper(),"both") for r in backlog)
        lines += ["## Supporting Metrics","",f"- Complete tasks: {sum(x=='complete' for x in taskstate.values())}",f"- Partial tasks: {sum(x=='partial' for x in taskstate.values())}",f"- Missing tasks: {sum(x=='missing' for x in taskstate.values())}",f"- Complete requirements: {sc['complete']}",f"- Partial/mention/wrong-depth requirements: {sc['partial']+sc['mention-only']+sc['wrong-depth']}",f"- Missing requirements: {sc['missing']}",f"- {'Beginner-ready' if cert=='cpp' else 'Scenario-ready'} files: {depths['fundamental'] if cert=='cpp' else depths['scenario-ready']}",f"- {'Files below fundamental depth' if cert=='cpp' else 'Definition-only/awareness files'}: {depths['awareness']+depths['mention-only']}",f"- Listed-service representation: {sum(s['coverage_status']!='missing' and s[f'{cert}_listed']=='true' for s in services)}/{sum(s[f'{cert}_listed']=='true' for s in services)}",f"- P0 backlog gaps: {p0}",f"- P1 backlog gaps: {p1}","", "Separate quality dimensions: task coverage above; beginner/architecture depth from inventory; service representation from scope matrix; terminology and navigation in their dedicated audits.",""]
        return "\n".join(lines)
    (OUT/"CPP-COVERAGE-DASHBOARD.md").write_text(dashboard("cpp",cpp,CPP_DOMAINS),encoding="utf-8")
    (OUT/"SAA-COVERAGE-DASHBOARD.md").write_text(dashboard("saa",saa,SAA_DOMAINS),encoding="utf-8")

    (OUT/"TERMINOLOGY-AUDIT.md").write_text(f"""# Terminology Audit

Checked: **{CHECKED}**. No lesson was edited.

| Repository wording | Current official wording | Affected paths | Severity | Recommended correction | Official source |
|---|---|---|---|---|---|
| Amazon QuickSight | Amazon Quick (official SAA list wording) | `14-ai-ml-analytics-and-other-services/analytics/amazon-quicksight/01-overview.md` and references | medium; official materials are in transition | Confirm product-page branding before changing canonical title | [SAA scope]({SAA_SCOPE}) |
| Amazon SageMaker / older Studio wording | Amazon SageMaker AI in current exam scope | Files found through service matrix/manual review | medium | Use current service name while explaining older source terminology | [SAA scope]({SAA_SCOPE}) |
| AWS Personal Health Dashboard | AWS Health Dashboard | `12-billing-pricing-and-support/aws-health-dashboard/01-overview.md` and archived provenance | high | Correct active prose after verifying current AWS Health docs | [CPP guide]({CPP_GUIDE}) |
| AWS Single Sign-On | AWS IAM Identity Center | IAM/Organizations lessons if phrase appears | high | Replace active branding, preserving historical context where needed | [SAA guide]({SAA_GUIDE}) |
| Amazon Elastic Transcoder | Retired service; official SAA guide still lists it in one guide surface | `90-archive/obsolete-services/amazon-elastic-transcoder.md` | low/archive | Retain as historical archive and flag official-list inconsistency | [SAA scope]({SAA_SCOPE}) |
| AWS CodeCommit | No longer available to new customers; scope relevance requires review | `10-monitoring-management-and-deployment/aws-codecommit/01-overview.md` | medium | Keep supplementary until official scope and service status are reconciled | [CPP scope]({CPP_SCOPE}) |

Capitalization and acronym variants are listed per file in the canonical inventory. These findings require source-by-source confirmation before mechanical replacement.
""",encoding="utf-8")
    (OUT/"PRICING-AND-SUPPORT-FRESHNESS-AUDIT.md").write_text(f"""# Pricing and Support Freshness Audit

Checked: **{CHECKED}**. Exact prices, discounts, quotas, plan features, and response times are volatile and must be rechecked at implementation.

| Area | Classification | Finding | Action |
|---|---|---|---|
| AWS Support plan names and features | requires-live-verification | Existing support lessons contain plan comparisons that need line-by-line comparison to the current official Support pages. | Batch 8 factual review; cite checked date. |
| Response times and TAM claims | conceptually-correct-but-date-sensitive | Numeric response commitments and account-team descriptions can change. | Retain concepts only after live verification. |
| Trusted Advisor access | conceptually-correct-but-date-sensitive | Access varies by check and support entitlement. | Avoid blanket all-or-nothing claims. |
| AWS Health terminology | outdated | Older Personal Health Dashboard terminology remains in provenance and may appear in prose. | Use AWS Health Dashboard in active notes. |
| AWS Free Tier | requires-live-verification | Offers and eligibility change. | Cite current Free Tier page and checked date. |
| EC2 On-Demand, Spot, Reserved Instances, Savings Plans | partial-topic | Core models are represented, but comparison depth and current caveats are uneven. | Consolidate decision guidance in Batch 8. |
| Data-transfer and NAT costs | requires-live-verification | Exact charges vary by Region, direction, and architecture. | Teach cost drivers; cite current pricing pages. |
| Exact discounts and free usage | unsupported | Any unreferenced percentage or quantity must not be treated as current. | Verify or remove during Phase 6. |

Primary scope anchors: [CPP guide]({CPP_GUIDE}) and [SAA guide]({SAA_GUIDE}). Pricing pages must be consulted for each implementation item.
""",encoding="utf-8")

    cpp_quality=[]
    for name,cat in [("Cloud benefits","01-"),("Shared responsibility","01-"),("Global infrastructure","02-"),("IAM","03-"),("Compute","04-"),("Storage","05-"),("Databases","06-"),("Networking","07-"),("Security and compliance","09-"),("Billing and support","12-")]:
        rr=[r for r in inv if r['main_category'].startswith(cat)]; ready=sum(r['actual_cpp_depth']=='fundamental' for r in rr); rating="beginner-ready" if ready>=max(1,len(rr)//3) else "adequate" if any(r['actual_cpp_depth']=='awareness' for r in rr) else "too-shallow" if rr else "missing"
        cpp_quality.append((name,rating,f"{ready}/{len(rr)} files score fundamental", "Add definitions, business purpose, benefits, use cases, pricing/responsibility, comparisons, and basic scenarios where mapped."))
    (OUT/"CPP-FUNDAMENTALS-QUALITY-AUDIT.md").write_text("# CPP Fundamentals Quality Audit\n\nA beginner-ready rating requires meaningful body content, not badges.\n\n"+md_table(["Area","Rating","Evidence","Required action"],cpp_quality),encoding="utf-8")
    arch_areas=["Highly available web applications","Multi-tier architectures","Serverless applications","Event-driven systems","Container architectures","Relational databases","NoSQL databases","Caching","Hybrid connectivity","Multi-account access","Secure data storage","Backup","Disaster recovery","Migration","Data ingestion","Cost-optimized compute","Cost-optimized storage","Cost-optimized databases","Cost-optimized networking"]
    arows=[]
    for a in arch_areas:
        paths,_,strength=evidence(a); state="missing" if not paths else "definition-only" if depth(TEXT[ROOT/paths[0]],"saa") in ("mention-only","awareness") else "partial" if strength<8 else "adequate"
        arows.append((a,state,"; ".join(paths) or "none","Needs explicit requirements, service selection, integration, failure modes, operations, and cost/performance/security/resilience trade-offs."))
    (OUT/"SAA-ARCHITECTURE-QUALITY-AUDIT.md").write_text("# SAA Architecture Quality Audit\n\nA definition is not SAA coverage. `scenario-ready` requires choosing among valid designs under constraints.\n\n"+md_table(["Architecture area","Status","Evidence","Missing decisions and trade-offs"],arows),encoding="utf-8")

    tiny=[r for r in inv if int(re.search(r"(\d+) words",r['notes']).group(1))<120]; noindex=[r for r in inv if r['navigation_status']=='missing-local-index'];
    (OUT/"STRUCTURE-QUALITY-AUDIT.md").write_text(f"""# Structure Quality Audit

No restructuring occurred. The audit inspected {len(inv)} canonical Markdown files.

| Finding | Count | Evidence | Backlog treatment |
|---|---:|---|---|
| Tiny or too-shallow files | {len(tiny)} | Canonical inventory `content_quality` and word counts | Merge or expand only when educationally justified. |
| Files without a local service/category index | {len(noindex)} | Canonical inventory `navigation_status` | Improve navigation in Batch 10. |
| Over-fragmented service folders | manual review | IAM, EC2, Storage Gateway, and billing contain multiple small feature files | Preserve facts; merge only under a separate migration log. |
| Duplicate canonical owners | no exact duplicates detected by path scan | Phase 4 owner maps and current tree | Validate with repository duplicate script. |
| Comparison overlap | 10 comparison lessons | `15-comparisons-and-decision-guides/` | Keep decision-focused; avoid repeating service definitions. |
| Category README accuracy | partial | README counts/navigation require refresh after Phase 6 | Batch 10 navigation item. |
| Misleading/legacy terminology | several manual-review findings | Terminology audit | Batch 1/8 corrections. |
| Empty directories and numbering inconsistencies | validation required | Existing validation scripts | Do not restructure in Phase 5. |

Phase 4 reports remain provenance. Any future move, merge, rename, or archive must use `git mv` and update the migration log.
""",encoding="utf-8")
    claims=[]
    claim_re=re.compile(r"100% coverage|all services covered|no topics missing|85/85|108/108|complete and accurate|exam guaranteed",re.I)
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in (".md",".csv",".txt") and ".git" not in p.parts and OUT not in p.parents:
            try: body=p.read_text(encoding="utf-8",errors="replace")
            except OSError: continue
            for m in claim_re.finditer(body): claims.append((p.relative_to(ROOT).as_posix(),m.group(0),"Phase 5 task/requirement maps show partial and missing correct-depth coverage.","Historical or structural completeness only; not current exam completeness.","Mark superseded; do not delete provenance."))
    claim_md="# Previous Coverage Claims Review\n\nPhase 5 supersedes older certification-completeness claims while preserving their records.\n\n"+md_table(["Path","Exact claim","Evidence","Correct interpretation","Future action"],claims if claims else [("none found","none","Search completed","No matching explicit claim","No action")])
    (OUT/"PREVIOUS-COVERAGE-CLAIMS-REVIEW.md").write_text(claim_md,encoding="utf-8")

    batch_lines=["# Phase 6 Batch Plan","","Authority: `PHASE-6-CONTENT-BACKLOG.csv`. Only rows with the selected batch may be implemented. Dependencies must be satisfied first.",""]
    for b in range(1,11):
        label=f"Batch {b}"; items=[r for r in backlog if r['batch']==label]; purpose=["Critical foundations and factual corrections","Core compute and storage","Core networking and content delivery","Databases and caching","Serverless and application integration","Security, monitoring, and governance","Resilience and architecture patterns","Billing, pricing, and support","Analytics, AI/ML, and awareness services","Comparisons and exam preparation"][b-1]
        batch_lines += [f"## {label}: {purpose}","",f"- Purpose: {purpose}.",f"- Included backlog IDs: {', '.join(r['backlog_id'] for r in items)}",f"- Certification focus: {', '.join(sorted(set(r['certification'] for r in items)))}",f"- Official domains addressed: {', '.join(sorted(set(r['official_domain'] for r in items)))}",f"- Target categories: {', '.join(sorted(set(r['target_path'].split('/')[0] for r in items)))}","- Exact target files:",""]+[f"  - `{r['target_path']}` ({r['backlog_id']})" for r in items]+["",f"- Dependencies: {', '.join(sorted(set(r['dependencies'] for r in items)))}","- Excluded topics: work assigned to every other batch; no opportunistic lesson rewrites.","- Validation requirements: official-source verification, required depth and sections, badge/scope review, filename validation, link validation, and no unassigned changes.","- Definition of done: every included acceptance criterion passes; maps and dashboards are updated; no unrelated content changes.",f"- Expected next batch: {'Batch '+str(b+1) if b<10 else 'Phase 6 re-audit and closure review'}.",""]
    (OUT/"PHASE-6-BATCH-PLAN.md").write_text("\n".join(batch_lines),encoding="utf-8")

    cpc=status_counts(cpp); sac=status_counts(saa); bc=Counter(r['batch'] for r in backlog)
    readme=f"""# Certification Audit

Phase 5 compares canonical lesson bodies with the official CLF-C02 and SAA-C03 guides checked **{CHECKED}**. Domain/task coverage and service representation are separate measures: listing a service is not proof that a task is taught. CPP needs beginner-friendly fundamentals; SAA needs architecture decisions and trade-offs.

Primary sources: [CPP guide]({CPP_GUIDE}), [CPP technologies]({CPP_TECH}), [CPP scope]({CPP_SCOPE}), [CPP out-of-scope list]({CPP_OUT}), [SAA guide]({SAA_GUIDE}), [SAA scope]({SAA_SCOPE}), and [SAA out-of-scope list]({SAA_OUT}). Official service lists are non-exhaustive and subject to change.

Statuses: complete, partial, mention-only, wrong-depth, missing, misplaced, outdated, over-scoped, duplicate-or-overlapping, fact-review-required, and not-applicable. Priorities run P0 blocking through P4 supplementary/archive.

## Artifact Guide

- Baselines record official tasks, requirements, concepts, and scope.
- Inventory records every canonical Markdown file exactly once.
- Task maps connect each paraphrased knowledge/skill statement to body evidence.
- Service/concept/depth/badge matrices separate representation from correct depth.
- Quality audits cover terminology, pricing, fundamentals, architecture, structure, scope, and prior claims.
- Dashboards report separate evidence measures, never a guaranteed readiness score.
- `PHASE-6-CONTENT-BACKLOG.csv` is implementation authority; filter its `batch` column.
- `PHASE-6-BATCH-PLAN.md` defines batch boundaries, dependencies, validation, and done criteria.

Previous completeness claims are superseded where they conflict with this body-based, current-guide audit. Re-audit after the backlog is implemented.
"""
    (OUT/"README.md").write_text(readme,encoding="utf-8")
    audit=f"""# Phase 5 Official CPP and SAA Coverage Audit

## Audit Metadata

Checked {CHECKED}; audit branch `audit/phase5-official-coverage`; checkpoint `8bfc169`. Audit and planning only.

## Repository and Git State

The Phase 4 working state was preserved on `backup/pre-phase5-audit-20260721-2100`, committed locally, and used to create the audit branch. Nothing was pushed.

## Official Exam Versions Verified

- AWS Certified Cloud Practitioner: **CLF-C02**, four domains, 19 tasks.
- AWS Certified Solutions Architect - Associate: **SAA-C03**, four domains, 14 tasks.

## Official Sources Used

[CPP guide]({CPP_GUIDE}), [CPP technologies]({CPP_TECH}), [CPP scope]({CPP_SCOPE}), [CPP out-of-scope list]({CPP_OUT}), [SAA guide]({SAA_GUIDE}), [SAA scope]({SAA_SCOPE}), [SAA out-of-scope list]({SAA_OUT}).

## Methodology

All {len(inv)} Markdown files under categories 01-16 were read. Evidence matching used body text and exact headings; filename, folder, README listing, badge, or one service mention was never sufficient. Requirements were scored complete 1.0, partial 0.5, mention-only 0.1, wrong-depth 0.25, missing 0, and outdated at most 0.25. Automated candidates are deliberately conservative and require human source verification during implementation.

## Important Scope Limitations

AWS describes service lists as non-exhaustive and changeable. The audit maps the sources checked on {CHECKED}; it does not promise permanent or guaranteed exam coverage.

## Canonical Repository Inventory

{len(inv)} Markdown files across 16 active categories were inspected, including navigation READMEs. Every file appears once in the inventory. {len(set(s for r in inv for s in r['services_mentioned'].split('; ') if s))} official-name services and {len(set(c for r in inv for c in r['concepts_covered'].split('; ') if c))} audited concepts were detected in bodies.

## CPP Coverage Summary

Requirements: {cpc['complete']} complete, {cpc['partial']+cpc['mention-only']+cpc['wrong-depth']} partial/mention/wrong-depth, {cpc['missing']} missing. See the CPP dashboard for domain scores.

## CPP Domain Findings

Service recognition is broader than foundations. Cloud concepts, shared responsibility, global infrastructure, and beginner-oriented comparisons need coherent treatment.

## CPP Critical Gaps

P0/P1 work centers on foundational cloud value, shared responsibility, IAM, global infrastructure, core compute/storage/database/network recognition, and current pricing/support facts.

## SAA Coverage Summary

Requirements: {sac['complete']} complete, {sac['partial']+sac['mention-only']+sac['wrong-depth']} partial/mention/wrong-depth, {sac['missing']} missing. Definition-level service notes dominate; architecture readiness is substantially lower than representation.

## SAA Domain Findings

Secure, resilient, high-performing, and cost-optimized decisions are uneven. Major gaps include multi-tier design, Multi-AZ/Multi-Region reasoning, database and storage selection, failure behavior, and cross-dimension trade-offs.

## SAA Critical Gaps

The backlog prioritizes secure access/data, loose coupling, HA/DR, elastic compute, VPC design, database selection, and explicit scenario reasoning.

## Shared CPP and SAA Depth Findings

Shared topics often have useful awareness content but lack a beginner narrative for CPP and decision/trade-off depth for SAA. Both badges cannot substitute for both depths.

## Service-Scope Findings

The service matrix checks {len(services)} distinct current listed service names across the two official lists. Missing representation is tracked without treating every service as equally important.

## Architecture-Quality Findings

The architecture audit identifies missing or definition-only treatment across web, serverless, event-driven, container, data, hybrid, recovery, and cost-optimization scenarios.

## Terminology Findings

AWS Health, IAM Identity Center, SageMaker AI, Amazon Quick/QuickSight transition wording, retired Elastic Transcoder, and CodeCommit availability need controlled review.

## Pricing and Support Freshness Findings

Support features, response times, Free Tier offers, exact discounts, and data-transfer charges remain date-sensitive. Phase 6 must verify each against current official pages.

## Structure and Navigation Findings

The hierarchy is canonical, but small-file fragmentation, missing local indexes, comparison overlap, and post-implementation navigation refresh require attention. No restructuring occurred.

## Out-of-Scope and Supplementary Findings

Absence from a non-exhaustive list is not a deletion reason. Supplementary and historical notes are retained and labeled for role review.

## Previous Coverage Claims Review

Explicit broad claims were searched. Any found are interpreted as historical/structural and superseded for current certification completeness by Phase 5.

## Prioritized Phase 6 Backlog Summary

{len(backlog)} actionable items: {sum(r['priority']=='P0' for r in backlog)} P0, {sum(r['priority']=='P1' for r in backlog)} P1, {sum(r['priority']=='P2' for r in backlog)} P2, and {sum(r['priority'] in ('P3','P4') for r in backlog)} P3/P4.

## Phase 6 Batch Summary

Batch counts: {', '.join(f'{k}: {bc[k]}' for k in [f'Batch {i}' for i in range(1,11)])}. Batch 1 and Batch 2 are directly filterable in the CSV.

## Final Evidence-Based Result

The repository has broad service representation but remains partial at CPP foundational depth and especially at SAA architecture/scenario depth. Phase 5 creates an evidence-based implementation plan; full certification coverage is not claimed until the backlog is implemented and re-audited.
"""
    (OUT/"PHASE-5-OFFICIAL-COVERAGE-AUDIT.md").write_text(audit,encoding="utf-8")
    print(f"generated {len(inv)} inventory rows, {len(cpp)} CPP requirements, {len(saa)} SAA requirements, {len(services)} services, {len(backlog)} backlog items")

if __name__ == "__main__": main()
