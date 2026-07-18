# DRAWING TREE / CONFIGURATION BREAKDOWN STRUCTURE
## MAAP-1F "WILDFIRE" FIREFIGHTING VARIANT
## Tandem-Rotor Heavy-Lift Autonomous Aerial Firefighting Helicopter

---

| | |
|---|---|
| **Document No.** | AF-MAAP1F-DT-0003 |
| **Revision** | A (Initial Release) |
| **Classification** | Eurus Systems Proprietary — Export Controlled (ITAR/EAR Applicable) |
| **Derived From** | Program Requirements Baseline AF-MAAP1-PRB-0001, Rev A<br>Key Specifications Document AF-MAAP1-KSD-0002, Rev A |
| **Configuration** | MAAP-1F "Wildfire" Firefighting Variant |
| **Owner** | MAAP-1F Variant Chief Engineer |
| **Date** | [Current Date] |
| **Effectivity** | All MAAP-1F aircraft, serial numbers FF-0001 through FF-9999 |

---

## DRAWING TREE ORGANIZATION

This Drawing Tree establishes the hierarchical configuration breakdown for the MAAP-1F Firefighting variant. The tree is organized into the following levels:

- **Level 0:** Complete Aircraft
- **Level 1:** Major Assemblies (Green Aircraft + Firefighting Mission Systems)
- **Level 2:** Primary Subassemblies
- **Level 3:** Major Components
- **Level 4:** Detail Components and Line Replaceable Units (LRUs)
- **Level 5:** Subcomponent Details (where applicable for critical firefighting systems)

**Common Configuration Boundary:**
Per PRB Section 5.1, all assemblies designated as "Green Aircraft" (shaded entries) are common across MAAP-1C/1F/1I variants and maintained under unified configuration control. Firefighting variant-unique assemblies are designated with suffix "-FF" nomenclature.

**Drawing Number Convention:**
- **AF-MAAP1F-XX-YYYY-ZZ**
  - **AF:** AetherForge Program
  - **MAAP1F:** MAAP-1 Firefighting Variant
  - **XX:** Level number (01-05)
  - **YYYY:** Sequential assembly number
  - **ZZ:** Dash number for configuration variants

---

## LEVEL 0: COMPLETE AIRCRAFT

**AF-MAAP1F-00-0001 — MAAP-1F "WILDFIRE" COMPLETE AIRCRAFT ASSEMBLY**

Top-level assembly drawing defining the firefighting variant complete aircraft configuration including:
- Green Aircraft baseline airframe and dynamic systems
- Firefighting mission equipment package
- Water/retardant tank system
- Fire detection and mapping sensors
- Optionally-piloted crew station (removable configuration)
- External firefighting load provisions (Bambi bucket hardpoints)

**Configuration:** Optionally-piloted (SAE Level 2 autonomy at IOC, Level 3 by FOC per PRB Section 3.5)

**Reference Documents:**
- AF-MAAP1-PRB-0001 (Program Requirements Baseline)
- AF-MAAP1-KSD-0002 (Key Specifications Document)
- AF-MAAP1F-ICD-007 (Firefighting Mission Systems Interface Control Document)
- AF-MAAP1F-SRD-0004 (MAAP-1F System Requirements Document)

---

## LEVEL 1: MAJOR ASSEMBLIES

### 1.0 GREEN AIRCRAFT ASSEMBLIES (Common to all variants)

**AF-MAAP1-01-1000 — FORWARD ROTOR PYLON ASSEMBLY** *(Green Aircraft - Common)*
- Complete forward rotor system including hub, blades, transmission, and pylon structure
- Reference: Common configuration per ICD-001

**AF-MAAP1-01-1100 — AFT ROTOR PYLON ASSEMBLY** *(Green Aircraft - Common)*
- Complete aft rotor system including hub, blades, transmission, and pylon structure
- Reference: Common configuration per ICD-001

**AF-MAAP1-01-1200 — INTERCONNECT DRIVE SHAFT ASSEMBLY** *(Green Aircraft - Common)*
- Synchronizing shaft between forward and aft transmissions
- Torque rating: 5,400 shp (takeoff power)

**AF-MAAP1-01-2000 — FORWARD FUSELAGE ASSEMBLY** *(Green Aircraft - Common)*
- Primary load-bearing composite fuselage structure forward of Mission Bay
- Cockpit/crew station interface provisions (firefighting variant: dual-pilot station installed)

**AF-MAAP1-01-2100 — AFT FUSELAGE ASSEMBLY** *(Green Aircraft - Common)*
- Primary composite fuselage structure aft of Mission Bay
- Tailcone integration interface

**AF-MAAP1-01-2200 — MISSION BAY STRUCTURE ASSEMBLY** *(Green Aircraft - Common with FF-specific hardpoints)*
- Central fuselage section housing mission equipment
- Firefighting variant: Reinforced floor structure for internal water/retardant tank installation
- Tank attach hardpoints per ICD-007

**AF-MAAP1-01-2300 — TAILCONE ASSEMBLY** *(Green Aircraft - Common)*
- Aft aerodynamic fairing and structural closeout
- Environmental sensor mounting provisions

**AF-MAAP1-01-3000 — PROPULSION SYSTEM ASSEMBLY** *(Green Aircraft - Common)*
- Twin turboshaft engines, nacelles, engine controls, fuel system core

**AF-MAAP1-01-4000 — LANDING GEAR SYSTEM ASSEMBLY** *(Green Aircraft - Common)*
- Fixed tricycle landing gear with crashworthy energy attenuation
- Designed for unimproved landing zone operations

**AF-MAAP1-01-5000 — FLIGHT CONTROL SYSTEM ASSEMBLY** *(Green Aircraft - Common)*
- Triplex digital fly-by-wire primary flight controls
- Autonomous GNC computer core
- Variant parameter tables loaded for firefighting flight envelope

**AF-MAAP1-01-6000 — ELECTRICAL POWER GENERATION & DISTRIBUTION ASSEMBLY** *(Green Aircraft - Common)*
- Dual-redundant generators, battery system, primary electrical bus architecture

**AF-MAAP1-01-7000 — CORE AVIONICS SUITE ASSEMBLY** *(Green Aircraft - Common)*
- Mission computers (hardware), communication systems, navigation systems
- MOSA-compliant open architecture per PRB Section 6

**AF-MAAP1-01-8000 — ENVIRONMENTAL CONTROL SYSTEM (ECS) ASSEMBLY** *(Green Aircraft - Common)*
- Core heating/cooling distribution system
- Firefighting variant: Enhanced cooling package for high-temperature operations

---

### 2.0 FIREFIGHTING VARIANT-UNIQUE ASSEMBLIES

**AF-MAAP1F-01-9000-FF — INTERNAL WATER/RETARDANT TANK SYSTEM ASSEMBLY**
- 2,000-gallon (7,570 L) capacity internal belly-mounted tank system
- Integrated fill, discharge, and control subsystems
- Primary firefighting payload delivery system

**AF-MAAP1F-01-9100-FF — EXTERNAL FIREFIGHTING LOAD PROVISIONS ASSEMBLY**
- Dual cargo hook system (forward/aft) for external firefighting buckets
- Bambi bucket interface hardpoints (up to 2,600-gallon capacity)
- Load monitoring and automatic release system

**AF-MAAP1F-01-9200-FF — FIRE DETECTION & MAPPING SENSOR SUITE ASSEMBLY**
- Forward-looking infrared (FLIR) thermal imaging system
- Fire hotspot detection and tracking algorithms
- Real-time fire perimeter mapping sensors

**AF-MAAP1F-01-9300-FF — FIREFIGHTING MISSION AVIONICS ASSEMBLY**
- Firefighting-specific mission software applications
- Drop pattern calculation and guidance system
- Fire line overlay display system
- Integration with GCS firefighting mission planning tools

**AF-MAAP1F-01-9400-FF — PILOT CREW STATION ASSEMBLY (OPTIONALLY-PILOTED CONFIGURATION)**
- Dual-pilot cockpit with firefighting-specific displays
- Manual flight control override interfaces
- Removable configuration (<8 labor-hours per PRB Section 3.5)
- Transition path to autonomous-only operations by FOC

**AF-MAAP1F-01-9500-FF — WATER SCOOPING SYSTEM ASSEMBLY (OPTIONAL KIT)**
- Retractable snorkel fill probe for hover-fill from natural water sources
- High-volume pump system (500 GPM fill rate target)
- Automatic fill control and tank level monitoring

**AF-MAAP1F-01-9600-FF — RETARDANT INJECTION & FOAM SYSTEM ASSEMBLY (OPTIONAL KIT)**
- Fire retardant chemical injection system for internal tank
- Foam concentrate tank and proportioning system
- Retardant mix ratio control (adjustable 0.5% to 8% concentration)

---

## LEVEL 2: PRIMARY SUBASSEMBLIES

### 2.1 FORWARD ROTOR PYLON ASSEMBLY (AF-MAAP1-01-1000)

**AF-MAAP1-02-1001 — Forward Rotor Hub Assembly** *(Green Aircraft)*
- Fully-articulated four-blade hub with elastomeric bearings
- Blade attachment fittings and pitch control mechanisms

**AF-MAAP1-02-1002 — Forward Rotor Blade Set (4 blades)** *(Green Aircraft)*
- Composite construction, 21 ft chord, -12° twist
- Titanium leading edge erosion strips
- Individual blade drawing: AF-MAAP1-03-1002-01 through -04

