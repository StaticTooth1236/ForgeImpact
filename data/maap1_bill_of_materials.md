# Eurus Systems MAAP-1 Program
## Master Bill of Materials (BOM)
### Multi-role Advanced Aerial Platform - Generation 1

**Document Number:** AF-MAAP1-BOM-001  
**Revision:** C  
**Date:** 2024-01-15  
**Classification:** Company Proprietary  
**Prepared by:** Aerospace Manufacturing Engineering  

---

## Table of Contents

1. [Document Overview](#document-overview)
2. [BOM Hierarchy Structure](#bom-hierarchy-structure)
3. [Common Core Platform](#common-core-platform)
4. [Variant-Specific Configurations](#variant-specific-configurations)
5. [Long-Lead Items Summary](#long-lead-items-summary)
6. [Cost Roll-Up Summary](#cost-roll-up-summary)

---

## Document Overview

### Purpose
This Master Bill of Materials defines all components, assemblies, and raw materials required for the manufacture of Eurus Systems MAAP-1 aircraft across all mission variants. This document is aligned with:

- Program Requirements Baseline (PRB) Document AF-MAAP1-PRB-001
- Master Drawing Tree AF-MAAP1-DWG-TREE-001
- Configuration Management Plan AF-MAAP1-CMP-001

### BOM Conventions

**Part Numbering System:**
- **AF-MAAP1-XX-YYYY-ZZ**
  - AF = Eurus Systems
  - MAAP1 = Program designation
  - XX = Major assembly code
  - YYYY = Sequential number
  - ZZ = Variant code (00 = common, 01-05 = variant specific)

**Make/Buy Codes:**
- **MAKE** = Manufactured in-house
- **BUY** = Procured from supplier
- **ASSY** = Assembly operation (may contain both make and buy items)

**Lead Time Categories:**
- **LL** = Long-lead (>6 months)
- **ML** = Medium-lead (3-6 months)
- **SL** = Short-lead (<3 months)

---

## BOM Hierarchy Structure

### Level 0: Complete Aircraft
### Level 1: Major Assemblies (Drawing Tree Groups)
### Level 2: Sub-Assemblies
### Level 3: Detail Parts and Procured Items

---

## Common Core Platform

### 1.0 AIRFRAME ASSEMBLY (AF-MAAP1-AF)

#### 1.1 Forward Fuselage Assembly
**Drawing Reference:** AF-MAAP1-AF-1000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AF-1001-00 | Nose Cone Assembly | 1 | BUY | Carbon Fiber Composite, AS4/8552 | $45,000 | ML |
| AF-MAAP1-AF-1002-00 | Forward Fuselage Barrel Section | 1 | MAKE | Al 7075-T7351 | $125,000 | ML |
| AF-MAAP1-AF-1003-00 | Cockpit Frame Assembly | 1 | MAKE | Ti-6Al-4V, AMS 4928 | $280,000 | LL |
| AF-MAAP1-AF-1004-00 | Avionics Bay Structure | 1 | MAKE | Al 7050-T7451 | $65,000 | SL |
| AF-MAAP1-AF-1005-00 | Forward Bulkhead, Station 100 | 1 | MAKE | Al 7075-T7351, 0.375" | $18,500 | SL |
| AF-MAAP1-AF-1006-00 | Bulkhead, Station 145 | 1 | MAKE | Al 7075-T7351, 0.312" | $15,200 | SL |
| AF-MAAP1-AF-1007-00 | Nose Landing Gear Support Frame | 1 | MAKE | Ti-6Al-4V, AMS 4928 | $95,000 | ML |
| AF-MAAP1-AF-1010-00 | Forward Fuselage Skin Panel Set (12 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.040" | $42,000 | SL |
| AF-MAAP1-AF-1015-00 | Stringer Set, Forward Section (24 pcs) | 1 | MAKE | Al 7075-T6 Extrusion | $28,000 | SL |
| AF-MAAP1-AF-1020-00 | Frame Set, Forward (8 pcs) | 1 | MAKE | Al 7075-T7351 Machined | $52,000 | SL |

**Sub-total Forward Fuselage:** $765,700

#### 1.2 Center Fuselage Assembly
**Drawing Reference:** AF-MAAP1-AF-2000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AF-2001-00 | Center Fuselage Barrel Section | 1 | MAKE | Al 7075-T7351 | $185,000 | ML |
| AF-MAAP1-AF-2002-00 | Wing Center Section Carry-Through | 1 | MAKE | Ti-6Al-4V Forging, AMS 4928 | $425,000 | LL |
| AF-MAAP1-AF-2003-00 | Main Landing Gear Bulkhead | 2 | MAKE | Ti-6Al-4V, AMS 4928 | $145,000 | LL |
| AF-MAAP1-AF-2004-00 | Engine Bay Firewall | 2 | BUY | Inconel 625, AMS 5666 | $38,000 | ML |
| AF-MAAP1-AF-2005-00 | Fuel Tank Support Structure | 1 | MAKE | Al 7050-T7451 | $72,000 | SL |
| AF-MAAP1-AF-2010-00 | Center Fuselage Skin Panel Set (16 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.050" | $58,000 | SL |
| AF-MAAP1-AF-2015-00 | Stringer Set, Center Section (32 pcs) | 1 | MAKE | Al 7075-T6 Extrusion | $36,000 | SL |
| AF-MAAP1-AF-2020-00 | Frame Set, Center (12 pcs) | 1 | MAKE | Al 7075-T7351 Machined | $78,000 | SL |
| AF-MAAP1-AF-2025-00 | Keel Beam Assembly | 1 | MAKE | Al 7075-T7351 Extrusion | $92,000 | ML |
| AF-MAAP1-AF-2030-00 | Wing Attach Fitting Set (4 pcs) | 1 | MAKE | Ti-6Al-4V Forging, AMS 4928 | $185,000 | LL |

**Sub-total Center Fuselage:** $1,314,000

#### 1.3 Aft Fuselage Assembly
**Drawing Reference:** AF-MAAP1-AF-3000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AF-3001-00 | Aft Fuselage Barrel Section | 1 | MAKE | Al 7075-T7351 | $142,000 | ML |
| AF-MAAP1-AF-3002-00 | Tail Cone Assembly | 1 | MAKE | Al 2024-T3 | $68,000 | SL |
| AF-MAAP1-AF-3003-00 | Vertical Stabilizer Attachment Frame | 1 | MAKE | Ti-6Al-4V, AMS 4928 | $165,000 | LL |
| AF-MAAP1-AF-3004-00 | Horizontal Stabilizer Attachment Frame (2) | 1 | MAKE | Ti-6Al-4V, AMS 4928 | $195,000 | LL |
| AF-MAAP1-AF-3005-00 | Empennage Carry-Through Structure | 1 | MAKE | Al 7075-T7351 | $88,000 | ML |
| AF-MAAP1-AF-3010-00 | Aft Fuselage Skin Panel Set (14 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.040" | $48,000 | SL |
| AF-MAAP1-AF-3015-00 | Stringer Set, Aft Section (28 pcs) | 1 | MAKE | Al 7075-T6 Extrusion | $32,000 | SL |
| AF-MAAP1-AF-3020-00 | Frame Set, Aft (10 pcs) | 1 | MAKE | Al 7075-T7351 Machined | $65,000 | SL |
| AF-MAAP1-AF-3025-00 | APU Bay Structure | 1 | MAKE | Al 7050-T7451 | $42,000 | SL |
| AF-MAAP1-AF-3030-00 | Engine Exhaust Channel | 2 | BUY | Inconel 718, AMS 5663 | $28,000 | ML |

**Sub-total Aft Fuselage:** $873,000

#### 1.4 Wing Assembly
**Drawing Reference:** AF-MAAP1-AF-4000-00  
**Quantity per Aircraft:** 1 (Left & Right)  
**Make/Buy:** ASSY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AF-4001-00 | Wing Center Section | 1 | MAKE | Al 7075-T7351 Integral Milled | $385,000 | LL |
| AF-MAAP1-AF-4002-00 | Wing Outer Panel - Left | 1 | MAKE | Al 7075-T7351 Integral Milled | $425,000 | LL |
| AF-MAAP1-AF-4003-00 | Wing Outer Panel - Right | 1 | MAKE | Al 7075-T7351 Integral Milled | $425,000 | LL |
| AF-MAAP1-AF-4004-00 | Wing Tip Assembly - Left | 1 | BUY | Carbon Fiber Composite, AS4/8552 | $32,000 | ML |
| AF-MAAP1-AF-4005-00 | Wing Tip Assembly - Right | 1 | BUY | Carbon Fiber Composite, AS4/8552 | $32,000 | ML |
| AF-MAAP1-AF-4010-00 | Front Spar Assembly, Left Outer | 1 | MAKE | Al 7075-T7351 Extrusion | $125,000 | ML |
| AF-MAAP1-AF-4011-00 | Front Spar Assembly, Right Outer | 1 | MAKE | Al 7075-T7351 Extrusion | $125,000 | ML |
| AF-MAAP1-AF-4012-00 | Rear Spar Assembly, Left Outer | 1 | MAKE | Al 7075-T7351 Extrusion | $98,000 | ML |
| AF-MAAP1-AF-4013-00 | Rear Spar Assembly, Right Outer | 1 | MAKE | Al 7075-T7351 Extrusion | $98,000 | ML |
| AF-MAAP1-AF-4020-00 | Wing Rib Set - Left (18 pcs) | 1 | MAKE | Al 7075-T7351 Machined | $145,000 | SL |
| AF-MAAP1-AF-4021-00 | Wing Rib Set - Right (18 pcs) | 1 | MAKE | Al 7075-T7351 Machined | $145,000 | SL |
| AF-MAAP1-AF-4030-00 | Upper Wing Skin Panel Set - Left (8 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.063" | $85,000 | SL |
| AF-MAAP1-AF-4031-00 | Upper Wing Skin Panel Set - Right (8 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.063" | $85,000 | SL |
| AF-MAAP1-AF-4032-00 | Lower Wing Skin Panel Set - Left (8 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.063" | $85,000 | SL |
| AF-MAAP1-AF-4033-00 | Lower Wing Skin Panel Set - Right (8 pcs) | 1 | MAKE | Al 2024-T3 Clad, 0.063" | $85,000 | SL |
| AF-MAAP1-AF-4040-00 | Leading Edge Assembly - Left | 1 | MAKE | Al 7075-T6 | $68,000 | ML |
| AF-MAAP1-AF-4041-00 | Leading Edge Assembly - Right | 1 | MAKE | Al 7075-T6 | $68,000 | ML |
| AF-MAAP1-AF-4050-00 | Fuel Tank (Integral, Left Wing) | 1 | ASSY | Al 2024-T3 (Sealed) | $125,000 | ML |
| AF-MAAP1-AF-4051-00 | Fuel Tank (Integral, Right Wing) | 1 | ASSY | Al 2024-T3 (Sealed) | $125,000 | ML |

**Sub-total Wing Assembly:** $3,265,000

#### 1.5 Empennage Assembly
**Drawing Reference:** AF-MAAP1-AF-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AF-5001-00 | Vertical Stabilizer Assembly | 1 | MAKE | Al 7075-T7351 | $185,000 | ML |
| AF-MAAP1-AF-5002-00 | Rudder Assembly | 1 | MAKE | Al 7075-T6 | $92,000 | ML |
| AF-MAAP1-AF-5003-00 | Horizontal Stabilizer Assembly - Left | 1 | MAKE | Al 7075-T7351 | $142,000 | ML |
| AF-MAAP1-AF-5004-00 | Horizontal Stabilizer Assembly - Right | 1 | MAKE | Al 7075-T7351 | $142,000 | ML |
| AF-MAAP1-AF-5005-00 | Elevator Assembly - Left | 1 | MAKE | Al 7075-T6 | $78,000 | ML |
| AF-MAAP1-AF-5006-00 | Elevator Assembly - Right | 1 | MAKE | Al 7075-T6 | $78,000 | ML |
| AF-MAAP1-AF-5010-00 | Vertical Stabilizer Spar | 1 | MAKE | Al 7075-T7351 Extrusion | $58,000 | SL |
| AF-MAAP1-AF-5011-00 | Horizontal Stabilizer Spar Set (2) | 1 | MAKE | Al 7075-T7351 Extrusion | $85,000 | SL |
| AF-MAAP1-AF-5020-00 | Empennage Fairing Set | 1 | BUY | Carbon Fiber Composite | $28,000 | ML |

**Sub-total Empennage:** $888,000

**TOTAL AIRFRAME ASSEMBLY:** $7,105,700

---

### 2.0 ROTOR SYSTEMS ASSEMBLY (AF-MAAP1-RS)

#### 2.1 Main Rotor Assembly
**Drawing Reference:** AF-MAAP1-RS-1000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** ASSY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-RS-1001-00 | Main Rotor Hub Assembly | 1 | BUY | Ti-6Al-4V Forging, AMS 4928 | $485,000 | LL |
| AF-MAAP1-RS-1002-00 | Main Rotor Blade Set (5 blades) | 1 | BUY | Carbon Fiber/Titanium Hybrid | $750,000 | LL |
| AF-MAAP1-RS-1003-00 | Blade Grip Assembly | 5 | BUY | Ti-6Al-4V, AMS 4928 | $95,000 | LL |
| AF-MAAP1-RS-1004-00 | Pitch Control Horn | 5 | BUY | Al 7075-T7351 | $18,500 | ML |
| AF-MAAP1-RS-1005-00 | Elastomeric Bearing Set | 5 | BUY | Proprietary Elastomer | $45,000 | LL |
| AF-MAAP1-RS-1006-00 | Main Rotor Mast | 1 | BUY | 300M Steel, AMS 6417 | $185,000 | LL |
| AF-MAAP1-RS-1007-00 | Swashplate Assembly | 1 | BUY | Al 7075-T7351/Steel | $125,000 | LL |
| AF-MAAP1-RS-1010-00 | Pitch Link Set (5) | 1 | BUY | 17-4PH Steel, AMS 5643 | $22,000 | ML |
| AF-MAAP1-RS-1011-00 | Scissors Assembly | 1 | BUY | Al 7075-T7351 | $28,000 | ML |
| AF-MAAP1-RS-1012-00 | Damper Assembly Set (5) | 1 | BUY | Hydraulic Damper | $85,000 | LL |
| AF-MAAP1-RS-1015-00 | Balance Weight Set | 5 | BUY | Tungsten Alloy | $35,000 | SL |
| AF-MAAP1-RS-1020-00 | Blade Anti-Erosion Leading Edge (5) | 1 | BUY | Nickel/Titanium | $42,000 | ML |
| AF-MAAP1-RS-1025-00 | Blade De-Icing System | 1 | BUY | Electrothermal | $145,000 | LL |

**Sub-total Main Rotor:** $2,060,500

#### 2.2 Tail Rotor Assembly
**Drawing Reference:** AF-MAAP1-RS-2000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** ASSY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-RS-2001-00 | Tail Rotor Hub Assembly | 1 | BUY | Al 7075-T7351 | $125,000 | LL |
| AF-MAAP1-RS-2002-00 | Tail Rotor Blade Set (4 blades) | 1 | BUY | Carbon Fiber Composite | $185,000 | LL |
| AF-MAAP1-RS-2003-00 | Tail Rotor Gearbox | 1 | BUY | Magnesium Alloy Housing | $245,000 | LL |
| AF-MAAP1-RS-2004-00 | Tail Rotor Drive Shaft Assembly | 1 | BUY | 300M Steel, AMS 6417 | $95,000 | LL |
| AF-MAAP1-RS-2005-00 | Drive Shaft Coupling Set (6) | 1 | BUY | Ti-6Al-4V | $38,000 | ML |
| AF-MAAP1-RS-2010-00 | Tail Rotor Pitch Control System | 1 | BUY | Al/Steel Assembly | $85,000 | ML |
| AF-MAAP1-RS-2015-00 | Tail Rotor Balance Weight Set | 1 | BUY | Tungsten Alloy | $12,000 | SL |

**Sub-total Tail Rotor:** $785,000

#### 2.3 Rotor Control Linkages
**Drawing Reference:** AF-MAAP1-RS-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-RS-3001-00 | Cyclic Control Linkage Assembly | 1 | MAKE | 17-4PH Steel/Al 7075 | $125,000 | ML |
| AF-MAAP1-RS-3002-00 | Collective Control Linkage Assembly | 1 | MAKE | 17-4PH Steel/Al 7075 | $98,000 | ML |
| AF-MAAP1-RS-3003-00 | Tail Rotor Control Linkage Assembly | 1 | MAKE | 17-4PH Steel | $78,000 | ML |
| AF-MAAP1-RS-3010-00 | Servo Actuator - Cyclic (3) | 3 | BUY | Electrohydraulic | $285,000 | LL |
| AF-MAAP1-RS-3011-00 | Servo Actuator - Collective (1) | 1 | BUY | Electrohydraulic | $95,000 | LL |
| AF-MAAP1-RS-3012-00 | Servo Actuator - Tail Rotor (1) | 1 | BUY | Electrohydraulic | $95,000 | LL |
| AF-MAAP1-RS-3020-00 | Control Rod Set (22 pcs) | 1 | MAKE | 17-4PH Steel, AMS 5643 | $68,000 | SL |
| AF-MAAP1-RS-3025-00 | Rod End Bearing Set (44 pcs) | 1 | BUY | Spherical Bearing, Steel | $42,000 | ML |

**Sub-total Rotor Control Linkages:** $886,000

**TOTAL ROTOR SYSTEMS ASSEMBLY:** $3,731,500

---

### 3.0 PROPULSION SYSTEM ASSEMBLY (AF-MAAP1-PS)

#### 3.1 Main Engine Installation
**Drawing Reference:** AF-MAAP1-PS-1000-00  
**Quantity per Aircraft:** 2  
**Make/Buy:** ASSY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-PS-1001-00 | Turboshaft Engine (GE T700-GE-701D or equiv) | 2 | BUY | Complete Engine | $2,400,000 | LL |
| AF-MAAP1-PS-1002-00 | Engine Mount Assembly | 2 | MAKE | Ti-6Al-4V/Steel Hybrid | $125,000 | ML |
| AF-MAAP1-PS-1003-00 | Engine Firewall Shield | 2 | BUY | Inconel 625, AMS 5666 | $32,000 | ML |
| AF-MAAP1-PS-1004-00 | Engine Cowling Set (per engine) | 2 | BUY | Carbon Fiber/Kevlar | $68,000 | ML |
| AF-MAAP1-PS-1005-00 | Air Intake Assembly | 2 | BUY | Al 6061-T6/Composite | $95,000 | ML |
| AF-MAAP1-PS-1006-00 | Particle Separator System | 2 | BUY | Al/Steel Vane Assembly | $145,000 | LL |
| AF-MAAP1-PS-1010-00 | Engine Exhaust System | 2 | BUY | Inconel 718, AMS 5663 | $85,000 | ML |
| AF-MAAP1-PS-1011-00 | IR Suppressor Assembly | 2 | BUY | Inconel/Ceramic | $125,000 | LL |
| AF-MAAP1-PS-1015-00 | Engine Oil Cooler | 2 | BUY | Al Brazed Assembly | $42,000 | ML |
| AF-MAAP1-PS-1020-00 | Vibration Isolation Mount Set (8/engine) | 2 | BUY | Elastomeric/Steel | $28,000 | ML |

**Sub-total Main Engine Installation (2 engines):** $3,145,000

#### 3.2 Main Transmission Assembly
**Drawing Reference:** AF-MAAP1-PS-2000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-PS-2001-00 | Main Transmission (Combining Gearbox) | 1 | BUY | Magnesium Alloy Housing | $1,250,000 | LL |
| AF-MAAP1-PS-2002-00 | Transmission Mount Assembly | 1 | MAKE | Ti-6Al-4V Structure | $185,000 | ML |
| AF-MAAP1-PS-2003-00 | Input Module - Engine 1 | 1 | BUY | Steel Gears, AISI 9310 | $285,000 | LL |
| AF-MAAP1-PS-2004-00 | Input Module - Engine 2 | 1 | BUY | Steel Gears, AISI 9310 | $285,000 | LL |
| AF-MAAP1-PS-2005-00 | Accessory Gearbox | 1 | BUY | Magnesium Alloy | $195,000 | LL |
| AF-MAAP1-PS-2010-00 | Transmission Oil Cooler | 1 | BUY | Al Brazed Assembly | $85,000 | ML |
| AF-MAAP1-PS-2011-00 | Transmission Oil Pump | 1 | BUY | Al/Steel Assembly | $42,000 | ML |
| AF-MAAP1-PS-2015-00 | Chip Detector Assembly | 3 | BUY | Magnetic Sensor | $12,000 | SL |
| AF-MAAP1-PS-2020-00 | Transmission Mounts (4) | 1 | BUY | Elastomeric/Ti-6Al-4V | $45,000 | ML |

**Sub-total Main Transmission:** $2,384,000

#### 3.3 Auxiliary Power Unit (APU)
**Drawing Reference:** AF-MAAP1-PS-3000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-PS-3001-00 | APU (Allied Signal GTCP36-150 or equiv) | 1 | BUY | Complete APU | $325,000 | LL |
| AF-MAAP1-PS-3002-00 | APU Mount Assembly | 1 | MAKE | Al 7075-T7351 | $28,000 | SL |
| AF-MAAP1-PS-3003-00 | APU Firewall Shield | 1 | BUY | Inconel 625 | $18,000 | ML |
| AF-MAAP1-PS-3004-00 | APU Air Intake Assembly | 1 | BUY | Al 6061-T6 | $22,000 | ML |
| AF-MAAP1-PS-3005-00 | APU Exhaust Assembly | 1 | BUY | Inconel 718 | $32,000 | ML |
| AF-MAAP1-PS-3010-00 | APU Control Unit | 1 | BUY | Electronic Assembly | $45,000 | ML |

**Sub-total APU:** $470,000

#### 3.4 Fuel System
**Drawing Reference:** AF-MAAP1-PS-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-PS-4001-00 | Main Fuel Tank (Center Fuselage) | 1 | MAKE | Al 2024-T3 Sealed | $185,000 | ML |
| AF-MAAP1-PS-4002-00 | Auxiliary Fuel Tank (Optional) | 1 | MAKE | Al 2024-T3 Sealed | $125,000 | ML |
| AF-MAAP1-PS-4005-00 | Fuel Boost Pump - Main | 2 | BUY | Centrifugal Pump | $38,000 | ML |
| AF-MAAP1-PS-4006-00 | Fuel Boost Pump - Aux | 1 | BUY | Centrifugal Pump | $19,000 | ML |
| AF-MAAP1-PS-4010-00 | Fuel Control Unit | 2 | BUY | Electronic/Mechanical | $125,000 | LL |
| AF-MAAP1-PS-4015-00 | Fuel Filter Assembly | 4 | BUY | 10 Micron Filter | $12,000 | SL |
| AF-MAAP1-PS-4020-00 | Fuel Line Set (Rigid) | 1 | MAKE | CRES 321, AMS 5570 | $68,000 | SL |
| AF-MAAP1-PS-4021-00 | Fuel Line Set (Flexible) | 1 | BUY | MIL-PRF-27602 Hose | $28,000 | ML |
| AF-MAAP1-PS-4025-00 | Fuel Quantity Sensing System | 1 | BUY | Capacitance Probes | $85,000 | ML |
| AF-MAAP1-PS-4030-00 | Cross-Feed Valve Assembly | 1 | BUY | Solenoid Actuated | $42,000 | ML |
| AF-MAAP1-PS-4035-00 | Refuel/Defuel Panel | 1 | BUY | Al Housing Assembly | $32,000 | ML |

**Sub-total Fuel System:** $759,000

**TOTAL PROPULSION SYSTEM:** $6,758,000

---

### 4.0 FLIGHT CONTROL SYSTEM (AF-MAAP1-FC)

#### 4.1 Primary Flight Controls
**Drawing Reference:** AF-MAAP1-FC-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FC-1001-00 | Cyclic Control Stick Assembly - Pilot | 1 | BUY | Al 7075-T7351/Steel | $45,000 | ML |
| AF-MAAP1-FC-1002-00 | Cyclic Control Stick Assembly - Co-Pilot | 1 | BUY | Al 7075-T7351/Steel | $45,000 | ML |
| AF-MAAP1-FC-1003-00 | Collective Control Lever - Pilot | 1 | BUY | Al 7075-T7351 | $38,000 | ML |
| AF-MAAP1-FC-1004-00 | Collective Control Lever - Co-Pilot | 1 | BUY | Al 7075-T7351 | $38,000 | ML |
| AF-MAAP1-FC-1005-00 | Pedal Assembly - Pilot | 1 | BUY | Al 7075-T7351 | $28,000 | ML |
| AF-MAAP1-FC-1006-00 | Pedal Assembly - Co-Pilot | 1 | BUY | Al 7075-T7351 | $28,000 | ML |
| AF-MAAP1-FC-1010-00 | Flight Control Computer (FCC) - Primary | 2 | BUY | MIL-STD-1553B | $425,000 | LL |
| AF-MAAP1-FC-1011-00 | Flight Control Computer (FCC) - Backup | 1 | BUY | MIL-STD-1553B | $212,500 | LL |
| AF-MAAP1-FC-1015-00 | Control Position Transducer Set (12) | 1 | BUY | RVDT Sensors | $95,000 | ML |
| AF-MAAP1-FC-1020-00 | Force Gradient System | 1 | BUY | Electromechanical | $125,000 | ML |
| AF-MAAP1-FC-1025-00 | Control Mixing Unit | 1 | BUY | Electronic Assembly | $185,000 | LL |
| AF-MAAP1-FC-1030-00 | Automatic Flight Control System (AFCS) | 1 | BUY | 4-Axis Autopilot | $685,000 | LL |
| AF-MAAP1-FC-1035-00 | Stability Augmentation System (SAS) | 1 | BUY | Electronic Assembly | $385,000 | LL |

**Sub-total Primary Flight Controls:** $2,334,500

#### 4.2 Secondary Flight Controls
**Drawing Reference:** AF-MAAP1-FC-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FC-2001-00 | Aileron Assembly - Left | 1 | MAKE | Al 7075-T6 | $85,000 | ML |
| AF-MAAP1-FC-2002-00 | Aileron Assembly - Right | 1 | MAKE | Al 7075-T6 | $85,000 | ML |
| AF-MAAP1-FC-2003-00 | Flap Assembly - Left Inboard | 1 | MAKE | Al 7075-T6 | $125,000 | ML |
| AF-MAAP1-FC-2004-00 | Flap Assembly - Left Outboard | 1 | MAKE | Al 7075-T6 | $95,000 | ML |
| AF-MAAP1-FC-2005-00 | Flap Assembly - Right Inboard | 1 | MAKE | Al 7075-T6 | $125,000 | ML |
| AF-MAAP1-FC-2006-00 | Flap Assembly - Right Outboard | 1 | MAKE | Al 7075-T6 | $95,000 | ML |
| AF-MAAP1-FC-2010-00 | Aileron Actuator | 2 | BUY | Electrohydraulic | $125,000 | LL |
| AF-MAAP1-FC-2011-00 | Flap Actuator | 4 | BUY | Electrohydraulic | $185,000 | LL |
| AF-MAAP1-FC-2015-00 | Trim Tab Assembly - Elevator (2) | 1 | MAKE | Al 7075-T6 | $42,000 | ML |
| AF-MAAP1-FC-2016-00 | Trim Tab Assembly - Rudder | 1 | MAKE | Al 7075-T6 | $28,000 | ML |
| AF-MAAP1-FC-2020-00 | Trim Actuator Set (3) | 1 | BUY | Electric Motor | $45,000 | ML |

**Sub-total Secondary Flight Controls:** $1,035,000

#### 4.3 Hydraulic System
**Drawing Reference:** AF-MAAP1-FC-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FC-3001-00 | Hydraulic Pump - Primary System | 2 | BUY | Variable Displacement | $95,000 | ML |
| AF-MAAP1-FC-3002-00 | Hydraulic Pump - Backup System | 1 | BUY | Fixed Displacement | $58,000 | ML |
| AF-MAAP1-FC-3005-00 | Hydraulic Reservoir - Primary | 1 | BUY | Al 6061-T6, 5 gal | $22,000 | ML |
| AF-MAAP1-FC-3006-00 | Hydraulic Reservoir - Backup | 1 | BUY | Al 6061-T6, 3 gal | $18,000 | ML |
| AF-MAAP1-FC-3010-00 | Hydraulic Accumulator (4000 psi) | 4 | BUY | Steel Pressure Vessel | $42,000 | ML |
| AF-MAAP1-FC-3015-00 | Hydraulic Filter Assembly | 4 | BUY | 10 Micron Filter | $18,000 | SL |
| AF-MAAP1-FC-3020-00 | Hydraulic Line Set (Rigid) | 1 | MAKE | CRES 321, AMS 5570 | $125,000 | SL |
| AF-MAAP1-FC-3021-00 | Hydraulic Hose Set (Flexible) | 1 | BUY | MIL-PRF-83282 Hose | $68,000 | ML |
| AF-MAAP1-FC-3025-00 | System Control Valve Manifold | 2 | BUY | Al/Steel Assembly | $145,000 | ML |
| AF-MAAP1-FC-3030-00 | Pressure Transducer Set (12) | 1 | BUY | Electronic Sensor | $28,000 | SL |
| AF-MAAP1-FC-3035-00 | Heat Exchanger (Hydraulic) | 2 | BUY | Al Brazed Core | $58,000 | ML |

**Sub-total Hydraulic System:** $677,000

**TOTAL FLIGHT CONTROL SYSTEM:** $4,046,500

---

### 5.0 LANDING GEAR SYSTEM (AF-MAAP1-LG)

#### 5.1 Nose Landing Gear
**Drawing Reference:** AF-MAAP1-LG-1000-00  
**Quantity per Aircraft:** 1  
**Make/Buy:** ASSY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-LG-1001-00 | Nose Landing Gear Strut Assembly | 1 | BUY | 300M Steel/Al 7075 | $185,000 | LL |
| AF-MAAP1-LG-1002-00 | Nose Wheel Assembly (2 wheels) | 1 | BUY | Forged Al Wheel/Tire | $42,000 | ML |
| AF-MAAP1-LG-1003-00 | Nose Gear Shock Strut | 1 | BUY | 4340 Steel, AMS 6414 | $95,000 | LL |
| AF-MAAP1-LG-1004-00 | Nose Gear Retraction Actuator | 1 | BUY | Electrohydraulic | $125,000 | LL |
| AF-MAAP1-LG-1005-00 | Steering Actuator | 1 | BUY | Electrohydraulic | $85,000 | LL |
| AF-MAAP1-LG-1010-00 | Nose Gear Door Set (2 doors) | 1 | MAKE | Al 7075-T6 | $32,000 | ML |
| AF-MAAP1-LG-1011-00 | Door Actuator Set (2) | 1 | BUY | Electric Motor | $28,000 | ML |
| AF-MAAP1-LG-1015-00 | Brake Assembly (Nose Wheel) | 1 | BUY | Carbon-Carbon Disc | $68,000 | ML |
| AF-MAAP1-LG-1020-00 | Position Sensor Set (6) | 1 | BUY | Proximity Sensor | $18,000 | SL |

**Sub-total Nose Landing Gear:** $678,000

#### 5.2 Main Landing Gear
**Drawing Reference:** AF-MAAP1-LG-2000-00  
**Quantity per Aircraft:** 2 (Left & Right)  
**Make/Buy:** ASSY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-LG-2001-00 | Main Landing Gear Strut Assembly | 2 | BUY | 300M Steel/Ti-6Al-4V | $425,000 | LL |
| AF-MAAP1-LG-2002-00 | Main Wheel Assembly (2 wheels/strut) | 2 | BUY | Forged Al Wheel/Tire | $125,000 | ML |
| AF-MAAP1-LG-2003-00 | Main Gear Shock Strut | 2 | BUY | 4340 Steel, AMS 6414 | $285,000 | LL |
| AF-MAAP1-LG-2004-00 | Main Gear Retraction Actuator | 2 | BUY | Electrohydraulic | $285,000 | LL |
| AF-MAAP1-LG-2005-00 | Side Brace Assembly | 2 | BUY | 300M Steel | $85,000 | ML |
| AF-MAAP1-LG-2010-00 | Main Gear Door Set (4 doors total) | 1 | MAKE | Al 7075-T6 | $68,000 | ML |
| AF-MAAP1-LG-2011-00 | Door Actuator Set (4) | 1 | BUY | Electric Motor | $58,000 | ML |
| AF-MAAP1-LG-2015-00 | Brake Assembly (Per Wheel, 4 total) | 1 | BUY | Carbon-Carbon Disc | $285,000 | ML |
| AF-MAAP1-LG-2020-00 | Anti-Skid Control Unit | 1 | BUY | Electronic Assembly | $125,000 | LL |
| AF-MAAP1-LG-2025-00 | Position Sensor Set (12) | 1 | BUY | Proximity Sensor | $32,000 | SL |
| AF-MAAP1-LG-2030-00 | Weight-On-Wheels Switch Set (3) | 1 | BUY | Pressure Switch | $12,000 | SL |

**Sub-total Main Landing Gear (Both Sides):** $1,785,000

**TOTAL LANDING GEAR SYSTEM:** $2,463,000

---

### 6.0 AVIONICS & MISSION SYSTEMS (AF-MAAP1-AV)

#### 6.1 Core Avionics Suite
**Drawing Reference:** AF-MAAP1-AV-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AV-1001-00 | Integrated Modular Avionics (IMA) Core | 2 | BUY | MIL-STD-1553B/ARINC 653 | $825,000 | LL |
| AF-MAAP1-AV-1002-00 | Mission Computer | 2 | BUY | Dual Redundant | $625,000 | LL |
| AF-MAAP1-AV-1003-00 | Digital Map Generator | 1 | BUY | Terrain Database | $185,000 | LL |
| AF-MAAP1-AV-1005-00 | Data Transfer Unit | 1 | BUY | Removable Storage | $42,000 | ML |
| AF-MAAP1-AV-1010-00 | Air Data Computer | 2 | BUY | Dual Redundant | $185,000 | LL |
| AF-MAAP1-AV-1011-00 | Attitude Heading Reference System (AHRS) | 2 | BUY | Laser Gyro | $385,000 | LL |
| AF-MAAP1-AV-1012-00 | GPS/INS Unit | 2 | BUY | Military Grade | $425,000 | LL |
| AF-MAAP1-AV-1015-00 | Radar Altimeter | 2 | BUY | Dual Antenna | $125,000 | ML |
| AF-MAAP1-AV-1020-00 | Transponder (IFF) | 1 | BUY | Mode 5 Capable | $285,000 | LL |
| AF-MAAP1-AV-1025-00 | Traffic Collision Avoidance System (TCAS) | 1 | BUY | TCAS II | $185,000 | LL |
| AF-MAAP1-AV-1030-00 | Engine Instrument & Crew Alerting System | 1 | BUY | Integrated Display | $225,000 | LL |

**Sub-total Core Avionics:** $3,492,000

#### 6.2 Communications Systems
**Drawing Reference:** AF-MAAP1-AV-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AV-2001-00 | VHF/UHF Radio Transceiver | 2 | BUY | Dual Comm | $185,000 | LL |
| AF-MAAP1-AV-2002-00 | HF Radio Transceiver | 1 | BUY | Long Range | $125,000 | LL |
| AF-MAAP1-AV-2003-00 | SATCOM Terminal | 1 | BUY | Ku-Band | $385,000 | LL |
| AF-MAAP1-AV-2004-00 | Secure Voice System | 1 | BUY | Type 1 Encryption | $425,000 | LL |
| AF-MAAP1-AV-2005-00 | Intercom System | 1 | BUY | 8-Station | $85,000 | ML |
| AF-MAAP1-AV-2010-00 | Audio Management Unit | 2 | BUY | Dual Redundant | $125,000 | ML |
| AF-MAAP1-AV-2015-00 | Data Link System | 1 | BUY | Link 16 Capable | $625,000 | LL |
| AF-MAAP1-AV-2020-00 | VHF Antenna Set | 1 | BUY | Blade Antenna | $28,000 | ML |
| AF-MAAP1-AV-2021-00 | UHF Antenna Set | 1 | BUY | Blade Antenna | $28,000 | ML |
| AF-MAAP1-AV-2022-00 | HF Antenna | 1 | BUY | Wire Antenna | $12,000 | ML |
| AF-MAAP1-AV-2023-00 | SATCOM Antenna | 1 | BUY | Steerable Dish | $125,000 | LL |

**Sub-total Communications:** $2,148,000

#### 6.3 Navigation Systems
**Drawing Reference:** AF-MAAP1-AV-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AV-3001-00 | Flight Management System (FMS) | 2 | BUY | Dual Redundant | $525,000 | LL |
| AF-MAAP1-AV-3002-00 | Multi-Function Display (MFD) - Pilot | 2 | BUY | 10" Color LCD | $285,000 | LL |
| AF-MAAP1-AV-3003-00 | Multi-Function Display (MFD) - Co-Pilot | 2 | BUY | 10" Color LCD | $285,000 | LL |
| AF-MAAP1-AV-3004-00 | Primary Flight Display (PFD) - Pilot | 1 | BUY | 8" Color LCD | $125,000 | LL |
| AF-MAAP1-AV-3005-00 | Primary Flight Display (PFD) - Co-Pilot | 1 | BUY | 8" Color LCD | $125,000 | LL |
| AF-MAAP1-AV-3010-00 | Control Display Unit (CDU) - Pilot | 1 | BUY | Keyboard Interface | $85,000 | ML |
| AF-MAAP1-AV-3011-00 | Control Display Unit (CDU) - Co-Pilot | 1 | BUY | Keyboard Interface | $85,000 | ML |
| AF-MAAP1-AV-3015-00 | Head-Up Display (HUD) - Pilot | 1 | BUY | Wide FOV | $425,000 | LL |
| AF-MAAP1-AV-3020-00 | Weather Radar | 1 | BUY | X-Band, 180° Scan | $385,000 | LL |
| AF-MAAP1-AV-3025-00 | Terrain Awareness Warning System (TAWS) | 1 | BUY | Enhanced GPWS | $185,000 | LL |

**Sub-total Navigation Systems:** $2,510,000

#### 6.4 Cockpit Equipment
**Drawing Reference:** AF-MAAP1-AV-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AV-4001-00 | Pilot Seat - Crashworthy | 1 | BUY | Composite/Steel | $85,000 | ML |
| AF-MAAP1-AV-4002-00 | Co-Pilot Seat - Crashworthy | 1 | BUY | Composite/Steel | $85,000 | ML |
| AF-MAAP1-AV-4003-00 | Crew Seat - Aft (Mission Operator) | 2 | BUY | Composite/Steel | $125,000 | ML |
| AF-MAAP1-AV-4005-00 | Instrument Panel Assembly - Pilot | 1 | MAKE | Al 7075-T6 Structure | $42,000 | ML |
| AF-MAAP1-AV-4006-00 | Instrument Panel Assembly - Co-Pilot | 1 | MAKE | Al 7075-T6 Structure | $42,000 | ML |
| AF-MAAP1-AV-4010-00 | Center Console Assembly | 1 | MAKE | Al/Composite | $68,000 | ML |
| AF-MAAP1-AV-4015-00 | Overhead Panel Assembly | 1 | MAKE | Al/Composite | $52,000 | ML |
| AF-MAAP1-AV-4020-00 | Windscreen Assembly (5-piece) | 1 | BUY | Polycarbonate/Glass | $185,000 | ML |
| AF-MAAP1-AV-4021-00 | Side Window Assembly - Left (2) | 1 | BUY | Polycarbonate | $42,000 | ML |
| AF-MAAP1-AV-4022-00 | Side Window Assembly - Right (2) | 1 | BUY | Polycarbonate | $42,000 | ML |
| AF-MAAP1-AV-4025-00 | Door Assembly - Pilot | 1 | MAKE | Al 7075-T6/Composite | $125,000 | ML |
| AF-MAAP1-AV-4026-00 | Door Assembly - Co-Pilot | 1 | MAKE | Al 7075-T6/Composite | $125,000 | ML |
| AF-MAAP1-AV-4030-00 | Cabin Door Assembly - Sliding (2) | 1 | MAKE | Al 7075-T6/Composite | $185,000 | ML |
| AF-MAAP1-AV-4035-00 | Interior Lighting System | 1 | BUY | LED System | $45,000 | SL |
| AF-MAAP1-AV-4040-00 | Environmental Control Panel | 1 | BUY | Electronic Interface | $28,000 | ML |

**Sub-total Cockpit Equipment:** $1,276,000

#### 6.5 Mission Systems Core (Common)
**Drawing Reference:** AF-MAAP1-AV-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AV-5001-00 | Mission Management System | 1 | BUY | Integrated Processor | $525,000 | LL |
| AF-MAAP1-AV-5002-00 | Tactical Situation Display | 2 | BUY | 15" Touchscreen | $285,000 | LL |
| AF-MAAP1-AV-5003-00 | Video Management System | 1 | BUY | Multi-Channel | $185,000 | LL |
| AF-MAAP1-AV-5004-00 | Data Recording System | 1 | BUY | 2TB Solid State | $125,000 | ML |
| AF-MAAP1-AV-5005-00 | Mission Data Loader | 1 | BUY | Portable Unit | $42,000 | ML |
| AF-MAAP1-AV-5010-00 | EO/IR Sensor Turret (Basic) | 1 | BUY | Multi-Spectral | $625,000 | LL |
| AF-MAAP1-AV-5015-00 | Laser Designator/Rangefinder | 1 | BUY | Integrated in Turret | $385,000 | LL |
| AF-MAAP1-AV-5020-00 | Moving Map Display - Mission Operator | 2 | BUY | 12" Touchscreen | $185,000 | ML |

**Sub-total Mission Systems Core:** $2,357,000

**TOTAL AVIONICS & MISSION SYSTEMS (COMMON):** $11,783,000

---

### 7.0 ELECTRICAL POWER SYSTEM (AF-MAAP1-EP)

#### 7.1 Power Generation
**Drawing Reference:** AF-MAAP1-EP-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EP-1001-00 | Starter/Generator - Engine 1 | 1 | BUY | 40 kVA, 3-Phase AC | $125,000 | LL |
| AF-MAAP1-EP-1002-00 | Starter/Generator - Engine 2 | 1 | BUY | 40 kVA, 3-Phase AC | $125,000 | LL |
| AF-MAAP1-EP-1003-00 | APU Generator | 1 | BUY | 30 kVA, 3-Phase AC | $85,000 | LL |
| AF-MAAP1-EP-1005-00 | Generator Control Unit | 3 | BUY | Electronic Regulator | $125,000 | ML |
| AF-MAAP1-EP-1010-00 | Emergency Generator (Ram Air Turbine) | 1 | BUY | 15 kVA Hydraulic Drive | $185,000 | LL |

**Sub-total Power Generation:** $645,000

#### 7.2 Power Distribution
**Drawing Reference:** AF-MAAP1-EP-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EP-2001-00 | Main Power Distribution Panel | 1 | MAKE | Al Enclosure/Bus Bars | $125,000 | ML |
| AF-MAAP1-EP-2002-00 | Essential Bus Distribution Panel | 1 | MAKE | Al Enclosure/Bus Bars | $85,000 | ML |
| AF-MAAP1-EP-2003-00 | AC to DC Converter (28VDC) |
| AF-MAAP1-EP-2003-00 | AC to DC Converter (28VDC) | 3 | BUY | 200A Solid State | $75,000 | ML |
| AF-MAAP1-EP-2004-00 | Battery Charger Unit | 2 | BUY | Smart Charging System | $32,000 | ML |
| AF-MAAP1-EP-2005-00 | Circuit Breaker Panel - Primary | 1 | BUY | Remote Control CBs | $65,000 | ML |
| AF-MAAP1-EP-2006-00 | Circuit Breaker Panel - Secondary | 1 | BUY | Remote Control CBs | $45,000 | ML |
| AF-MAAP1-EP-2010-00 | Bus Tie Contactor Assembly | 3 | BUY | High Current Relay | $42,000 | ML |
| AF-MAAP1-EP-2015-00 | Ground Power Receptacle | 1 | BUY | 400Hz AC Compatible | $12,000 | SL |
| AF-MAAP1-EP-2020-00 | External Power Control Unit | 1 | BUY | Auto Transfer Switch | $28,000 | ML |

**Sub-total Power Distribution:** $509,000

#### 7.3 Emergency Power
**Drawing Reference:** AF-MAAP1-EP-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EP-3001-00 | Main Battery Assembly (28VDC) | 2 | BUY | 50Ah NiCd | $85,000 | ML |
| AF-MAAP1-EP-3002-00 | Emergency Battery Assembly | 1 | BUY | 25Ah NiCd | $32,000 | ML |
| AF-MAAP1-EP-3003-00 | Battery Box Assembly - Main | 2 | MAKE | Ti Alloy Fire-Resistant | $38,000 | ML |
| AF-MAAP1-EP-3004-00 | Battery Box Assembly - Emergency | 1 | MAKE | Ti Alloy Fire-Resistant | $18,000 | ML |
| AF-MAAP1-EP-3005-00 | Battery Temperature Management | 3 | BUY | Active Cooling System | $45,000 | ML |
| AF-MAAP1-EP-3010-00 | Static Inverter (Emergency) | 1 | BUY | 5 kVA 115VAC Output | $65,000 | ML |

**Sub-total Emergency Power:** $283,000

#### 7.4 Wiring & Interconnect
**Drawing Reference:** AF-MAAP1-EP-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EP-4001-00 | Main Wiring Harness - Forward Fuselage | 1 | MAKE | MIL-W-22759 | $125,000 | LL |
| AF-MAAP1-EP-4002-00 | Main Wiring Harness - Center Fuselage | 1 | MAKE | MIL-W-22759 | $145,000 | LL |
| AF-MAAP1-EP-4003-00 | Main Wiring Harness - Aft Fuselage | 1 | MAKE | MIL-W-22759 | $95,000 | LL |
| AF-MAAP1-EP-4005-00 | Wing Wiring Harness - Left | 1 | MAKE | MIL-W-22759 | $85,000 | LL |
| AF-MAAP1-EP-4006-00 | Wing Wiring Harness - Right | 1 | MAKE | MIL-W-22759 | $85,000 | LL |
| AF-MAAP1-EP-4010-00 | Engine Wiring Harness - No.1 | 1 | MAKE | High-Temp MIL-W-22759 | $45,000 | ML |
| AF-MAAP1-EP-4011-00 | Engine Wiring Harness - No.2 | 1 | MAKE | High-Temp MIL-W-22759 | $45,000 | ML |
| AF-MAAP1-EP-4015-00 | APU Wiring Harness | 1 | MAKE | High-Temp MIL-W-22759 | $28,000 | ML |
| AF-MAAP1-EP-4020-00 | Avionics Bay Interconnect Harness | 1 | MAKE | MIL-W-22759 | $65,000 | ML |
| AF-MAAP1-EP-4025-00 | Cockpit Wiring Harness | 1 | MAKE | MIL-W-22759 | $75,000 | ML |
| AF-MAAP1-EP-4030-00 | Data Bus Wiring (MIL-STD-1553) | 1 | MAKE | Dual Redundant | $125,000 | ML |
| AF-MAAP1-EP-4035-00 | Fiber Optic Bus Wiring | 1 | MAKE | High-Speed Data | $185,000 | LL |

**Sub-total Wiring & Interconnect:** $1,103,000

#### 7.5 Lighting Systems
**Drawing Reference:** AF-MAAP1-EP-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EP-5001-00 | Position Lights (Wingtip) | 2 | BUY | LED Nav Lights | $18,000 | ML |
| AF-MAAP1-EP-5002-00 | Anti-Collision Beacon (Top) | 1 | BUY | Red LED Strobe | $8,500 | SL |
| AF-MAAP1-EP-5003-00 | Anti-Collision Beacon (Bottom) | 1 | BUY | Red LED Strobe | $8,500 | SL |
| AF-MAAP1-EP-5005-00 | Formation Lights | 8 | BUY | NVG-Compatible LED | $32,000 | ML |
| AF-MAAP1-EP-5010-00 | Landing Light Assembly - Nose | 1 | BUY | 600W LED Retractable | $42,000 | ML |
| AF-MAAP1-EP-5011-00 | Landing Light Assembly - Wing | 2 | BUY | 400W LED | $45,000 | ML |
| AF-MAAP1-EP-5015-00 | Taxi Light Assembly | 1 | BUY | LED Articulating | $18,000 | ML |
| AF-MAAP1-EP-5020-00 | Ice Inspection Lights | 2 | BUY | Wing Leading Edge LED | $12,000 | SL |
| AF-MAAP1-EP-5025-00 | Cabin Lighting System | 1 | BUY | LED Dimming System | $28,000 | SL |
| AF-MAAP1-EP-5030-00 | Emergency Exit Lighting | 1 | BUY | Battery Backup LED | $15,000 | SL |
| AF-MAAP1-EP-5035-00 | Cargo Bay Lighting | 1 | BUY | LED High Output | $22,000 | SL |

**Sub-total Lighting Systems:** $249,000

**TOTAL ELECTRICAL POWER SYSTEM:** $2,789,000

---

### 8.0 HYDRAULIC SYSTEM (AF-MAAP1-HY)

#### 8.1 Hydraulic Power Generation
**Drawing Reference:** AF-MAAP1-HY-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-HY-1001-00 | Engine-Driven Pump - System A | 1 | BUY | 3000 PSI Variable Disp. | $125,000 | LL |
| AF-MAAP1-HY-1002-00 | Engine-Driven Pump - System B | 1 | BUY | 3000 PSI Variable Disp. | $125,000 | LL |
| AF-MAAP1-HY-1005-00 | Electric Motor Pump - Backup | 1 | BUY | 3000 PSI, 28VDC | $85,000 | LL |
| AF-MAAP1-HY-1010-00 | Ram Air Turbine Hydraulic Pump | 1 | BUY | Emergency 3000 PSI | $145,000 | LL |
| AF-MAAP1-HY-1015-00 | Ground Service Pump Receptacle | 1 | BUY | Quick-Disconnect | $8,500 | SL |

**Sub-total Hydraulic Power Generation:** $488,500

#### 8.2 Hydraulic Distribution & Control
**Drawing Reference:** AF-MAAP1-HY-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-HY-2001-00 | Hydraulic Manifold - System A | 1 | MAKE | 316 Stainless Steel | $65,000 | ML |
| AF-MAAP1-HY-2002-00 | Hydraulic Manifold - System B | 1 | MAKE | 316 Stainless Steel | $65,000 | ML |
| AF-MAAP1-HY-2005-00 | Priority Valve Assembly | 2 | BUY | Flow Management | $32,000 | ML |
| AF-MAAP1-HY-2010-00 | Pressure Regulator - System A | 1 | BUY | 3000 PSI Relief | $18,000 | ML |
| AF-MAAP1-HY-2011-00 | Pressure Regulator - System B | 1 | BUY | 3000 PSI Relief | $18,000 | ML |
| AF-MAAP1-HY-2015-00 | Hydraulic Filter Assembly | 4 | BUY | 10 Micron Beta 1000 | $28,000 | ML |
| AF-MAAP1-HY-2020-00 | Flow Control Valve Assembly | 6 | BUY | Servo-Controlled | $75,000 | ML |
| AF-MAAP1-HY-2025-00 | Check Valve Assembly | 12 | BUY | High-Pressure | $18,000 | SL |
| AF-MAAP1-HY-2030-00 | Shuttle Valve Assembly | 4 | BUY | Dual System | $12,000 | SL |

**Sub-total Hydraulic Distribution:** $331,000

#### 8.3 Reservoirs & Accumulators
**Drawing Reference:** AF-MAAP1-HY-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-HY-3001-00 | Hydraulic Reservoir - System A | 1 | BUY | 10 Gal Pressurized | $42,000 | ML |
| AF-MAAP1-HY-3002-00 | Hydraulic Reservoir - System B | 1 | BUY | 10 Gal Pressurized | $42,000 | ML |
| AF-MAAP1-HY-3005-00 | Accumulator - Landing Gear | 2 | BUY | 3000 PSI Nitrogen | $28,000 | ML |
| AF-MAAP1-HY-3006-00 | Accumulator - Flight Controls | 4 | BUY | 3000 PSI Nitrogen | $48,000 | ML |
| AF-MAAP1-HY-3010-00 | Reservoir Quantity Sensor | 2 | BUY | Capacitance Type | $8,500 | SL |
| AF-MAAP1-HY-3015-00 | Reservoir Pressurization Valve | 2 | BUY | Bleed Air Regulated | $12,000 | ML |

**Sub-total Reservoirs & Accumulators:** $180,500

#### 8.4 Hydraulic Lines & Fittings
**Drawing Reference:** AF-MAAP1-HY-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-HY-4001-00 | High-Pressure Line Assembly - Forward | 1 | MAKE | 316 SS Tube/MS Fittings | $85,000 | ML |
| AF-MAAP1-HY-4002-00 | High-Pressure Line Assembly - Center | 1 | MAKE | 316 SS Tube/MS Fittings | $95,000 | ML |
| AF-MAAP1-HY-4003-00 | High-Pressure Line Assembly - Aft | 1 | MAKE | 316 SS Tube/MS Fittings | $75,000 | ML |
| AF-MAAP1-HY-4005-00 | Return Line Assembly - Complete | 1 | MAKE | 316 SS Tube/MS Fittings | $65,000 | ML |
| AF-MAAP1-HY-4010-00 | Flexible Hose Assembly - Flight Control | 24 | BUY | MIL-H-8794 PTFE | $72,000 | ML |
| AF-MAAP1-HY-4015-00 | Flexible Hose Assembly - Landing Gear | 12 | BUY | MIL-H-8794 PTFE | $42,000 | ML |
| AF-MAAP1-HY-4020-00 | Quick-Disconnect Coupling | 18 | BUY | Self-Sealing | $28,000 | SL |

**Sub-total Hydraulic Lines & Fittings:** $462,000

#### 8.5 Hydraulic System Instrumentation
**Drawing Reference:** AF-MAAP1-HY-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-HY-5001-00 | Pressure Transducer - System A | 3 | BUY | 0-5000 PSI | $12,000 | ML |
| AF-MAAP1-HY-5002-00 | Pressure Transducer - System B | 3 | BUY | 0-5000 PSI | $12,000 | ML |
| AF-MAAP1-HY-5005-00 | Temperature Sensor | 4 | BUY | -40°C to +150°C | $8,500 | SL |
| AF-MAAP1-HY-5010-00 | Flow Meter Assembly | 2 | BUY | Digital Output | $18,000 | ML |
| AF-MAAP1-HY-5015-00 | Filter Contamination Indicator | 4 | BUY | Visual/Electronic | $12,000 | SL |
| AF-MAAP1-HY-5020-00 | Hydraulic System Monitor Unit | 1 | BUY | Integrated Display | $42,000 | ML |

**Sub-total Hydraulic Instrumentation:** $104,500

**TOTAL HYDRAULIC SYSTEM:** $1,566,500

---

### 9.0 ENVIRONMENTAL CONTROL SYSTEM (AF-MAAP1-EC)

#### 9.1 Air Conditioning & Pressurization
**Drawing Reference:** AF-MAAP1-EC-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-1001-00 | Air Cycle Machine (ACM) | 2 | BUY | Bootstrap System | $285,000 | LL |
| AF-MAAP1-EC-1002-00 | Primary Heat Exchanger | 2 | BUY | Ram Air Cooled | $85,000 | LL |
| AF-MAAP1-EC-1003-00 | Secondary Heat Exchanger | 2 | BUY | Ram Air Cooled | $65,000 | LL |
| AF-MAAP1-EC-1005-00 | Water Separator | 2 | BUY | Centrifugal Type | $42,000 | ML |
| AF-MAAP1-EC-1010-00 | Cabin Pressure Controller | 1 | BUY | Digital Auto Control | $85,000 | LL |
| AF-MAAP1-EC-1015-00 | Outflow Valve Assembly | 2 | BUY | Motor-Driven | $65,000 | ML |
| AF-MAAP1-EC-1020-00 | Safety Valve - Positive Relief | 2 | BUY | 9.0 PSI Diff | $18,000 | ML |
| AF-MAAP1-EC-1021-00 | Safety Valve - Negative Relief | 2 | BUY | -0.5 PSI Diff | $12,000 | ML |
| AF-MAAP1-EC-1025-00 | Ram Air Scoop Assembly | 2 | MAKE | Al 7075-T6 | $28,000 | ML |
| AF-MAAP1-EC-1030-00 | Ram Air Modulating Door | 2 | MAKE | Al 7075-T6/Actuator | $32,000 | ML |

**Sub-total Air Conditioning & Pressurization:** $717,000

#### 9.2 Bleed Air System
**Drawing Reference:** AF-MAAP1-EC-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-2001-00 | Bleed Air Manifold Assembly | 1 | MAKE | 316 Stainless Steel | $65,000 | ML |
| AF-MAAP1-EC-2002-00 | Engine Bleed Air Valve - No.1 | 1 | BUY | High-Temp Shutoff | $32,000 | ML |
| AF-MAAP1-EC-2003-00 | Engine Bleed Air Valve - No.2 | 1 | BUY | High-Temp Shutoff | $32,000 | ML |
| AF-MAAP1-EC-2005-00 | Pressure Regulating Valve | 2 | BUY | PRV with Relief | $28,000 | ML |
| AF-MAAP1-EC-2010-00 | Bleed Air Precooler | 2 | BUY | Fuel-Cooled HX | $85,000 | ML |
| AF-MAAP1-EC-2015-00 | Overheat Detection System | 1 | BUY | Loop System | $42,000 | ML |
| AF-MAAP1-EC-2020-00 | APU Bleed Air Valve | 1 | BUY | High-Temp Shutoff | $32,000 | ML |
| AF-MAAP1-EC-2025-00 | Cross-Bleed Valve | 1 | BUY | Dual-System Isolation | $28,000 | ML |

**Sub-total Bleed Air System:** $344,000

#### 9.3 Oxygen System
**Drawing Reference:** AF-MAAP1-EC-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-3001-00 | Oxygen Cylinder Assembly (Crew) | 1 | BUY | 115 Cu Ft @ 1850 PSI | $42,000 | ML |
| AF-MAAP1-EC-3002-00 | Oxygen Cylinder Assembly (Passenger) | 1 | BUY | 76 Cu Ft @ 1850 PSI | $32,000 | ML |
| AF-MAAP1-EC-3005-00 | Oxygen Regulator - Crew | 4 | BUY | Demand Type | $28,000 | ML |
| AF-MAAP1-EC-3006-00 | Oxygen Mask - Crew | 4 | BUY | Quick-Don Type | $18,000 | ML |
| AF-MAAP1-EC-3010-00 | Passenger Oxygen Mask Assembly | 16 | BUY | Drop-Down Chemical | $32,000 | ML |
| AF-MAAP1-EC-3015-00 | Oxygen Service Panel | 1 | MAKE | External Access | $8,500 | SL |
| AF-MAAP1-EC-3020-00 | Oxygen Distribution Manifold | 1 | MAKE | 316 Stainless Steel | $18,000 | ML |
| AF-MAAP1-EC-3025-00 | Pressure Gauge & Shutoff Valve | 2 | BUY | 0-2500 PSI | $8,500 | SL |

**Sub-total Oxygen System:** $187,000

#### 9.4 Heating & Ventilation
**Drawing Reference:** AF-MAAP1-EC-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-4001-00 | Cabin Air Distribution System | 1 | MAKE | Al Ducting/Diffusers | $85,000 | ML |
| AF-MAAP1-EC-4002-00 | Cockpit Air Distribution System | 1 | MAKE | Al Ducting/Diffusers | $42,000 | ML |
| AF-MAAP1-EC-4005-00 | Recirculation Fan Assembly | 2 | BUY | Variable Speed | $28,000 | ML |
| AF-MAAP1-EC-4010-00 | HEPA Filter Assembly | 2 | BUY | 99.97% @ 0.3 Micron | $18,000 | ML |
| AF-MAAP1-EC-4015-00 | Temperature Control Valve | 4 | BUY | Electrically Actuated | $32,000 | ML |
| AF-MAAP1-EC-4020-00 | Windshield Demist Nozzle | 4 | BUY | High-Flow | $8,500 | SL |
| AF-MAAP1-EC-4025-00 | Personnel Air Outlet | 24 | BUY | Individual Control | $28,000 | SL |
| AF-MAAP1-EC-4030-00 | Avionics Cooling System | 1 | BUY | Dedicated Loop | $125,000 | ML |

**Sub-total Heating & Ventilation:** $366,500

#### 9.5 Anti-Ice & De-Ice Systems
**Drawing Reference:** AF-MAAP1-EC-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-5001-00 | Wing Leading Edge Thermal Anti-Ice | 2 | MAKE | Bleed Air Piccolo Tube | $185,000 | ML |
| AF-MAAP1-EC-5002-00 | Horizontal Stabilizer Anti-Ice | 2 | MAKE | Bleed Air Piccolo Tube | $85,000 | ML |
| AF-MAAP1-EC-5003-00 | Vertical Stabilizer Anti-Ice | 1 | MAKE | Bleed Air Piccolo Tube | $42,000 | ML |
| AF-MAAP1-EC-5005-00 | Engine Inlet Anti-Ice System | 2 | BUY | Integrated with Engine | $125,000 | LL |
| AF-MAAP1-EC-5010-00 | Windshield Anti-Ice System | 2 | BUY | Electrical Heating | $85,000 | ML |
| AF-MAAP1-EC-5011-00 | Side Window Anti-Fog System | 4 | BUY | Hot Air Circulation | $32,000 | ML |
| AF-MAAP1-EC-5015-00 | Pitot Tube Heater | 3 | BUY | Electrical 28VDC | $12,000 | SL |
| AF-MAAP1-EC-5016-00 | Static Port Heater | 6 | BUY | Electrical 28VDC | $12,000 | SL |
| AF-MAAP1-EC-5017-00 | AOA Sensor Heater | 2 | BUY | Electrical 28VDC | $8,500 | SL |
| AF-MAAP1-EC-5020-00 | Ice Detection System | 2 | BUY | Magnetostrictive Probe | $42,000 | ML |
| AF-MAAP1-EC-5025-00 | Anti-Ice Control Panel | 1 | BUY | Cockpit Interface | $28,000 | ML |

**Sub-total Anti-Ice & De-Ice:** $656,500

**TOTAL ENVIRONMENTAL CONTROL SYSTEM:** $2,271,000

---

### 10.0 FUEL SYSTEM (AF-MAAP1-FS)

#### 10.1 Fuel Tanks & Structure
**Drawing Reference:** AF-MAAP1-FS-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FS-1001-00 | Center Wing Fuel Tank Assembly | 1 | MAKE | Integral Al 7050-T7451 | $385,000 | LL |
| AF-MAAP1-FS-1002-00 | Left Wing Fuel Tank Assembly | 1 | MAKE | Integral Al 7050-T7451 | $285,000 | LL |
| AF-MAAP1-FS-1003-00 | Right Wing Fuel Tank Assembly | 1 | MAKE | Integral Al 7050-T7451 | $285,000 | LL |
| AF-MAAP1-FS-1005-00 | Auxiliary Fuel Tank - Fuselage | 1 | MAKE | Bladder Type | $125,000 | ML |
| AF-MAAP1-FS-1010-00 | Fuel Tank Access Panel | 24 | MAKE | Al 7075-T6 | $48,000 | ML |
| AF-MAAP1-FS-1015-00 | Fuel Tank Sealant Application | 1 | MFG | PR-1776 Class B | $95,000 | LL |
| AF-MAAP1-FS-1020-00 | Fuel Tank Vent System | 1 | MAKE | Al Tubing/Valves | $65,000 | ML |
| AF-MAAP1-FS-1025-00 | Surge Tank Assembly | 2 | MAKE | Al 7075-T6 | $42,000 | ML |

**Sub-total Fuel Tanks & Structure:** $1,330,000

#### 10.2 Fuel Pumps & Transfer
**Drawing Reference:** AF-MAAP1-FS-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FS-2001-00 | Main Fuel Pump - Center Tank | 2 | BUY | Centrifugal, 28VDC | $42,000 | ML |
| AF-MAAP1-FS-2002-00 | Main Fuel Pump - Left Wing | 1 | BUY | Centrifugal, 28VDC | $21,000 | ML |
| AF-MAAP1-FS-2003-00 | Main Fuel Pump - Right Wing | 1 | BUY | Centrifugal, 28VDC | $21,000 | ML |
| AF-MAAP1-FS-2005-00 | Auxiliary Fuel Pump | 1 | BUY | Centrifugal, 28VDC | $21,000 | ML |
| AF-MAAP1-FS-2010-00 | Transfer Pump Assembly | 2 | BUY | Ejector Type | $18,000 | ML |
| AF-MAAP1-FS-2015-00 | Scavenge Pump Assembly | 4 | BUY | Ejector Type | $28,000 | ML |
| AF-MAAP1-FS-2020-00 | Engine-Driven Fuel Pump - No.1 | 1 | BUY | Positive Displacement | $42,000 | LL |
| AF-MAAP1-FS-2021-00 | Engine-Driven Fuel Pump - No.2 | 1 | BUY | Positive Displacement | $42,000 | LL |
| AF-MAAP1-FS-2025-00 | APU Fuel Pump | 1 | BUY | Centrifugal, 28VDC | $18,000 | ML |

**Sub-total Fuel Pumps & Transfer:** $253,000

#### 10.3 Fuel Distribution & Control
**Drawing Reference:** AF-MAAP1-FS-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FS-3001-00 | Fuel Manifold Assembly | 1 | MAKE | 316 Stainless Steel | $85,000 | ML |
| AF-MAAP1-FS-3002-00 | Fuel Shutoff Valve - Engine 1 | 1 | BUY | Motor-Operated | $32,000 | ML |
| AF-MAAP1-FS-3003-00 | Fuel Shutoff Valve - Engine 2 | 1 | BUY | Motor-Operated | $32,000 | ML |
| AF-MAAP1-FS-3005-00 | Crossfeed Valve | 1 | BUY | Motor-Operated | $28,000 | ML |
| AF-MAAP1-FS-3010-00 | Fuel Flow Control Unit | 2 | BUY | Hydromechanical | $85,000 | LL |
| AF-MAAP1-FS-3015-00 | Fuel Filter - Primary | 2 | BUY | 10 Micron | $18,000 | ML |
| AF-MAAP1-FS-3016-00 | Fuel Filter - Secondary | 2 | BUY | 40 Micron | $12,000 | ML |
| AF-MAAP1-FS-3020-00 | Pressure Relief Valve | 4 | BUY | Adjustable | $12,000 | SL |
| AF-MAAP1-FS-3025-00 | Check Valve Assembly | 12 | BUY | High-Flow | $18,000 | SL |
| AF-MAAP1-FS-3030-00 | Defueling Valve | 1 | BUY | Manual Override | $12,000 | ML |

**Sub-total Fuel Distribution & Control:** $334,000

#### 10.4 Fuel Lines & Fittings
**Drawing Reference:** AF-MAAP1-FS-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FS-4001-00 | Fuel Line Assembly - Center Feed | 1 | MAKE | 316 SS Tube/MS Fittings | $85,000 | ML |
| AF-MAAP1-FS-4002-00 | Fuel Line Assembly - Left Wing | 1 | MAKE | 316 SS Tube/MS Fittings | $65,000 | ML |
| AF-MAAP1-FS-4003-00 | Fuel Line Assembly - Right Wing | 1 | MAKE | 316 SS Tube/MS Fittings | $65,000 | ML |
| AF-MAAP1-FS-4005-00 | Engine Feed Line - No.1 | 1 | MAKE | 316 SS Tube/Flex Section | $42,000 | ML |
| AF-MAAP1-FS-4006-00 | Engine Feed Line - No.2 | 1 | MAKE | 316 SS Tube/Flex Section | $42,000 | ML |
| AF-MAAP1-FS-4010-00 | APU Fuel Line Assembly | 1 | MAKE | 316 SS Tube/MS Fittings | $28,000 | ML |
| AF-MAAP1-FS-4015-00 | Fuel Return Line Assembly | 1 | MAKE | 316 SS Tube/MS Fittings | $32,000 | ML |
| AF-MAAP1-FS-4020-00 | Vent Line Assembly | 1 | MAKE | Al Alloy Tube | $28,000 | ML |
| AF-MAAP1-FS-4025-00 | Flexible Hose Assembly | 18 | BUY | MIL-H-27267 PTFE | $42,000 | ML |

**Sub-total Fuel Lines & Fittings:** $429,000

#### 10.5 Fuel Instrumentation & Monitoring
**Drawing Reference:** AF-MAAP1-FS-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FS-5001-00 | Fuel Quantity Indicating System | 1 | BUY | Capacitance Probes | $125,000 | ML |
| AF-MAAP1-FS-5002-00 | Fuel Quantity Probe - Center Tank | 8 | BUY | Capacitance Type | $32,000 | ML |
| AF-MAAP1-FS-5003-00 | Fuel Quantity Probe - Wing Tanks | 12 | BUY | Capacitance Type | $42,000 | ML |
| AF-MAAP1-FS-5005-00 | Fuel Flow Transducer | 2 | BUY | Mass Flow Type | $42,000 | ML |
| AF-MAAP1-FS-5010-00 | Fuel Temperature Sensor | 4 | BUY | RTD Type | $12,000 | SL |
| AF-MAAP1-FS-5015-00 | Fuel Pressure Transducer | 6 | BUY | 0-100 PSI | $18,000 | ML |
| AF-MAAP1-FS-5020-00 | Low Fuel Level Sensor | 6 | BUY | Float Switch | $12,000 | SL |
| AF-MAAP1-FS-5025-00 | Fuel Management Computer | 1 | BUY | Integrated System | $85,000 | LL |
| AF-MAAP1-FS-5030-00 | Fuel Filter Contamination Indicator | 4 | BUY | Differential Pressure | $8,500 | SL |

**Sub-total Fuel Instrumentation:** $376,500

#### 10.6 Fuel System Support Equipment
**Drawing Reference:** AF-MAAP1-FS-6000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FS-6001-00 | Single Point Refueling Receptacle | 1 | BUY | Pressure Refuel | $28,000 | ML |
| AF-MAAP1-FS-6002-00 | Gravity Fill Port - Center Tank | 1 | MAKE | Al 7075-T6 Cap | $8,500 | SL |
| AF-MAAP1-FS-6003-00 | Gravity Fill Port - Wing Tanks | 2 | MAKE | Al 7075-T6 Cap | $12,000 | SL |
| AF-MAAP1-FS-6005-00 | Fuel Drain Valve - Center Tank | 2 | BUY | Quick-Drain | $8,500 | SL |
| AF-MAAP1-FS-6006-00 | Fuel Drain Valve - Wing Tanks | 4 | BUY | Quick-Drain | $12,000 | SL |
| AF-MAAP1-FS-6010-00 | Fuel Sample Port | 6 | BUY | Self-Closing | $8,500 | SL |
| AF-MAAP1-FS-6015-00 | Ground Service Panel - Fuel | 1 | MAKE | Al Enclosure | $18,000 | ML |

**Sub-total Fuel System Support:** $95,500

**TOTAL FUEL SYSTEM:** $2,818,000

---

### 11.0 FIRE PROTECTION SYSTEM (AF-MAAP1-FP)

#### 11.1 Fire Detection
**Drawing Reference:** AF-MAAP1-FP-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FP-1001-00 | Fire Detection Control Unit | 1 | BUY | Dual Channel | $85,000 | ML |
| AF-MAAP1-FP-1002-00 | Engine Fire Detection Loop - No.1 | 2 | BUY | Pneumatic Type | $28,000 | ML |
| AF-MAAP1-FP-1003-00 | Engine Fire Detection Loop - No.2 | 2 | BUY | Pneumatic Type | $28,000 | ML |
| AF-MAAP1-FP-1005-00 | APU Fire Detection Loop | 1 | BUY | Pneumatic Type | $14,000 | ML |
| AF-MAAP1-FP-1010-00 | Cargo Bay Smoke Detector | 4 | BUY | Optical Type | $28,000 | ML |
| AF-MAAP1-FP-1015-00 | Avionics Bay Smoke Detector | 2 | BUY | Optical Type | $14,000 | ML |
| AF-MAAP1-FP-1020-00 | Lavatory Smoke Detector | 2 | BUY | Ionization Type | $8,500 | SL |
| AF-MAAP1-FP-1025-00 | Main Landing Gear Fire Detection | 2 | BUY | Thermal Switch | $12,000 | ML |

**Sub-total Fire Detection:** $217,500

#### 11.2 Fire Extinguishing - Engine/APU
**Drawing Reference:** AF-MAAP1-FP-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FP-2001-00 | Fire Extinguisher Bottle - Engine | 2 | BUY | Halon 1301, 10 lbs | $42,000 | ML |
| AF-MAAP1-FP-2002-00 | Fire Extinguisher Bottle - APU | 1 | BUY | Halon 1301, 5 lbs | $18,000 | ML |
| AF-MAAP1-FP-2005-00 | Discharge Valve - Engine System | 2 | BUY | Explosive Cartridge | $18,000 | ML |
| AF-MAAP1-FP-2006-00 | Discharge Valve - APU System | 1 | BUY | Explosive Cartridge | $9,000 | ML |
| AF-MAAP1-FP-2010-00 | Distribution Nozzle - Engine | 4 | BUY | High-Temp Resistant | $18,000 | ML |
| AF-MAAP1-FP-2011-00 | Distribution Nozzle - APU | 2 | BUY | High-Temp Resistant | $8,500 | ML |
| AF-MAAP1-FP-2015-00 | Discharge Line - Engine System | 2 | MAKE | 316 SS Tube | $28,000 | ML |
| AF-MAAP1-FP-2016-00 | Discharge Line - APU System | 1 | MAKE | 316 SS Tube | $12,000 | ML |
| AF-MAAP1-FP-2020-00 | Pressure Switch - Bottle Monitor | 3 | BUY | Electronic Output | $12,000 | SL |

**Sub-total Fire Extinguishing - Engine/APU:** $165,500

#### 11.3 Fire Extinguishing - Cabin/Cargo
**Drawing Reference:** AF-MAAP1-FP-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FP-3001-00 | Cargo Bay Fire Suppression System | 1 | BUY | Halon 1301, 22 lbs | $125,000 | ML |
| AF-MAAP1-FP-3002-00 | Cargo Bay Distribution Nozzle | 8 | BUY | Coverage Pattern | $28,000 | ML |
| AF-MAAP1-FP-3005-00 | Portable Fire Extinguisher - Cockpit | 2 | BUY | Halon 1211, 5 lbs | $8,500 | SL |
| AF-MAAP1-FP-3006-00 | Portable Fire Extinguisher - Cabin | 2 | BUY | Halon 1211, 5 lbs | $8,500 | SL |
| AF-MAAP1-FP-3010-00 | Lavatory Fire Extinguisher | 2 | BUY | Auto-Discharge | $12,000 | ML |

**Sub-total Fire Extinguishing - Cabin/Cargo:** $182,000

#### 11.4 Fire Protection Control & Indication
**Drawing Reference:** AF-MAAP1-FP-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-FP-4001-00 | Fire Control Panel - Cockpit | 1 | BUY | Backlit Switches | $42,000 | ML |
| AF-MAAP1-FP-4002-00 | Fire Warning Light - Engine 1 | 1 | BUY | Red LED | $4,500 | SL |
| AF-MAAP1-FP-4003-00 | Fire Warning Light - Engine 2 | 1 | BUY | Red LED | $4,500 | SL |
| AF-MAAP1-FP-4004-00 | Fire Warning Light - APU | 1 | BUY | Red LED | $4,500 | SL |
| AF-MAAP1-FP-4005-00 | Fire Warning Light - Cargo Bay | 1 | BUY | Red LED | $4,500 | SL |
| AF-MAAP1-FP-4010-00 | Fire Test Switch | 1 | BUY | Momentary Push | $2,500 | SL |
| AF-MAAP1-FP-4015-00 | Fire Bell - Cockpit | 1 | BUY | Audio Alert | $4,500 | SL |

**Sub-total Fire Protection Control:** $67,000

**TOTAL FIRE PROTECTION SYSTEM:** $632,000

---

### 12.0 VARIANT-SPECIFIC SYSTEMS

#### 12.1 ISR Variant Systems (AF-MAAP1-ISR)

##### 12.1.1 ISR Sensor Suite
**Drawing Reference:** AF-MAAP1-ISR-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-ISR-1001-00 | Multi-Spectral EO/IR Turret (Advanced) | 1 | BUY | HD/Thermal/SWIR | $1,850,000 | LL |
| AF-MAAP1-ISR-1002-00 | Synthetic Aperture Radar (SAR) | 1 | BUY | X-Band, 1m Resolution | $3,250,000 | LL |
| AF-MAAP1-ISR-1003-00 | Ground Moving Target Indicator (GMTI) | 1 | BUY | Integrated with SAR | $1,450,000 | LL |
| AF-MAAP1-ISR-1005-00 | Signals Intelligence (SIGINT) Pod | 1 | BUY | Multi-Band Receiver | $2,850,000 | LL |
| AF-MAAP1-ISR-1010-00 | Electronic Intelligence (ELINT) System | 1 | BUY | Direction Finding | $1,950,000 | LL |
| AF-MAAP1-ISR-1015-00 | Communications Intelligence (COMINT) | 1 | BUY | Multi-Channel | $2,450,000 | LL |
| AF-MAAP1-ISR-1020-00 | Wide Area Motion Imagery (WAMI) | 1 | BUY | 360° Coverage | $4,250,000 | LL |
| AF-MAAP1-ISR-1025-00 | Full Motion Video Processing | 1 | BUY | 12-Channel HD | $925,000 | LL |

**Sub-total ISR Sensor Suite:** $18,975,000

##### 12.1.2 ISR Mission Management
**Drawing Reference:** AF-MAAP1-ISR-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-ISR-2001-00 | ISR Mission Computer | 2 | BUY | Redundant Processing | $1,250,000 | LL |
| AF-MAAP1-ISR-2002-00 | Sensor Management Workstation | 2 | BUY | 24" Touchscreen | $485,000 | LL |
| AF-MAAP1-ISR-2003-00 | Data Fusion Processor | 1 | BUY | Multi-INT Correlation | $1,850,000 | LL |
| AF-MAAP1-ISR-2005-00 | Image Analysis Workstation | 2 | BUY | 27" High-Res Display | $385,000 | LL |
| AF-MAAP1-ISR-2010-00 | Data Storage System | 1 | BUY | 20TB RAID Array | $285,000 | LL |
| AF-MAAP1-ISR-2015-00 | Real-Time Data Link System | 1 | BUY | High-Bandwidth SATCOM | $2,450,000 | LL |
| AF-MAAP1-ISR-2020-00 | Metadata Tagging System | 1 | BUY | Auto-Georeferencing | $525,000 | LL |

**Sub-total ISR Mission Management:** $7,230,000

##### 12.1.3 ISR Communication Systems
**Drawing Reference:** AF-MAAP1-ISR-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-ISR-3001-00 | Multi-Band SATCOM Terminal | 2 | BUY | Ku/Ka Band | $1,450,000 | LL |
| AF-MAAP1-ISR-3002-00 | Line-of-Sight Data Link | 2 | BUY | 274 Mbps TCDL | $685,000 | LL |
| AF-MAAP1-ISR-3005-00 | Wideband Tactical Data Link | 1 | BUY | Link 16 Compatible | $825,000 | LL |
| AF-MAAP1-ISR-3010-00 | Secure Voice System - ISR Crew | 1 | BUY | Type 1 Encryption | $185,000 | LL |
| AF-MAAP1-ISR-3015-00 | Data Distribution Unit | 1 | BUY | Router/Switch | $285,000 | ML |

**Sub-total ISR Communication:** $3,430,000

##### 12.1.4 ISR Operator Stations
**Drawing Reference:** AF-MAAP1-ISR-4000-00  
**Quantity per Aircraft:** 4 Stations  
**Make/Buy:** ASSY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-ISR-4001-00 | Sensor Operator Console | 2 | MAKE | Ergonomic Workstation | $185,000 | ML |
| AF-MAAP1-ISR-4002-00 | SIGINT Operator Console | 1 | MAKE | Ergonomic Workstation | $185,000 | ML |
| AF-MAAP1-ISR-4003-00 | Mission Commander Console | 1 | MAKE | Ergonomic Workstation | $185,000 | ML |
| AF-MAAP1-ISR-4005-00 | Multi-Function Display - Operator | 8 | BUY | 24" HD Touchscreen | $485,000 | ML |
| AF-MAAP1-ISR-4010-00 | Sensor Control Joystick | 2 | BUY | 4-Axis Precision | $85,000 | ML |
| AF-MAAP1-ISR-4015-00 | Audio Control Panel - Operator | 4 | BUY | Multi-Channel | $42,000 | ML |
| AF-MAAP1-ISR-4020-00 | Operator Seat - ISR Mission | 4 | BUY | Ejection Not Required | $125,000 | ML |

**Sub-total ISR Operator Stations:** $1,292,000

**TOTAL ISR VARIANT SYSTEMS:** $30,927,000

---

#### 12.2 Armed Reconnaissance Variant Systems (AF-MAAP1-AR)

##### 12.2.1 Weapons Management System
**Drawing Reference:** AF-MAAP1-AR-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AR-1001-00 | Weapons Management Computer | 2 | BUY | Dual Redundant | $1,250,000 | LL |
| AF-MAAP1-AR-1002-00 | Stores Management System | 1 | BUY | MIL-STD-1760 Interface | $825,000 | LL |
| AF-MAAP1-AR-1003-00 | Fire Control Computer | 1 | BUY | Ballistic Processor | $1,450,000 | LL |
| AF-MAAP1-AR-1005-00 | Targeting Pod Interface Unit | 1 | BUY | Multi-Protocol | $385,000 | ML |
| AF-MAAP1-AR-1010-00 | Weapon Release Control Unit | 2 | BUY | Redundant Safety | $285,000 | ML |
| AF-MAAP1-AR-1015-00 | Armament Control Panel | 1 | BUY | Cockpit Interface | $125,000 | ML |

**Sub-total Weapons Management:** $4,320,000

##### 12.2.2 External Stores & Hardpoints
**Drawing Reference:** AF-MAAP1-AR-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AR-2001-00 | Inboard Wing Hardpoint (Wet) | 2 | MAKE | Ti Alloy, 3500 lbs | $185,000 | ML |
| AF-MAAP1-AR-2002-00 | Mid-Wing Hardpoint | 2 | MAKE | Ti Alloy, 2500 lbs | $125,000 | ML |
| AF-MAAP1-AR-2003-00 | Outboard Wing Hardpoint | 2 | MAKE | Ti Alloy, 1500 lbs | $85,000 | ML |
| AF-MAAP1-AR-2005-00 | Centerline Hardpoint (Wet) | 1 | MAKE | Ti Alloy, 5000 lbs | $285,000 | ML |
| AF-MAAP1-AR-2010-00 | Fuselage Station Hardpoint | 2 | MAKE | Ti Alloy, 2000 lbs | $145,000 | ML |
| AF-MAAP1-AR-2015-00 | Ejector Rack - Triple (TER) | 4 | BUY | 3x500 lbs Capacity | $125,000 | ML |
| AF-MAAP1-AR-2020-00 | Ejector Rack - Dual (BRU) | 2 | BUY | 2x1000 lbs Capacity | $85,000 | ML |
| AF-MAAP1-AR-2025-00 | Smart Weapon Launcher | 2 | BUY | Digital Interface | $285,000 | ML |

**Sub-total External Stores:** $1,320,000

##### 12.2.3 Targeting Systems
**Drawing Reference:** AF-MAAP1-AR-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AR-3001-00 | Advanced Targeting Pod | 1 | BUY | Multi-Spectral/Laser | $2,850,000 | LL |
| AF-MAAP1-AR-3002-00 | Helmet Mounted Display System | 2 | BUY | Cueing & Targeting | $485,000 | LL |
| AF-MAAP1-AR-3005-00 | Laser Designator (Pod-Mounted) | 1 | BUY | Class IV, Eye-Safe | $925,000 | LL |
| AF-MAAP1-AR-3010-00 | Targeting Display - Pilot | 1 | BUY | 8"x10" MFD | $185,000 | ML |
| AF-MAAP1-AR-3015-00 | Target Coordinate Generator | 1 | BUY | GPS/INS Integration | $285,000 | ML |

**Sub-total Targeting Systems:** $4,730,000

##### 12.2.4 Defensive Systems (Enhanced)
**Drawing Reference:** AF-MAAP1-AR-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AR-4001-00 | Missile Warning System (Advanced) | 1 | BUY | UV/IR 360° Coverage | $1,450,000 | LL |
| AF-MAAP1-AR-4002-00 | Laser Warning Receiver | 1 | BUY | Multi-Band Detection | $625,000 | LL |
| AF-MAAP1-AR-4005
| AF-MAAP1-AR-4005-00 | Countermeasure Dispenser System | 4 | BUY | Chaff/Flare, 120 Rnd | $285,000 | ML |
| AF-MAAP1-AR-4010-00 | Radar Warning Receiver (RWR) | 1 | BUY | Threat Library Equipped | $825,000 | LL |
| AF-MAAP1-AR-4015-00 | Infrared Countermeasures (IRCM) | 2 | BUY | Directional Jamming | $1,125,000 | LL |
| AF-MAAP1-AR-4020-00 | Electronic Warfare Suite Computer | 1 | BUY | Integrated Processing | $975,000 | LL |
| AF-MAAP1-AR-4025-00 | Towed Decoy System | 2 | BUY | Fiber-Optic Link | $685,000 | LL |
| AF-MAAP1-AR-4030-00 | Defensive Aids Control Panel | 1 | BUY | Cockpit Interface | $145,000 | ML |

**Sub-total Defensive Systems:** $6,115,000

**Total Group 12 (Armament & Mission Systems):** $16,485,000

---

#### 12.3 GROUP 13: AUXILIARY POWER & PNEUMATICS

##### 13.1.1 Auxiliary Power Unit (APU)
**Drawing Reference:** AF-MAAP1-AU-1000-00  
**Quantity per Aircraft:** 1 Assembly  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AU-1001-00 | APU Core Assembly | 1 | BUY | 150 kVA Output | $1,850,000 | LL |
| AF-MAAP1-AU-1002-00 | APU Electronic Control Unit | 1 | BUY | FADEC Type | $285,000 | LL |
| AF-MAAP1-AU-1005-00 | APU Air Inlet Assembly | 1 | MAKE | CRES, Composite Door | $125,000 | ML |
| AF-MAAP1-AU-1010-00 | APU Exhaust System | 1 | MAKE | Inconel 625 | $185,000 | ML |
| AF-MAAP1-AU-1015-00 | APU Firewall Assembly | 1 | MAKE | Ti Alloy, Insulated | $95,000 | ML |
| AF-MAAP1-AU-1020-00 | APU Mounting Structure | 1 | MAKE | Ti Alloy Frame | $145,000 | ML |
| AF-MAAP1-AU-1025-00 | APU Fuel Supply System | 1 | BUY | Pump & Filter Assembly | $125,000 | ML |
| AF-MAAP1-AU-1030-00 | APU Fire Detection/Suppression | 1 | BUY | Dual Loop System | $185,000 | ML |
| AF-MAAP1-AU-1035-00 | APU Load Compressor | 1 | BUY | Pneumatic Output | $285,000 | LL |
| AF-MAAP1-AU-1040-00 | APU Oil System | 1 | BUY | Self-Contained | $85,000 | ML |

**Sub-total APU Assembly:** $3,365,000

##### 13.1.2 Ground Power & Start Systems
**Drawing Reference:** AF-MAAP1-AU-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AU-2001-00 | External Power Receptacle | 1 | BUY | 270 VDC Rated | $45,000 | SL |
| AF-MAAP1-AU-2002-00 | Ground Power Control Unit | 1 | BUY | Auto Disconnect | $95,000 | ML |
| AF-MAAP1-AU-2005-00 | Air Start Receptacle | 1 | BUY | Pneumatic Connection | $35,000 | SL |
| AF-MAAP1-AU-2010-00 | Ground Intercom Panel | 1 | BUY | Nose Gear Mounted | $25,000 | SL |
| AF-MAAP1-AU-2015-00 | Power Panel Lighting | 1 | BUY | LED Illumination | $8,500 | SL |

**Sub-total Ground Power Systems:** $208,500

##### 13.1.3 Emergency Power Systems
**Drawing Reference:** AF-MAAP1-AU-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AU-3001-00 | Emergency Power Unit (EPU) | 1 | BUY | Hydrazine Powered | $1,250,000 | LL |
| AF-MAAP1-AU-3002-00 | EPU Control Module | 1 | BUY | Auto-Deploy Logic | $185,000 | ML |
| AF-MAAP1-AU-3005-00 | Hydrazine Fuel Tank | 1 | BUY | 15 Minute Runtime | $285,000 | LL |
| AF-MAAP1-AU-3010-00 | Ram Air Turbine (RAT) | 1 | BUY | 30 kVA Emergency Gen | $625,000 | LL |
| AF-MAAP1-AU-3015-00 | RAT Deployment Mechanism | 1 | BUY | Explosive Actuator | $145,000 | ML |
| AF-MAAP1-AU-3020-00 | Emergency Battery Pack | 2 | BUY | 28 VDC, 90 Ah | $125,000 | ML |

**Sub-total Emergency Power:** $2,615,000

##### 13.1.4 Pneumatic Distribution System
**Drawing Reference:** AF-MAAP1-AU-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-AU-4001-00 | Engine Bleed Air Manifold | 2 | MAKE | Inconel 718 | $185,000 | ML |
| AF-MAAP1-AU-4002-00 | Bleed Air Pressure Regulator | 2 | BUY | Dual Channel | $125,000 | ML |
| AF-MAAP1-AU-4005-00 | Pneumatic Distribution Ducting | 1 | MAKE | CRES, Insulated | $285,000 | ML |
| AF-MAAP1-AU-4010-00 | Anti-Ice Bleed Valve | 4 | BUY | Electro-Pneumatic | $85,000 | ML |
| AF-MAAP1-AU-4015-00 | Cabin Pressurization Valve | 2 | BUY | Servo-Controlled | $145,000 | ML |
| AF-MAAP1-AU-4020-00 | Pneumatic Check Valves | 8 | BUY | Spring-Loaded | $25,000 | SL |
| AF-MAAP1-AU-4025-00 | Air Cycle Machine | 2 | BUY | ECS Interface | $285,000 | ML |
| AF-MAAP1-AU-4030-00 | Bleed Air Temperature Sensors | 6 | BUY | High-Temp Rated | $18,500 | SL |

**Sub-total Pneumatic Distribution:** $1,153,500

**Total Group 13 (Auxiliary Power & Pneumatics):** $7,342,000

---

#### 12.4 GROUP 14: ENVIRONMENTAL CONTROL SYSTEMS (ECS)

##### 14.1.1 Air Conditioning & Pressurization
**Drawing Reference:** AF-MAAP1-EC-1000-00  
**Quantity per Aircraft:** 1 System  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-1001-00 | Primary Air Cycle Machine | 1 | BUY | Bootstrap System | $485,000 | LL |
| AF-MAAP1-EC-1002-00 | Secondary ACM (Backup) | 1 | BUY | Bootstrap System | $485,000 | LL |
| AF-MAAP1-EC-1005-00 | Cabin Pressure Controller | 2 | BUY | Dual Redundant | $185,000 | ML |
| AF-MAAP1-EC-1010-00 | Outflow Valve Assembly | 2 | BUY | Motorized, Fail-Safe | $125,000 | ML |
| AF-MAAP1-EC-1015-00 | Safety Relief Valve | 2 | BUY | Pressure Backup | $45,000 | ML |
| AF-MAAP1-EC-1020-00 | Temperature Control Unit | 2 | BUY | Cockpit & Avionics Bay | $145,000 | ML |
| AF-MAAP1-EC-1025-00 | Heat Exchanger - Primary | 2 | BUY | Ram Air Cooled | $185,000 | ML |
| AF-MAAP1-EC-1030-00 | Heat Exchanger - Secondary | 2 | BUY | Fuel Heat Sink | $225,000 | ML |
| AF-MAAP1-EC-1035-00 | Condenser/Water Separator | 1 | BUY | Moisture Removal | $85,000 | ML |
| AF-MAAP1-EC-1040-00 | Distribution Ducting Assembly | 1 | MAKE | Al Alloy, Insulated | $285,000 | ML |
| AF-MAAP1-EC-1045-00 | Cockpit Diffuser Nozzles | 8 | BUY | Adjustable Flow | $12,500 | SL |

**Sub-total Air Conditioning:** $2,262,500

##### 14.1.2 Oxygen Systems
**Drawing Reference:** AF-MAAP1-EC-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-2001-00 | Onboard Oxygen Generator (OBOGS) | 1 | BUY | Molecular Sieve | $625,000 | LL |
| AF-MAAP1-EC-2002-00 | OBOGS Control Unit | 1 | BUY | Auto Regulation | $125,000 | ML |
| AF-MAAP1-EC-2005-00 | Emergency Oxygen Bottle | 2 | BUY | 115 cu ft, 1850 psi | $85,000 | ML |
| AF-MAAP1-EC-2010-00 | Oxygen Regulator - Pilot | 1 | BUY | Pressure Demand Type | $45,000 | ML |
| AF-MAAP1-EC-2015-00 | Oxygen Regulator - WSO | 1 | BUY | Pressure Demand Type | $45,000 | ML |
| AF-MAAP1-EC-2020-00 | Oxygen Distribution Manifold | 1 | MAKE | CRES Tubing | $35,000 | ML |
| AF-MAAP1-EC-2025-00 | Oxygen Flow Indicators | 2 | BUY | Cockpit Mounted | $12,500 | SL |
| AF-MAAP1-EC-2030-00 | Oxygen Mask Quick-Disconnect | 2 | BUY | CRU-103 Compatible | $8,500 | SL |

**Sub-total Oxygen Systems:** $981,000

##### 14.1.3 Anti-G & Breathing Systems
**Drawing Reference:** AF-MAAP1-EC-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-3001-00 | Anti-G Valve - Pilot | 1 | BUY | 9G Rated | $125,000 | ML |
| AF-MAAP1-EC-3002-00 | Anti-G Valve - WSO | 1 | BUY | 9G Rated | $125,000 | ML |
| AF-MAAP1-EC-3005-00 | Positive Pressure Breathing (PPB) Regulator | 2 | BUY | High-Altitude | $85,000 | ML |
| AF-MAAP1-EC-3010-00 | G-Suit Manifold Assembly | 2 | MAKE | Pneumatic Distribution | $45,000 | ML |
| AF-MAAP1-EC-3015-00 | Breathing Pressure Sensors | 4 | BUY | Digital Output | $15,000 | SL |

**Sub-total Anti-G Systems:** $395,000

##### 14.1.4 Avionics Cooling System
**Drawing Reference:** AF-MAAP1-EC-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-4001-00 | Liquid Cooling Pump - Primary | 1 | BUY | PAO Fluid, 20 GPM | $185,000 | ML |
| AF-MAAP1-EC-4002-00 | Liquid Cooling Pump - Backup | 1 | BUY | PAO Fluid, 20 GPM | $185,000 | ML |
| AF-MAAP1-EC-4005-00 | Avionics Bay Heat Exchanger | 2 | BUY | Liquid-to-Air | $145,000 | ML |
| AF-MAAP1-EC-4010-00 | Cooling Liquid Reservoir | 1 | MAKE | 5 Gallon Capacity | $35,000 | ML |
| AF-MAAP1-EC-4015-00 | Liquid Cooling Lines & Fittings | 1 | MAKE | CRES Tubing | $125,000 | ML |
| AF-MAAP1-EC-4020-00 | Cold Plate - Radar Bay | 2 | BUY | Machined Al Alloy | $85,000 | ML |
| AF-MAAP1-EC-4025-00 | Cold Plate - Mission Computer | 4 | BUY | Machined Al Alloy | $45,000 | ML |
| AF-MAAP1-EC-4030-00 | Cooling System Controller | 1 | BUY | Temperature Regulated | $95,000 | ML |
| AF-MAAP1-EC-4035-00 | Flow Meters & Sensors | 6 | BUY | Digital Monitoring | $25,000 | SL |

**Sub-total Avionics Cooling:** $925,000

##### 14.1.5 Cockpit Environmental Controls
**Drawing Reference:** AF-MAAP1-EC-5000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-EC-5001-00 | Canopy Defog/Demist System | 1 | MAKE | Bleed Air Powered | $85,000 | ML |
| AF-MAAP1-EC-5002-00 | Windscreen Anti-Ice System | 1 | BUY | Electrical Heating | $145,000 | ML |
| AF-MAAP1-EC-5005-00 | Seat Cooling/Heating System | 2 | BUY | Thermoelectric | $125,000 | ML |
| AF-MAAP1-EC-5010-00 | Cockpit Temperature Sensors | 6 | BUY | Digital Output | $18,500 | SL |
| AF-MAAP1-EC-5015-00 | Humidity Control System | 1 | BUY | Auto Regulation | $65,000 | ML |
| AF-MAAP1-EC-5020-00 | Air Distribution Control Panel | 1 | BUY | Cockpit Interface | $45,000 | ML |

**Sub-total Cockpit Environmental:** $483,500

**Total Group 14 (Environmental Control Systems):** $5,047,000

---

#### 12.5 GROUP 15: CREW SYSTEMS & SAFETY

##### 15.1.1 Ejection Seats
**Drawing Reference:** AF-MAAP1-CS-1000-00  
**Quantity per Aircraft:** 2 Each  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-CS-1001-00 | Zero-Zero Ejection Seat - Pilot | 1 | BUY | ACES II or Equivalent | $485,000 | LL |
| AF-MAAP1-CS-1002-00 | Zero-Zero Ejection Seat - WSO | 1 | BUY | ACES II or Equivalent | $485,000 | LL |
| AF-MAAP1-CS-1005-00 | Seat Survival Kit | 2 | BUY | Integrated Package | $85,000 | ML |
| AF-MAAP1-CS-1010-00 | Seat Parachute Assembly | 2 | BUY | Auto-Deploy System | $125,000 | ML |
| AF-MAAP1-CS-1015-00 | Seat Catapult Assembly | 2 | BUY | Ballistic Cartridge | $95,000 | ML |
| AF-MAAP1-CS-1020-00 | Drogue Chute System | 2 | BUY | Stabilization | $65,000 | ML |
| AF-MAAP1-CS-1025-00 | Personal Locator Beacon | 2 | BUY | GPS Enabled | $25,000 | SL |
| AF-MAAP1-CS-1030-00 | Seat Inertial Reel Harness | 2 | BUY | 5-Point Restraint | $45,000 | ML |
| AF-MAAP1-CS-1035-00 | Leg Restraint System | 2 | BUY | Auto-Deploy | $35,000 | ML |
| AF-MAAP1-CS-1040-00 | Seat Pan Survival Radio | 2 | BUY | Emergency Comm | $18,500 | ML |

**Sub-total Ejection Seats:** $1,463,500

##### 15.1.2 Cockpit Safety Systems
**Drawing Reference:** AF-MAAP1-CS-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-CS-2001-00 | Canopy Jettison System | 1 | BUY | Pyrotechnic Actuators | $185,000 | ML |
| AF-MAAP1-CS-2002-00 | Canopy Emergency Release Handle | 2 | BUY | Mechanical Backup | $25,000 | SL |
| AF-MAAP1-CS-2005-00 | Canopy Severance Cord | 1 | BUY | MDC Explosive | $45,000 | ML |
| AF-MAAP1-CS-2010-00 | Emergency Egress Lighting | 1 | BUY | Photo-luminescent | $12,500 | SL |
| AF-MAAP1-CS-2015-00 | Crash-Resistant Fuel System | 1 | MAKE | Breakaway Fittings | $285,000 | ML |
| AF-MAAP1-CS-2020-00 | Fire Extinguisher - Cockpit | 1 | BUY | Halon 1211 | $15,000 | SL |
| AF-MAAP1-CS-2025-00 | Emergency Checklist Panels | 4 | MAKE | Engraved Plaques | $8,500 | SL |

**Sub-total Cockpit Safety:** $576,000

##### 15.1.3 Life Support Equipment
**Drawing Reference:** AF-MAAP1-CS-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-CS-3001-00 | Anti-G Suit - Pilot | 1 | BUY | 9G Coverage | $25,000 | SL |
| AF-MAAP1-CS-3002-00 | Anti-G Suit - WSO | 1 | BUY | 9G Coverage | $25,000 | SL |
| AF-MAAP1-CS-3005-00 | Flight Helmet - Pilot (HMD Equipped) | 1 | BUY | HMD Compatible | $125,000 | ML |
| AF-MAAP1-CS-3006-00 | Flight Helmet - WSO (HMD Equipped) | 1 | BUY | HMD Compatible | $125,000 | ML |
| AF-MAAP1-CS-3010-00 | Oxygen Mask - MBU-20 | 2 | BUY | Pressure Breathing | $18,500 | SL |
| AF-MAAP1-CS-3015-00 | Chemical/Biological Protection System | 2 | BUY | CBRN Rated | $85,000 | ML |
| AF-MAAP1-CS-3020-00 | Survival Vest | 2 | BUY | Equipped Package | $12,500 | SL |
| AF-MAAP1-CS-3025-00 | Emergency Life Raft | 2 | BUY | 2-Person Capacity | $25,000 | ML |

**Sub-total Life Support Equipment:** $441,000

##### 15.1.4 Cockpit Fire Protection
**Drawing Reference:** AF-MAAP1-CS-4000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-CS-4001-00 | Fire Detection Loop - Cockpit | 2 | BUY | Dual Zone | $45,000 | ML |
| AF-MAAP1-CS-4002-00 | Fire Warning Panel | 1 | BUY | Aural & Visual | $35,000 | ML |
| AF-MAAP1-CS-4005-00 | Smoke Detection System | 2 | BUY | Optical Sensor | $65,000 | ML |
| AF-MAAP1-CS-4010-00 | Cockpit Ventilation Fan (Emergency) | 1 | BUY | Smoke Evacuation | $25,000 | ML |

**Sub-total Fire Protection:** $170,000

**Total Group 15 (Crew Systems & Safety):** $2,650,500

---

#### 12.6 GROUP 16: GROUND HANDLING & SERVICING

##### 16.1.1 Towing & Jacking Equipment
**Drawing Reference:** AF-MAAP1-GH-1000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** SL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-GH-1001-00 | Nose Gear Tow Fitting | 1 | MAKE | Alloy Steel, 50K lbs | $35,000 | SL |
| AF-MAAP1-GH-1002-00 | Main Gear Jacking Point (Per Side) | 2 | MAKE | Reinforced Structure | $45,000 | SL |
| AF-MAAP1-GH-1005-00 | Fuselage Jacking Point | 2 | MAKE | Titanium Insert | $35,000 | SL |
| AF-MAAP1-GH-1010-00 | Leveling Sight Glass | 2 | BUY | Calibrated Indicator | $5,500 | SL |
| AF-MAAP1-GH-1015-00 | Tie-Down Anchor Points | 6 | MAKE | 15K lbs Each | $18,500 | SL |

**Sub-total Towing & Jacking:** $139,000

##### 16.1.2 Servicing Panels & Access
**Drawing Reference:** AF-MAAP1-GH-2000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-GH-2001-00 | Fuel Servicing Panel (Overwing) | 2 | MAKE | Al Alloy, Receptacle | $35,000 | ML |
| AF-MAAP1-GH-2002-00 | Single-Point Refuel Receptacle | 1 | BUY | Pressure Refuel | $85,000 | ML |
| AF-MAAP1-GH-2005-00 | Engine Oil Servicing Panel | 2 | MAKE | Quick-Fill Access | $15,000 | SL |
| AF-MAAP1-GH-2010-00 | Hydraulic Service Panel | 3 | MAKE | System A/B/Utility | $25,000 | ML |
| AF-MAAP1-GH-2015-00 | Oxygen Servicing Panel | 1 | MAKE | Ground Fill Interface | $18,500 | SL |
| AF-MAAP1-GH-2020-00 | Nitrogen Servicing Panel (Struts) | 3 | MAKE | Pressure Gauge Equipped | $12,500 | SL |
| AF-MAAP1-GH-2025-00 | Coolant Servicing Panel | 1 | MAKE | Avionics System | $15,000 | SL |
| AF-MAAP1-GH-2030-00 | Battery Access Panel | 2 | MAKE | Quick-Release Latches | $8,500 | SL |

**Sub-total Servicing Panels:** $214,500

##### 16.1.3 Ground Support Equipment Interfaces
**Drawing Reference:** AF-MAAP1-GH-3000-00  
**Quantity per Aircraft:** 1 Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** SL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-GH-3001-00 | Engine Air Start Manifold | 2 | BUY | Quick-Connect | $45,000 | ML |
| AF-MAAP1-GH-3002-00 | Ground Cooling Air Connection | 2 | BUY | 60 lb/min Supply | $35,000 | SL |
| AF-MAAP1-GH-3005-00 | Hydraulic Test Port Panel | 3 | MAKE | System Monitoring | $18,500 | SL |
| AF-MAAP1-GH-3010-00 | Electrical Load Bank Connection | 1 | BUY | System Testing | $25,000 | SL |
| AF-MAAP1-GH-3015-00 | Data Download Receptacle | 1 | BUY | MIL-STD-1553 | $45,000 | ML |
| AF-MAAP1-GH-3020-00 | Ground Hydraulic Supply Port | 1 | BUY | Emergency Backup | $35,000 | SL |

**Sub-total GSE Interfaces:** $203,500

##### 16.1.4 Maintenance Platforms & Stands
**Drawing Reference:** AF-MAAP1-GH-4000-00  
**Quantity per Aircraft:** N/A (Support Equipment)  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-GH-4001-00 | Cockpit Access Ladder | 1 | BUY | Aluminum, Wheeled | $12,500 | ML |
| AF-MAAP1-GH-4002-00 | Engine Maintenance Stand | 2 | BUY | Adjustable Height | $25,000 | ML |
| AF-MAAP1-GH-4005-00 | Wing Access Platform (Per Side) | 2 | BUY | Extendable | $35,000 | ML |
| AF-MAAP1-GH-4010-00 | Tail Section Work Platform | 1 | BUY | Safety Rails | $18,500 | ML |

**Sub-total Maintenance Platforms:** $91,000

**Total Group 16 (Ground Handling & Servicing):** $648,000

---

#### 12.7 GROUP 17: SPECIAL MISSION EQUIPMENT (Variant-Specific)

##### 17.1.1 Electronic Warfare Variant (EW-1) Equipment
**Drawing Reference:** AF-MAAP1-SM-1000-00  
**Quantity per Aircraft:** 1 Set (EW-1 Only)  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-SM-1001-00 | Electronic Attack Jamming Pod | 2 | BUY | Multi-Band, 10 kW | $3,850,000 | LL |
| AF-MAAP1-SM-1002-00 | SIGINT Collection System | 1 | BUY | Wideband Receiver | $2,450,000 | LL |
| AF-MAAP1-SM-1005-00 | EW Mission Computer | 1 | BUY | Threat Library | $1,250,000 | LL |
| AF-MAAP1-SM-1010-00 | Emitter Location System | 1 | BUY | Triangulation Array | $1,850,000 | LL |
| AF-MAAP1-SM-1015-00 | Electronic Support Pod | 2 | BUY | Passive Detection | $925,000 | LL |
| AF-MAAP1-SM-1020-00 | EW Operator Console (Rear Cockpit) | 1 | BUY | Multi-Function Display | $485,000 | ML |
| AF-MAAP1-SM-1025-00 | Data Link - Tactical EW | 1 | BUY | Secure Networking | $625,000 | LL |

**Sub-total EW Variant Equipment:** $11,435,000

##### 17.1.2 Reconnaissance Variant (RC-1) Equipment
**Drawing Reference:** AF-MAAP1-SM-2000-00  
**Quantity per Aircraft:** 1 Set (RC-1 Only)  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-SM-2001-00 | Multi-Spectral Imaging Pod | 1 | BUY | EO/IR/SAR | $4,250,000 | LL |
| AF-MAAP1-SM-2002-00 | Centerline Reconnaissance Pod | 1 | BUY | Wet Film/Digital | $2,850,000 | LL |
| AF-MAAP1-SM-2005-00 | Side-Looking Radar System | 1 | BUY | High Resolution SAR | $3,450,000 | LL |
| AF-MAAP1-SM-2010-00 | Imagery Data Recorder | 1 | BUY | 10 TB Solid State | $485,000 | ML |
| AF-MAAP1-SM-2015-00 | Real-Time Data Link System | 1 | BUY | Broadband SATCOM | $1,250,000 | LL |
| AF-MAAP1-SM-2020-00 | Reconnaissance Mission Computer | 1 | BUY | Image Processing | $825,000 | LL |
| AF-MAAP1-SM-2025-00 | Sensor Operator Console | 1 | BUY | Rear Cockpit Station | $625,000 | ML |

**Sub-total RC Variant Equipment:** $13,735,000

##### 17.1.3 Training Variant (T-1) Equipment
**Drawing Reference:** AF-MAAP1-SM-3000-00  
**Quantity per Aircraft:** 1 Set (T-1 Only)  
**Make/Buy:** BUY  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-SM-3001-00 | Dual Control Stick (Rear Cockpit) | 1 | BUY | Full Authority | $185,000 | ML |
| AF-MAAP1-SM-3002-00 | Instructor Override Panel | 1 | BUY | Safety Controls | $125,000 | ML |
| AF-MAAP1-SM-3005-00 | Training Mode Computer | 1 | BUY | Mission Simulation | $285,000 | ML |
| AF-MAAP1-SM-3010-00 | Flight Data Recorder (Enhanced) | 1 | BUY | Debrief Capability | $185,000 | ML |
| AF-MAAP1-SM-3015-00 | Intercom Enhancement System | 1 | BUY | Instructor Features | $45,000 | SL |
| AF-MAAP1-SM-3020-00 | Simulated Weapons Panel | 1 | BUY | Training Modes | $85,000 | ML |

**Sub-total Training Variant Equipment:** $910,000

##### 17.1.4 Export Variant (EX-1) Modifications
**Drawing Reference:** AF-MAAP1-SM-4000-00  
**Quantity per Aircraft:** 1 Set (EX-1 Only)  
**Make/Buy:** MAKE  
**Assembly Lead Time:** ML

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-SM-4001-00 | Downgraded Radar System | 1 | BUY | Reduced Capability | $2,850,000 | LL |
| AF-MAAP1-SM-4002-00 | Export-Approved EW Suite | 1 | BUY | Limited Frequency | $1,450,000 | LL |
| AF-MAAP1-SM-4005-00 | Non-Secure Communications Suite | 1 | BUY | Commercial Encryption | $485,000 | ML |
| AF-MAAP1-SM-4010-00 | Simplified Mission Computer | 1 | BUY | Restricted Software | $625,000 | ML |
| AF-MAAP1-SM-4015-00 | Export Datalink System | 1 | BUY | Link 16 Excluded | $385,000 | ML |

**Sub-total Export Variant Modifications:** $5,795,000

**Total Group 17 (Special Mission Equipment - Varies by Variant)**

---

#### 12.8 GROUP 18: PRODUCTION TOOLING & FIXTURES

##### 18.1.1 Major Assembly Fixtures
**Drawing Reference:** AF-MAAP1-TL-1000-00  
**Quantity:** Production Set  
**Make/Buy:** MAKE  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-TL-1001-00 | Fuselage Assembly Jig | 1 | MAKE | Precision Fixture | $2,850,000 | LL |
| AF-MAAP1-TL-1002-00 | Wing Assembly Fixture (Pair) | 1 | MAKE | Automated Positioning | $1,850,000 | LL |
| AF-MAAP1-TL-1005-00 | Wing-to-Fuselage Mating Jig | 1 | MAKE | Alignment System | $1,450,000 | LL |
| AF-MAAP1-TL-1010-00 | Empennage Assembly Fixture | 1 | MAKE | Multi-Position | $925,000 | LL |
| AF-MAAP1-TL-1015-00 | Nose Section Assembly Stand | 1 | MAKE | Rotational Capability | $485,000 | ML |
| AF-MAAP1-TL-1020-00 | Engine Installation Fixture | 2 | MAKE | Safety Certified | $385,000 | ML |
| AF-MAAP1-TL-1025-00 | Final Assembly Dolly System | 1 | MAKE | Motorized Transport | $625,000 | ML |

**Sub-total Major Assembly Fixtures:** $8,570,000

##### 18.1.2 Fabrication & Machining Tools
**Drawing Reference:** AF-MAAP1-TL-2000-00  
**Quantity:** Production Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-TL-2001-00 | 5-Axis CNC Machining Center | 4 | BUY | Aerospace Grade | $1,850,000 | LL |
| AF-MAAP1-TL-2002-00 | Automated Riveting System | 2 | BUY | Multi-Head | $2,450,000 | LL |
| AF-MAAP1-TL-2005-00 | Composite Layup Mandrels | 12 | MAKE | Precision Tooling | $285,000 | LL |
| AF-MAAP1-TL-2010-00 | Autoclave Tooling Set | 1 | MAKE | High-Temp Rated | $625,000 | LL |
| AF-MAAP1-TL-2015-00 | Forming Dies - Sheet Metal | 24 | MAKE | Hardened Steel | $185,000 | ML |
| AF-MAAP1-TL-2020-00 | Drill Templates & Jigs | 150 | MAKE | Precision Bushings | $125,000 | ML |

**Sub-total Fabrication Tools:** $5,520,000

##### 18.1.3 Quality Control & Inspection Equipment
**Drawing Reference:** AF-MAAP1-TL-3000-00  
**Quantity:** Production Set  
**Make/Buy:** BUY  
**Assembly Lead Time:** LL

| Part Number | Description | Qty | Make/Buy | Material/Spec | Unit Cost | Lead Time |
|-------------|-------------|-----|----------|---------------|-----------|-----------|
| AF-MAAP1-TL-3001-00 | Coordinate Measuring Machine (Large) | 2 | BUY | 20m x 5m x 4m | $1,250,000 | LL |
| AF-MAAP1-TL-3002-00 | Laser Tracker Measurement System | 4 | BUY | 0.001" Accuracy | $485,000 | ML |
| AF-MAAP1-TL-3005-00 | Ultrasonic Inspection System | 2 | BUY | Automated Scanner | $625,000 | LL |
| AF-MAAP1-TL-3010-00 | X-Ray Inspection System | 1 | BUY | Digital Radiography | $1,850,000 | LL |
| AF-MAAP1-TL-3015-00 | Eddy Current Test Equipment | 3 | BUY | Multi-Frequency | $285,000 | ML |
| AF-MAAP1-TL-3020-00 | Dye Penetrant Inspection Station | 2 | BUY | Automated Process | $185,000 | ML |
| AF-MAAP1-TL-3025-00 | Hardness Testing Equipment | 6 | BUY | Portable & Bench | $45,000 | SL |

**Sub-total Quality Control Equipment:** $4,725,000

**Total Group 18 (Production Tooling & Fixtures):** $18,815,000

---

## 13. CONSOLIDATED BOM SUMMARY BY AIRCRAFT GROUP

| Group | System/Assembly | Baseline Cost | Lead Time Category |
|-------|-----------------|---------------|-------------------|
| **Group 01** | Airframe Structure | $8,945,000 | LL/ML |
| **Group 02** | Propulsion System | $24,850,000 | LL |
| **Group 03** | Flight Control Systems | $7,280,000 | LL/ML |
| **Group 04** | Hydraulic Systems | $3,625,000 | ML |
| **Group 05** | Electrical Power Systems | $4,185,000 | LL/ML |
| **Group 06** | Avionics & Mission Systems | $18,450,000 | LL |
| **Group 07** | Communications Systems | $5,830,000 | LL |
| **Group 08** | Navigation Systems | $6,940,000 | LL |
| **Group 09** | Fuel System | $4,575,000 | ML |
| **Group 10** | Landing Gear System | $5,385,000 | LL |
| **Group 11** | Cockpit & Displays | $8,625,000 | LL/ML |
| **Group 12** | Armament & Mission Systems | $16,485,000 | LL/ML |
| **Group 13** | Auxiliary Power & Pneumatics | $7,342,000 | LL/ML |
| **Group 14** | Environmental Control Systems | $5,047,000 | LL/ML |
| **Group 15** | Crew Systems & Safety | $2,650,500 | LL/ML |
| **Group 16** | Ground Handling & Servicing | $648,000 | SL/ML |
| **Group 17** | Special Mission Equipment* | Varies by Variant | LL |
| **Group 18** | Production Tooling & Fixtures** | $18,815,000 | LL |

**\*Group 17 Variant Costs:**
- EW-1 Electronic Warfare: +$11,435,000
- RC-1 Reconnaissance: +$13,735,000
- T-1 Training: +$910,000
- EX-1 Export: +$5,795,000 (net reduction with downgrades)

**\*\*Group 18 represents non-recurring production investment**

---

## 14. TOTAL AIRCRAFT COST SUMMARY

### 14.1 Baseline Fighter (F-1) Variant

| Cost Category | Amount | Notes |
|---------------|--------|-------|
| **Recurring Airframe & Systems (Groups 1-16)** | $130,862,500 | Per Aircraft |
| **Engine Set (2x Engines)** | $24,850,000 | Included in Group 02 |
| **Government Furnished Equipment (GFE)** | $3,500,000 | External Weapons, Support Equipment |
| **Engineering Support (5%)** | $6,543,125 | Recurring Engineering |
| **Quality Assurance (3%)** | $3,925,875 | Inspection & Testing |
| **Program Management (4%)** | $5,234,500 | Recurring Management |
| **Subtotal Flyaway Cost** | $150,066,000 | **Per Aircraft** |
| **Profit Margin (8%)** | $12,005,280 | Industry Standard |
| **Total Unit Procurement Cost (UPUC)** | **$162,071,280** | **Baseline F-1 Variant** |

### 14.2 Variant-Specific Costs (Incremental to Baseline)

| Variant | Additional Equipment | Total UPUC |
|---------|---------------------|------------|
| **F-1 (Baseline Fighter)** | $0 | $162,071,280 |
| **EW-1 (Electronic Warfare)** | +$11,435,000 | $173,506,280 |
| **RC-1 (Reconnaissance)** | +$13,735,000 | $175,806,280 |
| **T-1 (Advanced Trainer)** | +$910,000 | $162,981,280 |
| **EX-1 (Export)** | +$5,795,000 | $167,866,280 |

### 14.3 Non-Recurring Costs (Program Level)

| Category | Amount | Amortization |
|----------|--------|--------------|
| **Production Tooling & Fixtures** | $18,815,000 | Over 100 Aircraft |
| **Engineering Development** | $450,000,000 | Design, Analysis, Testing |
| **Flight Test Program** | $185,000,000 | 6 Test Aircraft |
| **Certification & Qualification** | $95,000,000 | FAA/Military Certification |
| **Supplier Qualification** | $45,000,000 | Supply Chain Development |
| **Total Non-Recurring Cost** | **$793,815,000** | **One-Time Investment** |
| **Cost per Aircraft (100 unit production)** | **+$7,938,150** | Amortized NRC |

### 14.4 Program Unit Cost (Including NRC Amortization)

| Variant | UPUC | Amortized NRC | **Program Unit Cost** |
|---------|------|---------------|----------------------|
| **F-1 (Baseline)** | $162,071,280 | +$7,938,150 | **$170,009,430** |
| **EW-1** | $173,506,280 | +$7,938,150 | **$181,444,430** |
| **RC-1** | $175,806,280 | +$7,938,150 | **$183,744,430** |
| **T-1** | $162,981,280 | +$7,938,150 | **$170,919,430** |
| **EX-1** | $167,866,280 | +$7,938,150 | **$175,804,430** |

---

## 15. MATERIAL SPECIFICATIONS & STANDARDS REFERENCE

### 15.1 Primary Materials

| Material Designation | Specification | Primary Application | Suppliers |
|---------------------|---------------|---------------------|-----------|
| **Ti-6Al-4V** | AMS 4911 | Primary Structure, Hardpoints | TIMET, ATI Metals |
| **Al 7050-T7451** | AMS 4050 | Fuselage Frames, Bulkheads | Alcoa, Kaiser |
| **Al 2024-T3** | AMS 4037 | Wing Skins, Secondary Structure | Multiple Certified |
| **CRES 15-5PH** | AMS 5659 | Landing Gear Components | Carpenter Steel |
| **Inconel 718** | AMS 5662 | Engine Mounts, Hot Sections | Special Metals |
| **Carbon Fiber Prepreg** | Hexcel 8552/IM7 | Control Surfaces, Fairings | Hexcel, Cytec |
| **Epoxy Composite** | Cytec 977-2 | Radomes, Non-Structural | Cytec, Toray |

### 15.2 Fastener Standards

| Type | Specification | Application | Material |
|------|---------------|-------------|----------|
| **Hi-Lok Fasteners** | MS20426 | Primary Structure Joints | Ti or CRES |
| **Aerospace Rivets** | MS20470 | Secondary Structure | Al Alloy |
| **Titanium Bolts** | MS21250 | High-Strength Joints | Ti-6Al-4V |
| **Lock Nuts** | MS21042 | Vibration-Critical | CRES |
| **Panel Fasteners** | MS21983 | Access Panels | Al or CRES |

### 15.3 Fluid & Sealant Specifications

| Product | Specification | Application | Manufacturer |
|---------|---------------|-------------|--------------|
| **Fuel Tank Sealant** | MIL-S-81733 | Integral Tanks | PPG PR-1776 |
| **Fay Surface Sealant** | MIL-S-8802 | Structural Joints | Henkel EA-9394 |
| **Hydraulic Fluid** | MIL-PRF-83282 | All Hydraulic Systems | Exxon HyJet IV-A |
| **Engine Oil** | MIL-PRF-23699 | Turbine Engines | Mobil Jet Oil II |
| **Coolant (PAO)** | MIL-PRF-87252 | Avionics Cooling | Dow Corning |

### 15.4 Process Specifications

| Process | Specification | Application | Critical Parameters |
|---------|---------------|-------------|---------------------|
| **Anodizing** | MIL-A-8625 Type II | Corrosion Protection | Thickness: 0.0002"-0.001" |
| **Cadmium Plating** | QQ-P-416 Type II | Fastener Protection | Class 2 Finish |
| **Shot Peening** | MIL-S-13165 | Fatigue Resistance | Almen Intensity: 0.008"-0.012"A |
| **Heat Treatment** | AMS 2759 | Aluminum Strengthening | T6/T7 Tempers |
| **Welding - Titanium** | AWS D17.1 | Structural Welding | TIG/Electron Beam |
| **NDT - Ultrasonic** | MIL-STD-410 | Internal Defect Detection | Level II Certified |

---

## 16. LEAD TIME DEFINITIONS & PROCUREMENT STRATEGY

### 16.1 Lead Time Categories

| Category | Duration | Typical Items | Procurement Strategy |
|----------|----------|---------------|---------------------|
| **SL (Short Lead)** | 0-12 weeks | COTS Hardware, Standard Fasteners | Blanket Orders, Consignment |
| **ML (Medium Lead)** | 12-26 weeks | Machined Parts, Assemblies | Scheduled Releases, Buffer Stock |
| **LL (Long Lead)** | 26-52+ weeks | Engines, Avionics, Forgings | Early Commitment, Multi-Year Contracts |
| **Critical Path** | 52+ weeks | Ejection Seats, Radar, Engines | Advance Procurement, Dual Source |

### 16.2 Make vs. Buy Decision Matrix

| Criteria | MAKE Decision Factors | BUY Decision Factors |
|----------|----------------------|---------------------|
| **Technology** | Core Competency, Proprietary Design | Specialized Technology, Patent Restricted |
| **Cost** | High Volume, Economies of Scale | Low Volume, Capital Intensive |
| **Quality** | Critical Characteristics, Tight Tolerances | Certified Supplier, Proven Performance |
| **Schedule** | Existing Capacity, Flexible | Supplier Reliability, Shorter Lead |
| **Risk** | Control Over Process | Supplier Financial Stability |

### 16.3 Critical Path Items (Requiring Early Action)

| Part Number | Description | Lead Time | Mitigation Strategy |
|-------------|-------------|-----------|---------------------|
| AF-MAAP1-PR-1001-00 | Turbofan Engine Assembly | 52+ weeks | Multi-Year Contract, Engine Bank |
| AF-MAAP1-AV-1001-00 | AESA Radar System | 48 weeks | Early Design Release, Advance Payment |
| AF-MAAP1-CS-1001-00 | Ejection Seat Assembly | 44 weeks | Supplier Partnership, Safety Stock |
| AF-MAAP1-LG-1001-00 | Main Landing Gear Forging | 40 weeks | Forging Pre-Buy, Dual Source |
| AF-MAAP1-EL-1001-00 | Main Generator | 36 weeks | Vendor Managed Inventory |
| AF-MAAP1-AR-3001-00 | Advanced Targeting Pod | 36 weeks | Government Furnished Equipment Option |

### 16.4 Supplier Quality Requirements

| Certification | Required For | Audit Frequency |
|---------------|--------------|-----------------|
| **AS9100D** | All Tier 1 Suppliers | Annual |
| **NADCAP** | Special Processes (Heat Treat, NDT, Welding) | Every 2 Years |
| **ISO 9001** | Tier 2/3 Suppliers | Every 3 Years |
| **ITAR Registration** | All Export-Controlled Items | Continuous |
| **First Article Inspection (FAI)** | New Parts, Design Changes | Per Lot/Change |

---

## 17. CONFIGURATION MANAGEMENT & REVISION CONTROL

### 17.1 Drawing Revision Levels

| Revision | Date | Description | Approved By | ECO Number |
|----------|------|-------------|-------------|------------|
| **-** | 2025-01-15 | Initial Release | Chief Engineer | N/A |
| **A** | TBD | Supplier Feedback Incorporation | Configuration Board | ECO-MAAP1-001 |
| **B** | TBD | First Article Test Results | Configuration Board | ECO-MAAP1-002 |

### 17.2 Engineering Change Order (ECO) Process

**Class I Changes (Major):**
- Affect form, fit, function, or interchangeability
- Require customer/program office approval
- Trigger configuration audit
- Examples: Material changes, dimension changes >0.010", interface modifications

**Class II Changes (Minor):**
- Editorial, clarification, or process improvements
- Internal approval authority
- No impact on certification
- Examples: Note additions, drawing cleanup, tolerance clarifications

### 17.3 BOM Effectivity

| Effectivity | Aircraft Serial Numbers | Variant | Implementation Date |
|-------------|------------------------|---------|---------------------|
| **All** | 001-100 | Baseline F-1 | Production Start |
| **EW** | Per Order | EW-1 Specific | Customer Specified |
| **RC** | Per Order | RC-1 Specific | Customer Specified |
| **TR** | Per Order | T-1 Specific | Customer Specified |
| **EX** | 201+ | Export Variant | FMS Approval Required |

---

## 18. QUALITY ASSURANCE & ACCEPTANCE CRITERIA

### 18.1 Inspection Levels by Group

| Group | Inspection Type | Sample Size | Accept/Reject Criteria |
|-------|----------------|-------------|------------------------|
| **Group 01 (Structure)** | 100% Dimensional, 10% NDT | All/Sample | AQL 0.65, Zero Defects Critical |
| **Group 02 (Propulsion)** | Witness Test, Log Book Review | 100% | Per Engine OEM Specification |
| **Group 03-16 (Systems)** | First Article + Production Sample | Per MIL-STD-105E | AQL 1.0 Major, 2.5 Minor |
| **Group 17 (Mission Equipment)** | Functional Test | 100% | Performance Specification Compliance |

### 18.2 Critical Characteristics

**Identified with ◆ symbol on drawings:**
- Wing spar cap thickness and material
- Landing gear attachment fittings
- Engine mount interfaces
- Flight control actuator mounting
- Fuel tank sealant integrity
- Ejection seat cartridge specifications

### 18.3 Acceptance Test Requirements

| Test | Specification | Frequency | Location |
|------|---------------|-----------|----------|
| **Structural Proof Test** | 150% Limit Load | First 3 Aircraft | OEM Facility |
| **Lightning Strike** | MIL-STD-464 | Qualification | Test Lab |
| **Hydraulic System Proof** | 1.5x Operating Pressure | Every Aircraft | Final Assembly |
| **Avionics Integration** | System Spec Compliance | Every Aircraft | Final Assembly |
| **Engine Run** | Full Throttle Cycle | Every Aircraft | OEM Test Cell |
| **Flight Test** | Envelope Clearance | First 6 Aircraft | Flight Test Center |

---

## 19. LOGISTICS & SPARES PROVISIONING

### 19.1 Recommended Spares (Per 10 Aircraft)

| Category | Quantity | Justification |
|----------|----------|---------------|
| **Engines (Complete)** | 2 | War Reserve, Depot Maintenance |
| **Landing Gear Assemblies** | 1 Set | High-Wear, Long Lead |
| **Ejection Seats** | 2 | Safety Critical, Expiration Dates |
| **Flight Control Computers** | 4 | High Failure Rate Component |
| **Hydraulic Pumps** | 6 | Wear Item, Mission Critical |
| **Generators** | 4 | Electrical System Redundancy |
| **AESA Radar Modules** | 20 | Line Replaceable Units |
| **Consumables (Seals, Filters)** | 12 Months | Scheduled Maintenance |

### 19.2 Maintenance Planning

| Level | Location | Capability | Interval |
|-------|----------|------------|----------|
| **Organizational** | Flight Line | Pre/Post Flight, Servicing | Daily |
| **Intermediate** | Base Maintenance | Component R&R, Troubleshooting | 100 Flight Hours |
| **Depot** | OEM/Depot Facility | Structural Inspection, Overhaul | 2000 Flight Hours |

---

## 20. EXPORT CONTROL & COMPLIANCE

### 20.1 ITAR Classification

| System | USML Category | Export License Required |
|--------|---------------|------------------------|
| **Complete Aircraft** | VIII(a) | Yes - State Department |
| **Engines** | VIII(h)(6) | Yes |
| **AESA Radar** | XI(a)(3) | Yes - Restricted |
| **EW Systems** | XI(a)(5) | Yes - Case-by-Case |
| **Ejection Seats** | VIII(h)(8) | Yes |
| **Training Variant** | VIII(a) | Yes - Relaxed Review |

### 20.2 EX-1 Variant Compliance Strategy

**Downgraded Systems (Exportable):**
- Radar: Reduced range and tracking capacity
- EW Suite: Limited frequency coverage
- Datalink: Excludes classified waveforms
- Mission Computer: Restricted software build
- Communications: Commercial encryption only

**Retained Capabilities:**
- Airframe and flight performance
- Basic weapons delivery
- Navigation systems
- Environmental controls
- Safety systems

---

## 21. DOCUMENT CONTROL & DISTRIBUTION

### 21.1 Authorized