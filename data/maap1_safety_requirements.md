# SAFETY REQUIREMENTS DOCUMENT
## Eurus Systems MAAP-1 "AetherForge" Heavy-Lift Tandem-Rotor Autonomous Helicopter Program

| | |
|---|---|
| **Document No.** | AF-MAAP1-SRD-0003 |
| **Revision** | A (Initial Release) |
| **Classification** | Eurus Systems Proprietary — Export Controlled (ITAR/EAR Applicable) |
| **Derived From** | Program Requirements Baseline AF-MAAP1-PRB-0001, Rev A<br>Key Specifications Document AF-MAAP1-KSD-0002, Rev A |
| **Owner** | MAAP-1 Chief Safety Engineer / System Safety Manager |
| **Date** | January 2025 |
| **Applicability** | All MAAP-1 Variants (MAAP-1F, MAAP-1I, MAAP-1C), All Development and Production Phases |

---

## DOCUMENT CONTROL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| System Safety Manager | [Name] | _____________ | ______ |
| Chief Engineer | [Name] | _____________ | ______ |
| Airworthiness Authority | [Name] | _____________ | ______ |
| Program Manager | [Name] | _____________ | ______ |

---

## EXECUTIVE SUMMARY

This Safety Requirements Document (SRD) establishes the comprehensive safety framework for the Eurus Systems MAAP-1 autonomous heavy-lift helicopter program. The document defines the safety philosophy, requirements, and processes necessary to achieve a safe, certifiable aircraft across all three mission variants (Firefighting, ISR, and Cargo) and throughout all phases of the program lifecycle.

**Key Safety Drivers:**
- **Autonomous/Optionally-Piloted Operations:** Elimination or reduction of onboard crew creates unique safety challenges requiring equivalent or superior safety levels compared to manned operations
- **Heavy-Lift Mission Profile:** High-energy operations with external loads demand robust crashworthiness and fail-safe design
- **Dual Certification Path:** Civil (FAA Part 29) and military airworthiness requirements must be satisfied
- **No Single-Point Failures:** Program constraint C-3 mandates no single failure shall result in loss of aircraft in autonomous configuration

**Safety Objectives:**
1. Achieve catastrophic failure probability of ≤1×10⁻⁹ per flight hour for flight-critical systems
2. Demonstrate autonomous system safety equivalent to manned VFR operations
3. Obtain FAA Type Certificate for baseline configuration with acceptable Special Conditions for autonomy
4. Establish comprehensive safety case supporting both civil and military airworthiness certification

---

## TABLE OF CONTENTS