**AF-MAAP1-02-1003 — Forward Transmission Assembly** *(Green Aircraft)*
- Split-torque planetary transmission
- Power rating: 2,700 shp continuous (per rotor)
- Interconnect shaft drive interface

**AF-MAAP1-02-1004 — Forward Pylon Structure Assembly** *(Green Aircraft)*
- Composite and metallic hybrid pylon structure
- Vibration isolation mounts
- Pylon fairing and aerodynamic enclosure

**AF-MAAP1-02-1005 — Forward Rotor Swashplate & Actuator Assembly** *(Green Aircraft)*
- Stationary and rotating swashplate components
- Three electro-hydraulic actuators (triplex redundancy)
- Position feedback sensors

---

### 2.2 AFT ROTOR PYLON ASSEMBLY (AF-MAAP1-01-1100)

**AF-MAAP1-02-1101 — Aft Rotor Hub Assembly** *(Green Aircraft)*
- Mirror image of forward hub, counter-rotating configuration

**AF-MAAP1-02-1102 — Aft Rotor Blade Set (4 blades)** *(Green Aircraft)*
- Identical to forward rotor blades (interchangeable)

**AF-MAAP1-02-1103 — Aft Transmission Assembly** *(Green Aircraft)*
- Identical configuration to forward transmission

**AF-MAAP1-02-1104 — Aft Pylon Structure Assembly** *(Green Aircraft)*
- 4-inch vertical offset relative to forward pylon (optimizes rotor overlap efficiency)

**AF-MAAP1-02-1105 — Aft Rotor Swashplate & Actuator Assembly** *(Green Aircraft)*
- Identical to forward rotor configuration

---

### 2.3 INTERNAL WATER/RETARDANT TANK SYSTEM (AF-MAAP1F-01-9000-FF)

**AF-MAAP1F-02-9001-FF — Primary Tank Structure Assembly**
- 2,000-gallon capacity internal tank
- Composite construction with internal baffles
- Crashworthy design per MIL-STD-1290
- Tank attach fittings interface to Mission Bay hardpoints

**AF-MAAP1F-02-9002-FF — Tank Fill System Assembly**
- Gravity fill port (60 GPM) and pressure refill port (150 GPM)
- Fill valve controls and automatic shutoff at capacity
- Snorkel fill interface provisions (optional kit integration point)

**AF-MAAP1F-02-9003-FF — Tank Discharge System Assembly**
- Electrically-actuated dump gates (primary and secondary doors)
- Programmable salvo/ripple release valves
- Emergency full-dump override control

**AF-MAAP1F-02-9004-FF — Tank Level & CG Management System Assembly**
- Capacitive fuel quantity indicating system (adapted for water/retardant)
- Real-time CG calculation and display
- Automatic ballast control integration with flight control system

**AF-MAAP1F-02-9005-FF — Tank Pressurization & Vent System Assembly**
- RAM air scoop pressurization for positive discharge pressure
- Overpressure relief valves
- Anti-slosh venting system

**AF-MAAP1F-02-9006-FF — Retardant Mixing & Distribution Manifold Assembly**
- Internal tank distribution piping for retardant injection
- Mixing nozzles for uniform retardant concentration
- Flushing system for post-mission cleaning

---

### 2.4 EXTERNAL FIREFIGHTING LOAD PROVISIONS (AF-MAAP1F-01-9100-FF)

**AF-MAAP1F-02-9101-FF — Forward Cargo Hook Assembly**
- Electrically-actuated cargo hook, 12,000 lb rating (Threshold) / 16,000 lb (Objective)
- Bambi bucket quick-release interface
- Emergency release override (<0.5 sec actuation)

**AF-MAAP1F-02-9102-FF — Aft Cargo Hook Assembly**
- Identical to forward hook, independent release control
- Dual-load tandem configuration capability (8,000 lb + 8,000 lb)

**AF-MAAP1F-02-9103-FF — External Load Monitoring System Assembly**
- Load cell instrumentation (weight measurement ±50 lb accuracy)
- Pendulum angle sensors (±2° accuracy)
- Load stability monitoring and automatic damping control

**AF-MAAP1F-02-9104-FF — Belly Camera System (External Load View)**
- Three EO/IR cameras (forward, aft, load view)
- Operator pan/tilt/zoom control from crew station or GCS
- Real-time video feed to cockpit displays and GCS

**AF-MAAP1F-02-9105-FF — Water Fill Hose & Nozzle Assembly (for Bambi bucket ops)**
- Retractable hose reel system
- Remote-controlled fill nozzle for bucket filling on ground
- 100 GPM fill rate capability

---

### 2.5 FIRE DETECTION & MAPPING SENSOR SUITE (AF-MAAP1F-01-9200-FF)

**AF-MAAP1F-02-9201-FF — Forward-Looking Infrared (FLIR) Turret Assembly**
- Multi-sensor stabilized turret: MWIR and LWIR thermal cameras
- 360° continuous rotation, -120° to +30° elevation
- Fire hotspot detection algorithms (automatic threshold-based alerting)

**AF-MAAP1F-02-9202-FF — Fire Perimeter Mapping Sensor Assembly**
- Wide-area thermal scanner with geo-referencing
- Real-time fire edge detection and mapping overlay
- Integration with GIS fire management systems

**AF-MAAP1F-02-9203-FF — Smoke Penetration LIDAR Assembly (Optional)**
- Laser-based terrain mapping through smoke obscuration
- Obstacle detection and autonomous landing zone identification
- Range: 500 m in heavy smoke conditions

**AF-MAAP1F-02-9204-FF — Environmental Sensor Package Assembly**
- Wind speed/direction anemometer (roof-mounted)
- Temperature and humidity sensors
- Barometric pressure sensor for fire behavior prediction

**AF-MAAP1F-02-9205-FF — Datalink Relay System for Ground Firefighting Teams**
- UHF/VHF voice relay for firefighter communications
- Data relay for ground team GPS positions and sensor data
- Integration with incident command communication networks

---

### 2.6 FIREFIGHTING MISSION AVIONICS (AF-MAAP1F-01-9300-FF)

**AF-MAAP1F-02-9301-FF — Firefighting Mission Computer Assembly**
- High-performance mission processor running firefighting-specific software
- Drop pattern calculation algorithms (GPS-guided corridor, salvo/ripple sequencing)
- Fire behavior modeling and prediction software integration

**AF-MAAP1F-02-9302-FF — Drop Control System Assembly**
- Programmable release sequencing controller
- GPS waypoint-triggered automatic release
- Manual override controls (pilot-initiated drop)

**AF-MAAP1F-02-9303-FF — Fire Line Overlay Display System Assembly**
- Real-time fire perimeter overlay on moving map display
- Drop pattern visualization and planning tool
- Integration with National Interagency Fire Center (NIFC) data feeds

**AF-MAAP1F-02-9304-FF — Autonomous Drop Mission Planner Software Module**
- Pre-mission drop pattern planning and optimization
- Terrain avoidance and optimal drop altitude calculation
- Multi-pass mission sequencing for sustained suppression operations

**AF-MAAP1F-02-9305-FF — GCS Firefighting Interface Software Package**
- Ground control station firefighting-specific displays
- Remote drop authorization and mission modification
- Real-time fire intelligence sharing with incident command

---

### 2.7 PILOT CREW STATION ASSEMBLY (AF-MAAP1F-01-9400-FF)

**AF-MAAP1F-02-9401-FF — Pilot Seats & Crashworthy Structure Assembly**
- Dual crashworthy pilot seats (energy attenuation per MIL-STD-1290)
- Quick-release seat mounting for crew station removal
- 5-point restraint harnesses with inertial reel systems

**AF-MAAP1F-02-9402-FF — Pilot Flight Control Interfaces Assembly**
- Cyclic and collective controls with force-feedback
- Anti-torque pedals
- Manual override of autonomous flight control modes

**AF-MAAP1F-02-9403-FF — Cockpit Display Suite Assembly**
- Multi-function displays (3× 10-inch touch-capable screens per pilot)
- Firefighting-specific display formats: fire map overlay, drop visualization, tank status
- Head-Up Display (HUD) with fire line guidance symbology (optional)

**AF-MAAP1F-02-9404-FF — Pilot Communication & Audio Panel Assembly**
- Dual VHF/UHF radios (firefighting air-to-air and air-to-ground frequencies)
- Integration with incident command radio networks
- Active noise reduction (ANR) headset interfaces

**AF-MAAP1F-02-9405-FF — Cockpit Environmental Control Module**
- Supplemental air conditioning for cockpit (high-temperature firefighting operations)
- Smoke filtration and positive pressure system
- Cockpit temperature target: ≤30°C in +49°C ambient with fire proximity heat load

**AF-MAAP1F-02-9406-FF — Emergency Egress & Crew Protection Systems Assembly**
- Crashworthy windscreen and side windows
- Emergency egress window jettison system
- Fire-resistant cockpit materials and coatings

---

### 2.8 WATER SCOOPING SYSTEM (AF-MAAP1F-01-9500-FF) — OPTIONAL KIT

**AF-MAAP1F-02-9501-FF — Retractable Snorkel Probe Assembly**
- Articulating snorkel arm with 15 ft extension (deployed)
- Hydraulic extension/retraction mechanism
- Automatic stow position with aerodynamic fairing

