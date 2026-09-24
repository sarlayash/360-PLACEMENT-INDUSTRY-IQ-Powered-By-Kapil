# Questions Level 3: Industry (Q41-Q60) and Level 4: Advanced (Q61-Q70)
from generate_base import make_q

def get_level3_and_part4():
    questions = []

    # =========================================================================
    # LEVEL 3: INDUSTRY (Q41 - Q60)
    # =========================================================================

    # Q41: Industry - Healthcare / Ethics & Operational Judgment
    questions.append(make_q(
        41, 3, "Ethical",
        "In a hospital or healthcare administration software rollout, an analytics algorithm flags emergency room readmission risks, but clinical staff report that the interface requires 6 extra clicks per patient, slowing emergency triage.",
        "How do you resolve the friction between clinical workflow speed and predictive risk analytics?",
        [
            ("A", "Mandate that nurses and doctors complete every field under threat of disciplinary reprimand.", {"eq": 35, "leadership_iq": 40, "job_readiness_iq": 45, "ethics_judgment_iq": 45}, "high", "punitive_mandate"),
            ("B", "Deploy a rapid workflow shadow team to observe ER triage firsthand, redesign the UI to auto-populate existing vital stats, and reduce required inputs to a single high-priority alert.", {"problem_solving_iq": 95, "critical_thinking_iq": 95, "leadership_iq": 90, "eq": 90}, "low", "context_aware_redesign"),
            ("C", "Turn off the predictive risk model completely and abandon clinical analytics.", {"problem_solving_iq": 45, "business_iq": 40, "adaptability_iq": 40, "aiq": 40}, "moderate", "premature_abandonment"),
            ("D", "Advise clinicians to enter dummy data during emergencies and fix records later.", {"ethics_judgment_iq": 30, "critical_thinking_iq": 35, "job_readiness_iq": 30, "risk": "high"}, "high", "data_pollution")
        ],
        {"problem_solving_iq": 35, "critical_thinking_iq": 30, "eq": 20, "ethics_judgment_iq": 15},
        45,
        "Technology implementations in mission-critical environments must adapt to frontline human workflows, not the other way around.",
        "Observe frontline friction directly; eliminate redundant data entry before demanding clinical compliance.",
        ["Healthcare", "IT", "Operations"]
    ))

    # Q42: Industry - Finance / Risk Management & Critical Thinking (with Micro-Scenario)
    questions.append(make_q(
        42, 3, "Business",
        "Your financial risk model indicates that an emerging loan portfolio yields 18% annualized returns, but 42% of borrowers have non-standard credit histories concentrated in a single fluctuating regional industry.",
        "What risk-adjusted recommendation do you deliver to the investment committee?",
        [
            ("A", "Recommend doubling portfolio exposure immediately to capitalize on the 18% yields before competitors enter.", {"critical_thinking_iq": 35, "business_iq": 40, "ethics_judgment_iq": 40, "iq": 45}, "high", "unhedged_greed"),
            ("B", "Advise capping single-industry exposure, structuring dynamic loss reserves, and requiring stress-testing against regional downturn scenarios before expanding capital allocation.", {"critical_thinking_iq": 98, "business_iq": 95, "problem_solving_iq": 90, "iq": 90}, "low", "stress_tested_hedging"),
            ("C", "Recommend terminating the entire credit product line immediately due to regional concentration.", {"business_iq": 55, "adaptability_iq": 50, "critical_thinking_iq": 55, "sales_iq": 50}, "moderate", "overly_risk_averse"),
            ("D", "Change the regional classification tags in the model so the concentration appears dispersed.", {"ethics_judgment_iq": 15, "business_iq": 20, "job_readiness_iq": 20, "risk": "high"}, "high", "regulatory_fraud")
        ],
        {"critical_thinking_iq": 40, "business_iq": 35, "problem_solving_iq": 15, "iq": 10},
        50,
        "Prudent capital management recognizes that outsized yield is invariably compensation for hidden correlation risk.",
        "Always stress-test high yields against correlated regional shocks; institute exposure caps and capital buffers.",
        ["Finance", "Banking", "Consulting"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "The regional commodity market plunges 30% two months later. Your pre-set exposure caps protected the institution from catastrophic defaults, but the executive sponsor asks whether to buy distressed assets now.",
            "followUpQuestion": "How do you evaluate entering distressed assets in the aftermath?",
            "followUpOptions": [
                {"key": "A", "text": "Execute a disciplined valuation scan on high-quality collateralized tranches with a conservative margin of safety.", "score": 95, "trait": "calculated_contrarian"},
                {"key": "B", "text": "Panic and freeze all banking operations indefinitely.", "score": 35, "trait": "hyper_reactive"},
                {"key": "C", "text": "Buy everything blindly without analyzing underlying borrower liquidity.", "score": 30, "trait": "reckless_speculation"}
            ]
        }
    ))

    # Q43: Industry - Supply Chain / Crisis & Adaptability
    questions.append(make_q(
        43, 3, "Crisis",
        "A geopolitical disruption halts container shipments from your primary manufacturing supplier 3 weeks prior to the peak commercial holiday fulfillment window.",
        "What is your supply chain crisis mitigation strategy?",
        [
            ("A", "Issue a blanket press release stating that holiday orders cannot be fulfilled this year.", {"communication_iq": 35, "business_iq": 35, "problem_solving_iq": 35, "adaptability_iq": 40}, "high", "premature_capitulation"),
            ("B", "Activate pre-vetted secondary domestic suppliers for critical components, prioritize fulfillment for committed high-margin backorders, and secure expedited regional air-freight buffers.", {"adaptability_iq": 95, "problem_solving_iq": 95, "business_iq": 90, "leadership_iq": 90}, "low", "multi_tier_resilience"),
            ("C", "Sue the primary shipping line for breach of contract while doing nothing about manufacturing.", {"critical_thinking_iq": 40, "business_iq": 40, "time_priority_iq": 40, "adaptability_iq": 40}, "high", "misplaced_retribution"),
            ("D", "Continue taking customer pre-orders and debiting cards while knowing goods may never arrive.", {"ethics_judgment_iq": 20, "job_readiness_iq": 25, "business_iq": 30, "sales_iq": 25}, "high", "consumer_deception")
        ],
        {"adaptability_iq": 35, "problem_solving_iq": 35, "business_iq": 20, "leadership_iq": 10},
        50,
        "Supply chain resilience depends on pre-contracted redundancy and rapid prioritization of high-value inventory flows.",
        "In logistics disruptions, balance expedited transport costs against long-term brand equity and customer retention.",
        ["Logistics", "Manufacturing", "Retail", "Operations"]
    ))

    # Q44: Industry - Retail & Customer Experience / Marketing IQ
    questions.append(make_q(
        44, 3, "Customer",
        "Mystery shopper audits reveal that while physical retail foot traffic is steady, in-store conversion has dropped 22% because customers use their smartphones to compare prices and buy online while standing in the aisles.",
        "How do you evolve the omnichannel retail strategy?",
        [
            ("A", "Install cellular jammers inside stores to block customers from checking online prices.", {"ethics_judgment_iq": 20, "marketing_iq": 25, "business_iq": 25, "risk": "high"}, "high", "illegal_suppression"),
            ("B", "Embrace showrooming: introduce instant price-matching via mobile app, train store associates as consultative advisors, and offer seamless scan-and-deliver curbside options.", {"marketing_iq": 95, "business_iq": 95, "adaptability_iq": 90, "creativity_iq": 90}, "low", "omnichannel_integration"),
            ("C", "Ban customers from taking mobile phones out of their pockets inside stores.", {"sales_iq": 20, "marketing_iq": 25, "communication_iq": 30, "business_iq": 25}, "high", "hostile_policing"),
            ("D", "Close all physical stores immediately and convert into an online-only e-commerce shop.", {"business_iq": 50, "critical_thinking_iq": 50, "adaptability_iq": 55, "problem_solving_iq": 50}, "moderate", "hasty_retreat")
        ],
        {"marketing_iq": 40, "business_iq": 35, "adaptability_iq": 15, "creativity_iq": 10},
        45,
        "Modern commerce integrates physical tactile immediacy with digital price transparency rather than fighting inevitable consumer behaviors.",
        "Transform physical stores from mere distribution points into high-trust consultative experience hubs.",
        ["Retail", "Marketing", "Customer Service", "Business"]
    ))

    # Q45: Industry - IT & Architecture / Programming & Scalability
    questions.append(make_q(
        45, 3, "Programming",
        "Your system is experiencing unpredictable latency spikes during flash sales. The monolith database is hitting 98% CPU utilization due to unbounded search queries running on unindexed text columns.",
        "What is the architecturally sound remediation?",
        [
            ("A", "Purchase a 10x larger database server cluster regardless of cost.", {"programming_iq": 45, "business_iq": 45, "iq": 50, "problem_solving_iq": 50}, "moderate", "brute_hardware"),
            ("B", "Introduce a distributed read-replica caching layer (e.g. Redis), implement strict query pagination, and offload complex text searches to a dedicated indexing engine.", {"programming_iq": 98, "iq": 95, "problem_solving_iq": 95, "critical_thinking_iq": 90}, "low", "decoupled_search_architecture"),
            ("C", "Limit flash sales to 10 customers at a time.", {"business_iq": 35, "sales_iq": 35, "programming_iq": 45, "problem_solving_iq": 40}, "high", "commercial_throttle"),
            ("D", "Disable search functionality entirely during flash sale windows.", {"job_readiness_iq": 45, "programming_iq": 50, "problem_solving_iq": 40, "business_iq": 45}, "moderate", "degraded_utility")
        ],
        {"programming_iq": 45, "iq": 30, "problem_solving_iq": 15, "business_iq": 10},
        45,
        "System scalability requires decoupling read-heavy analytical search from transactional state stores via dedicated caching and indexing tiers.",
        "Protect core databases by bounding queries and offloading search indexing to distributed read infrastructure.",
        ["IT", "Engineering", "E-commerce"]
    ))

    # Q46: Industry - Education & Training / Learning Agility
    questions.append(make_q(
        46, 3, "Learning",
        "A corporate training curriculum shows high course completion rates (94%) but when audited 60 days post-training, employees demonstrate zero measurable change in job workflow behaviors.",
        "How do you redesign the learning architecture for lasting behavioral retention?",
        [
            ("A", "Make the final multiple-choice test twice as long and increase the passing mark to 100%.", {"learning_agility_iq": 40, "critical_thinking_iq": 40, "job_readiness_iq": 45, "iq": 45}, "moderate", "rote_intensification"),
            ("B", "Replace passive slide-deck training with scenario-based micro-simulations, on-the-job peer coaching, and 30-day practical project milestones with manager reinforcement.", {"learning_agility_iq": 98, "critical_thinking_iq": 95, "job_readiness_iq": 90, "leadership_iq": 90}, "low", "experiential_transfer_design"),
            ("C", "Mandate that employees re-watch the exact same video modules every 30 days.", {"learning_agility_iq": 35, "time_priority_iq": 35, "eq": 40, "business_iq": 40}, "moderate", "tedious_repetition"),
            ("D", "Cancel all professional development funding across the organization.", {"business_iq": 40, "leadership_iq": 35, "learning_agility_iq": 30, "promotion_readiness_iq": 35}, "high", "cynical_withdrawal")
        ],
        {"learning_agility_iq": 45, "critical_thinking_iq": 25, "job_readiness_iq": 20, "leadership_iq": 10},
        45,
        "True learning agility hinges on experiential simulation, immediate application in real environments, and institutional habit scaffolding.",
        "Move beyond passive attendance metrics; measure learning by sustained on-the-job behavioral changes.",
        ["Education", "HR", "Corporate", "Consulting"]
    ))

    # Q47: Industry - Consulting & Strategy / Problem Solving IQ
    questions.append(make_q(
        47, 3, "Workplace",
        "A corporate client hires your consulting team to evaluate whether to build a custom enterprise CRM or license an established SaaS solution. The internal IT team strongly favors building from scratch, but executive management needs launch within 4 months.",
        "How do you frame your strategic recommendation?",
        [
            ("A", "Recommend building from scratch to please the internal IT team, regardless of the 4-month timeline.", {"critical_thinking_iq": 40, "business_iq": 40, "time_priority_iq": 40, "leadership_iq": 45}, "high", "stakeholder_appeasement"),
            ("B", "Present a rigorous Total Cost of Ownership (TCO) and Time-to-Value model: recommend licensing the SaaS platform for the immediate 4-month launch, with custom API integrations for competitive differentiation.", {"critical_thinking_iq": 95, "business_iq": 95, "problem_solving_iq": 95, "communication_iq": 90}, "low", "objective_tco_framework"),
            ("C", "Tell executive management that their 4-month goal is delusional and advise them to postpone indefinitely.", {"communication_iq": 45, "eq": 40, "job_readiness_iq": 45, "leadership_iq": 45}, "moderate", "confrontational_bluntness"),
            ("D", "Flip a coin and write a 100-page justification after the choice is made.", {"ethics_judgment_iq": 25, "critical_thinking_iq": 25, "business_iq": 25, "job_readiness_iq": 30}, "high", "dishonest_rationalization")
        ],
        {"critical_thinking_iq": 35, "business_iq": 35, "problem_solving_iq": 20, "communication_iq": 10},
        45,
        "Strategic advisory balances executive urgency with architectural sustainability through objective Total Cost of Ownership and Time-to-Value trade-offs.",
        "Anchor build-versus-buy decisions in quantifiable time-to-market and lifetime maintenance overhead.",
        ["Consulting", "IT", "Management", "Finance"]
    ))

    # Q48: Industry - Media & Communications / Crisis & Public Relations
    questions.append(make_q(
        48, 3, "Communication",
        "A leaked internal email showing an executive joking inappropriately about a sensitive social topic is published by investigative journalists and begins trending nationally.",
        "What is the most effective corporate communications response?",
        [
            ("A", "Claim that the executive's email account was hacked and deny all involvement.", {"ethics_judgment_iq": 20, "communication_iq": 25, "critical_thinking_iq": 30, "risk": "high"}, "high", "transparent_falsehood"),
            ("B", "Issue a swift, unreserved acknowledgment of the authentic email, take public responsibility without corporate deflections, announce immediate executive accountability, and reiterate company core values.", {"communication_iq": 95, "ethics_judgment_iq": 95, "leadership_iq": 90, "eq": 90}, "low", "transparent_accountability"),
            ("C", "Threaten legal defamation actions against every journalist reporting on the leak.", {"communication_iq": 35, "business_iq": 35, "eq": 30, "risk": "high"}, "high", "streisand_combative"),
            ("D", "Stay completely silent for 14 days hoping the news cycle moves on to another story.", {"communication_iq": 45, "leadership_iq": 40, "eq": 45, "marketing_iq": 45}, "moderate", "vacuum_surrender")
        ],
        {"communication_iq": 40, "ethics_judgment_iq": 30, "leadership_iq": 20, "eq": 10},
        40,
        "Public trust in high-visibility crises is salvaged through prompt, unequivocal truth-telling and demonstrated consequence management.",
        "In reputational crises, speed of genuine accountability determines whether trust survives.",
        ["Media", "PR", "Corporate", "Legal"]
    ))

    # Q49: Industry - Human Resources & Culture / EQ & People
    questions.append(make_q(
        49, 3, "Workplace",
        "Following an acquisition, employees from the acquiring firm and the acquired startup form hostile silos, with rumors spreading that the startup staff will be phased out systematically.",
        "What cultural integration intervention creates genuine solidarity?",
        [
            ("A", "Issue a stern company-wide email forbidding anyone from discussing cultural differences.", {"eq": 35, "leadership_iq": 40, "communication_iq": 40, "teamwork_iq": 40}, "moderate", "authoritarian_gag"),
            ("B", "Design blended cross-functional project pods with shared business objectives, host joint listening town halls with transparent integration roadmaps, and align incentive structures.", {"eq": 95, "leadership_iq": 95, "teamwork_iq": 95, "communication_iq": 90}, "low", "systemic_integration"),
            ("C", "Immediately fire all middle managers from the startup to eliminate perceived resistance.", {"eq": 25, "leadership_iq": 30, "ethics_judgment_iq": 35, "teamwork_iq": 25}, "high", "cultural_purge"),
            ("D", "Do nothing because corporate cultures naturally merge smoothly over 3 to 5 years on their own.", {"leadership_iq": 45, "critical_thinking_iq": 45, "job_readiness_iq": 45, "eq": 45}, "moderate", "passive_decay")
        ],
        {"eq": 35, "leadership_iq": 35, "teamwork_iq": 20, "communication_iq": 10},
        45,
        "Merger integration succeeds through shared operational missions, transparent equity of opportunity, and deliberate cross-pollination of talent.",
        "Build solidarity through joint stakes; unaddressed integration anxiety erodes acquired talent rapidly.",
        ["HR", "Management", "Corporate", "Consulting"]
    ))

    # Q50: Industry - AI & Ethics / Algorithmic Fairness (with Micro-Scenario)
    questions.append(make_q(
        50, 3, "AI",
        "An automated resume screening model used by your recruiting firm shows a 35% lower recommendation rate for qualified female candidates in senior engineering roles due to historical hiring bias in training data.",
        "What governance action must be enforced immediately?",
        [
            ("A", "Continue using the model since artificial intelligence is mathematical and therefore immune to human bias.", {"aiq": 20, "ethics_judgment_iq": 20, "critical_thinking_iq": 25, "iq": 30}, "high", "algorithmic_blindness"),
            ("B", "Halt automated scoring for that cohort, audit training data weights and feature selection, implement bias mitigation algorithms, and mandate human review calibration.", {"aiq": 98, "ethics_judgment_iq": 98, "critical_thinking_iq": 95, "job_readiness_iq": 90}, "low", "ethical_algorithmic_governance"),
            ("C", "Manually add 50 bonus points to all female candidates without fixing the underlying model.", {"aiq": 45, "ethics_judgment_iq": 45, "critical_thinking_iq": 45, "problem_solving_iq": 45}, "moderate", "crude_patch"),
            ("D", "Delete all male resumes from the database until parity is achieved.", {"ethics_judgment_iq": 30, "critical_thinking_iq": 30, "job_readiness_iq": 35, "business_iq": 30}, "high", "arbitrary_distortion")
        ],
        {"aiq": 40, "ethics_judgment_iq": 40, "critical_thinking_iq": 15, "job_readiness_iq": 5},
        45,
        "AI governance requires vigilance against historical data bias; algorithmic accountability requires immediate remediation and structured auditing.",
        "Mathematical models replicate historical inequities unless actively audited and counterweighted with debiasing frameworks.",
        ["IT", "HR", "Legal", "AI"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "While the model is halted, the hiring division manager complains that recruitment velocity has slowed down and requests reopening the un-audited algorithm temporarily.",
            "followUpQuestion": "How do you respond to the business velocity demand?",
            "followUpOptions": [
                {"key": "A", "text": "Hold the line on compliance: explain the severe legal, regulatory, and ethical exposure of deploying biased tools, while setting up an expedited human screening pod to clear the backlog.", "score": 95, "trait": "principled_resilience"},
                {"key": "B", "text": "Cave in and quietly turn the biased algorithm back on.", "score": 25, "trait": "ethical_collapse"},
                {"key": "C", "text": "Quit the company in protest without offering any interim recruiting solutions.", "score": 40, "trait": "impulsive_resignation"}
            ]
        }
    ))

    # Q51: Industry - Legal & Regulatory Compliance / Ethics IQ
    questions.append(make_q(
        51, 3, "Ethical",
        "A client operates in a region with newly enacted consumer privacy regulations. They ask your software development agency to insert a tracking cookie without explicit user opt-in, claiming enforcement will take years.",
        "How do you steer the client toward compliance?",
        [
            ("A", "Follow the client's instructions because the paying customer is always right.", {"ethics_judgment_iq": 30, "critical_thinking_iq": 35, "business_iq": 35, "job_readiness_iq": 35}, "high", "subservient_violation"),
            ("B", "Refuse the non-compliant implementation, present the legal and financial exposure of non-compliance, and demonstrate how privacy-first consent banners enhance customer brand trust.", {"ethics_judgment_iq": 95, "communication_iq": 95, "business_iq": 90, "leadership_iq": 85}, "low", "value_grounded_compliance"),
            ("C", "Secretly implement the tracking cookie and bill the client double.", {"ethics_judgment_iq": 15, "job_readiness_iq": 20, "critical_thinking_iq": 25, "risk": "high"}, "high", "corrupt_collusion"),
            ("D", "Report the client to regulatory authorities anonymously within one hour without discussing it with them.", {"communication_iq": 45, "eq": 40, "business_iq": 45, "leadership_iq": 40}, "moderate", "premature_betrayal")
        ],
        {"ethics_judgment_iq": 45, "communication_iq": 25, "business_iq": 20, "leadership_iq": 10},
        45,
        "Professional partners act as trusted advisors: protect clients from self-inflicted regulatory liability by reframing compliance as a strategic trust advantage.",
        "Uphold regulatory integrity by demonstrating how privacy compliance shields long-term enterprise valuation.",
        ["Legal", "IT", "Consulting", "Finance"]
    ))

    # Q52: Industry - Manufacturing & Quality Control / Problem Solving
    questions.append(make_q(
        52, 3, "Workplace",
        "A production line batch of smart IoT devices exhibits a 1.8% component failure rate during 72-hour stress testing, just below the contract threshold of 2.0% allowable defects.",
        "What is the high-integrity quality decision before mass shipment?",
        [
            ("A", "Ship immediately since 1.8% is legally under the contract threshold of 2.0%.", {"critical_thinking_iq": 50, "business_iq": 55, "job_readiness_iq": 55, "ethics_judgment_iq": 55}, "moderate", "bare_minimum_compliance"),
            ("B", "Analyze the defect distribution: isolate the root component batch, verify whether failures accelerate exponentially after 100 hours in customer hands, and pause release if field failure risks are elevated.", {"problem_solving_iq": 95, "critical_thinking_iq": 95, "business_iq": 90, "ethics_judgment_iq": 90}, "low", "root_cause_durability"),
            ("C", "Ship the batch and disable logging on the devices so customers cannot prove the defect.", {"ethics_judgment_iq": 15, "business_iq": 20, "risk": "high", "job_readiness_iq": 20}, "high", "willful_negligence"),
            ("D", "Scrap all 50,000 devices instantly without investigating what caused the failures.", {"business_iq": 40, "problem_solving_iq": 45, "time_priority_iq": 45, "critical_thinking_iq": 45}, "high", "reckless_waste")
        ],
        {"critical_thinking_iq": 40, "problem_solving_iq": 30, "business_iq": 15, "ethics_judgment_iq": 15},
        45,
        "Excellence in manufacturing distinguishes legal minimums from real-world reliability; analyze failure curves to protect brand longevity.",
        "Investigate whether borderline metrics conceal catastrophic post-warranty failure curves.",
        ["Manufacturing", "Engineering", "Hardware", "Operations"]
    ))

    # Q53: Industry - Sales & Enterprise Negotiations / Sales IQ
    questions.append(make_q(
        53, 3, "Sales",
        "In a final contract review for a 7-figure enterprise deal, the client's procurement procurement director demands unlimited liability and 120-day payment terms before signing.",
        "What is your principled negotiation posture?",
        [
            ("A", "Sign immediately because losing a 7-figure deal will destroy your quarterly sales quota.", {"sales_iq": 40, "business_iq": 35, "critical_thinking_iq": 35, "risk": "high"}, "high", "existential_concession"),
            ("B", "Maintain clear risk boundaries: respectfully explain that unlimited liability threatens company solvency, offer capped liability at 2x annual contract value, and trade 60-day terms for a structured discount or tiered milestones.", {"sales_iq": 98, "business_iq": 98, "critical_thinking_iq": 90, "communication_iq": 90}, "low", "principled_value_trade"),
            ("C", "Walk away from the table in anger and accuse the procurement director of acting in bad faith.", {"sales_iq": 35, "eq": 30, "communication_iq": 35, "business_iq": 40}, "high", "emotional_rupture"),
            ("D", "Agree to unlimited liability verbally but write something different in the fine print.", {"ethics_judgment_iq": 15, "sales_iq": 20, "business_iq": 20, "risk": "high"}, "high", "fraudulent_misdirection")
        ],
        {"sales_iq": 40, "business_iq": 35, "communication_iq": 15, "critical_thinking_iq": 10},
        50,
        "Sophisticated negotiators never trade away catastrophic structural risks (unlimited liability) for top-line revenue; trade value across multiple variables.",
        "Anchor contract negotiations to balanced mutual risk parity; never let quota pressure compromise legal solvency.",
        ["Sales", "Legal", "Executive", "Finance"]
    ))

    # Q54: Industry - IT & Cybersecurity / Critical Thinking & Ethics
    questions.append(make_q(
        54, 3, "Ethical",
        "A routine security audit discovers that an employee in accounting clicked on a sophisticated phishing email 48 hours ago, and outbound beaconing has begun to an unknown external IP address.",
        "What is the immediate containment protocol?",
        [
            ("A", "Email the accounting employee asking if they remember downloading any strange files.", {"problem_solving_iq": 40, "critical_thinking_iq": 40, "job_readiness_iq": 40, "time_priority_iq": 40}, "moderate", "leisurely_inquiry"),
            ("B", "Isolate the compromised endpoint from the network instantly, revoke active session tokens, preserve forensic memory snapshots, block the external IP across firewalls, and invoke the incident response team.", {"problem_solving_iq": 98, "critical_thinking_iq": 95, "time_priority_iq": 95, "job_readiness_iq": 90}, "low", "rapid_containment"),
            ("C", "Wipe and reformat the computer immediately to destroy all traces of the virus before examining logs.", {"problem_solving_iq": 50, "critical_thinking_iq": 45, "job_readiness_iq": 50, "risk": "high"}, "high", "forensic_destruction"),
            ("D", "Ignore it until Monday morning so the employee's weekend is not disturbed.", {"job_readiness_iq": 25, "critical_thinking_iq": 25, "time_priority_iq": 20, "risk": "high"}, "high", "catastrophic_delay")
        ],
        {"problem_solving_iq": 40, "critical_thinking_iq": 30, "time_priority_iq": 20, "job_readiness_iq": 10},
        40,
        "Cybersecurity containment requires surgical isolation without destroying forensic evidence: sever network connectivity and revoke credential tokens immediately.",
        "Contain active intrusion instantly while preserving volatile memory artifacts for forensics.",
        ["Cybersecurity", "IT", "Finance", "Operations"]
    ))

    # Q55: Industry - Project Management / Time & Priority (with Micro-Scenario)
    questions.append(make_q(
        55, 3, "Time & Priority",
        "Three critical path dependencies across different engineering teams converge into your delivery milestone next week, but Team B reports they are blocked by an API specification change made by Team A.",
        "How do you unblock the critical path?",
        [
            ("A", "Tell Team B to figure it out with Team A on their own time.", {"leadership_iq": 40, "time_priority_iq": 45, "teamwork_iq": 45, "problem_solving_iq": 45}, "moderate", "abdication"),
            ("B", "Convene an immediate technical synchronizer session between Team A and B leads: freeze API contracts, establish a mock API interface for parallel development, and update critical path burndowns.", {"leadership_iq": 95, "time_priority_iq": 95, "problem_solving_iq": 95, "communication_iq": 90}, "low", "interface_decoupling"),
            ("C", "Postpone the entire multi-department product launch by six months.", {"business_iq": 45, "time_priority_iq": 45, "leadership_iq": 45, "adaptability_iq": 50}, "moderate", "excessive_slippage"),
            ("D", "Order Team A to revert all modernizations and restore deprecated legacy protocols.", {"problem_solving_iq": 55, "adaptability_iq": 50, "critical_thinking_iq": 50, "time_priority_iq": 60}, "moderate", "regressive_fix")
        ],
        {"time_priority_iq": 40, "problem_solving_iq": 30, "leadership_iq": 20, "communication_iq": 10},
        45,
        "Complex project bottlenecks are resolved through contract freezing and architectural mocking, allowing dependent teams to continue development in parallel.",
        "Unblock cross-team dependencies by decoupling work streams with standardized contract mocks.",
        ["IT", "Engineering", "Consulting", "Operations"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "Team A's lead attends the sync but claims they cannot freeze the contract because user research is changing daily.",
            "followUpQuestion": "How do you navigate continuous research flux during delivery sprints?",
            "followUpOptions": [
                {"key": "A", "text": "Version the API: freeze v1.0 for the impending launch, while queueing dynamic user research enhancements into a planned v1.1 sprint.", "score": 95, "trait": "architectural_statesmanship"},
                {"key": "B", "text": "Cancel all user research permanently.", "score": 35, "trait": "reactionary_blindness"},
                {"key": "C", "text": "Let Team B wait indefinitely until research stops changing.", "score": 40, "trait": "passive_paralysis"}
            ]
        }
    ))

    # Q56: Industry - Customer Service & Retention / EQ & Problem Solving
    questions.append(make_q(
        56, 3, "Customer",
        "A long-time flagship client threatens to cancel their $200,000 annual subscription because a software bug caused their billing report to display incorrect currency symbols on their board presentation.",
        "How do you salvage the relationship and prevent churn?",
        [
            ("A", "Send an automated link to the software terms of service showing that minor visual glitches are non-compensable.", {"sales_iq": 30, "communication_iq": 35, "eq": 30, "business_iq": 35}, "high", "legalistic_alienation"),
            ("B", "Have the VP or Account Director schedule an in-person meeting within 4 hours, present a formal root-cause correction, deploy a verified fix, and credit one month of service with dedicated concierge audit support.", {"sales_iq": 98, "eq": 95, "business_iq": 95, "leadership_iq": 90}, "low", "concierge_restoration"),
            ("C", "Offer to buy their board members a fruit basket.", {"sales_iq": 35, "eq": 35, "business_iq": 30, "job_readiness_iq": 40}, "high", "trivial_condescension"),
            ("D", "Tell the client they overreacted because currency symbols do not change numerical totals.", {"communication_iq": 25, "eq": 20, "sales_iq": 25, "business_iq": 20}, "high", "dismissive_arrogance")
        ],
        {"sales_iq": 40, "eq": 35, "business_iq": 15, "communication_iq": 10},
        45,
        "Enterprise retention under emotional escalation requires executive humility, transparent remediation, and tangible restitution proportional to customer embarrassment.",
        "Recognize that enterprise churn is often triggered by customer loss of face in front of their stakeholders; restore their confidence first.",
        ["Sales", "Customer Service", "Corporate", "Consulting"]
    ))

    # Q57: Industry - Entrepreneurship & Resource Allocation / Business IQ
    questions.append(make_q(
        57, 3, "Business",
        "An early-stage startup has 5 months of cash runway left. Customer acquisition cost (CAC) is $450 while customer lifetime value (LTV) is currently $320.",
        "What strategic intervention must the leadership execute to avoid bankruptcy?",
        [
            ("A", "Spend remaining reserves on expensive Super Bowl or billboard advertising to scale faster.", {"business_iq": 20, "critical_thinking_iq": 25, "iq": 30, "risk": "high"}, "high", "accelerated_insolvency"),
            ("B", "Immediately pause paid acquisition channels with negative unit economics, analyze retention levers to expand LTV, focus on high-intent referral channels, and extend runway by trimming non-essential expenditures.", {"business_iq": 98, "critical_thinking_iq": 95, "problem_solving_iq": 90, "leadership_iq": 90}, "low", "unit_economic_turnaround"),
            ("C", "Hide the runway numbers from current investors and ask for more money without explaining unit metrics.", {"ethics_judgment_iq": 20, "business_iq": 25, "job_readiness_iq": 25, "risk": "high"}, "high", "deceptive_fundraising"),
            ("D", "Assume unit economics automatically fix themselves when user volume hits 1,000,000.", {"business_iq": 30, "critical_thinking_iq": 35, "iq": 35, "problem_solving_iq": 30}, "high", "delusional_scale")
        ],
        {"business_iq": 45, "critical_thinking_iq": 30, "problem_solving_iq": 15, "leadership_iq": 10},
        50,
        "Startups survive by mastering unit economics: you cannot scale negative gross margins into profitability without fixing the fundamental LTV/CAC ratio.",
        "Fix unit economics before pouring capital into customer acquisition; scale magnifies flaws, it doesn't cure them.",
        ["Startups", "Finance", "Business", "Management"]
    ))

    # Q58: Industry - Marketing & Analytics / Critical Thinking
    questions.append(make_q(
        58, 3, "Marketing",
        "An automated attribution platform credits 80% of all inbound e-commerce revenue to branded search ads, prompting marketing to shift 70% of the entire budget into bidding on their own company brand name.",
        "What critical marketing fallacy does this reflect?",
        [
            ("A", "It is entirely correct because bidding on your own name is the only way to get sales.", {"marketing_iq": 35, "critical_thinking_iq": 35, "business_iq": 40, "iq": 40}, "moderate", "attribution_naivety"),
            ("B", "It represents last-touch attribution cannibalization: users searching for the exact brand name were already intending to buy organically, resulting in paying for organic traffic without incremental lift.", {"marketing_iq": 98, "critical_thinking_iq": 95, "business_iq": 90, "iq": 90}, "low", "incrementality_analysis"),
            ("C", "It proves search ads should be completely eliminated across all channels.", {"marketing_iq": 45, "critical_thinking_iq": 50, "problem_solving_iq": 45, "business_iq": 45}, "moderate", "reactionary_elimination"),
            ("D", "It indicates that customers dislike social media and email marketing.", {"marketing_iq": 40, "critical_thinking_iq": 40, "iq": 45, "problem_solving_iq": 40}, "moderate", "non_sequitur")
        ],
        {"marketing_iq": 45, "critical_thinking_iq": 30, "business_iq": 15, "iq": 10},
        45,
        "Sophisticated growth marketing isolates incremental lift from baseline organic navigation; last-touch attribution often steals credit from brand equity.",
        "Measure incrementality through geo-holdout tests rather than crediting search ads with pre-existing intent.",
        ["Marketing", "E-commerce", "Analytics", "Startups"]
    ))

    # Q59: Industry - Communication & Negotiation / Communication IQ
    questions.append(make_q(
        59, 3, "Communication",
        "During an intense cross-border joint venture negotiation, your counterpart becomes visibly silent, takes prolonged pauses, and gives non-committal answers regarding timeline agreements.",
        "How do you interpret and navigate this diplomatic signal?",
        [
            ("A", "Fill the silence immediately by talking continuously and offering concessions to force an answer.", {"communication_iq": 40, "eq": 40, "sales_iq": 40, "job_readiness_iq": 45}, "high", "concession_panic"),
            ("B", "Respect the cultural cadence of silence: pause comfortably, reflectively summarize shared goals, and ask open-ended questions about their internal review milestones and consensus processes.", {"communication_iq": 95, "eq": 95, "sales_iq": 90, "adaptability_iq": 90}, "low", "cultural_cadence_mirroring"),
            ("C", "Pound on the table and demand an immediate yes-or-no commitment.", {"communication_iq": 30, "eq": 25, "leadership_iq": 30, "sales_iq": 30}, "high", "diplomatic_sabotage"),
            ("D", "End the negotiation abruptly and walk out of the room.", {"communication_iq": 35, "eq": 30, "adaptability_iq": 35, "sales_iq": 35}, "high", "immature_storming")
        ],
        {"communication_iq": 40, "eq": 35, "adaptability_iq": 15, "sales_iq": 10},
        45,
        "Cross-cultural and high-stakes negotiation requires comfort with silence: pauses often indicate thoughtful internal consultation rather than hostility.",
        "Hold space for conversational pauses; never negotiate against yourself to fill awkward silence.",
        ["Consulting", "Corporate", "Sales", "International"]
    ))

    # Q60: Industry - Promotion Readiness & Systemic Thinking
    questions.append(make_q(
        60, 3, "Promotion",
        "You notice that your department's monthly reporting cycle consumes 40 hours of manual data collation across 6 analysts, yet executive leadership only reviews two headline summary charts.",
        "What initiative demonstrates senior promotional leadership?",
        [
            ("A", "Continue the 40 hours of manual work because 'that is how it has always been done.'", {"promotion_readiness_iq": 35, "leadership_iq": 35, "problem_solving_iq": 40, "time_priority_iq": 35}, "moderate", "bureaucratic_inertia"),
            ("B", "Author an automated live dashboard that aggregates the headline metrics in real-time, eliminating 80% of manual effort and liberating 32 analyst hours/week for strategic insight generation.", {"promotion_readiness_iq": 98, "leadership_iq": 95, "problem_solving_iq": 95, "business_iq": 90}, "low", "systemic_efficiency_leadership"),
            ("C", "Complain to the other analysts that the executives don't appreciate hard work.", {"eq": 35, "communication_iq": 35, "leadership_iq": 30, "promotion_readiness_iq": 30}, "high", "cynical_griping"),
            ("D", "Stop submitting the reports entirely without notifying anyone.", {"job_readiness_iq": 25, "ethics_judgment_iq": 30, "communication_iq": 25, "risk": "high"}, "high", "insubordination")
        ],
        {"promotion_readiness_iq": 40, "leadership_iq": 30, "problem_solving_iq": 20, "business_iq": 10},
        45,
        "Senior candidates stand out by identifying institutional waste and designing automated self-serve systems that free organizational cognitive capacity.",
        "Transform routine reporting toil into automated visibility, freeing human capital for exploratory analytics.",
        ["Corporate", "Finance", "IT", "Operations"]
    ))

    # =========================================================================
    # LEVEL 4: ADVANCED (Q61 - Q70 of 80)
    # =========================================================================

    # Q61: Advanced - Leadership / Managing Toxic High Performers
    questions.append(make_q(
        61, 4, "Leadership",
        "The highest revenue-generating salesperson in the company consistently insults junior staff members, refuses to log customer notes in CRM, and threatens to resign whenever reprimanded.",
        "What is your executive leadership decision?",
        [
            ("A", "Grant them complete immunity and tell junior staff to develop thicker skin because revenue is sacred.", {"leadership_iq": 30, "eq": 30, "ethics_judgment_iq": 35, "teamwork_iq": 30}, "high", "toxic_capitulation"),
            ("B", "Set an unequivocal behavioral boundary in a private executive meeting: convey that sustainable performance requires cultural integrity, establish non-negotiable team standards, and prepare an account succession plan if they refuse.", {"leadership_iq": 98, "ethics_judgment_iq": 95, "eq": 90, "business_iq": 90}, "low", "principled_cultural_governance"),
            ("C", "Slash their commission by 50% without warning in their next paycheck.", {"leadership_iq": 45, "communication_iq": 40, "legal_iq": 35, "eq": 40}, "high", "arbitrary_retaliation"),
            ("D", "Gossip about their behavior with other managers hoping peer pressure solves it.", {"leadership_iq": 30, "communication_iq": 35, "eq": 35, "job_readiness_iq": 35}, "high", "passive_corrosion")
        ],
        {"leadership_iq": 40, "ethics_judgment_iq": 30, "eq": 20, "business_iq": 10},
        50,
        "A culture is defined by the worst behavior leadership tolerates; allowing brilliant jerks destroys systemic retention and team morale.",
        "Never hold culture hostage to individual output; establish explicit behavioral contracts with clear separation triggers.",
        ["Sales", "Corporate", "Management", "Consulting"]
    ))

    # Q62: Advanced - Business / Capital Allocation & Strategic Pivot
    questions.append(make_q(
        62, 4, "Business",
        "Your enterprise's legacy flagship product accounts for 75% of current profit but has entered a 6% annual decline, while a nascent AI-powered service is growing 150% annually but operates at a slight loss.",
        "How do you strategically allocate R&D and marketing capital?",
        [
            ("A", "Pour 100% of capital into defending the legacy product to preserve the 75% profit margin at all costs.", {"business_iq": 40, "critical_thinking_iq": 40, "adaptability_iq": 35, "innovative_iq": 35}, "high", "innovators_dilemma_trap"),
            ("B", "Execute an 'Innovator's Dilemma' transition strategy: manage the legacy product for efficient cash-flow harvesting, while systematically reallocating capital to scale the AI service toward profitability and market dominance.", {"business_iq": 98, "critical_thinking_iq": 95, "adaptability_iq": 95, "leadership_iq": 90}, "low", "strategic_portfolio_transition"),
            ("C", "Immediately shut down the legacy product tomorrow and fire the staff who maintain it.", {"business_iq": 35, "time_priority_iq": 30, "leadership_iq": 35, "risk": "high"}, "high", "revenue_suicide"),
            ("D", "Sell the entire company for scrap before anyone notices the 6% decline.", {"business_iq": 25, "critical_thinking_iq": 25, "leadership_iq": 20, "risk": "high"}, "high", "defeatist_fire_sale")
        ],
        {"business_iq": 40, "critical_thinking_iq": 30, "adaptability_iq": 20, "leadership_iq": 10},
        50,
        "Navigating the Innovator's Dilemma demands funding future growth curves using cash harvested from disciplined, efficient legacy operations.",
        "Balance cash generation with future transformation; harvest mature lines to fuel hyper-growth assets.",
        ["Corporate", "Finance", "Strategy", "Tech"]
    ))

    # Q63: Advanced - Critical Thinking / Algorithmic Misalignment
    questions.append(make_q(
        63, 4, "Critical Thinking",
        "An algorithmic stock trading or inventory replenishment model generates record profits for three quarters, but your mathematical inspection indicates it is exploiting a subtle regulatory loophole that could be closed by regulators next month.",
        "What is your fiduciary and ethical recommendation?",
        [
            ("A", "Conceal the vulnerability and continue trading at maximum volume until regulators discover it.", {"ethics_judgment_iq": 20, "critical_thinking_iq": 30, "risk": "high", "business_iq": 30}, "high", "willful_regulatory_risk"),
            ("B", "Brief executive leadership on the regulatory fragility: quantify the downside regulatory penalties, design an organic replacement model compliant with the anticipated rule change, and unwind dependent exposures gracefully.", {"critical_thinking_iq": 98, "ethics_judgment_iq": 98, "business_iq": 95, "problem_solving_iq": 90}, "low", "proactive_regulatory_hedging"),
            ("C", "Whistleblow to the press anonymously without letting internal leadership review the data first.", {"communication_iq": 45, "eq": 40, "leadership_iq": 45, "business_iq": 40}, "moderate", "premature_leak"),
            ("D", "Delete the trading model code so no one can prove profits came from the loophole.", {"ethics_judgment_iq": 15, "job_readiness_iq": 20, "critical_thinking_iq": 25, "risk": "high"}, "high", "evidence_destruction")
        ],
        {"critical_thinking_iq": 40, "ethics_judgment_iq": 35, "business_iq": 15, "problem_solving_iq": 10},
        50,
        "Regulatory arbitrage provides ephemeral profit coupled with catastrophic downside; robust leadership pivots toward durable, defensible competitive value.",
        "Never mistake regulatory latency for sustainable alpha; prepare for inevitable regulatory convergence.",
        ["Finance", "Legal", "Banking", "Consulting"]
    ))

    # Q64: Advanced - Adaptability / Organizational Restructuring
    questions.append(make_q(
        64, 4, "Adaptability",
        "Following a corporate merger, your entire department is being shifted from an agile, decentralized product pod model into a matrixed, centralized functional hierarchy.",
        "How do you steer your teams through this structural upheaval?",
        [
            ("A", "Organize covert resistance meetings to sabotage the incoming matrix hierarchy.", {"adaptability_iq": 30, "leadership_iq": 35, "eq": 35, "teamwork_iq": 35}, "high", "organizational_sabotage"),
            ("B", "Map out the new governance workflows, identify potential communication latency in the matrix, establish informal cross-functional bridge channels, and coach teams on influencing across matrix lines.", {"adaptability_iq": 98, "leadership_iq": 95, "communication_iq": 95, "eq": 90}, "low", "matrix_empowerment"),
            ("C", "Resign immediately on the first day the announcement is made.", {"adaptability_iq": 40, "job_readiness_iq": 40, "problem_solving_iq": 40, "leadership_iq": 40}, "moderate", "avoidant_exit"),
            ("D", "Pretend nothing has changed and continue operating rogue pods.", {"adaptability_iq": 35, "leadership_iq": 40, "business_iq": 35, "risk": "high"}, "high", "structural_denial")
        ],
        {"adaptability_iq": 40, "leadership_iq": 30, "communication_iq": 20, "eq": 10},
        50,
        "Thriving in structural reorganizations requires cognitive agility: mastering matrix influence, lateral communication, and stakeholder orchestration.",
        "In matrix transformations, trade direct hierarchical command for lateral relational influence.",
        ["Corporate", "Management", "HR", "Consulting"]
    ))

    # Q65: Advanced - AI / Autonomous Agents & Safety (with Micro-Scenario)
    questions.append(make_q(
        65, 4, "AI",
        "Your enterprise plans to deploy autonomous AI agents capable of initiating vendor purchase orders up to $10,000 without human sign-off to accelerate supply replenishment.",
        "What governance architecture protects against rogue loops and cascading budget depletion?",
        [
            ("A", "Deploy the agents with zero restrictions because AI models are smarter than human buyers.", {"aiq": 20, "critical_thinking_iq": 25, "business_iq": 25, "risk": "high"}, "high", "reckless_delegation"),
            ("B", "Implement tiered guardrails: daily aggregate spending ceilings, deterministic vendor verification checks, anomaly detection triggers on buying velocity, and mandatory human sign-off on non-standard SKU patterns.", {"aiq": 98, "critical_thinking_iq": 98, "business_iq": 95, "problem_solving_iq": 95}, "low", "defense_in_depth_governance"),
            ("C", "Restrict agent autonomy to $5 total purchases, making the tool useless for actual business operations.", {"aiq": 45, "business_iq": 45, "problem_solving_iq": 50, "adaptability_iq": 45}, "moderate", "crippling_caution"),
            ("D", "Require the CEO to manually approve every single 50-cent order created by the agent.", {"business_iq": 40, "time_priority_iq": 35, "leadership_iq": 40, "aiq": 45}, "moderate", "executive_bottleneck")
        ],
        {"aiq": 40, "critical_thinking_iq": 30, "business_iq": 20, "problem_solving_iq": 10},
        50,
        "Agentic autonomy demands defense-in-depth: rate limits, semantic guardrails, anomaly circuit breakers, and bounded blast radiuses.",
        "Govern autonomous AI through automated rate-limiting thresholds and semantic circuit breakers before giving financial keys.",
        ["IT", "Supply Chain", "Finance", "AI"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "During black swan market volatility, a supplier changes SKU syntax, triggering the anomaly circuit breaker and halting 12 critical orders.",
            "followUpQuestion": "How do you handle this operational halt?",
            "followUpOptions": [
                {"key": "A", "text": "Approve the 12 orders manually via emergency human triage while tuning the agent's schema-drift tolerance for dynamic vendor naming.", "score": 95, "trait": "adaptive_incident_triage"},
                {"key": "B", "text": "Permanently dismantle the anomaly detection system.", "score": 25, "trait": "guardrail_destruction"},
                {"key": "C", "text": "Cancel all 12 orders and sever relationships with the supplier.", "score": 35, "trait": "disproportionate_severance"}
            ]
        }
    ))

    # Q66: Advanced - Promotion Readiness / Executive Presence & Board Strategy
    questions.append(make_q(
        66, 4, "Promotion",
        "You are invited to present your department's multi-year vision to the Board of Directors. The previous presenter went 25 minutes overtime, leaving you with only 8 minutes before the board adjourns.",
        "How do you master this compressed high-stakes executive interaction?",
        [
            ("A", "Try to rush through all 45 slides at triple speed while speaking breathlessly.", {"communication_iq": 35, "promotion_readiness_iq": 35, "eq": 35, "time_priority_iq": 35}, "high", "slide_rushing"),
            ("B", "Acknowledge the compressed timeframe with calm confidence, skip to the single core strategic unlock slide, state the decisive capital and growth thesis in 3 minutes, and open the remaining 5 minutes for board questions.", {"promotion_readiness_iq": 98, "communication_iq": 98, "leadership_iq": 95, "eq": 95}, "low", "executive_presence_synthesis"),
            ("C", "Refuse to speak and demand the board reschedule a special 2-hour session just for you.", {"communication_iq": 30, "eq": 25, "promotion_readiness_iq": 30, "leadership_iq": 35}, "high", "prima_donna_obstruction"),
            ("D", "Read the printed executive summary word for word with your eyes glued to the paper.", {"communication_iq": 45, "eq": 45, "promotion_readiness_iq": 45, "leadership_iq": 45}, "moderate", "unengaging_recital")
        ],
        {"promotion_readiness_iq": 40, "communication_iq": 30, "leadership_iq": 20, "eq": 10},
        45,
        "Executive presence shines brightest in compression: distilling hours of strategic complexity into clear, calm, high-conviction decision frameworks under time pressure.",
        "Demonstrate command by collapsing 45 slides into one definitive thesis and engaging board members in peer dialogue.",
        ["Corporate", "Executive", "Strategy", "Management"]
    ))

    # Q67: Advanced - Ethics / Whistleblowing & Corporate Governance
    questions.append(make_q(
        67, 4, "Ethical",
        "During an internal review, you uncover clear evidence that a division vice president has been falsifying safety inspection timestamps on industrial machinery to meet quarterly production bonuses.",
        "What is the responsible and legally sound escalation pathway?",
        [
            ("A", "Approach the VP privately and ask for a share of their bonus in exchange for remaining silent.", {"ethics_judgment_iq": 10, "job_readiness_iq": 15, "risk": "high", "leadership_iq": 15}, "high", "criminal_blackmail"),
            ("B", "Document the forensic timestamp discrepancies with immutable logs, report directly via established corporate whistleblower/ombudsman channels and internal audit, and notify legal counsel to safeguard worker safety.", {"ethics_judgment_iq": 98, "critical_thinking_iq": 95, "leadership_iq": 90, "job_readiness_iq": 90}, "low", "forensic_whistleblowing"),
            ("C", "Post unverified allegations on public Reddit forums.", {"ethics_judgment_iq": 40, "communication_iq": 35, "job_readiness_iq": 40, "risk": "high"}, "high", "reckless_exposure"),
            ("D", "Ignore it because industrial safety is outside your direct job description.", {"ethics_judgment_iq": 30, "job_readiness_iq": 35, "critical_thinking_iq": 35, "leadership_iq": 30}, "high", "moral_abdication")
        ],
        {"ethics_judgment_iq": 50, "critical_thinking_iq": 25, "leadership_iq": 15, "job_readiness_iq": 10},
        50,
        "Safety and compliance fraud demands forensic documentation and unyielding escalation through official ombudsman and legal avenues to preserve human life and corporate governance.",
        "When physical safety is compromised, bypass informal channels and file formal forensic reports with audit committees.",
        ["Manufacturing", "Corporate", "Legal", "Operations"]
    ))

    # Q68: Advanced - Marketing & Brand / Crisis Management
    questions.append(make_q(
        68, 4, "Marketing",
        "An automated advertising algorithm inadvertently places your family-friendly consumer brand's banner ads adjacent to extremist propaganda videos on a video sharing platform, sparking an advertiser boycott movement.",
        "What decisive brand stewardship action do you execute?",
        [
            ("A", "Blame the video platform entirely in aggressive press releases while keeping the ads running.", {"marketing_iq": 40, "communication_iq": 40, "business_iq": 40, "eq": 45}, "high", "defensive_blame"),
            ("B", "Immediately pause programmatic ad spend across the platform, initiate a full audit of brand safety exclusions and negative keyword lists, publish a transparent action plan, and condition ad resumption on third-party verification.", {"marketing_iq": 98, "leadership_iq": 95, "critical_thinking_iq": 90, "business_iq": 90}, "low", "brand_safety_audit"),
            ("C", "Change your brand logo color and hope nobody notices the ads.", {"marketing_iq": 30, "critical_thinking_iq": 30, "problem_solving_iq": 30, "leadership_iq": 30}, "high", "cosmetic_evasion"),
            ("D", "Retire all marketing forever and rely purely on word of mouth.", {"marketing_iq": 35, "business_iq": 35, "adaptability_iq": 35, "problem_solving_iq": 35}, "moderate", "drastic_overkill")
        ],
        {"marketing_iq": 45, "leadership_iq": 25, "business_iq": 20, "critical_thinking_iq": 10},
        45,
        "Brand safety crises require immediate supply-side circuit breaking coupled with transparent inclusion protocols and third-party verification standards.",
        "Pause programmatic ad spend immediately; re-enter only when rigorous negative exclusions and verification seals are established.",
        ["Marketing", "Media", "Corporate", "PR"]
    ))

    # Q69: Advanced - Problem Solving / Complex Trade-offs
    questions.append(make_q(
        69, 4, "Problem Solving",
        "Your company must migrate 50 million user records to a modern cloud database. A zero-downtime migration will take 6 months and cost $1.2M; a 4-hour scheduled maintenance window will take 3 weeks and cost $80,000.",
        "How do you evaluate this multi-dimensional trade-off?",
        [
            ("A", "Default automatically to zero-downtime because downtime is always unacceptable under any circumstances.", {"problem_solving_iq": 50, "business_iq": 45, "critical_thinking_iq": 50, "time_priority_iq": 45}, "moderate", "dogmatic_architecture"),
            ("B", "Conduct a business impact analysis: quantify customer revenue loss and SLA penalties during a 4-hour weekend window (e.g. $15,000) versus the $1.12M premium and 5-month delay, and present the high-ROI scheduled window with customer notice.", {"problem_solving_iq": 98, "business_iq": 98, "critical_thinking_iq": 95, "time_priority_iq": 90}, "low", "cost_benefit_tradeoff"),
            ("C", "Cancel the database migration and leave data on servers that are currently out of warranty.", {"problem_solving_iq": 35, "business_iq": 35, "risk": "high", "critical_thinking_iq": 35}, "high", "paralyzed_deferral"),
            ("D", "Execute the migration during peak Monday morning business hours without telling customers.", {"problem_solving_iq": 20, "business_iq": 20, "ethics_judgment_iq": 20, "risk": "high"}, "high", "reckless_disruption")
        ],
        {"problem_solving_iq": 40, "business_iq": 35, "critical_thinking_iq": 15, "time_priority_iq": 10},
        50,
        "Engineering pragmatism evaluates real dollar impact: spending $1.12M to avoid $15,000 in scheduled weekend inconvenience is an irresponsible allocation of company capital.",
        "Quantify the real cost of downtime versus the cost of zero-downtime architecture; choose pragmatic economic trade-offs.",
        ["IT", "Finance", "Operations", "Consulting"]
    ))

    # Q70: Advanced - Teamwork / Cross-Functional Matrix Leadership (with Micro-Scenario)
    questions.append(make_q(
        70, 4, "Teamwork",
        "You are tasked with leading an enterprise digital transformation initiative involving Product, Sales, Compliance, and Engineering, none of whom report to you hierarchically.",
        "How do you establish cohesive momentum without direct formal authority?",
        [
            ("A", "Order everyone to follow your commands and claim you speak directly on behalf of the CEO.", {"leadership_iq": 35, "communication_iq": 35, "eq": 30, "teamwork_iq": 35}, "high", "false_authority"),
            ("B", "Build relational trust: interview each departmental stakeholder to uncover their specific incentives and pain points, co-author a shared charter where everyone's wins are aligned, and institute transparent cross-functional steering cadence.", {"leadership_iq": 98, "teamwork_iq": 98, "communication_iq": 95, "eq": 95}, "low", "coalition_building"),
            ("C", "Do all the work yourself in isolation so you don't have to deal with other departments.", {"teamwork_iq": 40, "leadership_iq": 35, "time_priority_iq": 40, "problem_solving_iq": 45}, "moderate", "martyr_isolation"),
            ("D", "Send daily escalation emails to senior leadership complaining that peers are unresponsive.", {"teamwork_iq": 35, "communication_iq": 35, "eq": 30, "leadership_iq": 30}, "high", "chronic_escalation")
        ],
        {"leadership_iq": 35, "teamwork_iq": 35, "communication_iq": 20, "eq": 10},
        50,
        "Influence without authority is the defining benchmark of senior leadership: aligning mutual incentives, establishing shared vision, and leading through coalition building.",
        "Win horizontal alignment by mapping how your project solves the personal metrics of each functional leader.",
        ["Corporate", "Management", "Consulting", "All"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "Compliance stalls your shared charter for three weeks citing regulatory concerns that were already addressed in writing.",
            "followUpQuestion": "How do you navigate Compliance's persistent hesitation?",
            "followUpOptions": [
                {"key": "A", "text": "Schedule a dedicated working session with Compliance counsel to walk through regulatory cross-walks clause-by-clause, co-drafting the protective clauses together.", "score": 95, "trait": "collaborative_consensus_builder"},
                {"key": "B", "text": "Bypass Compliance completely and launch without their sign-off.", "score": 25, "trait": "rogue_rebellion"},
                {"key": "C", "text": "Send a passive-aggressive email copying everyone's superiors.", "score": 35, "trait": "antagonistic_provocation"}
            ]
        }
    ))

    return questions

if __name__ == "__main__":
    qs = get_level3_and_part4()
    print(f"Loaded {len(qs)} questions for Level 3 and part of Level 4")
