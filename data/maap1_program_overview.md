# PROGRAM OVERVIEW DOCUMENT
## AetherForge MAAP-1 Tandem-Rotor Heavy-Lift Autonomous Helicopter Program

| | |
|---|---|
| **Document No.** | AF-MAAP1-POV-0003 |
| **Revision** | A (Initial Release) |
| **Classification** | Eurus Systems Proprietary |
| **Date** | [Current Date] |
| **Prepared By** | MAAP-1 Program Office |
| **Approved By** | Program Manager, MAAP-1 |

---

## EXECUTIVE SUMMARY

The **AetherForge MAAP-1** represents a transformative capability in heavy-lift rotorcraft aviation: the world's first certifiable tandem-rotor autonomous helicopter designed to deliver manned-aircraft-class payload and performance without exposing aircrew to high-risk mission environments. Developed by Eurus Systems, the MAAP-1 combines the proven efficiency of tandem-rotor design with state-of-the-art autonomous systems, creating a multi-role platform that excels in firefighting, intelligence/surveillance/reconnaissance (ISR), and cargo/logistics operations.

With a 12,000 lb external lift capability, 250+ nautical mile mission radius, and the ability to operate in extreme environmental conditions from -32°C Arctic cold to +49°C wildfire heat, the MAAP-1 addresses critical capability gaps across civilian emergency response, commercial logistics, and defense applications. The program's modular "Green Aircraft" architecture ensures over 80% commonality across three mission variants, dramatically reducing total ownership costs while enabling rapid mission reconfiguration.

The MAAP-1 is currently in Engineering and Manufacturing Development (EMD), progressing toward first flight in Program Month 54 and FAA Type Certification in Program Month 84. This document provides stakeholders with a comprehensive overview of the program's strategic vision, technical capabilities, development status, and the transformational value the AetherForge MAAP-1 brings to the heavy-lift helicopter market.

---

## 1. PROGRAM VISION AND STRATEGIC PURPOSE

### 1.1 The Challenge

Global demand for heavy-lift rotorcraft continues to grow across diverse mission areas—from combating increasingly severe wildland fires to delivering humanitarian relief in disaster zones to supporting remote industrial operations. Yet conventional manned heavy-lift helicopters face persistent challenges:

- **Crew Safety Risk**: Pilots face extreme danger in low-altitude firefighting, disaster relief, and combat logistics missions
- **Operating Costs**: Dual-crew requirements, extensive training pipelines, and complex maintenance drive costs to $8,000-12,000 per flight hour
- **Limited Availability**: Pilot shortages and crew duty-day limitations constrain operational tempo
- **Mission Adaptability**: Traditional platforms require extensive modifications to transition between mission sets

These challenges demand a fundamentally new approach—one that preserves the proven performance of tandem-rotor design while leveraging autonomous technology to enhance safety, reduce costs, and expand operational flexibility.

### 1.2 The Vision

**Eurus Systems will field the industry's first certifiable, tandem-rotor, heavy-lift optionally-piloted/autonomous helicopter family, delivering manned-aircraft-class payload and range performance without exposing pilots to hazardous mission profiles, at a total cost of ownership at least 30% below comparable manned heavy-lift rotorcraft.**

This vision rests on four strategic pillars:

1. **Safety Through Autonomy**: Remove human crews from high-risk missions while maintaining equivalent safety levels through redundant autonomous systems
2. **Operational Efficiency**: Reduce cost per flight hour by 30%+ through elimination of second crew member, reduced training requirements, and modular maintenance design
3. **Mission Flexibility**: Deploy a single common airframe across firefighting, ISR, and cargo missions with rapid reconfiguration (less than 8 labor-hours)
4. **Certification Pathways**: Achieve FAA Type Certification for the baseline cargo variant, establishing regulatory framework for autonomous heavy-lift operations

### 1.3 Strategic Importance

The MAAP-1 addresses critical capability gaps identified by key stakeholder communities:

**Wildland Fire Management**
- Annual U.S. wildfire costs exceed $4 billion; demand for aerial firefighting assets outstrips supply during peak fire season
- MAAP-1's autonomous 2,000-gallon water/retardant delivery capability enables 24/7 operations without crew fatigue constraints
- Operates safely at 8,000+ ft density altitude in hot, smoky conditions where manned helicopter performance degrades

**Emergency Medical Services & Disaster Response**
- Delivers 6 litter + 6 ambulatory patient capacity with autonomous flight to austere landing zones
- Eliminates pilot exposure to hazardous weather and degraded visual environments during emergency response
- Rapid reconfiguration supports transition from medical evacuation to cargo delivery within hours

**Commercial & Defense Logistics**
- 12,000 lb external lift capability with 250 nm mission radius enables long-range heavy cargo delivery
- Dual-hook tandem configuration optimizes load stability and enables complex cargo combinations
- Autonomous operations reduce logistics footprint: one ground control station supports up to 4 aircraft

**Intelligence & Surveillance Operations**
- 6-hour endurance with stabilized EO/IR sensor suite provides persistent ISR capability
- Autonomous operation enables over-the-horizon missions without line-of-sight crew constraints
- Reduced acoustic signature (95 dBA vs. 105+ dBA for conventional heavy-lift helicopters) supports covert surveillance

---

## 2. SYSTEM OVERVIEW

### 2.1 Configuration and Design Philosophy

The MAAP-1 employs a **tandem, counter-rotating rotor configuration**—a design proven over six decades to deliver superior lifting efficiency compared to conventional single-rotor helicopters. This configuration choice yields decisive advantages:

**Lift Efficiency Without Compromise**
- Eliminates tail rotor power loss (typically 10-15% of total engine power), directing all available power to lift generation
- 42-foot diameter rotors (9.5% overlap) generate 2,770 ft² of total disc area
- Disc loading of only 9.39 lb/ft² at maximum gross weight enables superior hover performance

**Exceptional Load Handling**
- Longitudinal center-of-gravity range of 10.5% Mean Aerodynamic Chord (versus ~3% for conventional helicopters) accommodates widely varying cargo distributions
- Dual cargo hooks separated by 28 feet enable tandem external loads (8,000 + 8,000 lb configuration) with enhanced stability
- Automatic ballast system maintains optimal CG position across all loading scenarios

**Operational Robustness**
- Twin turboshaft engines (2,000 shp each, 2,400 shp One-Engine-Inoperative emergency rating) ensure safe single-engine landing capability at maximum gross weight
- Fixed tricycle landing gear with crashworthy design (30 ft/s vertical, 40 ft/s horizontal impact survivability) eliminates hydraulic gear failure modes
- Composite primary structure delivers corrosion resistance and damage tolerance for austere environment operations

### 2.2 Physical Characteristics

| **Dimension** | **Specification** |
|---|---|
| Overall Length (rotors turning) | 80.0 ft (24.4 m) |
| Rotor Diameter (each) | 42.0 ft (12.8 m) |
| Overall Height | 18.5 ft (5.6 m) |
| Cabin Volume | 950-1,100 ft³ |
| Cabin Door Opening | 74 in W × 78 in H (drive-on/drive-off capable) |
| Empty Weight | 14,200 lb (target) |
| Maximum Takeoff Weight | 26,000 lb (threshold) / 28,500 lb (objective) |

