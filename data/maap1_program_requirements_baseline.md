# PROGRAM REQUIREMENTS BASELINE
## Eurus Systems MAAP-1 Tandem-Rotor Heavy-Lift Autonomous Helicopter Program

| | |
|---|---|
| **Document No.** | AF-MAAP1-PRB-0001 |
| **Revision** | A (Baseline Release) |
| **Classification** | Eurus Systems Proprietary — Export Controlled (ITAR/EAR Applicable — See Section 9) |
| **Configuration Status** | CONTROLLED — Changes require Program Control Board (PCB) Class I Disposition |
| **Owner** | MAAP-1 Chief Engineer / Program Manager |
| **Applicability** | All MAAP-1 Variants (MAAP-1F, MAAP-1I, MAAP-1C), All IPTs, All Suppliers Tier 1–3 |

---

## 1. PURPOSE AND PRECEDENCE

This Program Requirements Baseline (PRB) is the single authoritative source for MAAP-1 program requirements, performance thresholds, design philosophy, and management strategy. All System Requirements Documents (SRDs), Interface Control Documents (ICDs), Drawing Trees, Bills of Materials (BOMs), Test Plans, and Supplier Statements of Work (SOWs) shall trace directly to this document. In the event of conflict between this PRB and any subordinate document, this PRB governs unless a documented and PCB-approved deviation exists.

This document establishes requirements common to the MAAP-1 baseline airframe and dynamic system, and the variant-specific requirements for the three program variants:

- **MAAP-1F "Wildfire"** — Autonomous Aerial Firefighting Variant
- **MAAP-1I "Sentinel"** — Intelligence, Surveillance, and Reconnaissance (ISR) Variant
- **MAAP-1C "Atlas"** — Cargo/Logistics Variant

All requirements in this document shall be uniquely identified and maintained in the Program Requirements Management Tool (PRMT) with full bidirectional traceability to subordinate specifications.
---

## 2. PROGRAM VISION AND STRATEGIC OBJECTIVES

### 2.1 Vision Statement

Eurus Systems will field the industry's first certifiable, tandem-rotor, heavy-lift **optionally-piloted/autonomous** helicopter family, delivering manned-aircraft-class payload and range performance without a pilot exposed to hazardous mission profiles, at a total cost of ownership at least 30% below comparable manned heavy-lift rotorcraft.

### 2.2 Strategic Objectives (SMART)

| # | Objective | Metric / Target | Rationale |
|---|---|---|---|
| SO-1 | Achieve Type Certification of the baseline MAAP-1C variant | FAA Part 21/29 Type Certificate by Program Month (PM) 84 | Establishes certification basis and de-risks derivative variant certification |
| SO-2 | Field a common airframe supporting 3 mission variants with ≥80% structural part commonality | ≥80% by part count, ≥70% by weight, common through Drawing Tree Level 3 (major assembly) | Reduces NRE, tooling, and sustainment cost; enables mixed-fleet logistics |
| SO-3 | Reduce total cost of ownership (TCO) vs. comparable manned heavy-lift rotorcraft (e.g., CH-47/Mi-26 class benchmark) | ≥30% reduction in $/flight-hour over 20-year life cycle | Program affordability mandate from Eurus Systems Board |
| SO-4 | Demonstrate autonomous mission execution with no onboard pilot for Cargo and ISR variants | ≥95% mission completion rate without human intervention beyond mission-level tasking, in OT&E | Core value proposition: risk reduction and crew cost elimination |
| SO-5 | Achieve Low-Rate Initial Production (LRIP) readiness | PM 66 (LRIP Decision Gate) | Schedule anchor for supply chain and tooling investment |
| SO-6 | Achieve Full-Rate Production (FRP) capacity | 18 aircraft/year sustained by PM 108 | Business case production ramp requirement |
| SO-7 | Limit non-recurring engineering (NRE) cost growth | ≤10% cumulative growth over Milestone B baseline through Critical Design Review (CDR) | Program cost discipline |
| SO-8 | Establish export-compliant baseline configuration | Technology Control Plan approved prior to PDR | Enables international partner and customer engagement without late redesign |