**AF-MAAP1F-02-9502-FF — High-Volume Water Pump Assembly**
- Centrifugal pump driven by hydraulic motor
- Flow rate: 500 GPM (target) at hover-fill altitude
- Inlet debris screen (prevents ingestion of rocks/vegetation)

**AF-MAAP1F-02-9503-FF — Snorkel Fill Control System Assembly**
- Automatic hover altitude hold during fill operations
- Tank level monitoring with automatic shutoff at capacity
- Pilot/GCS-initiated fill start/stop controls

**AF-MAAP1F-02-9504-FF — Water Source Detection & Assessment System**
- Downward-looking LIDAR for water surface detection
- Depth estimation algorithm (minimum depth: 3 ft for safe scooping)
- Water quality sensor (salinity detection for corrosion prevention)

---

### 2.9 RETARDANT INJECTION & FOAM SYSTEM (AF-MAAP1F-01-9600-FF) — OPTIONAL KIT

**AF-MAAP1F-02-9601-FF — Fire Retardant Concentrate Tank Assembly**
- 200-gallon capacity auxiliary tank for retardant concentrate
- Chemical-resistant tank material (compatible with long-term fire retardants)
- Separate fill port and level indication

**AF-MAAP1F-02-9602-FF — Retardant Injection Pump & Proportioning System Assembly**
- Positive-displacement metering pump
- Variable mix ratio control: 0.5% to 8% retardant concentration
- Automatic proportioning based on main tank discharge flow rate

**AF-MAAP1F-02-9603-FF — Foam Concentrate Tank & System Assembly**
- 150-gallon foam concentrate tank (Class A foam for wildland fires)
- Foam proportioning system (0.5% to 3% foam concentration)
- Eductor-based mixing for uniform foam generation

**AF-MAAP1F-02-9604-FF — Chemical Mixing Manifold & Distribution Assembly**
- Injection nozzles in main tank discharge piping
- Static mixers for uniform retardant/foam distribution
- Flushing system with freshwater rinse capability

**AF-MAAP1F-02-9605-FF — Retardant/Foam Tank Flushing & Cleaning System**
- Integrated flushing manifold with spray nozzles
- Post-mission automated cleaning cycle (10-minute flush duration)
- Wastewater discharge port with environmental containment provisions

---

## LEVEL 3: MAJOR COMPONENTS

### 3.1 PRIMARY TANK STRUCTURE (AF-MAAP1F-02-9001-FF)

**AF-MAAP1F-03-9001-01-FF — Main Tank Shell Assembly**
- Composite tank body: carbon fiber outer skin, Kevlar inner liner
- Dimensions: 180 in (L) × 60 in (W) × 48 in (H)
- Internal volume: 2,000 gallons (7,570 liters) usable capacity
- Design pressure: 5 psi internal, crash load per MIL-STD-1290

**AF-MAAP1F-03-9001-02-FF — Tank Baffle System Assembly**
- Six longitudinal baffles and four lateral baffles
- Anti-slosh design: limits fluid CG shift to ±4 inches during maneuvers
- Drain holes for complete tank drainage (post-mission cleaning)

**AF-MAAP1F-03-9001-03-FF — Tank Attach Hardpoint Fittings (8 places)**
- Titanium attach fittings bonded to composite tank shell
- Interface with Mission Bay floor hardpoints per ICD-007
- Load rating: 3,000 lb ultimate load per fitting (vertical crash load)

**AF-MAAP1F-03-9001-04-FF — Tank Access Hatches & Inspection Ports**
- Four inspection hatches (24 in diameter) for internal tank inspection
- Quick-release latch mechanisms
- Gasket seals (water-tight, chemical-resistant)

**AF-MAAP1F-03-9001-05-FF — Tank Thermal Insulation Assembly**
- 1-inch closed-cell foam insulation on exterior tank surfaces
- Reduces water temperature rise from fire proximity radiant heat
- Target: ≤10°C water temperature rise in 30-minute fire proximity exposure

---

### 3.2 TANK DISCHARGE SYSTEM (AF-MAAP1F-02-9003-FF)

**AF-MAAP1F-03-9003-01-FF — Primary Discharge Door Assembly**
- Two hydraulically-actuated clamshell doors (forward and aft sections)
- Opening area: 1,800 in² total (optimized for 2-second full discharge)
- Actuation time: 0.5 sec (door fully open)

**AF-MAAP1F-03-9003-02-FF — Secondary Discharge Door Assembly**
- Electrically-actuated secondary doors for salvo/ripple release control
- Six independent door sections (programmable sequencing)
- Actuation time: 0.3 sec per section

**AF-MAAP1F-03-9003-03-FF — Discharge Door Actuator Assemblies**
- Hydraulic actuators: Primary doors (2× actuators, 4,000 lb force each)
- Electric linear actuators: Secondary doors (6× actuators, 1,200 lb force each)
- Position feedback sensors for door position indication