**Transportability**: Two complete aircraft fit in a single C-17 cargo aircraft with rotors/pylons removed (4-hour disassembly per aircraft), enabling rapid global deployment.

### 2.3 Autonomous Systems Architecture

The MAAP-1's autonomy represents the program's most significant innovation—integrating mature autonomous flight technologies with newly developed mission-specific capabilities to enable safe, reliable operations without onboard pilots.

**Core Autonomous Capabilities**

*Flight Management*
- Triplex digital fly-by-wire flight control system (no mechanical backup—full authority digital control)
- Dual-redundant autonomous Guidance, Navigation & Control (GNC) computers with hot-standby automatic failover (<100 ms switchover)
- 100 Hz primary flight control update rate ensures stability in turbulent conditions and during external load operations

*Navigation & Positioning*
- Triple-redundant GPS receivers (dual-frequency, SAASM/GNSS capable)
- Dual-redundant fiber-optic gyro Inertial Navigation Systems (INS) with <0.5 nm/hr drift
- Tightly-coupled GPS/INS integration with vision-based Terrain-Relative Navigation (TRN) for GPS-denied operations
- Navigation accuracy: ±5 m CEP (95%) with GPS nominal; ±50 m CEP after 15 min GPS-denied operation

*Detect and Avoid (DAA)*
- Cooperative detection via ADS-B In and TCAS II (optional)
- Non-cooperative detection via 360° X-band RADAR (3-5 nm detection range)
- 50-100 simultaneous target tracking capability with automatic threat prioritization
- Autonomous collision avoidance maneuvers within ±30° bank / ±500 fpm vertical limits

*Command & Control*
- Primary C-band line-of-sight datalink (10 Mbps down / 2 Mbps up, 150 nm range)
- Backup L-band datalink (2 Mbps bidirectional, 100 nm range)
- Beyond-line-of-sight Ku/Ka-band SATCOM (5 Mbps down / 1 Mbps up, global coverage)
- Autonomous lost-link behavior: 30-second loiter → 120-second expanded search → Return-to-Launch or Land-at-Nearest-Suitable-Site

**Autonomy Levels by Variant**

| **Variant** | **Initial Capability (IOC)** | **Full Capability (FOC)** |
|---|---|---|
| MAAP-1C (Cargo) | Level 3: Remotely supervised autonomous operation | Level 4: Fully autonomous mission execution |
| MAAP-1I (ISR) | Level 3: Remotely supervised autonomous operation | Level 4: Fully autonomous mission execution |
| MAAP-1F (Firefighting) | Level 2: Optionally-piloted with autonomous assist | Level 3: Remotely supervised autonomous operation |

This phased approach balances rapid capability delivery with regulatory risk management, particularly for firefighting operations where current FAA regulations require more extensive piloted flight test demonstration.

### 2.4 Ground Control Station

MAAP-1 operations are managed through a transportable or vehicle-mounted Ground Control Station (GCS) featuring:

- **Three operator stations**: Pilot, Mission Payload Operator, Mission Commander
- **Multi-function color displays**: Sunlight-readable (1,000+ nit brightness), touch-capable
- **Control modes**: Mission-level tasking / Supervisory control / Direct pilot control (emergency override)
- **Low latency**: ≤200 ms command-to-aircraft via line-of-sight datalink, ≤500 ms via SATCOM
- **Multi-aircraft capability**: Single GCS can simultaneously control up to 4 aircraft (objective)

The GCS architecture follows a "human-on-the-loop" philosophy: the autonomous system executes mission plans independently while operators monitor progress, update objectives, and intervene only when necessary. This approach maximizes operational efficiency while preserving human judgment for complex tactical decisions.

---

## 3. KEY CAPABILITIES

### 3.1 Heavy-Lift Performance

The MAAP-1 delivers exceptional lifting capability across a wide operational envelope:

**External Load Performance**
- **Single-hook capability**: 12,000 lb (threshold) / 16,000 lb (objective)
- **Dual-hook tandem loads**: 8,000 + 8,000 lb independently releasable (threshold) / 10,000 + 10,000 lb (objective)
- **Hook separation**: 28 feet fore/aft for optimal load stability
- **Sling length**: Up to 120-150 ft for long-line operations
- **Emergency release**: <0.5 second electrically actuated release for all load conditions

**Internal Cargo Capacity**
- **Cabin payload**: 8,000 lb (threshold) / 9,500 lb (objective)
- **Floor loading**: 150 lb/ft² uniform distributed load limit
- **Pallet positions**: 2× 463L-equivalent pallets (88" × 108")
- **Cargo system**: Rail/roller system with 24 tie-down points (5,000 lb rated each)
- **Access**: 74" × 78" aft ramp enables drive-on/drive-off loading of standard ground support equipment

**Hover Performance in Demanding Conditions**
- **Out-of-ground-effect (OGE) hover ceiling**: 8,000 ft pressure altitude at maximum gross weight, ISA +20°C (95°F)
- **In-ground-effect (IGE) hover ceiling**: 10,000 ft pressure altitude at MGTOW, ISA +20°C
- **Design driver**: Western U.S. wildland fire operations in mountainous terrain during summer heat

This hover performance—validated through rigorous engineering analysis and to be demonstrated in flight test—enables MAAP-1 to operate effectively in "hot-and-high" conditions that severely degrade or ground competing platforms.

### 3.2 Range and Endurance

**Mission Radius with Heavy External Load**
- **Design mission (12,000 lb external)**: 125 nm radius (250 nm total range) threshold / 175 nm radius (350 nm range) objective
- **Mission profile**: Includes 30-minute fuel reserve, 10-minute loiter at destination
- **Reduced payload (8,000 lb)**: 160-210 nm mission radius

**Ferry Range (Self-Deployment)**
- **Internal fuel only**: 450-500 nm
- **With auxiliary fuel tanks**: 580-650 nm
- **Enables**: CONUS-wide repositioning without disassembly; theater deployment from sea-based logistics hubs

**Endurance for Loiter-Intensive Missions**
- **Design endurance**: 4.0 hours (threshold) / 6.0 hours (objective)
- **ISR mission profile**: 4.5-5.8 hours with 4,000 lb mission equipment payload
- **Firefighting multi-drop**: 3.5-4.5 hours including 6-8 water drops and transit
- **Best-endurance loiter**: 5.2-7.0 hours with no payload and auxiliary fuel

### 3.3 Speed Performance

- **Maximum cruise speed**: 135 KTAS (threshold) / 150 KTAS (objective)
- **Long-range cruise**: 120 KTAS (optimized for fuel efficiency)
- **Never-exceed speed (VNE)**: 165 KTAS
- **Best rate-of-climb speed**: 65 KIAS

While tandem-rotor helicopters sacrifice some top speed compared to conventional configurations (due to aerodynamic interference between rotors), the MAAP-1's cruise performance remains competitive with manned heavy-lift benchmarks while delivering superior hover efficiency—the critical metric for cargo delivery and firefighting missions.

