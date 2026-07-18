# Project Management Plan Update — MAAP-1

**Document Control Information**

| Field | Detail |
|---|---|
| **Program** | MAAP-1 (Multi-Purpose Autonomous Aircraft Program) |
| **Document Type** | Project Management Plan Update — Formal Change Record |
| **Change Reference** | PCR-BAT-001: Primary Battery Supplier Transition, Samsung SDI → LG Energy Solution |
| **Revision** | Rev B (Supersedes Rev A Baseline) |
| **Prepared By** | Program Management Office |
| **Distribution** | Program VP, Chief Engineer, CFO, Supply Chain Director, CCB Chair, Program Controller, Electrical IPT Lead, Contracts Manager, Quality Director |
| **Authority** | CCB approval required prior to implementation; Program VP and CFO concurrence required given estimated cost impact exceeding $2M |
| **Status** | DRAFT — Pending CCB Review and Approval |

---

## 1. Introduction

### 1.1 Purpose of This Update

This Project Management Plan (PMP) Update formally documents the programmatic, technical, financial, and supply chain implications of Proposed Change PCR-BAT-001: the transition of the MAAP-1 primary battery supplier from Samsung SDI to LG Energy Solution (LGES). It supersedes the supplier management provisions of the Rev A baseline PMP with respect to the battery commodity and establishes the governance framework, decision gates, and execution requirements that must be satisfied before any transition is authorized.

This document has been produced by synthesizing four specialized agent analyses (Change Impact, Cost/Margin, Manufacturing, Supply Chain) and seven document-level impact assessments covering the Integrated Master Schedule (IMS), Risk Register, Program Requirements Baseline (PRB), Financial and Contract Management Plan, Manufacturing Ramp Plan, Supply Chain and Procurement Plan, Bill of Materials (BOM), and Customer Demand Forecast. All findings, recommendations, and risk entries herein reflect that consolidated body of analysis.

### 1.2 Background and Change Context

The MAAP-1 program Risk Register already identifies LG Energy Solution as the designated secondary battery supplier under RISK-SC-001, with a planned qualification completion target of Month 18 and qualification activities already initiated. Samsung SDI currently serves as the sole qualified primary supplier, a condition the Risk Register rates as **High risk (Score: 12, Likelihood: Medium, Consequence: High)** due to single-source dependency on a safety-critical, long-lead component.

PCR-BAT-001 proposes to **elevate LGES from secondary to primary supplier** and, by implication, to terminate or materially reduce the Samsung SDI relationship. While the strategic direction of this change — achieving dual-source resilience for a high-consequence commodity — is directionally consistent with the program's supply chain philosophy as applied to other critical items such as flight control processors and landing gear, the proposed change inverts the risk architecture at a moment when LGES qualification is incomplete. This PMP Update governs the conditions under which the transition can be executed safely, the costs that must be funded, the risks that must be managed, and the schedule constraints that must be respected.

### 1.3 Critical Preliminary Finding — BOM Chemistry Discrepancy

The BOM impact assessment has surfaced a material discrepancy that must be resolved before this change can be processed through the CCB. The current MAAP-1 BOM (document `maap1_bill_of_materials.md`, Section 7.3) specifies **Nickel-Cadmium (NiCd) chemistry** for the Main Battery Assembly (AF-MAAP1-EP-3001-00, 50Ah, 28VDC) and Emergency Battery Assembly (AF-MAAP1-EP-3002-00, 25Ah). Neither Samsung SDI nor LG Energy Solution is a primary aerospace NiCd manufacturer; both are lithium-ion/lithium-polymer cell manufacturers.

This discrepancy implies one of two scenarios:

- **Scenario A:** The PCR references an incorrect or superseded BOM revision, and Samsung SDI was never actually the primary battery supplier against the current specification. In this case, the entire premise of the change requires re-examination against the correct baseline.
- **Scenario B:** The PCR reflects an intended but not yet formally baselined conversion from NiCd to lithium-ion chemistry, in which case PCR-BAT-001 is not a supplier substitution but a **major design change** with substantially greater certification, cost, and schedule implications than a like-for-like supplier swap.

**Action Item BOM-001 (Owner: Chief Engineer; Due: 15 days from CCB submission):** Verify the current approved BOM revision, confirm the battery chemistry specification, and determine whether Samsung SDI or LG Energy Solution appears on any currently approved procurement document, approved supplier list entry, or qualification record. The CCB shall not approve the transition without written resolution of this discrepancy.

For the remainder of this PMP Update, analysis proceeds under the **working assumption that the program intends a lithium-ion battery system** consistent with the specialized agent analyses, and that the BOM requires correction or update as part of this change package. Where assumptions are made, they are explicitly noted.

### 1.4 Governing Documents

This PMP Update is issued under and consistent with the following program baseline documents:

- MAAP-1 Integrated Master Schedule (IMS), January 2025 Baseline
- MAAP-1 Program Requirements Baseline (PRB) and Requirements Baseline Continuation
- MAAP-1 Test and Evaluation Master Plan (TEMP)
- MAAP-1 Risk Register
- MAAP-1 Financial and Contract Management Plan
- MAAP-1 Supply Chain and Procurement Plan
- MAAP-1 Manufacturing Ramp Plan
- MAAP-1 Bill of Materials
- MAAP-1 Customer Demand Forecast
- MAAP-1 Quality Management Plan

---

## 2. Project Scope

### 2.1 Scope of the Proposed Change

PCR-BAT-001, as analyzed, encompasses the following scope elements:

**In Scope:**

1. **Primary supplier designation change:** LGES transitions from secondary/contingency status to primary qualified supplier for the MAAP-1 battery system (both Main Battery Assembly and Emergency Battery Assembly).

2. **Samsung SDI relationship restructuring:** Samsung SDI transitions from primary to secondary/backup status. Critically, this PMP Update does **not** authorize Samsung SDI contract termination prior to full LGES qualification. Any termination or reduction of Samsung SDI orders is a separate action requiring independent CCB approval and legal review of contractual termination liability.

3. **LGES qualification elevation:** The existing secondary supplier qualification effort is re-scoped from contingency-activation rigor to full primary supplier qualification, including First Article Inspection (FAI), AS9100D audit, capacity commitment verification, BMS IP technology escrow, cybersecurity assessment, and financial health review.

4. **Electrical interface delta assessment:** Formal evaluation of BMS communication protocol, voltage/current profile, thermal management interface, and data bus integration compatibility between Samsung SDI and LGES battery pack architectures against ICD-002 (Electrical Power Interface — Mission Bus, Load Shedding Priority).

5. **Configuration baseline updates:** Engineering Change Proposal (ECP) to update the BOM (Section 7.3), Electrical Interface drawings, BMS Interface Control Document, weight and balance documentation, and Illustrated Parts Catalog. RVTM-0001 must be updated to flag any Test-method requirements previously closed or in-progress using Samsung SDI hardware.

6. **Regulatory coordination:** Early engagement with FAA certification authority and DoD airworthiness office regarding supplier change notification and determination of whether a Major Change review under 14 CFR Part 21.93 (or equivalent military standard) is required.

7. **Buffer stock management:** Extension of the minimum battery pack buffer stock from 12 units (4 months) to 18 units (6 months) during the transition window to protect production continuity.

