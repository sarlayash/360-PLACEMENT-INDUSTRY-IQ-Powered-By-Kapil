// 360° PLACEMENT & INDUSTRY IQ - Comprehensive Scoring & Intelligence Engine
// Powered by SarlaYash Mission - Legacy Of Values. Future Of Learning.

(function(global) {
    const DOMAIN_DEFINITIONS = [
        { id: "iq", name: "IQ", color: "#2563eb", rgb: "37, 99, 235", icon: "🧠", summary: "Logical reasoning, pattern recognition, and structured thinking." },
        { id: "eq", name: "EQ", color: "#ec4899", rgb: "236, 72, 153", icon: "❤️", summary: "Emotional awareness, empathy, and emotional regulation." },
        { id: "aiq", name: "AIQ", color: "#06b6d4", rgb: "6, 182, 212", icon: "🤖", summary: "Ability to understand, evaluate, and responsibly use AI." },
        { id: "programming_iq", name: "Programming IQ", color: "#8b5cf6", rgb: "139, 92, 246", icon: "💻", summary: "Algorithmic thinking, debugging, and computational reasoning." },
        { id: "problem_solving_iq", name: "Problem-Solving IQ", color: "#f97316", rgb: "249, 115, 22", icon: "🧩", summary: "Ability to break complex problems into actionable solutions." },
        { id: "communication_iq", name: "Communication IQ", color: "#eab308", rgb: "234, 179, 8", icon: "🗣️", summary: "Clarity, listening, written and verbal communication." },
        { id: "critical_thinking_iq", name: "Critical Thinking IQ", color: "#4f46e5", rgb: "79, 70, 229", icon: "🔍", summary: "Evidence evaluation, assumptions, bias detection, and reasoning." },
        { id: "creativity_iq", name: "Creativity IQ", color: "#d946ef", rgb: "217, 70, 239", icon: "💡", summary: "Original thinking, alternative approaches, and innovation." },
        { id: "adaptability_iq", name: "Adaptability IQ", color: "#14b8a6", rgb: "20, 184, 166", icon: "🌊", summary: "Response to changing requirements, technologies, and environments." },
        { id: "job_readiness_iq", name: "Job Readiness IQ", color: "#22c55e", rgb: "34, 197, 94", icon: "💼", summary: "Professional preparedness and workplace behaviour." },
        { id: "interview_iq", name: "Interview IQ", color: "#3b82f6", rgb: "59, 130, 246", icon: "🎙️", summary: "Interview decision-making, communication, and professional presentation." },
        { id: "sales_iq", name: "Sales IQ", color: "#ef4444", rgb: "239, 68, 68", icon: "📈", summary: "Customer understanding, objection handling, value creation, and negotiation." },
        { id: "marketing_iq", name: "Marketing IQ", color: "#fb923c", rgb: "251, 146, 60", icon: "📣", summary: "Audience understanding, positioning, messaging, and experimentation." },
        { id: "leadership_iq", name: "Leadership IQ", color: "#eab308", rgb: "234, 179, 8", icon: "👑", summary: "Ownership, delegation, conflict management, and team development." },
        { id: "teamwork_iq", name: "Teamwork IQ", color: "#10b981", rgb: "16, 185, 129", icon: "🤝", summary: "Collaboration, accountability, trust, and conflict resolution." },
        { id: "time_priority_iq", name: "Time & Priority IQ", color: "#7c3aed", rgb: "124, 58, 237", icon: "⏱️", summary: "Prioritisation, deadlines, trade-offs, and workload management." },
        { id: "business_iq", name: "Business IQ", color: "#1e40af", rgb: "30, 64, 175", icon: "🏢", summary: "Understanding of customers, costs, value, risk, and business outcomes." },
        { id: "promotion_readiness_iq", name: "Promotion Readiness IQ", color: "#f59e0b", rgb: "245, 158, 11", icon: "🚀", summary: "Strategic thinking, ownership, influence, maturity, and business impact." },
        { id: "learning_agility_iq", name: "Learning Agility IQ", color: "#2dd4bf", rgb: "45, 212, 191", icon: "🌱", summary: "Ability to learn, unlearn, relearn, and apply new knowledge." },
        { id: "ethics_judgment_iq", name: "Ethics & Professional Judgment IQ", color: "#94a3b8", rgb: "148, 163, 184", icon: "⚖️", summary: "Integrity, confidentiality, responsible behaviour, and compliance." }
    ];

    function getDomainMeta(dimId) {
        return DOMAIN_DEFINITIONS.find(d => d.id === dimId) || {
            id: dimId, name: dimId, color: "#64748b", rgb: "100, 116, 139", icon: "📌", summary: ""
        };
    }

    function getBand(score) {
        if (score >= 90) return { band: "Exceptional Readiness", code: "exceptional", color: "#10b981", badge: "🟢" };
        if (score >= 80) return { band: "Advanced Readiness", code: "advanced", color: "#3b82f6", badge: "🔵" };
        if (score >= 70) return { band: "Strong Readiness", code: "strong", color: "#8b5cf6", badge: "🟣" };
        if (score >= 60) return { band: "Developing Readiness", code: "developing", color: "#f59e0b", badge: "🟡" };
        if (score >= 50) return { band: "Foundation Stage", code: "foundation", color: "#f97316", badge: "🟠" };
        return { band: "Priority Development Area", code: "priority", color: "#ef4444", badge: "🔴" };
    }

    function getWeatherStatus(score) {
        if (score >= 80) return { label: "Strong", icon: "🟢", color: "#10b981", desc: "Solid autonomous capability; a core professional asset." };
        if (score >= 65) return { label: "Developing", icon: "🟡", color: "#f59e0b", desc: "Good baseline instinct; requires targeted practice." };
        if (score >= 50) return { label: "Watch", icon: "🟠", color: "#f97316", desc: "Inconsistent under pressure; high risk of friction." };
        return { label: "Priority Development", icon: "🔴", color: "#ef4444", desc: "Core gap requiring deliberate 30-day intervention." };
    }

    // Career Stage Titles (Section 20)
    function getCareerProfileTitle(stage) {
        const s = (stage || "").toLowerCase();
        if (s.includes("school") || s.includes("college") || s.includes("student")) return "Career Foundation Profile";
        if (s.includes("intern")) return "Professional Launch Profile";
        if (s.includes("fresher")) return "Job Readiness Profile";
        if (s.includes("manager")) return "Leadership & Promotion Profile";
        if (s.includes("entrepreneur") || s.includes("founder")) return "Founder & Business Readiness Profile";
        return "Professional Growth Profile";
    }

    class ScoringEngine {
        // Main assessment evaluation
        static evaluateAssessment(userProfile, questions, answers, timeLogs, microScenarioAnswers) {
            // answers: { [qId]: 'A' | 'B' | 'C' | 'D' }
            // timeLogs: { [qId]: secondsTaken }
            // microScenarioAnswers: { [qId]: 'A' | 'B' | 'C' }

            const domainAcc = {};
            DOMAIN_DEFINITIONS.forEach(d => {
                domainAcc[d.id] = { totalPoints: 0, maxPossible: 0, count: 0 };
            });

            let riskChoices = { low: 0, moderate: 0, high: 0 };
            let optionFrequency = { A: 0, B: 0, C: 0, D: 0 };
            let totalTime = 0;
            let fastestTime = 9999;
            let slowestTime = 0;
            let rapidAnswersCount = 0;
            let hesitationCount = 0;
            let microScenarioConsistencyHits = 0;
            let microScenariosAttempted = 0;

            questions.forEach(q => {
                const choiceKey = answers[q.id];
                if (!choiceKey) return;

                optionFrequency[choiceKey] = (optionFrequency[choiceKey] || 0) + 1;
                const chosenOpt = q.options.find(o => o.key === choiceKey);
                if (!chosenOpt) return;

                // Risk tracking
                if (chosenOpt.risk) {
                    riskChoices[chosenOpt.risk] = (riskChoices[chosenOpt.risk] || 0) + 1;
                }

                // Time tracking
                const t = timeLogs[q.id] || q.timeRecommendation || 30;
                totalTime += t;
                if (t < fastestTime) fastestTime = t;
                if (t > slowestTime) slowestTime = t;
                if (t < 5) rapidAnswersCount++;
                if (t > (q.timeRecommendation * 1.8)) hesitationCount++;

                // Difficulty factor: 1.0, 1.1, 1.2, 1.3, 1.4
                const diffFactor = 1.0 + (q.difficulty - 1) * 0.1;

                // Multidimensional scoring accumulation
                const weights = q.dimensionWeights;
                for (let dim in weights) {
                    const weightVal = weights[dim];
                    // Score from chosen option
                    let optScore = (chosenOpt.scores && chosenOpt.scores[dim] !== undefined)
                        ? chosenOpt.scores[dim]
                        : (chosenOpt.scores && chosenOpt.scores[dim.replace('_iq', '')] !== undefined)
                            ? chosenOpt.scores[dim.replace('_iq', '')]
                            : 70; // safe default baseline

                    const weightedScore = (weightVal * optScore * diffFactor);
                    const maxWeight = (weightVal * 100 * diffFactor);

                    if (domainAcc[dim]) {
                        domainAcc[dim].totalPoints += weightedScore;
                        domainAcc[dim].maxPossible += maxWeight;
                        domainAcc[dim].count++;
                    }
                }

                // Micro-scenario consistency evaluation
                if (q.microScenario && microScenarioAnswers[q.id]) {
                    microScenariosAttempted++;
                    const msChoice = microScenarioAnswers[q.id];
                    const msOpt = q.microScenario.followUpOptions.find(o => o.key === msChoice);
                    if (msOpt && msOpt.score >= 80) {
                        microScenarioConsistencyHits++;
                    }
                }
            });

            // 1. Calculate normalized 0-100 scores for every 20 dimensions
            const domainScores = {};
            DOMAIN_DEFINITIONS.forEach(d => {
                const acc = domainAcc[d.id];
                let rawNorm = acc.maxPossible > 0 ? (acc.totalPoints / acc.maxPossible) * 100 : 70;
                // Add contextual factor based on stage/experience without changing core competency
                rawNorm = Math.min(100, Math.max(30, Math.round(rawNorm)));
                domainScores[d.id] = rawNorm;
            });

            // 2. Anti-Gaming Engine Indicators (Hidden Indicators, Section 9)
            const answeredCount = Object.keys(answers).length;
            const maxOptionRepeated = Math.max(...Object.values(optionFrequency));
            const repeatRatio = answeredCount > 0 ? maxOptionRepeated / answeredCount : 0;
            
            // Consistency score
            let consistencyScore = 88;
            if (repeatRatio > 0.45) consistencyScore -= 20; // pattern repeating
            if (rapidAnswersCount > (answeredCount * 0.25)) consistencyScore -= 25; // rushing
            if (microScenariosAttempted > 0) {
                const msRate = microScenarioConsistencyHits / microScenariosAttempted;
                consistencyScore = Math.round(consistencyScore * 0.7 + (msRate * 100) * 0.3);
            }
            consistencyScore = Math.min(98, Math.max(45, consistencyScore));

            // Authenticity score (tests social desirability bias vs pragmatic realism)
            let authenticityScore = 90;
            const safeChoiceRatio = answeredCount > 0 ? riskChoices.low / answeredCount : 0.5;
            if (safeChoiceRatio > 0.85) authenticityScore -= 18; // safe answer bias / halo effect
            if (rapidAnswersCount > 10) authenticityScore -= 15;
            authenticityScore = Math.min(99, Math.max(50, authenticityScore));

            // Decision Stability
            let decisionStability = "High Stability";
            if (consistencyScore < 65) decisionStability = "Dynamic / Context-Shifting";
            else if (consistencyScore < 80) decisionStability = "Adaptive Stability";

            // Risk Orientation
            let riskOrientation = "Balanced & Calculated";
            if (riskChoices.high > riskChoices.low) riskOrientation = "Bold / Innovation-Oriented";
            else if (riskChoices.low > (answeredCount * 0.7)) riskOrientation = "Prudent & Risk-Averse";

            // Response Confidence
            let responseConfidence = "High Executive Confidence";
            if (hesitationCount > (answeredCount * 0.35)) responseConfidence = "Deliberative / Reflective";
            else if (rapidAnswersCount > (answeredCount * 0.35)) responseConfidence = "Rapid Intuitive";

            // Anti-gaming respectful language
            let antiGamingInsight = "Your response pattern demonstrates authentic professional pragmatism, reflecting real-world prioritization over idealized textbook answers.";
            if (safeChoiceRatio > 0.8) {
                antiGamingInsight = "Your response pattern suggests a preference for conservative, high-safety decisions. Cultivating calculated risk-taking will expand your strategic agility.";
            } else if (repeatRatio > 0.45) {
                antiGamingInsight = "Your response pattern suggests consistent structural decision heuristics across diverse operational dilemmas.";
            }

            // 3. Time Intelligence (Section 10)
            const avgResponseTime = answeredCount > 0 ? Math.round(totalTime / answeredCount) : 35;
            // Decision Speed Index (0-100: balanced sweet spot around 25-45s is optimal, rushed or extreme hesitation scaled thoughtfully)
            let speedIndex = 85;
            if (avgResponseTime < 12) speedIndex = 65; // too fast
            else if (avgResponseTime >= 20 && avgResponseTime <= 45) speedIndex = 95; // optimal thoughtful cadence
            else if (avgResponseTime > 75) speedIndex = 72; // deep deliberation

            const timeIntelligence = {
                totalTimeSeconds: totalTime,
                averageResponseTime: avgResponseTime,
                fastestResponse: fastestTime === 9999 ? 0 : fastestTime,
                slowestResponse: slowestTime,
                decisionHesitationCount: hesitationCount,
                decisionSpeedIndex: speedIndex,
                pacingAssessment: avgResponseTime < 15 ? "Fast, intuitive pacing" : (avgResponseTime <= 45 ? "Optimal professional cadence" : "Deep analytical deliberation")
            };

            // 4. Master 5 Readiness Pillars (Section 19)
            const cognitiveReadiness = Math.round(
                (domainScores.iq * 0.25) +
                (domainScores.critical_thinking_iq * 0.35) +
                (domainScores.problem_solving_iq * 0.25) +
                (domainScores.learning_agility_iq * 0.15)
            );

            const peopleReadiness = Math.round(
                (domainScores.eq * 0.30) +
                (domainScores.communication_iq * 0.30) +
                (domainScores.teamwork_iq * 0.20) +
                (domainScores.leadership_iq * 0.20)
            );

            const digitalReadiness = Math.round(
                (domainScores.aiq * 0.45) +
                (domainScores.programming_iq * 0.30) +
                (domainScores.adaptability_iq * 0.25)
            );

            const professionalReadiness = Math.round(
                (domainScores.job_readiness_iq * 0.30) +
                (domainScores.ethics_judgment_iq * 0.35) +
                (domainScores.time_priority_iq * 0.20) +
                (domainScores.interview_iq * 0.15)
            );

            const growthReadiness = Math.round(
                (domainScores.promotion_readiness_iq * 0.30) +
                (domainScores.business_iq * 0.30) +
                (domainScores.creativity_iq * 0.20) +
                (domainScores.sales_iq * 0.10) +
                (domainScores.marketing_iq * 0.10)
            );

            // Master Industry Readiness Index (0-100)
            const industryReadinessIndex = Math.round(
                (cognitiveReadiness * 0.22) +
                (peopleReadiness * 0.22) +
                (digitalReadiness * 0.18) +
                (professionalReadiness * 0.20) +
                (growthReadiness * 0.18)
            );

            // 5. Strengths & Development Areas Ranking (Sections 23 & 24)
            const sortedDomains = DOMAIN_DEFINITIONS.map(d => ({
                id: d.id,
                name: d.name,
                score: domainScores[d.id],
                band: getBand(domainScores[d.id]),
                weather: getWeatherStatus(domainScores[d.id]),
                color: d.color,
                icon: d.icon,
                summary: d.summary
            })).sort((a, b) => b.score - a.score);

            const top5Strengths = sortedDomains.slice(0, 5).map(s => {
                let why = "Demonstrates consistent high-order judgment across complex scenario trade-offs.";
                if (s.id === "critical_thinking_iq") why = "Frequently detected confounding variables, questioned superficial correlations, and demanded empirical verification.";
                else if (s.id === "leadership_iq") why = "Consistently prioritized team empowerment, objective decision frameworks, and accountability over autocratic control.";
                else if (s.id === "ethics_judgment_iq") why = "Maintained uncompromising fidelity to statutory compliance, confidentiality, and human dignity under intense pressure.";
                else if (s.id === "adaptability_iq") why = "Rapidly salvaged value from disrupted requirements and pivoted with structural poise.";
                else if (s.id === "communication_iq") why = "Selected transparent, audience-calibrated executive synthesis over defensive justification.";
                else if (s.id === "aiq") why = "Balanced proactive tool adoption with rigorous human-in-the-loop verification and guardrails.";
                else if (s.id === "business_iq") why = "Anchored operational choices to unit economics, customer lifetime value, and cost of delay.";
                return { ...s, why };
            });

            const top5Developments = sortedDomains.slice(-5).reverse().map(d => {
                return {
                    ...d,
                    whyItMatters: `Elevating ${d.name} removes a key friction point in cross-functional collaboration and career progression.`,
                    workplaceImpact: `In high-pressure situations, gaps here lead to delayed alignment, miscommunicated trade-offs, or reactive decisions.`,
                    practicalAction: `Integrate structured frameworks (e.g. Minto Pyramid, pre-mortems, or unit economics logs) before executing deliverables.`,
                    plan7Day: `Audit 3 recent work decisions through this competency lens and identify one alternative course of action.`,
                    plan30Day: `Lead a small cross-functional initiative or mini-project applying these principles, seeking feedback from a senior mentor.`
                };
            });

            // 6. Professional DNA (Section 30)
            // Archetypes: The Structured Problem Solver, The Adaptive Builder, The Strategic Communicator, The Analytical Operator, The People-Centric Leader, The Curious Explorer
            const dnaProfiles = [
                {
                    name: "The Structured Problem Solver",
                    match: (domainScores.problem_solving_iq + domainScores.critical_thinking_iq + domainScores.iq) / 3,
                    tagline: "Excels in breaking chaotic ambiguity into systematic, hypothesis-driven execution frameworks.",
                    traits: ["Rigorous Decomposition", "Empirical Validation", "Process Architecture"]
                },
                {
                    name: "The Adaptive Builder",
                    match: (domainScores.adaptability_iq + domainScores.creativity_iq + domainScores.learning_agility_iq) / 3,
                    tagline: "Pivots rapidly in the face of macro disruption, turning resource constraints into creative engines.",
                    traits: ["Resilience Under Ambiguity", "Rapid Prototyping", "Continuous Unlearning"]
                },
                {
                    name: "The Strategic Communicator",
                    match: (domainScores.communication_iq + domainScores.sales_iq + domainScores.marketing_iq) / 3,
                    tagline: "Translates technical and operational complexity into compelling, high-conviction human alignment.",
                    traits: ["Executive Presence", "Influence Without Authority", "Stakeholder Empathy"]
                },
                {
                    name: "The People-Centric Leader",
                    match: (domainScores.leadership_iq + domainScores.eq + domainScores.teamwork_iq) / 3,
                    tagline: "Cultivates deep psychological safety, mentors multipliers, and mediates high-stakes conflict with grace.",
                    traits: ["Cultural Stewardship", "Talent Magnetism", "Principled Empathy"]
                },
                {
                    name: "The Analytical Operator",
                    match: (domainScores.business_iq + domainScores.time_priority_iq + domainScores.job_readiness_iq) / 3,
                    tagline: "Relentlessly executes on unit economics, operational rhythm, and long-term capital discipline.",
                    traits: ["Fiduciary Rigor", "Execution Cadence", "Risk Containment"]
                },
                {
                    name: "The Curious Explorer",
                    match: (domainScores.aiq + domainScores.learning_agility_iq + domainScores.programming_iq) / 3,
                    tagline: "Stands on the technological frontier, pioneering agentic automation with principled foresight.",
                    traits: ["Frontier Tech Fluency", "Intellectual Humility", "Systems Experimentation"]
                }
            ].sort((a, b) => b.match - a.match);

            const professionalDNA = {
                primary: dnaProfiles[0],
                secondary: dnaProfiles[1],
                supporting: dnaProfiles.slice(2, 4),
                disclaimer: "This represents an assessment profile of observed decision-making heuristics, not a psychological or personality diagnosis."
            };

            // 7. Career Simulation (Section 25)
            const careerSimulation = {
                label: "Simulation based on assessment responses — not a prediction.",
                first30Days: {
                    strengths: `You will rapidly establish credibility in ${top5Strengths[0].name} and ${top5Strengths[1].name}, establishing structured habits and delivering early project wins.`,
                    challenges: `You may face slight hesitation when negotiating ambiguous boundaries in ${top5Developments[0].name}, requiring deliberate check-ins with your manager.`
                },
                first90Days: {
                    opportunities: `Cross-functional stakeholders will value your ${top5Strengths[2].name}. As project scope widens, actively practicing ${top5Developments[1].name} will prevent operational bottlenecks.`
                },
                first6Months: {
                    growthSignals: `Strong trajectory toward autonomy and team force multiplication; high potential to lead complex cross-vertical initiatives as you master ${top5Developments[0].name}.`
                }
            };

            // 8. Specialized Reports (Sections 26, 27, 28)
            const jobReadinessReport = {
                interviewReadiness: domainScores.interview_iq,
                resumeReadiness: Math.round((domainScores.job_readiness_iq + domainScores.communication_iq) / 2),
                communicationReadiness: domainScores.communication_iq,
                workplaceBehaviour: domainScores.job_readiness_iq,
                problemSolving: domainScores.problem_solving_iq,
                professionalism: domainScores.ethics_judgment_iq,
                learningAgility: domainScores.learning_agility_iq,
                aiReadiness: domainScores.aiq,
                teamReadiness: domainScores.teamwork_iq
            };

            const promotionReadinessReport = {
                ownership: domainScores.leadership_iq,
                strategicThinking: domainScores.critical_thinking_iq,
                businessImpact: domainScores.business_iq,
                influence: domainScores.communication_iq,
                leadership: domainScores.leadership_iq,
                delegation: Math.round((domainScores.leadership_iq + domainScores.time_priority_iq) / 2),
                communication: domainScores.communication_iq,
                decisionMaking: domainScores.problem_solving_iq,
                stakeholderManagement: Math.round((domainScores.communication_iq + domainScores.eq) / 2),
                learningAgility: domainScores.learning_agility_iq,
                verdict: "Your responses indicate strong signals in systemic leadership and strategic problem solving, positioning you well for broader scope."
            };

            const aiReadinessReport = {
                aiToolAwareness: domainScores.aiq,
                aiJudgement: Math.round((domainScores.aiq * 0.6) + (domainScores.critical_thinking_iq * 0.4)),
                promptThinking: Math.round((domainScores.aiq * 0.5) + (domainScores.communication_iq * 0.5)),
                verificationBehaviour: Math.round((domainScores.critical_thinking_iq * 0.6) + (domainScores.aiq * 0.4)),
                automationMindset: Math.round((domainScores.problem_solving_iq * 0.5) + (domainScores.aiq * 0.5)),
                aiEthics: Math.round((domainScores.ethics_judgment_iq * 0.6) + (domainScores.aiq * 0.4)),
                humanAiCollaboration: Math.round((domainScores.aiq * 0.5) + (domainScores.adaptability_iq * 0.5)),
                overallScore: domainScores.aiq
            };

            // 9. Industry Transferability (Section 29)
            const transferableSkillsIndex = {
                technology: Math.round((domainScores.programming_iq * 0.3) + (domainScores.aiq * 0.3) + (domainScores.problem_solving_iq * 0.4)),
                finance: Math.round((domainScores.business_iq * 0.4) + (domainScores.critical_thinking_iq * 0.3) + (domainScores.ethics_judgment_iq * 0.3)),
                healthcare: Math.round((domainScores.ethics_judgment_iq * 0.35) + (domainScores.eq * 0.35) + (domainScores.problem_solving_iq * 0.3)),
                education: Math.round((domainScores.learning_agility_iq * 0.4) + (domainScores.communication_iq * 0.4) + (domainScores.eq * 0.2)),
                sales: Math.round((domainScores.sales_iq * 0.45) + (domainScores.communication_iq * 0.3) + (domainScores.eq * 0.25)),
                marketing: Math.round((domainScores.marketing_iq * 0.45) + (domainScores.creativity_iq * 0.3) + (domainScores.business_iq * 0.25)),
                operations: Math.round((domainScores.time_priority_iq * 0.4) + (domainScores.problem_solving_iq * 0.3) + (domainScores.business_iq * 0.3)),
                management: Math.round((domainScores.leadership_iq * 0.4) + (domainScores.business_iq * 0.3) + (domainScores.promotion_readiness_iq * 0.3)),
                entrepreneurship: Math.round((domainScores.business_iq * 0.3) + (domainScores.adaptability_iq * 0.3) + (domainScores.creativity_iq * 0.2) + (domainScores.sales_iq * 0.2)),
                averageTransferability: 0
            };
            const sumTrans = Object.values(transferableSkillsIndex).reduce((a, b) => a + b, 0);
            transferableSkillsIndex.averageTransferability = Math.round(sumTrans / (Object.keys(transferableSkillsIndex).length - 1));

            // Unique Assessment ID (Section 36)
            const randomCode = Math.random().toString(36).substring(2, 8).toUpperCase();
            const currentYear = new Date().getFullYear();
            const assessmentId = `SY-360-IQ-${currentYear}-${randomCode}`;

            return {
                id: assessmentId,
                date: new Date().toISOString(),
                userProfile: { ...userProfile },
                profileTitle: getCareerProfileTitle(userProfile.currentStage),
                industryReadinessIndex,
                pillars: {
                    cognitiveReadiness,
                    peopleReadiness,
                    digitalReadiness,
                    professionalReadiness,
                    growthReadiness
                },
                domainScores,
                sortedDomains,
                top5Strengths,
                top5Developments,
                professionalDNA,
                careerSimulation,
                jobReadinessReport,
                promotionReadinessReport,
                aiReadinessReport,
                transferableSkillsIndex,
                antiGaming: {
                    consistencyScore,
                    authenticityScore,
                    decisionStability,
                    riskOrientation,
                    responseConfidence,
                    behaviouralConsistency: consistencyScore >= 80 ? "High Fidelity" : "Developing Consistency",
                    insight: antiGamingInsight
                },
                timeIntelligence,
                questionsCount: answeredCount,
                answers: { ...answers },
                timeLogs: { ...timeLogs }
            };
        }
    }

    global.DOMAIN_DEFINITIONS = DOMAIN_DEFINITIONS;
    global.getDomainMeta = getDomainMeta;
    global.getBand = getBand;
    global.getWeatherStatus = getWeatherStatus;
    global.getCareerProfileTitle = getCareerProfileTitle;
    global.ScoringEngine = ScoringEngine;
})(window);