### 3.4 Environmental Operating Envelope

The MAAP-1 is engineered for all-weather, global operations:

**Temperature Range**
- **Operating**: -32°C to +49°C (threshold) / -40°C to +52°C (objective)
- **Enables**: Arctic logistics operations to extreme desert/wildfire environments
- **Cold-weather provisions**: Engine and transmission preheat systems, optional rotor blade deicing

**Atmospheric Conditions**
- **Service ceiling**: 12,000-15,000 ft pressure altitude
- **Maximum demonstrated crosswind**: 35 kt steady (40 kt with pilot override)
- **Autonomous landing wind limits**: 25 kt steady / 35 kt gust (conservative envelope for unmanned operations)
- **All-weather certification**: Certified for flight in rain, blowing sand/dust, brownout landing conditions

**Unique Capability: Degraded Visual Environment (DVE) Operations**

The MAAP-1's autonomous sensor suite enables safe landing operations in conditions that would challenge or ground manned helicopters:
- Forward-looking infrared (FLIR) and millimeter-wave RADAR penetrate smoke, dust, and fog
- Terrain-relative navigation provides precise positioning when GPS is degraded
- Automatic landing site selection evaluates slope, obstacles, and surface hardness
- Brownout landing capability demonstrated in desert testing

This DVE capability is particularly critical for firefighting (landing in heavy smoke) and disaster response (operating in dust/debris from collapsed structures).

### 3.5 Modular Mission Systems: One Aircraft, Multiple Missions

A core MAAP-1 program tenet is **mission flexibility through modularity**. Rather than developing separate aircraft for each mission area, Eurus Systems designed a common "Green Aircraft" baseline with variant-specific mission equipment that installs through strictly controlled interfaces.

**Commonality Achievements**
- **≥80% structural part commonality** (by part count) across all three variants
- **≥70% weight commonality** (common through major assembly level)
- **Single type certificate** for the Green Aircraft, with variant-specific Supplemental Type Certificates (STCs) or amendments

**Rapid Mission Reconfiguration**
- Mission bay equipment installs/removes in **≤8 labor-hours** at organizational-level maintenance
- Standard interface control documents govern mechanical, electrical, and data connections
- No Green Aircraft structural modifications required for any baseline variant configuration

This modular approach yields decisive advantages:
- **Logistics efficiency**: Single spare parts inventory supports mixed fleets
- **Operational flexibility**: Aircraft transition between missions as operational needs shift
- **Technology insertion**: New mission systems integrate without redesigning the airframe
- **Cost reduction**: Development and production economies of scale across variants

---

## 4. MISSION VARIANTS

### 4.1 MAAP-1F "Wildfire" – Autonomous Firefighting Variant

**Mission**: Aerial delivery of water and fire retardant for wildland fire suppression

**Unique Capabilities**

*Internal Tank System*
- 2,000-gallon (7,570 L) belly-mounted water/retardant tank
- Snorkel hover-fill capability from natural water sources (lakes, rivers, portable tanks)
- Programmable salvo or ripple release with GPS-guided drop corridor
- Fill time: ~45 seconds from 10-foot hover over water source

*External Load Firefighting*
- Compatible with standard firefighting buckets (Bambi Bucket, etc.) up to 2,600-gallon capacity
- Dual-hook configuration enables bucket + auxiliary tank for extended-duration operations
- Automatic load stability augmentation compensates for water slosh during flight

*Fire Mission Systems*
- Forward-looking infrared (FLIR) with automatic hotspot detection and mapping
- Real-time fire perimeter tracking with automatic GCS overlay
- Smoke-penetrating sensors enable operations in zero-visibility conditions
- Autonomous drop point calculation accounts for wind, aircraft speed, and terrain

*Crew Configuration*
- **Initial Operational Capability (IOC)**: Optionally-piloted with removable dual-pilot station
- **Rationale**: Current FAA regulations require piloted demonstration for low-altitude external load operations over populated areas
- **Full Operational Capability (FOC)**: Transition to Level 3 autonomy (remotely supervised) as regulatory pathways mature

**Operational Concept**

1. **Forward-deploy** to incident base camp or remote airstrip near fire
2. **Mission tasking** via GCS: fire perimeter coordinates, drop zones, RTB/refill location
3. **Autonomous execution**: Fill → transit to fire → drop → return → repeat
4. **Sustained operations**: 3.5-4.5 hour sorties enable 6-8 drops per cycle; multiple aircraft provide continuous coverage
5. **Night operations**: FLIR and autonomous landing capability enable 24/7 operations without crew fatigue constraints

**Impact on Wildfire Management**

- **Cost reduction**: Estimated 40% lower cost per gallon delivered vs. manned heavy helicopters (reduced crew costs, higher utilization)
- **Safety enhancement**: Removes pilots from high-risk low-altitude operations in smoke, turbulence, and mountainous terrain
- **Operational tempo**: Autonomous operations eliminate crew duty-day limitations; aircraft can surge to 16+ flight hours per day during peak fire conditions
- **Geographic reach**: 125+ nm mission radius enables basing at regional airports rather than requiring forward-deployed staging areas

### 4.2 MAAP-1I "Sentinel" – Intelligence, Surveillance, and Reconnaissance Variant

**Mission**: Persistent airborne surveillance for defense, border security, law enforcement, and disaster assessment

**Unique Capabilities**

*Advanced Sensor Suite*
- Stabilized multi-sensor turret with 360° continuous rotation, -120° to +30° elevation
- HD electro-optical (1920×1080) + medium-wave infrared (MWIR) + long-wave infrared (LWIR) imaging
- Integrated laser designator and rangefinder for precision target geo-location
- Onboard real-time video processing with automatic object detection and tracking

*Extended Endurance Configuration*
- Standard auxiliary fuel tanks extend endurance to 6+ hours with 4,000 lb mission payload
- Loiter altitude: 2,000-10,000 ft optimized for sensor coverage vs. fuel efficiency
- Long-range datalink enables over-the-horizon operations up to 150 nm from GCS

*Mission Data Management*
- 4 TB solid-state mission recorder with FIPS 140-2 encryption
- Simultaneous dual HD video streams (full-motion video to GCS + metadata overlay)
- Automatic sensor-to-shooter datalink integration for time-sensitive targeting
- Post-mission data retrieval via secure network or physical media transfer

*Optional Signals Intelligence (SIGINT)*
- Communications intelligence (COMINT) receiver suite for electronic emissions collection
- Direction-finding capable for emitter geo-location
- Exportable/removable architecture accommodates customer-specific releasability requirements

*Crew Configuration*
- **Level 3 autonomy at IOC**: GCS crew monitors autonomous flight and controls sensor suite
- **Typical crew**: Pilot (supervisory flight control) + Sensor Operator (payload management) + optional Mission Commander
- **Level 4 autonomy by FOC**: Fully autonomous sensor slew-to-cue and target tracking; crew intervenes only for complex analysis or rules-of-engagement decisions

**Operational Scenarios**