### 2.3 Program Priorities (in order, for trade-space adjudication)

1. **Flight Safety and Airworthiness** (including autonomy safety case)
2. **Mission Performance (KPPs)** as defined in Section 3
3. **Program Schedule** (LRIP/FRP gates)
4. **Life Cycle Cost / Affordability**
5. **Growth Margin and Modularity for future variants**

All formal trade studies shall explicitly assess and document impacts to these priorities against this list and be adjudicated by the Program Control Board.

---

## 3. KEY PERFORMANCE PARAMETERS (KPPs) AND CONSTRAINTS

KPPs apply to the baseline MAAP-1C configuration unless otherwise noted. Variant-specific deltas are captured in Section 5. All Threshold (T) values are contractually binding minimums; Objective (O) values represent design goals to be pursued where they do not compromise Threshold performance, cost, or schedule.

### 3.1 Weight and Payload

| Parameter | Threshold | Objective | Rationale |
|---|---|---|---|
| Maximum Gross Takeoff Weight (MGTOW) | 26,000 lb (11,793 kg) | 28,500 lb (12,928 kg) | Sized to remain within Group III UAS-adjacent heavy-lift class while enabling dual-hook external load ops |
| Basic Empty Weight (BEW), MAAP-1C baseline | ≤14,200 lb | ≤13,600 lb | Drives payload fraction; BEW growth directly erodes useful load — tracked via formal Weight & Balance Control Program |
| Useful Load | ≥11,800 lb | ≥14,900 lb | Derived: MGTOW – BEW |
| Internal Cargo Payload | 8,000 lb | 9,500 lb | Cabin floor and door sized for standard 463L-equivalent pallets (2 positions) |
| External Sling Load (single hook) | 12,000 lb | 16,000 lb | Primary heavy-lift mission driver; tandem-rotor lift efficiency at hover is the core value proposition |
| External Sling Load (dual hook, tandem cargo) | 8,000 lb + 8,000 lb (independent release) | 10,000 lb + 10,000 lb | Enables long-line dual-load logistics and firefighting bucket + retardant tank combinations |
| Cabin Volume | 950 ft³ | 1,100 ft³ | Sized for standard litters (MEDEVAC growth option), pallets, or ISR mission pallets |
| Cabin Door / Ramp Opening | 74 in W x 78 in H (aft ramp) | — | Enables drive-on/drive-off of standard ground support equipment |

### 3.2 Range, Endurance, and Speed

| Parameter | Threshold | Objective | Rationale |
|---|---|---|---|
| Mission Radius at Design External Load (12,000 lb) | 125 nm (250 nm range) | 175 nm (350 nm range) | Defines standoff basing distance from forward operating locations |
| Ferry Range (internal aux tanks, no payload) | 450 nm | 500 nm | Self-deployment without disassembly for CONUS/theater repositioning |
| Endurance (design mission profile) | 4.0 hr | 6.0 hr | ISR loiter and firefighting multi-drop sortie duration |
| Maximum Cruise Speed (Vh, ISA, MGTOW) | 135 KTAS | 150 KTAS | Competitive with manned heavy-lift benchmark; tandem-rotor drag penalty accepted for lift efficiency |
| Never-Exceed Speed (Vne) | 165 KTAS | — | Structural/dynamic component design limit |
| Long-Range Cruise Speed | 120 KTAS | — | Fuel-efficiency optimized cruise for logistics missions |

### 3.3 Hover, Altitude, and Environmental Performance