**Out of Scope (separate CCB actions required):**

- Samsung SDI contract termination (requires independent legal, contractual, and CCB review)
- Any avionics software modification driven by BMS protocol incompatibility (triggers separate DO-178C work order under avionics configuration control)
- Identification and qualification of a replacement secondary supplier to restore the dual-source architecture post-transition
- Any changes to propulsion, flight control, or other electrical power system components not directly interfacing with the battery system

### 2.2 Common Configuration Implications

Per the PRB (Section 5.1), the electrical power system is identified as a common configuration element across all three MAAP-1 variants (MAAP-1A, MAAP-1M, and MAAP-1C). A change to the primary battery supplier therefore constitutes a **common configuration impact event**. The Chief Engineer and Program Executive Officer must formally assess whether the LGES battery system can be accepted under common configuration status or whether a variant-specific waiver is required. Any deviation from common configuration triggers a cost, schedule, and logistics footprint impact assessment across all three variants prior to CCB approval.

### 2.3 Scope Boundaries and Exclusions

This change does not alter the MAAP-1 program's core performance requirements, Key Performance Parameters (KPPs), or Key System Attributes (KSAs) as defined in the PRB. No KPP threshold values are assessed as being at risk as a result of the supplier change itself, provided that LGES battery performance is demonstrated to be form, fit, and function equivalent (or superior) to the Samsung SDI specification baseline. The Chief Engineer and Electrical IPT must explicitly confirm this determination through the ICD-002 delta assessment before the CCB finalizes the change.

---

## 3. Milestone List & Schedule Baseline

### 3.1 Program Schedule Baseline (Unchanged)

The following key program milestones from the January 2025 IMS baseline remain the governing schedule targets. This PMP Update does not authorize any revision to these dates; rather, it identifies which milestones are at risk and establishes the conditions that must be met to protect them.

| Milestone | Baseline Date | Risk Status Post-PCR-BAT-001 |
|---|---|---|
| LRIP-1 First Delivery | Q3 2027 | **AT RISK** — Medium probability of 2–4 month slip if LGES qualification is not complete prior to Iron Bird integration |
| Long-Lead Material Procurement Cutoff | 01 Jul 2028 | **AT RISK** — LGES supply agreement and lead time visibility must be contractually secured before this date |
| DTA-3 Avionics/Electrical Integration | 22 Nov 2028 – 05 Jun 2029 | **AT RISK** — Battery interface verification feeds this activity; BMS compatibility must be confirmed |
| Safety Analysis / FMEA Completion (WBS 3.9.5) | Target: Sep 2027 | **AT RISK** — Must be re-opened or re-baselined for LGES cell chemistry if thermal runaway profiles differ |
| First Flight | Q2 2028 | **LOW-MEDIUM RISK** — Protected if qualification accelerated; threatened if BMS incompatibility found |
| Airworthiness Certification | 05 Jan 2032 | **MEDIUM RISK** — New battery qualification evidence must be integrated into the Type Certificate Data Package |
| IOC | Q1 2030 | **MEDIUM RISK** — 3–4 month certification delay could compress flight test margins |
| FRP | Q3 2030 | **LOW RISK** — Sufficient downstream buffer if LRIP issues are contained |
| Qualification Completion Constraint | Q4 2031 | **MEDIUM RISK** — Re-qualification thread must complete well before this constraint |

### 3.2 Transition Milestone Schedule (New — PCR-BAT-001 Specific)

The following transition milestones are established by this PMP Update as program-tracked events under the IMS change action. They must be formally inserted into the IMS network by the Schedule Manager within 30 days of CCB approval, with logic ties to the affected downstream milestones identified above.

| Transition Milestone | Target Completion | Owner | Go/No-Go Gate |
|---|---|---|---|
| **T-00: BOM Chemistry Discrepancy Resolution** | Day 15 from CCB submission | Chief Engineer | Gate 0: CCB cannot proceed without resolution |
| **T-01: BMS Interface Compatibility Study Initiated** | Day 30 from PCR-BAT-001 approval | Electrical IPT Lead / Avionics Systems Lead | — |
| **T-02: LGES Financial Health Assessment (D&B ≥3A2)** | Day 14 from PCR-BAT-001 approval | Supply Chain Director | Gate 1 prerequisite |
| **T-03: CCB Formal Review and Change Approval** | Day 30 from PCR-BAT-001 submission | CCB Chair | Gate 0 |
| **T-04: LGES Qualification Gap Assessment vs. Tier 1 Standards** | Day 30 from CCB approval | Supply Chain Director + Quality Director | Gate 1 prerequisite |
| **T-05: FAA/DoD Airworthiness Authority Engagement (Supplier Change Notification)** | Day 30 from CCB approval | Chief Engineer / DER | Gate 1 prerequisite |
| **T-06: Buffer Stock Extended to 18 Units** | Day 45 from CCB approval | Materials Manager | Gate 1 prerequisite |
| **T-07: BMS Compatibility Study Complete** | Day 45 from CCB approval | Electrical IPT Lead | Gate 1 prerequisite |
| **T-08: LGES Technology Escrow Agreement Executed** | Month 3 from CCB approval | Contracts Manager / Legal | Gate 2 prerequisite |
| **T-09: LGES LTA Negotiation Complete (Pricing, Lead Time, Volume)** | Month 3–4 from CCB approval | Commodity Manager | Gate 2 prerequisite |
| **T-10: LGES AS9100D Audit Complete — No Major Nonconformances** | Month 12 | Supply Chain Director + Quality Director | **Gate 1: Go/No-Go** |
| **T-11: LGES First Article Inspection (FAI) Initiated** | Month 12–13 | Quality Director | Gate 2 prerequisite |
| **T-12: FAI Complete — Zero Open Category 1 Discrepancies** | Month 15 | Quality Director | **Gate 2: Go/No-Go** |
| **T-13: FAA/DoD Major Change Determination Received** | Month 15 | Chief Engineer / DER | **Gate 2: Go/No-Go** |
| **T-14: LGES Full Qualification Complete — Primary Designation Authorized** | **Month 18** | Supply Chain Director | **Gate 3: Primary Switch Authorized** |
| **T-15: Samsung SDI Retained as Qualified Secondary — Minimum Order Cadence Established** | Month 18 | Commodity Manager / Contracts | Gate 3 concurrent |
| **T-16: Supplier Transition Readiness Review (Formal Board)** | Month 18 | Program Manager | **Gate 3: Go/No-Go** |
| **T-17: First LRIP-2 Battery Delivery from LGES** | Month 24 | Supply Chain Director | Gate 4 prerequisite |
| **T-18: LGES OTD ≥ 90%, Quality Conformance Verified (First 6 Months)** | Month 24–30 | Quality Director | **Gate 4: Volume Split Decision** |
| **T-19: Replacement Secondary Supplier Identification Initiated** | Month 12 | Supply Chain Director | Long-term dual-source restoration |

### 3.3 Schedule Reserve Assessment

The IMS carries program-level management reserve of 30 days (§14.2 of the IMS document). Transition activities, if poorly managed, could consume this reserve entirely through ripple effects into avionics integration and safety analysis activities. The Schedule Manager must re-run Monte Carlo simulation inputs (P50/P70/P90) within 60 days of CCB approval, incorporating the new transition milestone thread with realistic probability distributions. The following schedule risk drivers shall be specifically parametrized:

