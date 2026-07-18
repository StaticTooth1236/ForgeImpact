# QUALITY MANAGEMENT PLAN
## Eurus Systems MAAP-1 "AetherForge" Program

---

| | |
|---|---|
| **Document No.** | AF-MAAP1-QMP-0001 |
| **Revision** | A (Initial Release) |
| **Classification** | Eurus Systems Proprietary — Program Controlled |
| **Effective Date** | [Current Date] |
| **Supersedes** | None (Initial Release) |
| **Applicable To** | All MAAP-1 Variants (MAAP-1F, MAAP-1I, MAAP-1C), All Program Phases |
| **Owner** | MAAP-1 Quality Director |
| **Approval Authority** | Program Manager |

---

## DOCUMENT CONTROL AND APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Quality Director** | [Name] | _____________ | ______ |
| **Chief Engineer** | [Name] | _____________ | ______ |
| **Manufacturing Director** | [Name] | _____________ | ______ |
| **Supply Chain Director** | [Name] | _____________ | ______ |
| **Program Manager** | [Name] | _____________ | ______ |

### Distribution List
- Program Control Board (PCB)
- All Integrated Product Teams (IPTs)
- Tier 1 Suppliers (via Supplier Quality Requirements Document)
- Customer Quality Representative (if assigned)
- Configuration Management Office

---

## EXECUTIVE SUMMARY

This Quality Management Plan (QMP) establishes the comprehensive quality management framework for the Eurus Systems MAAP-1 "AetherForge" heavy-lift tandem-rotor autonomous helicopter program. The QMP defines quality policies, organizational structure, processes, procedures, and metrics necessary to achieve program quality objectives across all phases from development through full-rate production and sustainment.

### Key Quality Objectives

1. **Zero Defects at Delivery:** Achieve 99%+ first-time acceptance rate at customer delivery gate by FRP
2. **Design Quality Excellence:** Close 100% of Critical Design Review (CDR) action items prior to first production release
3. **Manufacturing Quality Stability:** Achieve Manufacturing Readiness Level (MRL) 9 before FRP transition
4. **Supply Chain Quality:** Maintain supplier defect rate <500 DPPM (Defects Per Million Parts)
5. **Flight Safety Assurance:** Zero quality-related flight safety incidents or airworthiness deficiencies
6. **Regulatory Compliance:** Achieve FAA Type Certification with zero major findings at conformity inspection

### Quality Management System Standards

This QMP establishes a quality management system compliant with:
- **AS9100D** (Rev D): Quality Management Systems – Requirements for Aviation, Space, and Defense Organizations
- **ISO 9001:2015**: Quality Management Systems – Requirements
- **FAA Part 21**: Certification Procedures for Products and Articles
- **FAA Part 29**: Airworthiness Standards: Transport Category Rotorcraft
- **MIL-STD-1916**: DoD Preferred Methods for Acceptance of Product

The MAAP-1 Quality Management System (QMS) is certified to AS9100D and maintains FAA Design and Production Approval (Type Certificate and Production Certificate anticipated by PM 84).

---

## TABLE OF CONTENTS