*Border Security*
- Persistent surveillance of remote border areas with automatic intrusion detection
- Coordinated operations: multiple MAAP-1I aircraft provide overlapping coverage while autonomously deconflicting patrol areas
- Long endurance enables single-aircraft coverage of 150+ linear miles of border per sortie

*Disaster Assessment*
- Rapid deployment post-hurricane/earthquake for damage mapping and survivor detection
- FLIR sensors identify heat signatures from trapped survivors in collapsed structures
- Real-time imagery supports incident command decision-making

*Maritime Patrol*
- Coastal surveillance for illegal fishing, smuggling interdiction, and search-and-rescue
- Open-ocean endurance: 6+ hours on-station at 100 nm from shore
- Coordinate passage to response assets (Coast Guard cutters, law enforcement) via automatic datalink

*Defense Applications*
- Reconnaissance and surveillance for forward deployed forces
- Target acquisition and battle damage assessment
- Reduced acoustic signature (95 dBA vs. 105+ dBA conventional) supports covert observation missions

### 4.3 MAAP-1C "Atlas" – Cargo and Logistics Variant

**Mission**: Heavy external and internal cargo delivery to remote, austere locations

**Unique Capabilities**

*Optimized Cargo Handling*
- Dual cargo hooks (28 ft separation) rated to 12,000 lb single / 8,000+8,000 lb tandem
- Automated load weight sensing and pendulum angle monitoring
- Real-time load stability augmentation via flight control law adaptation
- Precision delivery: GPS-guided release point with ±15 m accuracy

*Flexible Internal Cargo Bay*
- 950-1,100 ft³ cabin volume with 8,000-9,500 lb capacity
- Reconfigurable rail/roller system accepts palletized or bulk cargo
- 74" × 78" aft ramp for drive-on/drive-off loading
- 24 tie-down points rated to 5,000 lb each for securing irregularly shaped cargo

*Long-Range Delivery*
- 125-175 nm mission radius with 12,000 lb external load
- 185-240 nm radius with 8,000 lb internal cargo (lower aerodynamic drag)
- Ferry range: 450-650 nm enables inter-theater repositioning without airlift support

*Autonomous Load Management*
- Automatic center-of-gravity calculation from load manifest data
- Dynamic ballast adjustment for dual external loads
- Obstacle avoidance during low-altitude cargo delivery flight
- Precision hover positioning (±1 m) over unimproved landing zones

*Crew Configuration*
- **Level 3 autonomy at IOC**: Single GCS operator monitors autonomous cargo flight, approves critical phases (load release)
- **Level 4 autonomy by FOC**: Fully autonomous cargo missions including load acquisition, transit, delivery, and release; human authorizes mission but does not actively supervise

**Operational Applications**

*Commercial Logistics*
- Heavy equipment delivery to remote mining, oil/gas, and construction sites
- Just-in-time cargo delivery reduces ground inventory and transportation costs
- Operates from unimproved sites without runway requirements

*Military Logistics (Non-Combat)*
- Forward Operating Base (FOB) sustainment: food, water, ammunition resupply
- Rapid response to isolated units without road access
- Reduced ground convoy exposure in denied/contested areas

*Humanitarian Relief*
- Post-disaster cargo delivery to communities with damaged infrastructure
- Medical supply delivery to remote clinics
- Temporary bridge: delivers food, water, shelter while ground routes are repaired

*Infrastructure Construction Support*
- Tower erection (communications, power transmission)
- Bridge component placement
- Heavy machinery positioning in inaccessible terrain

**Economic Value Proposition**

Compared to manned heavy-lift helicopters (CH-47, Mi-26 class):
- **30%+ lower operating cost** per flight hour (reduced crew, optimized maintenance)
- **Higher utilization rate**: 16+ flight hours per day achievable vs. 8-10 hours for crew-limited operations
- **Smaller logistics footprint**: One GCS supports 4 aircraft vs. 8+ crew for manned equivalents
- **Rapid ROI**: Commercial operators project 4-6 year payback period based on reduced operating costs

---

## 5. PERFORMANCE HIGHLIGHTS

### 5.1 Weight and Payload Summary

| **Parameter** | **Threshold** | **Objective** |
|---|---|---|
| Maximum Gross Takeoff Weight | 26,000 lb (11,793 kg) | 28,500 lb (12,928 kg) |
| Basic Empty Weight | ≤14,200 lb (6,441 kg) | ≤13,600 lb (6,169 kg) |
| Useful Load | ≥11,800 lb (5,352 kg) | ≥14,900 lb (6,759 kg) |
| Internal Cargo | 8,000 lb (3,629 kg) | 9,500 lb (4,309 kg) |
| External Load (single hook) | 12,000 lb (5,443 kg) | 16,000 lb (7,257 kg) |
| Fuel Capacity (internal) | 2,400 lb (1,089 kg) | 2,800 lb (1,270 kg) |

### 5.2 Speed and Range Summary

| **Parameter** | **Threshold** | **Objective** |
|---|---|---|
| Maximum Cruise Speed | 135 KTAS (250 km/h) | 150 KTAS (278 km/h) |
| Never-Exceed Speed (VNE) | 165 KTAS (306 km/h) | — |
| Mission Radius (12,000 lb external) | 125 nm (232 km) | 175 nm (324 km) |
| Ferry Range (no payload) | 450 nm (833 km) | 500 nm (926 km) |
| Endurance (design mission) | 4.0 hours | 6.0 hours |

### 5.3 Hover and Altitude Performance

| **Parameter** | **Threshold** | **Objective** |
|---|---|---|
| Hover Ceiling OGE (MGTOW, 95°F) | 8,000 ft PA (2,438 m) | 10,000 ft PA (3,048 m) |
| Hover Ceiling IGE (MGTOW, 95°F) | 10,000 ft PA (3,048 m) | 12,000 ft PA (3,658 m) |
| Service Ceiling | 12,000 ft (3,658 m) | 15,000 ft (4,572 m) |
| Rate of Climb (sea level, MGTOW) | 1,800 fpm (9.1 m/s) | 2,200 fpm (11.2 m/s) |

### 5.4 Reliability and Maintainability Targets

| **Parameter** | **Threshold** | **Objective** |
|---|---|---|
| Mean Time Between Mission Abort | 500 flight hours | 750 flight hours |
| Maintenance Man-Hours per Flight Hour | ≤4.5 MMH/FH | ≤3.5 MMH/FH |
| Mean Time To Repair (LRU replacement) | ≤45 minutes | ≤30 minutes |
| Operational Availability | 85% | 90% |
| Airframe Service Life | 20,000 flight hours / 30 years | 25,000 flight hours |

These reliability targets—substantially better than legacy heavy-lift platforms—result from:
- Modular Line Replaceable Unit (LRU) design with standardized interfaces
- Comprehensive Built-In Test Equipment (BITE) providing 95%+ fault detection coverage
- Health and Usage Monitoring System (HUMS) enabling predictive maintenance
- Composite primary structure eliminating corrosion maintenance burden

---

## 6. PROGRAM STATUS AND MILESTONES