- BMS compatibility study outcome (binary: compatible vs. requires redesign)
- FAA/DoD Major Change determination timeline (4–12 weeks)
- LGES FAI anomaly rate (if Category 1 discrepancies found, FAI closure adds 4–8 weeks)
- DO-178C re-qualification scope if BMS software update is required (adds 6–12 weeks)

---

## 4. Change Management Plan

### 4.1 CCB Process and Authority

PCR-BAT-001 is classified as a **Tier 1 Strategic Supplier Substitution** — the highest tier of supply chain change under the program's change management framework. It requires the following approval hierarchy:

| Approval Level | Authority | Trigger Condition |
|---|---|---|
| **CCB Chair** | Standard CCB approval | All supplier changes |
| **Chief Engineer** | Technical concurrence | ICD-002 impact; KPP/KSA determination; common configuration assessment |
| **Program Manager** | Program authority | Schedule baseline impact; LD exposure |
| **Program VP** | Executive authority | Cost impact > $500K; reserve draw |
| **CFO** | Financial authority | Cost impact > $2M; reserve replenishment |
| **Program Executive Officer** | Senior authority | Common configuration waiver (if required); MDA notification |

Per the Financial and Contract Management Plan, **every proposed change requires a cost estimate, schedule impact assessment, and margin impact assessment** before CCB approval. The CCB is directed to reject changes with negative margin impact unless strategic justification is documented and approved at the Program VP level. Given the estimated cost range of $5M–$26M, CFO concurrence is required on the reserve draw before the CCB convenes.

### 4.2 Change Package Requirements

The CCB submission package for PCR-BAT-001 must include the following elements, all of which must be complete before the CCB convenes:

1. **Fully burdened cost estimate** — including direct qualification costs, one-time transition costs, unit cost delta analysis, overhead absorption impact, and LD exposure quantification (see Section 5 for detailed breakdown)
2. **Schedule impact assessment** — with Monte Carlo re-run showing P50/P70/P90 distribution shift against IOC and First Flight milestones
3. **Margin impact assessment** — showing effect on the 9.1% baseline gross margin under low, most-likely, and high-cost scenarios
4. **Reserve adequacy analysis** — demonstrating whether the $15M Supplier Risk reserve is sufficient for the low-cost scenario and identifying the replenishment mechanism for the high-cost scenario
5. **ICD-002 delta assessment** (preliminary) — Chief Engineer attestation that BMS interface compatibility assessment has been initiated and timeline to conclusion is established
6. **BOM discrepancy resolution** (Action Item BOM-001) — documented resolution before CCB convenes
7. **FAA/DoD engagement plan** — schedule for authority notification and timeline for Major Change determination
8. **Samsung SDI bridge plan** — confirming that SDI supply agreement remains active through at least Month 20 and that buffer stock is being extended to 18 units
9. **Legal review of Samsung SDI termination liability** — Contracts Manager assessment of contractual exposure if SDI relationship is modified
10. **LGES capability assessment** (preliminary) — including financial health (D&B), capacity to 48 units/year, and qualification status vs. Month 18 target

### 4.3 Configuration Management Actions

The following formal configuration management actions are triggered by CCB approval of PCR-BAT-001:

- **Engineering Change Proposal (ECP):** Formal ECP to be processed covering BOM Section 7.3 (all six affected line items), Electrical Interface drawings, BMS Interface Control Document, weight and balance documentation, and IPC
- **ICD-002 Revision (if required):** If BMS compatibility study finds any deviation in voltage curve, peak discharge characteristics, communication protocol, or fault reporting format, a formal ICD-002 revision must be processed through the CCB with impact assessed across MAAP-1A, MAAP-1M, and MAAP-1C
- **ICD-003 Assessment:** Avionics IPT shall assess whether BMS data protocol changes affect the core data bus architecture documented in ICD-003
- **RVTM-0001 Update:** All Test-method closure entries referencing Samsung SDI hardware must be flagged and re-verification activities assigned with Chief Engineer concurrence
- **Effectivity Break Documentation:** Configuration management system must record a clear effectivity break point identifying the first aircraft incorporating LGES versus Samsung SDI battery packs, ensuring full material traceability as required by FAA
- **Appendix A — Change Log:** Upon CCB approval, a new revision entry documenting PCR-BAT-001 with CCB reference number and authority signatures must be added to all affected controlled documents

### 4.4 Contract Modification Requirements

If the battery supplier is specified (directly or by reference) in the prime contract, program specification, or a Government-approved supply chain plan, a formal Contract Modification will be required. The Contracts Manager shall determine modification class within 30 days of CCB approval:

- **Class II:** Cost impact $1M–$5M — Contracts Manager lead, Program Manager approval
- **Class I:** Cost impact > $5M or schedule impact > 90 days — CFO and Program VP involvement; customer notification required

Per the Financial and Contract Management Plan pricing strategy, any customer-funded contract modification shall target **15–18% margin recovery** on the change, and the cost estimate submitted to the customer shall include direct qualification costs, overhead, a 20% contingency buffer per the program's standard cost estimation practice, and a documented margin allocation.

---

## 5. Cost Management Plan & Cost Baseline

### 5.1 Baseline Program Financial Position

The MAAP-1 program operates under a Firm Fixed Price (FFP) contract structure with the following financial baseline:

| Financial Parameter | Baseline Value |
|---|---|
| Total Contract Revenue | $4,778M |
| Baseline Program Margin | $398M (9.1%) |
| Total Risk Reserve | $74M |
| Supplier Risk Reserve (20% of total) | $15M |
| Current Supplier Risk Reserve Adequacy Ratio | 1.33× (Green) |

On a FFP contract, there is no cost recovery mechanism. Every dollar of unrecovered transition cost is a direct margin reduction. This makes the sequencing and execution quality of this transition critically important to program financial health.

### 5.2 One-Time Transition Cost Estimate

The following cost estimate represents the consolidated output of the cost/margin, change impact, manufacturing, and supply chain analyses. All figures are program estimates pending formal should-cost modeling.

| Cost Element | Low Case | Most Likely | High Case | Notes |
|---|---|---|---|---|
| LGES qualification and FAI (environmental, performance, safety testing) | $2.0M | $3.0M | $5.0M | Higher end if significant chemistry/interface delta found |
| BMS integration, software adaptation, and DO-178C re-qualification (if required) | $0.5M | $2.0M | $8.0M | High uncertainty; binary driver based on BMS compatibility study outcome |
| CCB/ECP processing, ICD revisions, drawing updates | $0.5M | $0.75M | $1.0M | Based on scope of configuration changes |
| LGES technology escrow agreement (BMS IP) | $0.1M | $0.3M | $0.5M | Legal and engineering effort |
| Samsung SDI contract transition costs (termination liability, NRE recovery, minimum purchase commitments) | $0.5M | $2.0M | $5.0M | Requires legal review; contractual; highly variable |
| Extended buffer stock procurement (18-unit extended buffer during transition) | $1.0M | $2.5M | $5.0M | Dependent on battery pack unit price |
| LGES supplier co-location engineering support (Supplier Quality Engineer on-site) | $0.3M | $0.5M | $0.8M | Per Tier 1 engagement model in Supply Chain Plan |
| Workforce training on LGES handling, installation, and inspection criteria | $0.1M | $0.15M | $0.2M | Production technicians and quality inspectors |
| Overhead absorption loss if production rate reduced during gap (1 aircraft/month contingency) | $0.0M | $0.0M | $8.0M | Only triggered if buffer stock depleted; zero if transition managed correctly |
| Liquidated damages exposure (LRIP lot delay: $250K/month cap $5M/lot) | $0.0M | $0.75M | $5.0M | Only triggered if Q3 2027 delivery slips |
| **Total One-Time Transition Cost** | **$5.0M** | **$12.0M** | **$38.5M** | High case includes worst-case BMS incompatibility + production rate reduction + LD |