| Parameter | Threshold | Objective | Rationale |
|---|---|---|---|
| Hover Ceiling OGE, MGTOW, ISA +20°C (95°F Day) | 8,000 ft PA | 10,000 ft PA | "Hot-and-high" firefighting mission driver (Western US wildland fire terrain) |
| Hover Ceiling IGE, MGTOW, ISA +20°C | 10,000 ft PA | 12,000 ft PA | — |
| Service Ceiling | 12,000 ft | 15,000 ft | ISR and mountain rescue/logistics altitude requirement |
| One-Engine-Inoperative (OEI) Hover Capability | Safe landing capability at MGTOW at max approved hover altitude | Continued flight to suitable landing area | Twin-engine redundancy is a program safety mandate (see 3.6) |
| Operating Temperature Range | -32°C to +49°C | -40°C to +52°C | Global operating envelope: arctic logistics to desert/wildfire operations |
| Icing | Non-icing baseline; certified icing kit optional (MAAP-1I, MAAP-1C) | Full FIKI (Flight Into Known Icing) | Cost/weight driver — not baseline to all variants |
| Wind Envelope (autonomous ops, hover/landing) | 25 kt steady, 35 kt gust | 35 kt steady, 45 kt gust | Autonomous GNC control law authority limit; directly bounds automated landing site selection logic |
| Sand/Dust/Brownout Operation | Certified brownout landing capability with degraded visual environment (DVE) sensor suite | — | Autonomous ops in unimproved LZs is a core mission requirement |

### 3.4 Rotor System and Propulsion

| Parameter | Threshold | Objective | Rationale |
|---|---|---|---|
| Configuration | Tandem, overlapping, counter-rotating rotor system | — | Eliminates tail rotor power loss (~10-15% typical), maximizes lift-to-power ratio, superior CG/loading flexibility for cargo variant |
| Rotor Diameter (each) | 42 ft | — | Sized for MGTOW disc loading target ≤ 9.5 lb/ft² combined |
| Hub-to-Hub Spacing | 38 ft (overlap ~9.5%) | — | Balances fuselage length, footprint, and lift efficiency |
| Engines | 2x Turboshaft, FADEC-controlled | — | Twin-engine mandatory for OEI safety case (autonomous, no pilot recovery option) |
| Engine Rating (each, takeoff) | 2,000 shp | 2,200 shp | — |
| Engine Rating (OEI, 2.5 min) | 2,400 shp | — | Sized to sustain safe single-engine hover at threshold hot/high condition |
| Fuel Type | JP-8/Jet A-1 (single fuel policy) | — | Logistics commonality; no avgas dependency |
| Fuel Capacity (internal) | 2,400 lb | 2,800 lb (with aux cells) | Sized to meet range/endurance KPPs at design payload |

### 3.5 Autonomy and Mission Systems

| Parameter | Threshold | Objective | Rationale |
|-----------|-----------|-----------|-----------|
| **Autonomy Level** | **Level 3** (Remotely supervised autonomous operation) for MAAP-1C (Cargo) and MAAP-1I (ISR) variants at IOC.<br><br>**Level 2** (Optionally-piloted) for MAAP-1F (Firefighting) variant at IOC, with a defined incremental path to Level 3. | **Level 4** (Fully autonomous mission execution with human-on-the-loop exception management only) for MAAP-1C and MAAP-1I by FOC.<br><br>**Level 3** for MAAP-1F by FOC. | Level 4 autonomy on a heavy-lift rotorcraft conducting low-altitude, dynamic missions (especially firefighting) presents significant regulatory and technical risk. A phased approach reduces certification risk while still delivering the core value proposition of reduced crew exposure. Firefighting variant retains optional pilot capability longer due to current regulatory constraints on unpiloted low-level operations in the National Airspace System. |
| **Crew Station** | Removable/reconfigurable dual-pilot station (MAAP-1F initial operations only) | Fully de-mountable in <8 labor-hours without special tooling | Supports phased certification approach: optionally-piloted introduction for firefighting, with transition to autonomous-only operations for Cargo and ISR variants. |
| **Detect-and-Avoid (DAA)** | Cooperative + non-cooperative DAA providing equivalent level of safety to manned VFR traffic separation | ASTM F3442 / RTCA DO-365B or successor compliance | Required to enable Beyond Visual Line of Sight (BVLOS) operations and integration into civil and military airspace. |
| **Command & Control (C2) Link** | Dual redundant, encrypted, BLOS-capable via SATCOM + LOS datalink with autonomous lost-link behavior (RTL / loiter / land) | Triple redundant architecture with dynamic link management | Loss of command link is a top-level safety hazard for autonomous operations. Requires robust lost-link contingency logic. |
| **Autonomous GNC Reliability** | Loss of autonomous control function ≤ 1×10⁻⁷ per flight hour (catastrophic hazard category) | ≤ 1×10⁻⁸ per flight hour | Consistent with DO-178C / DO-254 DAL A allocation for flight-critical autonomy functions. Higher reliability target supports reduced crew complement and eventual zero-pilot operations. |