1. [Introduction and Scope](#1-introduction-and-scope)
2. [Safety Philosophy and Principles](#2-safety-philosophy-and-principles)
3. [Safety Requirements Overview](#3-safety-requirements-overview)
4. [System Safety Requirements](#4-system-safety-requirements)
5. [Autonomy Safety Requirements](#5-autonomy-safety-requirements)
6. [Structural Integrity and Crashworthiness](#6-structural-integrity-and-crashworthiness)
7. [Fire Protection and Hazardous Materials](#7-fire-protection-and-hazardous-materials)
8. [Design Assurance Level (DAL) Allocation](#8-design-assurance-level-dal-allocation)
9. [Hazard Identification and Risk Management](#9-hazard-identification-and-risk-management)
10. [Ground Safety](#10-ground-safety)
11. [Flight Safety and Operational Constraints](#11-flight-safety-and-operational-constraints)
12. [Certification and Airworthiness Basis](#12-certification-and-airworthiness-basis)
13. [Safety Testing and Verification](#13-safety-testing-and-verification)
14. [Safety Milestones and Schedule Integration](#14-safety-milestones-and-schedule-integration)
15. [Appendices](#15-appendices)

---

## 1. INTRODUCTION AND SCOPE

### 1.1 Purpose

This Safety Requirements Document establishes mandatory safety requirements for the MAAP-1 program from preliminary design through operational deployment and sustainment. It serves as the single authoritative source for:

- Top-level safety objectives and philosophy
- Derived safety requirements allocated to systems, subsystems, and components
- Design Assurance Level (DAL) allocation for flight-critical software and hardware
- Hazard identification, analysis, and mitigation approach
- Safety verification methods and acceptance criteria
- Certification safety case structure

All subordinate safety documentation (System Safety Assessment, Fault Tree Analyses, FMEA/FMECA, Safety of Flight Plans) shall trace to requirements defined herein.

### 1.2 Scope and Applicability

**Program Phases Covered:**
- Engineering and Manufacturing Development (EMD)
- Low-Rate Initial Production (LRIP) and Full-Rate Production (FRP)
- Initial Operational Capability (IOC) through Full Operational Capability (FOC)
- Operations and Sustainment throughout 20,000 flight hour / 30-year design service life

**Variants Covered:**
- MAAP-1F "Wildfire" (Firefighting, optionally-piloted)
- MAAP-1I "Sentinel" (ISR, autonomous)
- MAAP-1C "Atlas" (Cargo/Logistics, autonomous)

**Configuration Applicability:**
- Green Aircraft (common baseline, Section 5.1 of PRB)
- Variant-unique mission systems (Section 5.2 of PRB)
- All interface boundaries defined in ICDs

### 1.3 Document Structure

This document follows a hierarchical safety requirements structure:

```
Level 1: Top-Level Safety Objectives (Section 2)
    └─ Level 2: System-Level Safety Requirements (Sections 4-7)
        └─ Level 3: Subsystem Safety Requirements (Allocated to SRDs)
            └─ Level 4: Component Design Requirements (Allocated to specifications)
```

Requirements are uniquely identified using the nomenclature **SRD-XXX-YYY** where:
- **XXX** = Requirement category (e.g., AUT = Autonomy, STR = Structures, FCS = Flight Controls)
- **YYY** = Sequential requirement number

### 1.4 Relationship to Other Documents

| Document | Relationship |
|----------|--------------|
| **PRB (AF-MAAP1-PRB-0001)** | Parent requirements document; this SRD derives all safety requirements from PRB constraints and KPPs |
| **Key Specifications (AF-MAAP1-KSD-0002)** | Performance envelope defines operational safety boundaries |
| **System Safety Assessment (SSA)** | Implements requirements via ARP4761 process; demonstrates compliance |
| **FMEA/FMECA** | Component-level failure analysis feeding SSA |
| **Fault Tree Analysis (FTA)** | Top-down analysis verifying catastrophic failure probability targets |
| **Test and Evaluation Master Plan (TEMP)** | Verification methods for safety requirements |
| **Manufacturing Quality Plan** | Production safety controls |
| **Certification Plan** | Airworthiness safety case integration |

### 1.5 Precedence

In the event of conflict between this document and subordinate safety documentation, this SRD takes precedence unless a formal deviation has been approved by the Program Safety Review Board (PSRB) and documented in the Hazard Tracking System (HTS).

---

## 2. SAFETY PHILOSOPHY AND PRINCIPLES

### 2.1 Program Safety Philosophy

The MAAP-1 safety philosophy is built on five core principles:

#### **Principle 1: Equivalent Safety Standard**
Autonomous and optionally-piloted configurations shall provide an equivalent level of safety to comparable manned heavy-lift helicopters operating under Visual Flight Rules (VFR), as measured by:
- Catastrophic failure probability
- Fatal accident rate (projected)
- Serious injury rate (projected)
- Ground casualty risk

**Rationale:** Elimination of onboard crew does not reduce safety expectations for third parties (ground personnel, other airspace users, public). Regulatory acceptance of autonomous operations requires demonstrable safety equivalence.

#### **Principle 2: Defense in Depth**
Safety shall be achieved through multiple, independent layers of protection:
1. **Inherently safe design** (elimination of hazards where possible)
2. **Safety features** (design mitigations: redundancy, fault tolerance)
3. **Safety devices** (active protection systems: warnings, automatic recovery)
4. **Procedural safeguards** (operational limitations, checklists, training)
5. **Personal protective equipment** (for ground operations)

**Rationale:** No single safety measure is infallible; layered protections provide robustness against unknown failure modes and human factors.

#### **Principle 3: Fail-Safe / Fail-Operational Design**
All flight-critical systems shall be designed such that:
- No single failure results in catastrophic outcome (loss of aircraft or fatality)
- Primary flight-critical functions degrade gracefully through multiple fault states
- Autonomous systems revert to safe mode (controlled landing or return-to-base) upon loss of mission-critical functions

**Rationale:** Autonomous operations eliminate pilot as final safety layer; aircraft systems must provide equivalent safety function.

#### **Principle 4: Hazard-Driven Design**
Safety shall be integrated into design from conceptual phase through:
- Early hazard identification (Preliminary Hazard List at PDR)
- Iterative Functional Hazard Assessment throughout design evolution
- Risk-informed trade studies for safety-critical design decisions
- Continuous safety assessment at design reviews

**Rationale:** Retrofitting safety into mature design is costly and often inadequate; early integration enables inherently safer architecture.

#### **Principle 5: Safety Data-Driven Decision Making**
All safety-critical design decisions, requirement changes, and deviation approvals shall be:
- Supported by quantitative risk analysis where feasible
- Documented with traceability to hazard analysis
- Reviewed by independent safety authority (System Safety Working Group)
- Approved by appropriate authority level based on risk severity

**Rationale:** Subjective safety judgments lead to inconsistent risk acceptance; data-driven process ensures rigorous, auditable safety case.

### 2.2 Safety Objectives

#### 2.2.1 Top-Level Safety Objectives

| Objective ID | Objective Statement | Success Criteria |
|--------------|---------------------|------------------|
| **SO-1** | Achieve FAA Type Certificate for MAAP-1C baseline configuration | TC issued by PM 84 without significant Special Conditions that limit operational utility |
| **SO-2** | Demonstrate autonomous flight safety equivalent to manned VFR operations | DAA system compliance with ASTM F3442; lost-link procedures validated; <1×10⁻⁷/flt hr loss of autonomous control |
| **SO-3** | Achieve zero Class A (catastrophic) mishaps throughout EMD and LRIP phases | No loss of test aircraft or fatalities during 2,000+ flight test hours |
| **SO-4** | Validate crashworthiness to MIL-STD-1290 standards | Full-scale crash test demonstrates occupant survivability at 30 ft/s vertical, 40 ft/s horizontal |
| **SO-5** | Establish safety case acceptable to both civil (FAA) and military (USAF/USN) authorities | Airworthiness approvals obtained for all planned operational environments and mission profiles |

#### 2.2.2 Quantitative Safety Targets

**Aircraft-Level Safety Targets (per ARP4761 / FAA AC 29-2C):**

| Failure Condition Classification | Qualitative Effect | Quantitative Probability Target (per flight hour) |
|----------------------------------|--------------------|-------------------------------------------------|
| **Catastrophic** | Loss of aircraft and/or multiple fatalities | ≤ 1×10⁻⁹ |
| **Hazardous/Severe-Major** | Large reduction in safety margins; serious injury or fatality possible | ≤ 1×10⁻⁷ |
| **Major** | Significant reduction in safety margins; crew/passenger discomfort; some injuries | ≤ 1×10⁻⁵ |
| **Minor** | Slight reduction in safety margins; inconvenience; no injuries | ≤ 1×10⁻³ |
| **No Safety Effect** | No impact on safety | No probability requirement |

**System-Level Allocation:**
Quantitative targets shall be allocated to systems using Fault Tree Analysis (FTA) such that aircraft-level targets are met with margin. Preliminary allocation (to be refined during System Safety Assessment):

| System | Allocated Catastrophic Failure Probability |
|--------|-------------------------------------------|
| Flight Control System (including autonomous GNC) | ≤ 3×10⁻¹⁰ /flt hr |
| Propulsion System (engines + transmission + fuel) | ≤ 4×10⁻¹⁰ /flt hr |
| Rotor System | ≤ 2×10⁻¹⁰ /flt hr |
| Structural Integrity | ≤ 1×10⁻¹⁰ /flt hr |
| Fire Protection | Contribution ≤ 5×10⁻¹¹ /flt hr |

**Autonomy-Specific Targets (per PRB Section 3.5):**
- Loss of autonomous control function: ≤ 1×10⁻⁷ per flight hour (Threshold), ≤ 1×10⁻⁸ (Objective)
- Detect-and-Avoid (DAA) missed detection of collision threat: ≤ 1×10⁻⁶ per flight hour
- Lost-link safe recovery (RTL or autoland): ≥ 99.9% success rate

### 2.3 Safety Precedence in Design Trades

When trade-offs are required between competing program objectives, safety shall take precedence in accordance with PRB Section 2.3:

**Program Priorities (order of precedence):**
1. **Flight Safety and Airworthiness** (including autonomy safety case)
2. Mission Performance (KPPs)
3. Program Schedule (LRIP/FRP gates)
4. Life Cycle Cost / Affordability
5. Growth Margin and Modularity

**Application:**
- Safety-driven design changes shall not be deferred for cost or schedule reasons without Program Manager approval and PSRB review
- Safety-critical items are exempt from value engineering cost reduction unless equivalent safety is demonstrated
- Schedule pressures shall not drive reduction in safety verification testing (ref. Section 13)

### 2.4 Safety Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **Program Manager** | Accountable for overall program safety; approves Safety Management Plan; chairs PSRB; approves residual risk acceptance |
| **Chief Engineer** | Responsible for technical safety integrity; ensures design compliance with safety requirements; approves Engineering Change Proposals affecting safety |
| **System Safety Manager** | Manages System Safety Program per MIL-STD-882E; leads hazard analyses; maintains Hazard Tracking System; conducts Safety Assessments |
| **Airworthiness Authority (Government)** | Independent safety oversight; approves Flight Release for test; recommends Type Certificate issuance |
| **IPT Leads** | Implement safety requirements within their subsystems; support hazard analyses; report safety issues |
| **Flight Test Organization** | Conducts safe flight test operations; develops Safety-of-Flight plans; reports flight test safety data |
| **Quality Assurance** | Verifies production conformance to safety-critical design; maintains production Safety defect tracking |
| **Manufacturing** | Implements production safety controls; identifies and escalates manufacturing hazards |

**Program Safety Review Board (PSRB):**
- **Chair:** Program Manager
- **Members:** Chief Engineer, System Safety Manager, Airworthiness Authority, IPT Leads, Customer Representative (observer)
- **Frequency:** Monthly (routine), ad-hoc (for high-severity hazards or mishaps)
- **Authority:** Approve residual risk acceptance for Catastrophic and Hazardous hazards; approve safety waivers; direct corrective actions

---

## 3. SAFETY REQUIREMENTS OVERVIEW

### 3.1 Requirements Hierarchy

Safety requirements are organized into the following categories:

**Category 1: System Safety Requirements (Section 4)**
- Airworthiness and certification compliance
- System-level fault tolerance and redundancy
- Failure probability targets
- Safety-critical system identification

**Category 2: Autonomy Safety Requirements (Section 5)**
- Autonomous flight control safety
- Detect-and-Avoid (DAA) requirements
- Lost-link behavior and contingency management
- Human-machine interface safety
- Ground Control Station (GCS) safety

**Category 3: Structural Integrity and Crashworthiness (Section 6)**
- Structural design and certification
- Limit and ultimate load requirements
- Crashworthiness and occupant protection
- Lightning and high-intensity radiated fields (HIRF)

**Category 4: Fire Protection and Hazardous Materials (Section 7)**
- Fire detection and suppression
- Fuel system crashworthiness
- Hazardous material management
- Explosive safety (ordnance, if applicable)

**Category 5: Design Assurance Level (DAL) Allocation (Section 8)**
- Software criticality (DO-178C)
- Hardware criticality (DO-254)
- Development assurance process requirements

**Category 6: Ground Safety (Section 10)**
- Ground handling and servicing safety
- Maintenance safety
- Transport and storage safety

**Category 7: Flight Safety and Operational Constraints (Section 11)**
- Flight envelope protection
- External load safety
- Environmental operating limits
- Emergency procedures and escape systems

### 3.2 Requirements Traceability

All safety requirements shall be traced through the Requirements Verification Traceability Matrix (RVTM-0001) to:
- **Parent Requirement:** PRB constraint, KPP, or regulatory requirement
- **Verification Method:** Analysis, Test, Demonstration, or Inspection
- **Verification Status:** Not Started / In Progress / Complete / Verified
- **Responsible Organization:** Subsystem IPT or test organization

**Requirements Management:**
- All safety requirements entered into Program Requirements Management Tool (PRMT)
- Changes to safety requirements processed through Configuration Control Board (CCB)
- Safety requirement changes flagged for PSRB review
- Verification closure required before milestone gate passage

### 3.3 Compliance Verification Strategy

| Requirement Type | Primary Verification Method | Supporting Methods |
|------------------|----------------------------|-------------------|
| Quantitative failure probabilities | Analysis (Fault Tree Analysis, reliability prediction) | Test (component qualification, HALT/HASS) |
| Fault tolerance / redundancy | Inspection (design review), Demonstration (fault injection testing) | Analysis (FMEA) |
| Crashworthiness | Test (full-scale dynamic crash test) | Analysis (FEA simulation) |
| Fire protection | Test (flame penetration, material flammability) | Analysis (fire zone mapping) |
| Autonomous safety functions | Test (flight test with failure injection), Demonstration (simulation) | Analysis (software verification, formal methods) |
| Structural integrity | Test (static airframe test to ultimate load), Analysis (stress analysis) | Inspection (production inspection) |

---

## 4. SYSTEM SAFETY REQUIREMENTS

### 4.1 General Airworthiness Requirements

**SRD-AIR-001: Certification Compliance**  
The MAAP-1 aircraft shall comply with the applicable airworthiness regulations for its intended certification basis:
- **Civil Variants (MAAP-1C baseline, MAAP-1F optionally-piloted):** 14 CFR Part 29 (Transport Category Rotorcraft) as amended through [Amendment 29-XX, TBD at certification basis agreement]
- **Military Variants (MAAP-1I, MAAP-1F military operations):** MIL-HDBK-516C and applicable service-specific airworthiness criteria
- **Special Conditions:** FAA Special Conditions for autonomous flight systems (to be defined in coordination with FAA AIR-100)

**Verification:** Inspection (certification plan review), Analysis (compliance checklist), Test (certification flight testing per Type Certification Board approved plan)

---

**SRD-AIR-002: Design Service Life**  
The aircraft shall be designed for a service life of 20,000 flight hours or 30 years, whichever occurs first, with damage tolerance and safe-life principles applied as follows:
- **Damage-tolerant structure:** Primary structure (fuselage, rotor pylon, landing gear) shall meet fail-safe criteria with detectable crack growth between inspections
- **Safe-life components:** Rotor system dynamic components (blades, hubs, pitch links), transmission, drive shafts designed for retirement life with appropriate safety factors
- **Corrosion protection:** Designed for Class 2 corrosion environment (coastal/maritime) per MIL-STD-810H

**Verification:** Analysis (fatigue and damage tolerance analysis per AC 29-2C MG-18), Test (full-scale fatigue testing to 2× design life), Inspection (in-service inspection program)

---

**SRD-AIR-003: Flight Envelope Protection**  
The aircraft shall incorporate flight envelope protection systems that prevent:
- Exceeding VNE (Never-Exceed Speed): 165 KTAS
- Exceeding load factor limits: +3.5g / -1.0g (symmetric), ±2.0g (lateral)
- Rotor overspeed: >288 RPM (107% nominal)
- Rotor underspeed in flight: <240 RPM (90% nominal)
- Exceeding maximum operating altitude: 14,000 ft PA

**Verification:** Test (flight test with envelope expansion), Analysis (flight control system design review), Demonstration (piloted simulation with envelope violations attempted)

---

**SRD-AIR-004: Emergency Autorotation Capability**  
The aircraft shall demonstrate safe landing capability following complete loss of engine power via autorotation from:
- **Minimum altitude:** 500 ft AGL at MGTOW, 300 ft AGL at reduced weight
- **Maximum speed:** 135 KIAS entry speed
- **Landing distance:** ≤1,500 ft from 500 ft AGL (Threshold), ≤1,200 ft (Objective)
- **Touchdown speed:** ≤10 ft/s vertical at zero groundspeed

**Verification:** Test (flight test demonstration per FAA-approved test plan), Analysis (autorotation performance modeling validated against flight test)

---

### 4.2 Fault Tolerance and Redundancy Requirements

**SRD-FT-001: No Single-Point Failures (Flight-Critical Systems)**  
In accordance with PRB Constraint C-3, no single failure in autonomous (no-pilot) configuration shall result in loss of aircraft. Flight-critical systems shall meet the following redundancy requirements:

| System | Minimum Redundancy | Fail-Operational Requirement |
|--------|--------------------|-----------------------------|
| Flight Control Computers | Triplex (dissimilar redundancy preferred) | Fail-operational after any single failure |
| Control Actuation (per control axis) | Dual actuators or dual hydraulic channels | Safe flight and landing after single failure |
| Navigation (GPS/INS) | Triple-redundant GPS, Dual INS | Operate to safe landing with one GPS + one INS |
| Air Data System | Dual independent systems | Continued flight with degraded performance |
| Electrical Power Generation | Dual independent generators | Essential loads powered after single generator failure |
| Hydraulic Power | Dual independent hydraulic systems | Flight control authority maintained on single system |
| Engines and Transmissions | Twin engines with OEI capability | Safe landing from any hover altitude after single engine failure |

**Verification:** Analysis (FMEA, Fault Tree Analysis), Demonstration (fault injection testing), Test (flight test with simulated failures)

---

**SRD-FT-002: Dissimilar Redundancy for Flight Control**  
To mitigate common-mode software failures, the flight control system shall employ dissimilar redundancy:
- Primary flight control channels 1 and 2: Independently developed software implementations using diverse algorithms
- Channel 3: Dissimilar hardware platform and/or simplified control law implementation
- Cross-channel monitoring with voting logic to detect and isolate failed channel

**Verification:** Inspection (software architecture review against DO-178C objectives for DAL A), Analysis (common-mode failure analysis), Test (fault injection and dissimilar software validation testing)

---

**SRD-FT-003: Graceful Degradation**  
Following failure of a redundant element, the system shall:
- Automatically reconfigure to maintain safe flight (no crew action required in autonomous mode)
- Annunciate degraded status to Ground Control Station (GCS) within 5 seconds
- Restrict flight envelope as necessary to maintain safety margins (e.g., reduced VNE, altitude restriction)
- Provide sufficient capability to complete mission or execute safe return-to-base (RTB) / autoland

**Verification:** Demonstration (piloted simulation with progressive failures), Test (flight test with system degradation)

---

**SRD-FT-004: Independent Failure Detection**  
Each redundant system element shall have independent failure detection (self-monitoring) with the following performance:
- **Detection latency:** <100 ms for flight-critical failures (control computers, actuators)
- **Coverage:** ≥99% of failure modes affecting safety detected
- **False alarm rate:** <1 per 10,000 flight hours per channel

Built-In Test (BIT) and Health and Usage Monitoring System (HUMS) shall provide continuous monitoring with automatic fault isolation to Line Replaceable Unit (LRU) level.

**Verification:** Analysis (FMEA coverage analysis), Test (fault injection testing with BIT validation)

---

### 4.3 Propulsion System Safety Requirements

**SRD-PROP-001: One-Engine-Inoperative (OEI) Performance**  
The aircraft shall meet the following OEI performance requirements to ensure safe landing after single engine failure:

| Condition | Requirement |
|-----------|-------------|
| **OEI Hover Ceiling (MGTOW, ISA)** | ≥4,000 ft PA OGE (Threshold), ≥6,000 ft PA (Objective) |
| **OEI Rate of Climb (sea level, MGTOW)** | ≥500 fpm continuous OEI power |
| **OEI Continued Flight** | Safe flight to suitable landing area from any point in normal operating envelope |
| **OEI Power Duration** | 2.5 min emergency power, 30 min intermediate, unlimited continuous |

**Verification:** Test (flight test demonstration of OEI performance throughout envelope), Analysis (validated propulsion performance model)

---

**SRD-PROP-002: Engine Fire Detection and Suppression**  
Each engine compartment shall be equipped with:
- **Fire detection:** Dual-loop fire detection system with <5 second detection time from ignition
- **Fire suppression:** Automated fire extinguishing system (Halon 1301 or approved equivalent) activated within 2 seconds of confirmed fire detection
- **Post-fire isolation:** Automatic engine shutdown, fuel shutoff, and firewall integrity maintained for ≥15 minutes

**Verification:** Test (fire detection system certification testing per TSO-C1a/TSO-C85a), Analysis (fire zone analysis per AC 29-2C MG-12), Demonstration (ground fire testing with suppression system activation)

---

**SRD-PROP-003: Fuel System Safety**  
The fuel system shall be designed to minimize fire hazards and ensure continued operation after damage:
- **Crashworthy fuel cells:** Comply with MIL-STD-1290 (30 ft/s vertical, 40 ft/s horizontal impact survivability)
- **Fuel venting:** Flame arrestors in vent system; no fuel spillage during 60° pitch/roll maneuvers
- **Cross-feed capability:** Any engine can feed from all fuel tanks; automatic cross-feed activation on low-pressure detection
- **Fuel shutoff:** Positive fuel shutoff to each engine within 3 seconds of command (manual or automatic)

**Verification:** Test (fuel cell drop testing per MIL-STD-1290, fuel system functional testing), Analysis (fuel system schematic review against AC 29-2C MG-11)

---

**SRD-PROP-004: Transmission Run-Dry Capability**  
The main transmission and aft transmission shall sustain operation for ≥30 minutes following complete loss of lubrication oil to enable:
- Detection of oil loss via chip detectors and oil pressure sensors
- Crew notification and emergency procedure execution
- Safe landing at nearest suitable site

**Verification:** Test (transmission run-dry endurance test per component qualification plan), Analysis (thermal analysis of transmission under no-oil condition)

---

### 4.4 Electrical System Safety Requirements

**SRD-ELEC-001: Essential Electrical Power**  
The electrical system shall provide redundant power to essential loads (flight controls, navigation, communication) with the following architecture:
- **Dual independent generators:** Each capable of supplying 100% of essential loads
- **Battery backup:** 30-minute battery capacity for essential loads (allows safe landing after dual generator failure)
- **Automatic load shedding:** Non-essential loads automatically shed on single generator failure to preserve capacity for flight-critical systems

**Verification:** Analysis (electrical load analysis), Test (generator failure testing with load shedding validation), Demonstration (flight test with single/dual generator failure simulation)

---

**SRD-ELEC-002: Electrical Fire Prevention**  
Electrical system design shall minimize fire risk through:
- **Circuit protection:** Circuit breakers or fuses for all circuits; no single circuit failure propagates to multiple systems
- **Wire separation:** Flight-critical system wiring physically separated (≥3 inches) and in separate conduit/raceways from non-critical wiring
- **Arc fault detection:** Arc Fault Circuit Breakers (AFCB) or equivalent detection on high-power circuits (>20A)
- **Bonding and grounding:** Electrical bonding per MIL-STD-464D to prevent electrostatic discharge and lightning effects

**Verification:** Inspection (wiring installation inspection against IPC/WHMA-A-620), Test (electrical system certification testing including arc fault and lightning strike per DO-160G), Analysis (electrical bonding network analysis)

---

**SRD-ELEC-003: Lightning Protection**  
The aircraft shall be protected against direct lightning strikes per MIL-STD-464D and AC 29-2C MG-13:
- **Composite structure:** Embedded metallic mesh or conductive layers providing continuous current path
- **Fuel system:** Lightning diverter strips preventing spark ignition in fuel tanks/lines
- **Avionics protection:** Transient voltage suppression and shielding per DO-160G Section 22
- **Rotor blades:** Lightning diverter strips on blade leading edges

**Verification:** Test (direct lightning strike testing per SAE ARP5416 on representative structure), Analysis (lightning current path analysis and HIRF analysis per DO-160G), Inspection (production conformance inspection of lightning protection features)

---

### 4.5 Flight Control System Safety Requirements

**SRD-FCS-001: Flight Control Redundancy**  
The fly-by-wire flight control system shall be triplex-redundant with the following architecture:
- **Three independent flight control computers:** Physically separated, independent power supplies, dissimilar software (channels 1/2 vs. 3)
- **Dual actuators per control axis:** Each actuator capable of 100% control authority; failure of one actuator degrades but does not eliminate control
- **Dual independent hydraulic systems:** Each system capable of powering all flight control actuators

**Verification:** Analysis (FMEA demonstrating no single-point failures), Test (actuator failure testing, hydraulic system failure testing), Demonstration (piloted simulation with all single-failure combinations)

---

**SRD-FCS-002: Flight Control Failure Detection and Recovery**  
The flight control system shall detect and recover from failures:
- **Monitoring:** Cross-channel monitoring with disagreement detection (<50 ms latency)
- **Fault isolation:** Failed channel automatically isolated and removed from voting
- **Reconfiguration:** Automatic reconfiguration to dual-channel operation with continued safe flight
- **Reversion modes:** Automatic reversion to degraded control laws if necessary to maintain stability

**Verification:** Test (fault injection testing with all credible single and dual failures), Analysis (control law stability analysis in all reversion modes)

---

**SRD-FCS-003: Control Law Safety Features**  
Flight control laws shall incorporate the following safety features:
- **Envelope protection:** Automatic limiting to prevent exceeding structural limits, VNE, rotor speed limits
- **Stability augmentation:** Artificial stability to prevent pilot-induced oscillation (PIO) or loss of control
- **Trim freeze:** Automatic trim hold on pilot/GCS control disconnect
- **Rate limiting:** Control rate limits prevent abrupt uncommanded inputs from failures

**Verification:** Test (flight test validation of envelope protection and control law behavior), Analysis (control law design review against safety requirements), Demonstration (piloted simulation with envelope exceedance attempts)

---

**SRD-FCS-004: Control System Integrity Monitoring**  
Continuous monitoring of flight control system integrity shall include:
- **Position feedback:** Dual independent position sensors on all actuators; disagreement detection <0.5 degree
- **Force feedback:** Load cells or pressure transducers monitor control loads; over-limit detection
- **Control surface position:** Independent position measurement (LVDT or RVDT) separate from actuator feedback
- **Hydraulic system health:** Pressure, temperature, and fluid level monitoring with caution/warning thresholds

**Verification:** Analysis (sensor coverage analysis), Test (sensor failure testing, disagreement detection validation)

---

### 4.6 Rotor System Safety Requirements

**SRD-ROTOR-001: Blade Retention**  
Rotor blades shall remain attached to the hub under all operational conditions including:
- Limit load conditions (+3.5g / -1.0g) with appropriate safety factor
- Blade retention ultimate load: 1.5× maximum aerodynamic and centrifugal loads
- Retention through single fastener failure (fail-safe design)

**Verification:** Analysis (blade retention stress analysis with 1.5 factor of safety), Test (static blade retention testing to ultimate load), Inspection (production blade retention hardware inspection and torque verification)

---

**SRD-ROTOR-002: Blade Tracking and Vibration Limits**  
Rotor blade tracking and vibration shall be maintained within limits to prevent:
- Structural fatigue damage (high-cycle fatigue life reduction)
- Blade-to-blade contact
- Excessive cabin vibration (occupant discomfort and equipment damage)

**Tracking tolerance:** ±0.5 inch at blade tip  
**Vibration limits:**
- 1/rev: <0.2 inches per second (IPS) vertical at crew stations
- N/rev (N=number of blades): <0.4 IPS vertical at crew stations

**Verification:** Test (flight test vibration survey at all operating conditions), Analysis (blade tracking adjustment procedure validation), Inspection (production blade tracking inspection)

---

**SRD-ROTOR-003: Rotor Overspeed Protection**  
Rotor speed shall be governed within the following limits:
- **Nominal operating speed:** 268 RPM ±2%
- **Maximum transient:** 288 RPM (107% nominal) for <5 seconds (structural design limit)
- **Automatic limiting:** Engine governor prevents sustained rotor overspeed >285 RPM
- **Warning:** Caution annunciation at 280 RPM, warning at 285 RPM with automatic power reduction

**Verification:** Test (ground test with governor failure simulation, flight test validation of governing), Analysis (rotor dynamics analysis at overspeed conditions)

---

**SRD-ROTOR-004: Foreign Object Damage (FOD) Protection**  
Rotor blades shall be protected against damage from foreign object impact:
- **Leading edge protection:** Titanium or stainless steel erosion strip on blade leading edges
- **Lightning protection:** Lightning diverter strips integrated into leading edge protection
- **Impact tolerance:** Blade shall sustain bird strike (4 lb bird at cruise speed) without catastrophic failure
- **Damage tolerance:** Detectable damage (>1 inch leading edge dent) shall not propagate to failure before next scheduled inspection

**Verification:** Test (ballistic impact testing per AC 29-2C MG-7, bird strike testing), Analysis (damage tolerance analysis with crack growth modeling)

---

### 4.7 Structural Integrity Requirements

**SRD-STR-001: Design Load Factors**  
Primary structure shall be designed to the following load factors per MIL-STD-8698A:
- **Limit load:** Structure sustains load without permanent deformation
  - Positive: +3.5g (symmetric), +2.5g (with external load)
  - Negative: -1.0g (symmetric), -0.5g (with external load)
  - Lateral: ±2.0g
- **Ultimate load:** Structure sustains 1.5× limit load without failure (may exhibit permanent deformation)

**Verification:** Test (static airframe structural test to ultimate load for all critical load cases), Analysis (Finite Element Analysis validated against component testing)

---

**SRD-STR-002: Fatigue and Damage Tolerance**  
Primary structure shall be designed as damage-tolerant structure per AC 29-2C MG-18:
- **Detectable damage:** Structure with single-element damage (crack, corrosion, impact) survives for ≥2 inspection intervals
- **Inspection intervals:** Defined based on crack growth analysis and non-destructive inspection capability
- **Retirement life:** Component retirement before damage propagates to critical size with high confidence (99.9% survival)

**Verification:** Analysis (fatigue and damage tolerance analysis with 2× safety factor on crack growth life), Test (full-scale fatigue testing to 2× design life with periodic inspections)

---

**SRD-STR-003: Static Strength Verification**  
A full-scale static test article shall be subjected to ultimate loads for the following critical conditions:
- Symmetric pull-up (+3.5g × 1.5 = 5.25g)
- Asymmetric roll (±2.0g × 1.5 = ±3.0g lateral)
- Hard landing (vertical landing load case)
- External load: 16,000 lb × 1.5 = 24,000 lb on each cargo hook
- Ground handling loads (towing, jacking)

**Test article shall sustain all loads without structural failure (static test program plan TBD, coordinate with FAA ACO).**

**Verification:** Test (static airframe test per FAA-approved test plan)

---

**SRD-STR-004: Composite Structure Damage Tolerance**  
Composite primary structure shall demonstrate tolerance to:
- **Impact damage:** Barely Visible Impact Damage (BVID) from 100 ft-lb impact shall not reduce residual strength below limit load
- **Environmental degradation:** Hot/wet conditioning per AC 20-107B shall not reduce allowables below design values
- **Lightning strike:** Direct lightning strike per SAE ARP5416 shall not cause ignition or loss of structural integrity

**Verification:** Test (composite coupon and element testing per CMH-17 methodology, full-scale lightning strike testing), Analysis (building-block approach with validated material properties)

---

## 5. AUTONOMY SAFETY REQUIREMENTS

### 5.1 Autonomous Flight Control Safety

**SRD-AUT-001: Loss of Autonomous Control Probability**  
Per PRB Section 3.5, the probability of loss of autonomous control function shall not exceed:
- **Threshold:** 1×10⁻⁷ per flight hour
- **Objective:** 1×10⁻⁸ per flight hour

Loss of autonomous control is defined as inability to maintain controlled flight without human intervention (GCS pilot override or onboard pilot, if present).

**Verification:** Analysis (Fault Tree Analysis allocating to software and hardware components), Test (autonomous failure modes testing with recovery validation)

---

**SRD-AUT-002: Autonomous GNC Redundancy**  
The autonomous Guidance, Navigation, and Control (GNC) system shall employ dual-redundant computers with the following architecture:
- **Hot-standby configuration:** Both GNC computers operating continuously; automatic failover <100 ms
- **Independent navigation:** Each GNC computer receives data from independent GPS/INS sensors
- **Cross-monitoring:** Continuous comparison of GNC outputs; disagreement >threshold triggers failover and alert
- **Manual override:** GCS pilot can assume direct control at any time; autonomous system disengages within 200 ms

**Verification:** Analysis (FMEA demonstrating continued autonomous operation after single GNC computer failure), Test (GNC computer failure injection testing), Demonstration (piloted simulation with GNC failover)

---

**SRD-AUT-003: Autonomous System Design Assurance**  
Autonomous flight-critical software shall be developed to DO-178C Design Assurance Level (DAL) as follows:
- **Primary GNC software:** DAL A (loss of function is catastrophic)
- **Navigation sensor fusion:** DAL A
- **DAA collision avoidance logic:** DAL B (loss of function is hazardous)
- **Mission management software:** DAL C (loss degrades mission capability)

Hardware components (processors, sensors) shall be developed to DO-254 equivalent DALs.

**Verification:** Inspection (software development process audit per DO-178C), Analysis (software safety assessment), Test (software verification testing per DO-178C objectives for each DAL)

---

**SRD-AUT-004: Autonomous Mode Transitions**  
Transitions between autonomous and manual (GCS) control shall be:
- **Commanded transitions:** Smooth transfer with no transients; ≤2 seconds transition time
- **Automatic reversion:** If autonomous system detects inability to continue safe flight, automatic reversion to GCS control with alert
- **Transient suppression:** No uncommanded aircraft motion >0.1g during transition
- **Indication:** Clear, unambiguous indication to GCS pilot of active control mode at all times

**Verification:** Test (flight test of all transition scenarios), Demonstration (piloted simulation with transitions under varied flight conditions)

---

**SRD-AUT-005: Autonomous System Health Monitoring**  
Continuous monitoring of autonomous system health with the following capabilities:
- **Self-test:** Comprehensive Built-In Test (BIT) on power-up and periodic in-flight (every 60 seconds)
- **Performance monitoring:** Real-time comparison of commanded vs. achieved flight path; deviation >threshold triggers alert
- **Sensor validation:** Cross-check of redundant navigation sensors; failed sensor automatically removed from solution
- **Predictive monitoring:** Degradation trends detected and annunciated before function loss

**Verification:** Test (BIT coverage testing, sensor failure injection), Analysis (monitoring coverage assessment per FMEA)

---

### 5.2 Detect-and-Avoid (DAA) Requirements

**SRD-DAA-001: DAA System Compliance**  
The Detect-and-Avoid (DAA) system shall comply with:
- **ASTM F3442-20:** "Standard Specification for Detect and Avoid System Performance"
- **RTCA DO-365B:** "Minimum Operational Performance Standards for Detect and Avoid Systems"
- **FAA Order 8900.1 (Volume 16, Chapter 1):** Guidance for UAS operations in the NAS

**Verification:** Analysis (compliance matrix against ASTM F3442 requirements), Test (DAA certification testing per DO-365B MOPS), Demonstration (shadow-mode testing during manned flight operations)

---

**SRD-DAA-002: DAA Detection Performance**  
The DAA system shall detect and track air traffic with the following performance:

| Traffic Type | Detection Range (min) | Tracking Accuracy | Update Rate |
|--------------|-----------------------|-------------------|-------------|
| **Cooperative (ADS-B)** | 10 nm (Threshold), 15 nm (Objective) | ±0.1 nm horizontal, ±100 ft vertical | 1 Hz |
| **Non-cooperative (Radar)** | 3 nm (Threshold), 5 nm (Objective) | ±0.3 nm horizontal, ±200 ft vertical | 2 Hz |
| **Visual (EO/IR, objective)** | 2 nm | ±0.2 nm | 5 Hz |

**Missed detection rate:** ≤1×10⁻⁶ per flight hour (intruder aircraft within 5 nm)  
**False alarm rate:** <1 per 100 flight hours (Threshold), <1 per 500 flight hours (Objective)

**Verification:** Test (DAA sensor performance testing against calibrated targets, flight test with live traffic), Analysis (detection probability modeling with Monte Carlo simulation)

---

**SRD-DAA-003: Collision Avoidance Maneuvers**  
Upon detection of collision threat (Time to Closest Point of Approach <60 seconds, miss distance <500 ft), the DAA system shall:
- **Alert GCS:** Immediate visual and aural alert to GCS pilot with traffic display overlay
- **Automatic maneuver (if no GCS response within 10 seconds):**
  - Maneuver authority: ±30° bank, ±500 fpm vertical rate, ±20 KIAS speed change
  - Maneuver objective: Increase miss distance to ≥1,500 ft horizontal, ≥500 ft vertical
  - Maneuver completion: Return to original flight path after threat resolved
- **GCS override:** GCS pilot may override automatic maneuver at any time

**Well Clear definition:** ≥2,000 ft horizontal, ≥450 ft vertical (per RTCA DO-365B)

**Verification:** Test (flight test with scripted collision encounters, DAA logic validation in simulation), Demonstration (live traffic testing with chase aircraft)

---

**SRD-DAA-004: DAA Sensor Integration and Fusion**  
DAA sensors (ADS-B In, Radar, EO/IR) shall be integrated with automatic sensor fusion:
- **Track correlation:** Tracks from multiple sensors automatically correlated (same target)
- **Sensor weighting:** Track quality based on sensor confidence (e.g., ADS-B prioritized over radar for cooperative traffic)
- **Redundancy:** Loss of any single DAA sensor does not eliminate DAA capability (degraded performance acceptable)

**Verification:** Test (multi-sensor fusion validation testing with known traffic scenarios), Analysis (sensor fusion algorithm validation)

---

### 5.3 Lost-Link Behavior and Contingency Management

**SRD-LINK-001: Lost-Link Definition**  
"Lost-link" condition is declared when:
- No command/control messages received from GCS for >30 seconds (primary LOS datalink)
- No backup link (SATCOM or secondary LOS) available for >120 seconds

**Verification:** Test (flight test with link interruption at various phases of flight), Demonstration (simulation of lost-link scenarios)

---

**SRD-LINK-002: Lost-Link Behavior (Phased Response)**  
Upon lost-link condition, the aircraft shall execute the following autonomous sequence:

**Phase 1 (0-30 seconds): Link Re-Acquisition Attempt**
- Continue current mission segment (e.g., maintain loiter, continue transit to next waypoint)
- Expand link search pattern (frequency hopping, antenna steering)
- Climb altitude if terrain-obscured (up to +1,000 ft)

**Phase 2 (30-120 seconds): Hold and Search**
- Establish loiter orbit at current position
- Continue aggressive link search (all available datalinks)
- Reduce airspeed to loiter speed (85 KTAS) to maximize endurance

**Phase 3 (>120 seconds): Pre-Programmed Contingency Execution**
Execute pre-programmed lost-link contingency per mission profile:
- **Option A (default): Return-to-Launch (RTL)**
  - Navigate to launch/home base via shortest safe route
  - Execute autonomous landing at surveyed landing zone
- **Option B: Land-at-Nearest-Suitable-Site**
  - Identify suitable landing site within gliding distance using terrain database and DVE sensors
  - Execute autonomous landing
- **Option C: Loiter-Until-Fuel-Critical, then Land**
  - Loiter at current position until fuel <30 min reserve
  - Identify and execute landing at nearest suitable site

**Fuel exhaustion contingency:** If fuel reaches 20 min reserve and no link re-established, automatic transition to emergency autoland at nearest site.

**Verification:** Test (flight test of all lost-link phases with link restoration at various times), Demonstration (end-to-end lost-link scenario testing from mission planning through autonomous landing)

---

**SRD-LINK-003: Link Re-Establishment**  
When datalink is re-established after lost-link condition:
- Immediate status report to GCS (fuel state, position, system health)
- GCS pilot may resume control or allow autonomous completion of RTL/land
- Lost-link event automatically logged with detailed telemetry for post-mission analysis

**Verification:** Test (link re-establishment testing at all phases of lost-link response), Demonstration (operator procedures validation in GCS trainer)

---

**SRD-LINK-004: Lost-Link Recovery Success Rate**  
Per PRB Section 3.5, lost-link safe recovery (successful RTL or autoland without damage) shall be achieved in ≥99.9% of lost-link events.

**Verification:** Analysis (reliability prediction for lost-link recovery sequence), Test (statistical validation through repeated lost-link testing >100 trials in simulation), Demonstration (flight test lost-link recovery ≥10 times without failure)

---

### 5.4 Fail-Safe Modes and Degraded Operations

**SRD-FAIL-001: Autonomous System Failure Modes**  
Upon detection of autonomous system degradation or failure, the aircraft shall automatically transition to appropriate fail-safe mode:

| Failure Condition | Fail-Safe Mode | Required Action |
|-------------------|----------------|-----------------|
| **Loss of primary GPS** | GPS-denied navigation (INS + vision-based nav) | RTL to surveyed site within INS drift limits (<50 m CEP after 15 min) |
| **Loss of all GPS** | Manual GCS control required | Alert GCS, revert to direct pilot control, navigate to known position via pilotage |
| **Loss of single GNC computer** | Automatic failover to backup GNC | Continue autonomous ops with reduced redundancy; RTL at next suitable time |
| **Loss of both GNC computers** | Revert to basic flight control (stability augmentation only) | GCS pilot assumes direct control; execute precautionary landing |
| **DAA sensor failure (single)** | Degraded DAA (reduced range/coverage) | Continue autonomous ops in Class G airspace only; avoid controlled airspace |
| **DAA total failure** | Visual flight rules (VFR) only | Immediate GCS notification; operate only in visual conditions with GCS visual observer; RTL ASAP |
| **Datalink degraded (intermittent)** | Reduce autonomous authority | Simplify mission tasks; avoid complex maneuvers; remain within GCS visual range if possible |

**Verification:** Demonstration (failure modes testing in piloted simulation), Test (flight test with induced failures and fail-safe mode validation)

---

**SRD-FAIL-002: Degraded Mode Flight Envelope**  
In degraded autonomous modes, flight envelope shall be automatically restricted:
- **Reduced VNE:** From 165 KTAS to 120 KTAS (reduced control authority or sensor availability)
- **Increased margins:** Minimum altitude increased from 10 ft AGL to 50 ft AGL (reduced precision navigation)
- **Prohibited operations:** No external load operations in degraded mode; no operations in IMC; no operations in controlled airspace (unless ATC coordination)

**Verification:** Analysis (degraded mode flight envelope analysis), Test (flight test validation of reduced envelope)

---

**SRD-FAIL-003: Manual Override Authority**  
At all times during autonomous operations, the GCS pilot shall have the capability to:
- **Assume direct control:** Override autonomous system within 200 ms of command
- **Terminate autonomous sequence:** Abort any autonomous maneuver (landing, DAA avoidance, etc.)
- **Command emergency procedures:** Immediate engine shutdown, emergency descent, etc.

Override commands shall have priority over all autonomous functions with immediate (<100 ms) system response.

**Verification:** Test (manual override testing during all autonomous modes), Demonstration (GCS pilot override validation in simulation and flight test)

---

### 5.5 Ground Control Station (GCS) Safety

**SRD-GCS-001: GCS Redundancy and Availability**  
The GCS shall be designed for high availability:
- **Dual operator stations:** Either station can control aircraft; automatic handover <5 seconds
- **No single-point failures:** Loss of any single GCS component does not result in loss of control (aircraft reverts to autonomous mode)
- **Uninterruptible power:** Battery backup for ≥30 minutes of GCS operation after facility power loss

**Verification:** Test (GCS component failure testing with handover validation), Demonstration (GCS failure scenarios in operational environment)

---

**SRD-GCS-002: GCS Human Factors Safety**  
The GCS operator interface shall be designed per human factors safety principles:
- **Alerting hierarchy:** Critical alerts (collision, system failure) use distinct visual/aural coding prioritized over non-critical alerts
- **Mode awareness:** Current control mode (autonomous, manual, degraded) clearly indicated at all times with no ambiguity
- **Workload management:** GCS pilot workload <70% during normal operations (measured via NASA-TLX or equivalent)
- **Crew Resource Management:** Procedures support effective crew coordination for multi-operator operations

**Verification:** Test (human factors usability testing with representative operators), Analysis (task analysis and workload assessment), Demonstration (operational scenarios with experienced and novice crews)

---

**SRD-GCS-003: GCS Cybersecurity**  
The GCS and datalink shall be protected against cyber threats:
- **Encryption:** All command/control messages encrypted per FIPS 140-2 (AES-256 minimum)
- **Authentication:** Mutual authentication between GCS and aircraft prevents unauthorized control
- **Intrusion detection:** Real-time monitoring for anomalous commands or datalink activity
- **Physical security:** GCS facility access control and surveillance

**Verification:** Test (cybersecurity penetration testing by independent red team), Inspection (security architecture review), Analysis (threat assessment per NIST SP 800-171)

---

## 6. STRUCTURAL INTEGRITY AND CRASHWORTHINESS

### 6.1 Structural Design Requirements

**SRD-STR-101: Load Factor Compliance**  
Detailed in Section 4.7, SRD-STR-001.

---

**SRD-STR-102: Fatigue Life Requirements**  
Detailed in Section 4.7, SRD-STR-002.

---

**SRD-STR-103: Composite Structure Lightning Protection**  
Detailed in Section 4.2, SRD-ELEC-003.

---

### 6.2 Crashworthiness Requirements

**SRD-CRASH-001: Crashworthiness Design Standard**  
The aircraft shall be designed to crashworthiness standards per MIL-STD-1290A (Light Fixed- and Rotary-Wing Aircraft Crash Resistance):
- **Vertical impact:** 30 ft/s (20 mph) with <50g peak occupant deceleration
- **Horizontal impact:** 40 ft/s (27 mph) with <30g peak occupant deceleration
- **Combined impact:** 42 ft/s vector (30 vertical + 40 horizontal simultaneous)

**Verification:** Test (full-scale crash test with instrumented anthropomorphic test dummies), Analysis (crash dynamics simulation validated against sled testing)

---

**SRD-CRASH-002: Occupant Protection**  
Crew and passenger seating shall provide occupant protection:
- **Energy-attenuating seats:** Stroke ≥6 inches, load-limiting <15g average during stroke
- **Restraints:** 5-point harness (crew), 4-point or lap belt (passengers) with <3,000 lb ultimate tensile load
- **Head strike protection:** Padded or energy-absorbing surfaces within head strike envelope
- **Post-crash egress:** All exits operable after crash impact with <50 lb force; emergency exit marking visible in low-light conditions

**Verification:** Test (seat drop testing per MIL-STD-1290 Appendix A), Analysis (occupant injury analysis using simulation tools), Demonstration (egress testing after full-scale crash test)

---

**SRD-CRASH-003: Fuel System Crashworthiness**  
Detailed in Section 4.3, SRD-PROP-003. Additionally:
- **No fuel spillage:** Fuel system sustains crash impact without spillage external to aircraft for ≥5 minutes post-crash
- **Fire prevention:** No ignition sources (hot surfaces, electrical arcs) in proximity to fuel system; bonding prevents electrostatic discharge

**Verification:** Test (fuel cell drop testing per MIL-STD-1290, post-crash fuel spillage measurement)

---

**SRD-CRASH-004: Emergency Egress**  
Emergency egress capability shall be provided:
- **Egress time:** All occupants can egress within 90 seconds via normal and emergency exits
- **Emergency exits:** Jettison panels or doors operable from inside and outside; marked with high-visibility markings
- **Post-crash fire survival:** Structure provides ≥5 minutes protection from external fire for occupant egress

**Verification:** Demonstration (egress time trial with full crew and passengers), Test (emergency exit operation after crash test)

---

### 6.3 Bird Strike and Foreign Object Impact

**SRD-IMPACT-001: Bird Strike Tolerance**  
Windshield and rotor blades shall withstand bird strikes per FAA AC 29-2C MG-7:
- **Windshield:** 4 lb bird at cruise speed (135 KTAS) shall not penetrate windshield or cause incapacitation of pilot (if optionally-piloted)
- **Rotor blades:** 4 lb bird at cruise speed shall not cause catastrophic blade failure; detectable damage permissible if <50% strength reduction

**Verification:** Test (windshield bird strike testing per AS5485, rotor blade ballistic impact testing with simulated bird)

---

**SRD-IMPACT-002: Hail and Ice Impact**  
Structure and windows exposed to hail/ice impact during flight shall withstand:
- **Hail size:** 1.5 inch diameter hail at cruise speed
- **Ice shedding:** Ice shed from rotor blades shall not penetrate fuselage or damage critical systems

**Verification:** Test (coupon-level hail impact testing), Analysis (ice shedding trajectory analysis and protection design)

---

## 7. FIRE PROTECTION AND HAZARDOUS MATERIALS

### 7.1 Fire Detection and Suppression

**SRD-FIRE-001: Fire Zones**  
Designated fire zones shall be identified and protected per AC 29-2C MG-12:
- **Powerplant fire zones:** Engine compartments, transmission compartments, exhaust systems
- **Fuel fire zones:** Fuel tanks, fuel lines, fuel system components
- **Electrical fire zones:** High-power electrical equipment bays (inverters, generators)

Each fire zone shall be:
- Isolated by fire-resistant barriers (≥15 minute burn-through resistance)
- Equipped with fire detection (dual-loop) and suppression systems
- Drained to prevent pooling of flammable fluids

**Verification:** Analysis (fire zone mapping and barrier analysis), Test (fire barrier burn-through testing per FAR 25 Appendix F), Demonstration (fire detection and suppression system functional testing)

---

**SRD-FIRE-002: Fire Detection System**  
Detailed in Section 4.3, SRD-PROP-002. Additional requirements:
- **Dual-loop:** Two independent fire detection loops in each fire zone; alert on single-loop detection, confirmed fire on dual detection
- **Detection time:** <5 seconds from ignition to crew/GCS alert
- **False alarm rate:** <1 per 5,000 flight hours per fire zone
- **Test capability:** Built-in test function verifies detection system integrity before each flight

**Verification:** Test (fire detection system certification testing per TSO-C1a), Analysis (fire detection coverage assessment)

---

**SRD-FIRE-003: Fire Suppression System**  
Detailed in Section 4.3, SRD-PROP-002. Additional requirements:
- **Agent:** Halon 1301 or approved environmentally acceptable alternative (e.g., HFC-125)
- **Discharge time:** ≤2 seconds after activation
- **Agent quantity:** Sufficient to suppress fire in largest fire zone with margin
- **Dual-shot capability:** Two suppression discharges available for re-ignition

**Verification:** Test (fire suppression effectiveness testing per MIL-DTL-38310), Demonstration (ground fire testing with suppression activation)

---

**SRD-FIRE-004: Flammable Fluid Leakage Management**  
Systems containing flammable fluids (fuel, hydraulic fluid, oil) shall:
- **Leak detection:** Sensors detect fluid leakage ≥1 quart/min with alert to crew/GCS
- **Drainage:** Leaked fluids drain overboard via firewall-penetrating drains (no pooling in fire zones)
- **Ignition prevention:** No ignition sources (electrical, hot surfaces >450°F) in drainage paths

**Verification:** Analysis (drainage system design review), Test (fluid leakage detection testing), Demonstration (simulated leak with drainage verification)

---

### 7.2 Material Flammability

**SRD-FLAM-001: Cabin Material Flammability**  
All materials in crew and cabin areas shall meet flammability requirements per FAR 25.853:
- **Burn rate:** <2.5 inches/minute (horizontal burn test)
- **Heat release rate:** <65 kW-min/m² (Ohio State University calorimeter test)
- **Smoke density:** <200 (NBS smoke chamber test)

**Verification:** Test (material flammability testing per FAR 25 Appendix F)

---

**SRD-FLAM-002: Insulation and Soundproofing Material**  
Thermal and acoustic insulation materials shall be:
- **Fire-resistant:** Self-extinguishing within 15 seconds of flame removal
- **Non-dripping:** No flaming drips that could ignite adjacent materials

**Verification:** Test (insulation flammability testing per FAR 25.856)

---

**SRD-FLAM-003: Wiring and Wire Bundle Flammability**  
Electrical wiring insulation shall meet:
- **Flame propagation:** Self-extinguishing per FAR 25.869 (60-degree angle test)
- **Arc tracking resistance:** >300 seconds to tracking failure (FAA Technical Order)

**Verification:** Test (wire insulation flammability and arc tracking testing)

---

### 7.3 Hazardous Materials Management

**SRD-HAZ-001: Hazardous Materials Identification**  
All hazardous materials used in aircraft construction, operation, and maintenance shall be identified and managed per:
- **OSHA Hazard Communication Standard (29 CFR 1910.1200)**
- **EPA hazardous waste regulations (40 CFR 260-279)**
- **DoD hazardous materials management (DoDI 4715.08)**

Hazardous materials shall be listed in the Aircraft Hazardous Materials Inventory (AHMI) with Safety Data Sheets (SDS) maintained.

**Verification:** Inspection (AHMI review and SDS availability audit)

---

**SRD-HAZ-002: Composite Material Safety**  
Composite structure manufacturing and maintenance operations shall address:
- **Respiratory protection:** Workers exposed to composite dust (carbon fiber, epoxy) provided with appropriate respirators
- **Skin protection:** Protective clothing and gloves prevent epoxy resin skin contact
- **Fire hazards:** Dust collection systems prevent combustible dust accumulation

**Verification:** Inspection (manufacturing safety procedures audit), Demonstration (worker safety training completion)

---

**SRD-HAZ-003: Ordnance and Explosive Safety (if applicable to MAAP-1F variant)**  
If the MAAP-1F variant carries explosive ordnance (rockets, missiles):
- **Compliance:** MIL-STD-1576 (Electroexplosive Subsystem Safety), NAVSEA OP 5 Vol 1 (Ammunition and Explosives Safety Ashore)
- **Electrical protection:** RF hazards analysis for electromagnetic radiation effects on ordnance (EMR per MIL-STD-464D Section 5.12)
- **Lightning protection:** Ordnance shall be protected from direct lightning attachment and induced currents

**Verification:** Analysis (explosive safety analysis and EMR hazard assessment), Test (lightning and EMR testing of ordnance installation)

---

## 8. DESIGN ASSURANCE LEVEL (DAL) ALLOCATION

### 8.1 DAL Allocation Methodology

Design Assurance Levels (DALs) shall be assigned to aircraft systems,

## 8. DESIGN ASSURANCE LEVEL (DAL) ALLOCATION

### 8.1 DAL Allocation Methodology

Design Assurance Levels (DALs) shall be assigned to aircraft systems, subsystems, software, and hardware components based on the Functional Hazard Assessment (FHA) and Fault Tree Analysis (FTA) conducted per ARP4761. The allocation process follows:

1. **Functional Hazard Assessment (FHA):** Identify all aircraft functions and assess qualitative severity of function loss
2. **Preliminary System Safety Assessment (PSSA):** Allocate quantitative failure probability targets to systems
3. **Common Cause Analysis (CCA):** Identify potential common-mode failures across redundant channels
4. **Design Assurance Level Assignment:** Map failure condition severity to DAL per DO-178C (software) and DO-254 (hardware)

**DAL Assignment Criteria (per ARP4761 / AC 29-2C MG-9):**

| Failure Condition Classification | Software DAL (DO-178C) | Hardware DAL (DO-254) | Development Assurance |
|----------------------------------|------------------------|----------------------|---------------------|
| **Catastrophic** | DAL A | DAL A | Highest rigor; formal methods encouraged; independence required |
| **Hazardous/Severe-Major** | DAL B | DAL B | High rigor; independence required |
| **Major** | DAL C | DAL C | Moderate rigor; peer reviews required |
| **Minor** | DAL D | DAL D | Basic rigor; standard development practices |
| **No Safety Effect** | DAL E or no DAL | DAL E or no DAL | Industry-standard commercial practices acceptable |

### 8.2 Flight Control System DAL Allocation

**SRD-DAL-001: Flight Control Software DAL**  
Flight control system software shall be developed and verified to the following Design Assurance Levels:

| Software Component | DAL | Rationale |
|--------------------|-----|-----------|
| **Primary Flight Control Laws (Channels 1 & 2)** | DAL A | Loss results in catastrophic failure (loss of aircraft control) |
| **Backup Flight Control Laws (Channel 3)** | DAL A | Must provide equivalent safety after dual primary channel failure |
| **Control Law Mode Logic** | DAL A | Incorrect mode transition can result in loss of control |
| **Actuator Command Processing** | DAL A | Direct control surface command generation |
| **Sensor Validation and Voting Logic** | DAL B | Failure can result in undetected sensor fault, hazardous condition |
| **Flight Envelope Protection** | DAL B | Loss degrades safety margins but pilot/GCS can maintain control |
| **Trim and Stability Augmentation** | DAL B | Loss results in degraded handling qualities |
| **Built-In Test (BIT) Software** | DAL C | Failure results in undetected system degradation (major) |
| **Maintenance and Diagnostic Software** | DAL D | No direct flight safety impact |

**Verification:** Inspection (software development plan review per DO-178C), Test (software verification at each DAL level per DO-178C objectives), Analysis (software safety assessment traceability)

---

**SRD-DAL-002: Flight Control Hardware DAL**  
Flight control system hardware shall be developed and verified to the following Design Assurance Levels:

| Hardware Component | DAL | Rationale |
|--------------------|-----|-----------|
| **Flight Control Computers (FCCs)** | DAL A | Catastrophic failure if all FCCs fail |
| **Control Surface Actuators** | DAL B | Dual-redundant per axis; single failure is hazardous but not catastrophic |
| **Position Sensors (LVDT/RVDT)** | DAL B | Dual-redundant per actuator; voting logic detects single failure |
| **Air Data Sensors** | DAL B | Dual-redundant; loss of single sensor is hazardous |
| **Inertial Measurement Units (IMUs)** | DAL B | Triple-redundant; voting logic isolates failures |
| **Power Supplies (flight control bus)** | DAL A | Loss of power to all FCCs is catastrophic |
| **Hydraulic System Components** | DAL B | Dual-redundant hydraulics; single system failure is hazardous |

**Verification:** Inspection (hardware development review per DO-254), Test (environmental qualification testing per RTCA DO-160G), Analysis (reliability prediction and FMEA)

---

### 8.3 Autonomous GNC System DAL Allocation

**SRD-DAL-003: Autonomous GNC Software DAL**  
Autonomous Guidance, Navigation, and Control (GNC) software shall be developed to the following DALs:

| Software Component | DAL | Rationale |
|--------------------|-----|-----------|
| **Primary GNC Computer (Channels 1 & 2)** | DAL A | Loss of autonomous control is catastrophic in zero-pilot configuration |
| **Navigation Sensor Fusion (GPS/INS integration)** | DAL A | Loss results in navigation failure and inability to complete autonomous mission safely |
| **Waypoint Navigation Logic** | DAL B | Loss results in mission abort but manual GCS control available (hazardous) |
| **DAA Collision Avoidance Logic** | DAL B | Loss results in inability to detect/avoid traffic (hazardous) |
| **Lost-Link Contingency Logic** | DAL A | Incorrect RTL/autoland can result in catastrophic outcome |
| **Autoland/Precision Approach Logic** | DAL A | Incorrect landing commands can result in controlled flight into terrain |
| **Mission Management Software** | DAL C | Loss degrades mission effectiveness but does not threaten safety directly |
| **Payload Management Software** | DAL C | Loss impacts mission but not flight safety (unless external load release failure) |

**Verification:** Inspection (DO-178C compliance audit), Test (autonomous mission scenario testing with failure injection), Demonstration (shadow-mode testing during manned operations)

---

**SRD-DAL-004: Autonomous GNC Hardware DAL**  
Autonomous GNC hardware shall be developed to the following DALs:

| Hardware Component | DAL | Rationale |
|--------------------|-----|-----------|
| **GNC Computers (dual-redundant)** | DAL A | Loss of both computers results in loss of autonomous capability |
| **GPS Receivers (triple-redundant)** | DAL B | Dual-redundant with INS backup; single failure is hazardous |
| **Inertial Navigation Systems (dual INS)** | DAL B | Dual-redundant with GPS backup; single failure is hazardous |
| **Radar Altimeter** | DAL B | Critical for autoland; dual-redundant |
| **EO/IR Sensors (terrain/obstacle detection)** | DAL C | Degraded visual environment sensor; loss impacts autoland capability (major) |
| **DAA Sensors (ADS-B, Radar)** | DAL B | Loss results in reduced collision avoidance capability (hazardous) |

**Verification:** Inspection (DO-254 compliance review), Test (sensor qualification testing), Analysis (hardware reliability prediction)

---

### 8.4 Propulsion and Transmission System DAL Allocation

**SRD-DAL-005: Engine Control System DAL**  
Engine Full Authority Digital Engine Control (FADEC) software and hardware shall meet the following DALs:

| Component | DAL | Rationale |
|-----------|-----|-----------|
| **FADEC Software (Primary Channel)** | DAL A | Single-engine failure with loss of FADEC is catastrophic at low altitude |
| **FADEC Software (Backup Channel)** | DAL A | Dual-channel FADEC per engine; must be fail-operational |
| **FADEC Hardware (Dual-Channel per Engine)** | DAL A | Loss of both FADEC channels results in engine shutdown |
| **Engine Overspeed Protection Logic** | DAL A | Failure can result in uncontained engine failure (catastrophic) |
| **Fire Detection System (Dual-Loop)** | DAL B | Failure results in undetected engine fire (hazardous) |
| **Fire Suppression Control Logic** | DAL B | Failure to suppress fire results in hazardous condition |
| **Fuel Shutoff Valve Control** | DAL A | Must operate correctly to isolate failed engine |

**Verification:** Inspection (FADEC certification review per engine OEM standards), Test (FADEC failure modes testing), Analysis (engine system FMEA)

---

**SRD-DAL-006: Transmission Health Monitoring**  
Transmission health monitoring system components shall meet the following DALs:

| Component | DAL | Rationale |
|-----------|-----|-----------|
| **Chip Detector System** | DAL B | Failure results in undetected transmission degradation (hazardous) |
| **Oil Pressure/Temperature Monitoring** | DAL B | Failure results in inability to detect lubrication loss |
| **Transmission Vibration Monitoring (HUMS)** | DAL C | Degraded predictive maintenance capability (major impact) |
| **Torque and RPM Monitoring** | DAL B | Critical for detecting transmission overload |

**Verification:** Test (sensor failure injection testing), Analysis (monitoring coverage assessment)

---

### 8.5 Electrical Power System DAL Allocation

**SRD-DAL-007: Electrical Power System DAL**  
Electrical power generation, distribution, and management system components shall meet the following DALs:

| Component | DAL | Rationale |
|-----------|-----|-----------|
| **Generator Control Units (GCU)** | DAL A | Loss of all electrical power is catastrophic (loss of flight control) |
| **Electrical Load Management Software** | DAL B | Incorrect load shedding can result in loss of essential systems (hazardous) |
| **Battery Management System** | DAL B | Battery backup required for 30-min safe landing after dual generator failure |
| **Power Distribution Units (PDUs)** | DAL B | Critical for routing power to essential buses |
| **Circuit Protection (Essential Buses)** | DAL B | Incorrect breaker operation can result in loss of essential systems |
| **Voltage/Frequency Regulation** | DAL B | Out-of-tolerance power can damage avionics |

**Verification:** Test (electrical system failure testing, load shedding validation), Analysis (electrical load analysis)

---

### 8.6 Avionics and Data Bus DAL Allocation

**SRD-DAL-008: Core Avionics Bus DAL**  
Core avionics data bus and communication systems shall meet the following DALs:

| Component | DAL | Rationale |
|-----------|-----|-----------|
| **Flight-Critical Data Bus (redundant channels)** | DAL A | Loss of data communication between FCCs and actuators is catastrophic |
| **Mission Data Bus** | DAL C | Loss degrades mission capability but not flight safety |
| **Datalink Command Processing (C2 link)** | DAL B | Loss results in lost-link condition (hazardous if contingency logic fails) |
| **SATCOM/LOS Datalink Hardware** | DAL C | Redundant datalinks; single link loss is major (mission degradation) |
| **Voice Communication System** | DAL D | Loss impacts coordination but not flight safety directly |

**Verification:** Inspection (data bus architecture review), Test (data bus failure injection testing), Analysis (communication latency and reliability analysis)

---

### 8.7 DAA and Collision Avoidance System DAL Allocation

**SRD-DAL-009: DAA System DAL**  
Detect-and-Avoid system components shall meet the following DALs:

| Component | DAL | Rationale |
|-----------|-----|-----------|
| **ADS-B In Receiver** | DAL B | Loss results in inability to detect cooperative traffic (hazardous) |
| **Non-Cooperative Radar** | DAL B | Loss results in inability to detect non-cooperative traffic (hazardous) |
| **DAA Track Fusion and Correlation Logic** | DAL B | Incorrect track data can result in missed collision threat |
| **Collision Avoidance Maneuver Logic** | DAL B | Incorrect maneuver can result in hazardous condition |
| **Traffic Display (GCS)** | DAL C | Display failure requires operator to rely on aural alerts |
| **DAA Self-Test and Monitoring** | DAL C | Failure results in undetected DAA degradation (major) |

**Verification:** Test (DAA sensor performance testing, collision scenario testing), Demonstration (live traffic flight testing)

---

### 8.8 Software Development Process Requirements

**SRD-DAL-010: DO-178C Compliance**  
All flight-critical software shall be developed in accordance with RTCA DO-178C "Software Considerations in Airborne Systems and Equipment Certification" with the following objectives satisfied:

**DAL A Software Objectives:**
- **Planning Process:** Software Plans reviewed and approved; independence from development team
- **Development Process:** High-level requirements (HLR), low-level requirements (LLR), software architecture, source code developed with requirements-based coverage analysis
- **Verification Process:** 
  - Requirements-based testing (HLR coverage, LLR coverage)
  - Structural coverage analysis (Modified Condition/Decision Coverage - MC/DC for all code)
  - Robustness testing (boundary value, error injection)
  - Independent verification and validation (IV&V)
- **Configuration Management:** Baseline control, change control, version control, traceability
- **Quality Assurance:** Independent audits, process compliance verification, tool qualification
- **Certification Liaison:** Coordination with FAA for software accomplishment summary (SAS)

**DAL B Software Objectives:**
- Same as DAL A with reduced structural coverage (Decision Coverage rather than MC/DC)
- Reduced independence requirements (peer reviews acceptable)

**DAL C Software Objectives:**
- Requirements-based testing with statement coverage
- Peer reviews for verification
- Standard configuration management practices

**Verification:** Inspection (software development plan audit per DO-178C), Analysis (software accomplishment summary review), Test (software verification review at each lifecycle phase)

---

**SRD-DAL-011: DO-254 Compliance (Complex Hardware)**  
All flight-critical complex hardware (FPGAs, ASICs, programmable logic devices) shall be developed in accordance with RTCA DO-254 "Design Assurance Guidance for Airborne Electronic Hardware" with objectives appropriate to the assigned DAL:

**DAL A Hardware Objectives:**
- Hardware design life cycle planning with independence
- Requirements capture and traceability
- Conceptual design with safety assessment
- Detailed design with formal verification methods
- Hardware/software integration testing
- Validation and verification per DO-254 Tables A-1 through A-10
- Configuration management and quality assurance equivalent to DO-178C
- Tool qualification for hardware development and verification tools

**Verification:** Inspection (hardware development review per DO-254), Test (environmental qualification per DO-160G), Analysis (hardware safety assessment)

---

### 8.9 DAL Traceability and Documentation

**SRD-DAL-012: Safety Assessment Documentation**  
For all systems assigned DAL A or DAL B, the following safety assessment documentation shall be developed and maintained:

1. **Functional Hazard Assessment (FHA):** System-level failure effects and severity classification
2. **Preliminary System Safety Assessment (PSSA):** Architectural analysis demonstrating compliance with safety requirements
3. **System Safety Assessment (SSA):** Final quantitative analysis demonstrating catastrophic failure probability ≤1×10⁻⁹ per flight hour
4. **Software Safety Assessment:** Analysis per DO-178C showing software contribution to system failure rates
5. **Hardware Safety Assessment:** Analysis per DO-254 showing hardware contribution to system failure rates
6. **Common Cause Analysis (CCA):** Identification of potential common-mode failures and mitigations

All documentation shall be traceable to this SRD and the Program Requirements Baseline (PRB).

**Verification:** Inspection (safety assessment documentation review at PDR, CDR, and Type Certification), Analysis (traceability matrix validation)

---

**SRD-DAL-013: Independent Verification and Validation (IV&V)**  
For all DAL A systems, an independent verification and validation (IV&V) organization, separate from the development team and reporting independently to the Program Manager, shall:
- Review all software and hardware requirements, design, and implementation
- Conduct independent testing (witness or perform verification testing)
- Review test results and verification evidence
- Provide independent assessment of compliance with DO-178C / DO-254 objectives
- Issue IV&V reports at each major milestone (PDR, CDR, qualification, certification)

**Verification:** Inspection (IV&V reports reviewed and accepted by System Safety Manager and Airworthiness Authority)

---

## 9. HAZARD IDENTIFICATION AND RISK MANAGEMENT

### 9.1 Hazard Analysis Process

**SRD-HAZ-001: System Safety Program Requirements**  
The MAAP-1 program shall implement a System Safety Program per MIL-STD-882E "System Safety" with the following tailoring for civil/military dual-certification:

**Process Flow:**
1. **Preliminary Hazard List (PHL):** Developed at program initiation, updated continuously
2. **Preliminary Hazard Analysis (PHA):** Conducted during conceptual and preliminary design phases
3. **Subsystem Hazard Analysis (SSHA):** Conducted during detailed design phase for each subsystem
4. **System Hazard Analysis (SHA):** Integrates SSHA results; conducted during integration and test
5. **Operating and Support Hazard Analysis (O&SHA):** Addresses ground operations, maintenance, and support hazards
6. **Functional Hazard Assessment (FHA):** Per ARP4761, identifies aircraft-level functional failures
7. **Fault Tree Analysis (FTA):** Top-down analysis for catastrophic and hazardous failure conditions
8. **Failure Modes and Effects Analysis (FMEA) / FMECA:** Bottom-up analysis at component level

**Verification:** Inspection (hazard analysis documentation review at each design review), Analysis (hazard tracking system audit)

---

**SRD-HAZ-002: Hazard Risk Assessment Criteria**  
All identified hazards shall be assessed using the MIL-STD-882E Risk Assessment Matrix:

**Severity Categories:**

| Category | Description | Definition |
|----------|-------------|------------|
| **Catastrophic (I)** | Loss of aircraft and/or multiple fatalities | Could result in death, permanent total disability, loss exceeding $10M, or environmental catastrophe |
| **Critical (II)** | Severe injury, major system damage | Could result in permanent partial disability, injuries requiring hospitalization of 3+ personnel, loss $1M-$10M |
| **Marginal (III)** | Minor injury, minor system damage | Could result in injury or occupational illness resulting in lost work day(s), loss $100K-$1M |
| **Negligible (IV)** | Minimal injury, minimal system damage | Could result in injury not requiring lost work, loss <$100K |

**Probability Levels:**

| Level | Description | Quantitative (per flight hour) | Qualitative |
|-------|-------------|-------------------------------|-------------|
| **Frequent (A)** | Likely to occur frequently | >1×10⁻³ | Continuously experienced |
| **Probable (B)** | Will occur several times | >1×10⁻⁵ to ≤1×10⁻³ | Will occur frequently |
| **Occasional (C)** | Likely to occur sometime | >1×10⁻⁷ to ≤1×10⁻⁵ | Will occur several times |
| **Remote (D)** | Unlikely but possible | >1×10⁻⁹ to ≤1×10⁻⁷ | Unlikely but can reasonably be expected to occur |
| **Improbable (E)** | Very unlikely | ≤1×10⁻⁹ | Unlikely to occur but possible |

**Risk Assessment Matrix:**

| Severity → <br> Probability ↓ | Catastrophic (I) | Critical (II) | Marginal (III) | Negligible (IV) |
|-------------------------------|------------------|---------------|----------------|-----------------|
| **Frequent (A)** | High | High | Serious | Medium |
| **Probable (B)** | High | High | Serious | Medium |
| **Occasional (C)** | High | Serious | Medium | Low |
| **Remote (D)** | Serious | Medium | Medium | Low |
| **Improbable (E)** | Medium | Medium | Low | Low |

**Risk Acceptance Authority:**

| Risk Level | Acceptance Authority | Action Required |
|------------|---------------------|-----------------|
| **High** | Program Manager + Milestone Decision Authority | Unacceptable; must mitigate before approval |
| **Serious** | Program Manager + PSRB | Requires mitigation plan with timeline |
| **Medium** | Program Manager | Mitigation plan recommended; risk acceptance documented |
| **Low** | Chief Engineer or System Safety Manager | Accept with monitoring; document rationale |

**Verification:** Analysis (hazard risk assessment completed for all identified hazards), Inspection (PSRB review minutes documenting risk acceptance decisions)

---

**SRD-HAZ-003: Hazard Tracking System (HTS)**  
All hazards identified throughout the program lifecycle shall be entered into the Hazard Tracking System (HTS) with the following data fields:

- Hazard ID (unique identifier)
- Hazard description
- Affected system/subsystem
- Severity category (I-IV)
- Probability level (A-E)
- Risk level (High/Serious/Medium/Low)
- Hazard cause (failure modes, external factors)
- Hazard effects (consequences)
- Mitigation approach (design, procedural, warning)
- Verification method (how mitigation effectiveness is verified)
- Status (Open / Mitigated / Closed)
- Responsible organization
- Target closure date
- Actual closure date
- Risk acceptance authority and date

The HTS shall be reviewed monthly at Program Management Reviews (PMRs) and Program Safety Review Board (PSRB) meetings. Any new High or Serious risk hazards shall trigger immediate PSRB review within 5 working days.

**Verification:** Inspection (HTS database audit), Demonstration (HTS reporting at PMR and PSRB meetings)

---

### 9.2 Top-Level Hazards and Mitigations

The following table identifies the preliminary top-level hazards for the MAAP-1 program (derived from FHA). This list shall be refined during detailed design and updated in the HTS.

**SRD-HAZ-004: Preliminary Hazard List**

| Hazard ID | Hazard Description | Severity | Probability (Objective) | Risk Level | Primary Mitigation Approach |
|-----------|-------------------|----------|------------------------|------------|----------------------------|
| **HAZ-001** | Loss of autonomous control due to GNC computer failure | Catastrophic (I) | Improbable (E) | Medium | Dual-redundant GNC computers with automatic failover; manual GCS override |
| **HAZ-002** | Mid-air collision due to DAA system failure | Catastrophic (I) | Remote (D) | Serious | Redundant DAA sensors (ADS-B + Radar); GCS pilot monitoring; automatic collision avoidance |
| **HAZ-003** | Loss of aircraft control due to flight control system failure | Catastrophic (I) | Improbable (E) | Medium | Triplex flight control computers with dissimilar redundancy; dual actuators per axis |
| **HAZ-004** | Uncontrolled flight into terrain due to navigation failure | Catastrophic (I) | Remote (D) | Serious | Triple-redundant GPS, dual INS, terrain database, radar altimeter; automatic pull-up |
| **HAZ-005** | Loss of both engines (dual engine failure) | Catastrophic (I) | Improbable (E) | Medium | Independent engine systems; autorotation capability demonstrated; fuel system redundancy |
| **HAZ-006** | Transmission failure (loss of rotor drive) | Catastrophic (I) | Improbable (E) | Medium | Transmission TBO enforcement; run-dry capability (30 min); chip detector monitoring |
| **HAZ-007** | Structural failure (rotor blade separation or fuselage break-up) | Catastrophic (I) | Improbable (E) | Medium | Damage-tolerant structure; periodic inspections; ultimate load testing; flutter analysis |
| **HAZ-008** | Loss of tail control (directional control failure) | Catastrophic (I) | N/A | N/A | Not applicable (tandem-rotor design has no tail rotor) |
| **HAZ-009** | Fire in engine compartment with inability to suppress | Critical (II) | Occasional (C) | Serious | Dual-loop fire detection; automatic fire suppression; firewall integrity |
| **HAZ-010** | Loss of electrical power (dual generator failure) | Hazardous (II) | Remote (D) | Medium | Dual independent generators; 30-min battery backup for essential loads; automatic load shedding |
| **HAZ-011** | Unintended external load release | Critical (II) | Occasional (C) | Serious | Dual-independent load release control; automatic release inhibit in unsafe conditions |
| **HAZ-012** | Lightning strike causing avionics failure or fuel ignition | Critical (II) | Occasional (C) | Serious | Lightning protection per MIL-STD-464D; bonding and grounding; shielded avionics |
| **HAZ-013** | Icing accumulation causing loss of rotor lift or control | Critical (II) | Occasional (C) | Serious | Ice detection system; automatic icing alert and flight envelope restriction; optional deice system |
| **HAZ-014** | Hydraulic system failure (loss of flight control authority) | Hazardous (II) | Remote (D) | Medium | Dual independent hydraulic systems; each system capable of full control authority |
| **HAZ-015** | Fuel exhaustion due to incorrect fuel planning or leak | Critical (II) | Occasional (C) | Serious | Redundant fuel quantity indication; automatic low-fuel warnings; fuel leak detection |
| **HAZ-016** | Rotor overspeed (structural failure due to excessive RPM) | Catastrophic (I) | Remote (D) | Serious | Engine governor system with dual-channel redundancy; rotor overspeed warning and automatic power reduction |
| **HAZ-017** | Bird strike causing windshield penetration or rotor damage | Critical (II) | Probable (B) | High | Windshield designed to 4-lb bird strike; rotor blades tested to ballistic impact; damage tolerance |
| **HAZ-018** | Cybersecurity breach (unauthorized command injection) | Catastrophic (I) | Remote (D) | Serious | Encrypted datalinks (AES-256); mutual authentication; intrusion detection; physical GCS security |
| **HAZ-019** | Loss of communication (lost-link) with inability to execute RTL | Critical (II) | Occasional (C) | Serious | Dual-redundant datalinks (LOS + SATCOM); autonomous lost-link procedures tested; fuel reserves for RTL |
| **HAZ-020** | External load pendulum oscillation causing loss of control | Critical (II) | Occasional (C) | Serious | Load stability monitoring; automatic damping via flight control; load weight/configuration limits |
| **HAZ-021** | Ground collision during autonomous taxi | Marginal (III) | Probable (B) | Serious | Autonomous taxi obstacle detection (LIDAR/cameras); low-speed taxi limits; ground crew monitoring |
| **HAZ-022** | Hard landing causing landing gear collapse or airframe damage | Critical (II) | Occasional (C) | Serious | Autoland system with radar altimeter; sink rate limiting; crashworthy landing gear and structure |
| **HAZ-023** | Brownout/whiteout conditions causing DVE landing accident | Critical (II) | Occasional (C) | Serious | DVE sensors (LIDAR, millimeter-wave radar); autonomous landing abort logic; pilot takeover option |
| **HAZ-024** | Incorrect CG due to load miscalculation or shift | Critical (II) | Remote (D) | Medium | Automatic weight & balance calculation; CG monitoring; load shift detection; ballast system |
| **HAZ-025** | Maintenance error (incorrect assembly or missed inspection) | Critical (II) | Occasional (C) | Serious | Maintenance procedures with checkpoints; HUMS monitoring; independent inspection requirements |

**Note:** This preliminary hazard list shall be expanded during Subsystem Hazard Analysis (SSHA) to include all identified component-level and operational hazards. Each hazard shall have a detailed Hazard Analysis Report (HAR) documenting causes, effects, mitigations, and verification.

**Verification:** Analysis (hazard analysis reports completed for all preliminary hazards), Inspection (PSRB review and acceptance of hazard mitigations)

---

### 9.3 Safety-Critical Functions and Items List

**SRD-HAZ-005: Safety-Critical Functions**  
The following aircraft functions are designated as **Safety-Critical** (loss of function results in Catastrophic or Hazardous failure condition):

1. **Primary Flight Control:** Pitch, roll, yaw authority via fly-by-wire system
2. **Autonomous GNC:** Navigation accuracy, waypoint following, autoland capability
3. **Engine Control:** FADEC operation, overspeed protection, fuel shutoff
4. **Transmission Lubrication:** Oil pressure/temperature monitoring, chip detection
5. **Electrical Power:** Generation, distribution to essential buses, battery backup
6. **Fire Detection and Suppression:** Engine/transmission fire zones
7. **Navigation:** GPS/INS position accuracy for autonomous operations
8. **Detect-and-Avoid:** Traffic detection, collision avoidance maneuvers
9. **Lost-Link Contingency:** RTL/autoland execution after communication loss
10. **Rotor Speed Governing:** Maintain rotor RPM within safe limits
11. **Load Factor Limiting:** Prevent structural overstress via flight envelope protection
12. **External Load Release:** Controlled release in emergency and on command

All Safety-Critical functions shall be subject to Fault Tree Analysis (FTA) demonstrating compliance with allocated failure probability requirements. No single-point failure in a Safety-Critical function shall result in loss of aircraft (per PRB C-3).

**Verification:** Analysis (FTA for each Safety-Critical function), Inspection (design review demonstrating fault tolerance)

---

**SRD-HAZ-006: Safety-Critical Items List (SCIL)**  
All hardware and software components that perform Safety-Critical functions shall be identified on the Safety-Critical Items List (SCIL) and subject to enhanced configuration control:

**Configuration Control Requirements for SCIL Items:**
- Class I configuration control (Program Manager approval required for changes)
- Serialized tracking with individual component history records
- Enhanced receiving inspection and acceptance testing
- Restricted substitution (no "equivalent" replacements without engineering analysis)
- Traceability to raw material certifications (for dynamic components)
- Mandatory failure reporting and corrective action for any SCIL item failure

**SCIL Items (Preliminary, to be finalized at CDR):**
- Flight Control Computers (all three channels)
- Control surface actuators
- FADEC units (all channels, both engines)
- GNC computers (both channels)
- GPS receivers and INS units
- Transmission assemblies (forward, aft, interconnect shaft)
- Rotor hubs and blade retention hardware
- Main rotor blades
- Engine fuel control units and shutoff valves
- Electrical generators and generator control units
- Primary structure load-path fittings and attachments

**Verification:** Inspection (SCIL maintained in configuration management system), Analysis (traceability from SCIL to Hazard Analysis and FTA)

---

## 10. GROUND SAFETY

### 10.1 Ground Handling and Servicing Safety

**SRD-GND-001: Ground Operations Hazard Analysis**  
An Operating and Support Hazard Analysis (O&SHA) shall be conducted to identify and mitigate hazards associated with:
- Aircraft ground handling (towing, jacking, tie-down)
- Fueling and defueling operations
- Engine ground runs and maintenance run-ups
- Rotor blade installation/removal
- Battery charging and electrical servicing
- Hydraulic and oil servicing
- External load rigging and cargo loading
- Maintenance tasks requiring entry into confined spaces or work at height

**Verification:** Inspection (O&SHA documentation review), Analysis (ground safety procedures derived from O&SHA)

---

**SRD-GND-002: Rotor Blade Safety**  
Rotor blades present significant ground safety hazards due to:
- Blade droop when rotor is not turning (blades hang below hub, head-strike hazard)
- Blade flapping during startup and shutdown (dynamic motion hazard)
- Rotor downwash (high-velocity air, FOD generation)

**Safety Requirements:**
- Rotor safety arcs marked on ground with high-visibility paint/cones (minimum 50 ft radius)
- Blade droop clearance markers installed on ground during maintenance
- Blade tie-down provisions when rotor is not turning
- No personnel entry within rotor disc area when engines are running (except authorized flight crew with specific training and PPE)
- Rotor engagement/disengagement procedures with positive ground crew communication

**Verification:** Demonstration (ground operations procedures validation), Inspection (rotor safety markings and signage)

---

**SRD-GND-003: Fueling Safety**  
Fuel servicing operations shall comply with:
- NFPA 407 "Standard for Aircraft Fuel Servicing"
- MIL-STD-3033 "Fueling and Defueling Operations"

**Safety Requirements:**
- Bonding cable connected before fuel nozzle connection (static discharge prevention)
- Fire extinguisher (150 lb minimum, PKP or Halon) positioned within 50 ft of aircraft during fueling
- No smoking/open flames within 50 ft of aircraft during fueling
- Engines shut down during fueling (no hot refueling without specific authorization and additional safety measures)
- Fuel spillage containment and cleanup procedures
- Single-point refuel connection with self-sealing coupling (prevents spillage if hose disconnected under pressure)

**Verification:** Demonstration (fueling procedures validation), Test (fuel system ground testing including spillage containment)

---

**SRD-GND-004: Engine Ground Run Safety**  
Ground engine runs (maintenance run-ups, functional checks) shall be conducted in accordance with:

**Safety Requirements:**
- Designated engine run-up area with blast deflectors or sufficient clearance (minimum 200 ft behind aircraft)
- Rotor blade tie-downs removed and rotor engagement checklist completed
- Trained ground crew with communication headsets assigned to monitor aircraft during run
- Fire watch posted with fire extinguisher
- No personnel or equipment within 100 ft forward or lateral to aircraft (rotor downwash and FOD hazard)
- Chocks installed and parking brake set
- Foreign Object Damage (FOD) walk-down before engine start
- Emergency shutdown procedures briefed to all personnel

**Verification:** Demonstration (ground run procedures validation), Inspection (engine run area markings and safety equipment)

---

**SRD-GND-005: Maintenance Safety**  
Maintenance tasks identified as high-risk in the O&SHA shall have detailed safety procedures including:

| Maintenance Task | Safety Hazard | Mitigation Measures |
|------------------|---------------|---------------------|
| **Rotor blade removal** | Blade drop, pinch points | Blade slings rated to 500 lb; lockout/tagout for rotor brake; two-person minimum |
| **Engine removal** | Heavy lift (450 lb), hot surfaces | Engine hoist with redundant rigging; cool-down period; protective gloves |
| **Confined space entry (fuel tanks)** | Toxic fumes, oxygen deficiency | Atmospheric testing; forced ventilation; attendant outside tank; rescue harness |
| **Work at height (rotor hub, pylon)** | Fall hazard | Fall arrest system; work platforms with guardrails; two-point tie-off |
| **Electrical maintenance (high voltage)** | Electrocution | Lockout/tagout procedures; insulated tools; qualified electrician only |
| **Hydraulic system servicing** | High-pressure fluid injection injury | Depressurize system before opening; protective gloves and face shield |
| **Transmission oil change** | Hot oil burns | Cool-down period (2 hours minimum); protective equipment; drain pan with spill containment |

**Verification:** Demonstration (maintenance procedures validation with safety observation), Inspection (maintenance manual safety warnings and checklists)

---

### 10.2 Transport and Storage Safety

**SRD-GND-006: Aircraft Transport Configuration**  
Aircraft transport (ground or air transport) shall comply with the following configuration requirements:

**Ground Transport (Truck/Trailer):**
- Rotor blades removed and secured in blade containers
- Main transmission drained of oil (or secured with sealing caps)
- Landing gear tie-downs installed
- Battery disconnected (master switch off, external power source removed)
- All access panels secured and safety-wired
- Protective covers installed (engine intakes, exhaust, pitot/static ports)

**Air Transport (C-17, C-130J):**
- Rotor pylons folded or removed per transportability plan
- Weight and CG calculated and certified for transport aircraft
- Aircraft tie-down at hard points (10,000 lb rated tie-down fittings, 8 locations minimum)
- Protective padding at tie-down contact points
- Nitrogen-charged struts (landing gear) to prevent settling

**Verification:** Demonstration (transport configuration procedures validation), Inspection (transportability plan review and load certification)

---

**SRD-GND-007: Storage and Preservation**  
Aircraft in long-term storage (>30 days) shall be preserved per the following requirements:

**Preservation Procedures:**
- Rotor blades removed and stored horizontally on blade racks (prevents warping)
- Engine preservation per engine OEM manual (corrosion inhibiting oil, desiccant plugs in intakes/exhausts)
- Transmission preservation (oil maintained or drained and flushed with preservative)
- Fuel system preservation (fuel drained or fuel stabilizer added)
- Landing gear and flight controls locked in neutral position
- Cockpit/cabin dehumidification (desiccant bags, dehumidifier unit, or climate-controlled storage)
- Battery removed and stored in climate-controlled facility with trickle charging
- Protective covers installed (airframe cover, engine covers, window covers)

**Inspection Requirements:**
- Weekly inspection during storage (visual check for corrosion, fluid leaks, pest intrusion)
- Monthly operational checks (landing gear extension/retraction if applicable, flight control movement, electrical system power-up)
- De-preservation and return-to-service inspection before first flight after storage >90 days

**Verification:** Inspection (preservation procedures documented in maintenance manual), Demonstration (preservation and de-preservation procedures validated)

---

**SRD-GND-008: Foreign Object Damage (FOD) Prevention**  
FOD prevention program shall include:

**FOD Prevention Measures:**
- FOD walks conducted before every flight (100 ft radius around aircraft)
- Tool control program (shadow boards, tool inventory checklists)
- Engine intake covers installed whenever engines not running
- Magnetic FOD detection devices in high-traffic areas
- Personnel training on FOD awareness and reporting
- Incident reporting system for FOD events and near-misses

**Verification:** Inspection (FOD program procedures review), Demonstration (FOD walk and tool control procedures validated)

---

## 11. FLIGHT SAFETY AND OPERATIONAL CONSTRAINTS

### 11.1 Flight Envelope Protection

**SRD-FLT-001: Automatic Flight Envelope Protection System**  
The flight control system shall incorporate automatic flight envelope protection to prevent:

| Condition | Protection Method | Alert Threshold | Hard Limit |
|-----------|-------------------|-----------------|------------|
| **VNE Exceedance** | Automatic pitch-up command, collective reduction | 160 KTAS (97% VNE) | 165 KTAS (VNE) |
| **Positive Load Factor Excess** | Automatic cyclic input limiting | +3.3g (94% limit load) | +3.5g (limit load) |
| **Negative Load Factor Excess** | Automatic cyclic input limiting | -0.9g (90% limit load) | -1.0g (limit load) |
| **Rotor Overspeed** | Automatic collective increase, throttle reduction | 280 RPM (104% nominal) | 288 RPM (107% nominal) |
| **Rotor Underspeed (in flight)** | Automatic collective reduction, throttle increase | 250 RPM (93% nominal) | 240 RPM (90% nominal) |
| **Bank Angle (autonomous mode)** | Automatic roll limiting | 50° bank angle | 60° bank angle |
| **Descent Rate** | Automatic collective increase, descent rate limiting | 2,500 fpm | 3,000 fpm (except autorotation) |

**Pilot/GCS Override:**
- Pilot (optionally-piloted MAAP-1F) may override envelope protection via persistent control input (>5 seconds continuous input beyond limit)
- GCS operator may override autonomous limits via Emergency Direct Control mode (authenticated command sequence)
- Override events automatically logged for post-flight review

**Verification:** Test (flight test validation of envelope protection limits), Demonstration (piloted simulation with envelope exceedance attempts)

---

**SRD-FLT-002: Stall and Retreating Blade Stall Protection**  
The aircraft shall provide warning and protection against aerodynamic stall conditions:

**Stall Warning:**
- Onset of retreating blade stall detected via rotor system vibration monitoring (accelerometers on rotor hub)
- Crew/GCS alert at 90% of stall boundary (based on airspeed, load factor, density altitude)
- Automatic airspeed reduction command in autonomous mode if stall boundary approached

**Stall Protection:**
- Flight control system automatically limits aft cyclic and collective inputs approaching stall boundary
- Maximum demonstrated airspeed reduced at high density altitude and high gross weight (automatic scheduling based on performance model)

**Verification:** Test (flight test demonstration of stall warning and protection at various conditions), Analysis (rotor aerodynamic stall boundary modeling)

---

### 11.2 External Load Operations Safety

**SRD-FLT-003: External Load Operational Limits**  
External sling load operations shall be conducted within the following limits:

| Parameter | Single Hook (12,000 lb) | Single Hook (16,000 lb Objective) | Dual Hook (8k + 8k lb) |
|-----------|------------------------|----------------------------------|------------------------|
| **Maximum Airspeed** | 120 KTAS | 100 KTAS | 110 KTAS |
| **Maximum Wind (Steady/Gust)** | 20 kt / 30 kt | 15 kt / 25 kt | 18 kt / 28 kt |
| **Load Pendulum Angle (Max)** | 20° from vertical | 15° from vertical | 15° per load |
| **Maximum Altitude (AGL, hover)** | 200 ft | 150 ft | 200 ft |
| **Maximum Sling Length** | 120 ft | 100 ft | 120 ft per load |
| **Load Factor Limits** | +2.5g / -0.5g | +2.0g / -0.3g | +2.5g / -0.5g |

**External Load Certification:**
- All external load configurations require load certification (load weight, dimensions, drag coefficient measured or estimated)
- Automatic load stability monitoring via load cell and angle sensors
- Automatic load release if pendulum angle exceeds 25° or load cell detects structural overload

**Verification:** Test (flight test with representative external loads), Demonstration (load stability monitoring system validation)

---

**SRD-FLT-004: Emergency External Load Release**  
Emergency jettison of external load shall be available with the following requirements:

**Emergency Release Triggers (Automatic):**
- Load pendulum oscillation exceeding 25° amplitude for >10 seconds (uncontrollable load)
- Load weight exceeding hook rating by >10% (overload detection)
- Single-engine failure below OEI hover ceiling with load (automatic load jettison enables OEI safe landing)
- Pilot/GCS emergency jettison command (instantaneous release on command)

**Release Mechanism:**
- Electrically actuated cargo hook with redundant release solenoids
- Mechanical backup release (cable-pull handle in cockpit for MAAP-1F, GCS command for autonomous)
- Release time: <0.5 seconds from command to load separation
- Load release indication: Visual and aural alert to crew/GCS

**Jettison Zone Restrictions:**
- Automatic jettison inhibited over populated areas (geofencing database integrated with GNC)
- Pilot/GCS override available if jettison required for flight safety (crew decision authority)

**Verification:** Test (cargo hook release testing with instrumented loads), Demonstration (emergency jettison procedures validation in simulation and flight test)

---

### 11.3 Environmental Operating Constraints

**SRD-FLT-005: Weather Minimums (Autonomous Operations)**  
Autonomous flight operations (MAAP-1C, MAAP-1I) shall be restricted to the following weather minimums:

| Parameter | Autonomous Operations (Threshold) | Autonomous Operations (Objective) | Optionally-Piloted (MAAP-1F) |
|-----------|----------------------------------|----------------------------------|------------------------------|
| **Ceiling (Cloud Base)** | 1,000 ft AGL | 500 ft AGL | 300 ft AGL (VFR minima) |
| **Visibility** | 3 statute miles | 1 statute mile | 1/2 statute mile (with DVE sensors) |
| **Wind (Surface, Steady/Gust)** | 25 kt / 35 kt | 35 kt / 45 kt | 40 kt / 50 kt (pilot judgment) |
| **Icing Conditions** | Prohibited (non-FIKI baseline) | Light icing with optional icing kit | Moderate icing with FIKI kit |
| **Turbulence** | Light to Moderate | Moderate | Severe (limit operations, pilot judgment) |
| **Thunderstorms** | 20 nm avoidance radius | 10 nm avoidance (with weather radar) | 5 nm avoidance (pilot judgment with radar) |

**Autonomous Weather Decision Logic:**
- Real-time weather data ingested from onboard sensors (air data, OAT probe) and datalink (NEXRAD, METAR, TAF)
- Automatic mission abort if weather deteriorates below minimums
- Return-to-base or divert-to-alternate if destination weather below minimums
- No autonomous takeoff if current weather below minimums

**Verification:** Demonstration (autonomous weather decision logic tested in simulation with varied weather scenarios), Test (flight test in various weather conditions within safe limits)

---

**SRD-FLT-006: Night Operations**  
Night flight operations (civil twilight to civil dawn) shall comply with:

**Autonomous Night Operations:**
- Autonomous night operations authorized for MAAP-1C and MAAP-1I if:
  - Lighting system operational (navigation lights, anti-collision beacon, landing/search lights)
  - Night vision compatible cockpit lighting (if crew present)
  - Autonomous landing site equipped with approach lighting (surveyed sites only) or DVE sensors operational
  - GCS operator night-qualified and current

**Optionally-Piloted Night Operations (MAAP-1F):**
- Pilot night-current (3 takeoffs/landings to a full stop in preceding 90 days)
- Night vision goggles (NVGs) authorized with NVG-compatible cockpit lighting

**Verification:** Test (night flight test program validating systems and procedures), Demonstration (night autonomous landing validation)

---

### 11.4 Emergency Procedures and Escape Systems

**SRD-FLT-007: Emergency Autorotation Procedures**  
Emergency autorotation procedures following complete loss of engine power shall be:

**Autorotation Entry (Immediate Actions):**
1. Lower collective immediately (maintain rotor RPM in green arc: 260-276 RPM)
2. Establish autorotation airspeed: 65 KIAS (best glide)
3. Select suitable landing area within gliding distance
4. Transmit emergency call (if time permits): "Mayday, Mayday, [callsign], dual engine failure, autorotating"

**Autorotation Descent:**
- Glide ratio: 2.8:1 (no wind)
- Rate of descent: 1,800 fpm at 65 KIAS
- Maintain rotor RPM: 260-276 RPM (adjust collective as required)
- Plan approach to landing area (aim for 50 ft AGL at normal approach angle)

**Landing Flare and Touchdown:**
- Begin flare at 50-100 ft AGL (depending on rate of descent)
- Apply aft cyclic to reduce rate of descent and forward groundspeed
- Apply collective at minimum altitude (ground effect height) to cushion landing
- Touchdown at minimum practical groundspeed and vertical speed

**Autonomous Autorotation:**
- Autonomous GNC system capable of executing autorotation and landing without pilot intervention (Objective capability, to be demonstrated during flight test)
- Automatic selection of landing site from terrain database and real-time DVE sensor data
- Automatic flare and touchdown with collective management

**Verification:** Test (autorotation demonstration at various weights and altitudes per certification requirements), Demonstration (autonomous autorotation validation in flight test)

---

**SRD-FLT-008: Ditching Procedures (Water Landing)**  
In the event of forced landing on water:

**Ditching Procedures:**
- Approach into wind (if possible) at minimum safe airspeed (60 KIAS)
- Maintain level attitude; avoid nose-down or tail-low attitude at touchdown
- Touchdown at minimum rate of descent (<500 fpm)
- Crew/passengers don life vests before ditching if time permits
- Emergency exits usable after ditching (cabin does not flood immediately due to sealed structure)

**Flotation System (Optional):**
- Emergency flotation system (inflatable bags) available as optional kit for maritime operations
- Flotation system provides ≥30 minutes flotation time for evacuation

**Verification:** Analysis (ditching loads and structural integrity analysis), Demonstration (ditching procedures briefed and practiced in simulator)

---

**SRD-FLT-009: Crew Escape and Survivability (MAAP-1F Optionally-Piloted)**  
Crew escape and survival equipment shall include:

**Crew Survival Equipment:**
- Crashworthy crew seats with 5-point harness (16g forward, 8g lateral, 20g vertical crashworthiness per MIL-STD-1290)
- Emergency exits: 2× crew doors (74 in × 78 in aft ramp), jettison-able cockpit windows
- Emergency egress lighting (battery-powered, automatic activation on electrical failure)
- Fire extinguisher (5 lb Halon or equivalent, cockpit-mounted)
- First aid kit (per FAA requirements)
- Survival kit (cold weather or overwater configuration depending on mission area)
- Emergency Locator Transmitter (ELT) with 406 MHz beacon

**Emergency Egress Time:**
- All crew members shall be capable of egressing aircraft within 90 seconds via normal and emergency exits (demonstrated during certification)

**Verification:** Test (emergency egress time trial), Demonstration (crew survival equipment functionality validation)

---

## 12. CERTIFICATION AND AIRWORTHINESS BASIS

### 12.1 Certification Strategy

**SRD-CERT-001: Dual Civil/Military Certification Approach**  
The MAAP-1 program shall pursue a phased dual-certification approach:

**Phase 1: Civil Type Certification (MAAP-1C Baseline)**
- Certification Authority: FAA Aircraft Certification Office (ACO)
- Certification Basis: 14 CFR Part 29 (Transport Category Rotorcraft), Amendment 29-XX (TBD at certification basis agreement)
- Special Conditions: Autonomous flight systems, optionally-piloted operations, beyond visual line of sight (BVLOS) operations
- Target: Type Certificate (TC) issued by Program Month (PM) 84

**Phase 2: Military Airworthiness Approval (MAAP-1I, MAAP-1F Military Variants)**
- Certification Authority: U.S. Air Force (MAAP-1I ISR), U.S. Navy/USMC (MAAP-1F Firefighting for military wildfire operations if applicable)
- Certification Basis: MIL-HDBK-516C (Airworthiness Certification Criteria), applicable service-specific airworthiness requirements
- Approach: Leverage FAA TC as basis; supplement with military-specific requirements (crashworthiness, survivability, electromagnetic effects)
- Target: Military Flight Release by PM 90

**Phase 3: Variant Type Certification (MAAP-1F Firefighting Variant)**
- Certification Authority: FAA ACO
- Certification Basis: Amended Type Certificate (ATC) based on MAAP-1C TC
- Deltas: Optionally-piloted cockpit, external load provisions for firefighting equipment, water/retardant tank system
- Target: Amended TC by PM 90

**Verification:** Inspection (certification plan approved by FAA and military airworthiness authorities), Analysis (compliance checklist demonstrating coverage of all applicable regulations)

---

**SRD-CERT-002: Certification Basis Documentation**  
The certification basis shall be formally documented in the following submittals to the FAA:

1. **Type Certification Board (TCB) Establishment:** PM 18
   - Aircraft description and intended operations
   - Proposed certification basis (14 CFR Part 29, amendment level, Special Conditions)
   - Compliance plan overview

2. **Certification Plan:** PM 24
   - Detailed compliance methods for each regulation (Analysis, Test, Demonstration, Inspection)
   - Special Conditions justification and proposed means of compliance
   - Issue Papers for novel or high-risk certification items (autonomy, crashworthiness, etc.)
   - Delegation plan (Designated Engineering Representatives, if applicable)

3. **Type Inspection Authorization (TIA) Application:** PM 60
   - Conformity demonstration plan
   - Production conformance inspection procedures
   - Quality system documentation

4. **Certification Test Program:** PM 66-78
   - Ground testing (static structural test, systems integration testing)
   - Flight testing (performance, handling qualities, systems validation)

5. **Type Certificate Application:** PM 80
   - Compliance documentation (test reports, analysis reports, drawings)
   - Flight Manual (FAA-approved)
   - Type Certificate Data Sheet (TCDS) draft

**Verification:** Inspection (certification documentation reviewed and accepted by FAA at each milestone)

---

### 12.2 Special Conditions for Autonomous Operations

**SRD-CERT-003: Special Conditions Development**  
The following areas require FAA Special Conditions due to novel autonomous systems not addressed by existing Part 29 regulations:

| Special Condition Area | Issue Description | Proposed Means of Compliance |
|------------------------|-------------------|------------------------------|
| **Autonomous Flight Control System** | Part 29 assumes pilot-in-the-loop for flight control; autonomous system has no pilot override in MAAP-1C/I | Demonstrate equivalent level of safety via redundancy, fault tolerance, and lost-link procedures; probabilistic safety analysis (1×10⁻⁹ catastrophic failure rate) |
| **Detect-and-Avoid (DAA) System** | Part 29 assumes visual see-and-avoid by pilot; autonomous system requires electronic DAA | Compliance with ASTM F3442 and RTCA DO-365B; flight test demonstration of collision avoidance performance |
| **Beyond Visual Line of Sight (BVLOS)** | Part 29 assumes operations within visual range of pilot/observer | Datalink reliability demonstration; lost-link contingency procedures; geofencing and airspace coordination |
| **Ground Control Station (GCS)** | Part 29 does not address remote piloting concepts | GCS as extension of cockpit; human factors design per FAA Human Factors guidance; redundant GCS capability |
| **Cybersecurity** | Part 29 does not address cyber threats to command/control links | Compliance with RTCA DO-326A / DO-356A (Airworthiness Security); encryption, authentication, intrusion detection |
| **Software and Hardware Complexity** | Autonomous systems involve complex software/hardware not typical of Part 29 helicopters | DO-178C DAL A/B for flight-critical software; DO-254 DAL A/B for complex hardware; independent V&V |

**Special Conditions Coordination:**
- Draft Special Conditions submitted to FAA by PM 18 (PDR timeframe)
- Public comment period per FAA administrative process
- Final Special Conditions agreed and published by PM 30 (mid-detailed design phase)

**Verification:** Inspection (Special Conditions agreed and published in Federal Register), Analysis (compliance demonstration for each Special Condition)

---

### 12.3 Airworthiness Compliance Matrix

**SRD-CERT-004: Compliance Demonstration Matrix**  
A comprehensive compliance matrix shall be developed mapping each applicable regulation to verification method and status:

**Matrix Structure:**

| Regulation | Requirement Description | Compliance Method | Responsible Organization | Verification Evidence | Status |
|------------|------------------------|-------------------|-------------------------|----------------------|--------|
| 14 CFR 29.25 | Weight limits | Analysis + Test | Weights IPT | Weight & Balance Report, weighing test | Open / Closed |
| 14 CFR 29.143 | Controllability and maneuverability | Test (flight test) | Flight Test IPT | Flight Test Report 143 | Open / Closed |
| ... | ... | ... | ... | ... | ... |

**Compliance Methods:**
- **Analysis:** Engineering analysis, modeling, simulation (validated analysis tools)
- **Test:** Ground test or flight test with instrumented data collection
- **Demonstration:** Functional demonstration without detailed measurement (e.g., crew egress time trial)
- **Inspection:** Design review, drawing review, or physical inspection

**Compliance Status Tracking:**
- **Open:** Requirement identified, compliance approach defined, verification not yet started
- **In Progress:** Verification activity underway
- **Complete:** Verification evidence collected, awaiting FAA review
- **Closed:** FAA review complete, compliance accepted

The Compliance Demonstration Matrix shall be reviewed at each Program Design Review (PDR, CDR) and updated monthly during certification test program.

**Verification:** Inspection (Compliance Matrix reviewed and accepted by FAA ACO at CDR and Final Certification Review)

---

## 13. SAFETY TESTING AND VERIFICATION

### 13.1 Ground Safety Testing

**SRD-TEST-001: Static Structural Testing**  
A full-scale static structural test article shall be subjected to the following tests to demonstrate compliance with SRD-STR-001 (Design Load Factors):

**Test Sequence:**
1. **Proof Load Testing (Limit Load):**
   - Apply limit loads for all critical flight conditions
   - Inspect structure for permanent deformation (none permissible)
   - Load cases: +3.5g symmetric pull-up, ±2.0g lateral roll, -1.0g push-over, landing impact, external load (12,000 lb and 16,000 lb)

2. **Ultimate Load Testing (1.5× Limit Load):**
   - Apply ultimate loads (5.25g symmetric, ±3.0g lateral, etc.)
   - Structure must sustain ultimate load for 3 seconds without failure
   - Permanent deformation acceptable; catastrophic failure not acceptable

3. **Residual Strength Testing:**
   - After ultimate load testing, apply limit load to assess residual strength
   - Document permanent deformation and structural damage

**Test Article:**
- Production-representative airframe structure (not flight test article due to permanent deformation expected)
- Instrumented with strain gauges (500+ channels) to validate Finite Element Analysis (FEA) models

**Verification:** Test (static structural test per FAA-approved test plan), Analysis (FEA correlation with test results)

---

**SRD-TEST-002: Full-Scale Fatigue Testing**  
A full-scale fatigue test article shall be subjected to cyclic loading representing 2× design service life (40,000 equivalent flight hours):

**Test Objectives:**
- Validate safe-life and damage-tolerant design assumptions
- Identify fatigue-critical areas requiring inspection
- Develop inspection intervals and techniques

**Test Spectrum:**
- Load spectrum developed from mission profile analysis (typical flight loads, maneuver loads, gust loads)
- Accelerated testing with periodic inspections at intervals representing operational inspection schedule
- Teardown inspection at completion to assess damage tolerance margins

**Verification:** Test (full-scale fatigue test per AC 29-2C MG-18), Analysis (fatigue life prediction validated against test results)

---

**SRD-TEST-003: Crashworthiness Testing**  
Crashworthiness testing shall demonstrate compliance with SRD-CRASH-001 (MIL-STD-1290 design standard):

**Test Sequence:**

1. **Seat Drop Testing:**
   - Energy-attenuating crew seats tested to 15g average, 20g peak acceleration
   - Anthropomorphic test dummies (95th percentile male) instrumented with load cells and accelerometers
   - Pass/Fail criteria: <1,500 lb spinal load, <230 HIC (Head Injury Criterion)

2. **Full-Scale Airframe Drop Testing:**
   - Test article: Production-representative forward fuselage section with crew seats, landing gear, fuel cells installed
   - Drop conditions:
     - Test 1: 30 ft/s vertical impact
     - Test 2: 40 ft/s horizontal impact (simulated via pendulum swing or rocket sled)
     - Test 3: Combined 42 ft/s impact (30 vertical + 40 horizontal vector)
   - Instrumentation: High-speed video (1,000 fps), accelerometers on structure and dummies, fuel cell pressure sensors
   - Pass/Fail criteria: <50g peak occupant deceleration, no fuel spillage for 5 minutes post-impact, occupant survival space maintained

**Verification:** Test (crashworthiness testing per MIL-STD-1290 and FAA-approved test plan)

---

**SRD-TEST-004: Fire Testing**  
Fire detection and suppression system testing shall demonstrate compliance with SRD-FIRE-001 through SRD-FIRE-003:

**Test Sequence:**

1. **Fire Detection System Certification Testing:**
   - Detector response time testing (TSO-C1a compliance)
   - False alarm rate testing (thermal and vibration environments per DO-160G)
   - Coverage testing (all areas of fire zone have detection within 5 seconds)

2. **Firewall Burn-Through Testing:**
   - Firewall materials subjected to 2,000°F flame for 15 minutes per FAR 25 Appendix F
   - Acceptance criteria: No burn-through, no hot spots on cold side >400°F above ambient

3. **Fire Suppression Effectiveness Testing:**
   - Engine compartment mockup with fire source (fuel spray fire)
   - Fire suppression system activated and fire extinguished within 2 seconds
   - Re-ignition testing (second fire started after suppression, automatic second-shot discharge)

**Verification:** Test (fire testing per TSO-C1a, FAR 25 Appendix F, and MIL-DTL-38310)

---

### 13.2 Flight Safety Testing

**SRD-TEST-005: Flight Test Program Safety**  
The flight test program shall be conducted under a Safety-of-Flight (SOF) process ensuring test team and aircraft safety:

**SOF Process:**
1. **Pre-Flight Test Hazard Analysis:**
   - Identify hazards unique to each test point or test phase
   - Assess risk using MIL-STD-882E risk matrix
   - Define mitigations (flight test techniques, chase aircraft, emergency procedures)

2. **Flight Test Risk Assessment Review:**
   - Conducted before each test phase (hover testing, envelope expansion, systems testing, etc.)
   - Attended by Flight Test Director, Test Pilot, Flight Test Engineers, System Safety Manager, Airworthiness Authority
   - Risk acceptance by Flight Test Director and Airworthiness Authority

3. **Flight Test Cards:**
   - Detailed test procedures for each test point
   - Build-up approach (incremental expansion of flight envelope)
   - Abort criteria (test point discontinued if parameters exceed safe limits)
   - Emergency procedures specific to test condition

4. **Flight Test Instrumentation:**
   - Real-time telemetry monitored by ground-based Flight Test Engineer
   - Exceedance monitoring with automatic alerts (test pilot notified immediately if limit approached)
   - Data recording (1,000+ parameters at 50-100 Hz) for post-flight analysis

5. **Chase Aircraft:**
   - Chase aircraft with experienced test pilot provides visual monitoring during envelope expansion and critical test points
   - Radio communication with test aircraft and Flight Test Director

**Verification:** Inspection (SOF documentation reviewed and approved before each test phase), Demonstration (SOF process audit by independent safety authority)

---

**SRD