### 6.1 Current Program Phase

The MAAP-1 program is in **Engineering and Manufacturing Development (EMD)**, having completed Preliminary Design Review (PDR) and progressing toward Critical Design Review (CDR). All major subsystems are in detailed design, with long-lead procurement underway for propulsion, transmission, and avionics systems.

### 6.2 Key Milestones Achieved

| **Milestone** | **Date** | **Status** |
|---|---|---|
| Program Initiation | PM 0 | ✓ Complete |
| Requirements Baseline Approval | PM 6 | ✓ Complete |
| Preliminary Design Review (PDR) | PM 18 | ✓ Complete |
| Propulsion System Down-Select | PM 24 | ✓ Complete |
| Wind Tunnel Testing (1/5 scale) | PM 28 | ✓ Complete |
| Long-Lead Procurement Authorization | PM 30 | ✓ Complete |
| Autonomy Software Architecture Review | PM 32 | ✓ Complete |

### 6.3 Upcoming Program Milestones

| **Milestone** | **Target Date** | **Significance** |
|---|---|---|
| **Critical Design Review (CDR)** | **PM 42** | Final design freeze; transition to fabrication |
| **Static Airframe Test** | PM 48 | Ultimate load demonstration for certification |
| **Ground Systems Integration** | PM 50 | Flight control/avionics integration complete |
| **First Flight** | **PM 54** | Begin company flight test program |
| **FAA Conformity Inspection** | PM 72 | Production-representative aircraft inspection |
| **Flight Test Completion** | PM 78 | 500 flight hours; all test points complete |
| **FAA Type Certificate (MAAP-1C)** | **PM 84** | Baseline cargo variant certification |
| **Low-Rate Initial Production (LRIP)** | PM 66 | Initial production commitment decision |
| **Full-Rate Production (FRP)** | PM 108 | Sustained 18 aircraft/year production rate |

### 6.4 Risk Management

The MAAP-1 program employs a rigorous risk management process, tracking technical, schedule, cost, and programmatic risks through weekly Integrated Product Team (IPT) reviews and monthly Program Management Reviews (PMR).

**Key Risk Areas and Mitigations**

*Autonomous System Certification*
- **Risk**: No established FAA certification framework for heavy autonomous cargo helicopters
- **Mitigation**: Early coordination with FAA AFS-400 and AFS-700; participation in industry working groups (RTCA SC-228 JARUS); phased certification approach starting with optionally-piloted MAAP-1F variant

*Weight Growth*
- **Risk**: Composite structure weight growth erodes payload performance
- **Mitigation**: Rigorous weight control program with 15% margin at PDR decreasing to 3% at CDR; weekly weight tracking by IPT; formal weight control board approval required for all changes affecting structural weight

*Supply Chain (Long-Lead Items)*
- **Risk**: Engine and transmission delivery delays impact first flight schedule
- **Mitigation**: Early vendor engagement and long-lead procurement (PM 30); dual-source strategy for critical components; contractual delivery incentives

*Software Complexity*
- **Risk**: Autonomous GNC software development underestimated; DO-178C DAL A/B compliance schedule impact
- **Mitigation**: Modular software architecture with early prototyping; automated test framework; experienced DO-178C development team; independent software verification and validation (IV&V) contractor engaged at PDR

The program's overall risk posture is assessed as **MODERATE** with no HIGH risks requiring Milestone Decision Authority escalation.

---

## 7. STRATEGIC VALUE AND CUSTOMER BASE

### 7.1 Target Markets and Customers

**Primary Markets**

*Aerial Firefighting Agencies*
- U.S. Forest Service, Bureau of Land Management, state forestry agencies
- International wildfire agencies (Australia, Canada, Mediterranean countries)
- Private aerial firefighting contractors (Coulson Aviation, Erickson Inc., etc.)
- **Market size**: 200+ aircraft potential over 15 years

*Defense and Homeland Security*
- U.S. Department of Defense (Army, Air Force, Special Operations Command)
- NATO member nations and Five-Eyes partners
- Border security and law enforcement agencies (CBP, state/local agencies)
- **Market size**: 150+ aircraft potential (non-combat logistics, ISR, training)

*Commercial Logistics*
- Heavy-lift cargo operators (Columbia Helicopters, Global Helicopter Services, etc.)
- Resource extraction industries (mining, oil/gas field support)
- Infrastructure construction contractors
- Humanitarian relief organizations (UN agencies, NGOs)
- **Market size**: 100+ aircraft potential

*Emerging Markets*
- Offshore wind farm construction and maintenance
- Urban air mobility (heavy cargo delivery to vertiports)
- Arctic operations (remote site support, scientific research)
- Island nation logistics (Pacific, Caribbean)

### 7.2 Competitive Advantages

| **Advantage** | **vs. Manned Heavy-Lift Helicopters** | **vs. Large UAVs/Drones** |
|---|---|---|
| **Operating Cost** | 30%+ lower ($/flight hour) | Similar or better with heavy-lift capability |
| **Payload Capacity** | Comparable (12,000 lb+) | 5-10× greater than Class III UAVs |
| **Crew Risk** | Eliminates pilot exposure to hazards | Equivalent (no crew) |
| **Operational Tempo** | 50%+ higher (no crew duty limits) | Equivalent |
| **Certification Basis** | FAA Type Certificate (civil operations) | First in heavy-lift class |
| **Mission Flexibility** | Modular: 3 missions from 1 airframe | Typically single-mission designs |
| **Hover Efficiency** | Tandem-rotor: superior to conventional | Fixed-wing UAVs cannot hover |

### 7.3 Economic Value Proposition

**For Aerial Firefighting Operators**
- **Lower acquisition cost**: $21.5M unit price (FY25$, FRP Lot 5) vs. $30-40M for comparable manned helicopters
- **Reduced operating costs**: ~$5,000/flight hour vs. $8,000-12,000 for manned equivalents
- **Higher availability**: 85-90% operational availability vs. 65-75% for aging manned fleets
- **Extended season**: Autonomous ops enable night firefighting; 24/7 availability vs. crew-limited day-only ops
- **ROI**: 5-7 year payback period based on reduced costs and higher utilization

**For Defense Customers**
- **Mission flexibility**: Single platform supports cargo, ISR, and training missions vs. separate fleets
- **Reduced logistics footprint**: 80%+ commonality across variants; single spare parts pipeline
- **Lower training costs**: One GCS operator vs. two-person aircrew; reduced flight hour requirements
- **Force multiplier**: Four aircraft controlled by one GCS vs. eight crew for manned equivalents
- **Reduced casualty risk**: No aircrew exposure in combat logistics / ISR missions

**For Commercial Operators**
- **Market expansion**: Autonomous heavy-lift enables new service offerings (unmanned remote site support)
- **Regulatory pathway**: FAA Type Certificate de-risks commercial operations vs. experimental/restricted category
- **Scalability**: Modular design and GCS multi-aircraft control enable rapid fleet expansion
- **Technology roadmap**: Open-architecture mission systems support customer-specific equipment integration

### 7.4 International Partnership Opportunities