**Working estimate for reserve planning: $10M–$18M (most likely to high-probability range)**

### 5.3 Recurring Unit Cost Impact

| Scenario | Recurring Impact | Notes |
|---|---|---|
| **Favorable** | −3% to −5% unit cost reduction on battery packs | LGES competitive pricing at volume + annual cost reduction commitments (≥3% per Strategic Partner model) |
| **Neutral** | 0% (cost parity) | Comparable pricing achieved through LTA negotiation |
| **Unfavorable** | +5% to +10% unit cost increase on battery packs | LGES commands premium for aerospace qualification overhead; learning curve reset; estimated $5M–$15M total program cost growth across 183 aircraft |

A formal should-cost model and competitive quote from LGES must be obtained and compared against the existing Samsung SDI contracted rates before any cost scenario can be confirmed. The Commodity Manager is directed to complete this analysis within 60 days of CCB approval. The LTA negotiation shall target an 88–92% learning curve slope for battery packs and a minimum 3% annual cost reduction commitment consistent with the Strategic Partner engagement model.

### 5.4 Margin Impact Analysis

| Cost Element | Low Case Margin Impact | High Case Margin Impact |
|---|---|---|
| Qualification and FAI costs | −0.04% | −0.10% |
| BMS integration and DO-178C re-qualification | −0.01% | −0.17% |
| Unit cost premium during transition period | −0.06% | −0.17% |
| Overhead absorption loss (rate reduction) | — | −0.17% |
| LD exposure | — | −0.10% |
| **Total Margin Impact** | **−0.10%** | **−0.54%** |

The high-case scenario ($38.5M total cost, −0.54% margin) represents **35% of the total $74M risk reserve** being consumed by a single change. In the context of the program's "Slow Burn" stress test — which shows margin compressing to 3.1% from a $248M cost overrun driven by learning curve underperformance, supplier cost escalation, and EPA cap risk — adding $15M–$38M from a battery transition gone wrong is a **meaningful contributor to potential margin collapse**. The "Perfect Storm" scenario already shows a potential $53M program loss; this change, poorly executed, closes that gap further.

### 5.5 Reserve Adequacy and Funding Mechanism

| Scenario | Required Reserve Draw | Current Reserve Adequacy Post-Draw | Status |
|---|---|---|---|
| Low case ($5M) | $5M from Supplier Risk Reserve | 0.67× | **Yellow** |
| Most-likely case ($12M) | $12M (exceeds $15M Supplier Risk Reserve) | Requires cross-reserve draw | **Red — Replenishment Required** |
| High case ($38.5M) | Exceeds all reserve categories | Corporate reserve escalation required | **Critical** |

**Reserve Funding Decision Rules:**

1. Transition costs driven by supply chain risk realization (e.g., Samsung SDI performance degradation, financial distress, geopolitical disruption) shall be drawn from the $15M Supplier Risk Reserve, not from program margin
2. Costs driven by a program-initiated preference change without a triggering risk event shall be self-funded from identified cost savings per the margin-neutral change funding policy
3. If the most-likely case ($12M) is confirmed as the working estimate, a reserve replenishment action must be initiated immediately, with the CFO identifying offsetting cost opportunities (accelerated automation ROI, renegotiation of other supplier agreements) to restore reserve adequacy above the 1.0× minimum threshold
4. If the high-cost scenario materializes, a formal corporate reserve escalation must be briefed to the Program VP and CFO, and a customer cost recovery conversation shall be initiated through the Contract Modification process at Class I authority level

### 5.6 Economic Price Adjustment (EPA) Considerations

The existing EPA clause structure covers Electronics/Avionics at 15% weighting using a PPI-Electrical Equipment index. Battery packs as a distinct commodity — with significant lithium, cobalt, and nickel material content — may not be adequately hedged by existing EPA indices. The Contracts Manager shall assess whether the LGES LTA requires a supplemental EPA clause tied to relevant battery material commodity indices. Failure to establish this protection exposes the program to unhedged cost risk that directly feeds the "Slow Burn" scenario, where supplier cost reductions failing to materialize were modeled as a $45M material cost risk.

---

## 6. Risk Management Plan & Risk Register

### 6.1 Risk Management Approach for PCR-BAT-001

All risks introduced or modified by PCR-BAT-001 shall be formally entered into the MAAP-1 Risk Register within 30 days of CCB approval. The Supply Chain Director (current Risk Owner for RISK-SC-001) is the designated Risk Owner for all transition-related risks until LGES achieves full primary qualification at Month 18 Gate 3. At Gate 3, risk ownership shall be formally transferred and the register updated to reflect the new steady-state risk posture.

Quarterly schedule risk assessments must include PCR-BAT-001 transition status as a standing agenda item until all Gate 4 criteria are satisfied.

### 6.2 Risk Register Updates — Existing Risks

**RISK-SC-001: Single-Source Battery Pack Supplier Creates Production Vulnerability**

| Field | Current State | Recommended Update |
|---|---|---|
| **Risk Score** | 12 (High) — Likelihood: Medium, Consequence: High | During transition (pre-Gate 3): **Elevated to 15–16 (Critical)** due to LGES qualification gap and potential SDI buffer erosion. Post-Gate 3 (LGES fully qualified, SDI retained as secondary): **Reduce to 8 (Medium)** |
| **Description** | Samsung SDI single-source primary; LGES qualification initiated | Update to reflect LGES elevated to primary designation target; SDI retained as bridge supplier; transition window identified as highest-risk period |
| **Mitigation — Secondary Supplier** | "Qualify LG Energy Solution by Month 18" | Identify and initiate qualification of a replacement secondary supplier (separate action); LGES is becoming primary, not secondary |
| **Mitigation — Buffer Stock** | 4-month / 12-unit minimum | Update to 6-month / 18-unit minimum during transition window; clarify that existing SDI buffer stock may not be compatible with LGES packs if form factor or BMS differs |
| **Mitigation — Technology Escrow** | Scoped to Samsung SDI BMS IP | Add: "Re-establish escrow agreement covering LG Energy Solution BMS IP (T-08)" |
| **Mitigation — Supply Agreement** | Structured for Samsung SDI | Add: "Negotiate new LTA with LGES including 6-month lead time visibility, volume pricing, and 3% annual cost reduction commitment" |
| **Status** | Open — Secondary supplier qualification initiated | Update to: "Open — Transition in progress; LGES primary designation pending Gate 3 approval; SDI bridge agreement maintained" |

**RISK-S-002: Certification Authority Engagement Delays Type Certification**