**AF-MAAP1F-03-9003-04-FF — Emergency Full-Dump Override Mechanism**
- Mechanical cable-actuated release (backup to electrical/hydraulic systems)
- Pilot-accessible T-handle in cockpit (red "EMERGENCY

# DRAWING TREE / CONFIGURATION BREAKDOWN STRUCTURE
## MAAP-1F "WILDFIRE" FIREFIGHTING VARIANT
## Tandem-Rotor Heavy-Lift Autonomous Aerial Firefighting Helicopter

---

**AF-MAAP1F-03-9003-04-FF — Emergency Full-Dump Override Mechanism** *(continued)*

- Mechanical cable-actuated release (backup to electrical/hydraulic systems)
- Pilot-accessible T-handle in cockpit (red "EMERGENCY DUMP" placard)
- Direct mechanical linkage to primary door actuators (bypasses electrical controls)
- Fail-safe design: Cable tension release opens doors under gravity and residual tank pressure

**AF-MAAP1F-03-9003-05-FF — Discharge Flow Control Valves**
- Variable-orifice valves for programmable discharge rate control
- Electrically-actuated butterfly valves (6× independent sections)
- Flow rate range: 50 GPM (minimum ripple) to 1,000 GPM (full salvo)
- Position feedback potentiometers for valve angle indication

**AF-MAAP1F-03-9003-06-FF — Discharge Door Position Sensors**
- Redundant position switches (2× per door section)
- Feedback to flight control system for CG shift compensation
- Door-open/door-closed discrete signals to cockpit annunciation

---

### 3.3 FIRE DETECTION & MAPPING SENSOR SUITE COMPONENTS (AF-MAAP1F-02-9201-FF)

**AF-MAAP1F-03-9201-01-FF — FLIR Turret Gimbal Assembly**
- 3-axis stabilized gimbal: azimuth, elevation, roll
- Stabilization accuracy: ±0.5 milliradians
- Brushless DC gimbal motors with encoder feedback
- Continuous 360° rotation (azimuth), -120° to +30° elevation

**AF-MAAP1F-03-9201-02-FF — MWIR Thermal Camera Module**
- Mid-Wave Infrared sensor: 3-5 μm spectral band
- Resolution: 640×512 pixel cooled detector
- Sensitivity: <20 mK NETD (Noise Equivalent Temperature Difference)
- Frame rate: 60 Hz
- Fire hotspot detection range: 5 km (large wildfire), 2 km (small hotspots)

**AF-MAAP1F-03-9201-03-FF — LWIR Thermal Camera Module**
- Long-Wave Infrared sensor: 8-14 μm spectral band
- Resolution: 640×512 pixel uncooled microbolometer
- Sensitivity: <50 mK NETD
- Frame rate: 30 Hz
- Smoke penetration capability superior to MWIR for obscured fire edge detection

**AF-MAAP1F-03-9201-04-FF — Visible Light EO Camera (HD)**
- High-definition visible spectrum camera
- Resolution: 1920×1080 (Full HD), optional 4K upgrade
- 30× optical zoom capability
- Low-light performance: <0.01 lux (starlight mode with image intensification)
- Automatic exposure and white balance for varying light conditions

**AF-MAAP1F-03-9201-05-FF — Laser Range Finder / Designator Module**
- Eye-safe 1.54 μm laser rangefinder
- Range accuracy: ±3 m at 5 km
- Maximum range: 10 km (reflective target), 5 km (typical terrain)
- Laser designator capability (optional): NATO-compatible laser codes for coordination with other aircraft
- Pulse repetition frequency: 10 Hz

**AF-MAAP1F-03-9201-06-FF — Turret Environmental Housing**
- Sealed, nitrogen-purged housing for sensor protection
- Sapphire optical windows (IR-transmissive, scratch-resistant)
- IP67-rated environmental sealing (dust/water ingress protection)
- Heating elements for anti-ice/anti-fog operation down to -40°C

**AF-MAAP1F-03-9201-07-FF — Turret Control Electronics Unit**
- Gimbal servo drive electronics
- Video processing and compression hardware
- Ethernet interface to mission computer (GigE Vision protocol)
- Power conditioning for camera modules

---

### 3.4 FIRE PERIMETER MAPPING SENSOR ASSEMBLY (AF-MAAP1F-02-9202-FF)

**AF-MAAP1F-03-9202-01-FF — Wide-Area Thermal Scanner Head**
- Scanning LWIR thermal camera with wide field-of-view optics
- Field of view: 120° (horizontal) × 60° (vertical)
- Resolution: 320×240 pixel microbolometer (optimized for wide-area scanning)
- Scan rate: 2 Hz (full swath coverage)
- Automatic fire edge detection algorithm (threshold-based thermal gradient analysis)

**AF-MAAP1F-03-9202-02-FF — GPS/INS Geo-Referencing Module**
- Tightly-coupled GPS/INS receiver for image geo-location
- Position accuracy: <5 m CEP (95%)
- Attitude accuracy: <0.1° (pitch/roll), <0.3° (heading)
- Time-stamped image frames for fire perimeter overlay generation

**AF-MAAP1F-03-9202-03-FF — Onboard Fire Mapping Computer**
- High-performance edge processor (GPU-accelerated)
- Real-time fire perimeter vectorization and GIS overlay generation
- Automatic fire growth rate calculation (perimeter change detection over time)
- Output formats: KML/KMZ (Google Earth), Shapefile (GIS), GeoTIFF (raster overlay)
- Datalink transmission to incident command GIS systems

**AF-MAAP1F-03-9202-04-FF — Scanning Thermal Imager Mounting Bracket**
- Belly-mounted, forward-looking installation
- Vibration isolation mounts (reduces image blur from rotor vibration)
- Quick-release attachment for rapid sensor swap or maintenance

---

### 3.5 SMOKE PENETRATION LIDAR ASSEMBLY (AF-MAAP1F-02-9203-FF) — OPTIONAL

**AF-MAAP1F-03-9203-01-FF — LIDAR Transmitter/Receiver Head**
- 905 nm or 1550 nm laser diode transmitter
- Scanning mechanism: Rotating polygon mirror (360° horizontal scan)
- Vertical field-of-view: -15° to +15° (nodding mirror mechanism)
- Scan rate: 10 Hz (full panoramic scan)
- Maximum range: 500 m in heavy smoke (visibility <50 m), 2 km in clear air

**AF-MAAP1F-03-9203-02-FF — LIDAR Signal Processing Unit**
- Time-of-flight measurement electronics
- Point cloud generation and obstacle detection algorithms
- Automatic terrain classification (ground, vegetation, structures, power lines)
- Obstacle alert generation (height AGL and lateral distance to obstacles)

**AF-MAAP1F-03-9203-03-FF — LIDAR-Derived Terrain Database Generator**
- Real-time 3D terrain mesh generation from LIDAR point clouds
- Integration with pre-loaded terrain databases for landing zone identification
- Automatic safe landing zone detection algorithm:
  - Slope <10°
  - Obstacle clearance radius ≥50 ft
  - Surface roughness assessment (detect rocks, stumps, debris)

**AF-MAAP1F-03-9203-04-FF — LIDAR/Camera Data Fusion Module**
- Fuses LIDAR point cloud with EO/IR camera imagery
- Generates augmented reality display overlays for pilot/GCS operator
- Obstacle warnings superimposed on video feed with range/bearing annotations

---

### 3.6 ENVIRONMENTAL SENSOR PACKAGE (AF-MAAP1F-02-9204-FF)

**AF-MAAP1F-03-9204-01-FF — Roof-Mounted Anemometer Assembly**
- Ultrasonic anemometer (no moving parts, high reliability)
- Wind speed range: 0-100 kt, accuracy ±2 kt
- Wind direction: 0-360°, accuracy ±5°
- Mounting location: Aft fuselage roof, above rotor downwash zone
- Heated sensor head for anti-ice operation

**AF-MAAP1F-03-9204-02-FF — Temperature and Humidity Sensor Module**
- Ambient air temperature sensor: -50°C to +70°C, accuracy ±0.5°C
- Relative humidity sensor: 0-100% RH, accuracy ±3%
- Aspirated sensor housing (forced airflow for accurate measurement)
- Fire proximity heat load compensation algorithm (filters out radiant heat spikes)

**AF-MAAP1F-03-9204-03-FF — Barometric Pressure Sensor**
- Pressure altitude measurement: -1,000 ft to +20,000 ft PA
- Accuracy: ±10 ft altitude equivalent
- Integration with fire behavior prediction models (atmospheric stability assessment)

**AF-MAAP1F-03-9204-04-FF — Pyranometer (Solar Radiation Sensor) — Optional**
- Measures incoming solar radiation (W/m²)
- Used for fire behavior modeling (solar heating contribution to fire intensity)
- Spectral range: 300-3,000 nm (broadband)

**AF-MAAP1F-03-9204-05-FF — Environmental Data Logger and Transmitter**
- Records environmental data at 1 Hz sample rate
- Transmits data via datalink to GCS and incident command weather stations
- Integration with National Fire Danger Rating System (NFDRS) data feeds

---

### 3.7 DATALINK RELAY SYSTEM (AF-MAAP1F-02-9205-FF)

**AF-MAAP1F-03-9205-01-FF — UHF/VHF Voice Relay Transceiver**
- UHF band: 225-400 MHz (military/fire aviation frequencies)
- VHF band: 118-174 MHz (civil aviation and fire ground frequencies)
- Transmit power: 25 W (UHF), 10 W (VHF)
- Relay mode: Automatic cross-band repeat (UHF ↔ VHF)
- Enables firefighter ground teams to communicate via aircraft relay to incident command

**AF-MAAP1F-03-9205-02-FF — Data Relay Router / Gateway**
- IP-based data router for ground team sensor data relay
- Accepts inputs: GPS position reports, infrared cameras (handheld), weather stations
- Protocols supported: TCP/IP, UDP multicast, MQTT (IoT messaging)
- Bandwidth: 2 Mbps aggregate throughput
- Enables real-time ground team position tracking on incident command Common Operating Picture (COP)

**AF-MAAP1F-03-9205-03-FF — High-Gain Antenna Array (Ground Team Link)**
- Electronically-steerable phased array antenna (bottom fuselage installation)
- Coverage pattern: ±60° from nadir (covers ground teams below aircraft)
- Frequency: 2.4 GHz or 5.8 GHz ISM band (license-free operation)
- Automatic beam steering to maintain link with moving ground teams

**AF-MAAP1F-03-9205-04-FF — Incident Command Network Integration Module**
- Interface to National Interagency Fire Center (NIFC) communication networks
- Supports CAD (Computer-Aided Dispatch) data feeds
- Integration with ICS-214 (Incident Command System activity logs)
- Encrypted data transmission per FIPS 140-2 (sensitive incident data protection)

---

### 3.8 FIREFIGHTING MISSION COMPUTER COMPONENTS (AF-MAAP1F-02-9301-FF)

**AF-MAAP1F-03-9301-01-FF — Mission Processor Module**
- High-performance CPU: Quad-core 2.5 GHz (ruggedized commercial-off-the-shelf)
- GPU co-processor: CUDA-capable for fire modeling and image processing
- Memory: 32 GB DDR4 RAM, 1 TB NVMe SSD storage
- Operating system: Real-time Linux or VxWorks (DO-178C certifiable variant)
- Conduction-cooled chassis (no internal fans, sealed enclosure)

**AF-MAAP1F-03-9301-02-FF — Drop Pattern Calculation Algorithm Module**
- Software application: Ballistic trajectory model for water/retardant drop
- Inputs: Aircraft altitude, airspeed, wind vector, release point GPS coordinates
- Outputs: Predicted drop footprint (ellipse), coverage density, drift compensation
- GPS-guided corridor mode: Automatic salvo sequencing along pre-planned flight path
- Real-time updates based on actual wind measurements during drop run

**AF-MAAP1F-03-9301-03-FF — Fire Behavior Modeling Software**
- Integration with FARSITE or FlamMap fire spread prediction models (USFS standard tools)
- Inputs: Fire perimeter (from mapping sensors), terrain data, fuel type, weather
- Outputs: Predicted fire growth vectors, priority suppression zones
- Recommends optimal drop locations for maximum fire containment effectiveness

**AF-MAAP1F-03-9301-04-FF — Mission Database Storage Module**
- Pre-loaded terrain databases (10 m DEM resolution for operating area)
- Fire retardant base locations and refill point database
- Emergency landing zone database (helispots, airports)
- NOTAMs and temporary flight restrictions (TFR) for wildfire airspace

**AF-MAAP1F-03-9301-05-FF — Mission Computer Redundancy and Health Monitoring**
- Dual-redundant mission computer architecture (primary and backup)
- Automatic failover on primary computer fault (<2 second switchover)
- Built-in test (BIT) runs continuously, reports faults to cockpit/GCS
- Watchdog timer resets processor on software hang condition

---

### 3.9 DROP CONTROL SYSTEM COMPONENTS (AF-MAAP1F-02-9302-FF)

**AF-MAAP1F-03-9302-01-FF — Drop Controller Processor**
- Dedicated drop sequencing processor (independent of mission computer for safety)
- Dual-redundant microcontroller architecture
- Software developed to DO-178C DAL B (mission-critical but not flight-critical)
- Receives drop authorization from mission computer or pilot manual override

**AF-MAAP1F-03-9302-02-FF — GPS Waypoint Trigger Module**
- Monitors aircraft GPS position against programmed drop waypoints
- Automatic release trigger when aircraft crosses waypoint boundary (±10 m CEP)
- Configurable lead/lag offset for wind drift compensation
- Salvo mode: Sequential door openings at fixed time intervals (programmable 0.1-2.0 sec spacing)

**AF-MAAP1F-03-9302-03-FF — Manual Drop Control Panel (Cockpit Installation)**
- Pilot-accessible drop control panel in cockpit overhead console
- Controls:
  - Master ARM/SAFE switch (prevents inadvertent release)
  - Drop mode selector: SALVO / RIPPLE / MANUAL
  - Salvo door count selector (1-6 doors)
  - Manual release button (guarded, requires ARM + button press)
- Status indicators: Tank level, door position, system ready/fault

**AF-MAAP1F-03-9302-04-FF — GCS Remote Drop Authorization Interface**
- Datalink interface for GCS operator to authorize drop remotely
- Two-person authorization protocol (GCS operator + Mission Commander)
- Drop authorization codes transmitted encrypted via C2 datalink
- Prevents unauthorized or accidental drops in autonomous mode

**AF-MAAP1F-03-9302-05-FF — Drop Recorder / Data Logger**
- Records all drop events with high-precision timestamps
- Logs: GPS position, altitude, airspeed, wind vector, tank quantity before/after, door sequence
- Data exported for post-mission drop effectiveness analysis
- Supports regulatory reporting requirements (e.g., EPA retardant application records)

---

### 3.10 FIRE LINE OVERLAY DISPLAY SYSTEM (AF-MAAP1F-02-9303-FF)

**AF-MAAP1F-03-9303-01-FF — Moving Map Display Software Module**
- Base layer: Aeronautical chart or satellite imagery
- Overlay layers: Fire perimeter (real-time from mapping sensors), drop zones, TFRs, ground team positions
- Touch-screen pan/zoom interface
- Automatic map orientation: North-up or Track-up (pilot-selectable)

**AF-MAAP1F-03-9303-02-FF — Fire Perimeter Overlay Generator**
- Receives fire perimeter vectors from fire mapping computer
- Color-coded fire intensity zones: Low (green), Moderate (yellow), High (red)
- Time-stamped perimeter updates (shows fire growth over time)
- Displays predicted fire spread vectors (future perimeter at T+1 hr, T+6 hr)

**AF-MAAP1F-03-9303-03-FF — Drop Pattern Visualization Module**
- Superimposes predicted drop footprint on moving map display
- Real-time footprint updates based on current aircraft state (altitude, speed, wind)
- Drop coverage density heatmap (gallons per square foot)
- Post-drop actual coverage overlay (based on GPS-logged release points and wind data)

**AF-MAAP1F-03-9303-04-FF — Display Hardware Interface**
- Ethernet interface to cockpit multi-function displays (MFDs)
- ARINC 661 display protocol (standard avionics display format)
- Video output: 1920×1080 resolution, 60 Hz refresh rate
- Redundant display interfaces (primary and backup MFD channels)

---

## LEVEL 4: DETAIL COMPONENTS AND LINE REPLACEABLE UNITS (LRUs)

### 4.1 TANK STRUCTURE DETAIL COMPONENTS (AF-MAAP1F-03-9001-XX-FF)

**AF-MAAP1F-04-9001-01-FF — Tank Shell Composite Layup**
- Inner layer: Kevlar fabric (impact resistance, leak containment)
- Mid layer: Carbon fiber unidirectional tape (primary structural load-carrying)
- Outer layer: Fiberglass cloth (environmental protection, lightning strike dissipation)
- Resin system: Epoxy, fire-retardant formulation per FAR 25.853(a) (meets or exceeds burn rate limits)

**AF-MAAP1F-04-9001-02-FF — Tank Inspection Hatch Cover**
- 24-inch diameter circular hatch
- Material: Composite (same layup as tank shell)
- Seal: Silicone gasket, water-tight and chemical-resistant
- Latch mechanism: Over-center cam locks (8 places around perimeter)
- Tool-free opening (hand-operated latches)

**AF-MAAP1F-04-9001-03-FF — Anti-Slosh Baffle Panel**
- Material: Composite honeycomb sandwich panel
- Thickness: 0.5 inch
- Perforation: 40% open area (drain holes, 1-inch diameter, staggered pattern)
- Attachment: Bonded to tank shell with structural adhesive (secondary mechanical fasteners as backup)

**AF-MAAP1F-04-9001-04-FF — Tank Hardpoint Attach Fitting (Detail)**
- Material: Titanium 6Al-4V alloy
- Forging with machined attachment lugs
- Ultimate load rating: 3,000 lb per fitting (vertical crash load)
- Interface: Bonded into composite tank shell with titanium doubler plates
- Fasteners: NAS6604 bolts (1/2-inch diameter, close-tolerance) to Mission Bay hardpoints

**AF-MAAP1F-04-9001-05-FF — Tank Level Sensor Probe**
- Type: Capacitive fuel quantity probe (adapted for water/retardant)
- Measurement range: 0-2,000 gallons
- Accuracy: ±1% full scale (±20 gallons)
- Number of probes: 4 (redundant measurement, averaged for display)
- Output signal: ARINC 429 digital interface to avionics

---

### 4.2 TANK FILL SYSTEM DETAIL COMPONENTS (AF-MAAP1F-03-9002-XX-FF)

**AF-MAAP1F-04-9002-01-FF — Gravity Fill Port Assembly**
- Port diameter: 4 inches
- Location: Top of tank, aft section (accessible from ground via ladder)
- Fill cap: Quick-release quarter-turn cap with D-ring handle
- Overflow vent: Prevents tank overpressure during ground fill operations
- Fill rate: 60 GPM (limited by port diameter and tank vent capacity)

**AF-MAAP1F-04-9002-02-FF — Pressure Refill Port Assembly**
- Port diameter: 2.5 inches (high-velocity fill nozzle interface)
- Coupling: Dry-break quick-disconnect (Stucchi or Parker compatible)
- Check valve: Prevents backflow when fill hose disconnected
- Fill rate: 150 GPM at 50 psi supply pressure (rapid refill for high sortie rate operations)
- Location: Side of fuselage, external access panel

**AF-MAAP1F-04-9002-03-FF — Fill Valve Actuator**
- Type: Electrically-actuated ball valve
- Actuation: 24 VDC motor, 5-second open/close time
- Position feedback: Limit switches (open/closed discrete signals)
- Manual override: Hand-wheel on valve stem (emergency manual operation)

**AF-MAAP1F-04-9002-04-FF — Automatic Shutoff Float Valve**
- Mechanical float-actuated valve (no electrical power required)
- Closes fill valve when tank reaches 2,000-gallon capacity
- Backup to electronic tank level indication (prevents overflow)
- Material: Stainless steel and fluorocarbon seals (chemical compatibility)

**AF-MAAP1F-04-9002-05-FF — Snorkel Fill Interface Coupling (Optional Kit Integration Point)**
- Standardized coupling for snorkel fill probe connection
- Location: Bottom of tank, forward section
- Coupling type: Camlock quick-connect
- Strainer screen: 50-mesh stainless steel (prevents debris ingestion during water scooping)

---

### 4.3 TANK DISCHARGE SYSTEM DETAIL COMPONENTS (AF-MAAP1F-03-9003-XX-FF)

**AF-MAAP1F-04-9003-01-FF — Primary Discharge Door Hinge Assembly**
- Type: Piano hinge (continuous hinge along door edge)
- Material: Stainless steel
- Length: 60 inches per door section
- Designed for 10,000+ open/close cycles (equivalent to 2,000 flight hours at 5 drops per sortie)

**AF-MAAP1F-04-9003-02-FF — Primary Door Hydraulic Actuator**
- Type: Double-acting hydraulic cylinder
- Stroke: 12 inches
- Bore: 2.5 inches
- Force: 4,000 lb at 3,000 psi hydraulic pressure
- Speed: 0.5 second full stroke (door fully open)
- End cushions: Hydraulic damping to prevent impact loads

**AF-MAAP1F-04-9003-03-FF — Secondary Door Electric Linear Actuator**
- Type: Electromechanical ball screw actuator
- Stroke: 8 inches
- Force: 1,200 lb at stall
- Speed: 2 inches/second (0.3 second per door section opening)
- Power: 28 VDC aircraft power bus
- Position feedback: Integrated potentiometer (analog position signal)

**AF-MAAP1F-04-9003-04-FF — Discharge Door Seal**
- Material: Silicone rubber extrusion
- Profile: P-shaped bulb seal
- Compression: 25% at door closed position (maintains water-tight seal)
- Temperature range: -54°C to +120°C
- Replacement interval: 600 flight hours or 2 years (whichever first)

**AF-MAAP1F-04-9003-05-FF — Emergency Cable Release Handle (Cockpit)**
- Location: Cockpit overhead panel, red T-handle with "EMERGENCY DUMP" placard
- Cable: 1/8-inch diameter stainless steel cable, Teflon-lined conduit
- Pull force: 15 lb (within pilot strength capability)
- Function: Releases mechanical door locks, allows doors to open under gravity + tank pressure

---

### 4.4 CARGO HOOK ASSEMBLY DETAIL COMPONENTS (AF-MAAP1F-02-9101-FF / -9102-FF)

**AF-MAAP1F-04-9101-01-FF — Cargo Hook Body**
- Type: Electrically-actuated cargo hook
- Load rating: 12,000 lb (Threshold) / 16,000 lb (Objective)
- Material: High-strength steel forging (AISI 4340 alloy)
- Finish: Cadmium plating (corrosion protection)
- Hook jaw opening: 1.5 inches (accommodates standard D-ring shackles)

**AF-MAAP1F-04-9101-02-FF — Hook Actuation Motor**
- Type: 28 VDC brushless motor with integral gearbox
- Actuation time: <0.5 second (hook open to release load)
- Holding torque: 50 lb-ft (prevents inadvertent release under vibration)
- Manual release backup: Mechanical cable-pull override

**AF-MAAP1F-04-9101-03-FF — Load Cell (Weight Measurement)**
- Type: Strain gauge load cell
- Capacity: 20,000 lb (125% of objective hook rating)
- Accuracy: ±50 lb (±0.25% full scale)
- Output: Analog 0-5 VDC signal (ratiometric to excitation voltage)
- Integration: Signal conditioned and digitized for display on MFDs and GCS

**AF-MAAP1F-04-9101-04-FF — Hook Swivel Bearing**
- Allows 360° rotation of external load (prevents cable twist buildup)
- Bearing type: Spherical roller bearing (high radial and thrust load capacity)
- Lubrication: Sealed, grease-lubricated (maintenance-free for 1,000 flight hours)

**AF-MAAP1F-04-9101-05-FF — Emergency Release Solenoid**
- Electrically-actuated backup release mechanism
- Activation: Cockpit emergency release button or GCS remote command
- Power: 28 VDC, 5 amp momentary pulse
- Redundancy: Dual solenoid coils (either can release hook)

---

### 4.5 FLIR TURRET DETAIL COMPONENTS (AF-MAAP1F-03-9201-XX-FF)

**AF-MAAP1F-04-9201-01-FF — Azimuth Gimbal Motor and Encoder**
- Motor type: Brushless DC motor, frameless design
- Torque: 5 Nm continuous
- Encoder: Absolute rotary encoder, 16-bit resolution (0.0055° per count)
- Slip ring assembly: Transfers power and data signals across rotating interface (unlimited rotation)

**AF-MAAP1F-04-9201-02-FF — Elevation Gimbal Motor and Encoder**
- Identical motor specification to azimuth axis
- Range of motion: -120° to +30° (limited by mechanical hard stops)
- Hard stop protection: Torque limiting in motor controller prevents damage from stall condition

**AF-MAAP1F-04-9201-03-FF — Roll Stabilization Motor (Image Stabilization)**
- Motor type: Direct-drive torque motor
- Torque: 2 Nm continuous
- Function: Compensates for aircraft roll and vibration (maintains stable image)
- Bandwidth: 50 Hz (sufficient to reject rotor-induced vibration)

**AF-MAAP1F-04-9201-04-FF — MWIR Camera Dewar / Cryocooler Assembly**
- Cryocooler type: Stirling cycle, integral to camera module
- Operating temperature: 77 K (-196°C, liquid nitrogen equivalent temperature)
- Cool-down time: <5 minutes from power-on to operational temperature
- Mean time between failure (cryocooler): >8,000 hours

**AF-MAAP1F-04-9201-05-FF — Sapphire Optical Window**
- Material: Single-crystal sapphire (Al₂O₃)
- Diameter: 6 inches
- Thickness: 0.25 inches
- Coating: Multi-layer anti-reflection coating (3-5 μm and 8-14 μm dual-band)
- Hardness: 9 Mohs (second only to diamond, extreme scratch resistance)

**AF-MAAP1F-04-9201-06-FF — Turret Nitrogen Purge System**
- Function: Maintains positive internal pressure with dry nitrogen (prevents moisture and dust ingress)
- Pressure: 2 psi above ambient
- Nitrogen reservoir: 1-liter capacity (sufficient for 100 flight hours)
- Leak rate specification: <0.1 psi per 24 hours

---

### 4.6 ENVIRONMENTAL SENSOR DETAIL COMPONENTS (AF-MAAP1F-03-9204-XX-FF)

**AF-MAAP1F-04-9204-01-FF — Ultrasonic Anemometer Transducer Array**
- Configuration: 4 ultrasonic transducers arranged in cross pattern
- Measurement principle: Time-of-flight difference for sound waves in wind
- Heating element: 50 W resistive heater (prevents ice accumulation on transducers)
- Power consumption: 5 W (normal), 55 W (with anti-ice active)

**AF-MAAP1F-04-9204-02-FF — Temperature Sensor Probe**
- Type: Platinum RTD (Resistance Temperature Detector), PT1000 element
- Accuracy: ±0.5°C over -50°C to +70°C range
- Response time: <5 seconds (90% of step change)
- Radiation shield: Aspirated housing with forced airflow (eliminates solar heating error)

**AF-MAAP1F-04-9204-03-FF — Humidity Sensor Element**
- Type: Capacitive polymer humidity sensor
- Accuracy: ±3% RH over 0-100% range
- Response time: <15 seconds (63% of step change)
- Long-term drift: <1% RH per year

**AF-MAAP1F-04-9204-04-FF — Barometric Pressure Transducer**
- Type: Piezoresistive silicon pressure sensor
- Range: 500-1,100 hPa (equivalent to -1,000 ft to +20,000 ft altitude)
- Accuracy: ±1 hPa (±10 ft altitude equivalent)
- Temperature compensation: Internal temperature sensor corrects for sensor thermal drift

---

## LEVEL 5: SUBCOMPONENT DETAILS (CRITICAL FIREFIGHTING SYSTEMS)

### 5.1 TANK COMPOSITE SHELL DETAILED CONSTRUCTION (AF-MAAP1F-04-9001-01-FF)

**AF-MAAP1F-05-9001-01-01-FF — Inner Kevlar Liner Ply Schedule**
- Ply 1-4: Kevlar 49 fabric, 8 harness satin weave, 0°/90° orientation
- Ply thickness: 0.010 inch per ply
- Total liner thickness: 0.040 inch (4 plies)
- Function: Ballistic fragment containment (survivability), leak resistance

**AF-MAAP1F-05-9001-01-02-FF — Mid Carbon Fiber Structural Plies**
- Ply 5-12: Carbon fiber unidirectional tape, alternating 0°/±45°/90° orientations
- Ply thickness: 0.0075 inch per ply
- Total structural thickness: 0.060 inch (8 plies)
- Fiber: Toray T700 or equivalent (high strength, intermediate modulus)

**AF-MAAP1F-05-9001-01-03-FF — Outer Fiberglass Protection Layer**
- Ply 13-16: E-glass fabric, plain weave, 0°/90° orientation
- Ply thickness: 0.012 inch per ply
- Total protection layer thickness: 0.048 inch (4 plies)
- Function: Environmental protection (UV, moisture), electrical isolation (lightning strike)

**AF-MAAP1F-05-9001-01-04-FF — Epoxy Resin Matrix**
- Resin system: Epoxy, fire-retardant formulation (brominated or phosphorus-based additive)
- Resin type: 350°F cure, toughened epoxy (e.g., Hexcel 8552 or equivalent)
- Fiber volume fraction: 55-60%
- Burn rate compliance: ≤2.5 inches/minute per FAR 25.853(a) vertical burn test

---

### 5.2 DISCHARGE DOOR HYDRAULIC ACTUATOR INTERNAL COMPONENTS (AF-MAAP1F-04-9003-02-FF)

**AF-MAAP1F-05-9003-02-01-FF — Actuator Cylinder Barrel**
- Material: Hard-anodized aluminum alloy (7075-T6)
- Bore diameter: 2.5 inches
- Honing finish: 8 microinch Ra (mirror finish for seal life)
- Pressure rating: 5,000 psi (safety factor 1.67× over 3,000 psi operating pressure)

**AF-MAAP1F-05-9003-02-02-FF — Piston and Piston Rod Assembly**
- Piston material: Aluminum alloy with bronze wear bands
- Rod material: Hard-chrome-plated steel (AISI 4140)
- Rod diameter: 1.5 inches
- Surface finish: <4 microinch Ra (minimizes seal wear)

**AF-MAAP1F-05-9003-02-03-FF — Hydraulic Seals and O-Rings**
- Piston seal: Polyurethane U-cup seal (pressure-energized)
- Rod seal: Nitrile rubber (NBR) U-cup with PTFE backup ring
- Wiper seal: Polyurethane scraper ring (prevents contamination ingress)
- O-rings: AS568 standard sizes, nitrile rubber (NBR), -40°F to +250°F temperature range

**AF-MAAP1F-05-9003-02-04-FF — End Cushions (Hydraulic Damping)**
- Function: Decelerate piston before hard stop impact (extends actuator life)
- Mechanism: Orifice restriction in hydraulic flow path near end of stroke
- Cushion adjustment: Factory-set orifice size (not field-adjustable)

---

### 5.3 FLIR MWIR CAMERA INTERNAL COMPONENTS (AF-MAAP1F-04-9201-04-FF)

**AF-MAAP1F-05-9201-04-01-FF — HgCdTe Focal Plane Array (FPA)**
- Detector material: Mercury Cadmium Telluride (HgCdTe)
- Array format: 640×512 pixels
- Pixel pitch: 15 μm
- Spectral response: 3.4-4.8 μm (optimized for fire detection)
- Operating temperature: 77 K (cryogenic cooling required)

**AF-MAAP1F-05-9201-04-02-FF — Readout Integrated Circuit (ROIC)**
- Function: Converts detector photocurrent to digital signal
- Integration time: Variable (1 μs to 10 ms, automatic exposure control)
- Analog-to-digital converter: 14-bit resolution
- Frame rate: 60 Hz

**AF-MAAP1F-05-9201-04-03-FF — Cryocooler Compressor and Expander**
- Compressor: Reciprocating linear motor
- Expander: Displacer piston with regenerator
- Refrigeration capacity: 1.5 W at 77 K
- Power consumption: 15 W electrical input
- Vibration export: <0.1 g at camera mounting interface (low vibration design)

**AF-MAAP1F-05-9201-04-04-FF — IR Optics (Germanium Lens Assembly)**
- Lens material: Germanium (Ge), single-crystal
- Lens configuration: 4-element design (focal length: 100 mm, f/2.0)
- Anti-reflection coating: Multi-layer dielectric coating (>95% transmission at 3-5 μm)
- Athermalization: Passive (lens spacers designed to maintain focus over -40°C to +60°C ambient)

---

### 5.4 LOAD CELL INTERNAL CONSTRUCTION (AF-MAAP1F-04-9101-03-FF)

**AF-MAAP1F-05-9101-03-01-FF — Strain Gauge Bridge Assembly**
- Configuration: Wheatstone bridge with 4 active strain gauges
- Strain gauge type: Foil strain gauge, 350 ohm resistance
- Bonding: Epoxy-bonded to flexure element
- Temperature compensation: Self-temperature-compensated (STC) gauges matched to flexure material

**AF-MAAP1F-05-9101-03-02-FF — Flexure Element (Load-Sensing Member)**
- Material: 17-4 PH stainless steel, precipitation-hardened
- Geometry: Double-ended shear beam design
- Elastic deflection: 0.020 inch at rated load (20,000 lb)
- Fatigue life: >1 million load cycles at rated load

**AF-MAAP1F-05-9101-03-03-FF — Environmental Sealing**
- Enclosure: Welded stainless steel housing
- Sealing: Hermetically sealed (helium leak rate <1×10⁻⁸ cc/sec)
- Cable gland: IP68-rated cable entry (submersion-proof)
- Desiccant: Silica gel pack inside housing (absorbs residual moisture)

**AF-MAAP1F-05-9101-03-04-FF — Signal Conditioning Electronics (Integral)**
- Amplifier: Instrumentation amplifier with gain of 1,000
- Excitation voltage: 10 VDC regulated (internal precision voltage reference)
- Output signal: 0-5 VDC analog (ratiometric to load)
- Calibration: Factory-calibrated with NIST-traceable dead weights

---

## BILL OF MATERIALS (BOM) SUMMARY — FIREFIGHTING VARIANT-UNIQUE ASSEMBLIES

| Assembly Drawing Number | Assembly Title | Quantity per Aircraft | Lead Item? | Critical Item? |
|---|---|---|---|---|
| AF-MAAP1F-01-9000-FF | Internal Water/Retardant Tank System Assembly | 1 | Yes | Yes |
| AF-MAAP1F-01-9100-FF | External Firefighting Load Provisions Assembly | 1 | Yes | No |
| AF-MAAP1F-01-9200-FF | Fire Detection & Mapping Sensor Suite Assembly | 1 | Yes | Yes |
| AF-MAAP1F-01-9300-FF | Firefighting Mission Avionics Assembly | 1 | No | Yes |
| AF-MAAP1F-01-9400-FF | Pilot Crew Station Assembly | 1 | No | No |
| AF-MAAP1F-01-9500-FF | Water Scooping System Assembly (Optional Kit) | 0-1 | Yes | No |
| AF-MAAP1F-01-9600-FF | Retardant Injection & Foam System Assembly (Optional Kit) | 0-1 | No | No |

**Notes:**
- **Lead Item:** Long-lead procurement item requiring early commitment to meet production schedule
- **Critical Item:** Single-source supplier, high technical risk, or long qualification timeline

---

## CONFIGURATION NOTES AND INTERCHANGEABILITY

### CN-1: Tank System Interchangeability
The internal water/retardant tank assembly (AF-MAAP1F-01-9000-FF) is **not interchangeable** between aircraft without re-rigging and weight-and-balance verification due to individual aircraft CG variations. Each tank is serialized and assigned to a specific aircraft tail number.

### CN-2: Sensor Suite Growth Path
The Fire Detection & Mapping Sensor Suite (AF-MAAP1F-01-9200-FF) is designed with open sensor bay provisions for future upgrades. Interface control document ICD-007 governs sensor mounting, power, and data interfaces. Future sensor additions (e.g., hyperspectral imagers, upgraded LIDAR) shall conform to ICD-007 without requiring modification to baseline sensor mounting structure.

### CN-3: Crew Station Removal Configuration
Per PRB Section 3.5, the Pilot Crew Station Assembly (AF-MAAP1F-01-9400-FF) is designed for removal in <8 labor-hours. Removal procedure documented in Maintenance Manual Section 25-XX-XX. Upon crew station removal:
- Crew station weight: 850 lb (pilot seats, controls, displays, environmental ducting)
- Useful load increase: +850 lb (available for additional fuel or retardant capacity)
- CG shift: +0.8% MAC forward (within allowable CG envelope at reduced gross weight)

### CN-4: Optional Kit Installation Sequence
Water Scooping System (AF-MAAP1F-01-9500-FF) and Retardant Injection System (AF-MAAP1F-01-9600-FF) are mutually compatible and may be installed simultaneously. Installation of both kits:
- Weight addition: +420 lb (scooping system) + +280 lb (retardant system) = +700 lb total
- Useful load reduction: -700 lb
- Power consumption increase: +5 kW (scooping pump) + +2 kW (retardant pump) = +7 kW total
- Requires electrical load analysis to verify no exceedance of generator capacity

---

## MAINTENANCE PLANNING AND SCHEDULED INSPECTIONS (FIREFIGHTING-SPECIFIC ITEMS)

| Item | Inspection/Maintenance Action | Interval | Labor-Hours |
|---|---|---|---|
| Internal Tank (AF-MAAP1F-02-9001-FF) | Visual inspection for cracks, delamination, corrosion | 150 flight hours (Phase 2) | 2.0 |
| Tank Discharge Doors (AF-MAAP1F-02-9003-FF) | Operational check, seal inspection, hinge lubrication | 50 flight hours (Phase 1) | 1.5 |
| Tank Discharge Doors | Reseal door seals (replace gaskets) | 600 flight hours | 4.0 |
| Cargo Hooks (AF-MAAP1F-02-9101-FF / -9102-FF) | Load test (125% rated load), non-destructive inspection (NDI) | 300 flight hours (Phase 3) | 3.0 per hook |
| FLIR Turret (AF-MAAP1F-02-9201-FF) | Clean optical windows, check gimbal alignment, BIT test | 50 flight hours (Phase 1) | 1.0 |
| FLIR Cryocooler | Cryocooler performance test (cool-down time, temperature stability) | 300 flight hours (Phase 3) | 2.0 |
| Environmental Sensors (AF-MAAP1F-02-9204-FF) | Calibration verification (cross-check against reference instruments) | 600 flight hours | 1.5 |
| Water Scooping Pump (AF-MAAP1F-02-9502-FF) | Impeller inspection, seal replacement, performance test | 300 flight hours (if installed) | 6.0 |
| Retardant Injection Pump (AF-MAAP1F-02-9602-FF) | Chemical flush, seal replacement, flow calibration | 150 flight hours (if installed) | 4.0 |

**Total Additional Scheduled Maintenance (Firefighting Variant):** Approximately **+1.2 MMH/FH** above baseline Green Aircraft maintenance burden, assuming full-capability configuration with all optional kits installed.

---

## DESIGN FEATURES FOR SUSTAINMENT AND LOGISTICS

### DF-1: Modular Tank Construction
The internal tank system is designed in three major modules:
- **Tank shell assembly** (AF-MAAP1F-02-9001-FF): Removable as a single unit for depot-level repair or replacement
- **Fill system module** (AF-MAAP1F-02-9002-FF): LRU-level replacement, no tank removal required
- **Discharge system module** (AF-MAAP1F-02-9003-FF): Door assemblies replaceable individually

Depot-level tank replacement time: <16 labor-hours (tank drop and reinstall)

### DF-2: Sensor Suite Open Architecture
All firefighting sensors interface via standardized MIL-STD-1553 or Ethernet connections per ICD-007. Sensor LRUs are **plug-and-play** with automatic Built-In Test (BIT) initialization upon power-up. No special alignment or calibration procedures required for field-level LRU replacement (calibration data stored in sensor EEPROM).

### DF-3: Retardant System Corrosion Protection
All wetted surfaces in retardant flow path constructed from:
- Stainless steel (300-series) or titanium (pumps, valves, fittings)
- PTFE-lined hoses and gaskets
- Anodized aluminum (non-wetted structure)

Post-mission flushing procedure (10-minute automated cycle) prevents chemical buildup and corrosion. Flushing system validation per MIL-STD-3023 (corrosion prevention for chemical handling systems).

---

## APPLICABLE STANDARDS AND SPECIFICATIONS

| Standard/Spec | Title | Applicable Assemblies |
|---|---|---|
| MIL-STD-1290 | Light Fixed- and Rotary-Wing Aircraft Crashworthiness | Tank structure (crash loads) |
| FAR 25.853(a) | Flammability of Interior Materials (vertical burn test) | Tank composite shell, crew station materials |
| MIL-STD-810H | Environmental Engineering Considerations and Laboratory Tests | Sensors, avionics, hydraulic components |
| MIL-STD-464D | Electromagnetic Environmental Effects | FLIR turret, avionics |
| RTCA DO-160G | Environmental Conditions and Test Procedures for Airborne Equipment | Mission computers, displays |
| MIL-PRF-83282 | Hydraulic Fluid, Fire Resistant | Tank discharge system hydraulics |
| ASTM F3442 | Detect and Avoid System Performance | Fire detection sensor suite integration with DAA |
| NFPA 1145 | Code for the Organization and Operation of Aircraft Rescue and Fire-Fighting Services | Firefighting operational procedures (reference) |

---

## DRAWING TREE INDEX (ALPHABETICAL BY ASSEMBLY TITLE)

| Assembly Title | Drawing Number |
|---|---|
| Belly Camera System (External Load View) | AF-MAAP1F-02-9104-FF |
| Cargo Hook Assembly, Aft | AF-MAAP1F-02-9102-FF |
| Cargo Hook Assembly, Forward | AF-MAAP1F-02-9101-FF |
| Chemical Mixing Manifold & Distribution Assembly | AF-MAAP1F-02-9604-FF |
| Cockpit Display Suite Assembly | AF-MAAP1F-02-9403-FF |
| Cockpit Environmental Control Module | AF-MAAP1F-02-9405-FF |
| Datalink Relay System for Ground Firefighting Teams | AF-MAAP1F-02-9205-FF |
| Display Hardware Interface | AF-MAAP1F-03-9303-04-FF |
| Drop Control System Assembly | AF-MAAP1F-02-9302-FF |
| Drop Controller Processor | AF-MAAP1F-03-9302-01-FF |
| Drop Pattern Visualization Module | AF-MAAP1F-03-9303-03-FF |
| Drop Recorder / Data Logger | AF-MAAP1F-03-9302-05-FF |
| Emergency Egress & Crew Protection Systems Assembly | AF-MAAP1F-02-9406-FF |
| Emergency Full-Dump Override Mechanism | AF-MAAP1F-04-9003-04-FF |
| Environmental Sensor Package Assembly | AF-MAAP1F-02-9204-FF |
| External Load Monitoring System Assembly | AF-MAAP1F-02-9103-FF |
| Fire Behavior Modeling Software | AF-MAAP1F-03-9301-03-FF |
| Fire Detection & Mapping Sensor Suite Assembly | AF-MAAP1F-01-9200-FF |
| Fire Line Overlay Display System Assembly | AF-MAAP1F-02-9303-FF |
| Fire Perimeter Mapping Sensor Assembly | AF-MAAP1F-02-9202-FF |
| Fire Perimeter Overlay Generator | AF-MAAP1F-03-9303-02-FF |
| Firefighting Mission Avionics Assembly | AF-MAAP1F-01-9300-FF |
| Firefighting Mission Computer Assembly | AF-MAAP1F-02-9301-FF |
| FLIR Turret Gimbal Assembly | AF-MAAP1F-03-9201-01-FF |
| Foam Concentrate Tank & System Assembly | AF-MAAP1F-02-9603-FF |
| Forward-Looking Infrared (FLIR) Turret Assembly | AF-MAAP1F-02-9201-FF |
| GCS Firefighting Interface Software Package | AF-MAAP1F-02-9305-FF |
| GCS Remote Drop Authorization Interface | AF-MAAP1F-03-9302-04-FF |
| GPS Waypoint Trigger Module | AF-MAAP1F-03-9302-02-FF |
| High-Volume Water Pump Assembly | AF-MAAP1F-02-9502-FF |
| Internal Water/Retardant Tank System Assembly | AF-MAAP1F-01-9000-FF |
| Laser Range Finder / Designator Module | AF-MAAP1F-03-9201-05-FF |
| LIDAR Signal Processing Unit | AF-MAAP1F-03-9203-02-FF |
| LIDAR Transmitter/Receiver Head | AF-MAAP1F-03-9203-01-FF |
| LWIR Thermal Camera Module | AF-MAAP1F-03-9201-03-FF |
| Manual Drop Control Panel (Cockpit Installation) | AF-MAAP1F-03-9302-03-FF |
| Mission Database Storage Module | AF-MAAP1F-03-9301-04-FF |
| Mission Processor Module | AF-MAAP1F-03-9301-01-FF |
| Moving Map Display Software Module | AF-MAAP1F-03-9303-01-FF |
| MWIR Thermal Camera Module | AF-MAAP1F-03-9201-02-FF |
| Pilot Communication & Audio Panel Assembly | AF-MAAP1F-02-9404-FF |
| Pilot Crew Station Assembly | AF-MAAP1F-01-9400-FF |
| Pilot Flight Control Interfaces Assembly | AF-MAAP1F-02-9402-FF |
| Pilot Seats & Crashworthy Structure Assembly | AF-MAAP1F-02-9401-FF |
| Primary Tank Structure Assembly | AF-MAAP1F-02-9001-FF |
| Retardant Injection & Foam System Assembly | AF-MAAP1F-01-9600-FF |
| Retardant Injection Pump & Proportioning System Assembly | AF-MAAP1F-02-9602-FF |
| Retardant/Foam Tank Flushing & Cleaning System | AF-MAAP1F-02-9605-FF |
| Retractable Snorkel Probe Assembly | AF-MAAP1F-02-9501-FF |
| Fire Retardant Concentrate Tank Assembly | AF-MAAP1F-02-9601-FF |
| Smoke Penetration LIDAR Assembly | AF-MAAP1F-02-9203-FF |
| Snorkel Fill Control System Assembly | AF-MAAP1F-02-9503-FF |
| Tank Access Hatches & Inspection Ports | AF-MAAP1F-03-9001-04-FF |
| Tank Attach Hardpoint Fittings | AF-MAAP1F-03-9001-03-FF |
| Tank Baffle System Assembly | AF-MAAP1F-03-9001-02-FF |
| Tank Discharge System Assembly | AF-MAAP1F-02-9003-FF |
| Tank Fill System Assembly | AF-MAAP1F-02-9002-FF |
| Tank Level & CG Management System Assembly | AF-MAAP1F-02-9004-FF |
| Tank Pressurization & Vent System Assembly | AF-MAAP1F-02-9005-FF |
| Tank Thermal Insulation Assembly | AF-MAAP1F-03-9001-05-FF |
| Turret Control Electronics Unit | AF-MAAP1F-03-9201-07-FF |
| Turret Environmental Housing | AF-MAAP1F-03-9201-06-FF |
| Visible Light EO Camera (HD) | AF-MAAP1F-03-9201-04-FF |
| Water Fill Hose & Nozzle Assembly | AF-MAAP1F-02-9105-FF |
| Water Scooping System Assembly | AF-MAAP1F-01-9500-FF |
| Water Source Detection & Assessment System | AF-MAAP1F-02-9504-FF |
| Wide-Area Thermal Scanner Head | AF-MAAP1F-03-9202-01-FF |

---

## APPENDIX A — DRAWING TREE REVISION HISTORY

| Revision | Date | Description | ECO Number | Approver |
|---|---|---|---|---|
| A | [Current Date] | Initial Release | N/A | MAAP-1F Chief Engineer |

---

## APPENDIX B — CONFIGURATION CONTROL AND EFFECTIVITY

### Effectivity Matrix

This Drawing Tree applies to all MAAP-1F "Wildfire" Firefighting Variant aircraft with serial numbers in the range:
- **FF-0001** through **FF-9999**

### Configuration Baselines

| Configuration Item | Baseline Designation | Effectivity |
|---|---|---|
| Green Aircraft (Common Systems) | Baseline A | All MAAP-1F aircraft |
| Firefighting Mission Systems | FF-Baseline 1 | Serial FF-0001 to FF-0050 (LRIP) |
| Firefighting Mission Systems | FF-Baseline 2 | Serial FF-0051 onward (FRP, includes production improvements) |

### Change Incorporation

All Engineering Change Orders (ECOs) affecting the MAAP-1F Drawing Tree shall be processed through the Program Configuration Control Board (CCB) per CM Plan AF-MAAP1-CM-0001. Changes to Green Aircraft common systems require cross-variant impact assessment per PRB Section 12.

---

## SIGNATURE AND APPROVAL

**APPROVED FOR RELEASE:**

**[Signature]**  
**Name:** [MAAP-1F Variant Chief Engineer]  
**Title:** Chief Engineer, MAAP-1F Firefighting Variant  
**Organization:** Eurus Systems — MAAP-1 Program Office  
**Date:** _______________

**CONCURRENCE:**

**[Signature]**  
**Name:** [MAAP-1 Program Chief Engineer]  
**Title:** Chief Engineer, MAAP-1 Program (All Variants)  
**Organization:** Eurus Systems  
**Date:** _______________

**APPROVED:**

**[Signature]**  
**Name:** [MAAP-1 Program Manager]  
**Title:** Program Manager, MAAP-1 Program  
**Organization:** Eurus Systems  
**Date:** _______________

---

*END OF DRAWING TREE DOCUMENT AF-MAAP1F-DT-0003, REVISION A*

*This document contains technical data subject to export control under the International Traffic in Arms Regulations (ITAR, 22 CFR 120-130) and/or the Export Administration Regulations (EAR, 15 CFR 730-774). Unauthorized disclosure or transfer to foreign persons may result in criminal and civil penalties.*