1. [Introduction and Scope](#1-introduction-and-scope)
2. [Quality Policy and Objectives](#2-quality-policy-and-objectives)
3. [Quality Organization Structure](#3-quality-organization-structure)
4. [Quality Management System Framework](#4-quality-management-system-framework)
5. [Quality Planning by Program Phase](#5-quality-planning-by-program-phase)
6. [Design Assurance and Verification](#6-design-assurance-and-verification)
7. [Manufacturing Quality Control](#7-manufacturing-quality-control)
8. [Supplier Quality Management](#8-supplier-quality-management)
9. [Non-Conformance Management and CAPA](#9-non-conformance-management-and-capa)
10. [Quality Audits and Assessments](#10-quality-audits-and-assessments)
11. [Quality Records and Documentation](#11-quality-records-and-documentation)
12. [Quality Metrics and KPIs](#12-quality-metrics-and-kpis)
13. [Integration with Configuration and Risk Management](#13-integration-with-configuration-and-risk-management)
14. [Training and Competency](#14-training-and-competency)
15. [Continuous Improvement](#15-continuous-improvement)

**Appendices:**
- Appendix A: Quality Organization Charts
- Appendix B: Quality Procedures Index
- Appendix C: Inspection and Test Plan Templates
- Appendix D: Supplier Quality Requirements
- Appendix E: Quality Forms and Checklists
- Appendix F: Acronyms and Definitions

---

## 1. INTRODUCTION AND SCOPE

### 1.1 Purpose

This Quality Management Plan defines the comprehensive quality management approach for the Eurus Systems MAAP-1 program, establishing:

- Quality policies, objectives, and performance metrics aligned with program requirements
- Quality organizational structure, roles, and responsibilities
- Quality management system processes and procedures
- Design quality assurance and verification/validation methodologies
- Manufacturing quality control strategies across production ramp phases
- Supplier quality management requirements and oversight processes
- Non-conformance management and corrective/preventive action systems
- Quality audit programs (internal, external, supplier)
- Quality documentation and records management
- Integration points with Configuration Management and Risk Management

### 1.2 Scope and Applicability

This QMP applies to:

**Program Phases:**
- Design and Development (through CDR and First Flight)
- Low-Rate Initial Production (LRIP Phases 1-3)
- Full-Rate Production (FRP Phases 1-2)
- Sustainment and Product Support

**Product Scope:**
- MAAP-1 "Green Aircraft" baseline configuration (common to all variants)
- Variant-unique systems for MAAP-1F (Firefighting), MAAP-1I (ISR), MAAP-1C (Cargo)
- Government Furnished Equipment (GFE) integration where Eurus has quality responsibility
- All deliverable hardware, software, and documentation

**Organizational Scope:**
- Eurus Systems facilities (primary manufacturing, composite fabrication, final assembly, test)
- All Tier 1, 2, and 3 suppliers providing hardware, software, or services to the MAAP-1 program
- Subcontractors performing work under Eurus-issued statements of work

### 1.3 Relationship to Other Program Documents

This QMP is subordinate to and derives requirements from:

| Document | Relationship |
|----------|--------------|
| **Program Requirements Baseline (PRB)** AF-MAAP1-PRB-0001 | Establishes quality-related requirements, KPPs, and constraints |
| **Configuration Management Plan (CMP)** AF-MAAP1-CMP-0001 | Defines change control processes that quality verifies and enforces |
| **Manufacturing Ramp Plan** MAAP1-MFG-PLAN-2024-001 | Establishes production rate transitions that quality must support |
| **Systems Engineering Management Plan (SEMP)** | Defines verification and validation processes quality executes |
| **Test and Evaluation Master Plan (TEMP)** | Establishes test programs requiring quality oversight and data collection |
| **Risk Management Plan (RMP)** | Identifies quality-related risks requiring mitigation and monitoring |
| **Supply Chain Management Plan** | Defines supplier selection and management processes quality supports |

### 1.4 Document Maintenance and Revision Control

**Document Owner:** MAAP-1 Quality Director

**Revision Authority:**
- Minor revisions (procedural updates, template changes): Quality Director approval
- Major revisions (organizational changes, requirement changes): Program Manager approval via Configuration Control Board (CCB)

**Review Cycle:**
- Annual review for currency and effectiveness
- Event-driven reviews at major program phase transitions (PDR, CDR, LRIP Gates, FRP Gate)
- Revision within 30 days of PRB or CMP changes affecting quality requirements

**Distribution:**
- Controlled electronic copy maintained in Program Document Management System
- Automatic notification to all holders upon revision
- Supplier access to relevant sections via Supplier Portal (read-only)

---

## 2. QUALITY POLICY AND OBJECTIVES

### 2.1 Eurus Systems Corporate Quality Policy

> *"Eurus Systems is committed to delivering aerospace products and services that meet or exceed customer requirements, regulatory standards, and industry best practices. We achieve quality excellence through a culture of continuous improvement, empowered employees, robust processes, and data-driven decision-making. Quality is the responsibility of every employee and is integral to our business success."*

**Policy Statement Endorsed:** Eurus Systems CEO, [Date]

### 2.2 MAAP-1 Program Quality Policy

The MAAP-1 program implements the Eurus Systems Quality Policy through the following commitments:

1. **Customer Focus:** We design, manufacture, and deliver products that meet documented customer requirements as defined in the Program Requirements Baseline and applicable contracts.

2. **Right First Time:** We prevent defects through robust design, validated processes, and proactive risk management rather than relying on inspection to find defects.

3. **Continuous Improvement:** We systematically identify opportunities for improvement and implement data-driven solutions to enhance quality, reduce cost, and improve delivery.

4. **Regulatory Compliance:** We maintain full compliance with FAA airworthiness requirements, AS9100D quality system standards, and all applicable government and industry regulations.

5. **Supply Chain Partnership:** We develop and maintain supplier relationships based on mutual quality objectives, transparent performance metrics, and collaborative problem-solving.

6. **Empowered Workforce:** We provide our workforce with the training, tools, authority, and support necessary to achieve quality objectives and stop production when quality is at risk.

7. **Data-Driven Decisions:** We collect, analyze, and act upon objective quality data to drive process improvements and management decisions.

### 2.3 MAAP-1 Quality Objectives

Quality objectives are established to support program Key Performance Parameters (KPPs) and strategic objectives defined in PRB Section 2.2.

#### 2.3.1 Design Quality Objectives

| Objective | Metric | Target | Phase |
|-----------|--------|--------|-------|
| **Design Requirement Compliance** | % of requirements verified by CDR | 100% | Development |
| **Design Review Action Closure** | Open action items at CDR closure | Zero critical/major | Development |
| **Design FMEA Completion** | % of identified failure modes with mitigation | 100% | Development |
| **Safety Assessment Closure** | Unmitigated hazards at First Flight | Zero (Cat I/II)<br>≤5% (Cat III/IV) | Development |
| **Drawing/Specification Quality** | Discrepancies per 100 released drawings | <2 | Development/Production |
| **Software Quality (Flight Critical)** | DO-178C DAL A/B compliance | 100% | Development/Production |

#### 2.3.2 Manufacturing Quality Objectives

| Objective | Metric | LRIP Target | FRP Target |
|-----------|--------|-------------|------------|
| **First-Time Quality** | % parts/assemblies accepted first time | 95% | 99% |
| **Defects Per Million Opportunities (DPMO)** | Manufacturing defects per million ops | 3,000 | 500 |
| **Customer Acceptance Rate** | % aircraft accepted at delivery gate | 98% | 99.5% |
| **Scrap/Rework Rate** | % of manufacturing cost | <3% | <1% |
| **In-Process Defect Escape Rate** | Defects found downstream vs. source | <2% | <0.5% |
| **Process Capability (Cpk)** | Critical characteristics | ≥1.33 | ≥1.67 |
| **Tool Calibration Compliance** | % tools in calibration at audit | 100% | 100% |

#### 2.3.3 Supplier Quality Objectives

| Objective | Metric | LRIP Target | FRP Target |
|-----------|--------|-------------|------------|
| **Supplier Defect Rate** | DPPM (parts and assemblies) | <1,000 | <500 |
| **Supplier On-Time Delivery (Quality Released)** | % deliveries accepted on schedule | >90% | >95% |
| **Supplier Corrective Action Closure** | % CARs closed on time | >85% | >95% |
| **Supplier Audit Compliance** | Average audit score | >85/100 | >90/100 |
| **First Article Inspection Pass Rate** | % FAI passed first submission | >80% | >90% |

#### 2.3.4 Flight Safety and Airworthiness Objectives

| Objective | Metric | Target |
|-----------|--------|--------|
| **Flight Safety Incidents** | Quality-related flight safety events | Zero |
| **Airworthiness Deficiencies** | FAA findings (major) at conformity | Zero |
| **Safety-Critical Nonconformance** | Cat I/II nonconformances | Zero escapes to flight |
| **Autonomous System Reliability** | Loss of control function per FH | <1×10⁻⁷ (per PRB) |
| **Crashworthiness Compliance** | Compliance to MIL-STD-1290 | 100% |

#### 2.3.5 Customer Satisfaction Objectives

| Objective | Metric | Target |
|-----------|--------|--------|
| **Delivery Quality** | Customer acceptance discrepancies per aircraft | <5 |
| **Warranty Defects** | Defects discovered in first 90 days | <2 per aircraft |
| **Customer Satisfaction Score** | Survey rating (1-10 scale) | ≥8.5 |
| **Field Service Response** | Response time to quality issues | <24 hours |

### 2.4 Quality Objective Deployment and Review

**Deployment Process:**
1. Program-level objectives established annually by Quality Director with Program Manager approval
2. Functional-level objectives flowed down to departments (Design, Manufacturing, Supply Chain)
3. Individual performance objectives aligned to functional objectives
4. Supplier quality objectives incorporated in quality agreements and SOWs

**Review Cadence:**
- **Monthly:** Quality Steering Committee reviews metrics vs. objectives
- **Quarterly:** Program Management Review includes quality objective status
- **Semi-Annual:** Quality Director presents performance trends to Executive Leadership
- **Annual:** Objectives reviewed and updated for following year

**Escalation Triggers:**
- Any objective >15% off target for two consecutive months: Corrective Action Plan required
- Any objective trending to miss annual target: Executive escalation and resource review
- Customer satisfaction score <7.0: Immediate Program Manager notification and recovery plan

---

## 3. QUALITY ORGANIZATION STRUCTURE

### 3.1 Quality Organizational Philosophy

The MAAP-1 program employs a **matrix quality organization** combining:

- **Functional Quality Organization:** Centralized Quality department providing quality engineering, inspection, audit, and systems support
- **Program-Embedded Quality:** Quality representatives embedded in Integrated Product Teams (IPTs) with dotted-line reporting to IPT Leads and solid-line reporting to Quality Director
- **Independent Oversight:** Quality Director reports directly to Program Manager (not to Engineering or Operations) to maintain organizational independence

**Key Principles:**
- Quality has authority to stop production, reject product, and escalate issues without operational pressure
- Quality participates in design reviews, production planning, and supplier selection decisions
- Quality is adequately resourced (target: 8-12% of direct workforce)
- Quality personnel have access to all areas, records, and personnel necessary to perform their duties

### 3.2 Quality Leadership Structure

#### Program Quality Director
**Reports To:** MAAP-1 Program Manager (solid line), Eurus Corporate VP Quality (dotted line)

**Responsibilities:**
- Overall quality system effectiveness and compliance
- Quality policy implementation and objective setting
- Quality budget and resource management
- Interface with customer quality representatives and regulatory authorities
- Approval authority for major nonconformances and deviations
- Quality representation on Program Control Board
- Supplier quality performance oversight

**Authority:**
- Stop production for safety or quality concerns
- Reject non-conforming product
- Require corrective action implementation
- Escalate unresolved quality issues to Program Manager
- Approve/disapprove quality system changes

---

#### Design Quality Manager
**Reports To:** Quality Director (solid), Chief Engineer (dotted)

**Responsibilities:**
- Design FMEA facilitation and closure tracking
- Design review participation and action closure
- Engineering drawing/specification review and approval
- Design verification and validation planning
- Software quality assurance (coordination with Software IPT)
- Certification liaison for design airworthiness compliance
- Configuration audit planning and execution

**Staff (Development Phase):**
- 3× Design Quality Engineers
- 2× Software Quality Engineers
- 1× Certification Quality Specialist

---

#### Manufacturing Quality Manager
**Reports To:** Quality Director (solid), Manufacturing Director (dotted)

**Responsibilities:**
- Manufacturing inspection planning and execution
- Production acceptance testing oversight
- Manufacturing process qualification and validation
- Statistical process control implementation
- Shop floor quality support and problem resolution
- Quality data collection and analysis
- Calibration and tool control program management

**Staff (Scaled by Phase):**

| Phase | Quality Engineers | Inspectors | Lab Technicians |
|-------|------------------|------------|-----------------|
| LRIP-1 | 4 | 12 | 2 |
| LRIP-3 | 6 | 28 | 4 |
| FRP-2 | 10 | 52 | 6 |

---

#### Supplier Quality Manager
**Reports To:** Quality Director (solid), Supply Chain Director (dotted)

**Responsibilities:**
- Supplier quality requirements definition
- Source inspection and supplier audits
- Supplier corrective action management
- Incoming inspection oversight
- Supplier performance metrics and scorecards
- Supplier development and improvement initiatives
- Government source inspection coordination

**Staff:**
- 2× Supplier Quality Engineers
- 4× Source Inspectors (field-based)
- 6× Receiving Inspectors (facility-based)
- 1× Supplier Quality Data Analyst

---

#### Quality Engineering Manager
**Reports To:** Quality Director

**Responsibilities:**
- Quality system maintenance and improvement
- Internal audit program management
- Quality procedure development and training
- Nonconformance and CAPA system administration
- Quality metrics reporting and analysis
- Customer quality interface support
- Regulatory compliance oversight (AS9100D, ISO 9001)

**Staff:**
- 2× Quality System Engineers
- 2× Internal Auditors (Lead and Auditor)
- 1× Quality Records Administrator
- 1× Quality Training Coordinator

---

### 3.3 Quality Organization Charts

**See Appendix A for detailed organizational charts by program phase**

### 3.4 Roles, Responsibilities, and Authorities (RACI Matrix)

**Key:**
- **R** = Responsible (does the work)
- **A** = Accountable (final authority/approval)
- **C** = Consulted (input required)
- **I** = Informed (kept updated)

| Activity | Quality Director | Design Quality Mgr | Mfg Quality Mgr | Supplier Quality Mgr | Chief Engineer | Mfg Director |
|----------|------------------|-------------------|----------------|---------------------|---------------|--------------|
| Quality Policy Setting | A | C | C | C | C | C |
| Design Review Approval | I | R/C | I | I | A | I |
| Drawing Release Approval | I | R/A | C | I | A | I |
| Manufacturing Process Approval | C | I | R/A | I | C | A |
| Product Acceptance (Final) | A | I | R | I | I | C |
| Supplier Approval | C | I | C | R/A | I | A |
| Nonconformance Disposition | A | R (design) | R (mfg) | R (supplier) | C | C |
| Internal Audit Execution | A | C | C | C | I | I |
| CAPA Approval | A | C | C | C | I | I |
| Quality Metrics Reporting | R/A | R | R | R | I | I |

### 3.5 Quality Staffing Plan by Phase

**Workforce Scaling Aligned to Manufacturing Ramp Plan (MAAP1-MFG-PLAN-2024-001):**

| Phase | Production Rate | Direct Labor | Quality Staff | Quality % |
|-------|----------------|--------------|---------------|-----------|
| Development (Pre-LRIP) | 0 | 65 | 12 | 18% |
| LRIP-1 | 2/year | 95 | 18 | 11% |
| LRIP-2 | 6/year | 180 | 24 | 10% |
| LRIP-3 | 12/year | 295 | 38 | 9.5% |
| FRP-1 | 24/year | 485 | 58 | 9% |
| FRP-2 | 48/year | 750 | 78 | 8.5% |

**Staffing Strategy:**
- Front-load quality resources in development to prevent downstream defects
- Maintain >15% quality ratio during early production to build culture and mature processes
- Target 8-10% quality ratio at FRP as processes stabilize and automation increases
- Maintain flexibility through contract quality support (up to 20% of workforce)

---

## 4. QUALITY MANAGEMENT SYSTEM FRAMEWORK

### 4.1 QMS Scope and Standards Compliance

The MAAP-1 Quality Management System is established, documented, implemented, and maintained in accordance with:

**Primary Standards:**
- **AS9100D:2016** – Quality Management Systems – Requirements for Aviation, Space, and Defense Organizations
- **ISO 9001:2015** – Quality Management Systems – Requirements

**Regulatory Requirements:**
- **14 CFR Part 21** – Certification Procedures for Products and Articles (FAA Design/Production Approval)
- **14 CFR Part 29** – Airworthiness Standards: Transport Category Rotorcraft
- **FAA Order 8110.4C** – Type Certification (Process Requirements)

**Additional Standards (as applicable):**
- **AS9145** – Advanced Product Quality Planning (APQP) and Production Part Approval Process (PPAP)
- **MIL-STD-1916** – DoD Preferred Methods for Acceptance of Product
- **DO-178C** – Software Considerations in Airborne Systems and Equipment Certification (via Software Quality Assurance)
- **DO-254** – Design Assurance Guidance for Airborne Electronic Hardware

### 4.2 QMS Process Architecture

The MAAP-1 QMS follows the **Plan-Do-Check-Act (PDCA) / Process Approach** model defined in ISO 9001:

```
┌─────────────────────────────────────────────────────┐
│          CUSTOMER REQUIREMENTS (PRB)                │
└──────────────────┬──────────────────────────────────┘
                   │
         ┌─────────▼─────────┐
         │   PLAN            │
         │ - Quality Planning│
         │ - Requirements    │
         │ - Resources       │
         └─────────┬─────────┘
                   │
         ┌─────────▼─────────┐
         │   DO              │
         │ - Design          │
         │ - Manufacture     │
         │ - Supply Chain    │
         └─────────┬─────────┘
                   │
         ┌─────────▼─────────┐
         │   CHECK           │
         │ - Inspect/Test    │
         │ - Audit           │
         │ - Metrics         │
         └─────────┬─────────┘
                   │
         ┌─────────▼─────────┐
         │   ACT             │
         │ - Nonconformance  │
         │ - CAPA            │
         │ - Improvement     │
         └─────────┬─────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│         CUSTOMER SATISFACTION / PRODUCT             │
└─────────────────────────────────────────────────────┘
```

### 4.3 QMS Core Processes

#### 4.3.1 Management Processes

| Process | Owner | Purpose | Key Outputs |
|---------|-------|---------|-------------|
| **Quality Planning** | Quality Director | Establish quality objectives, resources, and plans | Quality Management Plan, Phase Quality Plans |
| **Management Review** | Program Manager | Review QMS effectiveness and improvement opportunities | Management review minutes, action items |
| **Document and Records Management** | Quality Engineering Mgr | Control quality documents and maintain records | Controlled documents, archived records |
| **Internal Audit** | Quality Engineering Mgr | Verify QMS compliance and effectiveness | Audit reports, findings, CAPAs |
| **CAPA Management** | Quality Engineering Mgr | Systematic problem resolution and prevention | Corrective action reports, effectiveness verification |

#### 4.3.2 Realization Processes

| Process | Owner | Purpose | Key Outputs |
|---------|-------|---------|-------------|
| **Design Quality Assurance** | Design Quality Mgr | Ensure design meets requirements and is producible | Design FMEAs, verification reports, design reviews |
| **Design Verification/Validation** | Design Quality Mgr | Confirm design compliance through test/analysis | V&V reports, test data, certifications |
| **Manufacturing Planning** | Mfg Quality Mgr | Plan inspection, test, and process controls | Inspection plans, process control plans |
| **Production Acceptance** | Mfg Quality Mgr | Verify conformance to requirements | Inspection records, test reports, acceptance certificates |
| **Supplier Quality Management** | Supplier Quality Mgr | Ensure purchased product meets requirements | Approved supplier list, supplier audits, incoming inspection |

#### 4.3.3 Support Processes

| Process | Owner | Purpose | Key Outputs |
|---------|-------|---------|-------------|
| **Calibration Management** | Mfg Quality Mgr | Ensure measurement system accuracy | Calibration certificates, tool control records |
| **Nonconformance Control** | Quality Engineering Mgr | Identify, segregate, and disposition nonconforming product | Nonconformance reports, Material Review Board minutes |
| **Training and Competency** | Quality Training Coordinator | Ensure personnel qualification | Training records, competency assessments |
| **Quality Records Management** | Quality Records Admin | Maintain objective evidence of conformance | Organized, retrievable, protected quality records |

### 4.4 QMS Documentation Hierarchy

```
Level 1: Quality Manual
         └─ Defines QMS scope, policy, and process interactions
            Document: AF-MAAP1-QM-0001
            
Level 2: Quality Management Plan (This Document)
         └─ Defines program-specific quality strategy
            Document: AF-MAAP1-QMP-0001
            
Level 3: Quality Procedures (Corporate and Program-Specific)
         └─ "How to" procedures for QMS processes
            Documents: QP-xxx (Corporate), AF-MAAP1-QP-xxx (Program)
            
Level 4: Work Instructions and Standards
         └─ Detailed instructions for specific tasks
            Documents: WI-xxx, MFG-STD-xxx, INSP-xxx
            
Level 5: Forms, Templates, and Records
         └─ Documentation of quality activities
            Documents: QF-xxx (forms), QR-xxx (records)
```

**Document Control:**
- All QMS documents maintained in Program Document Management System (DMS)
- Revision control per Configuration Management Plan (AF-MAAP1-CMP-0001)
- Electronic approval workflow with controlled access
- Automatic obsolete document removal and archival
- External documents (standards, customer specs) controlled via reference list

### 4.5 AS9100D Compliance Matrix

**AS9100D Clause Mapping to MAAP-1 QMS:**

| Clause | Requirement | MAAP-1 Implementation | Reference Section |
|--------|-------------|----------------------|-------------------|
| 4.1 | Understanding organization and context | PRB strategic objectives, stakeholder analysis | Section 2 |
| 4.2 | Interested parties needs | Customer requirements, regulatory compliance | Section 2.3 |
| 4.3 | QMS scope | MAAP-1 program scope definition | Section 1.2 |
| 4.4 | QMS and processes | Process architecture, documentation | Section 4.2, 4.3 |
| 5.1 | Leadership and commitment | Quality policy, management review | Section 2.1 |
| 5.2 | Quality policy | MAAP-1 quality policy statement | Section 2.2 |
| 5.3 | Organizational roles | Quality organization, RACI matrix | Section 3 |
| 6.1 | Risk and opportunity management | Quality risk register integration | Section 13.2 |
| 6.2 | Quality objectives | Program quality objectives | Section 2.3 |
| 7.1 | Resources | Quality staffing plan, budget | Section 3.5 |
| 7.2 | Competence | Training and qualification | Section 14 |
| 7.3 | Awareness | Quality communication plan | Section 14.4 |
| 7.4 | Communication | Quality meetings, reporting | Section 12 |
| 7.5 | Documented information | Document control, records management | Section 11 |
| 8.1 | Operational planning | Phase quality plans | Section 5 |
| 8.2 | Product requirements | Requirements traceability | Section 6.1 |
| 8.3 | Design and development | Design quality assurance | Section 6 |
| 8.4 | External providers | Supplier quality management | Section 8 |
| 8.5 | Production and service | Manufacturing quality control | Section 7 |
| 8.6 | Product release | Acceptance processes | Section 7.5 |
| 8.7 | Nonconforming outputs | Nonconformance management | Section 9 |
| 9.1 | Monitoring and measurement | Quality metrics and KPIs | Section 12 |
| 9.2 | Internal audit | Internal audit program | Section 10.1 |
| 9.3 | Management review | Quality Steering Committee | Section 4.6 |
| 10.1 | Nonconformity and CAPA | CAPA process | Section 9.2 |
| 10.2 | Continual improvement | Continuous improvement program | Section 15 |

**AS9100D-Specific Requirements:**

| Requirement | Implementation |
|-------------|----------------|
| **Configuration Management (8.1.1)** | Integrated with CMP, Section 13.1 |
| **Product Safety (8.1.1)** | Safety-critical characteristics identification, Section 6.5.3 |
| **Risk Management (8.1.1)** | Quality risk integration with RMP, Section 13.2 |
| **Work Transfer (8.1.2)** | Not applicable (no planned work transfers) |
| **Verification of Externally Provided Processes (8.4.3)** | Supplier audits, source inspection, Section 8.4 |
| **Counterfeit Parts Prevention (8.4.3)** | Supplier controls, traceability, Section 8.5 |
| **Key Characteristics (8.5.1.2)** | Critical and key characteristics management, Section 7.4 |
| **Production Process Verification (8.5.1.3)** | First article inspection, process validation, Section 7.2 |
| **Control of Monitoring and Measuring Equipment (7.1.5.1)** | Calibration program, Section 7.8 |

### 4.6 Management Review Process

**Quality Steering Committee:**

**Charter:** Provide senior management oversight of MAAP-1 QMS effectiveness, review quality performance, and direct quality improvement initiatives.

**Membership:**
- Program Manager (Chair)
- Quality Director (Secretary)
- Chief Engineer
- Manufacturing Director
- Supply Chain Director
- Customer Quality Representative (if assigned)

**Meeting Frequency:** Monthly during development and LRIP; Quarterly during FRP

**Agenda Topics:**
1. Quality metrics review vs. objectives (Section 12)
2. Customer feedback and satisfaction trends
3. Audit results (internal, external, supplier)
4. Nonconformance trends and major issues
5. CAPA effectiveness review
6. Supplier quality performance
7. Quality resource adequacy
8. Quality system improvement opportunities
9. Changes affecting QMS (org, process, requirements)
10. Follow-up on previous action items

**Outputs:**
- Meeting minutes with decisions and action items (owner, due date)
- Quality objective updates (as needed)
- Resource allocation decisions
- Quality improvement initiatives approval
- Escalation to Executive Leadership (as required)

**Records:** Meeting minutes retained per Section 11.5 (minimum 10 years)

---

## 5. QUALITY PLANNING BY PROGRAM PHASE

Quality planning is tailored to the distinct characteristics and risks of each program phase, from early development through sustained production.

### 5.1 Phase-Based Quality Strategy

```
Program Timeline with Quality Focus Areas:

Development          LRIP              FRP           Sustainment
(PM 0-54)         (PM 54-78)      (PM 78-108+)    (PM 108+)
    │                 │               │                │
    │                 │               │                │
┌───▼────────┐   ┌────▼──────┐   ┌───▼──────┐   ┌────▼────────┐
│Design      │   │Process    │   │Production│   │Field        │
│Quality     │   │Validation │   │Stability │   │Performance  │
│Assurance   │   │& Control  │   │& Efficiency│   │& Support    │
└────────────┘   └───────────┘   └──────────┘   └─────────────┘
     │                │                │                │
     ▼                ▼                ▼                ▼
- Design Reviews - First Article - Learning Curve - Warranty Analysis
- V&V Planning   - Process FAI   - SPC Deployment - Obsolescence Mgmt
- FMEA/Safety    - Tool Proving  - Automation    - Product Improvement
- Requirements   - Supplier      - Supplier      - Lessons Learned
  Verification     Qualification    Scorecards
```

### 5.2 Development Phase Quality Plan (Through First Flight, PM 54)

**Phase Objectives:**
- Establish design quality baseline with 100% requirements verification
- Identify and mitigate design risks through FMEA and safety assessment
- Build quality into design through Design for Manufacturing and Assembly (DFMA)
- Prepare for production with mature processes and qualified suppliers

#### 5.2.1 Design Reviews

**Formal Design Review Gates:**

| Review | Timing | Quality Role | Quality Deliverables |
|--------|--------|--------------|----------------------|
| **System Requirements Review (SRR)** | PM 12 | Review requirements for completeness, verifiability, traceability | Requirements quality assessment, verification planning |
| **Preliminary Design Review (PDR)** | PM 24 | Review design concept for feasibility, risk, producibility | Design FMEA (preliminary), manufacturing risk assessment, quality plan |
| **Critical Design Review (CDR)** | PM 42 | Verify design maturity, producibility, inspection planning | Design FMEA (complete), inspection plans, process FMEAs, supplier quality plans |
| **Test Readiness Review (TRR)** | PM 50 | Verify test configuration, procedures, acceptance criteria | Test procedure approval, calibration verification |
| **Flight Readiness Review (FRR)** | PM 54 | Verify airworthiness, configuration control, flight safety | Airworthiness conformity statement, configuration audit |

**Design Review Quality Checklist (Example – CDR):**

- [ ] All design requirements traceable to PRB
- [ ] Design verification methods assigned for all requirements
- [ ] Design FMEAs complete for all major assemblies
- [ ] Critical and key characteristics identified
- [ ] Manufacturing process capability assessments complete
- [ ] Supplier quality plans approved
- [ ] Inspection and test plans drafted
- [ ] Configuration management processes defined
- [ ] Software quality assurance plan approved (if applicable)
- [ ] Safety assessment complete with hazards mitigated
- [ ] Producibility reviews conducted with manufacturing
- [ ] No open high-risk design issues

**Action Item Management:**
- All design review actions logged in Program Action Item Tracker
- Quality-assigned actions tracked to closure with verification evidence
- Critical actions (flight safety, airworthiness) must close before next gate
- Monthly action review in Quality Steering Committee

#### 5.2.2 Design FMEA Process

**Objective:** Systematically identify potential failure modes in the design and implement design changes or process controls to prevent or detect them.

**DFMEA Approach (per AIAG/VDA FMEA Handbook):**

**Scope:**
- System-level DFMEA: Major subsystems and interfaces
- Subsystem-level DFMEA: Major assemblies (fuselage, rotor system, propulsion, etc.)
- Component-level DFMEA: High-risk or novel components (as needed)

**Risk Prioritization:**
- **Severity (S):** 1-10 scale (10 = catastrophic failure, safety impact)
- **Occurrence (O):** 1-10 scale (10 = very high probability of failure)
- **Detection (D):** 1-10 scale (10 = no detection method before customer)
- **Action Priority (AP):** S × O × D (high AP = high priority for action)

**DFMEA Review Cadence:**
- Initial DFMEA: Conceptual design phase
- Updated DFMEA: PDR (all subsystems)
- Final DFMEA: CDR (complete with process controls defined)
- Living document: Updated for design changes, production feedback

**Quality Role in DFMEA:**
- Facilitate DFMEA sessions with cross-functional teams
- Challenge detection rankings (ensure realistic assessment)
- Verify recommended actions incorporated in design or manufacturing
- Track action closure and effectiveness
- Report high-risk FMEAs to Quality Steering Committee

**DFMEA Output to Manufacturing:**
- Critical and key characteristics requiring special process control (Section 7.4)
- Inspection requirements and methods
- Test requirements (functional, environmental, etc.)
- Supplier quality requirements for high-risk purchased items

#### 5.2.3 Design Verification and Validation (V&V)

**V&V Strategy aligned to PRB Section 10:**

**Verification Methods (Per Requirement):**
- **Test (T):** Physical testing on hardware (component, subsystem, system level)
- **Analysis (A):** Engineering analysis (structural FEA, thermal, etc.), simulation
- **Inspection (I):** Visual examination, dimensional measurement, document review
- **Demonstration (D):** Functional demonstration without instrumented data collection

**Quality Verification Activities:**

**Requirements Verification Matrix (RVM):**
- Maintained in Requirements Management Tool with bidirectional traceability
- Quality reviews RVM for completeness at SRR, PDR, CDR
- Quality approves verification methods and acceptance criteria
- Quality witnesses or performs verification activities per method:
  - **Test:** Quality witness testing, review test reports, verify calibration
  - **Analysis:** Quality reviews analysis reports for completeness and rigor
  - **Inspection:** Quality performs or witnesses inspections per approved procedures
  - **Demonstration:** Quality witnesses demonstrations, documents results

**Validation Activities:**
- **End-to-end mission scenarios:** Validate that integrated system meets user needs
- **Operational environment testing:** Hot/high altitude, cold weather, degraded visual environment (DVE)
- **Autonomous system validation:** Demonstrate mission success without pilot intervention
- **Customer acceptance testing:** Customer-defined validation test scenarios

**Quality Role:**
- Review and approve V&V plans and procedures
- Verify test article configuration control (correct drawing revision, mod status)
- Witness critical tests (first article, safety-critical, certification tests)
- Review and approve test reports
- Verify all requirements verified before production release

**V&V Records:**
- Test plans and procedures (approved)
- Test reports with raw data, analysis, and conclusions
- Inspection records with actual measurements
- Analysis reports with assumptions, methods, results
- Verification status in RVM (open/closed with evidence)
- Traceability matrix from requirement → verification → evidence

#### 5.2.4 Software Quality Assurance (SQA)

**Scope:** Flight-critical software developed to DO-178C Design Assurance Level (DAL) A or B per PRB constraint C-5.

**SQA Organization:**
- Software Quality Engineers embedded in Software IPT
- Report to Design Quality Manager (solid line)
- Independent from software development team (organizational independence per DO-178C)

**SQA Activities by DO-178C Process:**

| DO-178C Process | SQA Activity |
|-----------------|--------------|
| **Planning** | Review and approve Software Development Plan (SDP), Software Verification Plan (SVP), Software Configuration Management Plan (SCMP), Software Quality Assurance Plan (SQAP) |
| **Development** | Review software requirements for completeness, ambiguity, verifiability; review software design for compliance to requirements and standards; audit coding standards compliance |
| **Verification** | Witness or review requirements-based testing, structural coverage analysis, review test procedures and results; verify traceability |
| **Configuration Management** | Audit software baselines, change control, version control; verify problem reporting closure |
| **Quality Assurance** | Audit compliance to plans, standards, and procedures; verify independence of verification; report findings to Program Manager and Certification Authority |

**SQA Deliverables:**
- Software Accomplishment Summary (SAS) for certification
- SQA audit reports and findings
- Software verification traceability matrix
- Software conformity review for production release

**Tool Qualification:**
- Tools used for verification (compilers, test tools) qualified per DO-178C Section 12
- Tool qualification plans reviewed and approved by SQA
- Tool qualification records maintained

#### 5.2.5 Development Phase Quality Metrics

| Metric | Target | Reporting Frequency |
|--------|--------|---------------------|
| Design Review Action Closure Rate | 100% critical/major by gate | Weekly during review cycle |
| Requirements Verification Completion | 100% by CDR | Monthly |
| Design FMEA Coverage | 100% subsystems by CDR | Monthly |
| Open High Severity DFMEA Items | Zero by First Flight | Weekly after CDR |
| Software Requirements Traceability | 100% | Monthly |
| Software Test Coverage (DAL A) | 100% statement, 100% branch | Per software build |
| Design Change Rate (post-CDR) | <5% total requirements | Monthly |

---

### 5.3 LRIP Phase Quality Plan (PM 54-78, Units 1-22)

**Phase Objectives:**
- Validate manufacturing processes with First Article Inspection (FAI)
- Prove process capability and stability
- Qualify suppliers and establish supply chain quality
- Build quality culture and train production workforce
- Transition from prototype to production mindset

#### 5.3.1 LRIP Phase 1 (2 Units/Year, Units 1-4)

**Quality Focus: Process Validation and Learning**

**Key Activities:**

**1. First Article Inspection (FAI) Program**
   - **Scope:** All manufacturing processes, tooling, and supplier-provided parts/assemblies
   - **Standard:** AS9102 First Article Inspection Requirement
   - **Execution:**
     - FAI performed on first unit produced with production tooling and processes
     - 100% dimensional inspection of critical and key characteristics
     - Functional testing per production acceptance test procedures
     - Documented in AS9102 Form 1 (Index), Form 2 (Accountability), Form 3 (Results)
   - **Approval:** Manufacturing Quality Manager approval before production continuation
   - **Records:** FAI reports retained for life of program, available to customer/auditors

**2. Production Process Validation**
   - Statistical validation of process capability (Cpk) for critical characteristics
   - Minimum 30 data points before Cpk calculation
   - Target: Cpk ≥1.33 (LRIP), ≥1.67 (FRP goal)
   - Processes not meeting Cpk target: 100% inspection until improvement implemented

**3. Supplier Qualification**
   - Supplier FAI per AS9102 for all purchased parts
   - Source inspection on first 3 deliveries from new suppliers
   - Supplier process audits before production release
   - Approved supplier list maintained (Section 8.3)

**4. Workforce Training**
   - Quality training for all production personnel: 16 hours initial, 8 hours annual
   - Training topics: Quality policy, inspection techniques, nonconformance reporting, FOD prevention
   - Operator qualification for special processes (welding, bonding, NDT)
   - Certification records maintained per Section 14.2

**5. Lessons Learned Capture**
   - Post-unit quality review after each LRIP-1 unit
   - Document manufacturing quality issues, root causes, corrective actions
   - Feed lessons learned into process improvements for next unit
   - Monthly lessons learned review with Manufacturing and Engineering

**LRIP-1 Quality Metrics:**

| Metric | Target | Actual (Tracked Monthly) |
|--------|--------|--------------------------|
| First-Time Quality (FTQ) | 90% | ___% |
| FAI Pass Rate (first submission) | 80% | ___% |
| Process Cpk (critical characteristics) | ≥1.33 | ___ |
| Supplier Defect Rate (DPPM) | <2,000 | ___ |
| Customer Acceptance Rate | 95% | ___% |
| Major Nonconformances | <10 per unit | ___ |

#### 5.3.2 LRIP Phase 2 (6 Units/Year, Units 5-10)

**Quality Focus: Process Improvement and Stabilization**

**Key Activities:**

**1. Statistical Process Control (SPC) Deployment**
   - Implement SPC on 15 critical characteristics
   - Real-time control charts on shop floor (X-bar/R charts)
   - Out-of-control conditions trigger immediate investigation
   - Quality Engineers train operators on SPC interpretation

**2. Process Improvement Implementation**
   - Incorporate LRIP-1 lessons learned
   - Reduce inspection burden through process capability demonstration
   - Automate data collection for critical characteristics (eliminate manual transcription errors)
   - Implement poka-yoke (error-proofing) devices where feasible

**3. Supplier Performance Management**
   - Quarterly supplier scorecards (quality, delivery, responsiveness)
   - Supplier corrective actions for defect rate >1,000 DPPM
   - Supplier development visits for strategic suppliers
   - Second-source qualification for single-source risks

**4. Inspection Optimization**
   - Reduce sampling inspection frequency for stable processes (per MIL-STD-1916 sampling)
   - Implement automated inspection (laser scanning, CMM programming) where cost-effective
   - Focus inspection resources on high-risk and new processes

**LRIP-2 Quality Metrics:**

| Metric | Target | Actual (Tracked Monthly) |
|--------|--------|--------------------------|
| First-Time Quality (FTQ) | 95% | ___% |
| Process Cpk (critical characteristics) | ≥1.33 | ___ |
| Supplier Defect Rate (DPPM) | <1,000 | ___ |
| Customer Acceptance Rate | 98% | ___% |
| Scrap/Rework Rate | <3% | ___% |
| SPC Out-of-Control Events | <5 per month | ___ |

#### 5.3.3 LRIP Phase 3 (12 Units/Year, Units 11-22)

**Quality Focus: Readiness for Full-Rate Production**

**Key Activities:**

**1. Manufacturing Readiness Assessment**
   - Formal Manufacturing Readiness Level (MRL) assessment per DoD MRL Deskbook
   - Target: MRL 9 (Low-Rate Production demonstrated) by end of LRIP-3
   - Independent assessment by Quality + external auditor
   - Closure of all MRL gaps before FRP Gate

**2. Advanced Quality Planning**
   - Expand SPC to 50 critical characteristics
   - Deploy predictive quality analytics (trend analysis, early warning indicators)
   - Implement automated test equipment (ATE) for functional testing
   - Prepare for high-rate inspection capacity (hire and train additional inspectors)

**3. Supplier Readiness Verification**
   - Verify supplier capacity for FRP rates (audit supplier expansion plans)
   - Conduct supply chain resilience assessment (backup suppliers, inventory buffers)
   - Require supplier SPC implementation for critical parts

**4. Full-Rate Production Readiness Review (FRRR)**
   - Executive-level review conducted 6 months before FRP transition
   - Review areas:
     - Quality metrics trending to FRP targets
     - Process capability demonstrated and stable
     - Supplier quality performance acceptable
     - Inspection capacity adequate for FRP rate
     - Quality workforce trained and qualified
     - Nonconformance and CAPA processes effective
   - Go/No-Go decision to proceed with FRP based on FRRR

**LRIP-3 Quality Metrics:**

| Metric | Target | Actual (Tracked Monthly) |
|--------|--------|--------------------------|
| First-Time Quality (FTQ) | 97% | ___% |
| Process Cpk (critical characteristics) | ≥1.50 | ___ |
| Supplier Defect Rate (DPPM) | <500 | ___ |
| Customer Acceptance Rate | 99% | ___% |
| Scrap/Rework Rate | <2% | ___% |
| Internal Audit Findings (major) | Zero | ___ |

---

### 5.4 FRP Phase Quality Plan (PM 78-108+, Units 23+)

**Phase Objectives:**
- Maintain quality performance at high production rates
- Achieve cost reduction through quality improvement
- Sustain process control and continuous improvement culture
- Support customer field operations with responsive quality support

#### 5.4.1 FRP Phase 1 (24 Units/Year, Units 23-46)

**Quality Focus: Stabilization at Higher Rate**

**Key Activities:**

**1. Rate Transition Management**
   - Enhanced quality surveillance during rate ramp (daily production quality reviews)
   - Real-time quality metrics dashboards visible to production leadership
   - Rapid response quality team on standby for issues
   - Weekly quality performance reviews for first 3 months after rate increase

**2. Quality System Maturity**
   - Full SPC deployment (120+ characteristics monitored)
   - Automated data collection eliminates manual data entry
   - Predictive maintenance on inspection equipment (minimize downtime)
   - Lean manufacturing integration (quality at the source, visual management)

**3. Cost of Quality Optimization**
   - Track cost of quality (prevention, appraisal, internal failure, external failure)
   - Target: Reduce cost of quality by 20% vs. LRIP-3 (through defect prevention)
   - Shift resources from inspection to prevention activities

**4. Customer Support Readiness**
   - Establish field service quality support (24/7 hotline)
   - Warranty defect tracking and root cause analysis
   - Rapid response team for field quality issues
   - Proactive communication with customer quality on emerging issues

**FRP-1 Quality Metrics:**

| Metric | Target | Actual (Tracked Monthly) |
|--------|--------|--------------------------|
| First-Time Quality (FTQ) | 98% | ___% |
| Process Cpk (critical characteristics) | ≥1.67 | ___ |
| Supplier Defect Rate (DPPM) | <500 | ___ |
| Customer Acceptance Rate | 99.5% | ___% |
| Scrap/Rework Rate | <1% | ___% |
| Warranty Defects (first 90 days) | <2 per aircraft | ___ |

#### 5.4.2 FRP Phase 2 (48 Units/Year, Units 47+)

**Quality Focus: Sustained Excellence and Continuous Improvement**

**Key Activities:**

**1. World-Class Quality Performance**
   - Benchmark against aerospace industry best practices
   - Target: Top quartile performance in industry quality benchmarks
   - Six Sigma Black Belt deployment for complex problem-solving
   - Kaizen events (monthly) for targeted quality improvement

**2. Advanced Analytics and AI**
   - Machine learning algorithms for defect prediction
   - Automated anomaly detection in SPC data
   - Digital twin integration for virtual inspection and test
   - Blockchain for supply chain traceability (under evaluation)

**3. Supplier Partnership Excellence**
   - Supplier awards and recognition program
   - Joint cost reduction initiatives with strategic suppliers
   - Supplier-led innovation workshops
   - Supply chain transparency (real-time quality data sharing)

**4. Quality Culture Sustainment**
   - Quality excellence awards for employees
   - Quality metrics visible throughout factory (digital displays)
   - "Stop the Line" authority reinforced and celebrated
   - Continuous quality training and competency development

**FRP-2 Quality Metrics:**

| Metric | Target | Actual (Tracked Monthly) |
|--------|--------|--------------------------|
| First-Time Quality (FTQ) | 99% | ___% |
| Process Cpk (critical characteristics) | ≥1.67 | ___ |
| Supplier Defect Rate (DPPM) | <500 | ___ |
| Customer Acceptance Rate | 99.5% | ___% |
| Scrap/Rework Rate | <1% | ___% |
| Cost of Quality (% revenue) | <4% | ___% |

---

## 6. DESIGN ASSURANCE AND VERIFICATION

### 6.1 Requirements Management and Traceability

**Objective:** Ensure all design requirements are captured, traceable, verifiable, and verified.

**Requirements Management Tool:** [IBM DOORS, Jama Connect, or equivalent]

**Requirements Hierarchy:**

```
Program Requirements Baseline (PRB)
    └─ System Requirements Document (SRD)
        └─ Subsystem Specifications
            └─ Component Specifications
                └─ Supplier Specifications
```

**Quality Role in Requirements Management:**

1. **Requirements Review (Quality Gate):**
   - Review all requirements for:
     - **Completeness:** All aspects of functionality defined
     - **Clarity:** Unambiguous, single interpretation
     - **Verifiability:** Can be objectively verified (Test, Analysis, Inspection, Demonstration)
     - **Traceability:** Linked to parent requirement and verification method
   - Approve requirements before release to design

2. **Requirements Verification Matrix (RVM):**
   - Maintained in requirements tool with bidirectional traceability
   - Fields tracked:
     - Requirement ID and text
     - Parent requirement (traceability up)
     - Verification method (T/A/I/D)
     - Verification procedure reference
     - Verification status (not started / in work / complete / deferred)
     - Verification evidence (test report, analysis report, inspection record)
     - Responsible organization and engineer
   - Quality audits RVM monthly for completeness and accuracy

3. **Requirements Change Control:**
   - All requirements changes processed through Configuration Control Board (CCB)
   - Quality assesses verification impact of requirement changes:
     - Re-verification required?
     - Additional testing required?
     - Supplier impact (purchased item specification change)?
   - Quality approves verification plan update for changed requirements

**Requirements Quality Metrics:**

| Metric | Target |
|--------|--------|
| Requirements with Defined Verification Method | 100% |
| Requirements Traceability to Parent | 100% |
| Requirements Verified by CDR | 100% (Threshold Level) |
| Requirements Verified by First Flight | 100% (All Levels) |
| Ambiguous Requirements (per review) | Zero |

### 6.2 Design Review Process

**Design Review Governance:**

**Review Types:**
- **Formal Program Reviews:** SRR, PDR, CDR, TRR, FRR (defined in Section 5.2.1)
- **Subsystem Design Reviews:** Conducted by IPTs, Quality participates
- **Peer Reviews:** Engineering-led technical reviews, Quality spot-checks
- **Producibility Reviews:** Manufacturing-led reviews, Quality facilitates

**Quality Participation Matrix:**

| Review Type | Quality Participation | Quality Deliverables |
|-------------|----------------------|----------------------|
| Formal Program Reviews | Mandatory attendance, voting member | Quality assessment report, open issues list |
| Subsystem Design Reviews | Selective attendance (critical subsystems) | Design quality checklist |
| Peer Reviews | Not required (but may attend) | None (Engineering-led) |
| Producibility Reviews | Mandatory attendance | Manufacturing risk assessment, inspection planning |

**Design Review Quality Checklist (Excerpt):**

**General:**
- [ ] All requirements traceable and assigned verification methods
- [ ] Design FMEA complete for scope of review
- [ ] Hazard analysis complete (safety-critical systems)
- [ ] Configuration management processes defined
- [ ] Drawings and specifications IAW standards

**PDR-Specific:**
- [ ] Preliminary design feasible and meets requirements
- [ ] Technology readiness levels adequate (TRL ≥6 for critical tech)
- [ ] Manufacturing risk assessment complete
- [ ] Preliminary inspection and test plans reviewed

**CDR-Specific:**
- [ ] Design mature and ready for production
- [ ] All critical and key characteristics identified
- [ ] Process FMEAs complete
- [ ] Supplier selection complete, quality plans approved
- [ ] Final inspection and test plans approved
- [ ] First article inspection planning complete
- [ ] Software quality plans approved (if applicable)
- [ ] Certification plan approved (airworthiness)

**Action Item Management:**
- All design review actions logged with:
  - Action description
  - Responsible party
  - Due date
  - Criticality (Critical / Major / Minor)
  - Closure criteria
- Quality tracks action closure with verification evidence
- Critical and Major actions must close before next gate
- Monthly action review in Quality Steering Committee

### 6.3 Design FMEA and Hazard Analysis

**(Expanded from Section 5.2.2)**

**Design FMEA Process Flow:**

```
1. Define FMEA Scope (system, subsystem, component)
     ↓
2. Identify Functions and Requirements
     ↓
3. Identify Potential Failure Modes (how function can fail)
     ↓
4. Identify Potential Effects of Failure (impact on customer, safety)
     ↓
5. Assign Severity Ranking (1-10, based on effect)
     ↓
6. Identify Potential Causes of Failure (design deficiency, process variation)
     ↓
7. Assign Occurrence Ranking (1-10, based on likelihood)
     ↓
8. Identify Current Design Controls (how failure is prevented or detected)
     ↓
9. Assign Detection Ranking (1-10, based on control effectiveness)
     ↓
10. Calculate Action Priority (AP = S × O × D)
     ↓
11. Identify Recommended Actions (design change, process control, test)
     ↓
12. Assign Action Responsibility and Target Date
     ↓
13. Implement Actions and Update FMEA
     ↓
14. Verify Effectiveness (recalculate AP after action)
```

**FMEA Severity Ranking Criteria (Aerospace-Specific):**

| Rank | Severity | Criteria | Examples |
|------|----------|----------|----------|
| 10 | Catastrophic | Failure results in loss of aircraft or fatality | Primary structure failure, flight control loss |
| 9 | Hazardous | Failure results in major injury or severe aircraft damage | Landing gear collapse, engine fire |
| 8 | Major | Failure results in minor injury or significant damage, mission abort | Hydraulic system failure, avionics failure |
| 7 | Serious | Failure results in reduced safety margin, mission degradation | Backup system failure, reduced performance |
| 6 | Moderate | Failure results in unscheduled maintenance, mission impact | Accessory failure, sensor degradation |
| 5 | Low | Failure results in scheduled maintenance, minor inconvenience | Indicator light failure, minor discomfort |
| 4 | Minor | Failure results in minor defect noticed by most customers | Cosmetic defect, minor noise |
| 3 | Very Minor | Failure results in minor defect noticed by discriminating customers | Fit and finish issue |
| 2 | Slight | Failure results in very minor defect, most customers don't notice | Barely perceptible issue |
| 1 | None | No effect | No customer impact |

**Action Priority Thresholds:**

| AP Range | Action Required |
|----------|-----------------|
| AP ≥ 100 | **Mandatory action:** Design change or robust process control required before production |
| AP 50-99 | **Recommended action:** Consider design improvement or enhanced process control |
| AP < 50 | **Monitor:** Track in production, consider continuous improvement |

**Special Case: High Severity (S=9 or 10):**
- Regardless of AP score, all S=9 or S=10 failure modes require action to:
  - Eliminate failure mode (design change), OR
  - Reduce occurrence (design margin, redundancy), OR
  - Improve detection (inspection, test) to ensure zero escapes to flight

**Hazard Analysis Integration:**

**System Safety Assessment (SSA) per ARP4761:**
- Functional Hazard Assessment (FHA): System-level hazards identified
- Preliminary System Safety Assessment (PSSA): Preliminary safety requirements
- System Safety Assessment (SSA): Final safety requirements and verification

**Hazard Severity Classification:**

| Category | Effect | Probability Requirement |
|----------|--------|-------------------------|
| **Catastrophic (Cat I)** | Loss of aircraft, fatality | <10⁻⁹ per flight hour |
| **Hazardous (Cat II)** | Major injury, severe damage | <10⁻⁷ per flight hour |
| **Major (Cat III)** | Minor injury, significant damage | <10⁻⁵ per flight hour |
| **Minor (Cat IV)** | Nuisance, minor impact | No probability requirement |

**Quality Role in Hazard Analysis:**
- Review hazard analysis for completeness
- Verify safety-critical characteristics identified in design
- Ensure process controls implemented for safety-critical manufacturing
- Witness safety-critical verification tests
- Audit safety-critical inspection and test records

### 6.4 Producibility and Design for Manufacturing (DFM)

**Objective:** Ensure designs are manufacturable, inspectable, and cost-effective.

**Producibility Review Process:**

**Timing:**
- Preliminary Producibility Review: 30% design complete
- Final Producibility Review: 90% design complete (before CDR)
- Ongoing producibility input during design phase

**Participants:**
- Manufacturing Engineering
- Quality Engineering
- Tooling Engineering
- Supply Chain
- Cost Estimating

**Producibility Review Checklist:**

**General Design:**
- [ ] Design minimizes part count (modular design)
- [ ] Standard parts used where possible (fasteners, hardware)
- [ ] Tolerances appropriate for manufacturing capability (not over-toleranced)
- [ ] Assembly sequence feasible (no trapped assemblies)
- [ ] Access for tooling, inspection, and maintenance

**Composite Structures:**
- [ ] Layup feasible with available tooling (no undercuts)
- [ ] Ply drops and splices minimized
- [ ] Core placement and edge banding feasible
- [ ] Out-of-autoclave (OOA) curing compatible
- [ ] Inspection access for ultrasonic testing

**Metallic Fabrication:**
- [ ] Machining within CNC capability (no excessive setups)
- [ ] Forming feasible (bend radii, springback compensation)
- [ ] Welding/joining feasible with qualified processes
- [ ] Surface treatment and coating compatible

**Systems Installation:**
- [ ] Harness routing feasible (no interference)
- [ ] Connector access for assembly and maintenance
- [ ] Hydraulic/fuel line installation feasible
- [ ] Adequate space for systems integration

**Inspection and Test:**
- [ ] Critical dimensions measurable with standard tools
- [ ] Inspection access (no hidden features)
- [ ] Functional test points accessible
- [ ] Nondestructive testing (NDT) feasible

**Quality Input to Producibility:**
- Identify inspection challenges (measurement, access)
- Recommend design changes to improve inspectability
- Define critical and key characteristics requiring special control
- Review tolerance stack-ups for manufacturing capability

**Producibility Risk Assessment:**

| Risk Level | Criteria

## 6. DESIGN ASSURANCE AND VERIFICATION *(continued)*

### 6.4 Producibility and Design for Manufacturing (DFM) *(continued)*

**Producibility Risk Assessment:**

| Risk Level | Criteria | Response Action |
|------------|----------|-----------------|
| **High** | - Unproven manufacturing process<br>- Tight tolerances beyond demonstrated capability<br>- Complex assembly requiring >10 operations<br>- Single-source material/process | - Require manufacturing demonstration before CDR<br>- Design trade study for alternative approach<br>- Manufacturing Engineering approval required<br>- Supplier qualification program |
| **Medium** | - Established process, limited production history<br>- Tolerances at edge of capability (Cpk 1.0-1.33)<br>- Moderate assembly complexity<br>- Limited supplier base (2-3 sources) | - Early supplier engagement<br>- Process capability study before production release<br>- Inspection plan review<br>- Contingency sourcing identified |
| **Low** | - Proven manufacturing process<br>- Standard tolerances (Cpk >1.33)<br>- Simple assembly<br>- Multiple qualified suppliers | - Standard production release process<br>- Routine quality oversight |

**DFM Metrics and Targets:**

| Metric | Target | Notes |
|--------|--------|-------|
| Parts per Assembly (major assemblies) | ≤50% reduction vs. baseline concept | Modular design, part consolidation |
| Unique Part Numbers | ≤3,000 (total aircraft) | Part standardization across variants |
| Special Processes Required | ≤15 distinct process types | Limits qualification/training burden |
| Assembly Tools Required | Standard tooling >80% | Minimizes special tooling cost |
| Manufacturing Cycle Time | ≤18 months (green aircraft, FRP) | Critical path schedule driver |

### 6.5 Critical and Key Characteristics Management

**Definition of Terms:**

- **Critical Characteristic (CC):** A feature whose variation significantly affects product safety, performance, interchangeability, or regulatory compliance. Non-conformance requires Material Review Board (MRB) disposition and engineering approval.

- **Key Characteristic (KC):** A feature whose variation significantly affects product fit, function, or manufacturing process stability. Non-conformance may be dispositioned by Quality with Manufacturing/Engineering consultation.

#### 6.5.1 Critical Characteristics Identification Process

**Critical Characteristics shall be identified through:**

1. **Design FMEA:** Severity 9-10 failure modes with occurrence or detection concerns
2. **Safety Assessment:** Features affecting safety-critical functions (flight control, structural integrity, crashworthiness)
3. **Certification Requirements:** Features required for airworthiness compliance (FAA Part 29)
4. **Interface Control:** Features defining variant interfaces or assembly-to-assembly fit
5. **Regulatory Requirements:** Features subject to FAA/customer inspection or approval

**Critical Characteristics Designation:**

| Category | Symbol | Definition | Examples |
|----------|--------|------------|----------|
| **Flight Safety Critical** | ◊ (diamond) | Feature whose failure could result in loss of aircraft or fatality | Primary structure load paths, flight control actuator mounting, rotor blade attachment bolts |
| **Mission Critical** | ▲ (triangle) | Feature whose failure results in mission abort or severe degradation | Transmission housing, engine mounts, fuel system integrity |
| **Key Interchangeability** | ● (circle) | Feature defining part-to-part or assembly-to-assembly interfaces | Bolt hole patterns, mating surfaces, electrical connectors |

#### 6.5.2 Critical Characteristics Documentation

**Drawing Requirements:**
- All CCs and KCs identified on engineering drawings with appropriate symbol
- CC/KC features called out in drawing notes with specific inspection requirements
- Statistical process control (SPC) requirements identified where applicable
- First Article Inspection (FAI) required for all CC/KC features

**Process Control:**
- Manufacturing Process Control Plan (PCP) required for all CC features
- PCP defines:
  - In-process inspection points and methods
  - Process monitoring requirements (SPC charts)
  - Operator training and certification requirements
  - Tooling and equipment calibration intervals
  - Corrective action triggers (out-of-control conditions)

**Inspection Requirements:**

| Characteristic Type | Sampling Plan | Inspection Method | Acceptance Criteria |
|---------------------|---------------|-------------------|---------------------|
| **Flight Safety Critical** | 100% inspection | Documented inspection per procedure, independent verification | Zero defects, no deviations without MRB approval |
| **Mission Critical** | 100% or statistical sampling per MIL-STD-1916 | Standard inspection methods, may use automated inspection | Cpk ≥1.33 or 100% inspection |
| **Key Characteristics** | Statistical sampling (Normal Inspection Level II) | Standard methods | Cpk ≥1.33 or reduced sampling with demonstrated stability |

#### 6.5.3 Critical Characteristics Database

**Maintain centralized CC/KC database with:**
- Unique identifier for each characteristic
- Associated part number and drawing reference
- Characteristic classification (Flight Safety, Mission, Key)
- Nominal dimension and tolerance
- Measurement method and inspection frequency
- Process control requirements
- Responsible Quality Engineer
- Traceability to DFMEA or safety assessment
- Current process capability (Cpk) data

**Database updated:**
- At design release (initial population)
- Upon Engineering Change Order (ECO) affecting CC/KC
- Quarterly based on production data (Cpk updates)
- Annually during management review

### 6.6 Design Validation and Qualification Testing

#### 6.6.1 Qualification Test Strategy

**Objective:** Demonstrate that design meets all performance, environmental, and durability requirements before production release.

**Qualification Test Categories:**

| Test Category | Purpose | Typical Test Articles | Timing |
|---------------|---------|----------------------|--------|
| **Development Testing** | Prove design concept, identify issues early | Breadboard, brassboard, engineering models | Ongoing during design phase |
| **Qualification Testing** | Demonstrate compliance to requirements | Production-representative articles | Post-CDR, pre-production release |
| **Reliability Testing** | Demonstrate reliability allocation | Multiple production articles | LRIP phase with production units |
| **Certification Testing** | Demonstrate airworthiness compliance | Conforming production aircraft | Pre-Type Certificate |

#### 6.6.2 Structural Qualification

**Static Testing:**

| Test | Description | Article | Acceptance Criteria |
|------|-------------|---------|---------------------|
| **Limit Load Test** | Apply 100% design limit loads to all major load paths | Full-scale airframe test article | No permanent deformation, all structure returns to tolerance |
| **Ultimate Load Test** | Apply 150% design limit loads (ultimate load factor) | Same test article (after limit load test) | Structure withstands ultimate load for 3 seconds without catastrophic failure |
| **Crash Test** | Dynamic impact testing per MIL-STD-1290 | Full-scale fuselage section with seats/fuel system | Occupant injury criteria met, fuel system integrity maintained |

**Fatigue Testing:**

| Test | Description | Article | Acceptance Criteria |
|------|-------------|---------|---------------------|
| **Full-Scale Fatigue Test** | Apply simulated flight load spectrum for 2× design life (40,000 equivalent flight hours) | Production-representative airframe | No structural failure; crack growth within predictions; validate inspection intervals |
| **Component Fatigue Testing** | High-cycle fatigue testing of dynamic components | Rotor hubs, transmission gears, drive shafts | Meet 5,000 flight hour life requirement with 4× safety factor |

**Test Instrumentation:**
- 500+ strain gauges on critical load paths
- Deflection measurement (photogrammetry or laser tracking)
- Acoustic emission monitoring for crack detection
- Load cells at all primary load introduction points

**Quality Role in Structural Testing:**
- Verify test article configuration (correct revision, no nonconformances)
- Witness all qualification tests
- Review and approve test procedures
- Verify instrumentation calibration
- Review test data and reports
- Approve structural qualification closure in RVM

#### 6.6.3 Environmental Qualification Testing

**Per PRB Section 10.1 and Key Specifications Document Section 10:**

| Environmental Test | Standard | Test Levels | Test Article Type |
|-------------------|----------|-------------|-------------------|
| **Temperature (Operating)** | MIL-STD-810H, Method 501.6 | -40°C to +52°C (Objective) | Avionics LRUs, mission equipment |
| **Temperature (Storage)** | MIL-STD-810H, Method 501.6 | -54°C to +71°C | Sealed components, batteries |
| **Altitude** | MIL-STD-810H, Method 500.6 | -1,000 to +14,000 ft operating | Avionics, pressurized components |
| **Humidity** | MIL-STD-810H, Method 507.6 | 95% RH, +38°C, 10 days | Electronics, composite structure samples |
| **Salt Fog** | MIL-STD-810H, Method 509.6 | Class 2 (coastal/maritime) | Corrosion protection validation |
| **Sand and Dust** | MIL-STD-810H, Method 510.6 | Blowing sand, blowing dust | Engine inlet, avionics cooling, seals |
| **Vibration (Random)** | MIL-STD-810H, Method 514.7 | Helicopter vibration spectrum, 6 hr per axis | Avionics, mission systems |
| **Shock (Crash)** | MIL-STD-810H, Method 516.7 | 20 g terminal peak sawtooth, 11 ms | Avionics, emergency equipment |
| **EMI/EMC** | MIL-STD-464D | Direct strike (Zone 1A), HIRF (Category M) | Integrated aircraft (ground test and flight test) |

**Environmental Test Sequence (Combined Environment):**
1. Functional baseline test (room ambient)
2. Low temperature soak + functional test
3. High temperature soak + functional test
4. Humidity exposure + functional test
5. Altitude chamber test + functional test
6. Vibration (3 axes, 6 hr each)
7. Shock (3 axes, 3 shocks each)
8. Final functional test (room ambient)
9. Post-test teardown inspection

**Acceptance Criteria:**
- All functional parameters within specification during and after environmental exposure
- No degradation >10% of any performance parameter
- Visual inspection reveals no cracks, corrosion, or material degradation
- Post-test electrical insulation resistance meets minimum values

#### 6.6.4 Avionics and Software Qualification

**Hardware Qualification (per RTCA DO-254 for complex electronics):**

| Design Assurance Level | Applicable Systems | Qualification Requirements |
|------------------------|-------------------|---------------------------|
| **DAL A (Catastrophic)** | Flight control computers, autonomous GNC | Full DO-254 process, independent design review, extensive testing |
| **DAL B (Hazardous)** | Engine FADEC, primary displays | DO-254 process, design review, comprehensive testing |
| **DAL C (Major)** | Mission computers, secondary avionics | Reduced DO-254 rigor, focused testing |
| **DAL D (Minor)** | Non-essential mission systems | Standard commercial practices acceptable |

**Software Qualification (per RTCA DO-178C):**

| Software Function | Design Assurance Level | Lines of Code (approx.) | Verification Requirements |
|-------------------|------------------------|-------------------------|--------------------------|
| **Primary Flight Control Laws** | DAL A | 125,000 | 100% requirements-based testing, 100% statement coverage, 100% branch coverage, MC/DC analysis |
| **Autonomous GNC Core** | DAL A | 180,000 | Same as flight control; includes formal methods for safety-critical algorithms |
| **Engine Control (FADEC)** | DAL A/B (supplier responsibility) | 80,000 | Per engine OEM DO-178C certification |
| **Mission Management Software** | DAL C | 220,000 | Requirements-based testing, 100% statement coverage |
| **Ground Control Station Software** | DAL D | 350,000 | Standard software testing practices, not airborne software |

**Software Quality Assurance Activities (per Section 5.2.4):**
- Independence: SQA organization independent of software development
- Process audit: Verify compliance to Software Development Plan (SDP) and Software Configuration Management Plan (SCMP)
- Product audit: Review software requirements, design, code, test procedures, and test results
- Traceability audit: Verify requirements-to-code-to-test traceability
- Tool qualification: Qualify compilers, code generators, test tools per DO-178C Section 12
- Configuration audit: Verify software baseline integrity before release

**Software Qualification Completion Criteria:**
- 100% requirements verified (test or analysis)
- Structural coverage objectives met (per DAL)
- All problem reports closed or dispositioned (no open safety-critical issues)
- Software Accomplishment Summary (SAS) complete and approved
- Independent Software Quality Assurance audit findings closed
- Certification Authority (FAA) acceptance of software compliance

#### 6.6.5 Integrated System Testing

**Ground Test Phases:**

| Phase | Scope | Test Article | Duration |
|-------|-------|--------------|----------|
| **Iron Bird Testing** | Flight control system integration and functional testing (no flight loads) | Ground test rig with production flight control hardware, hydraulics, rotor heads (non-rotating) | 6 months, 1,000+ test hours |
| **Functional Ground Testing** | Complete aircraft systems integration (engines running, rotors turning, no flight) | Ground Test Vehicle (GTV) - first production-representative aircraft | 3 months, 200+ engine run hours |
| **Electromagnetic Compatibility (EMC) Testing** | Radiated and conducted emissions/immunity testing | GTV in anechoic chamber and outdoor ground plane | 4 weeks |
| **Autonomous Systems Ground Testing** | GNC algorithms, sensor fusion, DAA system validation (hardware-in-the-loop) | GTV with full mission systems, simulated environment | 4 months, 500+ test scenarios |

**Flight Test Phases:**

| Phase | Scope | Test Aircraft | Flight Hours (planned) |
|-------|-------|---------------|----------------------|
| **Initial Airworthiness (Phase I)** | Envelope expansion: build-up to VNE, altitude, load factor limits | FTA-1 (Flight Test Aircraft 1) | 150 hours |
| **Performance and Flying Qualities (Phase II)** | Verify performance KPPs, handling qualities per ADS-33 | FTA-1, FTA-2 | 200 hours |
| **Mission Systems (Phase III)** | Autonomous operations, DAA system, mission equipment validation | FTA-2, FTA-3 (mission-equipped) | 100 hours |
| **Reliability and Maintainability (Phase IV)** | Integrated testing with production aircraft, MTBF validation | LRIP Units 1-4 | 500+ hours (fleet data) |
| **Certification (Phase V)** | FAA conformity flights, final compliance demonstration | Conforming production aircraft | 50 hours |

**Total Flight Test Program:** 1,000+ flight hours across development and certification phases

**Quality Role in Ground and Flight Testing:**
- Approve test procedures (safety review, compliance with test plan)
- Witness first-of-type tests and safety-critical tests
- Monitor test configuration control (ensure correct baseline, no unapproved modifications)
- Review test data for anomalies or non-conformances
- Participate in test readiness reviews and flight readiness reviews
- Verify test completion and requirements closure in RVM
- Audit test records and documentation for completeness

### 6.7 Configuration Audits

**Configuration audits verify that as-built product matches approved design documentation and meets all specified requirements.**

#### 6.7.1 Functional Configuration Audit (FCA)

**Purpose:** Verify that product performance meets all requirements as documented in specifications.

**Timing:** 
- Component/subsystem level: Prior to production release (post-qualification testing)
- Aircraft level: Prior to Type Certificate application (certification aircraft)

**FCA Process:**
1. **Audit Planning:** Define audit scope, schedule, participants (30 days prior)
2. **Documentation Review:** Verify all test reports, analysis reports, inspection records available
3. **Requirements Verification Review:** Review RVM for completeness (100% closure)
4. **Discrepancy Resolution:** Identify and resolve any open issues, deviations, or waivers
5. **Audit Report:** Document findings, approved deviations, compliance statement
6. **Approval:** Quality Director and Chief Engineer sign-off; Customer representative concurrence

**FCA Success Criteria:**
- 100% of Threshold requirements verified (Test, Analysis, Inspection, or Demonstration)
- All Critical (Safety) requirements verified by Test or Analysis (not by Inspection alone)
- No open major nonconformances affecting safety or performance
- All approved deviations documented with rationale and impact assessment
- All test articles configuration-controlled and traceable to production baseline

#### 6.7.2 Physical Configuration Audit (PCA)

**Purpose:** Verify that as-built product matches approved engineering drawings, specifications, and BOMs.

**Timing:**
- First Article: After First Article Inspection (FAI) and prior to production release
- Production aircraft: Prior to customer delivery (final acceptance inspection)
- Post-modification: After any major engineering change or retrofit

**PCA Process:**
1. **Drawing Tree Review:** Verify all drawings released and at correct revision
2. **BOM Verification:** Confirm all installed parts match approved BOM (part number, serial number, revision)
3. **Physical Inspection:** Visual and dimensional inspection of critical features, interfaces, and installations
4. **Marking and Labeling:** Verify data plates, safety labels, maintenance markings per specification
5. **Software Load Verification:** Confirm correct software versions installed (checksum verification)
6. **Discrepancy Disposition:** Resolve any as-built vs. as-designed discrepancies (ECO or deviation)
7. **Audit Report:** Document configuration baseline, approved differences, acceptance recommendation
8. **Approval:** Quality Manager sign-off; customer representative witness (as applicable)

**PCA Inspection Sample (Aircraft Level):**
- 100% of major assemblies (fuselage, rotor system, transmission, engines)
- 100% of safety-critical installations (flight controls, fuel system, crashworthy structure)
- 10% sample of electrical harnesses (connector torque, routing, labeling)
- 100% of external interfaces (cargo hooks, mission equipment mounts, ground service points)
- 100% of data plates and markings

**PCA Success Criteria:**
- Zero discrepancies between as-built configuration and engineering baseline
- All deviations properly documented and approved before audit
- All serialized components recorded in aircraft configuration record
- Software versions match approved release (no unauthorized software loads)
- Aircraft logbook entries complete and accurate

#### 6.7.3 Configuration Audit Records

**Records maintained for each configuration audit:**
- Audit plan and checklist
- Requirements Verification Traceability Matrix (RVM) status report (FCA)
- Drawing tree and BOM verification report (PCA)
- Audit findings log with disposition
- Approved deviations and waivers list
- Audit report with approval signatures
- Photographic evidence (as applicable)

**Record Retention:** Minimum 10 years after aircraft retirement or end of service life

---

## 7. MANUFACTURING QUALITY CONTROL

### 7.1 Manufacturing Quality Philosophy

**Core Principles:**

1. **Quality at the Source:** Empower manufacturing operators to identify and stop defects at the point of origin; operators are first line of defense.

2. **Prevention Over Detection:** Design processes to prevent defects rather than relying solely on inspection to find them.

3. **Statistical Process Control:** Use real-time data to monitor process stability and trigger corrective action before defects occur.

4. **Right First Time:** Build quality into manufacturing processes through planning, training, and process validation; minimize rework and scrap.

5. **Continuous Improvement:** Systematically analyze quality data, implement improvements, and drive cost and schedule performance through quality excellence.

### 7.2 Manufacturing Process Control

#### 7.2.1 Process Control Plan (PCP) Requirements

**Mandatory for:**
- All processes producing Critical or Key Characteristics
- Special processes (welding, bonding, heat treat, NDT, coating)
- New or unproven manufacturing processes
- Processes with historical quality issues (Cpk <1.33 or defect rate >1,000 DPPM)

**PCP Content (per AIAG/AS9145 APQP methodology):**

| Section | Content | Owner |
|---------|---------|-------|
| **Process Description** | Process flow diagram, equipment list, tooling requirements | Manufacturing Engineering |
| **Input Requirements** | Material specifications, incoming part requirements, environmental conditions | Quality Engineering |
| **Process Parameters** | Critical process variables (temperature, pressure, time, etc.) with control limits | Manufacturing Engineering |
| **Control Methods** | In-process inspection points, SPC charts, automated monitoring | Quality Engineering |
| **Measurement Systems** | Gages, fixtures, measurement procedures, calibration frequency | Quality Engineering |
| **Sampling Plans** | Inspection frequency, sample size, acceptance criteria (per MIL-STD-1916 or AS9145) | Quality Engineering |
| **Reaction Plans** | Out-of-control conditions, corrective actions, escalation procedures | Manufacturing + Quality |
| **Operator Instructions** | Work instructions, setup procedures, inspection criteria | Manufacturing Engineering |
| **Training Requirements** | Operator qualification, certification requirements, retraining intervals | Manufacturing + Quality |

**PCP Approval:**
- Developed by Manufacturing Engineering with Quality Engineering input
- Approved by Manufacturing Quality Manager before process validation
- Updated whenever process changes, equipment changes, or quality issues arise
- Annual review for currency

#### 7.2.2 First Article Inspection (FAI)

**Purpose:** Verify that manufacturing processes are capable of producing conforming product before full-rate production begins.

**FAI Scope (per AS9102):**
- All new part numbers introduced to production
- All manufacturing processes (machining, forming, composites, assembly, etc.)
- All Tier 1 supplier-produced parts and assemblies
- Any process change affecting form, fit, or function

**FAI Execution:**

| Step | Activity | Responsibility | Deliverable |
|------|----------|----------------|-------------|
| 1 | Produce FAI sample using production tooling, processes, and operators | Manufacturing | FAI sample part/assembly |
| 2 | Perform 100% dimensional inspection of all characteristics per drawing | Quality Inspection | AS9102 Form 3 (inspection results) |
| 3 | Perform functional testing per acceptance test procedure | Quality Engineering | Test report |
| 4 | Verify material certifications and process certifications | Quality Engineering | Material traceability |
| 5 | Complete AS9102 Forms 1 (Index), 2 (Accountability), 3 (Results) | Quality Engineering | FAI package |
| 6 | Review FAI package for completeness and compliance | Manufacturing Quality Manager | Approval signature |
| 7 | Disposition: Pass / Pass with deviation / Fail | Manufacturing Quality Manager | Production release or corrective action |

**FAI Acceptance Criteria:**
- 100% of characteristics within drawing tolerance
- All Critical and Key Characteristics meet Cpk ≥1.33 (minimum 30 samples for Cpk calculation)
- Functional tests pass with no anomalies
- Material and process certifications complete and compliant
- No safety-related discrepancies

**FAI Failure Response:**
- **Minor deviation (non-critical characteristic):** Manufacturing disposition with Engineering concurrence; may proceed with production under deviation
- **Major deviation (critical/key characteristic):** Stop production; initiate root cause analysis and corrective action; re-run FAI after correction
- **Functional test failure:** Stop production; Engineering investigation required; re-run FAI after design or process correction

**FAI Records Retention:** Permanent (life of program); available for customer/auditor review

#### 7.2.3 Process Validation and Capability Studies

**Process Capability Metrics:**

- **Cp (Process Capability Index):** (USL - LSL) / 6σ
  - Measures inherent process capability (assumes process centered on nominal)
  
- **Cpk (Process Capability Index, accounting for centering):** min[(USL - μ)/3σ, (μ - LSL)/3σ]
  - Measures actual process capability considering process mean offset

**Process Capability Targets:**

| Phase | Target Cpk | Notes |
|-------|------------|-------|
| **LRIP-1** | ≥1.33 | Acceptable for early production; requires 100% inspection if not met |
| **LRIP-3** | ≥1.50 | Demonstrating process maturity |
| **FRP** | ≥1.67 | World-class capability; enables reduced inspection |

**Process Validation Requirements:**

| Process Type | Sample Size (minimum) | Validation Method | Acceptance Criteria |
|--------------|----------------------|-------------------|---------------------|
| **Critical Characteristics** | 30 consecutive parts | Statistical analysis (Cpk calculation) | Cpk ≥1.33 (LRIP), ≥1.67 (FRP) |
| **Special Processes** | Per process specification | Process parameter monitoring + product testing | 100% pass rate, parameters within control limits |
| **Automated Processes** | 50 parts (machine capability study) | Automated data collection, control charts | Cpk ≥1.67, zero out-of-control conditions |

**Process Not Capable (Cpk <1.33):**
- **Short-term response:** Increase inspection frequency to 100% until capability improved
- **Long-term response:** Initiate process improvement project (Six Sigma DMAIC methodology)
  - Define: Characterize problem (defect rate, cost impact)
  - Measure: Collect detailed process data (temperature, pressure, setup, operator, etc.)
  - Analyze: Identify root causes (variation sources, equipment issues, training gaps)
  - Improve: Implement corrective actions (equipment upgrade, process optimization, tooling modification)
  - Control: Implement SPC, update PCP, verify sustained improvement
- **Target timeline:** Cpk ≥1.33 within 3 months or escalate to Quality Steering Committee for resource support

### 7.3 In-Process Inspection and Testing

#### 7.3.1 Inspection Planning

**Inspection and Test Plan (ITP) Requirements:**
- Developed during manufacturing planning (concurrent with PCP)
- Identifies all inspection points, methods, acceptance criteria
- Defines inspection frequency (100%, sampling, first/last piece)
- Specifies inspection equipment and measurement uncertainty
- Approved by Manufacturing Quality Manager before production release

**Inspection Point Selection Criteria:**

| Priority | Inspection Point | Rationale |
|----------|------------------|-----------|
| 1 | After operations affecting Critical Characteristics | Safety and airworthiness assurance; zero tolerance for escapes |
| 2 | After irreversible or concealing operations | Verification before feature becomes inaccessible (e.g., before closeout panels, bonding) |
| 3 | After Key Characteristics | Interchangeability and fit assurance |
| 4 | At final assembly stage | Final verification before next assembly level |
| 5 | At natural hold points | Between shifts, before transfer to next workstation |

**Inspection Types:**

| Type | Description | Application |
|------|-------------|-------------|
| **Source Inspection** | Operator self-inspection, documented on traveler | Non-critical operations; operator-certified for inspection |
| **In-Process Inspection** | Quality inspector verification during manufacturing | Critical/Key Characteristics; special processes; first article |
| **Final Inspection** | Independent Quality inspection at completion | All deliverable parts/assemblies before acceptance |
| **Receiving Inspection** | Inspection of purchased items upon receipt | Supplier-provided parts, raw materials |

#### 7.3.2 Inspection Methods and Equipment

**Dimensional Inspection:**

| Method | Application | Typical Tolerance Range | Equipment |
|--------|-------------|------------------------|-----------|
| **Hand Tools (calipers, micrometers)** | General dimensions, non-critical features | ±0.005" to ±0.030" | Calibrated hand gages |
| **Height Gages / Surface Plate** | Precision dimensions, vertical measurements | ±0.001" to ±0.010" | Granite surface plate, height gage |
| **Coordinate Measuring Machine (CMM)** | Complex geometry, tight tolerances, 3D features | ±0.0005" to ±0.005" | Bridge-type CMM with touch probe |
| **Laser Scanning / Photogrammetry** | Large structures, contour verification, full-field measurement | ±0.010" to ±0.050" | Portable laser tracker, structured light scanner |
| **Optical Comparator** | Small parts, profile verification, 2D features | ±0.0005" to ±0.002" | Optical comparator with digital readout |

**Non-Destructive Testing (NDT):**

| Method | Application | Detectability | Equipment | Operator Qualification |
|--------|-------------|---------------|-----------|------------------------|
| **Visual Inspection (VT)** | Surface defects, cracks, corrosion, FOD | Surface only, >0.010" features | Borescope, magnifying glass, proper lighting | NDT Level I or II per ASNT SNT-TC-1A |
| **Liquid Penetrant (PT)** | Surface-breaking cracks in non-porous materials | 0.001" crack opening | Dye penetrant, developer, UV light | NDT Level II |
| **Magnetic Particle (MT)** | Surface and near-surface cracks in ferromagnetic materials | Surface to 0.010" deep | Magnetic yoke, iron powder, UV light | NDT Level II |
| **Ultrasonic Testing (UT)** | Internal defects, voids, delaminations (composites), thickness measurement | 0.050" flaw size (typical) | UT flaw detector, transducers | NDT Level II or III |
| **Radiographic Testing (RT)** | Internal defects, porosity, inclusions (castings, welds) | 2% thickness sensitivity (typical) | X-ray or gamma-ray source, film/digital detector | NDT Level II or III |
| **Eddy Current (ET)** | Surface and near-surface cracks, material conductivity variations | 0.010" crack depth | Eddy current instrument, probes | NDT Level II |

**NDT Procedure Qualification:**
- All NDT procedures qualified per ASNT SNT-TC-1A or NAS-410
- Procedure qualification includes: sensitivity demonstration, repeatability study, operator qualification test
- Procedures reviewed and approved by NDT Level III and Quality Engineering
- Procedures updated whenever process, equipment, or material changes

#### 7.3.3 Functional Testing

**Acceptance Test Procedures (ATP):**

| Test Type | Scope | Acceptance Criteria | Frequency |
|-----------|-------|---------------------|-----------|
| **Component Functional Test** | Verify component operation per specification (actuators, valves, pumps, avionics LRUs) | All functions operate within specified limits; no anomalies | 100% of serialized components |
| **Subsystem Integration Test** | Verify subsystem integration and interfaces (hydraulic system, electrical system, flight controls) | End-to-end functionality verified; interface parameters nominal | 100% of aircraft (ground test phase) |
| **Power-On System Test** | Verify all aircraft systems with engines running, rotors turning (no flight) | All systems operational; Built-In Test (BIT) passes; no fault codes | 100% of aircraft (functional ground test) |
| **Pre-Delivery Flight Test** | Functional check flight before customer delivery | All flight systems operational; handling qualities acceptable; no discrepancies | 100% of production aircraft |

**Automated Test Equipment (ATE):**
- Deployed in FRP phase to reduce test time and improve repeatability
- ATE provides go/no-go results with data logging for trend analysis
- ATE calibration and software verification per Quality procedure
- Operator training required before ATE operation

**Test Failure Response:**
- Document test failure in nonconformance system (Section 9)
- Troubleshoot and identify root cause (component failure, setup error, test equipment issue)
- Replace or repair component; re-test to verify correction
- Trend test failures monthly; initiate reliability improvement if failure rate exceeds allocation

### 7.4 Statistical Process Control (SPC)

#### 7.4.1 SPC Deployment Strategy

**Phase-Based SPC Rollout:**

| Phase | SPC Characteristics Monitored | SPC Tools Deployed | Workforce Training |
|-------|-------------------------------|--------------------|--------------------|
| **LRIP-1** | 15 most critical characteristics (pilot program) | Manual control charts (X-bar/R charts on shop floor) | Quality Engineers + lead operators (40 hrs) |
| **LRIP-2** | 50 critical and key characteristics | Semi-automated data collection (digital calipers, SPC software) | All operators in pilot areas (8 hrs) |
| **LRIP-3** | 120 characteristics across all major assemblies | Fully automated data collection and charting (integrated with MES) | All production operators (8 hrs initial + 4 hrs annual) |
| **FRP** | 200+ characteristics; real-time monitoring | Predictive analytics, automated alerts, digital dashboards | Continuous improvement culture: all employees |

#### 7.4.2 SPC Chart Types and Applications

| Chart Type | Application | Data Type | Control Limits |
|------------|-------------|-----------|----------------|
| **X-bar/R Chart (Individuals and Range)** | Continuous data (dimensions, torque, pressure, etc.) | Variable (measured) | ±3 sigma from process mean |
| **p-Chart (Proportion Defective)** | Defect rates, pass/fail data (e.g., % parts rejected) | Attribute (count) | Based on binomial distribution |
| **c-Chart (Count of Defects)** | Number of defects per unit (e.g., FOD incidents per aircraft) | Attribute (count) | Based on Poisson distribution |
| **CUSUM (Cumulative Sum)** | Detecting small shifts in process mean over time | Variable (measured) | Decision interval (h) and reference value (k) |
| **EWMA (Exponentially Weighted Moving Average)** | Detecting small to moderate shifts, smoothing noisy data | Variable (measured) | Weighted control limits based on lambda (λ) |

**SPC Chart Selection:**
- **X-bar/R Chart:** Most common for dimensional data; monitors both process mean (X-bar) and process variation (R)
- **p-Chart:** Use when tracking defect rates (e.g., % of parts out of tolerance)
- **c-Chart:** Use when tracking defect counts per unit (e.g., number of FOD incidents per inspection)
- **CUSUM / EWMA:** Advanced charts for early detection of process shifts; used in FRP phase for critical processes

#### 7.4.3 Control Chart Interpretation and Reaction

**Out-of-Control Conditions (per Western Electric Rules):**

| Rule | Condition | Interpretation | Action |
|------|-----------|----------------|--------|
| **Rule 1** | Any point beyond ±3 sigma control limits | Special cause variation; process out of control | **Immediate:** Stop process, identify cause, correct, resume after verification |
| **Rule 2** | 2 of 3 consecutive points beyond ±2 sigma (same side) | Process shifting; possible special cause | **Within shift:** Investigate cause, adjust process if needed, monitor closely |
| **Rule 3** | 4 of 5 consecutive points beyond ±1 sigma (same side) | Process mean shifting; tool wear or setup drift | **Within shift:** Investigate and correct; may indicate need for process adjustment |
| **Rule 4** | 8 consecutive points on same side of centerline | Sustained process shift; systematic change | **Within shift:** Identify root cause (new operator, material lot, tool change), correct |
| **Rule 5** | 15 consecutive points within ±1 sigma (both sides) | Process variability reduced (good) OR stratified data (bad) | Investigate: confirm real improvement or check for measurement/sampling error |
| **Rule 6** | 14 consecutive points alternating up and down | Systematic oscillation; possible measurement system issue | Investigate measurement system, process setup, or material variation |
| **Rule 7** | 8 consecutive points beyond ±1 sigma (either side) | Increased process variation; possible special cause | Investigate cause of increased variation; may require process re-validation |

**Reaction Plan (Out-of-Control Conditions):**

1. **Immediate Actions (within 15 minutes):**
   - Tag affected parts/assemblies "HOLD - SPC Out of Control"
   - Notify Quality Engineer and Manufacturing Supervisor
   - Initiate investigation (5 Whys, Fishbone diagram)
   
2. **Short-Term Containment (within 4 hours):**
   - Identify root cause (equipment, material, method, operator, environment)
   - Implement immediate correction (adjust process, replace tool, retrain operator)
   - Verify correction with 5 consecutive conforming parts
   - Disposition held parts (inspect 100%, sort conforming from non-conforming)
   
3. **Long-Term Corrective Action (within 2 weeks):**
   - Document root cause in CAPA system (Section 9.2)
   - Implement permanent corrective action (equipment upgrade, process change, training)
   - Update Process Control Plan to prevent recurrence
   - Verify effectiveness (monitor SPC chart for 30 days, confirm no recurrence)

#### 7.4.4 Process Capability Monitoring

**Capability Studies Frequency:**

| Process Status | Cpk Study Frequency | Sample Size | Trigger for Re-Study |
|----------------|---------------------|-------------|----------------------|
| **New Process (initial validation)** | After 30 parts produced | 30 parts (minimum) | N/A (initial study) |
| **Capable Process (Cpk ≥1.67)** | Quarterly | 50 parts | Any process change, SPC out-of-control for >1 week |
| **Marginally Capable (1.33 ≤ Cpk <1.67)** | Monthly | 50 parts | Any process change, SPC out-of-control condition |
| **Not Capable (Cpk <1.33)** | Weekly (during improvement) | 30 parts | After each process improvement iteration |

**Cpk Improvement Initiatives:**

**Target:** All Critical and Key Characteristics achieve Cpk ≥1.67 by FRP Phase 1.

**Improvement Methodology:**
1. **Prioritize characteristics:** Focus on lowest Cpk values first (highest defect risk)
2. **Multi-Vari Study:** Identify variation sources (within-piece, piece-to-piece, time-to-time, setup-to-setup)
3. **Design of Experiments (DOE):** Optimize process parameters (speeds, feeds, temperatures, etc.)
4. **Mistake-Proofing (Poka-Yoke):** Implement error-proofing devices (fixtures, sensors, interlocks)
5. **Verify Improvement:** Re-run capability study after changes; confirm Cpk improvement sustained for 30 days

**Continuous Improvement Target:** Improve Cpk by average of 0.10 per quarter during LRIP phase.

### 7.5 Production Acceptance and Delivery

#### 7.5.1 Final Inspection

**Final Inspection Scope (100% of aircraft):**

**Structural Integrity:**
- Fuselage structure: No cracks, dents, or damage exceeding limits
- Rotor blades: Blade tracking within ±0.5 in, no damage, balance within limits
- Landing gear: Proper extension/retraction, no leaks, torque values recorded
- All fasteners: Proper installation, safety wiring, torque seals intact

**Systems Functionality:**
- Flight control systems: Full range of motion, no binding, control rigging within tolerance
- Hydraulic systems: Pressure test passed, no leaks, fluid level and condition acceptable
- Electrical systems: Continuity checks passed, no shorts, proper bonding and grounding
- Fuel system: Leak test passed, fuel quantity indication accurate, cross-feed operation verified
- Propulsion: Engine runs completed, no anomalies, all parameters within limits

**Mission Systems (Variant-Specific):**
- MAAP-1C: Cargo hook operation verified, load monitoring system functional
- MAAP-1I: EO/IR turret operation verified, video downlink functional
- MAAP-1F: Water/retardant tank tested (leak check, drop system functional)

**Configuration Verification:**
- Serial number and data plate verification (correct aircraft serial number, model, registration)
- Drawing and BOM verification (all parts installed match approved configuration)
- Software load verification (correct versions installed, checksum verified)
- Logbook review (all maintenance entries complete, discrepancies cleared)
- Customer-furnished equipment (GFE) installed and functional (if applicable)

**Final Inspection Checklist Approval:**
- Inspected by: Quality Inspector (certified)
- Reviewed by: Manufacturing Quality Manager
- Accepted by: Quality Director or Delegate
- Customer Witness: (signature if customer acceptance inspection required)

**Final Inspection Pass Rate Targets:**

| Phase | First-Time Pass Rate | Notes |
|-------|----------------------|-------|
| **LRIP-1** | ≥95% | Learning curve; accept some rework |
| **LRIP-3** | ≥98% | Processes maturing |
| **FRP** | ≥99.5% | Stable production; minimal discrepancies |

**Final Inspection Failure:**
- If discrepancies found: Tag aircraft "HOLD - FINAL INSPECTION DISCREPANCY"
- Document discrepancies in nonconformance system
- Disposition by Engineering and Quality (repair, rework, or use-as-is with deviation)
- Re-inspect after correction
- No aircraft released to customer with open discrepancies

#### 7.5.2 Pre-Delivery Flight Test

**Purpose:** Functional check flight to verify all systems operate correctly in flight environment before customer acceptance.

**Pre-Delivery Flight Test Profile (all production aircraft):**

| Phase | Duration | Maneuvers / Checks | Acceptance Criteria |
|-------|----------|-------------------|---------------------|
| **Pre-Flight** | 30 min | Ground systems check, weight & balance verification | All systems operational, BIT passed |
| **Hover Check** | 10 min | Hover OGE, control response check, vibration check | Smooth operation, vibration within limits, no anomalies |
| **Transition to Forward Flight** | 5 min | Accelerate to 80 KTAS, trim check | Smooth transition, controllable, no unusual vibrations |
| **Cruise Flight** | 20 min | Cruise at 120 KTAS, avionics check, autopilot engagement | All systems functional, autopilot holds altitude/heading |
| **Maneuvering** | 10 min | Turns (±30° bank), climbs, descents | Responsive controls, no anomalies, G-load within limits |
| **Autonomous Systems Check** | 15 min | Engage autonomous mode, waypoint navigation, DAA system test (if traffic available) | Autonomous mode transitions smoothly, waypoint navigation accurate, DAA alerts functional |
| **Landing** | 5 min | Approach and landing | Smooth approach, landing within touchdown zone, no anomalies |
| **Post-Flight** | 15 min | Post-flight inspection, logbook entry | No damage, no leaks, discrepancies documented |

**Total Flight Duration:** ~75 minutes

**Pre-Delivery Flight Acceptance Criteria:**
- All systems operate within normal parameters (no cautions or warnings)
- Handling qualities acceptable (pilot evaluation: satisfactory or better)
- Vibration levels within specification (<0.2 in/sec at all flight conditions)
- Autonomous systems functional (if applicable to variant)
- No maintenance discrepancies discovered during post-flight inspection

**Pre-Delivery Flight Failure:**
- If discrepancies found: Aircraft returns to hangar for troubleshooting and repair
- Document discrepancies in nonconformance system
- Re-flight required after repair (repeat discrepant portion of flight profile)
- No aircraft delivered to customer until pre-delivery flight successfully completed

#### 7.5.3 Customer Acceptance Process

**Acceptance Options:**

| Option | Description | Customer Involvement | Typical Timeline |
|--------|-------------|---------------------|------------------|
| **Source Acceptance (at factory)** | Customer representative witnesses final inspection and pre-delivery flight | Customer QA representative on-site; signs acceptance certificate | 2-3 days at factory before delivery |
| **Destination Acceptance** | Customer accepts aircraft after delivery to customer facility | Eurus delivers aircraft; customer conducts acceptance inspection at destination | 1 week after delivery |
| **Certificate of Conformance (CoC)** | Customer accepts based on Eurus-provided documentation without witness | No customer on-site; relies on Eurus Quality system | Certificate issued at delivery |

**Source Acceptance Process (most common for government/military customers):**

1. **Notification (T-30 days):** Eurus notifies customer of planned delivery date; provides preliminary acceptance data package
2. **Pre-Acceptance Review (T-7 days):** Customer reviews acceptance data package (test reports, inspection records, logbooks)
3. **Customer Inspection (T-2 days):** Customer QA representative arrives at factory; conducts acceptance inspection
4. **Acceptance Flight (T-1 day):** Customer representative flies on pre-delivery flight (or observes from chase aircraft)
5. **Acceptance Decision (T-0):** Customer signs DD Form 250 (Material Inspection and Receiving Report) or equivalent acceptance document
6. **Delivery (T-0):** Aircraft ownership transfers; Eurus ferries aircraft to customer location or customer flies away

**Acceptance Data Package Contents:**
- Aircraft configuration record (drawing tree, BOM, serial numbers)
- Final inspection checklist (signed)
- Pre-delivery flight test report (signed by pilot and Quality)
- Test and inspection summary (summary of all production acceptance tests)
- Material certifications (engine, transmission, critical components)
- Weight and balance report (as-weighed, current configuration)
- Logbooks (airframe, engine, component logs)
- Flight manual and maintenance manuals (approved revisions)
- FAA Type Certificate Data Sheet (or military equivalent)
- Warranty documentation

**Customer Acceptance Rejection:**
- If customer rejects aircraft: Document rejection reason; initiate corrective action
- Eurus has 30 days to correct discrepancies and re-present aircraft for acceptance
- If correction not feasible within 30 days: Negotiate delivery schedule extension or substitute aircraft
- **Program Goal:** Zero customer rejections at final acceptance by FRP phase

#### 7.5.4 Delivery Quality Metrics

**Tracked Monthly and Reported to Quality Steering Committee:**

| Metric | Target (FRP) | Definition |
|--------|--------------|------------|
| **Customer Acceptance Rate** | ≥99.5% | % of aircraft accepted by customer on first presentation |
| **Delivery Discrepancies per Aircraft** | <5 | Number of minor discrepancies noted by customer at acceptance (accepted with open items) |
| **Pre-Delivery Flight Defects** | <2 per aircraft | Number of discrepancies discovered during pre-delivery flight |
| **On-Time Delivery Performance** | ≥95% | % of aircraft delivered within ±7 days of contract delivery date |
| **Delivery Documentation Completeness** | 100% | % of aircraft delivered with complete acceptance data package (no missing documents) |

### 7.6 Special Processes Control

**Definition:** Special processes are manufacturing processes where conformance to requirements cannot be fully verified by inspection of the finished product (e.g., welding, adhesive bonding, heat treatment, NDT, coating). Quality of these processes depends on process control rather than product inspection.

#### 7.6.1 Qualified Special Processes (MAAP-1 Program)

| Process | Application | Qualification Standard | Re-Qualification Frequency |
|---------|-------------|------------------------|---------------------------|
| **Welding (GTAW, GMAW)** | Metallic structure, engine mounts, fittings | AWS D17.1 (Fusion Welding for Aerospace) | Annual (welders), Whenever procedure changes (process) |
| **Adhesive Bonding** | Composite structure, honeycomb sandwich panels | ASTM D5868 (Lap Shear Adhesion) | Quarterly (process validation), Annual (operator certification) |
| **Heat Treatment** | Steel forgings, aluminum alloy parts (T6 temper) | AMS2750 (Pyrometry), AMS2759 (Heat Treatment) | Semi-annual (equipment/instrumentation), Whenever equipment changes |
| **Non-Destructive Testing (NDT)** | All critical structure and components | ASNT SNT-TC-1A or NAS-410 | Annual (NDT personnel certification), Whenever procedure changes |
| **Chemical Processing (Anodize, Alodine, Passivate)** | Aluminum and steel corrosion protection | MIL-A-8625 (Anodizing), MIL-DTL-5541 (Chem Film) | Quarterly (process baths validation), Whenever chemistry changes |
| **Painting/Coating** | Exterior paint, corrosion protection topcoat | MIL-PRF-85285 (Polyurethane Coating) | Annual (operator qualification), Whenever paint system changes |
| **Composite Fabrication (Layup, Cure)** | Primary and secondary composite structure | Internal specification AF-MAAP1-SPEC-COMP-001 | Quarterly (oven validation), Annual (layup operator certification) |

#### 7.6.2 Special Process Qualification Requirements

**Process Qualification:**
- Demonstrate process capability using production equipment, materials, and operators
- Produce qualification coupons or test articles; perform destructive and non-destructive testing
- Document process parameters (temperature, pressure, time, materials) and acceptable ranges
- Achieve test results meeting or exceeding specification requirements
- Quality Engineer approval required before production use

**Operator/Technician Certification:**
- Classroom training on process theory, procedures, and acceptance criteria
- Hands-on training under supervision of certified operator
- Practical examination (produce acceptable parts/coupons under observation)
- Written examination (process knowledge, specifications, quality requirements)
- Certification issued by Quality Training Coordinator; valid for 1-2 years depending on process
- Annual recertification required (practical exam + refresher training)

**Equipment and Tooling Qualification:**
- Calibration of all process control instruments (thermocouples, pressure gages, timers, ovens)
- Validation of equipment performance (temperature uniformity surveys for ovens, pull testing for welding equipment)
- Periodic re-validation (quarterly to annually depending on process criticality)
- Equipment out-of-calibration: Stop production; re-validate equipment; disposition affected parts (inspection or scrap)

#### 7.6.3 Welding Process Control

**Welding Procedures:**
- All welding performed per approved Welding Procedure Specifications (WPS) qualified per AWS D17.1
- WPS defines: Base materials, filler materials, welding process, joint design, preheat/interpass temperature, post-weld heat treatment, inspection requirements
- Procedure Qualification Record (PQR) documents qualification testing (tensile, bend, macro-etch, radiographic testing)

**Welder Qualification:**
- Welders certified per AWS D17.1 for specific WPS, material, and position
- Qualification coupons tested (visual, radiographic, destructive tests)
- Certification valid for 6 months; extended by 6 months if welder performs production welding in qualified process
- Recertification required if welder inactive >6 months

**Weld Inspection:**
- 100% visual inspection of all production welds (per AWS D17.1 acceptance criteria)
- NDT per WPS requirements (radiographic, ultrasonic, or dye penetrant)
- Critical welds (flight safety): 100% radiographic or ultrasonic inspection
- Weld defects (cracks, porosity, incomplete fusion, undercut): Evaluate per AWS D17.1; repair per approved procedure or scrap part

**Weld Repair:**
- Welding defects requiring repair: Documented in nonconformance system
- Repair procedure approved by Engineering and Quality before implementation
- Maximum 2 repairs per joint; >2 repairs requires Engineering disposition (may require scrap)
- Post-repair inspection same as original weld (visual + NDT)

#### 7.6.4 Composite Fabrication Process Control

**Composite Layup:**
- All composite structure fabricated per approved Composite Fabrication Procedures (CFP)
- CFP defines: Ply schedule, material lot control, shelf life, out-time tracking, vacuum bagging technique, cure cycle
- Operators certified for composite layup (40-hour training + practical exam)

**Material Control:**
- Prepreg material stored in freezer (-18°C); shelf life tracked from date of manufacture
- Out-time tracking: Material removed from freezer logged; cumulative out-time cannot exceed specification limit (typically 30 days for epoxy prepreg)
- Material exceeding shelf life or out-time: Quarantined; tested for usability or scrapped

**Cure Cycle Monitoring:**
- Autoclave or oven cure per approved cure cycle (temperature, pressure, time profile)
- Cure cycle monitored with thermocouples embedded in layup and attached to autoclave chamber
- Automated data logging: Temperature/pressure vs. time recorded for every cure
- Cure cycle deviation >±5°C or >±5 psi pressure: Hold part; Engineering disposition required (may require testing or scrap)

**Composite Inspection:**
- Visual inspection: 100% of cured composite (surface quality, no voids, no wrinkles, no contamination)
- Ultrasonic inspection: 100% of primary structure (bond quality, delamination detection, porosity measurement)
  - Acceptance criteria: <2% porosity, no delaminations >0.5 in diameter
- First Article Inspection: Destructive testing of witness panels (cure degree by DSC, fiber volume fraction, interlaminar shear strength)

**Composite Repair:**
- Minor defects (surface scratches, small voids): Repair per approved procedure (fill, sand, re-coat)
- Major defects (delamination, porosity >2%): Engineering disposition required; may require:
  - Scarf repair (grind out defect, bond in repair plies, re-cure)
  - Bolted doubler (if repair not feasible)
  - Scrap part (if defect in critical load path)

### 7.7 Foreign Object Debris (FOD) Prevention Program

**Objective:** Eliminate foreign object debris in manufactured aircraft to prevent safety hazards (e.g., FOD ingestion by engines, interference with flight controls).

#### 7.7.1 FOD Prevention Measures

**Tool and Equipment Control:**
- Tool accountability system: All tools issued to technicians logged; tools must be returned and accounted for before aircraft leaves workstation
- Tool shadowing: Tool boards with cut-out shapes for each tool; missing tool immediately visible
- Inventory check: Daily inventory of all tools; missing tool triggers FOD search of affected aircraft

**Consumables Control:**
- Consumables (rags, tape, wire, zip ties, hardware) tracked and controlled
- "No Loose Items" policy: All consumable items must be captured in containers when not in use
- End-of-shift inspection: Technician inspects work area and accounts for all consumables before leaving

**Work Area Cleanliness:**
- Clean-as-you-go policy: Technicians clean work area after each task
- Daily work area inspection: Supervisor inspects work area at end of shift; FOD violations documented
- Weekly deep cleaning: Vacuum and wipe down all work areas, tools, and equipment

**Aircraft Openings Protection:**
- All aircraft openings (fuel tank ports, engine inlets, hydraulic reservoirs, electrical connectors) sealed with protective covers when not being worked on
- Cover accountability: Log covers installed/removed; cover not accounted for triggers FOD search

#### 7.7.2 FOD Inspections

**Daily FOD Walk:**
- Manufacturing and Quality personnel walk aircraft assembly area daily (start of shift)
- Document FOD findings (type, location, quantity)
- Trend FOD findings monthly; identify hot spots and implement targeted improvements

**Pre-Closeout FOD Inspection:**
- Before closing any aircraft structure (panels, fairings, access doors), technician performs FOD inspection of enclosed area
- Inspection documented on traveler (signature + date)
- Quality spot-checks 10% of pre-closeout inspections (random selection)

**Final FOD Inspection (Before Delivery):**
- Comprehensive FOD inspection of entire aircraft performed by Quality Inspector
- Inspection includes: Visual inspection of all compartments, borescope inspection of inaccessible areas, shake test (shake control cables, listen for loose items)
- Acceptance criteria: Zero FOD; any FOD found triggers investigation and corrective action

#### 7.7.3 FOD Incident Response

**FOD Found During Manufacturing:**
- Document FOD incident in Quality database (type, location, suspected source)
- Investigate root cause (missing tool, loose hardware, inadequate cleaning)
- Implement corrective action (tool accountability improvement, training, process change)
- Trend FOD incidents; target <1 FOD incident per 10 aircraft produced by FRP

**FOD Found in Flight:**
- FOD discovered during flight test or customer operation: Report immediately to Quality Director and Chief Engineer
- Initiate Product Safety Investigation (Section 9.5) to determine if FOD presents flight safety risk
- Issue Service Bulletin if fleet-wide inspection or corrective action required
- Root cause analysis: Trace FOD back to manufacturing process; implement systemic corrective action

**FOD Program Metrics:**
- FOD incidents per aircraft (target: <1 per 10 aircraft)
- Tool accountability violations (target: <1 per month)
- Pre-closeout FOD inspection compliance (target: 100%)
- Final FOD inspection findings (target: zero)

### 7.8 Calibration and Measurement System Control

**Objective:** Ensure all inspection, measuring, and test equipment (IMTE) provides accurate and reliable measurements to support product acceptance decisions.

#### 7.8.1 Calibration Program Requirements

**Calibration System Standard:** ISO/IEC 17025 (General Requirements for Competence of Testing and Calibration Laboratories)

**Equipment Requiring Calibration:**
- All measuring equipment used for product acceptance (dimensional gages, torque wrenches, pressure gages, thermocouples, multimeters, etc.)
- Test equipment used for functional testing (oscilloscopes, signal generators, power supplies, load cells, etc.)
- Production process control equipment (oven controllers, autoclave instruments, mixing equipment scales)

**Calibration Frequency:**
- Established based on manufacturer recommendation, industry standards, and historical performance
- Typical frequencies:
  - Hand tools (calipers, micrometers): Annually or 2,000 uses
  - Torque wrenches: Semi-annually or 5,000 cycles
  - Electronic test equipment: Annually
  - Thermocouples / RTDs: Annually
  - Pressure gages: Semi-annually
  - Load cells / scales: Quarterly (if used for critical measurements)

**Calibration Standards:**
- All calibrations traceable to National Institute of Standards and Technology (NIST) or equivalent national metrology institute
- Calibration performed by:
  - **Internal calibration lab** (ISO/IEC 17025 accredited) for common equipment
  - **External accredited lab** for complex or specialized equipment
  - **Original Equipment Manufacturer (OEM)** for proprietary test equipment

#### 7.8.2 Calibration Process

**Calibration Procedure:**
1. Equipment submitted for calibration at scheduled interval or when suspected out-of-tolerance
2. As-Found calibration: Test equipment against known standards; document as-found condition
3. Adjustment (if required): Adjust equipment to bring within tolerance
4. As-Left calibration: Re-test equipment; verify within tolerance after adjustment
5. Calibration label: Affix label to equipment with calibration date, due date, and calibration lab identifier
6. Calibration certificate: Issue certificate documenting as-found/as-left condition, standards used, uncertainty, and traceability

**Out-of-Tolerance Equipment:**
- If equipment found out-of-tolerance during calibration:
  - Tag equipment "OUT OF SERVICE - DO NOT USE"
  - Evaluate impact: Identify all product inspected/tested with out-of-tolerance equipment since last successful calibration
  - Disposition: Engineering and Quality determine if product must be re-inspected, tested, or accepted as-is
  - Root cause analysis: Determine why equipment went out of tolerance (abuse, drift, inadequate calibration interval)
  - Corrective action: Adjust calibration interval, replace equipment, or provide additional training

**Calibration Records:**
- Maintain calibration database with:
  - Equipment ID, description, location
  - Calibration procedure reference
  - Calibration frequency and due date
  - Calibration history (dates, as-found/as-left data, technician)
  - Out-of-tolerance incidents and disposition
- Records retained for 10 years minimum

#### 7.8.3 Measurement System Analysis (MSA)

**Objective:** Verify that measurement systems (gage + procedure + operator) are capable of discriminating conforming from non-conforming product.

**MSA Methods:**

| Method | Application | Acceptance Criteria |
|--------|-------------|---------------------|
| **Gage R&R (Repeatability & Reproducibility)** | Variable data (dimensional measurements) | Total GR&R <10% of tolerance (preferred), <30% (acceptable) |
| **Attribute Agreement Analysis** | Attribute data (pass/fail inspections) | >90% agreement between operators and standard |
| **Bias and Linearity Study** | Verify gage accuracy across measurement range | Bias <5% of tolerance, linearity slope not significantly different from 1.0 |

**Gage R&R Study Execution:**
- Select 10 parts spanning the tolerance range (3 at low limit, 4 at mid, 3 at high limit)
- 3 operators measure each part 3 times in random order (blind study)
- Analyze data using ANOVA or Range method
- Calculate:
  - **Equipment Variation (EV):** Repeatability (gage consistency)
  - **Appraiser Variation (AV):** Reproducibility (operator-to-operator variation)
  - **Total GR&R = √(EV² + AV²)** expressed as % of tolerance
- **Interpretation:**
  - GR&R <10%: Excellent measurement system
  - GR&R 10-30%: Acceptable; may be acceptable depending on application
  - GR&R >30%: Unacceptable; measurement system must be improved

**MSA Frequency:**
- Initial MSA: Before releasing new measurement system to production
- Periodic MSA: Annually for critical characteristics
- Event-driven MSA: After gage repair, calibration adjustment, or if measurement consistency questioned

**MSA Failure Response:**
- If GR&R >30%:
  - Improve measurement procedure (better fixturing, clearer instructions, better lighting)
  - Upgrade measurement equipment (higher resolution, better repeatability)
  - Provide additional operator training
  - Re-run MSA after improvement; verify GR&R acceptable before production use

---

## 8. SUPPLIER QUALITY MANAGEMENT

### 8.1 Supplier Quality Philosophy

**Strategic Approach:**

The MAAP-1 supply chain comprises over 200 Tier 1 suppliers providing approximately 70% of aircraft content by value. Supplier quality performance directly impacts MAAP-1 cost, schedule, and product quality. The supplier quality strategy focuses on:

1. **Supplier Selection:** Rigorous qualification process ensures only capable suppliers awarded contracts
2. **Requirements Flow-Down:** Clear, unambiguous quality requirements communicated to all suppliers
3. **Partnership Model:** Collaborative relationships with strategic suppliers; shared quality objectives
4. **Performance Management:** Data-driven supplier scorecards; rewards and consequences
5. **Continuous Improvement:** Joint supplier development initiatives to drive quality and cost improvements

### 8.2 Supplier Classification and Requirements

#### 8.2.1 Supplier Categories

| Category | Description | % of Suppliers | Quality Requirements |
|----------|-------------|----------------|---------------------|
| **Strategic** | Critical, sole-source, or high-value suppliers (engines, transmission, flight controls, avionics) | 10% (~20 suppliers) | - AS9100 certified (mandatory)<br>- Dedicated supplier quality engineer<br>- Quarterly business reviews<br>- Joint development agreements |
| **Preferred** | Important, multiple-source options, proven performers | 30% (~60 suppliers) | - ISO 9001 certified (minimum)<br>- Annual supplier audits<br>- Semi-annual performance reviews |
| **Qualified** | Standard parts, commodity items, adequate performers | 50% (~100 suppliers) | - ISO 9001 or equivalent<br>- Periodic audits (risk-based)<br>- Performance monitoring |
| **Conditional** | New suppliers, limited history, performance concerns | 10