Current score: Critical (16). The battery supplier change adds an additional source of certification schedule pressure beyond existing GNC and autonomy certification risks. Update the risk description to include: *"Battery supplier substitution (PCR-BAT-001) introduces potential Major Change review requirement under 14 CFR Part 21.93; FAA engagement must be initiated within 30 days of CCB approval (T-05)."* The bi-weekly DER coordination cadence should include battery change status as a standing agenda item until FAA determination is received.

**RISK-C-002 and RISK-C-003: Unit Cost Escalation and Certification Cost Overrun**

Both risks require updated probability and impact inputs in the Monte Carlo simulation to reflect the transition-period cost spike. The Cost/Schedule Risk Owner shall update these entries with the PCR-BAT-001 cost estimate range and flag them at the next Program Management Review (PMR).

### 6.3 New Risk Register Entries — PCR-BAT-001

The following new risks are formally established by this PMP Update and must be entered into the Risk Register:

| Risk ID | Title | Likelihood | Consequence | Score | Owner |
|---|---|---|---|---|---|
| **RISK-SC-007** | Battery Supplier Transition Creates Temporary Single-Source Gap and Certification Re-work | Medium | High | **12 (High)** | Supply Chain Director |
| **RISK-CERT-001** | FAA/DoD Requires Major Change Re-approval for Battery Supplier Substitution | Low–Medium | High | **9 (Medium)** | Chief Engineer / DER |
| **RISK-TECH-001** | BMS Interface Incompatibility Requires ICD-002 Revision and Avionics Software Re-qualification (DO-178C) | Low–Medium | High | **9 (Medium)** | Electrical IPT Lead |
| **RISK-SC-008** | LGES Qualification Delay Beyond Month 18 Threatens LRIP-1 First Delivery (Q3 2027) | Medium | High | **12 (High)** | Supply Chain Director |
| **RISK-SC-009** | Samsung SDI Termination Costs Exceed Budget Allocation / Legal Exposure | Low–Medium | Medium | **6 (Medium)** | Contracts Manager / Legal |
| **RISK-SC-010** | Korean Supplier Geographic Concentration Unchanged — Geopolitical Risk Not Mitigated | Medium (ongoing) | High | **12 (High)** | Supply Chain Director |
| **RISK-FIN-001** | Supplier Risk Reserve Inadequacy — Transition Costs Exhaust $15M Reserve in Most-Likely Scenario | Medium | High | **12 (High)** | Program Controller / CFO |
| **RISK-MFG-001** | Production Rate Reduction to 1 Aircraft/Month Triggered by Battery Supply Gap During Transition | Low–Medium | High | **9 (Medium)** | Manufacturing Director |
| **RISK-BOM-001** | BOM Chemistry Discrepancy (NiCd vs. Li-ion) — Change Request Based on Incorrect Source Data | High (if unresolved) | Critical | **16 (Critical)** | Chief Engineer |

### 6.4 Risk Mitigation Actions (Consolidated)

| Risk ID | Primary Mitigation | Secondary Mitigation | Contingency |
|---|---|---|---|
| RISK-SC-001 (updated) | Retain SDI through Month 20; extend buffer to 18 units | Accelerate LGES qualification; assign resident SQE at LGES facility | Activate broker procurement at premium; invoke contingency production rate reduction |
| RISK-SC-007 | Gate-based transition framework (Gates 1–4); SDI bridge agreement | 18-unit buffer stock maintained throughout transition | Revert to SDI primary if LGES fails Gate 3 |
| RISK-CERT-001 | FAA/DoD engagement initiated Day 30 (T-05); written determination requested before qualification spend committed | DER pre-submission of battery qualification data package | Extend SDI supply agreement if certification delay materializes |
| RISK-TECH-001 | BMS compatibility study completed Day 45 (T-07); ICD-002 delta assessment initiated immediately | Scope DO-178C impact before committing to LGES qualification spend | Require LGES BMS protocol to match SDI as a procurement specification requirement |
| RISK-SC-008 | Assign dedicated Supplier Quality Engineer to LGES facility; parallel qualification testing where possible | Gate 1 go/no-go at Month 12 provides early warning | Maintain SDI as primary beyond Month 18 if Gate 3 criteria not met |
| RISK-SC-010 | Accept residual risk; document in risk register | Initiate long-term domestic third-source assessment at FRP gate | No near-term mitigation available; geopolitical diversification requires multi-year effort |
| RISK-FIN-001 | CCB change not approved without reserve adequacy review and CFO concurrence | Identify offsetting cost savings to replenish reserve | Corporate reserve escalation; customer cost recovery conversation |
| RISK-BOM-001 | Action Item BOM-001 — resolve within 15 days; CCB cannot convene without resolution | N/A | If Scenario B (NiCd→Li-ion conversion), re-scope PCR-BAT-001 as major design change |

---

## 7. Procurement / Supply Chain Management Plan

### 7.1 Supplier Tier Classification and Engagement Model

LG Energy Solution is designated as a **Tier 1 Strategic Supplier candidate** for the MAAP-1 battery system upon CCB approval of PCR-BAT-001. Full Tier 1 Strategic designation is contingent on satisfying all Gate 3 criteria by Month 18. Prior to Gate 3, LGES is managed under an **accelerated qualification track** with oversight equivalent to Tier 1 Preferred Supplier status, including:

- Monthly operational reviews (conducted by Commodity Manager)
- Formal qualification milestone tracking against transition milestones T-02 through T-14
- Source inspection at LGES facility during initial production runs (monthly minimum for the first 6 months post-FAI)
- Resident Supplier Quality Engineer (SQE) co-located at LGES manufacturing facility from T-10 through T-17

Samsung SDI shall be maintained as a **Tier 1 Preferred Supplier (bridge status)** throughout the transition period, with no reduction in engagement cadence or supply agreement terms until Gate 3 is formally passed and a bridge wind-down plan is approved by the CCB.

### 7.2 Samsung SDI Relationship Management

**The most critical single supply chain management action is: Do not terminate Samsung SDI until LGES Gate 3 qualification is complete and verified.**

The following requirements govern the Samsung SDI relationship during the transition:

1. A **bridge purchase order** covering LRIP-1 full demand plus the 18-unit extended buffer stock must be issued within 30 days of CCB approval — before any notification is made to Samsung SDI regarding primary supplier status change
2. The Contracts Manager and Legal shall complete a full review of the Samsung SDI Long-Term Agreement (LTA) within 30 days, specifically assessing: early termination penalties, minimum purchase commitments, tooling ownership, advance material orders, and any government-flow-down requirements
3. Samsung SDI shall not be notified of the primary status change until the bridge purchase order and legal review are both complete
4. The Samsung SDI technology escrow agreement for BMS IP shall remain in full effect throughout the transition period; disposition of this escrow agreement shall be addressed only after LGES technology escrow is fully executed (T-08)
5. Post-Gate 3, Samsung SDI shall be retained as a **Qualified Secondary Supplier** with a minimum periodic order cadence (frequency to be determined by Commodity Manager) sufficient to maintain production familiarity and qualification currency — consistent with the program's dual-sourcing philosophy as applied to landing gear (Safran primary, second source at FRP-1)

### 7.3 LG Energy Solution Supplier Qualification Requirements