The MAAP-1 is designed from inception for **international cooperation and export**:

- **Export-compliant baseline**: Green Aircraft contains no technology requiring export license modification for NATO/Five-Eyes nations (per ITAR/EAR analysis)
- **Modular defensive systems**: Easily removable architecture accommodates country-specific releasability determinations
- **Coalition interoperability**: NATO STANAG-compliant datalinks and command/control interfaces
- **Co-production potential**: Modular design enables licensed production of mission-specific systems by international partners

Current international engagement includes:
- Discussions with **Australian Department of Defence** for ISR and logistics variants
- Cooperative development discussions with **Canadian Department of National Defence** for Arctic operations configuration
- Market surveys in progress with **European Union** firefighting agencies

---

## 8. TECHNOLOGICAL INNOVATION

The MAAP-1 integrates proven aerospace technologies with cutting-edge autonomous systems, creating a platform that is both certifiable (building on decades of tandem-rotor operational experience) and transformational (pioneering autonomous heavy-lift operations).

### 8.1 Autonomy and Artificial Intelligence

**Advanced Flight Control Algorithms**
- Model-predictive control for external load stability augmentation
- Adaptive control laws compensate for varying cargo weight, CG position, and aerodynamic drag
- Machine learning algorithms optimize fuel efficiency based on real-time wind and weather data

**Perception and Situational Awareness**
- Multi-sensor fusion (GPS/INS, RADAR, EO/IR, LiDAR) creates comprehensive environmental model
- Terrain-relative navigation enables precision landing in GPS-denied environments
- Obstacle detection and avoidance during low-altitude cargo delivery
- Automatic landing zone selection evaluates slope, obstacles, surface hardness, and winds

**Decision-Making Under Uncertainty**
- Probabilistic mission planning accounts for weather forecasts, airspace restrictions, and fuel reserves
- Real-time mission re-planning when original plan becomes infeasible (weather divert, landing zone obstruction)
- Lost-link contingency logic prioritizes mission completion, aircraft safety, and ground safety

### 8.2 Modular Open Systems Architecture (MOSA)

The MAAP-1 is a flagship example of MOSA principles in aerospace:

**Open Interfaces**
- Core avionics employ VITA 65 OpenVPX hardware standard and FACE Technical Standard software architecture
- Government-owned interface specifications for all critical subsystems
- Mission system software portable across variants without recompilation

**Benefits Realized**
- **Technology refresh**: New mission payloads integrate without redesigning airframe or flight control systems
- **Competition**: Open architecture enables competitive procurement of mission systems throughout service life
- **Vendor independence**: No single-source proprietary lock-in for safety-critical systems

### 8.3 Advanced Materials and Structures

**Composite Primary Structure**
- Carbon/glass fiber hybrid construction delivers optimal strength-to-weight ratio
- Inherent corrosion resistance eliminates 60%+ of maintenance burden associated with legacy aluminum structures
- Damage tolerance: Structure maintains integrity after impact damage; composite repairs achievable at organizational level

**Dynamic Components Optimization**
- Rotor blades: Composite construction with titanium erosion strips; -12° linear twist optimized for hover and cruise efficiency
- Transmission: Split-torque planetary design with 30-minute oil-out run capability
- Drive shaft: Composite interconnecting shaft (28.5 ft length) delivers weight savings vs. metallic design

### 8.4 Human-Machine Teaming

The MAAP-1 GCS represents state-of-the-art human-autonomy interaction:

**Adaptive Automation**
- System dynamically adjusts automation level based on mission phase, environmental conditions, and operator workload
- Intelligent alerting: Machine learning algorithms reduce false alarms while ensuring critical alerts are never missed
- Predictive workload management: System anticipates high-workload mission phases and automates lower-priority tasks

**Operator Trust and Transparency**
- Real-time display of autonomous system confidence levels ("I am 95% confident the landing zone is obstacle-free")
- Explanation interface: Operator can query "Why did you choose this route?" and receive natural-language response
- Graduated autonomy: New operators begin with high supervisory oversight; system grants increasing autonomy as operator experience grows

---

## 9. SUSTAINABILITY AND ENVIRONMENTAL RESPONSIBILITY

### 9.1 Environmental Performance

**Reduced Noise Signature**
- 95 dBA @ 500 ft lateral (takeoff) vs. 105+ dBA for conventional heavy-lift helicopters
- Low rotor tip speed (622 ft/s vs. 700+ ft/s) reduces noise generation
- Enables operations near populated areas with reduced community impact

**Fuel Efficiency**
- Tandem-rotor design eliminates tail rotor power loss (~10-15% fuel savings vs. conventional configuration)
- Optimized cruise speed (120 KTAS) balances range and fuel consumption
- Projected 20-25% lower fuel consumption per ton-mile vs. manned heavy-lift benchmarks

**Emissions Reduction**
- Modern turboshaft engines meet stringent emissions standards (NOx, particulates)
- Autonomous operations optimize flight profiles for minimum fuel burn
- Single platform replaces multiple mission-specific aircraft, reducing fleet-wide emissions

### 9.2 Sustainable Operations

**Extended Service Life**
- 20,000-30,000 flight hour airframe design life (vs. 10,000-15,000 for legacy platforms)
- Modular design enables component-level replacement rather than whole-aircraft retirement
- Technology insertion capability extends economic life beyond structural service life

**Reduced Logistics Footprint**
- Modular maintenance reduces consumable parts waste
- Health monitoring enables on-condition maintenance (replace only when needed vs. fixed calendar schedules)
- 80%+ parts commonality across variants reduces supply chain redundancy

### 9.3 Circular Economy Principles

**Design for Disassembly**
- Bolted construction (vs. riveted) enables non-destructive disassembly at end-of-life
- Composite materials recyclable through thermal decomposition processes
- Modular avionics enable reuse in next-generation platforms

**Remanufacturing Program (Planned)**
- Eurus Systems will offer remanufacturing services at 10,000 and 20,000 flight hours
- Zero-time recertification extends service life while upgrading to latest avionics and mission systems
- Reduces whole-aircraft waste; remanufactured aircraft cost 40-50% of new production

---

## 10. PATH TO MARKET: CERTIFICATION AND PRODUCTION

### 10.1 Certification Strategy

**FAA Type Certification (14 CFR Part 29)**
- Baseline MAAP-1C cargo variant will pursue full FAA Type Certificate under Part 29 (Transport Category Rotorcraft)
- Certification basis includes Special Conditions for autonomous operations (to be negotiated with FAA AFS-400)
- Type Certificate establishes regulatory framework for derivative variants

**Phased Certification Approach**
1. **Phase 1 (MAAP-1C)**: Full Type Certificate for autonomous cargo operations in unrestricted airspace
2. **Phase 2 (MAAP-1F)**: Optionally-piloted firefighting variant via Type Certificate amendment; demonstrates manned operations before transition to autonomous
3. **Phase 3 (MAAP-1I)**: ISR variant Type Certificate amendment for extended-endurance autonomous operations

