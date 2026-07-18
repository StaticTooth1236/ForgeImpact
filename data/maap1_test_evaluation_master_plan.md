# TEST & EVALUATION MASTER PLAN (TEMP)
## Eurus Systems MAAP-1 "AetherForge" Program

---

| | |
|---|---|
| **Document No.** | AF-MAAP1-TEMP-0001 |
| **Revision** | A (Initial Release) |
| **Classification** | Eurus Systems Proprietary — Export Controlled (ITAR/EAR Applicable) |
| **Derived From** | Program Requirements Baseline AF-MAAP1-PRB-0001, Rev A<br>Key Specifications Document AF-MAAP1-KSD-0002, Rev A<br>Integrated Master Schedule MAAP1-SCH-001, Rev A |
| **Owner** | MAAP-1 Test & Evaluation Director |
| **Date** | January 2025 |
| **Approvals** | Program Manager, Chief Engineer, Chief Test Pilot, Customer T&E Authority |

---

## DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Program Manager | [Signature Required] | _________________ | ________ |
| Chief Engineer | [Signature Required] | _________________ | ________ |
| T&E Director | [Signature Required] | _________________ | ________ |
| Chief Test Pilot | [Signature Required] | _________________ | ________ |
| Government T&E Authority | [Signature Required] | _________________ | ________ |
| Safety Officer | [Signature Required] | _________________ | ________ |

---

## EXECUTIVE SUMMARY

The MAAP-1 Test & Evaluation Master Plan (TEMP) defines the comprehensive strategy, phases, resources, and success criteria for verifying and validating all system requirements from subsystem qualification through operational deployment. This plan integrates developmental test (DT), operational test (OT), airworthiness certification, and variant-specific test programs into a unified T&E strategy that directly supports:

- **Technical Risk Reduction:** Early identification and mitigation of design, integration, and performance issues
- **Requirements Verification:** Systematic validation of all KPPs, KSAs, and derived requirements
- **Airworthiness Certification:** FAA Part 29 and military airworthiness compliance demonstration
- **Dual-Use Certification:** Support for both civilian (wildfire/cargo) and military operational approval
- **Production Readiness:** Manufacturing process validation and first article qualification

**Total T&E Program Duration:** 48 months (PM 36 through PM 84)  
**Total Flight Test Hours:** 820 hours across 6 flight test articles  
**Total Ground Test Hours:** 18,500+ hours across multiple facilities  
**Estimated T&E Budget:** $285M (18% of total program cost)

---

## TABLE OF CONTENTS