Full Tier 1 Strategic Supplier qualification for LGES requires the following elements, all of which are Gate 3 prerequisites:

| Qualification Element | Standard | Gate Required | Owner |
|---|---|---|---|
| AS9100D Certification (or equivalent) | Verified by external audit; no major nonconformances | Gate 1 (Month 12) | Quality Director |
| Financial Health Assessment | D&B rating ≥3A2; annual financial review | Gate 1 (Month 12) | Supply Chain Director |
| Demonstrated aerospace capability | Prior aerospace program evidence; capacity assessment to 48 units/year | Gate 1 (Month 12) | Commodity Manager |
| Cybersecurity Assessment | NIST SP 800-171 compliance; self-assessment plus program review | Gate 2 (Month 15) | IT Security / Export Compliance |
| ITAR Registration | Required if handling CUI or export-controlled data | Gate 2 (Month 15) | Export Compliance |
| Conflict Mineral Compliance | 3TG conflict-free sourcing certification | Gate 2 (Month 15) | Supply Chain Director |
| Technology Escrow Agreement (BMS IP) | Executed agreement covering LGES BMS architecture | Gate 2 (Month 15) | Contracts Manager / Legal |
| Business Continuity Plan | 30-day safety stock of critical sub-tier components | Gate 2 (Month 15) | Supply Chain Director |
| First Article Inspection (FAI) | AS9102B compliant; zero open Category 1 discrepancies | Gate 2 (Month 15) | Quality Director |
| Capacity commitment to 48 units/year | Contractually secured in LTA | Gate 3 (Month 18) | Commodity Manager |
| LTA executed | Pricing, lead times, learning curve, volume commitments, annual cost reduction (≥3%) | Gate 3 (Month 18) | Commodity Manager / Contracts |
| 6-month lead time visibility | Contractually required; demonstrated | Gate 3 (Month 18) | Supply Chain Director |
| FAA/DoD battery data package submitted | Qualification evidence package accepted by authority | Gate 3 (Month 18) | Chief Engineer / DER |

### 7.4 Long-Term Agreement (LTA) Negotiation Parameters

The Commodity Manager is directed to negotiate the LGES LTA to the following minimum commercial terms, consistent with the Strategic Partner engagement model in the Supply Chain and Procurement Plan:

- **Pricing structure:** Volume-tiered unit pricing at production rates of 2, 6, 12, 24, and 48 units/year; initial pricing locked for 24 months
- **Learning curve:** Target 88–92% slope; contractually defined and tracked against actuals
- **Annual cost reduction commitment:** ≥3% per year from LTA execution date
- **Lead time commitment:** Maximum 6-month production lead time from purchase order to delivery; 12-month demand visibility window provided by program
- **Minimum order quantities:** Set at levels that sustain LGES production familiarity without creating excess inventory
- **EPA clause:** Negotiate supplemental EPA tied to relevant battery material commodity indices (lithium carbonate, cobalt sulfate, NMC precursor) to hedge against raw material cost volatility not covered by the existing program EPA structure
- **EOL notification:** 24-month minimum advance notice required for any cell chemistry discontinuation per the Supply Chain Plan obsolescence mitigation standard
- **Capacity reservation:** LGES must contractually reserve manufacturing capacity to meet FRP-2 peak rate (48 units/year) with 90-day activation notice

### 7.5 Replacement Secondary Supplier Strategy

The transition of LGES from secondary to primary designation eliminates the dual-source architecture the program was building. **A replacement secondary supplier identification and qualification program must be initiated by Month 12 (T-19)**, concurrent with the LGES qualification completion effort. This is not optional — the program's supply chain risk philosophy applied to other critical components (flight control processors, landing gear) requires dual-source coverage for all High-risk, safety-critical items.

Candidate replacement secondary suppliers for assessment include established aerospace battery manufacturers. The Supply Chain Director shall present a replacement secondary supplier recommendation to the CCB no later than Month 15.

### 7.6 Geopolitical Diversification Assessment

A critical finding of the supply chain analysis is that **both Samsung SDI and LG Energy Solution are South Korean manufacturers**. The proposed change provides zero improvement in geographic concentration risk (RISK-SC-010, DR-018). If geopolitical resilience is a stated driver for this change, it must be acknowledged that the change does not address it. The Supply Chain Director shall include in the LRIP-3 Gate review package an assessment of whether a domestic U.S. battery manufacturer (e.g., a domestic cell manufacturer with aerospace qualification history) should be pursued as a long-term third source or eventual primary, and whether the program's FRP-gate supplier strategy should be updated accordingly.

### 7.7 Make-or-Buy Alignment

The vertical integration strategy confirms that batteries remain a **BUY item**. Battery pack manufacturing is capital-intensive, technology-specialized, and non-core to the program's differentiating capabilities. This determination is unchanged by PCR-BAT-001. The change is a within-BUY sourcing decision. No make-or-buy reconsideration is required.

---

## 8. Quality Management Plan

### 8.1 Quality Oversight Philosophy for Supplier Transition

The battery system is a safety-critical, flight-essential component. All quality management activities associated with the LGES transition shall be governed by the program's phase-based quality strategy, with **elevated surveillance applied throughout the transition period** consistent with the precedent established for fastener quality management (100% receiving inspection for first 10 lots) and the first-article inspection requirements applied to other Tier 1 supplier onboarding actions.

### 8.2 First Article Inspection (FAI) Requirements

Per AS9102B, a supplier change for a critical component mandates a new and complete First Article Inspection. The LGES FAI shall include:

1. **Full dimensional inspection** of the first production unit from LGES against the applicable drawing and specification baseline
2. **Functional and performance testing** against the battery system specification (capacity, voltage profile, peak discharge, cycle life at acceptance criteria level)
3. **BMS software version control verification** — LGES BMS firmware version and configuration baseline must be formally established and documented as a controlled configuration item
4. **Material certifications and traceability documentation** — full material traceability from raw cell to delivered pack assembly
5. **Integration testing** on the aircraft electrical system testbed, confirming ICD-002 interface compliance
6. **Thermal characterization validation** — confirm thermal runaway propagation path and thermal management interface compatibility with existing Battery Box Assemblies (AF-MAAP1-EP-3003-00 and -3004-00)

**Planned FAI duration: 12–16 weeks** from first article delivery to FAI closure, assuming no anomalies. The Quality Director shall establish a FAI execution plan with weekly status reporting to the Supply Chain Director and Program Manager beginning at T-11.

### 8.3 Receiving Inspection Requirements

- **First 10 production lots from LGES: 100% receiving inspection** — all Critical and Key Characteristics verified per the Characteristics Control Plan
- **Lots 11–30: 50% sampling inspection** — subject to reduction to 25% sampling upon demonstration of ≥99% conformance rate over 10 consecutive lots with zero Critical characteristic escapes
- **Steady state (Lot 31+): Standard sampling per ANSI/ASQ Z1.4** — subject to re-elevation to 100% if any Critical characteristic escape occurs

### 8.4 Critical Characteristic Designation

The following battery pack parameters shall be designated as **Critical Characteristics** requiring 100% verification at receiving inspection throughout the qualification period:

- Delivered energy capacity (Ah) — within ±2% of specification
- Open circuit voltage at delivery — within specification band
- Cell balance (maximum cell-to-cell voltage deviation) — at delivery inspection
- BMS firmware version (label and electronic verification) — must match approved configuration baseline
- Physical integrity (no visible damage, connector engagement verification)
- Thermal management interface confirmation (cooling plate contact verification)

### 8.5 Supplier Quality Plan Requirements

A new **LGES-specific Supplier Quality Plan (SQP)** must be developed, reviewed, and approved before the first LGES production delivery enters the assembly flow. The SQP shall include:

- LGES quality management system description and AS9100D certification evidence
- Process FMEA for battery pack manufacturing, with specific coverage of cell selection, assembly, BMS installation, and pack-level testing
- Control Plan for all Critical and Key Characteristics
- Statistical Process Control (SPC) requirements for key in-process parameters
- Corrective Action and Preventive Action (CAPA) process interface with the program's supplier corrective action system
- Source inspection access rights for program Supplier Quality Engineers at LGES facility
- First-article and periodic lot testing requirements

### 8.6 Process FMEA Update Requirements

The existing Process FMEA for battery installation operations must be updated to:

- Reflect any LGES-specific handling requirements (electrostatic sensitivity, temperature conditioning, transportation orientation)
- Address any changes in torque specifications for LGES battery mounting interface
- Capture new failure modes associated with LGES-specific BMS architecture if BMS compatibility study identifies differences
- Update thermal runaway failure mode analysis if LGES cell chemistry produces different thermal runaway characteristics than the Samsung SDI baseline

The updated Process FMEA must be reviewed and approved by the Quality Director and Chief Systems Engineer before the first LGES unit enters the assembly flow.

### 8.7 Configuration Management Quality Gates

The following quality-controlled configuration management actions are required in sequence:

1. **Pre-transition:** Chief Engineer approval of ICD-002 delta assessment; confirmation that no KPP/KSA thresholds are at risk from LGES substitution
2. **Pre-FAI:** Approved LGES drawing baseline and part number established in the configuration management system; effectivity break documented
3. **FAI closure:** Quality Director sign-off required before any production LGES units are accepted into the assembly line
4. **Gate 3 prerequisite:** Zero open Category 1 discrepancies in FAI; receiving inspection first 10 lots complete with documented results

---

## 9. Staffing & Resource Management

### 9.1 Staffing Implications

The LGES qualification and transition program requires dedicated staffing resources beyond the current program baseline plan. The following positions and assignments are required:

| Role | Assignment | Duration | Notes |
|---|---|---|---|
| **Resident Supplier Quality Engineer (SQE)** | Co-located at LGES manufacturing facility | Months 10–24 (pre-FAI through first LRIP-2 delivery) | Dedicated, not split-funded; serves as program's primary quality interface at LGES |
| **Battery System Lead Engineer** | LGES interface technical authority | Months 1–18 | Leads BMS compatibility study; ICD-002 delta assessment; FAI witness |
| **Commodity Manager (Battery)** | LGES LTA negotiation and ongoing supplier management | Full transition period through Gate 4 | Elevated from standard cadence to weekly engagement during transition |
| **Electrical IPT Representative** | BMS compatibility study and ICD-002 revision (if required) | Months 1–8 | Dedicated involvement through BMS compatibility study completion; part-time thereafter |
| **Avionics IPT Representative** | ICD-003 assessment; BMS data protocol compatibility | Months 1–4 | Scoped effort; terminates after ICD-003 determination |
| **Legal / Contracts** | Samsung SDI LTA review; LGES LTA negotiation; technology escrow agreements | Months 1–6 | Peak effort at transition initiation; reduces to periodic review thereafter |
| **Export Compliance** | ITAR review; LGES cybersecurity assessment coordination | Months 2–6 | Discrete effort |
| **Program Controller** | Reserve draw tracking; margin impact reporting; Monte Carlo re-run | Monthly throughout transition | Adds battery supplier transition as standing cost reporting element |
| **Schedule Manager** | IMS update; new WBS thread insertion; Monte Carlo simulation update | Months 1–2 (initial); quarterly thereafter | New transition milestone thread must be in IMS within 30 days of CCB approval |

### 9.2 Resource Loading and Budget

The staffing resources identified above are not currently planned in the program baseline headcount and represent an **incremental resource requirement** that must be funded from the transition cost estimate (Section 5.2). The supplier co-location SQE cost alone is estimated at $300K–$800K over the 14-month co-location period. The Program Manager shall direct the Program Controller to include all staffing costs associated with PCR-BAT-001 in the fully burdened cost estimate submitted to the CCB.

### 9.3 Training Requirements

Production technicians and quality inspectors who will handle, install, and inspect LGES battery packs must receive formal training before the first LGES unit enters the assembly flow. Minimum training content:

- LGES battery pack handling procedures (ESD, temperature conditioning, transportation orientation)
- Installation and torque procedures reflecting any LGES-specific mechanical interface differences
- LGES BMS visual inspection criteria (connector verification, firmware version label check)
- Emergency response procedures for LGES cell chemistry (thermal runaway characteristics may differ from SDI baseline)
- Receiving inspection criteria and Critical Characteristic verification methods

Training materials shall be developed by the Manufacturing Engineering team in coordination with the Resident SQE and reviewed by the Quality Director before first use. Training records shall be maintained in the program configuration management system.

### 9.4 Organizational Responsibility Matrix (PCR-BAT-001)

| Function | Role in Transition |
|---|---|
| **Chief Engineer** | ICD-002 delta assessment authority; KPP/KSA confirmation; common configuration waiver (if required); FAA/DoD engagement lead |
| **Supply Chain Director** | Overall Risk Owner (RISK-SC-001, -SC-007, -SC-008, -SC-010); LGES qualification oversight; Gate 1–4 go/no-go authority |
| **Quality Director** | LGES SQP approval; FAI execution authority; receiving inspection program; Gate 1–3 quality sign-off |
| **Electrical IPT Lead** | BMS compatibility study lead; ICD-002 revision (if required) |
| **Avionics IPT Lead** | ICD-003 assessment; BMS data bus protocol review |
| **Commodity Manager** | LGES LTA negotiation; SDI bridge agreement maintenance; replacement secondary supplier identification |
| **Program Controller** | Reserve adequacy tracking; margin impact reporting; Monte Carlo inputs |
| **Schedule Manager** | IMS update; Monte Carlo simulation; milestone tracking |
| **Contracts Manager** | SDI LTA termination liability review; LGES LTA execution; technology escrow agreements; contract modification |
| **Legal** | SDI termination liability assessment; LGES technology escrow negotiation |
| **Export Compliance** | ITAR review; LGES cybersecurity assessment |
| **Manufacturing Director** | Production rate contingency readiness; workforce training; Work Instruction updates |
| **Program Manager** | CCB submission authority; Gate 3–4 decision authority; customer notification (if required by contract) |

---

## 10. Overall Assessment & Recommended Path Forward

### 10.1 Overall Change Assessment Summary