**International Certification**
- EASA (European Union Aviation Safety Agency) validation planned post-FAA certification
- Transport Canada validation for Canadian market
- Australian CASA validation for Asia-Pacific market

**Military Airworthiness**
- U.S. DoD airworthiness certification per MIL-HDBK-516C
- Military Flight Release process for defense variants follows commercial certification
- NATO STANAG 4703 compliance for coalition interoperability

### 10.2 Production Ramp and Industrial Base

**Production Facilities**
- Final assembly: Eurus Systems primary manufacturing facility, [Location TBD]
- Composite fabrication: Integrated in-house composite manufacturing center
- Flight test: Co-located flight test facility with 10,000 ft runway

**Production Rate Targets**

| **Phase** | **Rate** | **Cumulative Aircraft** | **Timeframe** |
|---|---|---|---|
| **Engineering & Manufacturing Development** | 3 aircraft (test fleet) | 3 | PM 54-66 |
| **Low-Rate Initial Production (LRIP)** | 6 aircraft/year | 15 | PM 66-90 |
| **Full-Rate Production (FRP)** | 18 aircraft/year | 51+ | PM 90+ |

**Supply Chain Strategy**
- Tier 1 suppliers: Major subsystems (engines, transmission, avionics, mission systems)
- Tier 2/3 suppliers: Detailed parts and subassemblies
- Strategic partnerships: Co-development agreements with key suppliers ensure long-term supportability

**Quality and Configuration Management**
- AS9100D certified quality management system
- Digital twin: Every production aircraft has complete digital model for lifecycle configuration management
- Continuous process improvement: Production engineering team implements cost/quality improvements throughout production run

### 10.3 Customer Support and Training

**Integrated Logistics Support (ILS)**
- Comprehensive Logistics Support Analysis (LSA) identifies all support equipment, spares, and training requirements
- Performance-Based Logistics (PBL) contracts available: Eurus Systems guarantees operational availability in exchange for fixed annual fee
- Global spares distribution: Regional warehouses in North America, Europe, Asia-Pacific

**Training Systems**
- Full-mission Ground Control Station simulator (Level 6 fidelity)
- Part-task trainers for maintenance personnel
- Computer-based training for mission planning and system operation
- Initial cadre training: 8-week course for pilots/operators, 12-week course for maintainers

**Sustainment Throughout Service Life**
- 24/7 technical support hotline
- Remote diagnostics: Aircraft transmit health data to Eurus Systems support center for predictive maintenance analysis
- Tech refresh roadmap: Planned avionics and mission system upgrades every 5-7 years
- Service life extension programs at 10,000 and 20,000 flight hours

---

## 11. LOOKING FORWARD: FUTURE CAPABILITIES

The MAAP-1 platform is designed for growth, with identified capability enhancements planned for post-Initial Operational Capability introduction:

### 11.1 Swarm Operations (Collaborative Autonomy)

**Vision**: Multiple MAAP-1 aircraft coordinate autonomously to execute complex missions

**Capabilities**
- Shared situational awareness: Aircraft exchange sensor data to create common operating picture
- Dynamic task allocation: Swarm autonomously divides mission tasks based on aircraft capabilities, fuel state, and position
- Cooperative behaviors: Formation flight, coordinated fire suppression drops, distributed ISR coverage

**Applications**
- **Wildfire suppression**: 3-4 aircraft autonomously coordinate drops to create continuous fire break
- **Logistics**: Swarm delivers components of large infrastructure project in coordinated sequence
- **Search and rescue**: Multiple ISR aircraft divide search area, automatically hand off tracks between platforms

**Technical Readiness**: Swarm algorithms under development in simulation; flight test demonstration planned for FOC+18 months

### 11.2 Artificial Intelligence & Machine Learning Integration

**Planned AI/ML Enhancements**

*Predictive Maintenance*
- ML algorithms analyze vibration, temperature, and usage data to predict component failures 50-100 flight hours in advance
- Automatic spare parts ordering and maintenance scheduling optimization
- Target: 20% reduction in unscheduled maintenance events

*Mission Optimization*
- Reinforcement learning for real-time fuel-optimal path planning
- Weather pattern recognition for proactive mission re-planning
- Cargo loading optimization for center-of-gravity management

*Computer Vision for Enhanced Autonomy*
- Deep learning for landing zone assessment (obstacle detection, slope estimation, surface classification)
- Automatic power line detection during low-altitude flight
- Fire perimeter mapping and hotspot detection for firefighting missions

### 11.3 Hybrid-Electric Propulsion (Technology Demonstrator)

**Long-Term Vision**: Transition to hybrid-electric or fully-electric propulsion for reduced emissions and operating costs

**Concept**
- Turboshaft generator provides electrical power to electric drive motors on each rotor
- Batteries provide peak power for hover/takeoff; generator recharges in cruise
- Projected 30-40% fuel savings in typical cargo mission profile

**Status**: Feasibility study underway; subscale demonstrator planned for 2028 timeframe

**Challenges**
- Battery energy density: Current technology insufficient for heavy-lift mission profiles without significant weight penalty
- Electrical system weight: High-power electrical distribution adds ~1,500 lb vs. mechanical transmission
- Thermal management: Cooling system for motors/batteries adds complexity

**Pathway**: Monitor battery technology maturation (solid-state batteries projected 2×-3× energy density improvement); retrofit existing MAAP-1 airframes as technology matures

---

## 12. CONCLUSION

The **AetherForge MAAP-1** represents a transformational leap in rotary-wing aviation—combining the proven lifting efficiency of tandem-rotor design with cutting-edge autonomous systems to create a platform that is safer, more capable, and more affordable than any manned heavy-lift helicopter in service today.

### Key Takeaways

1. **Unmatched Heavy-Lift Performance**: 12,000+ lb payload, 250+ nm range, 8,000 ft hot-and-high hover capability
2. **Mission Flexibility**: Three variants (firefighting, ISR, cargo) share 80%+ commonality for logistics efficiency
3. **Autonomous Safety**: Level 3/4 autonomy removes crews from high-risk missions while maintaining equivalent safety through redundant systems
4. **Economic Value**: 30%+ lower operating costs vs. manned platforms; 5-7 year ROI for commercial operators
5. **Regulatory Pathways**: FAA Type Certification approach de-risks civil and commercial operations
6. **Global Market**: 450+ aircraft potential across firefighting, defense, commercial logistics, and emerging applications
7. **Technology Leadership**: First-in-class autonomous heavy-lift helicopter; establishes Eurus Systems as industry pioneer

### The Path Ahead

With Critical Design Review approaching (PM 42), first flight on the horizon (PM 54), and FAA Type Certification targeted for PM 84, the MAAP-1 program is on track to deliver transformational capability to customers worldwide. The engineering challenges are significant—certifying autonomous operations at this scale and complexity is unprecedented—but the Eurus Systems team brings deep expertise in rotorcraft design, autonomous systems, and regulatory collaboration.

The MAAP-1 is more than a helicopter—it is a vision of aviation's future, where intelligent machines augment human capability, reduce risk, and expand the boundaries of what rotorcraft can achieve. From fighting wildfires in the Sierra Nevada to delivering humanitarian relief to disaster zones to supporting military logistics in contested environments, the AetherForge MAAP-1 will redefine what is possible in heavy-lift operations.