### 3.6 Reliability, Maintainability, and Life

| Parameter | Threshold | Objective | Rationale |
|---|---|---|---|
| Mean Time Between Mission Abort (MTBMA) | 500 flight hours | 750 flight hours | Operational availability driver |
| Mean Time Between Failure — Flight Critical Systems | 5,000 flight hours | 10,000 flight hours | Autonomy removes pilot in-flight troubleshooting capability, raising reliability bar vs. manned equivalents |
| Airframe Design Service Life | 20,000 flight hours / 30 years | 25,000 flight hours | Life-cycle cost driver; sized to dynamic component overhaul intervals |
| Scheduled Maintenance Man-Hours per Flight Hour (MMH/FH) | ≤4.5 | ≤3.5 | Affordability KPP; modular LRU design directly supports this target |
| Mean Time To Repair (MTTR), Line Replaceable Unit | ≤45 min (95th percentile LRUs) | ≤30 min | Sortie generation rate requirement |
| Corrosion Protection / Environmental Durability | MIL-STD-810H compliant, Class 2 corrosion environment (coastal/maritime) | — | Firefighting and ISR basing in austere/coastal environments |

### 3.7 Program-Level Constraints

| Constraint | Description |
|---|---|
| C-1 | Program shall not exceed $21.5M (FY25$) per aircraft at FRP (Lot 5 pricing) |
| C-2 | Aircraft shall be transportable via C-17 (2 aircraft, blades/pylons removed) without irreversible structural modification |
| C-3 | No single-point failure shall result in loss of aircraft in autonomous (no-pilot) configuration |
| C-4 | Baseline design shall not require export license modification for NATO/Five-Eyes sales (see Section 9) |
| C-5 | All flight-critical software shall be developed to DO-178C DAL A/B as allocated by the System Safety Assessment |
| C-6 | Program shall retain minimum 15% weight growth margin at PDR, decreasing per standard weight growth curve to 3% at CDR |

---

## 4. SYSTEM OVERVIEW

The MAAP-1 is a twin-turboshaft, tandem-rotor, heavy-lift rotorcraft employing a common structural and dynamic system baseline ("Green Aircraft") with variant-unique mission equipment packages installed at defined interface planes. The Green Aircraft comprises:

- Forward and aft rotor pylons, transmissions, and interconnect drive shaft
- Composite primary structure (fuselage, tailcone, sponsons)
- Twin-engine propulsion system with FADEC and common engine nacelles
- Fly-by-wire flight control system (triplex primary, autonomous GNC computer)
- Common landing gear (fixed tricycle, crashworthy)
- Common electrical power generation and distribution architecture
- Common core avionics bus (open-architecture, MOSA-compliant) supporting variant-specific mission system integration via defined ICDs

Variant differentiation is confined, to the maximum extent practicable, to mission bay equipment, external hardpoints, and software mission applications, in accordance with the modularity strategy in Section 6.

---

## 5. VARIANT DIFFERENTIATION

### 5.1 Common Baseline ("Green Aircraft") Boundary

The following systems are **common across all three variants** and shall be developed, qualified, and produced as a single configuration item set:

- Airframe primary structure (Drawing Tree Level 2: Forward Fuselage, Aft Fuselage, Tailcone, Sponsons)
- Rotor system, transmissions, drive train, rotor blades
- Engines, engine controls, fuel system (core)
- Landing gear
- Primary/backup electrical power generation
- Flight control system (actuators, primary flight computers)
- Autonomous GNC core
- Common core avionics bus, mission computers (hardware), and cockpit/crew station display architecture (display formats/software applications are variant-unique per Section 5.2)
- Environmental control system (core distribution; variant-unique heat loads addressed via auxiliary conditioning packages)
- Crashworthy fuel system and crew seating (baseline energy attenuation architecture)
- Vehicle health management system (core sensors and data bus architecture)