| Dimension | Pre-Mitigation Assessment | Post-Mitigation Assessment (if executed per this PMP Update) |
|---|---|---|
| **Certification Timeline** | High risk — 6–12 month slip if pursued as immediate primary swap | Medium risk — 2–4 month slip if qualification accelerated and BMS compatibility confirmed early |
| **Unit Cost (Transition)** | $5M–$38.5M one-time; wide range reflecting BMS uncertainty | $10M–$18M most-likely with proper execution; low case achievable if BMS compatibility confirmed quickly |
| **Unit Cost (Steady State)** | Neutral to +10% until LTA locked | Neutral to −3% with competitive LTA and learning curve commitments |
| **Supply Chain Risk Score** | Elevated to 15–16 (Critical) during unconstrained transition | Held to 12 (High) during transition; reduced to 8 (Medium) post-Gate 3 |
| **Reserve Adequacy** | 0.75–0.92× (Red) under most-likely and high cost scenarios | 1.10× (Yellow) if CCB-controlled reserve draw and replenishment actions are executed |
| **Production Continuity** | At risk during transition gap | Protected by 18-unit extended buffer stock and SDI bridge agreement |
| **Dual-Source Architecture** | Temporarily dismantled | Restored at Gate 3 (LGES primary, SDI secondary); replacement secondary qualified by FRP-1 |
| **Geopolitical Diversification** | No improvement (both suppliers South Korean) | No improvement — documented as residual risk; long-term domestic sourcing assessment initiated |
| **Program Margin** | −0.10% to −0.54% direct impact | −0.10% to −0.30% with competitive LTA and cost recovery through contract modification |
| **Overall Change Risk** | HIGH | MEDIUM (with full mitigation execution) |

### 10.2 Strategic Recommendation

**The proposed change is strategically defensible but must not be executed as a simple supplier swap.** The dual-source architecture that LGES primary + SDI secondary represents is the correct long-term end-state — consistent with the program's supply chain philosophy and the original intent of RISK-SC-001. However, executing a full primary supplier designation before LGES qualification is complete, before the BMS compatibility question is answered, and before the FAA/DoD certification authority has weighed in on supplier change requirements would be **a significant program risk event that could consume program reserves, threaten the Q3 2027 LRIP-1 delivery, and compress the First Flight and IOC schedule margins**.

The recommended path forward is a **controlled, gate-managed dual-source transition** — not a supplier swap. The framing of this change should be communicated internally and to the customer (if applicable) as: *"Establishing LG Energy Solution as co-primary battery supplier while retaining Samsung SDI as qualified secondary, with competitive volume allocation at FRP based on demonstrated performance and pricing."* This framing:

- Avoids the risk of a single-source gap during transition
- Creates competitive pricing pressure on Samsung SDI throughout the transition period
- Achieves the supply chain resilience objective without creating a certification gap
- Is consistent with the landing gear dual-source model already embedded in the program

### 10.3 Decision Recommendation

**The CCB is directed to:**

1. **Authorize PCR-BAT-001 in principle**, subject to resolution of the BOM chemistry discrepancy (Action Item BOM-001) and submission of the complete CCB change package per Section 4.2
2. **Re-frame the change** from "primary supplier substitution" to "dual-source qualification with LGES as designated primary at Gate 3" — this framing is lower-risk and equally achieves the supply chain resilience objective
3. **Require a reserve adequacy review and CFO concurrence** before formally approving any reserve draw; the most-likely cost scenario ($12M) exceeds the $15M Supplier Risk Reserve when considered alongside other concurrent supplier risks
4. **Require Gate 1 go/no-go results** (Month 12) before any modification or termination action against the Samsung SDI supply agreement
5. **Reject any transition action that would reduce Samsung SDI supply below 18-unit buffer stock threshold** at any point before Gate 3 is formally passed

### 10.4 Immediate Action Items (Next 30 Days)

The following actions must be completed within 30 days regardless of CCB status, as they are prerequisite to any transition decision:

| Priority | Action | Owner | Due Date |
|---|---|---|---|
| **CRITICAL** | Resolve BOM chemistry discrepancy (Action BOM-001) — confirm battery specification and whether Samsung SDI/LGES appear on any current procurement document | Chief Engineer | Day 15 |
| **CRITICAL** | Issue Samsung SDI bridge purchase order covering LRIP-1 demand + 18-unit buffer; do not notify SDI of primary status change before bridge order is placed | Commodity Manager | Day 20 |
| **CRITICAL** | Legal review of Samsung SDI LTA — termination liability, minimum purchase commitments, tooling ownership | Contracts Manager / Legal | Day 30 |
| **CRITICAL** | Initiate BMS Interface Compatibility Study — assign Electrical IPT lead and Avionics IPT representative | Electrical IPT Lead | Day 30 |
| **HIGH** | Complete LGES Financial Health Assessment (D&B ≥3A2) | Supply Chain Director | Day 14 |
| **HIGH** | Initiate FAA/DoD supplier change notification engagement; request written determination on Major Change status | Chief Engineer / DER | Day 30 |
| **HIGH** | Prepare complete CCB change package per Section 4.2 requirements | Program Controller + Supply Chain Director | Day 30 |
| **HIGH** | Update Risk Register — elevate RISK-SC-001 to transition-period score; add RISK-SC-007 through RISK-BOM-001 | Supply Chain Director | Day 30 |
| **HIGH** | Conduct reserve adequacy review; brief CFO on estimated transition cost range | Program Controller | Day 30 |
| **MEDIUM** | Insert new battery supplier transition WBS thread in IMS network; re-run Monte Carlo simulation | Schedule Manager | Day 45 |
| **MEDIUM** | Identify replacement secondary supplier candidates; present recommendation by Month 15 | Supply Chain Director | Month 15 |

### 10.5 Success Criteria for This Change

This change will be considered successfully executed when all of the following conditions are met:

1. LGES achieves full Tier 1 Strategic Supplier qualification per all Gate 3 criteria by Month 18
2. LGES LTA is executed with pricing at or below Samsung SDI contracted rates, a documented learning curve slope of 88–92%, and a 3% annual cost reduction commitment
3. Samsung SDI is retained as a Qualified Secondary Supplier with an executed secondary supply agreement and minimum periodic order cadence
4. The 18-unit buffer stock is maintained continuously throughout the transition period without drawdown
5. FAA/DoD Major Change determination is received and the battery qualification evidence package is accepted by the certifying authority without requiring re-opening of the Type Certificate basis
6. ICD-002 delta assessment confirms full electrical interface compatibility, or — if an ICD revision is required — the revised ICD is CCB-approved and assessed across all three variants without schedule impact beyond the transition milestone plan
7. LRIP-1 first delivery (Q3 2027) is achieved on schedule
8. No LD is triggered as a result of the battery supplier transition
9. Total transition cost is contained within the most-likely estimate ($12M) or below
10. A replacement secondary supplier qualification is initiated by Month 12 and a candidate is recommended to the CCB by Month 15, with qualification targeting completion no later than FRP-1

---

**Document Approval Signatures (Required Before Distribution)**

| Role | Name | Signature | Date |
|---|---|---|---|
| Program Manager | | | |
| Chief Engineer | | | |
| Supply Chain Director | | | |
| Program Controller | | | |
| Quality Director | | | |
| CCB Chair | | | |
| Program VP | | | |
| CFO (if reserve draw confirmed > $2M) | | | |

---

*This PMP Update is a controlled program document. Revisions require CCB approval. The next scheduled review is the Month 12 Gate 1 decision board, at which point this document shall be updated to reflect qualification status, BMS compatibility study results, FAA/DoD determination status, and reserve adequacy position.*