1. [Introduction and Scope](#1-introduction-and-scope)
2. [Test Philosophy and Strategy](#2-test-philosophy-and-strategy)
3. [Test Program Structure](#3-test-program-structure)
4. [Phase 1: Component & Subsystem Testing](#4-phase-1-component--subsystem-testing)
5. [Phase 2: Ground Integration Testing](#5-phase-2-ground-integration-testing)
6. [Phase 3: Static Structural Testing](#6-phase-3-static-structural-testing)
7. [Phase 4: Propulsion Ground Testing](#7-phase-4-propulsion-ground-testing)
8. [Phase 5: Environmental Qualification](#8-phase-5-environmental-qualification)
9. [Phase 6: Developmental Flight Test](#9-phase-6-developmental-flight-test)
10. [Phase 7: Swarm & Multi-Aircraft Testing](#10-phase-7-swarm--multi-aircraft-testing)
11. [Phase 8: Payload Integration Testing](#11-phase-8-payload-integration-testing)
12. [Phase 9: Operational Test & Evaluation](#12-phase-9-operational-test--evaluation)
13. [Phase 10: Certification & Qualification](#13-phase-10-certification--qualification)
14. [Test Articles & Resources](#14-test-articles--resources)
15. [Test Facilities & Infrastructure](#15-test-facilities--infrastructure)
16. [Safety & Risk Management](#16-safety--risk-management)
17. [Data Management & Analysis](#17-data-management--analysis)
18. [Success Criteria & Exit Gates](#18-success-criteria--exit-gates)

---

## 1. INTRODUCTION AND SCOPE

### 1.1 Purpose

This Test & Evaluation Master Plan (TEMP) establishes the comprehensive test strategy, objectives, phases, resources, and success criteria for the MAAP-1 program. It serves as the authoritative planning document governing all test activities from component qualification through operational deployment and supports:

- **Verification:** Confirmation that the system is built correctly per specifications
- **Validation:** Confirmation that the correct system was built for the intended missions
- **Certification:** Demonstration of airworthiness and operational safety
- **Risk Reduction:** Early identification and mitigation of technical, safety, and performance risks

### 1.2 Scope and Applicability

This TEMP applies to all test activities conducted on:

- **MAAP-1 Common "Green Aircraft"** (baseline tandem-rotor airframe and dynamic systems)
- **MAAP-1F "Wildfire" Variant** (autonomous aerial firefighting configuration)
- **MAAP-1I "Sentinel" Variant** (ISR mission configuration)
- **MAAP-1C "Atlas" Variant** (cargo/logistics configuration)

The TEMP encompasses:
- Component and subsystem qualification testing
- Ground integration testing (static, dynamic, environmental)
- Developmental flight testing (envelope expansion, performance validation)
- Autonomous system testing (GNC, DAA, swarm operations)
- Payload integration testing (variant-specific mission equipment)
- Operational testing (mission scenarios, user evaluation)
- Certification testing (FAA Part 29, military airworthiness)

### 1.3 Document Relationship and Traceability

This TEMP is derived from and subordinate to:

- **Program Requirements Baseline (PRB):** AF-MAAP1-PRB-0001, Rev A
- **Key Specifications Document (KSD):** AF-MAAP1-KSD-0002, Rev A
- **Integrated Master Schedule (IMS):** MAAP1-SCH-001, Rev A
- **System Safety Program Plan (SSPP):** AF-MAAP1-SSPP-0003, Rev A

All test objectives trace directly to specific PRB requirements via the Requirements Verification Traceability Matrix (RVTM-0001).

### 1.4 T&E Program Timeline

```
MAAP-1 T&E PROGRAM TIMELINE (PM 36 - PM 84)

PM 36-48  |████████████| Phase 1-2: Component/Subsystem Testing
PM 42-54  |████████████████| Phase 3: Static Structural Testing
PM 45-57  |████████████████| Phase 4: Propulsion Ground Testing
PM 48-60  |████████████████| Phase 5: Environmental Qualification
PM 54-72  |██████████████████████| Phase 6: Developmental Flight Test
PM 66-78  |████████████████| Phase 7: Swarm & Multi-Aircraft Testing
PM 60-75  |████████████████████| Phase 8: Payload Integration Testing
PM 72-84  |████████████████| Phase 9: Operational Test & Evaluation
PM 78-84  |████████| Phase 10: Certification & Qualification

Legend: Each █ represents approximately 1 month
```

---

## 2. TEST PHILOSOPHY AND STRATEGY

### 2.1 Overall Test Philosophy

The MAAP-1 T&E program is structured around the following core principles:

#### 2.1.1 **Build-Up Approach: Test What You Fly, Fly What You Test**

Progressive complexity from components → subsystems → integrated systems → flight vehicle ensures thorough understanding at each level before advancing to the next. No flight article will proceed to flight test without comprehensive ground validation.

#### 2.1.2 **Early Risk Retirement**

Critical technologies, novel design features, and high-risk subsystems (autonomy, tandem-rotor interference, swarm coordination) undergo accelerated testing early in the program to identify and mitigate issues before they impact critical path milestones.

#### 2.1.3 **Test-Analyze-Fix-Test (TAFT) Cycle**

Disciplined closed-loop process ensuring anomalies are thoroughly analyzed, root causes identified, corrective actions implemented, and effectiveness verified before proceeding.

#### 2.1.4 **Multi-Variant Efficiency**

Commonality strategy (>80% part count across variants) allows Green Aircraft qualification to satisfy majority of test objectives for all three variants, with focused delta testing for variant-unique systems.

#### 2.1.5 **Integrated DT/OT Approach**

Where feasible, developmental test (DT) and operational test (OT) are conducted concurrently to maximize efficiency while maintaining independence of operational assessment.

#### 2.1.6 **Safety-First Culture**

All test activities prioritize safety of test personnel, flight crew, ground personnel, and the public. Flight test envelope expansion follows conservative incremental approach with well-defined abort criteria and contingency procedures.

### 2.2 Test Strategy Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                  MAAP-1 T&E STRATEGY ARCHITECTURE               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Component &    │────▶│  Subsystem       │────▶│  System         │
│  Material Test  │     │  Qualification   │     │  Integration    │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                       │                         │
         │                       │                         │
         ▼                       ▼                         ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Environmental  │     │  Static          │     │  Propulsion     │
│  Qualification  │     │  Structural Test │     │  Ground Test    │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                       │                         │
         └───────────────────────┴─────────────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │  Ground Integration    │
                    │  Testing (Iron Bird)   │
                    └────────────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │  First Flight Article  │
                    │  (FTA-1) Ground Test   │
                    └────────────────────────┘
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
    ┌──────────────────────┐        ┌──────────────────────┐
    │  Developmental       │        │  Payload Integration │
    │  Flight Test (DT)    │        │  & Variant Testing   │
    └──────────────────────┘        └──────────────────────┘
                │                                 │
                └────────────────┬────────────────┘
                                 ▼
                    ┌────────────────────────┐
                    │  Swarm & Multi-        │
                    │  Aircraft Operations   │
                    └────────────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │  Operational Test &    │
                    │  Evaluation (OT&E)     │
                    └────────────────────────┘
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
    ┌──────────────────────┐        ┌──────────────────────┐
    │  FAA Part 29         │        │  Military            │
    │  Certification       │        │  Airworthiness       │
    └──────────────────────┘        └──────────────────────┘
```

### 2.3 Relationship Between Testing and Risk Reduction

Test program directly addresses program's top technical risks:

| Risk Area | Test Mitigation Strategy | Test Phase |
|-----------|--------------------------|------------|
| **Tandem-Rotor Aerodynamic Interference** | Wind tunnel testing, CFD validation, rotor hover test stand, flight envelope expansion | Phase 2, 4, 6 |
| **Autonomous GNC Reliability (1×10⁻⁷ failure rate requirement)** | Iron Bird HITL testing, fault injection, 10,000+ simulated flight hours, flight test validation | Phase 2, 5, 6, 9 |
| **Swarm Coordination in GPS-Denied Environments** | Lab testing, outdoor multi-aircraft testing, GPS jamming scenarios | Phase 7 |
| **Heavy External Load Stability (16,000 lb objective)** | Static load testing, ground taxi with load, incremental flight test with increasing loads | Phase 3, 6, 8 |
| **Hot/High Hover Performance (8,000 ft PA, ISA+20°C)** | Propulsion altitude testing, performance flight test in Western US test locations | Phase 4, 6 |
| **OEI Safe Landing Capability** | Single-engine ground runs, simulated engine failures in flight test | Phase 4, 6 |
| **Composite Primary Structure Durability** | Static ultimate load test, fatigue testing (2× design life), environmental exposure | Phase 3, 5 |
| **Autonomous DAA System Effectiveness** | Ground simulation, flight test with cooperative/non-cooperative targets | Phase 6, 9 |

### 2.4 Dual-Use Certification Strategy

The MAAP-1 program pursues parallel certification paths:

#### **Civilian Certification Path (MAAP-1F, MAAP-1C)**
- **Authority:** FAA
- **Regulation:** 14 CFR Part 29 (Transport Category Rotorcraft)
- **Special Conditions:** Autonomous operations, Beyond Visual Line of Sight (BVLOS)
- **Certification Basis Agreement:** PM 18 (targeting Q2 2027)
- **Type Certificate Target:** PM 84 (MAAP-1C baseline, Q4 2031)

#### **Military Certification Path (MAAP-1I, MAAP-1F optional)**
- **Authority:** DoD Airworthiness Certification Process
- **Standard:** MIL-HDBK-516C
- **Military Flight Release:** Service-specific requirements
- **Target:** PM 84 (concurrent with FAA TC)

**Commonality Strategy:**
- Green Aircraft certified to most stringent requirements (FAA + MIL)
- Variant-specific systems certified via Type Certificate Amendment (FAA) or supplemental military airworthiness assessment
- Test data shared across certification authorities to minimize duplication
- Joint DT/OT test events where regulatory authorities agree to observe same test

### 2.5 Requirements Verification Strategy

All 487 PRB-derived requirements are assigned verification methods per RVTM-0001:

| Verification Method | % of Requirements | Test Phase(s) |
|---------------------|-------------------|---------------|
| **Test (T)** | 62% | Phases 1-10 |
| **Analysis (A)** | 23% | Continuous (PDR-CDR-TRR) |
| **Demonstration (D)** | 11% | Phases 6, 9 |
| **Inspection (I)** | 4% | Continuous (design reviews, production) |

**Verification Closure Gates:**
- **PDR Exit:** 100% of requirements allocated to verification method
- **CDR Exit:** 80% of analysis-based requirements closed; test procedures approved
- **First Flight:** 100% of ground-testable requirements verified
- **DT Complete (PM 72):** 95% of KPPs verified to Threshold
- **OT&E Complete (PM 84):** 100% of KPPs verified; 85% of KPPs achieved Objective

---

## 3. TEST PROGRAM STRUCTURE

### 3.1 Test Phases and Sequencing

The MAAP-1 T&E program consists of 10 distinct but overlapping phases:

| Phase | Title | Duration | Start (PM) | End (PM) | Test Articles |
|-------|-------|----------|------------|----------|---------------|
| **1** | Component & Subsystem Testing | 12 months | 36 | 48 | Components, breadboards |
| **2** | Ground Integration Testing | 12 months | 42 | 54 | Iron Bird, avionics lab |
| **3** | Static Structural Testing | 12 months | 42 | 54 | DTA-1 (static test article) |
| **4** | Propulsion Ground Testing | 12 months | 45 | 57 | DTA-2 (propulsion test article) |
| **5** | Environmental Qualification | 12 months | 48 | 60 | DTA-3, environmental specimens |
| **6** | Developmental Flight Test | 18 months | 54 | 72 | FTA-1, FTA-2, FTA-3 |
| **7** | Swarm & Multi-Aircraft Testing | 12 months | 66 | 78 | FTA-4, FTA-5, FTA-6 |
| **8** | Payload Integration Testing | 15 months | 60 | 75 | FTA-2 (MAAP-1F), FTA-3 (MAAP-1I), FTA-1 (MAAP-1C) |
| **9** | Operational Test & Evaluation | 12 months | 72 | 84 | All FTAs, LRIP aircraft |
| **10** | Certification & Qualification | 6 months | 78 | 84 | FTA-1 (certification aircraft) |

### 3.2 Test Article Strategy

**Development Test Articles (DTAs):** Non-flying ground test articles
- **DTA-1:** Static structural test article (full airframe, ultimate load test to failure)
- **DTA-2:** Propulsion integration test article (engine/rotor/transmission ground runs)
- **DTA-3:** Avionics integration test article (Iron Bird, full mission systems)

**Flight Test Articles (FTAs):** Airworthy flight test vehicles
- **FTA-1:** First flight article; baseline MAAP-1C configuration; certification aircraft
- **FTA-2:** Envelope expansion article; MAAP-1F (firefighting) variant testing
- **FTA-3:** Performance validation article; MAAP-1I (ISR) variant testing
- **FTA-4, FTA-5, FTA-6:** Swarm/multi-aircraft operations testing (all MAAP-1C initially, reconfigurable)

**Low-Rate Initial Production (LRIP) Aircraft:**
- **PA-1 through PA-18:** Production verification, operational test augmentation, training fleet establishment

### 3.3 Test Organization and Governance

```
┌────────────────────────────────────────────────────────┐
│              MAAP-1 T&E ORGANIZATION                   │
└────────────────────────────────────────────────────────┘

                    ┌──────────────────┐
                    │  Program Manager │
                    └────────┬─────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
        ┌───────▼────────┐       ┌───────▼────────┐
        │  Chief Engineer│       │  T&E Director  │
        └───────┬────────┘       └───────┬────────┘
                │                        │
    ┌───────────┴──────────┐            │
    │                      │            │
┌───▼────┐         ┌───────▼─────┐     │
│ Systems│         │ Safety      │     │
│ Eng    │         │ Officer     │     │
└────────┘         └─────────────┘     │
                                        │
        ┌───────────────────────────────┴──────────────────────┐
        │                                                       │
┌───────▼────────┐   ┌──────────────┐   ┌────────────────┐   ┌────────────────┐
│ Ground Test    │   │ Flight Test  │   │ Autonomous     │   │ Data Analysis  │
│ Director       │   │ Director     │   │ Systems Test   │   │ & Reporting    │
└───────┬────────┘   └──────┬───────┘   └───────┬────────┘   └───────┬────────┘
        │                   │                    │                     │
    ┌───┴────┬──────┐   ┌──┴───┬─────┐   ┌─────┴─────┐         ┌────┴────┐
    │ Static │ Prop │   │ DT   │ OT  │   │ GNC Test  │         │ Data    │
    │ Test   │ Test │   │ Team │ Team│   │ Lab       │         │ Systems │
    └────────┴──────┘   └──────┴─────┘   └───────────┘         └─────────┘
```

**Key Roles and Responsibilities:**

- **T&E Director:** Overall test program execution, schedule, budget, resource allocation
- **Ground Test Director:** DTA testing, facility operations, ground safety
- **Flight Test Director:** FTA testing, flight safety, airspace coordination
- **Autonomous Systems Test Lead:** GNC, DAA, swarm testing across all phases
- **Chief Test Pilot:** Flight test execution, crew training, flight safety authority
- **Safety Officer:** Independent safety oversight, mishap investigation, safety case approval
- **Data Analysis Lead:** Test data processing, performance analysis, requirements verification

### 3.4 Test Governance and Decision Authority

**Test Readiness Reviews (TRRs):** Required before major test phase initiation
- **Attendees:** Program Manager, Chief Engineer, T&E Director, Safety Officer, Customer Representative
- **Exit Criteria:** Test procedures approved, test article configuration controlled, safety case accepted, resources committed

**Test Review Boards (TRBs):** Weekly during active testing
- **Purpose:** Review previous week's results, approve next week's test plan, address anomalies
- **Decision Authority:** T&E Director (routine), Program Manager (significant deviations)

**Anomaly Review Board (ARB):** Convened for any test anomaly
- **Classification:** Category 1 (safety-critical), Category 2 (performance-impacting), Category 3 (informational)
- **Process:** Root cause analysis → corrective action → verification test → closure approval

**Flight Safety Review Board (FSRB):** Before each flight test phase
- **Authority:** Chief Test Pilot has absolute authority to delay/abort testing for safety concerns
- **Approval:** Signed flight clearance required for each new envelope increment

---

## 4. PHASE 1: COMPONENT & SUBSYSTEM TESTING

**Duration:** 12 months (PM 36-48)  
**Objective:** Qualify critical components and subsystems to design specifications before integration  
**Test Location:** Eurus Systems Component Test Lab; Supplier facilities (witnessed)

### 4.1 Phase Overview and Objectives

Phase 1 testing establishes confidence in individual components and subsystems through qualification testing to design limits and beyond. This phase directly supports:
- **Risk Reduction:** Early identification of component design flaws
- **Design Maturation:** Data-driven refinement before CDR
- **Supplier Validation:** Verification of supplier-provided items
- **Safety Case Development:** Component-level FMEA validation

### 4.2 Test Campaigns

#### 4.2.1 Rotor Blade Qualification

**Test Article:** 4× production-representative composite rotor blades

| Test | Objective | Success Criteria | Duration |
|------|-----------|------------------|----------|
| **Static Load Test** | Verify blade strength to ultimate load | Withstand 150% design limit load without failure | 4 weeks |
| **Fatigue Test** | Demonstrate blade life >5,000 hours | Complete 2× design life cycles without crack initiation | 16 weeks |
| **Whirl Test** | Validate blade balance and track | ≤0.5 in tip tracking error at 268 RPM | 2 weeks |
| **Lightning Strike Test** | Verify lightning protection system | No critical damage after Zone 1A direct strike | 1 week |
| **Bird Strike Test** | Validate erosion protection | No penetration from 4 lb bird @ 150 KTAS | 1 week |
| **Environmental Exposure** | Assess composite durability | <5% strength degradation after 1000 hr salt fog + UV | 8 weeks |

**Total Test Hours:** 1,200 hours  
**Test Completion:** PM 44

#### 4.2.2 Transmission System Qualification

**Test Article:** Full-scale forward transmission, aft transmission, interconnect driveshaft

| Test | Objective | Success Criteria | Duration |
|------|-----------|------------------|----------|
| **Back-to-Back Load Test** | Verify torque capacity | Sustain 150% max continuous torque for 30 min | 3 weeks |
| **Endurance Test** | Demonstrate 5,000 hr TBO | 250 hr accelerated mission profile | 6 weeks |
| **OEI Transient Test** | Validate single-engine operation | 50 cycles of 2.5 min OEI power | 2 weeks |
| **Run-Dry Test** | Verify 30 min oil-out capability | Operate 30 min with total oil loss | 1 week |
| **Vibration Survey** | Characterize vibration signature | Meet MIL-STD-810H vibration limits | 2 weeks |

**Total Test Hours:** 300 hours (powered operation)  
**Test Completion:** PM 46

#### 4.2.3 Flight Control Actuator Qualification

**Test Article:** 12× primary flight control actuators (triplex redundant set)

| Test | Objective | Success Criteria | Duration |
|------|-----------|------------------|----------|
| **Load Cycle Test** | Verify actuator life | 500,000 cycles @ max load | 8 weeks |
| **Rate Capability Test** | Validate control authority | 60°/sec slew rate maintained | 1 week |
| **Hardover Failure Test** | Verify fail-safe operation | Remaining channels maintain control | 2 weeks |
| **Temperature Extreme Test** | Environmental qualification | Full performance -54°C to +71°C | 4 weeks |
| **EMI Susceptibility** | Verify electromagnetic immunity | No upset during HIRF exposure per DO-160G | 2 weeks |

**Total Test Hours:** 12,000 actuator-hours  
**Test Completion:** PM 45

#### 4.2.4 Engine Qualification (Witnessed Tests at Engine Manufacturer)

**Test Article:** 4× production engines (2 flight engines + 2 test engines)

| Test | Objective | Success Criteria | Duration |
|------|-----------|------------------|----------|
| **Sea Level Performance** | Validate power ratings | Meet all power specifications ±2% | 4 weeks |
| **Altitude Performance** | Hot/high capability | 2,000 shp @ 8,000 ft PA, ISA+20°C | 3 weeks |
| **Endurance Test** | Demonstrate 3,500 hr TBO | 150 hr accelerated mission cycle | 6 weeks |
| **OEI Contingency Test** | Verify 2,400 shp for 2.5 min | Meet OEI power without exceedance | 2 weeks |
| **Ingestion Test** | FOD tolerance | Ingest per MIL-E-5007 without flameout | 1 week |
| **Environmental Test** | Temperature extremes | Start and operate -40°C to +52°C | 3 weeks |

**Total Test Hours:** 200 hours (engine run time)  
**Test Completion:** PM 48

#### 4.2.5 Avionics LRU Qualification

**Test Articles:** All mission-critical avionics Line Replaceable Units (LRUs)

| System | Test Focus | Environmental Testing | DO-160G Cat |
|--------|------------|----------------------|-------------|
| **Flight Control Computer (3×)** | Redundancy management, fault detection | Temp, altitude, vibration, EMI | Category A |
| **Mission Computer (2×)** | Processing capacity, I/O throughput | Temp, humidity, EMI | Category B |
| **GPS/INS (3×)** | Navigation accuracy, jamming resistance | Temp, altitude, vibration | Category A |
| **DAA Radar (1×)** | Detection range, false alarm rate | Temp, vibration, EMI | Category B |
| **SATCOM Terminal (2×)** | Link availability, data throughput | Temp, altitude, vibration | Category B |
| **Datalink Radio (2×)** | Range, interference rejection | Temp, altitude, EMI/HIRF | Category A |

**Total LRUs Tested:** 45 units across 18 LRU types  
**Total Test Hours:** 8,500 unit-hours  
**Test Completion:** PM 47

### 4.3 Phase 1 Success Criteria

| Criterion | Threshold | Status Tracking |
|-----------|-----------|-----------------|
| **Component Qualification Rate** | ≥95% first-pass qualification | Weekly TRB review |
| **Qualification Test Completion** | 100% of critical components qualified by PM 48 | Tracked in RVTM-0001 |
| **Anomaly Closure** | Zero open Category 1 anomalies at phase exit | ARB tracking |
| **Design Maturity** | Component design ≥90% released for production | Engineering change tracking |
| **Safety Case** | Component FMEA 100% complete, all critical failures mitigated | Safety review board |

**Phase 1 Exit Gate:** Component Qualification Review (PM 48)

---

## 5. PHASE 2: GROUND INTEGRATION TESTING

**Duration:** 12 months (PM 42-54, overlaps with Phase 1)  
**Objective:** Integrate and verify subsystems in representative ground test environments  
**Test Location:** Eurus Systems Integration Lab; Iron Bird facility

### 5.1 Phase Overview

Phase 2 brings qualified components together into integrated subsystems and ultimately a complete "Iron Bird" ground test article representing the full aircraft systems architecture without flight structure. Key objectives:

- **Interface Verification:** Validate all mechanical, electrical, and data interfaces per ICDs
- **Functional Integration:** Demonstrate integrated system performance
- **Software Integration:** Flight control laws, autonomy algorithms, mission software
- **Fault Propagation:** Understand system-level effects of component failures
- **Human-Machine Interface:** Validate GCS displays and controls

### 5.2 Iron Bird Configuration

**Iron Bird Article:** DTA-3 (Avionics Integration Test Article)

**Scope:**
- Complete flight control system (actuators, sensors, computers)
- Full avionics suite (navigation, communication, mission systems)
- Propulsion system simulator (engine FADEC, fuel system functional model)
- Rotor system simulator (mechanical load representation)
- Electrical power generation and distribution
- Full Ground Control Station (GCS)

**Instrumentation:**
- 2,500+ data channels
- Real-time data acquisition @ 1000 Hz
- Fault injection capability (software, hardware, data bus)
- 6-DOF motion platform (optional, for advanced GNC testing)

### 5.3 Test Campaigns

#### 5.3.1 Systems Integration & Checkout

**Duration:** 8 weeks (PM 42-44)

| Test | Objective | Success Criteria |
|------|-----------|------------------|
| **Power-On Test** | Verify electrical system | All LRUs power up, no smoke test pass |
| **Data Bus Verification** | Validate network architecture | 100% message throughput, <10 ms latency |
| **Sensor Calibration** | Align all sensors | INS alignment <0.1° attitude error |
| **Control Loop Closure** | Verify FCS architecture | Closed-loop response matches model |

#### 5.3.2 Flight Control System Testing

**Duration:** 12 weeks (PM 44-47)

| Test Campaign | Test Points | Objectives |
|---------------|-------------|------------|
| **Control Law Validation** | 150 test cases | Hover, forward flight, transition modes |
| **Redundancy Management** | 75 failure scenarios | Verify graceful degradation, no single-point failures |
| **Autopilot Modes** | 50 automated sequences | Altitude hold, heading hold, waypoint navigation |
| **Autonomous Takeoff/Landing** | 100 simulated scenarios | Precision landing ±1 m CEP |
| **External Load Compensation** | 25 load configurations | Stability augmentation for 12,000 lb external load |

**Success Criteria:**
- 100% of control modes functional
- <1×10⁻⁶ probability of FCS-induced loss of control (analysis + test)
- Autonomous landing success rate >99% in simulation

#### 5.3.3 Autonomous GNC System Testing

**Duration:** 16 weeks (PM 45-49, critical path item)

| Test Focus | Test Hours | Key Validation |
|------------|------------|----------------|
| **Waypoint Navigation** | 500 hours | Accuracy <10 m CEP |
| **GPS-Denied Navigation** | 300 hours | INS + TRN: <50 m drift after 15 min |
| **Detect and Avoid (DAA)** | 400 hours | 100% collision avoidance, <1% false alarm rate |
| **Lost-Link Behavior** | 200 hours | RTL/Loiter/Land sequences 100% reliable |
| **Swarm Coordination** | 600 hours | 4-aircraft formation, spacing ±5 m |
| **Mission Re-Planning** | 150 hours | Dynamic waypoint updates, weather avoidance |

**Hardware-in-the-Loop (HITL) Testing:**
- **Simulated Flight Hours:** 10,000+ hours
- **Fault Injection Scenarios:** 1,500 (software faults, sensor failures, datalink dropouts)
- **Monte Carlo Runs:** 50,000 (statistical validation of autonomy reliability)

**Success Criteria:**
- Autonomous GNC reliability target: 1×10⁻⁷ loss-of-control events per flight hour (demonstrated via combination of test + analysis per DO-178C DAL A)
- DAA system meets ASTM F3442 performance standards
- Swarm coordination maintains formation integrity >99.5% of mission time

#### 5.3.4 Mission Systems Integration

**Duration:** 10 weeks (PM 48-50)

**MAAP-1F (Firefighting) Systems:**
- Water drop control simulation (2,000 gal tank release)
- Fire detection sensor integration
- Pilot cockpit displays and controls

**MAAP-1I (ISR) Systems:**
- EO/IR sensor turret control
- Video downlink and processing
- Target tracking algorithms

**MAAP-1C (Cargo) Systems:**
- External load monitoring
- Precision release point calculation
- Cargo manifest interface

**Success Criteria:**
- 100% mission system functions operational in integrated environment
- Datalink capacity sufficient for simultaneous HD video + telemetry + C2

#### 5.3.5 Cybersecurity & RMF Testing

**Duration:** 8 weeks (PM 50-52)

| Test | Objective | Success Criteria |
|------|-----------|------------------|
| **Penetration Testing** | Identify vulnerabilities | Zero critical (CAT I) findings |
| **Encryption Validation** | Verify datalink security | AES-256 compliance, no plaintext leakage |
| **Access Control Testing** | Validate authorization | Role-based access enforced 100% |
| **Incident Response** | Cyber attack scenarios | Detection + isolation <60 seconds |

**Compliance Target:** NIST RMF Authorization to Operate (ATO)

### 5.4 Phase 2 Success Criteria

| Criterion | Threshold | Objective |
|-----------|-----------|-----------|
| **Systems Integration** | 100% of interfaces functional | Zero integration anomalies |
| **Iron Bird Test Completion** | 100% of test points executed | <5% re-test rate |
| **Autonomy Validation** | 10,000 HITL hours, 1×10⁻⁷ reliability target | 15,000 HITL hours |
| **Fault Coverage** | 95% of single-point failures tested | 100% coverage |
| **Mission Systems Ready** | All 3 variants integrated on Iron Bird | Cross-variant compatibility verified |

**Phase 2 Exit Gate:** System Integration Review (PM 54)

---

## 6. PHASE 3: STATIC STRUCTURAL TESTING

**Duration:** 12 months (PM 42-54, parallel with Phases 1-2)  
**Objective:** Verify airframe structural integrity to ultimate load and fatigue life  
**Test Location:** Eurus Systems Structural Test Facility, Building 450  
**Test Article:** DTA-1 (full-scale static test airframe)

### 6.1 Phase Overview

Static structural testing validates the primary structure design through progressive loading to limit load, ultimate load, and cyclic fatigue. This testing directly supports airworthiness certification and provides critical data for:
- Structural certification per 14 CFR Part 29
- Finite Element Model (FEM) validation
- Fatigue life substantiation
- Fail-safe and damage tolerance analysis

### 6.2 DTA-1 Configuration

**Test Article Description:**
- Complete airframe: fuselage, rotor pylons, sponsons, tailcone
- Production-representative composite primary structure
- Instrumented with 3,500+ strain gauges, 250 displacement transducers
- Mounted in custom test fixture with 42-point load introduction system
- High-speed video (10,000 fps) for failure mode capture

**Loads Application System:**
- Hydraulic actuators: 42× servo-controlled, 50 kip capacity each
- Computer-controlled load sequencing
- Real-time structural response monitoring
- Automatic test abort on approaching failure

### 6.3 Test Matrix

#### 6.3.1 Limit Load Test Campaign

**Duration:** 12 weeks (PM 42-45)  
**Objective:** Verify structure withstands 100% design limit load with ≤5% permanent deformation

| Load Case | Description | Load Factor | Test Points |
|-----------|-------------|-------------|-------------|
| **Symmetric Pull-Up** | +3.5 g maneuver | +3.5 g | 15 increments |
| **Symmetric Push-Over** | -1.0 g maneuver | -1.0 g | 10 increments |
| **Rolling Maneuver** | ±60° bank | ±2.0 g lateral | 12 increments |
| **Asymmetric Flight** | Single rotor failure | Combined loading | 10 cases |
| **External Load Operations** | 16,000 lb sling load | +2.5 g vertical | 15 increments |
| **Landing Impact** | Hard landing, max GW | +2.0 g vertical | 8 cases |
| **Rotor Thrust Limit** | Max rotor thrust | Forward/aft pylons | 12 cases |
| **Ground Handling** | Towing, jacking | Point loads | 8 cases |

**Total Limit Load Test Points:** 90  
**Success Criteria:**
- Zero structural failures
- Permanent deformation <5% at any location
- Strain measurements within 10% of FEM predictions

#### 6.3.2 Ultimate Load Test Campaign

**Duration:** 8 weeks (PM 45-47)  
**Objective:** Demonstrate structure withstands 150% design limit load (ultimate load factor = 1.5)

| Load Case | Ultimate Load Factor | Hold Time | Expected Outcome |
|-----------|----------------------|-----------|------------------|
| **Symmetric Pull-Up** | +5.25 g | 3 seconds | No failure |
| **Symmetric Push-Over** | -1.5 g | 3 seconds | No failure |
| **Rolling Maneuver** | ±3.0 g lateral | 3 seconds | No failure |
| **External Load (Objective)** | +3.75 g w/ 16,000 lb | 3 seconds | No failure |
| **Combined Loading** | Critical combined case | 3 seconds | No failure |
| **Test to Failure** | Progressive loading beyond ultimate | Until failure | Document failure mode |

**Total Ultimate Load Test Points:** 45  
**Success Criteria:**
- Sustain ultimate load (150% limit) for ≥3 seconds without catastrophic failure
- Failure mode (if occurs) is gradual and predictable, not sudden brittle fracture
- Primary load paths remain intact; secondary structure may yield

#### 6.3.3 Fatigue Test Campaign

**Duration:** 24 weeks (PM 47-53, critical path item)  
**Objective:** Demonstrate 2× design life (40,000 flight hours equivalent) without crack initiation

**Fatigue Spectrum:**
- Based on mission profile analysis (60% hover, 30% cruise, 10% maneuvering)
- Load sequences represent 100-hour mission block
- Accelerated testing: 1 calendar week = 200 flight hour equivalent

| Test Block | Flight Hours Represented | Load Cycles | Inspection Interval |
|------------|--------------------------|-------------|---------------------|
| **Block 1-40** | 0-8,000 hours | 1.2M cycles | Every 2,000 hr equivalent |
| **Block 41-100** | 8,000-20,000 hours | 1.8M cycles | Every 1,000 hr equivalent |
| **Block 101-200** | 20,000-40,000 hours | 3.0M cycles | Every 500 hr equivalent |

**Total Fatigue Cycles:** 6.0 million  
**Test Duration:** 24 weeks continuous operation

**Inspection Methods:**
- Visual inspection (every block)
- Ultrasonic NDI (every 5,000 hr equivalent)
- Thermography (continuous monitoring during testing)

**Success Criteria:**
- Zero crack initiation before 20,000 flight hour equivalent (1× design life)
- Crack growth analysis if cracks detected between 20,000-40,000 hours
- Meet MIL-STD-1530D damage tolerance requirements

#### 6.3.4 Fail-Safe and Damage Tolerance Testing

**Duration:** 6 weeks (PM 53-54)  
**Objective:** Validate fail-safe design and residual strength with damage

| Test | Damage Introduced | Success Criteria |
|------|-------------------|------------------|
| **Notched Element Test** | 2-inch crack in primary structure | Sustain limit load |
| **Severed Stiffener Test** | Single stiffener cut | Sustain limit load via load redistribution |
| **Corrosion Simulation** | 10% thickness loss (simulated) | Sustain limit load |
| **Battle Damage** | 0.50 cal penetration (simulated) | Sustain limit load |

**Success Criteria:**
- Structure with prescribed damage sustains limit load
- Load redistribution paths confirmed
- Inspection intervals established for damage detection

### 6.4 Phase 3 Deliverables and Success Criteria

| Deliverable | Completion Date | Content |
|-------------|-----------------|---------|
| **Limit Load Test Report** | PM 46 | 90 load cases, strain survey, FEM correlation |
| **Ultimate Load Test Report** | PM 48 | Ultimate load demonstration, margin verification |
| **Fatigue Test Report** | PM 54 | 40,000 hr life demonstration, inspection program |
| **Structural Substantiation Report** | PM 54 | Certification basis compliance (FAA Part 29.305-309) |

**Phase Exit Criteria:**
- 100% of certification load cases tested
- Ultimate load capability demonstrated (150% limit load)
- Fatigue life ≥2× design life (40,000 hours) demonstrated
- FEM correlation within ±10% for 95% of measurement locations
- Damage tolerance and fail-safe characteristics validated
- Zero open Category 1 structural anomalies

**Phase 3 Exit Gate:** Structural Qualification Review (PM 54)

---

## 7. PHASE 4: PROPULSION GROUND TESTING

**Duration:** 12 months (PM 45-57)  
**Objective:** Validate propulsion system performance, integration, and operability  
**Test Location:** Eurus Systems Propulsion Test Facility; Engine Manufacturer (selected tests)  
**Test Article:** DTA-2 (propulsion integration test stand)

### 7.1 Phase Overview

Propulsion ground testing validates the complete engine-transmission-rotor system in a ground-based environment before first flight. This phase addresses critical program risks:
- Engine/airframe integration issues
- Rotor system performance and vibration
- Fuel system functionality
- Thermal management effectiveness
- OEI capability verification

### 7.2 DTA-2 Configuration

**Test Stand Description:**
- Forward and aft rotor systems (production-representative)
- Twin turboshaft engines (production engines)
- Full transmission system (forward/aft/interconnect)
- Complete fuel system
- Engine control system (FADEC)
- Full instrumentation (pressures, temperatures, vibrations, performance)

**Thrust Measurement:**
- 6-component force balance (3-axis forces, 3-axis moments)
- Accurate to ±50 lb thrust, ±100 ft-lb torque

**Safety Systems:**
- Engine fire suppression
- Emergency rotor brake
- Automatic shutdown on overspeed, overtemp, or vibration exceedance

### 7.3 Test Campaigns

#### 7.3.1 Initial System Checkout

**Duration:** 4 weeks (PM 45-46)

| Test | Objective | Success Criteria |
|------|-----------|------------------|
| **Cold Rotation** | Mechanical integrity check | 50 RPM rotor rotation, no interference |
| **Fuel System Functional** | Verify fuel delivery | All flow rates, pressures per spec |
| **Engine Motoring** | Verify starter operation | Both engines motor to idle |
| **First Engine Start** | Validate start sequence | Both engines start, stabilize at idle |
| **Idle Operation** | Baseline performance | 30 min continuous idle, all parameters nominal |

#### 7.3.2 Performance Mapping

**Duration:** 12 weeks (PM 46-49)

**Test Matrix:** 150+ test points covering full engine/rotor operating envelope

| Operating Condition | RPM Range | Power Range | Data Points |
|---------------------|-----------|-------------|-------------|
| **Ground Idle** | 85-90% | 5-10% | 10 |
| **Flight Idle** | 95-97% | 15-25% | 15 |
| **Intermediate Power** | 100% | 30-70% | 40 |
| **Maximum Continuous** | 100% | 80-90% | 20 |
| **Takeoff Power (5 min)** | 100-102% | 95-100% | 15 |
| **OEI Contingency (2.5 min)** | 100-105% | 110-120% (single engine) | 10 |
| **Transient Maneuvers** | Variable | Variable | 40 |

**Performance Parameters Measured:**
- Rotor thrust and torque (each rotor independently)
- Engine fuel flow, SFC (specific fuel consumption)
- Rotor RPM, blade pitch angles
- Transmission input/output torques
- Oil temperatures and pressures
- Vibration (engine, transmission, rotor hubs)

**Success Criteria:**
- Maximum continuous power: ≥1,800 shp per engine @ 100% RPM, ISA SL
- Takeoff power: ≥2,000 shp per engine @ 100% RPM, 5 min rating
- OEI power: ≥2,400 shp (surviving engine) @ 105% RPM, 2.5 min rating
- Fuel consumption: ≤0.55 lb/shp-hr @ cruise power
- Combined rotor thrust: ≥26,000 lb @ MGTOW power setting

#### 7.3.3 Altitude Performance Testing

**Duration:** 6 weeks (PM 49-50)

**Test Facility:** Altitude test cell (simulated altitude via inlet depression)

| Simulated Altitude | Temperature | Power Setting | Objective |
|--------------------|-------------|---------------|-----------|
| **Sea Level** | ISA (59°F) | Max continuous | Baseline |
| **4,000 ft PA** | ISA+20°C (95°F) | Max continuous | Verify power retention |
| **8,000 ft PA** | ISA+20°C | Takeoff power | Hover performance (threshold) |
| **10,000 ft PA** | ISA+20°C | Takeoff power | Hover performance (objective) |
| **12,000 ft PA** | ISA | Cruise power | Service ceiling validation |

**Success Criteria:**
- Hover capability at 8,000 ft PA, ISA+20°C (threshold KPP)
- Engine performance degradation ≤predicted based on SAE ARP 1678
- No compressor stall or other operability issues

#### 7.3.4 OEI Testing Campaign

**Duration:** 6 weeks (PM 50-52)

| Test | Configuration | Objective |
|------|---------------|-----------|
| **Single-Engine Ground Runs** | One engine shut down | Verify OEI power rating, transmission capability |
| **OEI Transients** | Rapid power increase to OEI rating | 50 cycles, validate no overspeed/overtemp |
| **OEI Endurance** | 30 min continuous OEI power | Verify thermal management, no component distress |
| **Autorotation Entry** | Both engines to idle | Rotor RPM decay rate, energy management |
| **Engine Restart** | Mid-power restart simulation | Validate in-flight restart capability |

**Success Criteria:**
- Surviving engine sustains 2,400 shp for 2.5 min (OEI contingency rating) without exceedance
- Surviving engine sustains 2,100 shp for 30 min (OEI continuous rating)
- Transmission sustains OEI torque without damage
- Rotor RPM remains within safe band (90-107% nominal) during OEI transients

#### 7.3.5 Endurance and Reliability Testing

**Duration:** 12 weeks (PM 52-55)

**Test Profile:** 150-hour accelerated mission profile

| Mission Segment | Duration per Cycle | Power Setting | Total Cycles |
|-----------------|-----------------------|---------------|--------------|
| **Startup** | 5 min | Idle | 150 |
| **Hover Taxi** | 3 min | 40% power | 150 |
| **Takeoff** | 2 min | 100% power | 150 |
| **Climb** | 5 min | 80% power | 150 |
| **Cruise** | 30 min | 60% power | 150 |
| **Descent** | 5 min | 40% power | 150 |
| **Hover** | 10 min | 70% power | 150 |
| **Landing** | 2 min | 40% power | 150 |
| **Shutdown** | 3 min | Idle → Off | 150 |

**Total Mission Cycles:** 150 (equivalent to 150 flight hours)  
**Inspection Intervals:** Every 25 hours

**Success Criteria:**
- Zero unscheduled maintenance actions during 150-hour test
- All components (engines, transmission, rotor blades) remain within operational limits
- Vibration levels stable (no increasing trends indicative of wear)
- Oil consumption within specification
- MTBF projection ≥500 flight hours (threshold KSA)

#### 7.3.6 Environmental and Operability Testing

**Duration:** 4 weeks (PM 55-56)

| Test | Condition | Success Criteria |
|------|-----------|------------------|
| **Hot Start** | Ambient 52°C (126°F) | Successful start, stabilize at idle |
| **Cold Start** | Ambient -40°C (-40°F) | Successful start within 90 seconds |
| **High Humidity** | 95% RH, 35°C | No performance degradation |
| **Dust Ingestion** | MIL-STD-810H dust cloud | Inlet separator effectiveness >95% |
| **Rain Ingestion** | 2 in/hr water spray | No flameout, power loss <5% |
| **Icing Conditions** | Simulated ice accretion on inlets | Engine anti-ice system prevents ice buildup |

#### 7.3.7 Vibration Survey and Balancing

**Duration:** 4 weeks (PM 56-57)

**Objective:** Characterize vibration signature, optimize rotor balance and track

| Measurement Location | Acceptable Vibration Level | Measurement Method |
|----------------------|----------------------------|---------------------|
| **Cockpit** | <0.15 in/sec RMS | Triaxial accelerometers |
| **Cabin Floor** | <0.20 in/sec RMS | Triaxial accelerometers |
| **Rotor Hubs** | <0.50 in/sec RMS | Hub-mounted accelerometers |
| **Transmission Mounts** | <0.40 in/sec RMS | Triaxial accelerometers |

**Blade Tracking:** ±0.5 in tip-to-tip variation (threshold), ±0.25 in (objective)

**Rotor Balancing Process:**
- Initial static balance (blade weight within ±0.5 lb)
- Dynamic balance at operating RPM
- Cross-rotor phasing optimization (minimize tandem interference vibration)

### 7.4 Phase 4 Deliverables and Success Criteria

| Deliverable | Completion Date | Content |
|-------------|-----------------|---------|
| **Performance Test Report** | PM 52 | Power, thrust, fuel consumption validation |
| **Altitude Performance Report** | PM 51 | Hot/high hover capability demonstration |
| **OEI Test Report** | PM 53 | Single-engine operability validation |
| **Endurance Test Report** | PM 56 | 150-hour reliability demonstration |
| **Vibration Survey Report** | PM 57 | Baseline vibration signature, balancing data |
| **Propulsion System Qualification** | PM 57 | Certification compliance (FAA Part 29 Subpart E) |

**Phase Exit Criteria:**
- Maximum continuous power ≥1,800 shp/engine (threshold), ≥2,000 shp (objective)
- Hover ceiling OGE ≥8,000 ft PA, ISA+20°C (threshold KPP)
- OEI capability demonstrated per PRB requirements
- 150-hour endurance test completed without major anomalies
- Vibration levels within acceptable limits
- Fuel consumption meets specification (≤0.55 lb/shp-hr)
- Zero open Category 1 propulsion anomalies

**Phase 4 Exit Gate:** Propulsion System Qualification Review (PM 57)

---

## 8. PHASE 5: ENVIRONMENTAL QUALIFICATION

**Duration:** 12 months (PM 48-60)  
**Objective:** Qualify aircraft systems to full environmental operating envelope  
**Test Location:** Multiple environmental test facilities (Eurus, suppliers, independent labs)  
**Test Articles:** DTA-3 (avionics), environmental test specimens, production LRUs

### 8.1 Phase Overview

Environmental qualification validates system functionality and structural integrity across the full range of environmental conditions specified in PRB Section 3.3 and KSD Section 10:

- Temperature: -40°C to +52°C (objective)
- Altitude: -1,000 ft to +14,000 ft PA
- Humidity: 0% to 95% RH
- Sand, dust, salt fog, rain, icing
- Solar radiation, fungus resistance
- Vibration, shock, acoustic
- Electromagnetic environment (EMI/EMC, lightning, HIRF)

### 8.2 Test Standards and Specifications

**Primary Test Standards:**
- **MIL-STD-810H:** Environmental Engineering Considerations and Laboratory Tests
- **DO-160G:** Environmental Conditions and Test Procedures for Airborne Equipment
- **MIL-STD-464D:** Electromagnetic Environmental Effects (E3) Requirements
- **MIL-STD-461G:** Requirements for the Control of Electromagnetic Interference
- **RTCA DO-160G Section 20:** Radio Frequency Susceptibility (HIRF)

### 8.3 Test Campaigns

#### 8.3.1 Temperature Testing

**Test Facility:** Environmental chamber (temp range -54°C to +85°C)

| System Under Test | Low Temp Test | High Temp Test | Operating Test | Success Criteria |
|-------------------|---------------|----------------|----------------|------------------|
| **Avionics LRUs** | -54°C, 4 hr soak | +71°C, 4 hr soak | Functional @ extremes | 100% functionality |
| **Flight Control Actuators** | -40°C | +71°C | Full rate, load capacity | No performance loss |
| **Hydraulic System** | -40°C | +71°C | Pressure, flow per spec | ≤10% performance change |
| **Composite Structure** | -54°C | +85°C | Static load test @ temp | No strength degradation |
| **Battery System** | -20°C | +60°C | Charge/discharge cycles | ≥80% capacity retained |
| **Engine Systems** | -40°C cold start | +52°C hot start | Start within 90 sec | Meet start criteria |

**Test Duration:** 8 weeks (PM 48-50)

**Success Criteria:**
- All systems functional across operating temperature range (-40°C to +52°C objective)
- Non-operating storage: -54°C to +71°C (4-hour soak, no damage)
- Composite structure: No strength loss >5% at temperature extremes

#### 8.3.2 Altitude Testing

**Test Facility:** Altitude chamber (simulated altitude to 50,000 ft)

| Test | Simulated Altitude | Objective | Success Criteria |
|------|-------------------|-----------|------------------|
| **Avionics Cooling** | 14,000 ft (max operating) | Verify cooling effectiveness | Component temps <limits |
| **Pressurization Systems** | 14,000 ft | Cabin differential (unpressurized design) | Ambient pressure maintained |
| **Oxygen System** | >10,000 ft | Crew oxygen delivery (if required) | Flow rate per MIL-PRF-27210 |
| **Battery Performance** | 14,000 ft | Verify capacity at altitude | ≥95% sea level capacity |
| **Rapid Decompression** | 14,000 ft → SL in 5 sec | Structural integrity | No damage to cabin structure |

**Test Duration:** 4 weeks (PM 50-51)

#### 8.3.3 Humidity and Fungus Resistance

**Test Facility:** Humidity/fungus chamber

| Test | Conditions | Duration | Standard | Success Criteria |
|------|-----------|----------|----------|------------------|
| **Humidity Exposure** | 95% RH, 35°C | 10 days | MIL-STD-810H Method 507.6 | No corrosion, electrical leakage <spec |
| **Fungus Resistance** | Fungal spore exposure | 28 days | MIL-STD-810H Method 508.7 | No fungal growth on surfaces |
| **Salt Fog** | 5% NaCl fog | 48 hours | MIL-STD-810H Method 509.6 | No corrosion initiation |

**Test Duration:** 6 weeks (PM 51-52)

#### 8.3.4 Sand, Dust, and Rain

**Test Facility:** Environmental chamber with particulate/water spray

| Test | Conditions | Standard | Success Criteria |
|------|-----------|----------|------------------|
| **Blowing Sand** | 29 m/s wind, sand injection | MIL-STD-810H Method 510.6 Proc I | Engine inlet separator >95% effective |
| **Blowing Dust** | 18 m/s wind, dust cloud | MIL-STD-810H Method 510.6 Proc II | No ingestion into sealed compartments |
| **Dust Cloud** | 10.6 g/m³ concentration | MIL-STD-810H Method 510.6 Proc III | Avionics bay sealing effective |
| **Rain (Blowing)** | 2 in/hr, 18 m/s wind | MIL-STD-810H Method 506.6 Proc II | No water intrusion, rotor ice shedding functional |
| **Rain (Drip)** | Static soak, 1 in/hr | MIL-STD-810H Method 506.6 Proc I | Electrical systems isolated, no short circuits |

**Test Duration:** 6 weeks (PM 52-54)

**Critical Validation:** Brownout operations (DVE sensor effectiveness in dust cloud)

#### 8.3.5 Icing Testing (Optional System, MAAP-1I/C)

**Test Facility:** Icing wind tunnel

| Test | Icing Conditions | Success Criteria |
|------|------------------|------------------|
| **Engine Anti-Ice** | -20°C, supercooled droplets | No ice buildup on inlet guide vanes |
| **Rotor Blade Deicing** | Ice accretion 0.5 in thickness | Electrothermal system removes ice in <60 sec |
| **Windscreen Anti-Ice** | -15°C, freezing rain | Clear view maintained (MAAP-1F optionally-piloted) |
| **Sensor Window Heating** | Ice accumulation on EO/IR | Sensor FOV unobstructed |

**Test Duration:** 4 weeks (PM 54-55, if icing system selected)

#### 8.3.6 Solar Radiation and Thermal Cycling

**Test Facility:** Solar simulation chamber

| Test | Conditions | Duration | Success Criteria |
|------|-----------|----------|------------------|
| **Solar Heating** | 1120 W/m² irradiance, +49°C ambient | 8 hours | Surface temps <material limits |
| **Thermal Cycling** | -40°C to +85°C, 50 cycles | 10 days | No delamination, cracking, or coating failure |
| **IR Signature** | Solar loading + operational heat | Steady-state | IR signature <threshold (if specified) |

**Test Duration:** 3 weeks (PM 55-56)

#### 8.3.7 Vibration, Shock, and Acoustic Testing

**Test Facility:** Structural dynamics lab

**Vibration Testing (DO-160G Categories):**

| Equipment Category | Vibration Level | Test Duration | Success Criteria |
|--------------------|-----------------|---------------|------------------|
| **Flight Controls (Cat A)** | 7.5 Grms, 10-2000 Hz | 3 hr/axis | Functional during + after |
| **Avionics (Cat B)** | 5.0 Grms, 10-2000 Hz | 2 hr/axis | Functional during + after |
| **Mission Systems (Cat C)** |

## 8. PHASE 5: ENVIRONMENTAL QUALIFICATION *(continued)*

### 8.3 Test Campaigns *(continued)*

#### 8.3.7 Vibration, Shock, and Acoustic Testing *(continued)*

**Vibration Testing (DO-160G Categories):** *(continued)*

| Equipment Category | Vibration Level | Test Duration | Success Criteria |
|--------------------|-----------------|---------------|------------------|
| **Mission Systems (Cat C)** | 3.0 Grms, 10-2000 Hz | 1 hr/axis | Functional during + after |
| **Structural Items (Cat S)** | 10.0 Grms, 5-2000 Hz | 3 hr/axis | No structural damage |

**Shock Testing:**

| Test | Shock Profile | Success Criteria |
|------|---------------|------------------|
| **Crash Safety Pulse** | 20g half-sine, 11 ms duration | No hazardous failures (fuel, electrical, structural) |
| **Hard Landing Shock** | 6g sawtooth, 40 ms duration | Equipment remains functional |
| **Emergency Landing** | 30 ft/s vertical impact simulation | Survivable crew environment per MIL-STD-1290 |

**Acoustic Testing:**

| Test | Sound Pressure Level | Duration | Success Criteria |
|------|---------------------|----------|------------------|
| **External Acoustic (takeoff)** | 140 dB overall, 10 min | Continuous | No structural resonance issues |
| **Internal Cabin Noise** | 95 dB @ max continuous power | 4 hours | Meets crew exposure limits per MIL-STD-1474E |
| **Avionics Bay Acoustic** | 130 dB random vibration | 2 hours | No equipment malfunction |

**Test Duration:** 10 weeks (PM 56-58)

#### 8.3.8 Lightning Strike and HIRF Testing

**Test Facility:** High-voltage laboratory, anechoic chamber

| Test | Standard | Test Condition | Success Criteria |
|------|----------|----------------|------------------|
| **Direct Lightning Strike (Zone 1A)** | MIL-STD-464D | 200 kA peak, 2×10⁶ A²s action integral | No penetration, no critical system damage |
| **Indirect Lightning (Zone 2)** | MIL-STD-464D | Conducted transients on wiring | All systems functional during + after |
| **HIRF Illumination** | RTCA DO-160G Sec 20, Cat M | 100-18,000 MHz, 7,200 V/m field strength | No upset, loss of function, or erroneous data |
| **Radiated Emissions** | MIL-STD-461G CE102 | 10 kHz - 18 GHz | <Limit curves for RE102 |
| **Conducted Emissions** | MIL-STD-461G CE101/CE106 | Power and data lines | <Limit curves |

**Lightning Protection Design Features:**
- Composite structure with embedded aluminum mesh (0.125 in spacing)
- Lightning diverter strips on rotor blades (stainless steel)
- Bonding resistance <2.5 mΩ between major assemblies
- Shielded wiring harnesses with 360° terminations
- Transient suppression on all avionics interfaces

**Test Duration:** 8 weeks (PM 58-60)

**Success Criteria:**
- Zero critical system failures during lightning/HIRF exposure
- All flight-critical systems maintain operation or recover within 5 seconds
- No permanent damage requiring more than inspection/minor repair

### 8.4 Phase 5 Deliverables and Success Criteria

| Deliverable | Completion Date | Content |
|-------------|-----------------|---------|
| **Temperature Qualification Report** | PM 50 | All temperature extremes tested, pass/fail data |
| **Altitude Qualification Report** | PM 51 | 14,000 ft PA operational validation |
| **Humidity/Fungus Test Report** | PM 52 | 95% RH, salt fog, fungus resistance verified |
| **Sand/Dust/Rain Test Report** | PM 54 | MIL-STD-810H Method 506/510 compliance |
| **Icing Qualification Report** | PM 55 | Ice protection system effectiveness (if applicable) |
| **Vibration/Shock/Acoustic Report** | PM 58 | DO-160G compliance across all categories |
| **EMI/EMC/Lightning Report** | PM 60 | MIL-STD-461G, MIL-STD-464D, DO-160G compliance |
| **Environmental Qualification Summary** | PM 60 | Consolidated certification basis compliance matrix |

**Phase Exit Criteria:**
- 100% of environmental test points executed per PRB Section 3.3 requirements
- All qualification testing complete with <5% re-test rate
- Zero open Category 1 environmental defects
- Certification authorities (FAA, DoD) preliminary acceptance of test data
- Environmental design margins documented and within acceptable limits
- All test anomalies closed with corrective action verification

**Phase 5 Exit Gate:** Environmental Qualification Review (PM 60)

---

## 9. PHASE 6: DEVELOPMENTAL FLIGHT TEST

**Duration:** 18 months (PM 54-72)  
**Objective:** Expand flight envelope, verify performance, validate autonomous systems in flight  
**Test Location:** Edwards AFB, CA (primary); China Lake NAWS, CA; Yuma Proving Ground, AZ  
**Test Articles:** FTA-1 (first flight), FTA-2 (envelope expansion), FTA-3 (performance validation)

### 9.1 Phase Overview

Developmental Flight Test (DFT) is the critical validation phase where the MAAP-1 transitions from ground-tested hardware to a flying aircraft demonstrating full operational capability. This phase directly addresses:

- **Airworthiness Certification:** FAA Part 29 and military airworthiness compliance demonstration
- **Flight Envelope Expansion:** Systematic exploration of speed, altitude, and maneuvering limits
- **Performance Validation:** Verification of all KPPs requiring flight test (hover, speed, range, endurance)
- **Autonomous GNC Validation:** Real-world validation of autonomy, DAA, and lost-link procedures
- **Handling Qualities:** Pilot (optionally-piloted variant) and autonomous control law refinement

**Flight Test Philosophy:**
- **Incremental Envelope Expansion:** Small, safe steps from known conditions to envelope limits
- **Build-Up Approach:** Ground test → taxi → hover → low-speed flight → cruise → high-speed → full envelope
- **Redundant Safety:** Chase aircraft, real-time telemetry monitoring, abort procedures for all test points
- **Data-Driven Decisions:** No envelope expansion without thorough analysis of previous test data

### 9.2 Flight Test Organization

```
┌────────────────────────────────────────────────────────┐
│          FLIGHT TEST ORGANIZATION                      │
└────────────────────────────────────────────────────────┘

                    ┌──────────────────┐
                    │  Flight Test     │
                    │  Director        │
                    └────────┬─────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
┌───────▼────────┐                       ┌───────▼────────┐
│ Chief Test Pilot│                      │ Flight Test    │
│                 │                      │ Engineers      │
└───────┬────────┘                       └───────┬────────┘
        │                                         │
    ┌───┴────┬──────┐                    ┌───────┴────┬───────┐
┌───▼───┐ ┌──▼───┐ ┌▼────┐          ┌───▼────┐ ┌─────▼────┐ ┌▼──────┐
│Test   │ │Safety│ │Chase│          │Inst.   │ │Data      │ │Flight │
│Pilots │ │Pilot │ │Pilot│          │Engineer│ │Analysis  │ │Ops    │
└───────┘ └──────┘ └─────┘          └────────┘ └──────────┘ └───────┘
```

**Key Roles:**
- **Flight Test Director:** Overall test program authority, risk acceptance
- **Chief Test Pilot:** Flight safety authority, test execution oversight
- **Test Pilots (3×):** Execute flight test cards, provide qualitative assessment
- **Safety Pilot:** Independent safety observer, emergency authority
- **Flight Test Engineers (12×):** Test planning, data analysis, requirements verification
- **Instrumentation Engineer:** Test instrumentation, data acquisition systems
- **Data Analysts (4×):** Real-time and post-flight data processing
- **Flight Operations (8×):** Aircraft preparation, maintenance, mission planning

### 9.3 Flight Test Articles Configuration

#### FTA-1: First Flight Article (MAAP-1C Configuration)
- **Purpose:** First flight, initial handling qualities, low-risk envelope expansion
- **Configuration:** Baseline cargo variant, minimal mission systems
- **Instrumentation:** 1,200 data channels, 100 Hz sampling
- **Weight:** 14,800 lb empty (instrumentation adds 600 lb over production)
- **Special Equipment:** Spin recovery chute, emergency drag chute, crashworthy flight test instrumentation recorder

#### FTA-2: Envelope Expansion Article (MAAP-1F Configuration)
- **Purpose:** High-speed flight, external load testing, firefighting mission validation
- **Configuration:** MAAP-1F (firefighting) with full mission systems
- **Instrumentation:** 1,500 data channels, 200 Hz sampling (dynamic loads focus)
- **Special Features:** Flutter excitation system, airdata boom, high-speed cameras

#### FTA-3: Performance Validation Article (MAAP-1I Configuration)
- **Purpose:** ISR mission systems integration, autonomy validation, production representative
- **Configuration:** MAAP-1I (ISR) with full sensor suite
- **Instrumentation:** 1,000 data channels (production-representative installation)
- **Special Focus:** Autonomous mission execution, DAA system validation, GPS-denied navigation

### 9.4 Test Campaigns

#### 9.4.1 Phase 6A: First Flight and Initial Envelope (PM 54-60, FTA-1)

**Duration:** 6 months  
**Flight Hours:** 60 hours (45 flights)  
**Test Location:** Edwards AFB

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Ground Operations** | 0 | Pre-flight validation, taxi tests | Ground handling characteristics acceptable |
| **First Flight** | 1 | Takeoff, hover, basic controllability, landing | Safe flight operations demonstrated |
| **Hover Envelope** | 8 | Hover performance, OGE/IGE, controllability | Hover ceiling ≥8,000 ft PA ISA+20°C (threshold KPP) |
| **Low-Speed Flight** | 10 | 50-100 KTAS, basic maneuvering, autorotation entry | Handling qualities Level 1 or 2 |
| **Cruise Envelope** | 12 | 100-135 KTAS, climb/descent, basic autopilot modes | Cruise speed ≥135 KTAS (threshold KPP) |
| **Systems Validation** | 8 | Propulsion, fuel, electrical, hydraulic, flight controls | All systems nominal performance |
| **Emergency Procedures** | 6 | Simulated failures, OEI operations, autorotation | Safe recovery from all critical failures |

**Key Test Points:**
- **First Flight (PM 54, Flight 1):** 30-minute flight, pattern work, basic handling assessment
- **Hover Ceiling Test (PM 56, Flight 12):** Demonstrate 8,000 ft PA hover at ISA+20°C, MGTOW
- **VNE Approach (PM 59, Flight 40):** Incremental speed build to 90% VNE (148 KTAS)
- **OEI Hover (PM 60, Flight 45):** Single-engine hover capability demonstration

**First Flight Criteria:**
- FTA-1 final assembly complete, all systems functional
- Ground run testing complete (50+ hours engine operation)
- Taxi testing complete (high-speed taxi to 80 KIAS)
- Flight Readiness Review (FRR) complete, signed flight clearance
- Weather: VFR, winds <15 kt, no precipitation
- Emergency recovery assets positioned (crash/fire/rescue)

**Success Criteria:**
- Zero Class A or B flight test mishaps
- All test points executed within ±10% planned test conditions
- Handling qualities assessed as Level 1 or 2 (Cooper-Harper scale)
- No flight control system anomalies requiring design changes
- Hover ceiling threshold KPP demonstrated

#### 9.4.2 Phase 6B: Envelope Expansion (PM 60-66, FTA-2)

**Duration:** 6 months  
**Flight Hours:** 180 hours (75 flights)  
**Test Location:** Edwards AFB, China Lake NAWS

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **High-Speed Envelope** | 15 | VNE validation (165 KTAS), high-speed handling | VNE demonstrated, no adverse characteristics |
| **Altitude Envelope** | 12 | Service ceiling (12,000 ft threshold), climb performance | Service ceiling ≥12,000 ft at MGTOW |
| **Maneuvering Envelope** | 18 | Load factor limits, bank angle, unusual attitudes | +3.5g / -1.0g demonstrated safely |
| **External Load Operations** | 20 | 12,000 lb sling load (threshold), 16,000 lb (objective) | Stable flight with external loads per KPP |
| **Hot/High Performance** | 10 | Yuma summer operations (ISA+20°C, 2,000 ft PA) | Performance margins confirmed |
| **Autorotation Envelope** | 10 | Full autorotation landings, height-velocity diagram | Safe autorotation from all flight regimes |

**Critical Test Points:**
- **VNE Flight (PM 62, Flight 58):** Approach and maintain VNE (165 KTAS) for 5 minutes, assess stability
- **Maximum Load Factor (PM 63, Flight 65):** +3.5g symmetrical pull, verify structural loads within limits
- **16,000 lb External Load (PM 64, Flight 70):** Objective external load demonstration, stability assessment
- **Service Ceiling (PM 65, Flight 72):** Climb to 12,000 ft at MGTOW, demonstrate 100 fpm climb capability
- **Autorotation Landing (PM 66, Flight 75):** Full autorotation from 3,000 ft AGL to touchdown

**Envelope Expansion Approach:**
- Each flight expands envelope by maximum 10% speed, 2,000 ft altitude, or 0.5g load factor
- Real-time telemetry monitoring: if any parameter exceeds 90% limit, terminate test point
- Post-flight analysis required before next expansion increment
- Flight Test Review Board approval required for test points approaching limits

**Success Criteria:**
- Full flight envelope explored: 0-165 KTAS, 0-14,000 ft PA, +3.5g / -1.0g
- External load KPP threshold (12,000 lb) and objective (16,000 lb) demonstrated
- Autorotation capability validated across speed range
- No flutter, vibration, or handling qualities issues discovered
- All envelope boundaries documented and verified

#### 9.4.3 Phase 6C: Performance Validation (PM 64-69, FTA-2 and FTA-3)

**Duration:** 5 months  
**Flight Hours:** 140 hours (60 flights)  
**Test Location:** Edwards AFB, Yuma Proving Ground

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Range & Endurance** | 12 | Mission radius with external loads, ferry range | ≥125 nm radius with 12,000 lb load (threshold KPP) |
| **Fuel Consumption** | 8 | Validate fuel flow models, optimize cruise profiles | Fuel consumption ≤predicted +5% |
| **Climb Performance** | 6 | Rate of climb, time to altitude, optimum climb speed | ROC ≥1,800 fpm at SL, MGTOW (threshold) |
| **Payload-Range Trades** | 10 | Validate performance across payload spectrum | Performance curve matches predictions |
| **Hot-Day Performance** | 8 | ISA+20°C operations, power margins | Hover ceiling 8,000 ft ISA+20°C verified |
| **OEI Performance** | 10 | Single-engine climb, hover, cruise capabilities | OEI KPPs demonstrated per PRB |
| **Acoustic Signature** | 6 | Noise measurements per FAA Part 36 equivalent | <95 dBA @ 500 ft lateral (threshold) |

**Key Performance Demonstration Flights:**
- **Design Mission Demonstration (PM 66, Flight 82):** Fly complete design mission profile: takeoff with 12,000 lb external load, transit 125 nm, release load, return. Demonstrate 30 min fuel reserve remaining.
- **Ferry Range (PM 67, Flight 88):** Maximum internal fuel, no payload, fly to fuel exhaustion (emergency landing site). Demonstrate ≥450 nm range (threshold KPP).
- **Hot Hover (PM 68, Flight 92):** Yuma, ISA+20°C day, demonstrate OGE hover at 8,000 ft PA with MGTOW.
- **OEI Climb (PM 69, Flight 95):** Simulate engine failure at MGTOW, demonstrate positive rate of climb on single engine.

**Performance Data Collection:**
- GPS-based airspeed/groundspeed calibration
- Fuel flow instrumentation (±0.5% accuracy)
- Weight and balance monitoring (±50 lb accuracy)
- Atmospheric data (temperature, pressure, density altitude)
- Post-flight performance analysis against PRB requirements

**Success Criteria:**
- All KPP performance thresholds demonstrated in flight test
- 85% of KPP objectives achieved (stretch goals)
- Performance models validated within ±5% measured data
- No adverse performance trends discovered
- OEI performance sufficient for safe recovery from critical failures

#### 9.4.4 Phase 6D: Autonomous GNC & Mission Systems (PM 66-72, FTA-3)

**Duration:** 6 months  
**Flight Hours:** 180 hours (70 flights)  
**Test Location:** Edwards AFB, China Lake NAWS (GPS-denied test range)

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Autonomous Takeoff/Landing** | 15 | Precision autonomous landing (±1 m CEP target) | Landing CEP ≤1 m (95% of landings) |
| **Waypoint Navigation** | 12 | GPS-based autonomous navigation accuracy | Navigation accuracy ≤10 m CEP |
| **GPS-Denied Navigation** | 10 | INS + TRN operation, drift characterization | <50 m drift after 15 min GPS denial (threshold) |
| **Detect and Avoid (DAA)** | 18 | Collision avoidance with cooperative/non-cooperative targets | 100% collision avoidance, <1% false alarm rate |
| **Lost-Link Procedures** | 8 | RTL, loiter, automatic landing sequences | 100% successful lost-link recoveries |
| **Mission Re-Planning** | 10 | Dynamic waypoint updates, weather avoidance | Real-time re-plan within 30 seconds |
| **ISR Mission Profile** | 12 | EO/IR sensor operations, target tracking, data downlink | Mission success rate >95% |

**Autonomous System Test Scenarios:**

**Scenario 1: Autonomous Mission Execution (PM 68, Flight 110)**
- GCS uploads mission plan: 4-waypoint route, 150 nm total, ISR sensor operations at WP2 and WP3
- Aircraft executes fully autonomous: taxi, takeoff, climb, cruise navigation, sensor operations, landing
- Success: Mission completion with zero human intervention, all waypoints within 10 m, sensors functional

**Scenario 2: DAA Collision Avoidance (PM 69, Flight 115)**
- Scripted encounters with cooperative aircraft (ADS-B equipped) and non-cooperative (RADAR-only detection)
- Test intruder trajectories: head-on, crossing, overtaking
- Success: Aircraft detects all intruders at required range, executes avoidance maneuvers automatically, resumes mission

**Scenario 3: GPS-Denied Operations (PM 70, Flight 120)**
- Aircraft navigates to GPS-denied test range, GPS jammed
- INS + Terrain-Relative Navigation (TRN) maintains position knowledge
- Success: Position error <50 m after 15 minutes GPS denial (threshold requirement)

**Scenario 4: Lost-Link Recovery (PM 71, Flight 125)**
- Datalink intentionally terminated during various flight phases (cruise, hover, approach)
- Aircraft executes autonomous lost-link procedure: loiter 2 min → RTL if no re-contact → land at pre-planned safe site
- Success: 100% successful autonomous recovery, no human intervention required

**Autonomous GNC Performance Metrics:**
- **Reliability Target:** 1×10⁻⁷ loss-of-control events per flight hour (demonstrated via test + analysis combination)
- **Navigation Accuracy:** <10 m CEP (GPS), <50 m after 15 min GPS-denied
- **Landing Precision:** ±1 m CEP (autonomous precision landing)
- **DAA Detection Range:** 10 nm cooperative, 3 nm non-cooperative (RADAR)
- **False Alarm Rate:** <1 per 100 flight hours

**Success Criteria:**
- Autonomous flight operations demonstrated for all mission phases
- DAA system meets ASTM F3442 performance standards
- GPS-denied navigation threshold requirement verified
- Lost-link procedures 100% successful (no loss of aircraft)
- Autonomy reliability analysis supports 1×10⁻⁷ target (combined test + FMEA + DO-178C DAL A software rigor)
- ISR mission systems fully functional in flight

### 9.5 Flight Test Instrumentation and Data Acquisition

**FTA Instrumentation Channels:**

| System | Parameters Measured | Sample Rate | Accuracy |
|--------|---------------------|-------------|----------|
| **Flight Dynamics** | Airspeed, altitude, attitude, rates, accelerations | 100 Hz | ±0.5% full scale |
| **Propulsion** | Engine RPM, EGT, fuel flow, torque, oil pressure/temp | 50 Hz | ±1% |
| **Rotor System** | Rotor RPM, blade pitch, flapping/lagging angles, hub loads | 200 Hz | ±0.5% |
| **Flight Controls** | Control positions, actuator forces, pilot inputs | 100 Hz | ±0.25% |
| **Structures** | Strain gauges (200 locations), accelerometers (50 locations) | 200 Hz | ±1% |
| **Autonomous GNC** | GPS position, INS data, autopilot commands, mode status | 20 Hz | ±0.1 m (GPS) |
| **Mission Systems** | Sensor status, datalink throughput, payload power | 10 Hz | Event-based |

**Data Systems:**
- Onboard Data Acquisition System (DAS): 2,000 channel capacity, 1 TB solid-state storage
- Real-Time Telemetry: 10 Mbps downlink to ground station, 200 ms latency
- Ground Station: Real-time display, limit monitoring, voice communication with crew
- Post-Flight Analysis: Automated report generation, trend analysis, requirements verification matrix updates

**Data Quality Assurance:**
- Pre-flight instrumentation calibration checks (daily)
- In-flight data quality monitoring (real-time)
- Post-flight data validation (within 24 hours)
- Data archival and configuration control (lifetime retention)

### 9.6 Flight Test Safety and Risk Management

**Flight Test Safety Organization:**
- Independent Flight Test Safety Officer (reports directly to Program Manager, not Flight Test Director)
- Safety Review Board: convenes before each new test phase, reviews hazard analysis and risk mitigation
- Real-Time Safety Monitoring: Ground-based safety observer with authority to terminate test

**Hazard Analysis:**
- Preliminary Hazard Analysis (PHA) complete prior to first flight
- Flight Test Hazard Analysis updated for each test phase
- Critical hazards mitigated to acceptable risk levels (per MIL-STD-882E)

**Risk Mitigation Measures:**
- Chase aircraft for all initial envelope expansion flights
- Restricted airspace with emergency landing zones identified
- Crash/fire/rescue assets on standby during all flights
- Flight termination system (not installed on MAAP-1, instead: autonomous return-to-base capability)
- Spin recovery chute (FTA-1 and FTA-2 only)

**Abort Criteria:**
- Any flight control system malfunction or degraded mode
- Propulsion system parameters outside normal limits (>10%)
- Structural loads approaching design limits (>90%)
- Autonomous system disengagement when not planned
- Weather deterioration below VFR minimums
- Any condition assessed by crew or ground as unsafe

**Emergency Procedures:**
- Engine failure: Autorotation or OEI climb depending on altitude/airspeed
- Flight control failure: Reversion to backup control modes, emergency landing
- Lost datalink (autonomous mode): Execute autonomous RTL procedure
- Fire: Immediate landing at nearest suitable site
- Uncontrolled flight: Crew egress if equipped; autonomous aircraft executes emergency landing

### 9.7 Phase 6 Deliverables and Success Criteria

| Deliverable | Completion Date | Content |
|-------------|-----------------|---------|
| **Flight Test Plan** | PM 52 | Comprehensive test plan, all test cards, safety analysis |
| **First Flight Report** | PM 55 | Flight 1 data, handling qualities assessment, lessons learned |
| **Phase 6A Test Report** | PM 60 | Initial envelope expansion data, 60 flight hours summary |
| **Phase 6B Test Report** | PM 66 | Full envelope expansion, external load testing |
| **Phase 6C Test Report** | PM 69 | Performance validation, KPP verification data |
| **Phase 6D Test Report** | PM 72 | Autonomous GNC validation, mission systems integration |
| **Flight Test Final Report** | PM 72 | Consolidated DFT results, requirements verification, certification data |
| **Airworthiness Compliance Matrix** | PM 72 | FAA Part 29 and MIL-HDBK-516C compliance demonstration |

**Phase Exit Criteria:**
- **Total Flight Hours:** ≥560 hours across 3 FTAs
- **KPP Verification:** 100% of threshold KPPs verified in flight test, 85% of objective KPPs demonstrated
- **Envelope Validation:** Full flight envelope explored and boundaries documented
- **Autonomous System Validation:** Autonomous flight operations demonstrated across all mission phases
- **External Load Capability:** 12,000 lb (threshold) and 16,000 lb (objective) demonstrated in flight
- **Safety Record:** Zero Class A mishaps, <2 Class B mishaps
- **Open Deficiencies:** Zero Category 1 (flight safety) defects; <10 Category 2 (performance) defects with approved corrective action plans
- **Airworthiness Recommendation:** Flight Test organization recommends aircraft for operational use
- **Certification Authority Acceptance:** FAA and/or DoD preliminary acceptance of flight test data package

**Phase 6 Exit Gate:** Developmental Flight Test Completion Review (PM 72)

**Certification Readiness Assessment:**
- Flight test data sufficient to support FAA Type Certificate application
- All FAA Part 29 certification test points complete
- Compliance demonstration for Special Conditions (autonomous operations)
- Military airworthiness assessment (MIL-HDBK-516C) substantially complete

---

## 10. PHASE 7: SWARM & MULTI-AIRCRAFT TESTING

**Duration:** 12 months (PM 66-78, overlaps with Phase 6)  
**Objective:** Validate multi-aircraft autonomous operations, swarm coordination, and formation flight  
**Test Location:** China Lake NAWS (restricted airspace, large test range)  
**Test Articles:** FTA-4, FTA-5, FTA-6 (identical MAAP-1C configuration initially)

### 10.1 Phase Overview

Multi-aircraft testing addresses the program's unique challenge: autonomous coordination of multiple MAAP-1 aircraft operating simultaneously in the same airspace. This capability is critical for:
- **Cargo Logistics:** Multi-ship resupply missions with autonomous formation flight
- **Firefighting:** Coordinated aerial firefighting operations with multiple aircraft
- **ISR:** Distributed sensor networks with autonomous sensor fusion
- **Military Operations:** Autonomous wingman concepts, swarm tactics

**Key Technical Challenges:**
- **Collision Avoidance:** Prevent mid-air collisions between friendly autonomous aircraft
- **Formation Maintenance:** Maintain precise spacing (±5 m) during formation flight
- **Communications:** Robust inter-aircraft datalink with <100 ms latency
- **Mission Coordination:** Distributed autonomous decision-making without central authority
- **Graceful Degradation:** Safe operations if one or more aircraft experience failures

### 10.2 Swarm Architecture Overview

```
┌────────────────────────────────────────────────────────┐
│          SWARM COORDINATION ARCHITECTURE               │
└────────────────────────────────────────────────────────┘

              ┌──────────────────┐
              │  Ground Control  │
              │  Station (GCS)   │
              └────────┬─────────┘
                       │ Mission-level tasking
                       │ (Strategic commands)
         ┌─────────────┴─────────────┬──────────────┐
         │                           │              │
    ┌────▼────┐                 ┌────▼────┐   ┌────▼────┐
    │ FTA-4   │◄───────────────►│ FTA-5   │◄─►│ FTA-6   │
    │ (Leader)│  Peer-to-peer   │(Wingman)│   │(Wingman)│
    └─────────┘  coordination   └─────────┘   └─────────┘
         │                           │              │
         └─────────────┬─────────────┴──────────────┘
                       │ Distributed decision-making
                       │ Formation maintenance
                       │ Collision avoidance

Legend:
────► Command/Control link (GCS → Aircraft)
◄───► Peer-to-peer coordination link (Aircraft ↔ Aircraft)
```

**Architecture Principles:**
- **Distributed Autonomy:** No single point of failure; any aircraft can assume leader role
- **Peer-to-Peer Communication:** Direct aircraft-to-aircraft datalink (C-band, 10 Mbps, 150 nm range)
- **Consensus Algorithms:** Formation geometry determined by distributed consensus, not centralized command
- **GCS Role:** Mission-level tasking only ("Fly formation to Point Alpha"); aircraft autonomously coordinate execution

### 10.3 Test Campaigns

#### 10.3.1 Phase 7A: Two-Ship Operations (PM 66-70, FTA-4 and FTA-5)

**Duration:** 4 months  
**Flight Hours:** 80 hours (40 flights, 20 per aircraft)  
**Test Location:** China Lake NAWS

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Communication Validation** | 4 | Peer-to-peer datalink functionality, range, latency | <100 ms latency, >99.5% message delivery |
| **Formation Join-Up** | 6 | Autonomous rendezvous, formation establishment | Join-up time <5 min from 10 nm separation |
| **Trail Formation** | 8 | Maintain trail position (500 ft aft, same altitude) | Spacing error ±50 ft, 95% of time |
| **Echelon Formation** | 8 | Maintain echelon (500 ft lateral/aft, 100 ft altitude offset) | Spacing error ±50 ft lateral, ±20 ft vertical |
| **Formation Maneuvering** | 10 | Coordinated turns, climbs, descents in formation | Formation integrity maintained |
| **Leader Handoff** | 4 | Transfer formation lead between aircraft | <30 sec handoff time, zero formation disruption |

**Key Test Points:**
- **First Formation Flight (PM 67, Flight 5):** FTA-4 and FTA-5 perform autonomous join-up from takeoff, fly 50 nm transit in trail formation, land in sequence.
- **Formation DAA (PM 69, Flight 28):** Intruder aircraft approaches formation; both aircraft execute coordinated avoidance maneuver, reform after intruder clears.
- **Lost-Link in Formation (PM 70, Flight 38):** Datalink to FTA-5 (wingman) lost; FTA-5 automatically breaks formation, executes RTL; FTA-4 continues mission alone.

**Success Criteria:**
- Two-ship formations maintained for >90% of flight time
- Inter-aircraft communication reliability >99.5%
- Zero near-mid-air collisions (closest approach >500 ft)
- Autonomous formation maneuvering demonstrated (turns up to 60° bank)

#### 10.3.2 Phase 7B: Four-Ship Operations (PM 70-75, FTA-4, FTA-5, FTA-6 + LRIP PA-1)

**Duration:** 5 months  
**Flight Hours:** 160 hours (60 flights combined)  
**Test Location:** China Lake NAWS, Yuma Proving Ground

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Four-Ship Join-Up** | 6 | Autonomous formation establishment from 4 separate takeoffs | Formation established within 10 min |
| **Tactical Formations** | 12 | Finger-four, box, diamond formations | Spacing maintained ±5 m (objective) |
| **Coordinated Maneuvers** | 14 | Formation turns, altitude changes, speed changes | All aircraft maintain position |
| **Mission Execution** | 16 | Simulated cargo drop, ISR orbits, firefighting patterns | Mission objectives achieved |
| **Degraded Operations** | 8 | Aircraft failures, lost datalink, formation breakup/reform | Safe degradation, mission continuation or abort |
| **Emergency Procedures** | 4 | Mid-air emergency in formation, egress procedures | Safe aircraft separation, emergency recovery |

**Complex Mission Scenarios:**

**Scenario 1: Cargo Logistics Mission (PM 72, Flight 185)**
- 4-ship autonomous formation takeoff from Edwards AFB
- Cruise 200 nm to Yuma Proving Ground in diamond formation
- Automatic spacing to 2 nm trail separation for sequential landing zone approaches
- Sequential precision landings at 4 separate LZs (5 min intervals)
- Autonomous cargo offload simulation (10 min ground time each)
- Rejoin formation, return transit
- Success: All waypoints achieved, formation integrity maintained >95% of flight, all landings within ±2 m of planned touchdown point

**Scenario 2: Distributed ISR (PM 73, Flight 195)**
- 4-ship establishes orbit pattern around target area (each aircraft 90° around orbit)
- Sensor data from all 4 aircraft fused in real-time
- Target tracking handed off as aircraft rotate around orbit
- One aircraft diverted to investigate secondary target (formation continues with 3 aircraft)
- Diverted aircraft rejoins formation after secondary task complete
- Success: Continuous target custody maintained, sensor handoffs seamless, formation adapts to 3-ship and back to 4-ship

**Scenario 3: Swarm Resilience (PM 74, Flight 205)**
- 4-ship formation experiences scripted failures:
  - FTA-5: Simulated engine failure at PM+30 min → FTA-5 breaks formation, executes OEI landing at emergency site
  - FTA-6: Lost inter-aircraft datalink at PM+45 min → FTA-6 continues mission alone, does not reform
  - FTA-4, PA-1: Continue mission as 2-ship
- Success: No collisions during emergency breakup, remaining aircraft adapt mission plan, all aircraft land safely

**Success Criteria:**
- Four-ship formations routinely established and maintained
- Formation spacing objective: ±5 m (95% of time in steady cruise)
- Mission success rate: >90% (mission objectives achieved)
- Swarm resilience: Safe operations with up to 2 aircraft failures per 4-ship
- Zero mid-air collisions between swarm aircraft

#### 10.3.3 Phase 7C: Swarm Tactics and Edge Cases (PM 75-78)

**Duration:** 3 months  
**Flight Hours:** 100 hours (40 flights)  
**Test Location:** China Lake NAWS

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Large Formation (6+ aircraft)** | 8 | Six-ship formation operations | Formation maintained, no collisions |
| **Dynamic Re-Tasking** | 10 | Mission changes in-flight, formation adaptation | <2 min to adapt to new mission |
| **GPS-Denied Swarm** | 8 | Formation maintenance without GPS (INS + relative navigation) | Formation spacing error <20 m |
| **Adverse Weather** | 6 | Formation flight in moderate turbulence, reduced visibility | Formation integrity maintained |
| **Mixed Autonomy Levels** | 8 | Optionally-piloted + fully autonomous in same formation | Seamless coordination |

**Advanced Swarm Scenarios:**

**Scenario 1: Adaptive Swarm (PM 76, Flight 218)**
- Six-ship formation tasked to transit to target area
- Mid-mission: GCS updates task → 3 aircraft divert to secondary target, 3 continue to primary
- Formation automatically splits into two 3-ship elements
- After task completion, all 6 aircraft rendezvous at recovery base in new 6-ship formation
- Success: Autonomous formation split/rejoin with zero human coordination

**Scenario 2: Contested Environment (PM 77, Flight 228)**
- Four-ship formation encounters scripted threats:
  - Simulated radar threat → Formation executes terrain masking maneuver (descend to 500 ft AGL, tactical routing)
  - Multiple DAA intruders → Each aircraft independently avoids, formation automatically re-establishes after threats clear
- Success: Threat avoidance successful, formation resilience demonstrated

**Success Criteria:**
- Six-ship operations demonstrated (stretch goal: 8-ship)
- GPS-denied formation operations validated (INS + inter-aircraft ranging maintains relative position within 20 m)
- Dynamic mission re-planning demonstrated in multi-aircraft context
- Mixed autonomy operations (human-piloted + autonomous in same formation) feasible

### 10.4 Swarm Communication and Datalink

**Inter-Aircraft Datalink Specifications:**

| Parameter | Specification |
|-----------|---------------|
| **Frequency Band** | C-band (NATO-compatible), LOS datalink |
| **Data Rate** | 10 Mbps (shared across swarm) |
| **Range** | 150 nm line-of-sight |
| **Latency** | <100 ms (99th percentile) |
| **Message Types** | Position/velocity, intent vectors, sensor data, coordination messages |
| **Update Rate** | 10 Hz (position), 1 Hz (mission state) |
| **Encryption** | AES-256, swarm authentication |

**Datalink Architecture:**
- Peer-to-peer mesh network (no master/slave)
- Time-division multiple access (TDMA) to prevent collisions
- Automatic network reconfiguration if aircraft joins/leaves formation
- Graceful degradation: operates with partial connectivity

**Communication Failure Modes:**
- **Lost Inter-Aircraft Link:** Aircraft assumes independent operations, does not attempt to rejoin formation until link re-established
- **GCS Link Lost (entire swarm):** Formation continues mission autonomously per last known tasking or executes collective RTL
- **Partial Swarm Connectivity:** Aircraft maintain formation with neighbors they can communicate with; automatic sub-swarm formation

### 10.5 Phase 7 Deliverables and Success Criteria

| Deliverable | Completion Date | Content |
|-------------|-----------------|---------|
| **Swarm Test Plan** | PM 64 | Multi-aircraft test approach, scenarios, success criteria |
| **Two-Ship Test Report** | PM 70 | Formation flight demonstration, communication validation |
| **Four-Ship Test Report** | PM 75 | Complex mission scenarios, swarm resilience |
| **Swarm Tactics Report** | PM 78 | Advanced scenarios, GPS-denied ops, mixed autonomy |
| **Multi-Aircraft Safety Analysis** | PM 78 | Collision avoidance effectiveness, failure mode analysis |
| **Swarm Operations Manual** | PM 78 | Operational procedures for multi-aircraft missions |

**Phase Exit Criteria:**
- **Two-ship operations:** Routinely demonstrated (>20 sorties)
- **Four-ship operations:** Complex missions executed successfully (>15 sorties)
- **Formation precision:** ±5 m spacing objective demonstrated in 4-ship formation
- **Swarm communication:** >99.5% reliability demonstrated across >100 flight hours
- **Collision avoidance:** Zero near-mid-air collisions between swarm aircraft (<500 ft separation)
- **Graceful degradation:** Safe operations with up to 50% aircraft failures in swarm
- **Mission success rate:** >90% of multi-aircraft missions achieve objectives
- **Inter-aircraft DAA:** Demonstrated effective collision avoidance between swarm members and external intruders

**Phase 7 Exit Gate:** Multi-Aircraft Operations Qualification Review (PM 78)

---

## 11. PHASE 8: PAYLOAD INTEGRATION TESTING

**Duration:** 15 months (PM 60-75, overlaps with Phases 6-7)  
**Objective:** Integrate and validate variant-specific mission payloads  
**Test Location:** Edwards AFB, Yuma Proving Ground (firefighting), China Lake NAWS (ISR)  
**Test Articles:** FTA-2 (MAAP-1F), FTA-3 (MAAP-1I), FTA-1 (MAAP-1C post-DFT modification)

### 11.1 Phase Overview

Payload integration testing validates the modular mission equipment packages that differentiate the three MAAP-1 variants. While ground integration testing (Phase 2) validated interfaces in the lab, flight testing demonstrates real-world mission capability:

- **MAAP-1F (Firefighting):** Water/retardant tank, drop system, fire detection sensors
- **MAAP-1I (ISR):** EO/IR sensor turret, SIGINT suite, real-time video downlink
- **MAAP-1C (Cargo):** Precision external load delivery, dual-hook operations, cargo monitoring

**Integration Philosophy:**
- **Modularity Validation:** Confirm <8 labor-hours to reconfigure between payload packages (PRB MOSA-5 requirement)
- **Interface Verification:** Mechanical, electrical, data, and thermal interfaces per ICDs (Section 5.3 of PRB)
- **Mission Effectiveness:** Demonstrate operational utility of mission systems in realistic scenarios

### 11.2 Test Campaigns by Variant

#### 11.2.1 MAAP-1F (Firefighting) Payload Integration (PM 60-70, FTA-2)

**Duration:** 10 months  
**Flight Hours:** 120 hours (60 flights)  
**Test Location:** Yuma Proving Ground, Southern California wildfire test range

**Payload Configuration:**
- 2,000-gallon internal water/retardant tank (belly-mounted)
- Snorkel fill system (hover-fill from natural water sources)
- GPS-guided drop control system
- Forward-looking infrared (FLIR) with fire hotspot detection
- Pilot crew station (dual controls, firefighting-specific displays)

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Ground Integration** | 0 | Tank installation, systems checkout, weight/balance | All systems functional, CG within limits |
| **Tank Fill Operations** | 8 | Hover-fill from lake/reservoir, fill rate, stability | 2,000 gal fill in <3 min, stable hover during fill |
| **Water Drop Patterns** | 20 | Drop accuracy, pattern coverage, controllability | Drop within ±50 m of target line, coverage per USFS standards |
| **Retardant Ops** | 12 | Fire retardant drops, cleaning procedures, corrosion | Retardant system functional, no aircraft corrosion |
| **Fire Detection** | 8 | FLIR fire detection, hotspot tracking, operator interface | Fire detection range ≥5 km, false alarm rate <5% |
| **Operational Scenarios** | 12 | Simulated wildfire response, multi-drop sorties, crew coordination | Mission profiles executable, crew workload acceptable |

**Key Test Points:**

**Hover-Fill Test (PM 62, Flight 12):**
- FTA-2 hovers over Lake Isabella, CA at 10 ft AGL
- Snorkel deployed, tank filled from empty to 2,000 gallons
- Success Criteria: Fill time <3 min, hover stability maintained (±2 ft position hold), no water ingestion into engines

**Precision Drop Test (PM 64, Flight 28):**
- Target: 1,000 ft × 50 ft ground line marked at Yuma Proving Ground
- FTA-2 approaches at 120 KTAS, 150 ft AGL
- GPS-guided drop system releases 2,000 gal over target line
- Success Criteria: 90% of water/retardant lands within ±50 m of target line (measured via ground observers and dye tracer)

**Operational Mission Simulation (PM 68, Flight 55):**
- Simulated wildfire response scenario
- Takeoff from base, transit 50 nm to fire area
- Perform 6 water drops (hover-fill between drops from nearby reservoir)
- Each drop targets simulated fire line
- Success Criteria: All 6 drops within accuracy specification, mission completion time <3 hours, acceptable pilot workload (Cooper-Harper rating ≤4)

**MAAP-1F-Specific Success Criteria:**
- Water/retardant drop accuracy: ≥90% within ±50 m of target line
- Hover-fill capability: Demonstrated from lakes/reservoirs with <3 min fill time
- Fire detection system: Hotspot detection range ≥5 km, false alarm rate <5%
- Mission endurance: ≥3.5 hours with 6-8 drops (threshold KPP per PRB Section 3.2)
- Optionally-piloted operations: Pilot workload acceptable (Level 1 or 2 handling qualities)
- Tank structural integrity: No leaks, cracks, or deformation after 100 drop cycles

#### 11.2.2 MAAP-1I (ISR) Payload Integration (PM 62-73, FTA-3)

**Duration:** 11 months  
**Flight Hours:** 140 hours (65 flights)  
**Test Location:** China Lake NAWS, Edwards AFB

**Payload Configuration:**
- EO/IR multi-sensor stabilized turret (HD visible, MWIR, LWIR, laser designator/rangefinder)
- SIGINT (signals intelligence) receiver suite with direction-finding
- 4 TB mission data recorder (encrypted)
- Dual HD video downlink (real-time to GCS)
- Advanced mission computer with onboard object detection/tracking

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Sensor Integration** | 6 | Turret installation, sensor alignment, FOV verification | All sensors functional, boresight alignment <0.5 mrad |
| **Sensor Performance** | 12 | Resolution, detection range, tracking accuracy, environmental limits | Meet sensor specifications per vendor datasheet |
| **Data Management** | 8 | Recording capacity, data retrieval, encryption validation | 4 TB capacity, encryption per FIPS 140-2 |
| **Video Downlink** | 10 | Real-time HD video quality, latency, bandwidth, range | Latency <500 ms, continuous link at 150 nm range |
| **Autonomous Sensor Ops** | 15 | Automatic target tracking, cued search, sensor handoff | Track continuity >95%, handoff <5 seconds |
| **ISR Mission Scenarios** | 14 | Simulated reconnaissance, surveillance, target tracking missions | Mission success rate >95% |

**Key Test Points:**

**Sensor Detection Range Test (PM 65, Flight 25):**
- FTA-3 orbits at 10,000 ft AGL over China Lake test range
- Ground targets (vehicles, personnel) positioned at known locations
- EO/IR sensor attempts detection and identification at various ranges
- Success Criteria: Vehicle detection at ≥15 km (day), ≥10 km (night IR); personnel detection at ≥5 km (day), ≥3 km (night)

**Real-Time Video Downlink Test (PM 67, Flight 38):**
- FTA-3 orbits target area, sensors locked on moving ground vehicle
- HD video transmitted to GCS in real-time
- Measure latency (time from sensor capture to GCS display)
- Success Criteria: Latency <500 ms (threshold), <300 ms (objective); zero frame drops; continuous link at 150 nm range

**Autonomous ISR Mission (PM 71, Flight 60):**
- Mission tasking: Autonomous takeoff, transit to surveillance area, establish orbit over target building, track all vehicles entering/exiting for 4 hours, return, autonomous landing
- No human intervention except mission-level tasking
- Automatic target detection, tracking, and data recording
- Success Criteria: Mission completion with zero human intervention, all vehicle movements tracked and recorded, target custody maintained >95% of time

**SIGINT Operations (PM 72, Flight 63):**
- FTA-3 conducts signals intelligence collection over test range
- SIGINT suite detects, identifies, and geolocates emitters (test radios positioned on ground)
- Direction-finding accuracy measured
- Success Criteria: Emitter detection at ≥50 km range, geolocation accuracy ≤500 m (threshold), ≤100 m (objective)

**MAAP-1I-Specific Success Criteria:**
- EO/IR sensor performance: Detection ranges meet or exceed specifications
- Video downlink: HD quality, <500 ms latency, 150 nm range
- Autonomous sensor operations: Target tracking continuity >95%
- SIGINT capability: Emitter detection and geolocation demonstrated
- Mission endurance: ≥4 hours ISR mission with full sensor operations (threshold KPP)
- Data management: All mission data recorded, encrypted, and retrievable
- Mission success rate: >95% of ISR missions achieve tasked objectives

#### 11.2.3 MAAP-1C (Cargo) Advanced Payload Testing (PM 66-75, FTA-1 post-DFT)

**Duration:** 9 months  
**Flight Hours:** 100 hours (50 flights)  
**Test Location:** Yuma Proving Ground, Edwards AFB

**Note:** FTA-1 completed Phase 6 (Developmental Flight Test) and is now reconfigured for advanced cargo operations testing, demonstrating the modularity of the MAAP-1 design.

**Payload Configuration:**
- Dual independent cargo hooks (forward and aft, 16,000 lb rated each per objective)
- Real-time external load monitoring (weight, pendulum angle, stability)
- Precision GPS-guided cargo delivery system
- Cargo cameras (3× belly-mounted EO/IR with operator pan/tilt/zoom)
- Automatic ballast system (maintains CG within limits for asymmetric loads)

| Test Campaign | Flights | Objectives | Success Criteria |
|---------------|---------|-----------|------------------|
| **Dual-Hook Operations** | 12 | Tandem cargo loads, independent release, load stability | Dual loads carried safely, independent release functional |
| **Heavy Load Testing** | 10 | 16,000 lb single-hook external load (objective KPP) | Stable flight, external load delivered successfully |
| **Precision Delivery** | 12 | GPS-guided cargo release, accuracy measurement | Cargo lands within ±10 m of target (threshold), ±5 m (objective) |
| **Long-Line Ops** | 8 | External loads on 150 ft sling (objective) | Stable operations, no load oscillations >±15° |
| **Asymmetric Loading** | 6 | CG management with unequal dual loads | Automatic ballast system maintains CG within limits |
| **Operational Scenarios** | 12 | Simulated logistics missions, multiple load deliveries | Mission success rate >90% |

**Key Test Points:**

**16,000 lb External Load Test (PM 69, Flight 22):**
- FTA-1 hovers, ground crew attaches 16,000 lb test load to forward hook (objective KPP external load)
- Takeoff, climb to 2,000 ft AGL, cruise at 100 KTAS for 30 nm
- Load delivery to designated landing zone
- Success Criteria: Stable flight throughout (no pilot-induced oscillations), external load released within ±5 m of target, no aircraft systems degradation

**Dual-Hook Independent Release (PM 71, Flight 35):**
- FTA-1 carries two 8,000 lb loads (forward and aft hooks)
- Fly to delivery zone, release forward load at Target A, continue to Target B, release aft load
- Success Criteria: Independent release functional (forward hook releases without affecting aft load), both loads delivered within ±10 m of respective targets

**Precision Cargo Delivery (PM 73, Flight 44):**
- FTA-1 approaches target at 120 KTAS, 500 ft AGL
- GPS-guided cargo release system calculates release point based on wind, airspeed, load ballistics
- Automatic cargo release on command
- Success Criteria: Cargo lands within ±5 m of target (objective), operator requires zero manual input

**MAAP-1C-Specific Success Criteria:**
- External load capability: 12,000 lb (threshold KPP) and 16,000 lb (objective KPP) demonstrated in flight
- Dual-hook operations: Independent cargo release functional, both loads delivered accurately
- Precision delivery: Cargo lands within ±10 m (threshold), ±5 m (objective)
- Long-line operations: 150 ft sling length demonstrated (objective)
- Load stability: Pendulum angle <±15° during cruise flight
- Mission radius: ≥125 nm with 12,000 lb external load (threshold KPP verified)

### 11.3 Payload Reconfiguration Testing

**Objective:** Validate MOSA requirement (PRB MOSA-5): Mission kit installation/removal shall not exceed 8 labor-hours.

**Test Procedure (PM 74):**
1. FTA-2 configured as MAAP-1F (firefighting) after flight operations
2. Maintenance crew removes firefighting mission kit: water tank, snorkel system, fire sensors, crew station
3. Install cargo mission kit: dual cargo hooks, load monitoring system, cargo cameras
4. Aircraft now configured as MAAP-1C (cargo)
5. Functional checkout, weight & balance verification, return to flight status

**Success Criteria:**
- Total reconfiguration time: ≤8 labor-hours (per PRB MOSA-5 requirement)
- No special tooling required (standard hand tools only)
- Post-reconfiguration checkout: Zero discrepancies, all systems functional
- Weight & balance: CG remains within limits without additional ballast

**Result (actual test execution):**
- Reconfiguration time: 6.5 labor-hours (19% margin)
- Zero non-conformances during functional checkout
- Validates modularity strategy: single aircraft can support multiple mission profiles with rapid reconfiguration

### 11.4 Phase 8 Deliverables and Success Criteria

| Deliverable | Completion Date | Content |
|-------------|-----------------|---------|
| **MAAP-1F Payload Integration Report** | PM 70 | Firefighting mission systems validation |
| **MAAP-1I Payload Integration Report** | PM 73 | ISR sensor suite and autonomous ops validation |
| **MAAP-1C Advanced Cargo Report** | PM 75 | Heavy external load and precision delivery demonstration |
| **Payload Modularity Test Report** | PM 75 | MOSA-5 requirement verification (8-hour reconfiguration) |
| **Variant-Specific Flight Manuals** | PM 75 | Operating procedures for each variant |
| **Mission System Qualification Data** | PM 75 | Certification data for variant-unique systems |

**Phase Exit Criteria:**
- **MAAP-1F:** All firefighting mission systems functional, water drop accuracy demonstrated, fire detection validated
- **MAAP-1I:** ISR sensors meet performance specs, autonomous sensor operations validated, video downlink qualified
- **MAAP-1C:** External load KPPs (12k lb threshold, 16k lb objective) demonstrated, precision delivery verified
- **Modularity:** <8 labor-hour reconfiguration demonstrated between all variants
- **Mission Success Rate:** >90% for variant-specific mission scenarios
- **Zero Category 1 Defects:** All mission-critical payload systems fully functional

**Phase 8 Exit Gate:** Payload Integration Qualification Review (PM 75)

---

## 12. PHASE 9: OPERATIONAL TEST & EVALUATION

**Duration:** 12 months (PM 72-84)  
**Objective:** Independent operational assessment by representative users  
**Test Location:** Operational test sites (Fort Hunter Liggett, CA; Nellis AFB, NV; MCAS Yuma, AZ)  
**Test Articles:** All FTAs + LRIP aircraft (PA-1 through PA-6)

### 12.1 Phase Overview

Operational Test & Evaluation (OT&E) is an independent assessment conducted by operational users (not the contractor) to determine whether the MAAP-1 is operationally effective, suitable, and survivable for its intended missions. OT&E is a prerequisite for:

- Initial Operational Capability (IOC) declaration
- Full-Rate Production (FRP) decision
- Final acceptance by operational commands

**OT&E vs. Developmental Test:**
- **DT (Phases 6-8):** Contractor-led, verifies requirements, engineering focus
- **OT&E (Phase 9):** Government-led, validates operational utility, warfighter/end-user focus

**Key Evaluation Criteria:**
- **Operational Effectiveness:** Does the system achieve mission objectives?
- **Operational Suitability:** Can it be maintained and sustained in operational environments?
- **Operational Availability:** Is it available when needed? (target: 85% Ao per PRB KSA)
- **Mission Success Rate:** What percentage of missions are completed successfully? (target: >95% per PRB Section 3.5)
- **Survivability:** Can it operate in contested/hazardous environments?

### 12.2 OT&E Organization

**Operational Test Agency (OTA):**
- Independent government organization (not part of MAAP-1 program office)
- Reports directly to OSD (Office of the Secretary of Defense) or Service Operational Test Command
- Authority to issue independent assessment of operational capability

**Test Participants:**
- **Operational Users:** Military aircrew, firefighting pilots, cargo operators (representative of end users)
- **Maintenance Personnel:** Government or contractor logistics support personnel
- **Subject Matter Experts:** Experienced rotorcraft pilots, mission planners, logistics professionals

**Contractor Role:**
- Provide aircraft, spares, technical support (not test execution or data analysis)
- No involvement in test planning or evaluation (maintains independence)

### 12.3 Test Campaigns

#### 12.3.1 OT&E Phase 1: Initial Operational Assessment (PM 72-76)

**Duration:** 4 months  
**Flight Hours:** 200 hours (100 sorties across 6 aircraft)  
**Test Location:** Fort Hunter Liggett (cargo/firefighting), Nellis AFB (ISR)

| Test Campaign | Sorties | Objectives | Success Criteria |
|---------------|---------|------------|------------------|
| **Cargo Operations** | 30 | Logistics resupply missions, heavy external loads | Mission success rate >90% |
| **Firefighting Operations** | 25 | Simulated wildfire response, multi-drop sorties | Effective fire suppression, pilot workload acceptable |
| **ISR Operations** | 25 | Reconnaissance, surveillance, target tracking | Intelligence collection objectives met |
| **Maintenance Evaluation** | N/A | Scheduled/unscheduled maintenance, MTBF assessment | MMH/FH ≤4.5 (threshold KSA per PRB) |
| **Logistics Supportability** | N/A | Spare parts availability, supply chain effectiveness | Supply availability >90% (threshold per PRB KSA) |
| **Crew Training** | 20 | Pilot/operator training effectiveness, proficiency | Acceptable training time to proficiency |

**Operational Mission Scenarios:**

**Scenario 1: Forward Operating Base Resupply (Cargo)**
- Mission: Deliver 8,000 lb cargo load to remote FOB 150 nm from main base
- Flight Profile: Autonomous takeoff, cruise navigation, precision landing at unimproved LZ, cargo offload, return
- Evaluation Criteria: Mission completion time, navigation accuracy, landing precision, operator workload
- Representative Conditions: Conducted during day/night, various weather conditions

**Scenario 2: Wildfire Initial Attack (Firefighting)**
- Mission: Respond to simulated wildfire, perform 6 water drops on fire line, coordinate with ground crews
- Flight Profile: Rapid alert launch, transit to fire area, hover-fill from reservoir, precision drops, RTB
- Evaluation Criteria: Response time, drop accuracy, fire suppression effectiveness, pilot workload, safety
- Representative Conditions: High-temperature (ISA+20°C), moderate winds, mountainous terrain

**Scenario 3: Intelligence Collection (ISR)**
- Mission: Conduct 4-hour surveillance orbit over target area, detect/track/identify ground vehicles and personnel
- Flight Profile: Autonomous transit to surveillance area, establish orbit, sensor operations, real-time data transmission to GCS
- Evaluation Criteria: Detection performance, target tracking continuity, intelligence product quality, operator workload
- Representative Conditions: Day/night operations, varying weather, GPS-denied segments

**Initial Operational Assessment Outcomes:**
- Mission success rate: 94% (exceeds 90% threshold, approaches 95% objective)
- Maintenance: MMH/FH = 4.2 (meets threshold ≤4.5, trending toward objective ≤3.5)
- Supply availability: 92% (exceeds threshold >90%)
- Crew training: Pilots reach proficiency in 25 flight hours (acceptable per training system requirements)
- Operational effectiveness: Rated "effective" for all three mission variants
- Operational suitability: Rated "suitable with minor deficiencies" (open issues logged for resolution before IOC)

#### 12.3.2 OT&E Phase 2: Operational Effectiveness Evaluation (PM 76-80)

**Duration:** 4 months  
**Flight Hours:** 250 hours (120 sorties)  
**Test Location:** MCAS Yuma (multi-variant), China Lake NAWS (swarm operations)

| Test Campaign | Sorties | Objectives | Success Criteria |
|---------------|---------|------------|------------------|
| **Multi-Aircraft Operations** | 30 | Formation flight, swarm coordination, mission effectiveness | Swarm operations effective, collision avoidance 100% |
| **Adverse Conditions** | 25 | High winds, reduced visibility, night/IMC operations | Degraded operations acceptable |
| **Sustained Operations** | 40 | Multi-day surge operations, maintenance burden | Sortie