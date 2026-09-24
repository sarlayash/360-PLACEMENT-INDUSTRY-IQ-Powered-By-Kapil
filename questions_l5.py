# Questions Level 4 (Q71-Q80) and Level 5: Executive (Q81-Q100)
from generate_base import make_q

def get_level4_part2_and_level5():
    questions = []

    # Q71: Advanced - Crisis / Ransomware & Threat Response
    questions.append(make_q(
        71, 4, "Crisis",
        "Your enterprise data center is hit by ransomware encrypting sensitive customer data, and the threat actor demands $5M in cryptocurrency within 24 hours while threatening public data release.",
        "What is your multi-dimensional executive response protocol?",
        [
            ("A", "Pay the $5M immediately from company funds and keep the incident secret from regulators.", {"ethics_judgment_iq": 20, "critical_thinking_iq": 25, "business_iq": 25, "risk": "high"}, "high", "unverified_ransom_payment"),
            ("B", "Activate the cyber incident crisis committee: isolate systems, notify legal counsel, data protection authorities, and federal law enforcement, assess verified offline cold backups, and engage specialized forensic incident responders.", {"problem_solving_iq": 98, "ethics_judgment_iq": 98, "leadership_iq": 95, "critical_thinking_iq": 95}, "low", "rigorous_cyber_protocol"),
            ("C", "Issue a press release claiming that nothing happened and that all servers are operating normally.", {"communication_iq": 20, "ethics_judgment_iq": 20, "leadership_iq": 20, "risk": "high"}, "high", "public_deception"),
            ("D", "Unplug every computer in the world connected to the company network and fire the CISO.", {"leadership_iq": 35, "problem_solving_iq": 30, "eq": 30, "risk": "high"}, "high", "chaotic_panic")
        ],
        {"problem_solving_iq": 35, "ethics_judgment_iq": 35, "leadership_iq": 20, "critical_thinking_iq": 10},
        50,
        "Ransomware crises demand adherence to legal, regulatory, and forensic protocols; never pay ransoms blindly or conceal breaches from statutory regulators.",
        "Engage law enforcement and forensic negotiators while validating cold backups; prioritize statutory disclosure.",
        ["Cybersecurity", "Corporate", "Legal", "Executive"]
    ))

    # Q72: Advanced - Sales / Strategic Account Recovery
    questions.append(make_q(
        72, 4, "Sales",
        "Your company's largest account ($3.5M ARR) has issued an RFP (Request for Proposal) to market competitors after an internal executive sponsor champion leaves their firm.",
        "How do you execute a strategic account defense?",
        [
            ("A", "Offer an immediate 50% discount to stop them from evaluating competitors.", {"sales_iq": 45, "business_iq": 40, "critical_thinking_iq": 45, "problem_solving_iq": 45}, "high", "panic_discounting"),
            ("B", "Map the new stakeholder ecosystem immediately: uncover the incoming executive's strategic priorities, quantify the multi-million dollar ROI delivered over the past 3 years, and deliver a co-innovation roadmap aligned with their future charter.", {"sales_iq": 98, "business_iq": 95, "leadership_iq": 95, "communication_iq": 90}, "low", "value_realignment_defense"),
            ("C", "Complain to their procurement department that conducting an RFP is unfair after years of loyalty.", {"sales_iq": 35, "communication_iq": 35, "eq": 30, "job_readiness_iq": 35}, "high", "entitled_complaint"),
            ("D", "Refuse to participate in the RFP on the grounds that your product is superior.", {"sales_iq": 30, "business_iq": 30, "leadership_iq": 35, "risk": "high"}, "high", "arrogant_forfeiture")
        ],
        {"sales_iq": 40, "business_iq": 30, "leadership_iq": 20, "communication_iq": 10},
        50,
        "Account retention during sponsor turnover requires re-qualifying the account from scratch: anchor the value narrative to the new leadership's specific agenda.",
        "Re-underwrite the account relationship with fresh strategic discovery; never rely on past laurels when leadership changes.",
        ["Sales", "Consulting", "Enterprise", "Corporate"]
    ))

    # Q73: Advanced - Learning Agility / Rapid Vertical Pivot
    questions.append(make_q(
        73, 4, "Learning",
        "Your software agency has focused on hospitality tech for 8 years, but a sudden market shift creates a massive urgent demand in healthcare life sciences compliance.",
        "How do you orchestrate rapid capability acquisition?",
        [
            ("A", "Bid on multi-million dollar clinical trials projects today and fake your credentials.", {"ethics_judgment_iq": 15, "job_readiness_iq": 20, "risk": "high", "learning_agility_iq": 25}, "high", "reckless_fraud"),
            ("B", "Recruit key clinical domain advisors, conduct an intensive 30-day compliance gap audit (HIPAA/GxP), partner with specialized auditors, and transition senior architects through intensive regulatory immersion.", {"learning_agility_iq": 98, "adaptability_iq": 95, "business_iq": 95, "problem_solving_iq": 90}, "low", "structured_capability_pivot"),
            ("C", "Reject all healthcare opportunities because changing domains is too risky.", {"adaptability_iq": 40, "business_iq": 40, "learning_agility_iq": 40, "leadership_iq": 40}, "moderate", "stagnation"),
            ("D", "Ask developers to skim Wikipedia articles on healthcare for 2 hours and call them certified experts.", {"learning_agility_iq": 30, "critical_thinking_iq": 30, "ethics_judgment_iq": 30, "job_readiness_iq": 35}, "high", "superficial_facade")
        ],
        {"learning_agility_iq": 40, "adaptability_iq": 30, "business_iq": 20, "leadership_iq": 10},
        45,
        "Entering complex regulated verticals requires humility and institutional acceleration: pair seasoned internal problem solvers with authoritative domain compliance advisors.",
        "Bridge domain chasms through targeted expert recruitment and rigorous compliance scaffolding.",
        ["Healthcare", "Consulting", "Strategy", "Tech"]
    ))

    # Q74: Advanced - Time & Priority / Capacity Allocation
    questions.append(make_q(
        74, 4, "Time & Priority",
        "Executive leadership hands down 4 strategic priority initiatives for the year, but engineering capacity models prove the organization can only execute 2 with high quality without risking burnout and system degradation.",
        "How do you manage this executive prioritization challenge?",
        [
            ("A", "Accept all 4 initiatives silently and force teams to work 70-hour weeks all year.", {"leadership_iq": 35, "time_priority_iq": 30, "eq": 30, "teamwork_iq": 30}, "high", "burnout_attrition"),
            ("B", "Present a capacity versus value matrix to the C-suite: demonstrate trade-offs in quality, security, and time-to-market, and recommend sequencing the top 2 initiatives in H1 while staging 3 and 4 in H2.", {"time_priority_iq": 98, "leadership_iq": 95, "business_iq": 95, "communication_iq": 90}, "low", "strategic_sequencing"),
            ("C", "Publicly challenge the CEO in an all-hands meeting and call the executive staff disconnected from reality.", {"communication_iq": 35, "eq": 30, "job_readiness_iq": 35, "leadership_iq": 35}, "high", "hostile_insubordination"),
            ("D", "Start all 4 projects simultaneously and let them all finish half-baked and buggy.", {"time_priority_iq": 40, "critical_thinking_iq": 40, "business_iq": 40, "problem_solving_iq": 40}, "high", "diluted_mediocrity")
        ],
        {"time_priority_iq": 40, "leadership_iq": 30, "business_iq": 20, "communication_iq": 10},
        45,
        "Prioritization is about what you choose NOT to do right now; sequencing high-value projects prevents catastrophic institutional dilution.",
        "Present capacity bottlenecks as sequencing choices rather than outright refusals.",
        ["Management", "Strategy", "Operations", "IT"]
    ))

    # Q75: Advanced - Interview / Cognitive Diversity Hiring
    questions.append(make_q(
        75, 4, "Interview",
        "Your team consists entirely of analytical, risk-averse perfectionists. You are interviewing for a senior product lead to accelerate bold experimentation in an ambiguous new market.",
        "How do you evaluate candidates to avoid homophily bias?",
        [
            ("A", "Hire the candidate who has the exact same background, personality, and credentials as the existing team.", {"critical_thinking_iq": 35, "interview_iq": 35, "creativity_iq": 35, "eq": 40}, "high", "homophily_groupthink"),
            ("B", "Design a behavioral rubric that explicitly scores cognitive diversity, tolerance for ambiguity, hypothesis-driven experimentation, and the courage to challenge established consensus.", {"interview_iq": 98, "critical_thinking_iq": 95, "creativity_iq": 90, "leadership_iq": 90}, "low", "diversity_calibrated_hiring"),
            ("C", "Pick the most eccentric candidate with zero qualifications just to be different.", {"interview_iq": 40, "critical_thinking_iq": 40, "business_iq": 40, "problem_solving_iq": 45}, "high", "random_hiring"),
            ("D", "Outsource the hiring decision to a lottery draw.", {"interview_iq": 20, "job_readiness_iq": 20, "critical_thinking_iq": 25, "iq": 30}, "high", "abdication")
        ],
        {"interview_iq": 40, "critical_thinking_iq": 30, "creativity_iq": 20, "leadership_iq": 10},
        45,
        "Building resilient organizations requires deliberate cognitive diversity; hire for complementary perspectives that dismantle institutional blind spots.",
        "Actively hire for skills and thinking styles missing from your current team roster.",
        ["HR", "Executive", "Management", "Consulting"]
    ))

    # Q76: Advanced - Business / Cost of Delay vs Perfection
    questions.append(make_q(
        76, 4, "Business",
        "Your team has built a new payment integration. Perfectionist engineers want another 3 months to achieve 99.999% theoretical reliability, while the current version is at 99.95% and every month of delay costs $400,000 in lost revenue.",
        "How do you arbitrate this tension?",
        [
            ("A", "Delay launch for 3 months because anything less than five-nines perfection is a disgrace to engineering.", {"business_iq": 45, "critical_thinking_iq": 45, "time_priority_iq": 40, "problem_solving_iq": 45}, "moderate", "cost_blind_perfectionism"),
            ("B", "Calculate Cost of Delay: contrast the $1.2M revenue loss against the marginal SLA differential, establish automated canary deployments with rollback monitors, and launch now to capture value.", {"business_iq": 98, "critical_thinking_iq": 95, "time_priority_iq": 95, "leadership_iq": 90}, "low", "cost_of_delay_optimization"),
            ("C", "Launch immediately with zero testing or error monitoring.", {"risk": "high", "business_iq": 35, "critical_thinking_iq": 30, "problem_solving_iq": 35}, "high", "reckless_abandon"),
            ("D", "Fire the engineering team for having high standards.", {"eq": 25, "leadership_iq": 25, "teamwork_iq": 25, "communication_iq": 30}, "high", "hostile_management")
        ],
        {"business_iq": 45, "critical_thinking_iq": 25, "time_priority_iq": 20, "leadership_iq": 10},
        45,
        "Sound business judgment optimizes for Cost of Delay: know when the marginal cost of incremental perfection exceeds its commercial risk reduction.",
        "Evaluate engineering perfection through the economic lens of Cost of Delay.",
        ["IT", "Finance", "Strategy", "Management"]
    ))

    # Q77: Advanced - Programming / Managing Technical Debt
    questions.append(make_q(
        77, 4, "Programming",
        "A legacy monolithic ERP system has become so brittle that adding a single custom field takes 4 weeks and triggers regression errors in unrelated modules.",
        "What architectural modernization strategy balances continuous business delivery with debt elimination?",
        [
            ("A", "Halt all business feature development for 18 months to perform a complete ground-up rewrite.", {"business_iq": 40, "programming_iq": 50, "time_priority_iq": 40, "leadership_iq": 45}, "high", "second_system_syndrome"),
            ("B", "Apply the Strangler Fig architectural pattern: gradually carve out distinct domain boundaries into modular microservices or APIs over time, maintaining continuous business delivery while retiring legacy components iteratively.", {"programming_iq": 98, "business_iq": 95, "critical_thinking_iq": 95, "problem_solving_iq": 95}, "low", "strangler_pattern_evolution"),
            ("C", "Continue patching spaghetti code with more conditional if-statements indefinitely.", {"programming_iq": 40, "problem_solving_iq": 45, "critical_thinking_iq": 45, "time_priority_iq": 40}, "moderate", "debt_compounding"),
            ("D", "Abandon the software and tell accounting to do everything on physical paper.", {"business_iq": 25, "programming_iq": 30, "adaptability_iq": 30, "iq": 35}, "high", "technological_surrender")
        ],
        {"programming_iq": 45, "business_iq": 25, "critical_thinking_iq": 20, "problem_solving_iq": 10},
        50,
        "Successful legacy modernization avoids catastrophic 'big-bang' rewrites by deploying evolutionary patterns (like Strangler Fig) that replace systems incrementally.",
        "Refactor legacy debt via iterative boundary extraction rather than high-risk multi-year rewrites.",
        ["IT", "Engineering", "Architecture", "Operations"]
    ))

    # Q78: Advanced - Leadership / Resolving Inter-Departmental Turf Wars (with Micro-Scenario)
    questions.append(make_q(
        78, 4, "Leadership",
        "The Heads of Product and Engineering have stopped speaking directly to each other, communicating only through hostile email threads and blocking each other's roadmap proposals.",
        "As their executive leader, what intervention restores operational harmony?",
        [
            ("A", "Allow the battle to play out to see which leader is stronger.", {"leadership_iq": 30, "eq": 30, "teamwork_iq": 30, "business_iq": 35}, "high", "social_darwinism"),
            ("B", "Convene an offsite mediation session: reset non-negotiable standards of executive professionalism, address root incentives and territorial boundaries, and tie both leaders' compensation bonuses to joint shared product outcomes.", {"leadership_iq": 98, "eq": 95, "teamwork_iq": 95, "communication_iq": 90}, "low", "incentive_aligned_mediation"),
            ("C", "Promote one over the other without addressing the underlying conflict.", {"leadership_iq": 45, "eq": 40, "teamwork_iq": 40, "communication_iq": 45}, "moderate", "fanning_flames"),
            ("D", "Send both to separate overseas branches to keep them apart physically.", {"leadership_iq": 40, "problem_solving_iq": 40, "business_iq": 40, "eq": 45}, "moderate", "geographic_evasion")
        ],
        {"leadership_iq": 40, "eq": 30, "teamwork_iq": 20, "communication_iq": 10},
        50,
        "Executive turf wars stem from misaligned structural incentives; align organizational rewards to shared outcomes and enforce unyielding standards of mutual respect.",
        "Defuse executive turf wars by coupling individual incentives directly to collective cross-functional success.",
        ["Executive", "Management", "Corporate", "HR"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "One of the leaders agrees in the session, but resumes passive-aggressive subversion two weeks later by withholding roadmap documentation.",
            "followUpQuestion": "What is your immediate consequence management response?",
            "followUpOptions": [
                {"key": "A", "text": "Execute the pre-established boundary protocol: issue a formal executive final written warning with immediate removal from the steering committee if compliance is not demonstrated within 48 hours.", "score": 95, "trait": "unflinching_accountability"},
                {"key": "B", "text": "Pretend you didn't notice the subversion.", "score": 25, "trait": "spineless_avoidance"},
                {"key": "C", "text": "Apologize to them and give them a special bonus.", "score": 20, "trait": "rewarding_toxicity"}
            ]
        }
    ))

    # Q79: Advanced - AI / Autonomous Generative Code & Security
    questions.append(make_q(
        79, 4, "AI",
        "A development team begins using external generative AI code assistants to write proprietary cryptographic security modules, pasting internal architecture code into public cloud prompts.",
        "How do you govern generative AI engineering practices?",
        [
            ("A", "Ignore the practice since developers write code faster this way.", {"aiq": 25, "ethics_judgment_iq": 25, "critical_thinking_iq": 30, "risk": "high"}, "high", "ip_leakage_negligence"),
            ("B", "Institute clear enterprise AI policies: deploy on-premises or enterprise-contracted zero-retention LLM endpoints, establish data loss prevention (DLP) code gates, and require mandatory static analysis and peer security reviews for all AI-synthesized code.", {"aiq": 98, "ethics_judgment_iq": 95, "critical_thinking_iq": 95, "programming_iq": 90}, "low", "enterprise_ai_safeguarding"),
            ("C", "Confiscate all developer computers and disconnect the office from the internet forever.", {"aiq": 35, "adaptability_iq": 30, "business_iq": 30, "problem_solving_iq": 35}, "high", "reactionary_draconian"),
            ("D", "Order developers to change variable names before pasting confidential code into public web tools.", {"aiq": 40, "critical_thinking_iq": 45, "ethics_judgment_iq": 40, "job_readiness_iq": 40}, "moderate", "naive_obfuscation")
        ],
        {"aiq": 40, "ethics_judgment_iq": 30, "critical_thinking_iq": 15, "programming_iq": 15},
        50,
        "Enterprise AI enablement pairs productivity acceleration with stringent zero-data-retention agreements and automated secret scanning pipelines.",
        "Never paste proprietary architectural logic into consumer AI services; provision enterprise-shielded endpoints.",
        ["IT", "AI", "Cybersecurity", "Corporate"]
    ))

    # Q80: Advanced - Communication / Hostile Media Navigation
    questions.append(make_q(
        80, 4, "Communication",
        "During a live broadcast press interview, an aggressive journalist asks: 'Isn't it true that your company's latest restructuring is just a greedy cover for executive bonus hikes while abandoning loyal employees?'",
        "What communications pivot establishes command and credibility?",
        [
            ("A", "Lose your temper, yell at the journalist, and storm out of the television studio.", {"communication_iq": 25, "eq": 20, "leadership_iq": 25, "promotion_readiness_iq": 25}, "high", "temperamental_meltdown"),
            ("B", "Acknowledge the emotional gravity of career transitions with empathy, pivot to facts: detail the executive compensation freezes implemented, explain the industry structural realities driving the shift, and share the comprehensive transition support packages provided.", {"communication_iq": 98, "eq": 95, "leadership_iq": 95, "promotion_readiness_iq": 90}, "low", "masterful_press_pivot"),
            ("C", "Answer 'No comment' and stare blankly into the camera for the remainder of the broadcast.", {"communication_iq": 35, "eq": 35, "job_readiness_iq": 40, "leadership_iq": 35}, "high", "stony_defiance"),
            ("D", "Make up a story about a philanthropic donation to deflect the question.", {"ethics_judgment_iq": 20, "communication_iq": 30, "critical_thinking_iq": 30, "risk": "high"}, "high", "deceptive_deflection")
        ],
        {"communication_iq": 45, "eq": 30, "leadership_iq": 15, "promotion_readiness_iq": 10},
        45,
        "Mastering adversarial media requires calm emotional poise: validate the underlying human concern, anchor to verifiable facts, and bridge to the strategic reality.",
        "Under media interrogation, meet emotion with empathy and allegations with transparent data.",
        ["Media", "PR", "Executive", "Corporate"]
    ))

    # =========================================================================
    # LEVEL 5: EXECUTIVE (Q81 - Q100)
    # =========================================================================

    # Q81: Executive - Strategy / Vision vs Quarterly Pressures
    questions.append(make_q(
        81, 5, "Business",
        "Wall Street or private equity investors pressure your enterprise to cut long-term foundational R&D by 40% to beat this quarter's EBITDA earnings expectations by 2 cents per share.",
        "What is your fiduciary leadership stance as Chief Executive?",
        [
            ("A", "Cut R&D by 50% immediately to trigger an executive bonus payout this quarter.", {"business_iq": 30, "ethics_judgment_iq": 30, "critical_thinking_iq": 35, "leadership_iq": 30}, "high", "mercenary_short_termism"),
            ("B", "Defend sustainable enterprise valuation: clearly articulate the multi-year ROI and pipeline maturity of the R&D assets, identify operational efficiencies in non-core overhead instead, and communicate transparent guidance to long-term capital partners.", {"business_iq": 98, "leadership_iq": 98, "critical_thinking_iq": 95, "ethics_judgment_iq": 90}, "low", "long_term_fiduciary_stewardship"),
            ("C", "Falsify the quarterly accounting entries to make earnings look higher without cutting anything.", {"ethics_judgment_iq": 10, "business_iq": 15, "critical_thinking_iq": 20, "risk": "high"}, "high", "criminal_accounting"),
            ("D", "Send a public tweet insulting the intelligence of all financial analysts.", {"communication_iq": 25, "eq": 20, "leadership_iq": 25, "business_iq": 30}, "high", "reckless_antagonism")
        ],
        {"business_iq": 40, "leadership_iq": 35, "critical_thinking_iq": 15, "ethics_judgment_iq": 10},
        50,
        "True executive stewardship protects long-term competitive moats against short-term market myopia through transparent investor communication and disciplined balance sheet management.",
        "Never mortgage an enterprise's future innovation engine to satisfy ephemeral quarterly optics.",
        ["Executive", "Finance", "Strategy", "Corporate"]
    ))

    # Q82: Executive - Governance / Activist Shareholder Proxy Battle
    questions.append(make_q(
        82, 5, "Leadership",
        "An aggressive activist hedge fund acquires an 8% stake and demands three board seats and the immediate spin-off and sale of your core digital infrastructure division.",
        "How does the Board of Directors navigate this activist challenge?",
        [
            ("A", "Adopt an entrenched poison pill defense and refuse to speak to the activist fund.", {"leadership_iq": 45, "business_iq": 50, "communication_iq": 45, "critical_thinking_iq": 50}, "moderate", "dogmatic_entrenchment"),
            ("B", "Engage the activist in substantive strategic dialogue: evaluate their critique dispassionately with independent investment bankers, accelerate dormant value-creation initiatives, and present an optimized standalone plan to institutional shareholders.", {"leadership_iq": 98, "business_iq": 98, "critical_thinking_iq": 95, "communication_iq": 90}, "low", "strategic_shareholder_engagement"),
            ("C", "Surrender immediately and sell the division at a discount to avoid conflict.", {"leadership_iq": 35, "business_iq": 40, "eq": 40, "risk": "high"}, "high", "fiduciary_capitulation"),
            ("D", "Leak derogatory rumors about the activist fund manager to tabloid blogs.", {"ethics_judgment_iq": 20, "communication_iq": 25, "eq": 25, "leadership_iq": 25}, "high", "unethical_smear")
        ],
        {"leadership_iq": 40, "business_iq": 35, "critical_thinking_iq": 15, "communication_iq": 10},
        50,
        "Activist challenges should be treated as rigorous strategic audits: extract legitimate operational insights while defending enduring shareholder value through proactive board governance.",
        "Engage activists with rigorous analytical modeling; co-opt sound operational ideas while defending core strategic unity.",
        ["Executive", "Board", "Finance", "Corporate"]
    ))

    # Q83: Executive - Culture / Institutional Renewal
    questions.append(make_q(
        83, 5, "Leadership",
        "You take over as CEO of a 50-year-old market leader suffering from bureaucratic inertia, risk aversion, and declining innovation, where decisions require 14 layers of committee approvals.",
        "What systemic levers do you pull to awaken corporate agility?",
        [
            ("A", "Add 5 more oversight committees to investigate why the existing committees are slow.", {"leadership_iq": 25, "critical_thinking_iq": 30, "problem_solving_iq": 30, "business_iq": 30}, "high", "bureaucratic_parody"),
            ("B", "Dismantle redundant approval hierarchies, decentralize decision rights with clear spending limits, establish internal incubator sprint teams, reward courageous calculated failures, and tie executive metrics directly to innovation velocity.", {"leadership_iq": 98, "adaptability_iq": 98, "business_iq": 95, "creativity_iq": 90}, "low", "organizational_debureaucratization"),
            ("C", "Fire the entire company workforce and replace them with college freshers overnight.", {"leadership_iq": 25, "eq": 20, "business_iq": 25, "risk": "high"}, "high", "catastrophic_cleansing"),
            ("D", "Put motivational posters about agility in all the hallways and change nothing else.", {"leadership_iq": 35, "creativity_iq": 35, "communication_iq": 35, "job_readiness_iq": 35}, "moderate", "cosmetic_theatrics")
        ],
        {"leadership_iq": 40, "adaptability_iq": 30, "business_iq": 20, "creativity_iq": 10},
        50,
        "Cultural renewal requires structural deregulation: removing bureaucratic choke points, granting autonomy with accountability, and aligning incentives with bold calculated bets.",
        "Culture follows structure: collapse hierarchical approval layers to foster entrepreneurial initiative.",
        ["Executive", "Management", "Strategy", "HR"]
    ))

    # Q84: Executive - Ethics / Safety Recall vs Solvency
    questions.append(make_q(
        84, 5, "Ethical",
        "Your automotive or medical device company discovers a 1-in-100,000 potential micro-defect that could cause intermittent failures under extreme environmental conditions. A worldwide recall will wipe out 80% of this year's company profits.",
        "What is your executive decision?",
        [
            ("A", "Bury the internal safety report and set aside a legal settlement fund for future casualties.", {"ethics_judgment_iq": 10, "critical_thinking_iq": 20, "risk": "high", "leadership_iq": 15}, "high", "criminal_negligence"),
            ("B", "Order an immediate global product recall and transparent customer advisory: prioritize human life unreservedly, cooperate with international regulatory agencies, and mobilize 24/7 service replacement logistics.", {"ethics_judgment_iq": 99, "leadership_iq": 98, "business_iq": 90, "eq": 95}, "low", "uncompromising_safety_stewardship"),
            ("C", "Recall products only in countries where consumer protection laws enforce criminal penalties.", {"ethics_judgment_iq": 25, "business_iq": 30, "critical_thinking_iq": 35, "risk": "high"}, "high", "mercenary_selectivity"),
            ("D", "Blame the end-users for operating the equipment in extreme environmental conditions.", {"ethics_judgment_iq": 20, "communication_iq": 25, "eq": 25, "sales_iq": 20}, "high", "victim_blaming")
        ],
        {"ethics_judgment_iq": 50, "leadership_iq": 30, "eq": 10, "business_iq": 10},
        50,
        "When human safety is at stake, ethical clarity is absolute: short-term financial solvency can be rebuilt, but compromised integrity and lost lives can never be recovered.",
        "Never calculate human life in financial settlement spreadsheets; execute immediate, transparent remediation.",
        ["Healthcare", "Automotive", "Executive", "Legal"]
    ))

    # Q85: Executive - AI / Enterprise Transformation & Workforce Transition (with Micro-Scenario)
    questions.append(make_q(
        85, 5, "AI",
        "Your enterprise strategy envisions deploying agentic AI systems that will structurally automate 35% of existing knowledge-worker tasks across finance, legal, and operational analysis over the next 24 months.",
        "How do you lead a humane and value-creating organizational transition?",
        [
            ("A", "Carry out sudden mass layoffs with 24 hours notice to maximize instantaneous stock price pop.", {"eq": 20, "leadership_iq": 25, "ethics_judgment_iq": 25, "business_iq": 35}, "high", "predatory_disruption"),
            ("B", "Launch an Enterprise AI Reskilling Academy: transparently communicate the technological roadmap, design pathway bridges into high-value advisory, customer experience, and AI oversight roles, and provide structured outplacement and severance for surplus functions.", {"aiq": 98, "leadership_iq": 98, "ethics_judgment_iq": 95, "eq": 95}, "low", "responsible_ai_workforce_stewardship"),
            ("C", "Ban all AI tools across the enterprise to protect legacy jobs forever, ignoring competitor advancements.", {"aiq": 25, "adaptability_iq": 25, "business_iq": 30, "critical_thinking_iq": 30}, "high", "ostrich_strategy"),
            ("D", "Tell employees that AI is just a passing fad and that nothing will change.", {"communication_iq": 30, "eq": 30, "leadership_iq": 30, "aiq": 35}, "high", "deliberate_obfuscation")
        ],
        {"aiq": 35, "leadership_iq": 35, "ethics_judgment_iq": 20, "eq": 10},
        50,
        "Visionary executives champion technological leaps while honoring their workforce contract through aggressive reskilling, transparent roadmaps, and dignified transition safety nets.",
        "Lead AI transformation through transparent workforce capability bridges rather than clandestine labor purges.",
        ["Executive", "AI", "HR", "Corporate"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "Six months into the reskilling program, an external investor criticizes the academy as 'wasteful social work' and demands accelerated headcount cuts to boost quarterly operating margin.",
            "followUpQuestion": "How do you defend the human capital investment to the board?",
            "followUpOptions": [
                {"key": "A", "text": "Present retention data showing that retrained domain experts deploying AI deliver 3x higher product accuracy than raw entry-level contractors, proving higher enterprise lifetime value.", "score": 98, "trait": "visionary_statesman"},
                {"key": "B", "text": "Fold immediately and terminate the academy tomorrow.", "score": 25, "trait": "opportunistic_collapse"},
                {"key": "C", "text": "Ignore the board entirely and refuse to answer their emails.", "score": 30, "trait": "governance_obstruction"}
            ]
        }
    ))

    # Q86: Executive - Crisis / Solvency & Liquidity Shock
    questions.append(make_q(
        86, 5, "Crisis",
        "A sudden collapse of a major regional banking partner freezes 60% of your company's operational working capital 5 days before worldwide payroll is due for 12,000 employees.",
        "What is your rapid liquidity mobilization sequence?",
        [
            ("A", "Skip payroll silently and hope employees do not notice their bank balances on payday.", {"ethics_judgment_iq": 15, "leadership_iq": 20, "communication_iq": 25, "risk": "high"}, "high", "fraudulent_omission"),
            ("B", "Form an emergency Treasury War Room: activate secondary credit facilities, negotiate emergency liquidity backstops with syndicate banks, liquidate high-grade short-term treasuries, and maintain transparent, daily employee communications.", {"problem_solving_iq": 98, "leadership_iq": 98, "business_iq": 95, "communication_iq": 90}, "low", "crisis_liquidity_orchestration"),
            ("C", "File for immediate corporate liquidation without trying to access secondary credit.", {"business_iq": 35, "critical_thinking_iq": 35, "leadership_iq": 35, "problem_solving_iq": 35}, "high", "hasty_surrender"),
            ("D", "Ask employees to donate their personal savings back to the company.", {"ethics_judgment_iq": 20, "eq": 20, "leadership_iq": 20, "business_iq": 20}, "high", "exploitative_desperation")
        ],
        {"leadership_iq": 40, "problem_solving_iq": 30, "business_iq": 20, "communication_iq": 10},
        50,
        "Treasury crises test operational contingency depth: executing multi-channel liquidity syndication while maintaining transparent human leadership prevents organizational panic.",
        "Maintain secondary emergency liquidity conduits; communicate with transparent empathy while executing treasury backstops.",
        ["Finance", "Executive", "Banking", "Crisis"]
    ))

    # Q87: Executive - M&A / Strategic Acquisition Governance
    questions.append(make_q(
        87, 5, "Business",
        "Your company has the opportunity to acquire an emerging competitor for $400M. The target's founders demand complete independence from corporate oversight and exemption from your enterprise compliance standards.",
        "How do you govern this acquisition?",
        [
            ("A", "Accept all founder demands unconditionally because buying market share is all that counts.", {"critical_thinking_iq": 30, "ethics_judgment_iq": 30, "business_iq": 35, "leadership_iq": 35}, "high", "unmitigated_liability_absorption"),
            ("B", "Structure a balanced governance framework: protect their entrepreneurial culture and product autonomy, but mandate strict adherence to universal financial, legal, security, and safety compliance baselines.", {"business_iq": 98, "critical_thinking_iq": 95, "leadership_iq": 95, "ethics_judgment_iq": 90}, "low", "balanced_post_merger_governance"),
            ("C", "Break off all talks immediately and launch a campaign to drive the startup into bankruptcy.", {"business_iq": 45, "eq": 40, "leadership_iq": 45, "ethics_judgment_iq": 45}, "moderate", "vindictive_aggression"),
            ("D", "Sign the contract promising independence, then fire the founders the day after closing.", {"ethics_judgment_iq": 15, "leadership_iq": 20, "eq": 20, "business_iq": 25}, "high", "bad_faith_duplicity")
        ],
        {"business_iq": 40, "leadership_iq": 30, "critical_thinking_iq": 20, "ethics_judgment_iq": 10},
        50,
        "Post-merger integration requires protecting the target's creative vitality while establishing unbending fiduciary and ethical compliance guardrails.",
        "Differentiate operational autonomy from fiduciary compliance: protect creative freedom while anchoring risk governance.",
        ["M&A", "Strategy", "Executive", "Corporate"]
    ))

    # Q88: Executive - Leadership / Board Succession & Institutional Longevity
    questions.append(make_q(
        88, 5, "Promotion",
        "As CEO planning to retire in 24 months, you have two exceptional internal candidates: one is a operational genius who commands deep employee loyalty; the other is a visionary technologist who can out-innovate competitors.",
        "What is your succession preparation strategy?",
        [
            ("A", "Pick your personal favorite now and tell the other candidate to leave the firm.", {"leadership_iq": 40, "eq": 40, "promotion_readiness_iq": 45, "critical_thinking_iq": 45}, "moderate", "premature_alienation"),
            ("B", "Design a 2-year leadership crucible: rotate both into cross-functional development areas (giving the technologist operational P&L responsibility and the operator global strategic partnerships), while building an aligned executive team that pairs their strengths.", {"promotion_readiness_iq": 98, "leadership_iq": 98, "eq": 95, "business_iq": 90}, "low", "crucible_succession_architecture"),
            ("C", "Refuse to ever retire and remain CEO until you are 95 years old.", {"leadership_iq": 30, "adaptability_iq": 25, "promotion_readiness_iq": 30, "critical_thinking_iq": 35}, "high", "monarchical_entrenchment"),
            ("D", "Let them engage in covert political warfare to see who survives.", {"leadership_iq": 25, "teamwork_iq": 20, "eq": 25, "ethics_judgment_iq": 25}, "high", "destructive_gladiatorial")
        ],
        {"promotion_readiness_iq": 40, "leadership_iq": 35, "eq": 15, "business_iq": 10},
        50,
        "The ultimate test of leadership is succession: developing well-rounded successors through deliberate cross-domain stretch rotations that safeguard institutional continuity.",
        "The best leaders build organizations that outlast them by actively developing multidimensional successors.",
        ["Executive", "Governance", "HR", "Leadership"]
    ))

    # Q89: Executive - Critical Thinking / Geopolitical Decoupling
    questions.append(make_q(
        89, 5, "Critical Thinking",
        "Rising trade tensions indicate that your primary international manufacturing market may face 50% tariffs and technology export restrictions within 18 months.",
        "What strategic decoupling thesis do you present to the Board?",
        [
            ("A", "Lobby politicians frantically and assume global geopolitical trends will reverse themselves.", {"critical_thinking_iq": 40, "adaptability_iq": 40, "business_iq": 40, "leadership_iq": 45}, "moderate", "wishful_thinking"),
            ("B", "Formulate a 'China+1' or regionalized nearshoring diversification roadmap: establish redundant manufacturing hubs in secondary markets, secure localized supply contracts, and re-architect product hardware to utilize trade-compliant silicon.", {"critical_thinking_iq": 98, "business_iq": 98, "adaptability_iq": 95, "problem_solving_iq": 90}, "low", "geopolitical_diversification"),
            ("C", "Immediately burn down all existing international facilities tomorrow to make a political statement.", {"critical_thinking_iq": 20, "business_iq": 20, "risk": "high", "leadership_iq": 20}, "high", "irrational_vandalism"),
            ("D", "Smuggle components illegally through shell companies to evade tariffs.", {"ethics_judgment_iq": 10, "critical_thinking_iq": 15, "risk": "high", "job_readiness_iq": 20}, "high", "criminal_evasion")
        ],
        {"critical_thinking_iq": 40, "business_iq": 35, "adaptability_iq": 15, "problem_solving_iq": 10},
        50,
        "Global enterprises must build geopolitical resilience: shifting from fragile single-region hyper-efficiency to regionalized supply redundancy.",
        "Build structural multi-region redundancy before geopolitical sanctions freeze single-source supply chains.",
        ["Operations", "Manufacturing", "Executive", "Strategy"]
    ))

    # Q90: Executive - Innovation / Disruptive Moats (with Micro-Scenario)
    questions.append(make_q(
        90, 5, "Creativity",
        "A decentralized open-source technology threatens to eliminate the proprietary software lock-in that generates $1B in high-margin recurring licensing fees for your enterprise.",
        "How do you reinvent your corporate moat?",
        [
            ("A", "File patent infringement lawsuits against every open-source contributor you can locate.", {"critical_thinking_iq": 30, "creativity_iq": 30, "business_iq": 35, "marketing_iq": 30}, "high", "anti_developer_litigation"),
            ("B", "Embrace open-source leadership: open-core your base protocol to capture global developer mindshare, while building enterprise moats around secure managed orchestration, proprietary compliance modules, and mission-critical SLAs.", {"creativity_iq": 98, "business_iq": 98, "adaptability_iq": 95, "leadership_iq": 90}, "low", "open_core_ecosystem_pivot"),
            ("C", "Pretend open-source code cannot perform in real enterprise environments and do nothing.", {"business_iq": 35, "critical_thinking_iq": 35, "adaptability_iq": 35, "iq": 40}, "moderate", "willful_denial"),
            ("D", "Delete your company's GitHub account and forbid engineers from reading open code.", {"creativity_iq": 25, "adaptability_iq": 25, "leadership_iq": 25, "programming_iq": 30}, "high", "reactionary_insularity")
        ],
        {"creativity_iq": 40, "business_iq": 35, "adaptability_iq": 15, "leadership_iq": 10},
        50,
        "When open ecosystems commoditize proprietary code, market leaders pivot their moats to developer ecosystems, enterprise security, and operational reliability.",
        "Monetize the ecosystem around open protocols rather than fruitlessly litigating against open developer momentum.",
        ["IT", "Tech", "Executive", "Strategy"],
        micro_scenario={
            "triggerOption": "B",
            "complication": "Six months after open-sourcing the base protocol, a competing cloud giant forks your project and begins offering it as a bare-bones hosted service at 80% discount.",
            "followUpQuestion": "How do you defend your business model against cloud provider forking?",
            "followUpOptions": [
                {"key": "A", "text": "Innovate aggressively on developer experience, deep enterprise workflow integrations, and proprietary governance tooling that bare cloud infrastructure cannot match.", "score": 98, "trait": "ecosystem_innovator"},
                {"key": "B", "text": "Revert the license to closed source and sue all users.", "score": 30, "trait": "community_alienation"},
                {"key": "C", "text": "Shut down the business.", "score": 20, "trait": "total_surrender"}
            ]
        }
    ))

    # Q91: Executive - EQ & People / Compassionate Downsizing
    questions.append(make_q(
        91, 5, "EQ",
        "A secular decline in demand forces your company to eliminate 1,500 roles across 4 countries. How you handle this announcement will define your organizational reputation for decades.",
        "What principles govern the execution of this restructuring?",
        [
            ("A", "Deactivate all badges at midnight on Sunday and send a generic termination email with no severance details.", {"eq": 15, "leadership_iq": 20, "communication_iq": 20, "ethics_judgment_iq": 20}, "high", "callous_cruelty"),
            ("B", "Deliver the message personally as CEO: take direct responsibility without hiding behind macroeconomic euphemisms, provide above-market severance and extended healthcare, establish active job placement networks, and hold live town halls for remaining teams.", {"eq": 98, "leadership_iq": 98, "communication_iq": 95, "ethics_judgment_iq": 95}, "low", "dignified_human_stewardship"),
            ("C", "Have mid-level managers execute the firing while you take a vacation on a private yacht.", {"eq": 10, "leadership_iq": 15, "communication_iq": 15, "ethics_judgment_iq": 15}, "high", "abject_cowardice"),
            ("D", "Deny that any layoffs are occurring while quietly firing 50 people every day for a year.", {"communication_iq": 25, "eq": 25, "ethics_judgment_iq": 25, "leadership_iq": 25}, "high", "prolonged_water_torture")
        ],
        {"eq": 40, "leadership_iq": 30, "communication_iq": 20, "ethics_judgment_iq": 10},
        50,
        "Executive character is revealed during hardship: treating departing employees with generosity, transparency, and dignity preserves institutional honor.",
        "Own restructuring decisions directly; never offload personal executive accountability to impersonal algorithms or subordinates.",
        ["Executive", "HR", "Leadership", "Corporate"]
    ))

    # Q92: Executive - Ethics / International Corruption & Integrity
    questions.append(make_q(
        92, 5, "Ethical",
        "A foreign government official indicates that your company will win a $200M infrastructure concession if you route a $2M 'advisory facilitation fee' through an offshore consulting entity.",
        "What is your unequivocal executive mandate?",
        [
            ("A", "Pay the $2M fee immediately because foreign business customs require facilitation payments.", {"ethics_judgment_iq": 10, "job_readiness_iq": 15, "risk": "high", "critical_thinking_iq": 20}, "high", "criminal_foreign_bribery"),
            ("B", "Flatly reject the proposal: uphold strict Foreign Corrupt Practices Act (FCPA) and anti-bribery standards, mandate that all tenders proceed solely through official public procurement channels, and report the solicitation to legal counsel.", {"ethics_judgment_iq": 99, "leadership_iq": 98, "critical_thinking_iq": 95, "business_iq": 90}, "low", "uncompromising_anti_corruption"),
            ("C", "Ask if the official will accept $1M instead to reduce the cost.", {"ethics_judgment_iq": 10, "business_iq": 15, "critical_thinking_iq": 15, "risk": "high"}, "high", "brazen_negotiated_bribery"),
            ("D", "Transfer the funds in cash via personal luggage.", {"ethics_judgment_iq": 5, "job_readiness_iq": 10, "risk": "high", "leadership_iq": 10}, "high", "felonious_smuggling")
        ],
        {"ethics_judgment_iq": 50, "leadership_iq": 30, "critical_thinking_iq": 10, "business_iq": 10},
        50,
        "Integrity is indivisible: paying bribes corrupts an institution's soul and incurs devastating international criminal prosecution regardless of revenue size.",
        "Zero tolerance for foreign bribery; no commercial contract is worth compromising legal and ethical sovereignty.",
        ["Executive", "Legal", "International", "Infrastructure"]
    ))

    # Q93: Executive - Critical Thinking / Sunk Cost in Mega-Projects
    questions.append(make_q(
        93, 5, "Critical Thinking",
        "Your enterprise has spent $120M over 4 years developing a custom manufacturing automation system. Independent testing reveals modern external robotic platforms can now be bought off-the-shelf for $15M that perform 2x faster than your system.",
        "How do you resolve the sunk cost dilemma?",
        [
            ("A", "Continue spending $30M/year on the custom system because throwing away $120M would look embarrassing to prior leadership.", {"critical_thinking_iq": 25, "business_iq": 30, "problem_solving_iq": 30, "leadership_iq": 30}, "high", "sunk_cost_trap"),
            ("B", "Overcome the sunk cost fallacy: ruthlessly terminate the in-house development project, salvage reusable sensor algorithms and patents, transition to the superior $15M platform, and redirect capital toward core market expansion.", {"critical_thinking_iq": 99, "business_iq": 98, "leadership_iq": 95, "problem_solving_iq": 90}, "low", "rational_capital_reallocation"),
            ("C", "Hide the test results from the board of directors so no one finds out about the $15M platform.", {"ethics_judgment_iq": 15, "critical_thinking_iq": 20, "business_iq": 20, "risk": "high"}, "high", "fiduciary_fraud"),
            ("D", "Buy the competitor company and burn down their factory to stop their platform from existing.", {"ethics_judgment_iq": 10, "business_iq": 15, "leadership_iq": 15, "risk": "high"}, "high", "criminal_megalomania")
        ],
        {"critical_thinking_iq": 45, "business_iq": 35, "problem_solving_iq": 10, "leadership_iq": 10},
        50,
        "Mastery of capital discipline requires discarding sunk costs: evaluate decisions solely based on future marginal cash flows and operational effectiveness.",
        "Sunk capital is gone forever; allocate tomorrow's dollars strictly against tomorrow's highest marginal returns.",
        ["Executive", "Operations", "Finance", "Strategy"]
    ))

    # Q94: Executive - Communication / National Crisis Press Conference
    questions.append(make_q(
        94, 5, "Communication",
        "An industrial plant malfunction releases a non-toxic but foul-smelling cloud over a metropolitan area of 500,000 residents. Social media rumors claim the cloud contains lethal neurotoxins.",
        "How do you lead the emergency public broadcast?",
        [
            ("A", "Hide inside the facility and send a junior intern to read a prepared legalese statement.", {"communication_iq": 20, "leadership_iq": 20, "eq": 20, "ethics_judgment_iq": 25}, "high", "executive_cowardice"),
            ("B", "Stand before cameras immediately alongside public health officials: state verified atmospheric readings transparently, explain what chemical was released and its exact health profile, apologize unreservedly for the distress, and open independent air-monitoring stations.", {"communication_iq": 99, "leadership_iq": 98, "eq": 95, "ethics_judgment_iq": 90}, "low", "transparent_crisis_leadership"),
            ("C", "Claim that the citizens are imagining the smell and that the air has never been cleaner.", {"communication_iq": 15, "eq": 15, "leadership_iq": 15, "risk": "high"}, "high", "gaslighting_populace"),
            ("D", "Announce that the plant is shutting down permanently and leaving the country tonight.", {"communication_iq": 30, "business_iq": 30, "problem_solving_iq": 30, "leadership_iq": 35}, "high", "reactive_abdication")
        ],
        {"communication_iq": 45, "leadership_iq": 30, "eq": 15, "ethics_judgment_iq": 10},
        50,
        "In public emergencies, vacuum invites panic: step forward immediately, anchor communications to verified science, collaborate with civic authorities, and demonstrate relentless empathy.",
        "Defeat dangerous rumors by flooding the public domain with verified independent scientific telemetry.",
        ["Executive", "PR", "Government", "Environmental"]
    ))

    # Q95: Executive - Adaptability / Enterprise Operating Model
    questions.append(make_q(
        95, 5, "Adaptability",
        "Your multinational organization faces intense talent attrition because competitor firms offer flexible hybrid work while your regional directors demand a rigid 5-day in-office mandate.",
        "How do you architect an enduring future-ready workplace model?",
        [
            ("A", "Threaten to fire anyone who mentions remote work ever again.", {"adaptability_iq": 20, "leadership_iq": 25, "eq": 25, "business_iq": 30}, "high", "draconian_inflexibility"),
            ("B", "Architect an Outcome-Based Operating Model: establish purposeful office hubs for collaborative innovation and client workshops, permit distributed asynchronous execution for deep work, and evaluate talent strictly on impact rather than physical seat presence.", {"adaptability_iq": 98, "leadership_iq": 98, "eq": 95, "business_iq": 90}, "low", "outcome_based_hybrid_architecture"),
            ("C", "Close all offices permanently and never allow employees to see each other in person.", {"adaptability_iq": 50, "leadership_iq": 50, "teamwork_iq": 55, "eq": 55}, "moderate", "polar_overcorrection"),
            ("D", "Install surveillance software on every laptop to track mouse movements every 30 seconds.", {"eq": 15, "leadership_iq": 20, "ethics_judgment_iq": 20, "adaptability_iq": 25}, "high", "surveillance_distrust")
        ],
        {"adaptability_iq": 40, "leadership_iq": 30, "eq": 15, "business_iq": 15},
        50,
        "The future of work is not about where desks sit, but how trust and autonomy are governed: evaluate talent on measurable business impact, not performative office presence.",
        "Replace performative presenteeism with rigorous objective outcome evaluation.",
        ["Executive", "HR", "Corporate", "Management"]
    ))

    # Q96: Executive - Sales & Ecosystem / Direct vs Channel Strategy
    questions.append(make_q(
        96, 5, "Sales",
        "Your enterprise software has relied on direct sales, but growth has hit a plateau at $100M ARR. Channel partners and systems integrators refuse to resell your product because your direct sales force repeatedly poaches their deals.",
        "How do you rebuild trust and ignite an indirect partner ecosystem?",
        [
            ("A", "Continue poaching partner deals because direct revenue carries higher margins.", {"sales_iq": 35, "business_iq": 35, "leadership_iq": 35, "ethics_judgment_iq": 40}, "moderate", "channel_conflict_blindness"),
            ("B", "Institute ironclad Rules of Engagement: introduce Deal Registration protections, compensate direct sales reps equally for partner-originated deals, and dedicate professional services margin to external certified partners.", {"sales_iq": 98, "business_iq": 98, "leadership_iq": 95, "teamwork_iq": 90}, "low", "ecosystem_alignment_governance"),
            ("C", "Ban third-party partners and hire 1,000 junior cold-callers.", {"sales_iq": 40, "business_iq": 35, "time_priority_iq": 40, "problem_solving_iq": 40}, "high", "regressive_bloat"),
            ("D", "Sue the systems integrators for promoting competitive products.", {"sales_iq": 25, "communication_iq": 25, "business_iq": 30, "risk": "high"}, "high", "destructive_litigation")
        ],
        {"sales_iq": 40, "business_iq": 35, "leadership_iq": 15, "teamwork_iq": 10},
        50,
        "Scaling past $100M ARR requires ecosystem leverage: align internal sales commissions so your direct sales force champions partner success instead of fighting over deals.",
        "Neutralize channel conflict by aligning direct sales incentives to celebrate partner co-selling.",
        ["Sales", "Strategy", "Executive", "Partnerships"]
    ))

    # Q97: Executive - Promotion Readiness & Executive Talent Development
    questions.append(make_q(
        97, 5, "Promotion",
        "You are establishing the assessment criteria to select the next Chief Operating Officer (COO) from among 4 accomplished Senior Vice Presidents.",
        "What capability profile reflects true C-suite readiness?",
        [
            ("A", "Select whoever has worked at the company for the longest number of consecutive years.", {"promotion_readiness_iq": 35, "critical_thinking_iq": 35, "leadership_iq": 40, "iq": 40}, "moderate", "tenure_fallacy"),
            ("B", "Evaluate candidates on strategic synthesis, cross-functional organizational influence, crisis composure, talent magnetism, and the capacity to balance capital discipline with ambitious innovation.", {"promotion_readiness_iq": 99, "leadership_iq": 98, "critical_thinking_iq": 95, "business_iq": 95}, "low", "holistic_executive_evaluation"),
            ("C", "Choose whoever screams the loudest in boardroom disagreements to ensure toughness.", {"leadership_iq": 25, "eq": 20, "communication_iq": 25, "promotion_readiness_iq": 25}, "high", "toxic_machismo"),
            ("D", "Have the board draw names out of a hat to keep it fair.", {"promotion_readiness_iq": 15, "critical_thinking_iq": 20, "job_readiness_iq": 20, "leadership_iq": 20}, "high", "abdication")
        ],
        {"promotion_readiness_iq": 40, "leadership_iq": 35, "critical_thinking_iq": 15, "business_iq": 10},
        50,
        "C-Suite readiness transcends functional mastery: it requires system-level orchestration, emotional equilibrium under existential uncertainty, and inspiring collective belief.",
        "Promote leaders based on system-level synthesis and cultural stewardship, not functional tenure alone.",
        ["Executive", "HR", "Corporate", "Board"]
    ))

    # Q98: Executive - Digital & Frontier Tech / Quantum & Emerging Tech
    questions.append(make_q(
        98, 5, "AI",
        "Frontier technological disruptions (quantum computing, autonomous neuro-interfaces) loom on a 5-to-10 year horizon, threatening to break current data encryption standards across your financial enterprise.",
        "What anticipatory technology leadership do you demonstrate?",
        [
            ("A", "Ignore the horizon because 5-to-10 years is someone else's problem.", {"aiq": 30, "critical_thinking_iq": 30, "business_iq": 35, "leadership_iq": 35}, "high", "strategic_procrastination"),
            ("B", "Establish a Post-Quantum Cryptography transition taskforce: audit all encrypted enterprise assets, pilot quantum-resistant cryptographic algorithms, and collaborate with standard bodies (NIST) to future-proof customer trust.", {"aiq": 98, "critical_thinking_iq": 98, "leadership_iq": 95, "programming_iq": 90}, "low", "proactive_frontier_defense"),
            ("C", "Spend $500M buying experimental quantum computers before having any use case.", {"aiq": 45, "business_iq": 40, "critical_thinking_iq": 40, "time_priority_iq": 45}, "high", "frivolous_speculation"),
            ("D", "Stop encrypting customer data altogether so there is nothing for quantum computers to break.", {"ethics_judgment_iq": 5, "aiq": 10, "risk": "high", "critical_thinking_iq": 10}, "high", "absurd_negligence")
        ],
        {"aiq": 40, "critical_thinking_iq": 30, "leadership_iq": 15, "programming_iq": 15},
        50,
        "Frontier technology stewardship involves proactively upgrading fundamental infrastructure against horizon risks long before the disruption becomes an existential crisis.",
        "Upgrade systemic security foundations proactively; cryptographic migrations require multi-year lead times.",
        ["IT", "Finance", "AI", "Executive"]
    ))

    # Q99: Executive - Strategy / Margin vs Market Share
    questions.append(make_q(
        99, 5, "Business",
        "A well-capitalized tech giant enters your core market, offering heavily subsidized free services to capture market share. Your gross margin is 65% while theirs is effectively negative.",
        "How do you defend and grow your enterprise without burning out your treasury?",
        [
            ("A", "Offer all your products 100% free and burn through your entire cash reserves in 6 months.", {"business_iq": 30, "critical_thinking_iq": 35, "leadership_iq": 35, "risk": "high"}, "high", "treasury_exhaustion"),
            ("B", "Shift competition from subsidized commodity pricing to deeply embedded mission-critical workflows: deepen custom enterprise integrations, offer guaranteed high-touch SLAs, and deliver specialized compliance features that horizontal giants cannot support.", {"business_iq": 99, "critical_thinking_iq": 98, "sales_iq": 95, "leadership_iq": 90}, "low", "vertical_differentiation_moat"),
            ("C", "Surrender immediately and declare bankruptcy on day one.", {"business_iq": 20, "leadership_iq": 20, "critical_thinking_iq": 25, "problem_solving_iq": 20}, "high", "instant_surrender"),
            ("D", "Run smear ads claiming the competitor's executives are aliens.", {"communication_iq": 10, "ethics_judgment_iq": 10, "marketing_iq": 15, "eq": 15}, "high", "bizarre_defamation")
        ],
        {"business_iq": 45, "critical_thinking_iq": 30, "sales_iq": 15, "leadership_iq": 10},
        50,
        "Never fight a capital war on a subsidized giant's terms: retreat from commodity pricing and construct unassailable vertical integration moats.",
        "Counter subsidized horizontal competitors with deep vertical specialization and irreplaceable workflow integration.",
        ["Executive", "Strategy", "Finance", "Sales"]
    ))

    # Q100: Executive - Legacy & Stewardship / SarlaYash Mission Vision
    questions.append(make_q(
        100, 5, "Leadership",
        "As you reflect on the totality of your leadership legacy and institution-building journey, what foundational philosophy best encapsulates enduring organizational excellence?",
        "What philosophy anchors your leadership legacy?",
        [
            ("A", "Maximalist extraction: extract every possible dollar from customers and employees as fast as possible.", {"ethics_judgment_iq": 15, "leadership_iq": 20, "business_iq": 25, "eq": 20}, "high", "predatory_extraction"),
            ("B", "A Legacy of Values and the Future of Learning: building institutions anchored in unwavering integrity, relentless curiosity, empowering human potential, and creating compounding value for generations.", {"leadership_iq": 100, "ethics_judgment_iq": 100, "learning_agility_iq": 100, "eq": 98}, "low", "enduring_stewardship_legacy"),
            ("C", "Risk avoidance: keeping everything completely stagnant so nothing ever goes wrong.", {"leadership_iq": 35, "adaptability_iq": 30, "creativity_iq": 30, "business_iq": 35}, "moderate", "stagnant_timidity"),
            ("D", "Personal glorification: ensuring your statue is placed in the lobby and your name is on every building.", {"leadership_iq": 30, "eq": 25, "ethics_judgment_iq": 30, "communication_iq": 35}, "high", "narcissistic_monument")
        ],
        {"leadership_iq": 40, "ethics_judgment_iq": 30, "learning_agility_iq": 20, "eq": 10},
        50,
        "True greatness in leadership is measured not by personal monuments, but by the resilience of the values and human growth left in your wake.",
        "SarlaYash Mission: Legacy of Values. Future of Learning. Measure how you think, work, adapt, and grow.",
        ["All"]
    ))

    return questions

if __name__ == "__main__":
    qs = get_level4_part2_and_level5()
    print(f"Loaded {len(qs)} questions for Level 4 part 2 and Level 5")