### Next Steps for Stakeholders

**For Potential Customers**
- Contact Eurus Systems Business Development for detailed briefings and demonstrations
- Participate in user working groups to influence requirements for future capability increments
- Consider early production slot reservations (LRIP slots filling rapidly)

**For Industry Partners**
- Explore subcontractor and supplier opportunities across propulsion, avionics, and mission systems
- Investigate co-development partnerships for international variants
- Engage with Technology Transfer Office regarding MOSA interface licensing

**For Regulatory Agencies**
- Continue collaborative engagement on autonomous system certification frameworks
- Participate in Special Conditions development for autonomous heavy-lift operations
- Support harmonization of international airworthiness standards (FAA/EASA/Transport Canada)

**For Investors and Analysts**
- Review detailed program financials and business case (available under NDA)
- Attend quarterly program reviews and annual stakeholder conferences
- Monitor key program milestones (CDR, First Flight, Type Certification)

---

## APPENDIX A: TECHNICAL SPECIFICATIONS SUMMARY

| **Category** | **Parameter** | **Threshold** | **Objective** |
|---|---|---|---|
| **Dimensions** | Overall Length (rotors turning) | 80.0 ft (24.4 m) | — |
| | Rotor Diameter (each) | 42.0 ft (12.8 m) | — |
| | Overall Height | 18.5 ft (5.6 m) | — |
| **Weight** | Maximum Gross Takeoff Weight | 26,000 lb (11,793 kg) | 28,500 lb (12,928 kg) |
| | Basic Empty Weight | ≤14,200 lb (6,441 kg) | ≤13,600 lb (6,169 kg) |
| | Useful Load | ≥11,800 lb (5,352 kg) | ≥14,900 lb (6,759 kg) |
| **Payload** | Internal Cargo | 8,000 lb (3,629 kg) | 9,500 lb (4,309 kg) |
| | External Load (single hook) | 12,000 lb (5,443 kg) | 16,000 lb (7,257 kg) |
| | Dual External Load | 8,000 + 8,000 lb | 10,000 + 10,000 lb |
| **Performance** | Maximum Cruise Speed | 135 KTAS (250 km/h) | 150 KTAS (278 km/h) |
| | Never-Exceed Speed | 165 KTAS (306 km/h) | — |
| | Mission Radius (12,000 lb load) | 125 nm (232 km) | 175 nm (324 km) |
| | Ferry Range | 450 nm (833 km) | 500 nm (926 km) |
| | Endurance | 4.0 hours | 6.0 hours |
| **Hover** | OGE Hover Ceiling (MGTOW, 95°F) | 8,000 ft PA (2,438 m) | 10,000 ft PA (3,048 m) |
| | IGE Hover Ceiling (MGTOW, 95°F) | 10,000 ft PA (3,048 m) | 12,000 ft PA (3,658 m) |
| | Service Ceiling | 12,000 ft (3,658 m) | 15,000 ft (4,572 m) |
| **Propulsion** | Engines | 2× turboshaft, FADEC | — |
| | Takeoff Power (each) | 2,000 shp (1,491 kW) | 2,200 shp (1,641 kW) |
| | OEI Emergency Power (2.5 min) | 2,400 shp (1,790 kW) | 2,600 shp (1,939 kW) |
| | Fuel Capacity (internal) | 2,400 lb (1,089 kg) | 2,800 lb (1,270 kg) |
| **Autonomy** | Autonomy Level (Cargo/ISR at IOC) | Level 3 | Level 4 (by FOC) |
| | Autonomy Level (Firefighting at IOC) | Level 2 | Level 3 (by FOC) |
| **Reliability** | Mean Time Between Mission Abort | 500 flight hours | 750 flight hours |
| | MMH/FH (Maintenance Man-Hours) | ≤4.5 | ≤3.5 |
| | Operational Availability | 85% | 90% |
| **Environment** | Operating Temperature Range | -32°C to +49°C | -40°C to +52°C |
| | Maximum Crosswind (autonomous landing) | 25 kt steady, 35 kt gust | 35 kt steady, 45 kt gust |

---

## APPENDIX B: ACRONYMS AND DEFINITIONS

| **Acronym** | **Definition** |
|---|---|
| ADS-B | Automatic Dependent Surveillance–Broadcast |
| AGL | Above Ground Level |
| BLOS | Beyond Line of Sight |
| C2/C3 | Command and Control / Command, Control, and Communication |
| CDR | Critical Design Review |
| CG | Center of Gravity |
| DAA | Detect and Avoid |
| DVE | Degraded Visual Environment |
| EMD | Engineering and Manufacturing Development |
| EO/IR | Electro-Optical / Infrared |
| FAA | Federal Aviation Administration |
| FADEC | Full Authority Digital Engine Control |
| FLIR | Forward-Looking Infrared |
| FOC | Full Operational Capability |
| FRP | Full-Rate Production |
| GCS | Ground Control Station |
| GNSS | Global Navigation Satellite System |
| GPS | Global Positioning System |
| HUMS | Health and Usage Monitoring System |
| IGE | In Ground Effect |
| INS | Inertial Navigation System |
| IOC | Initial Operational Capability |
| ISR | Intelligence, Surveillance, Reconnaissance |
| KTAS | Knots True Airspeed |
| LOS | Line of Sight |
| LRIP | Low-Rate Initial Production |
| LRU | Line Replaceable Unit |
| MAAP | Modular Autonomous Aerial Platform |
| MGTOW | Maximum Gross Takeoff Weight |
| MMH/FH | Maintenance Man-Hours per Flight Hour |
| MOSA | Modular Open Systems Approach |
| OEI | One Engine Inoperative |
| OGE | Out of Ground Effect |
| PA | Pressure Altitude |
| PDR | Preliminary Design Review |
| RADAR | Radio Detection and Ranging |
| SATCOM | Satellite Communication |
| TCAS | Traffic Collision Avoidance System |
| VNE | Never-Exceed Speed |

---

## CONTACT INFORMATION

**Eurus Systems MAAP-1 Program Office**

**Program Manager**: [Name]  
**Email**: maap1-programoffice@eurussystems.com  
**Phone**: [Phone Number]

**Business Development Inquiries**: bd@eurussystems.com  
**Media Relations**: media@eurussystems.com  
**Investor Relations**: ir@eurussystems.com

**Website**: www.eurussystems.com/maap1  
**Secure File Exchange**: sftp.eurussystems.com (credentials upon request)

---

**APPROVED FOR RELEASE:**

---

**[Signature]**  
**[Name], Program Manager**  
MAAP-1 Program  
Eurus Systems

Date: _______________

---

*This document contains proprietary information of Eurus Systems and is provided for informational purposes only. Technical specifications are subject to change as the program matures through Engineering and Manufacturing Development. Export-controlled technical data has been redacted from this public overview document. For detailed technical specifications, contact the MAAP-1 Program Office.*

---

**END OF DOCUMENT**