Any proposed deviation from common configuration status for the above systems shall require a waiver approved by the Chief Engineer and the Program Executive Officer, with an associated impact assessment addressing cost, schedule, and logistics footprint across all three variants.

### 5.2 Variant-Unique Systems

| System | MAAP-1F (Firefighting) | MAAP-1I (ISR) | MAAP-1C (Cargo) |
|---|---|---|---|
| Mission bay configuration | Troop seating (24 combat-equipped), gunner stations (2x) | Litter racks (6 ambulatory + 6 litter), medical console | Cargo rail/roller system, palletized load capability |
| External hardpoints | 4x hardpoints, weapons-capable (gun pods, rocket pods) | 2x hardpoints, non-weapons (auxiliary fuel only) | 2x hardpoints, cargo hook rated to [TBD — CBD-0014] lbs |
| Defensive systems suite | Full DAS (missile warning, laser warning, countermeasures dispensers) | Missile warning only (no dispensers) | Missile warning only (no dispensers) |
| Armor package | Crew + troop compartment ballistic protection (Level per SSD-0009) | Crew compartment only | Crew compartment only |
| Mission software applications | Terrain following/terrain avoidance, weapons employment, formation autonomy | Patient monitoring interface, medical equipment power management | Load planning, external load stability augmentation, precision sling release |
| Rescue hoist | Not standard (kit-installable) | Standard, dual hoist (600 lb rated each) | Not applicable |
| Auxiliary fuel provisions | Internal auxiliary tank (mission kit) | Internal auxiliary tank (standard) | External tank provisions only |

Variant-unique systems shall interface with the Green Aircraft solely through the interface control documents identified in Section 5.3. No variant-unique system shall require modification to Green Aircraft structural load paths, primary wiring architecture, or flight control system software beyond parameter-table changes managed under configuration control.

### 5.3 Interface Control Documentation

The following Interface Control Documents (ICDs) shall govern the boundary between the Green Aircraft and variant-unique mission equipment packages. ICDs shall be baselined no later than PDR and placed under formal configuration control at CDR.

| ICD Number | Interface Description | Controlling Authority |
|---|---|---|
| ICD-001 | Mission bay structural attachment (floor rails, hardpoint fittings) | Chief Engineer, Structures IPT |
| ICD-002 | Electrical power interface (mission bus, load shedding priority) | Chief Engineer, Electrical IPT |
| ICD-003 | Core avionics bus / mission system data interface (MOSA-compliant) | Chief Engineer, Avionics IPT |
| ICD-004 | External hardpoint mechanical/electrical interface | Chief Engineer, Weapons/Stores IPT |
| ICD-005 | Environmental control system auxiliary tie-in | Chief Engineer, Subsystems IPT |
| ICD-006 | Crew/mission station display and control interface | Chief Engineer, Human Systems Integration IPT |

Changes to any baselined ICD shall be processed through the Program Configuration Control Board (CCB) in accordance with the Configuration Management Plan (CM-0001) and shall include an assessment of impact to all three variants, regardless of the variant originating the change request.

This Program Requirements Baseline establishes the authoritative foundation for all engineering, manufacturing, and sustainment activities. All subsequent program documentation shall maintain traceability to the requirements herein.

---

## 6. MODULARITY AND OPEN SYSTEMS STRATEGY

### 6.1 Modular Open Systems Approach (MOSA) Requirements

| Req ID | Requirement |
|---|---|
| MOSA-1 | Core avionics architecture shall employ open, non-proprietary standards for hardware (e.g., VITA 65/OpenVPX or successor) and software (FACE Technical Standard, current edition per DoDI 5000.87) |
| MOSA-2 | Mission system software applications shall be portable across variants without recompilation against variant-specific hardware, to the maximum extent practicable |
| MOSA-3 | The Government shall retain unlimited rights to all interface specifications defined in Section 5.3 ICDs |
| MOSA-4 | No single-source, proprietary data bus shall be employed for safety-critical or mission-critical data exchange without Government-owned interface specification |
| MOSA-5 | Mission kit installation/removal (Section 5.2 kit-installable items) shall not exceed 8 maintainer-hours at organizational-level maintenance, per kit |

### 6.2 Rationale

The modularity strategy is intended to minimize total ownership cost across the three-variant fleet by maximizing part commonality, enabling competitive re-procurement of mission systems over the program's service life, and reducing the qualification burden associated with variant-specific changes. The Program Office estimates that sustained commonality above 80% by recurring flyaway cost (Green Aircraft as a percentage of total aircraft cost) is achievable based on the variant differentiation boundary defined in Section 5.1–5.2; this figure shall be tracked as a program metric (see Section 11, Program Metrics) and reported at each Program Management Review.

---

## 7. KEY PERFORMANCE PARAMETERS (KPPs) AND KEY SYSTEM ATTRIBUTES (KSAs)

### 7.1 Key Performance Parameters

The following KPPs are derived from the validated Capability Development Document (CDD-MAAP-1, Rev [TBD]) and constitute threshold/objective requirements that shall not be altered without Joint Requirements Oversight Council (JROC) or equivalent validation authority approval.

| KPP ID | Title | Threshold | Objective |
|---|---|---|---|
| KPP-01 | Combat Radius (Assault variant, standard mission profile) | 250 NM | 325 NM |
| KPP-02 | Useful Load (internal, sea level standard day) | 6,000 lb | 8,500 lb |
| KPP-03 | External Load Capability (single hook, per Section 3.x sling load requirement) | 10,000 lb | 12,000 lb |
| KPP-04 | Cruise Speed (maximum continuous power, standard day, sea level) | 165 KTAS | 185 KTAS |
| KPP-05 | Survivability (aggregate, per classified annex ANX-0003) | Threshold per ANX-0003 | Objective per ANX-0003 |
| KPP-06 | Net-Ready (data interoperability per Section 8) | Compliant with mandated Net-Centric Data Strategy elements | Full interoperability across joint C2 architecture |
| KPP-07 | Autonomous Operation | Reduced-crew (1 pilot + autonomy) certified for MEDEVAC and Cargo variants | Fully autonomous (zero-pilot) certified for Cargo variant, permissive airspace |

KPP failure at Threshold value during any formal test event (DT or OT) shall trigger an immediate program deviation report to the Milestone Decision Authority in accordance with the Test and Evaluation Master Plan (TEMP-0001).

### 7.2 Key System Attributes

| KSA ID | Title | Threshold | Objective |
|---|---|---|---|
| KSA-01 | Reliability (Mean Time Between System Abort) | 25 flight hours | 40 flight hours |
| KSA-02 | Maintainability (Maintenance Man-Hours per Flight Hour, Green Aircraft) | 4.5 MMH/FH | 3.0 MMH/FH |
| KSA-03 | Sustainment Footprint (deployable support package, 4-aircraft detachment) | ≤ 12 C-17 equivalent loads | ≤ 8 C-17 equivalent loads |
| KSA-04 | Training Device Fidelity | Level 6 (per training system requirements ANX-0007) | Level 7 |
| KSA-05 | Cybersecurity (Risk Management Framework compliance) | Authorization to Operate at IOC | Continuous ATO (cATO) |

---

## 8. INTEROPERABILITY AND NET-READY REQUIREMENTS

### 8.1 General

The MAAP-1 system shall be designed to operate as a node within the Joint All-Domain Command and Control (JADC2) architecture and shall comply with the Net-Centric Data Strategy and applicable Data Sharing/Interoperability requirements identified in the Information Support Plan (ISP-0001).

### 8.2 Interoperability Requirements

| Req ID | Requirement |
|---|---|
| INT-1 | System shall exchange Link 16 and/or successor tactical data link messages as defined in ISP-0001, Table 4 |
| INT-2 | System shall be capable of receiving and displaying a Common Operating Picture (COP) feed compliant with the Joint Track Management standard in effect at CDR |
| INT-3 | Autonomous GNC core shall accept mission tasking via a Government-standard interface compliant with the UAS Control Segment (UCS) Architecture, as adapted for optionally-piloted operation |
| INT-4 | Voice and data communications suite shall be interoperable with joint/coalition tactical radios identified in the Communications Interoperability Annex (ANX-0011) |
| INT-5 | Identification Friend or Foe (IFF) shall comply with Mode 5/Mode S mandates in effect at time of Milestone C |

### 8.3 Coalition Interoperability

Given the anticipated Foreign Military Sales interest identified in Section 9, the core avionics architecture and data link suite shall be designed, to the maximum extent practicable, to accommodate NATO STANAG-compliant equivalents (e.g., Link 22, STANAG 4586 for UCS-equivalent tasking) without requiring redesign of the common avionics bus architecture defined in Section 6.

---

## 9. EXPORT CONTROL AND INTERNATIONAL PARTICIPATION

### 9.1 Baseline Design Intent

The Program Office has established, as a program constraint (C-4), that the Green Aircraft baseline design shall not incorporate technology that would require an export license modification for sales to NATO member nations and Five-Eyes partners (Australia, Canada, New Zealand, United Kingdom, United States), beyond standard Foreign Military Sales (FMS) case processing.

### 9.2 Requirements

| Req ID | Requirement |
|---|---|
| EXP-1 | Autonomous GNC core software shall be architected such that fully autonomous (zero-pilot) functionality can be disabled or removed via a defined software/hardware partition for export configurations, without affecting Green Aircraft airworthiness certification basis |
| EXP-2 | Defensive systems suite (Section 5.2) shall utilize a modular, removable architecture to accommodate country-specific releasability determinations |
| EXP-3 | Technical data packages shall be developed with a segregated architecture distinguishing ITAR-controlled content from content eligible for release under the applicable Technology Security and Foreign Disclosure (TSFD) determination |
| EXP-4 | Program Office shall maintain a current Technology Assessment/Control Plan (TA/CP) and update it at each major milestone review |

### 9.3 International Partner Participation

No international co-development partners are baselined as of this document's approval date. Should international partnership be pursued, all cost, schedule, and technical baseline impacts shall be processed as formal changes to this Program Requirements Baseline through the CCB, with corresponding updates to the Acquisition Strategy and applicable international agreements (e.g., MOU/MOA).

---

## 10. VERIFICATION AND VALIDATION APPROACH

### 10.1 Verification Methods

All requirements contained in this baseline shall be assigned a verification method in the Requirements Verification Traceability Matrix (RVTM-0001), using one or more of the following methods:

- **Analysis (A):** Verification via engineering analysis, modeling, or simulation
- **Demonstration (D):** Verification via operation of the system or a representative article, without instrumented data collection
- **Inspection (I):** Verification via visual examination, review of design documentation, or physical measurement
- **Test (T):** Verification via instrumented data collection during ground or flight test

### 10.2 Verification Responsibility

| Phase | Verification Activity | Responsible Entity |
|---|---|---|
| PDR–CDR | Requirements allocation and analysis-based closure of derived requirements | Chief Engineer / IPT Leads |
| CDR–First Flight | Component and subsystem qualification testing | Prime Contractor, Government-witnessed |
| First Flight–IOT&E | Developmental Test (DT), including airworthiness release process | Government DT Organization / Prime Contractor (combined test team) |
| IOT&E | Operational Test (OT), independent operational assessment | Operational Test Agency (independent of acquisition chain) |
| Post-IOC | Follow-on Test and Evaluation (FOT&E), as required | Operational Test Agency |

Full verification closure for all KPPs/KSAs shall be achieved prior to the Full-Rate Production decision. Closure status shall be reported at each Program Management Review via the RVTM and shall identify any requirement verified solely by Analysis where Test was originally planned, with rationale and Chief Engineer concurrence.

### 10.3 Modeling and Simulation

Use of Modeling and Simulation (M&S) in lieu of physical test for KPP/KSA closure shall require accreditation of the M&S tool or environment by the Program's designated Verification, Validation, and Accreditation (VV&A) authority, documented in the M&S Management Plan (MSMP-0001), prior to use for formal closure.

---

## 11. PROGRAM METRICS

The following metrics shall be tracked and reported at each Program Management Review (PMR) throughout the Engineering and Manufacturing Development (EMD) and Production phases:

| Metric | Description | Reporting Source |
|---|---|---|
| Weight growth margin | Actual vs. allocated margin per C-6 curve | Chief Engineer, Weights IPT |
| Green Aircraft commonality (% recurring flyaway cost) | Tracked against 80% target in Section 6.2 | Program Cost Analyst |
| Requirements closure (RVTM) | Percentage of requirements verified, by method | Systems Engineering IPT |
| Software DAL compliance | Percentage of flight-critical software lines of code under DO-178C DAL A/B process discipline | Software IPT Lead |
| KPP/KSA risk status | Threshold/Objective risk rating (Red/Yellow/Green) | Chief Engineer |
| Cybersecurity RMF status | Number of open Category I/II findings | Program Protection Lead |
| Schedule performance index (SPI) / Cost performance index (CPI) | Earned value metrics per EVMS | Program Control |

Any metric trending Red for two consecutive PMR cycles shall require a formal corrective action plan presented to the Program Manager, with escalation to the Milestone Decision Authority if unresolved after the subsequent cycle.

---

## 12. BASELINE CHANGE CONTROL

### 12.1 Configuration Control Board Authority

This Program Requirements Baseline is placed under formal configuration control effective upon signature (Section 1). All changes to requirements contained herein — including KPPs, KSAs, constraints, and the variant differentiation boundary of Section 5 — shall be processed exclusively through the Program CCB, chaired by the Program Manager with the Chief Engineer as technical authority.

### 12.2 Change Classification

| Class | Description | Approval Authority |
|---|---|---|
| Class I | Change affecting a KPP, KSA, cost or schedule baseline, or the Section 5.1 common configuration boundary | Milestone Decision Authority (KPP/KSA); Program Manager with MDA notification (cost/schedule) |
| Class II | Change affecting a derived requirement, ICD, or non-KPP/KSA performance parameter, with no cost/schedule baseline impact | Program CCB (Program Manager chair) |
| Class III | Administrative/editorial correction with no technical, cost, or schedule impact | Chief Engineer or designee |

### 12.3 Traceability

All approved changes shall be reflected in a revised version of this document, with a change log appended as Appendix A, and shall be propagated to the RVTM-0001, applicable ICDs, and the Systems Engineering Management Plan (SEMP-0001) within 30 calendar days of CCB approval.

---

## 13. APPLICABLE AND REFERENCE DOCUMENTS

| Document Number | Title |
|---|---|
| CDD-MAAP-1 | Capability Development Document, MAAP-1 |
| CBD-0002 | Program Cost Baseline Document |
| CBD-0014 | Sling Load Performance Specification |
| SSD-0009 | Survivability and Ballistic Protection Specification |
| CM-0001 | Configuration Management Plan |
| TEMP-0001 | Test and Evaluation Master Plan |
| ISP-0001 | Information Support Plan |
| ANX-0003 | Survivability Requirements (Classified Annex) |
| ANX-0007 | Training System Requirements Annex |
| ANX-0011 | Communications Interoperability Annex |
| RVTM-0001 | Requirements Verification Traceability Matrix |
| MSMP-0001 | Modeling and Simulation Management Plan |
| SEMP-0001 | Systems Engineering Management Plan |
| DoDI 5000.87 | Operation of the Software Acquisition Pathway |
| DO-178C | Software Considerations in Airborne Systems and Equipment Certification |

---

## APPENDIX A — CHANGE LOG

| Rev | Date | Description | CCB Reference | Approval Authority |
|---|---|---|---|---|
| — | [Baseline Date] | Initial baseline release | N/A | Program Manager / Chief Engineer |

*End of Program Requirements Baseline Document.*