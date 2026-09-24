// 360° PLACEMENT & INDUSTRY IQ - Master Application Controller
// Powered by SarlaYash Mission - Legacy Of Values. Future Of Learning.

(function(global) {
    class AppController {
        constructor() {
            this.allQuestions = [];
            this.activeQuestions = [];
            this.currentIndex = 0;
            this.userProfile = {
                name: '',
                ageGroup: '18-21',
                currentStage: 'College Student',
                domain: 'Technology',
                experience: '0'
            };
            this.answers = {}; // { [qId]: 'A' | 'B' | 'C' | 'D' }
            this.timeLogs = {}; // { [qId]: seconds }
            this.microAnswers = {}; // { [qId]: 'A' | 'B' | 'C' }
            this.activeTrackType = 'full'; // 'full' | 'domain' | 'level'
            this.currentReport = null;

            // Timer tracking
            this.questionStartTime = Date.now();
            this.timerInterval = null;
            this.elapsedSeconds = 0;

            // Settings
            this.settings = global.StorageEngine.getSettings();
            this.deferredPrompt = null;
        }

        init() {
            // Load questions dataset
            if (window.QUESTIONS_DATA && Array.isArray(window.QUESTIONS_DATA)) {
                this.allQuestions = window.QUESTIONS_DATA;
            } else {
                console.error("QUESTIONS_DATA not found");
            }

            // Restore saved profile if any
            const savedProfile = global.StorageEngine.getSavedProfile();
            if (savedProfile) {
                this.userProfile = { ...this.userProfile, ...savedProfile };
                this.populateProfileFields();
            }

            // Apply settings
            this.applyTheme(this.settings.theme);
            this.applyTextSize(this.settings.textSize);
            this.setupEventListeners();
            this.setupPWA();

            // Check if there is an existing latest report
            const history = global.StorageEngine.getHistory();
            if (history.length > 0) {
                const reportBtn = document.getElementById('btn-nav-my-report');
                if (reportBtn) reportBtn.classList.remove('hidden');
            }

            // Trigger domain advisor preview if profile already filled
            if (this.userProfile.name && this.userProfile.domain) {
                this.updateAdvisorPreview();
            }
        }

        populateProfileFields() {
            const nameInput = document.getElementById('input-user-name');
            const ageSelect = document.getElementById('select-age-group');
            const stageSelect = document.getElementById('select-current-stage');
            const domainSelect = document.getElementById('select-domain');
            const expSelect = document.getElementById('select-experience');

            if (nameInput) nameInput.value = this.userProfile.name || '';
            if (ageSelect) ageSelect.value = this.userProfile.ageGroup || '18-21';
            if (stageSelect) stageSelect.value = this.userProfile.currentStage || 'College Student';
            if (domainSelect) domainSelect.value = this.userProfile.domain || 'Technology';
            if (expSelect) expSelect.value = this.userProfile.experience || '0';
        }

        readProfileFromDOM() {
            const nameInput = document.getElementById('input-user-name');
            const ageSelect = document.getElementById('select-age-group');
            const stageSelect = document.getElementById('select-current-stage');
            const domainSelect = document.getElementById('select-domain');
            const expSelect = document.getElementById('select-experience');

            this.userProfile.name = (nameInput ? nameInput.value.trim() : '') || 'Candidate';
            this.userProfile.ageGroup = ageSelect ? ageSelect.value : '18-21';
            this.userProfile.currentStage = stageSelect ? stageSelect.value : 'College Student';
            this.userProfile.domain = domainSelect ? domainSelect.value : 'Technology';
            this.userProfile.experience = expSelect ? expSelect.value : '0';

            global.StorageEngine.saveProfile(this.userProfile);
        }

        // Domain Advisor (Sections 1 & 16)
        updateAdvisorPreview() {
            this.readProfileFromDOM();
            const advisorBox = document.getElementById('advisor-recommendation-box');
            if (!advisorBox) return;

            const domain = this.userProfile.domain;
            const stage = this.userProfile.currentStage;

            let recTitle = "";
            let recDesc = "";
            let priorityDomains = [];

            if (domain === "Technology") {
                recTitle = "Technology & Systems Architecture Track";
                recDesc = "Tailored for software engineering, system architecture, data analysis, and technical product workflows.";
                priorityDomains = ["Programming IQ", "AIQ", "Problem-Solving IQ", "Critical Thinking IQ", "Adaptability IQ"];
            } else if (domain === "Finance" || domain === "Banking") {
                recTitle = "Capital Allocation & Fiduciary Risk Track";
                recDesc = "Focuses on capital modeling, regulatory governance, risk trade-offs, and client fiduciary alignment.";
                priorityDomains = ["Business IQ", "Critical Thinking IQ", "Ethics IQ", "IQ", "Time & Priority IQ"];
            } else if (domain === "Marketing" || domain === "Sales") {
                recTitle = "Commercial Growth & Brand Strategy Track";
                recDesc = "Designed for client discovery, conversion funnel optimization, negotiation, and market positioning.";
                priorityDomains = ["Sales IQ", "Marketing IQ", "Communication IQ", "Creativity IQ", "EQ"];
            } else if (domain === "Healthcare") {
                recTitle = "Clinical Operations & Patient Trust Track";
                recDesc = "Calibrated for mission-critical care delivery, patient privacy, ethics, and emergency team triage.";
                priorityDomains = ["Ethics IQ", "EQ", "Problem-Solving IQ", "Teamwork IQ", "Critical Thinking IQ"];
            } else {
                recTitle = "Enterprise Leadership & Operations Track";
                recDesc = "Comprehensive scenario evaluation for cross-functional management, operational logistics, and strategy.";
                priorityDomains = ["Leadership IQ", "Teamwork IQ", "Communication IQ", "Business IQ", "Time & Priority IQ"];
            }

            advisorBox.innerHTML = `
                <div class="advisor-card">
                    <div class="advisor-badge">🎯 Advisor Recommendation for ${this.userProfile.name}</div>
                    <h3 class="advisor-title">${recTitle}</h3>
                    <p class="advisor-desc">${recDesc}</p>
                    <div class="advisor-priority-tags">
                        <strong>Target Competencies:</strong>
                        <div class="tag-row">
                            ${priorityDomains.map(d => `<span class="adv-tag">${d}</span>`).join('')}
                        </div>
                    </div>
                    <div class="advisor-actions">
                        <button type="button" class="btn btn-primary" id="btn-start-domain-track">
                            🚀 Launch Recommended ${domain} Track (30 Decisions)
                        </button>
                        <button type="button" class="btn btn-accent" id="btn-start-full-track">
                            ⭐ Take Master 360° Comprehensive (Full 100 Decisions)
                        </button>
                    </div>
                </div>
            `;

            document.getElementById('btn-start-domain-track')?.addEventListener('click', () => {
                this.startAssessment('domain');
            });
            document.getElementById('btn-start-full-track')?.addEventListener('click', () => {
                this.startAssessment('full');
            });
        }

        startAssessment(trackType = 'full') {
            this.readProfileFromDOM();
            this.activeTrackType = trackType;
            this.currentIndex = 0;
            this.answers = {};
            this.timeLogs = {};
            this.microAnswers = {};

            if (trackType === 'domain') {
                // Filter questions relevant to the user's domain and general competencies
                const d = this.userProfile.domain;
                let filtered = this.allQuestions.filter(q => {
                    return q.industryTags.includes(d) || q.industryTags.includes("All") || q.industryTags.includes("Corporate");
                });
                if (filtered.length < 30) {
                    filtered = this.allQuestions.slice(0, 30);
                } else if (filtered.length > 30) {
                    filtered = filtered.slice(0, 30);
                }
                this.activeQuestions = filtered;
            } else {
                // Full 100-question comprehensive assessment
                this.activeQuestions = [...this.allQuestions];
            }

            this.showView('view-assessment');
            this.renderCurrentQuestion();
        }

        renderCurrentQuestion() {
            if (this.currentIndex < 0 || this.currentIndex >= this.activeQuestions.length) return;

            const q = this.activeQuestions[this.currentIndex];
            this.questionStartTime = Date.now();
            this.startQuestionTimer(q.timeRecommendation || 45);

            // Play question sound
            global.soundEngine.playQuestionLoaded();

            // Progress
            const currentNum = this.currentIndex + 1;
            const totalNum = this.activeQuestions.length;
            const pct = Math.round((currentNum / totalNum) * 100);

            const progressBar = document.getElementById('assessment-progress-fill');
            const progressLabel = document.getElementById('assessment-progress-label');
            if (progressBar) progressBar.style.width = `${pct}%`;
            if (progressLabel) progressLabel.innerText = `Decision ${currentNum} of ${totalNum} (${pct}%)`;

            // Difficulty Level indicator
            const levelNames = {
                1: "Level 1 — Foundation",
                2: "Level 2 — Professional",
                3: "Level 3 — Industry",
                4: "Level 4 — Advanced",
                5: "Level 5 — Executive"
            };
            const levelEl = document.getElementById('question-difficulty-badge');
            if (levelEl) {
                levelEl.innerText = levelNames[q.difficulty] || `Level ${q.difficulty}`;
            }

            // Primary Domain & Rainbow Spectrum Styling
            const primaryDim = Object.keys(q.dimensionWeights)[0] || 'problem_solving_iq';
            const domainMeta = global.getDomainMeta(primaryDim);
            const domainBadge = document.getElementById('question-domain-badge');
            if (domainBadge) {
                domainBadge.style.borderColor = domainMeta.color;
                domainBadge.style.color = domainMeta.color;
                domainBadge.innerHTML = `<span class="d-icon">${domainMeta.icon}</span> ${domainMeta.name}`;
            }

            // Scenario & Decision prompt
            const scenarioEl = document.getElementById('question-scenario-text');
            const promptEl = document.getElementById('question-decision-prompt');
            if (scenarioEl) scenarioEl.innerText = q.scenario;
            if (promptEl) promptEl.innerText = q.question;

            // Render Options (A, B, C, D)
            const optionsContainer = document.getElementById('question-options-container');
            if (optionsContainer) {
                optionsContainer.innerHTML = q.options.map(opt => {
                    const isSelected = this.answers[q.id] === opt.key;
                    return `
                        <button type="button" class="option-btn ${isSelected ? 'selected' : ''}" data-key="${opt.key}" style="--opt-accent: ${domainMeta.color};">
                            <span class="opt-key-badge">${opt.key}</span>
                            <span class="opt-text">${opt.text}</span>
                        </button>
                    `;
                }).join('');

                // Attach option click listeners
                optionsContainer.querySelectorAll('.option-btn').forEach(btn => {
                    btn.addEventListener('click', (e) => {
                        const key = btn.getAttribute('data-key');
                        this.selectOption(key);
                    });
                });
            }

            // Navigation Buttons state
            const prevBtn = document.getElementById('btn-question-prev');
            const nextBtn = document.getElementById('btn-question-next');

            if (prevBtn) {
                prevBtn.disabled = this.currentIndex === 0;
            }
            if (nextBtn) {
                const hasSelected = !!this.answers[q.id];
                nextBtn.disabled = !hasSelected;
                nextBtn.innerText = (currentNum === totalNum) ? "Complete Assessment 🎯" : "Next Decision →";
            }
        }

        selectOption(optKey) {
            const q = this.activeQuestions[this.currentIndex];
            this.answers[q.id] = optKey;

            // Log time taken
            const elapsed = Math.round((Date.now() - this.questionStartTime) / 1000);
            this.timeLogs[q.id] = elapsed;

            // Sound
            global.soundEngine.playOptionSelected();

            // Update UI selection classes
            const optionsContainer = document.getElementById('question-options-container');
            if (optionsContainer) {
                optionsContainer.querySelectorAll('.option-btn').forEach(b => {
                    if (b.getAttribute('data-key') === optKey) {
                        b.classList.add('selected');
                    } else {
                        b.classList.remove('selected');
                    }
                });
            }

            const nextBtn = document.getElementById('btn-question-next');
            if (nextBtn) nextBtn.disabled = false;

            // Check if this triggers an Adaptive Micro-Scenario (Section 11)
            if (q.microScenario && q.microScenario.triggerOption === optKey && !this.microAnswers[q.id]) {
                this.triggerMicroScenario(q);
            }
        }

        triggerMicroScenario(q) {
            const ms = q.microScenario;
            const modalEl = document.getElementById('micro-scenario-modal');
            const promptEl = document.getElementById('ms-prompt-text');
            const questionEl = document.getElementById('ms-question-text');
            const optsContainer = document.getElementById('ms-options-container');

            if (!modalEl || !promptEl || !questionEl || !optsContainer) return;

            promptEl.innerText = ms.complication;
            questionEl.innerText = ms.followUpQuestion;

            optsContainer.innerHTML = ms.followUpOptions.map(opt => `
                <button type="button" class="btn btn-secondary ms-opt-btn" data-key="${opt.key}">
                    <span class="ms-key">${opt.key}.</span> ${opt.text}
                </button>
            `).join('');

            optsContainer.querySelectorAll('.ms-opt-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const chosen = btn.getAttribute('data-key');
                    this.microAnswers[q.id] = chosen;
                    global.soundEngine.playOptionSelected();
                    modalEl.classList.remove('active');
                });
            });

            modalEl.classList.add('active');
        }

        startQuestionTimer(recSeconds) {
            if (this.timerInterval) clearInterval(this.timerInterval);
            this.elapsedSeconds = 0;
            const timerEl = document.getElementById('question-timer-display');
            if (timerEl) timerEl.innerText = `00:00 (Rec: ${recSeconds}s)`;

            this.timerInterval = setInterval(() => {
                this.elapsedSeconds++;
                const mins = String(Math.floor(this.elapsedSeconds / 60)).padStart(2, '0');
                const secs = String(this.elapsedSeconds % 60).padStart(2, '0');
                if (timerEl) {
                    timerEl.innerText = `${mins}:${secs} (Rec: ${recSeconds}s)`;
                    if (this.elapsedSeconds > recSeconds * 1.5) {
                        timerEl.classList.add('timer-warning');
                    } else {
                        timerEl.classList.remove('timer-warning');
                    }
                }
            }, 1000);
        }

        stopQuestionTimer() {
            if (this.timerInterval) {
                clearInterval(this.timerInterval);
                this.timerInterval = null;
            }
        }

        prevQuestion() {
            if (this.currentIndex > 0) {
                this.stopQuestionTimer();
                this.currentIndex--;
                this.renderCurrentQuestion();
            }
        }

        nextQuestion() {
            const q = this.activeQuestions[this.currentIndex];
            if (!this.answers[q.id]) {
                alert("Please select a decision choice before proceeding.");
                return;
            }

            this.stopQuestionTimer();

            // Milestone sound check (every 20 questions)
            if ((this.currentIndex + 1) % 20 === 0 && (this.currentIndex + 1) < this.activeQuestions.length) {
                global.soundEngine.playMilestone();
            }

            if (this.currentIndex + 1 < this.activeQuestions.length) {
                this.currentIndex++;
                this.renderCurrentQuestion();
            } else {
                this.completeAssessment();
            }
        }

        completeAssessment() {
            this.stopQuestionTimer();
            global.soundEngine.playComplete();

            // Evaluate assessment
            this.currentReport = global.ScoringEngine.evaluateAssessment(
                this.userProfile,
                this.activeQuestions,
                this.answers,
                this.timeLogs,
                this.microAnswers
            );

            // Save to LocalStorage history
            global.StorageEngine.saveAssessment(this.currentReport);

            // Show Section 44 Assessment Complete Screen
            this.showView('view-assessment-complete');
        }

        generateAndShowReport() {
            if (!this.currentReport) {
                const history = global.StorageEngine.getHistory();
                if (history.length > 0) {
                    this.currentReport = history[0];
                } else {
                    this.showView('view-home');
                    return;
                }
            }

            this.renderReportView(this.currentReport);
            this.showView('view-report');
        }

        renderReportView(report) {
            // Header Details
            document.getElementById('report-candidate-name').innerText = report.userProfile.name;
            document.getElementById('report-candidate-stage').innerText = `${report.userProfile.currentStage} • ${report.userProfile.domain}`;
            document.getElementById('report-assessment-id').innerText = report.id;
            document.getElementById('report-date').innerText = new Date(report.date).toLocaleDateString('en-US', {
                year: 'numeric', month: 'short', day: 'numeric'
            });

            // Master Industry Readiness Index
            document.getElementById('report-index-value').innerText = report.industryReadinessIndex;
            document.getElementById('report-profile-title').innerText = report.profileTitle;
            document.getElementById('report-profile-band').innerText = report.sortedDomains[0].band.band;

            // 5 Readiness Pillars
            document.getElementById('pillar-cog-score').innerText = `${report.pillars.cognitiveReadiness}/100`;
            document.getElementById('pillar-cog-bar').style.width = `${report.pillars.cognitiveReadiness}%`;

            document.getElementById('pillar-peo-score').innerText = `${report.pillars.peopleReadiness}/100`;
            document.getElementById('pillar-peo-bar').style.width = `${report.pillars.peopleReadiness}%`;

            document.getElementById('pillar-dig-score').innerText = `${report.pillars.digitalReadiness}/100`;
            document.getElementById('pillar-dig-bar').style.width = `${report.pillars.digitalReadiness}%`;

            document.getElementById('pillar-pro-score').innerText = `${report.pillars.professionalReadiness}/100`;
            document.getElementById('pillar-pro-bar').style.width = `${report.pillars.professionalReadiness}%`;

            document.getElementById('pillar-gro-score').innerText = `${report.pillars.growthReadiness}/100`;
            document.getElementById('pillar-gro-bar').style.width = `${report.pillars.growthReadiness}%`;

            // Draw SVG Radar Chart
            this.renderSVGRadar(report.domainScores);

            // Professional DNA
            document.getElementById('dna-primary-title').innerText = report.professionalDNA.primary.name;
            document.getElementById('dna-primary-tagline').innerText = report.professionalDNA.primary.tagline;
            document.getElementById('dna-traits-list').innerHTML = report.professionalDNA.primary.traits.map(t => `<li>✓ ${t}</li>`).join('');
            document.getElementById('dna-secondary-title').innerText = `${report.professionalDNA.secondary.name} — ${report.professionalDNA.secondary.tagline}`;

            // Career Weather Map (Section 31)
            const weatherGrid = document.getElementById('weather-map-grid');
            if (weatherGrid) {
                weatherGrid.innerHTML = report.sortedDomains.map(d => `
                    <div class="weather-card" style="border-left: 4px solid ${d.weather.color};">
                        <div class="w-header">
                            <span class="w-title">${d.icon} ${d.name}</span>
                            <span class="w-badge" style="background: ${d.weather.color}22; color: ${d.weather.color};">
                                ${d.weather.icon} ${d.weather.label}
                            </span>
                        </div>
                        <div class="w-score">${d.score}/100</div>
                        <div class="w-desc">${d.weather.desc}</div>
                    </div>
                `).join('');
            }

            // 20-Domain Score Cards with Rainbow Spectrum (Sections 4 & 12)
            const domainCardsGrid = document.getElementById('domain-score-cards-grid');
            if (domainCardsGrid) {
                domainCardsGrid.innerHTML = report.sortedDomains.map(d => `
                    <div class="domain-card" style="--d-color: ${d.color};">
                        <div class="dc-top">
                            <div class="dc-name">${d.icon} ${d.name}</div>
                            <div class="dc-score" style="color: ${d.color}; font-weight: 800;">${d.score}</div>
                        </div>
                        <div class="dc-bar-bg">
                            <div class="dc-bar-fill" style="width: ${d.score}%; background: ${d.color};"></div>
                        </div>
                        <div class="dc-band">${d.band.badge} ${d.band.band}</div>
                        <div class="dc-summary">${d.summary}</div>
                    </div>
                `).join('');
            }

            // Top 5 Strengths with WHY (Section 23)
            const strengthsList = document.getElementById('top-strengths-list');
            if (strengthsList) {
                strengthsList.innerHTML = report.top5Strengths.map((s, idx) => `
                    <div class="strength-card" style="border-left: 4px solid ${s.color};">
                        <div class="sc-title">
                            <strong>#${idx + 1} ${s.icon} ${s.name}</strong>
                            <span class="sc-score">${s.score}/100 &bull; ${s.band.band}</span>
                        </div>
                        <div class="sc-why"><em>Data Signal:</em> ${s.why}</div>
                    </div>
                `).join('');
            }

            // Top 5 Development Areas with 7-Day & 30-Day plans (Section 24)
            const devList = document.getElementById('top-developments-list');
            if (devList) {
                devList.innerHTML = report.top5Developments.map((d, idx) => `
                    <div class="dev-card">
                        <div class="dc-header">
                            <strong>#${idx + 1} ${d.icon} ${d.name} (${d.score}/100)</strong>
                            <span class="dc-badge">Priority Focus</span>
                        </div>
                        <p><strong>Why It Matters:</strong> ${d.whyItMatters}</p>
                        <p><strong>Workplace Impact:</strong> ${d.workplaceImpact}</p>
                        <p><strong>Action:</strong> ${d.practicalAction}</p>
                        <div class="plan-grid">
                            <div class="plan-col">
                                <strong>📅 7-Day Quick Win:</strong>
                                <div>${d.plan7Day}</div>
                            </div>
                            <div class="plan-col">
                                <strong>🎯 30-Day Mastery:</strong>
                                <div>${d.plan30Day}</div>
                            </div>
                        </div>
                    </div>
                `).join('');
            }

            // Skill Gap Bridge (Section 32)
            const bridgeEl = document.getElementById('skill-gap-bridge-container');
            if (bridgeEl && report.top5Developments.length > 0) {
                const targetArea = report.top5Developments[0];
                bridgeEl.innerHTML = `
                    <div class="bridge-flow">
                        <div class="bridge-step current">
                            <span class="step-num">01</span>
                            <span class="step-label">CURRENT</span>
                            <strong>${targetArea.score}/100</strong>
                            <p>${targetArea.name} Baseline</p>
                        </div>
                        <div class="bridge-arrow">→</div>
                        <div class="bridge-step target">
                            <span class="step-num">02</span>
                            <span class="step-label">TARGET</span>
                            <strong>85+/100</strong>
                            <p>Advanced Readiness</p>
                        </div>
                        <div class="bridge-arrow">→</div>
                        <div class="bridge-step action">
                            <span class="step-num">03</span>
                            <span class="step-label">ACTION</span>
                            <p>${targetArea.practicalAction}</p>
                        </div>
                        <div class="bridge-arrow">→</div>
                        <div class="bridge-step practice">
                            <span class="step-num">04</span>
                            <span class="step-label">PRACTICE</span>
                            <p>${targetArea.plan7Day}</p>
                        </div>
                        <div class="bridge-arrow">→</div>
                        <div class="bridge-step reassess">
                            <span class="step-num">05</span>
                            <span class="step-label">REASSESS</span>
                            <p>Retake Assessment in 30 Days</p>
                        </div>
                    </div>
                `;
            }

            // Career Simulation (Section 25)
            document.getElementById('sim-day30-strengths').innerText = report.careerSimulation.first30Days.strengths;
            document.getElementById('sim-day30-challenges').innerText = report.careerSimulation.first30Days.challenges;
            document.getElementById('sim-day90-opps').innerText = report.careerSimulation.first90Days.opportunities;
            document.getElementById('sim-month6-signals').innerText = report.careerSimulation.first6Months.growthSignals;

            // Job Readiness Report (Section 26)
            const jr = report.jobReadinessReport;
            document.getElementById('jr-interview').innerText = `${jr.interviewReadiness}/100`;
            document.getElementById('jr-resume').innerText = `${jr.resumeReadiness}/100`;
            document.getElementById('jr-comm').innerText = `${jr.communicationReadiness}/100`;
            document.getElementById('jr-workplace').innerText = `${jr.workplaceBehaviour}/100`;
            document.getElementById('jr-problem').innerText = `${jr.problemSolving}/100`;
            document.getElementById('jr-pro').innerText = `${jr.professionalism}/100`;
            document.getElementById('jr-learning').innerText = `${jr.learningAgility}/100`;
            document.getElementById('jr-ai').innerText = `${jr.aiReadiness}/100`;
            document.getElementById('jr-team').innerText = `${jr.teamReadiness}/100`;

            // Promotion Readiness Report (Section 27)
            const pr = report.promotionReadinessReport;
            document.getElementById('pr-ownership').innerText = `${pr.ownership}/100`;
            document.getElementById('pr-strategic').innerText = `${pr.strategicThinking}/100`;
            document.getElementById('pr-impact').innerText = `${pr.businessImpact}/100`;
            document.getElementById('pr-influence').innerText = `${pr.influence}/100`;
            document.getElementById('pr-leadership').innerText = `${pr.leadership}/100`;
            document.getElementById('pr-verdict').innerText = pr.verdict;

            // AI Readiness Report (Section 28)
            const air = report.aiReadinessReport;
            document.getElementById('air-overall').innerText = `${air.overallScore}/100`;
            document.getElementById('air-awareness').innerText = `${air.aiToolAwareness}/100`;
            document.getElementById('air-judgement').innerText = `${air.aiJudgement}/100`;
            document.getElementById('air-prompt').innerText = `${air.promptThinking}/100`;
            document.getElementById('air-verification').innerText = `${air.verificationBehaviour}/100`;
            document.getElementById('air-ethics').innerText = `${air.aiEthics}/100`;
            document.getElementById('air-collab').innerText = `${air.humanAiCollaboration}/100`;

            // Industry Transferability Index (Section 29)
            const tsi = report.transferableSkillsIndex;
            const tsiGrid = document.getElementById('tsi-grid');
            if (tsiGrid) {
                const industries = [
                    { name: "Technology", score: tsi.technology },
                    { name: "Finance & Banking", score: tsi.finance },
                    { name: "Healthcare & Life Sciences", score: tsi.healthcare },
                    { name: "Education & EdTech", score: tsi.education },
                    { name: "Sales & Enterprise Commerce", score: tsi.sales },
                    { name: "Marketing & Brand Media", score: tsi.marketing },
                    { name: "Operations & Supply Chain", score: tsi.operations },
                    { name: "General Management", score: tsi.management },
                    { name: "Startups & Entrepreneurship", score: tsi.entrepreneurship }
                ];
                tsiGrid.innerHTML = industries.map(ind => `
                    <div class="tsi-item">
                        <div class="tsi-header">
                            <span>${ind.name}</span>
                            <strong>${ind.score}/100</strong>
                        </div>
                        <div class="tsi-bar"><div class="tsi-fill" style="width: ${ind.score}%;"></div></div>
                    </div>
                `).join('');
            }

            // Anti-Gaming & Time Intelligence (Sections 9, 10, 11)
            document.getElementById('ag-consistency-score').innerText = `${report.antiGaming.consistencyScore}/100`;
            document.getElementById('ag-authenticity-score').innerText = `${report.antiGaming.authenticityScore}/100`;
            document.getElementById('ag-stability').innerText = report.antiGaming.decisionStability;
            document.getElementById('ag-risk').innerText = report.antiGaming.riskOrientation;
            document.getElementById('ag-confidence').innerText = report.antiGaming.responseConfidence;
            document.getElementById('ag-insight-text').innerText = report.antiGaming.insight;

            document.getElementById('ti-speed-index').innerText = `${report.timeIntelligence.decisionSpeedIndex}/100`;
            document.getElementById('ti-avg-time').innerText = `${report.timeIntelligence.averageResponseTime}s / decision`;
            document.getElementById('ti-pacing').innerText = report.timeIntelligence.pacingAssessment;

            // Generate Verification QR Code (Section 36)
            const qrContainer = document.getElementById('report-qr-code-slot');
            if (qrContainer && global.generateQRCodeSVG) {
                qrContainer.innerHTML = global.generateQRCodeSVG(
                    `https://sarlayash.org/verify?id=${report.id}&name=${encodeURIComponent(report.userProfile.name)}&score=${report.industryReadinessIndex}`,
                    140
                );
            }
        }

        // 20-Dimension Interactive SVG Radar Chart (Section 19 & 21)
        renderSVGRadar(domainScores) {
            const container = document.getElementById('radar-svg-container');
            if (!container) return;

            const size = 520;
            const center = size / 2;
            const radius = 190;
            const dims = global.DOMAIN_DEFINITIONS;
            const total = dims.length; // 20

            // Concentric rings (20%, 40%, 60%, 80%, 100%)
            let ringsSvg = '';
            [0.2, 0.4, 0.6, 0.8, 1.0].forEach(level => {
                let points = [];
                for (let i = 0; i < total; i++) {
                    const angle = (Math.PI * 2 / total) * i - (Math.PI / 2);
                    const r = radius * level;
                    const x = center + r * Math.cos(angle);
                    const y = center + r * Math.sin(angle);
                    points.push(`${x.toFixed(1)},${y.toFixed(1)}`);
                }
                ringsSvg += `<polygon points="${points.join(' ')}" fill="none" stroke="var(--border-subtle, #334155)" stroke-dasharray="${level < 1 ? '3,3' : 'none'}" stroke-width="1"/>`;
            });

            // Radial axis lines and labels
            let axesSvg = '';
            let radarPoints = [];

            for (let i = 0; i < total; i++) {
                const angle = (Math.PI * 2 / total) * i - (Math.PI / 2);
                const maxR = radius;
                const axX = center + maxR * Math.cos(angle);
                const axY = center + maxR * Math.sin(angle);

                // Axis line
                axesSvg += `<line x1="${center}" y1="${center}" x2="${axX.toFixed(1)}" y2="${axY.toFixed(1)}" stroke="var(--border-subtle, #334155)" stroke-width="0.8"/>`;

                // Calculate polygon point
                const score = domainScores[dims[i].id] || 60;
                const rScore = (score / 100) * radius;
                const ptX = center + rScore * Math.cos(angle);
                const ptY = center + rScore * Math.sin(angle);
                radarPoints.push(`${ptX.toFixed(1)},${ptY.toFixed(1)}`);

                // Label
                const labelR = radius + 28;
                const lx = center + labelR * Math.cos(angle);
                const ly = center + labelR * Math.sin(angle);
                const align = Math.abs(angle + Math.PI/2) < 0.1 || Math.abs(angle - Math.PI/2) < 0.1 
                    ? 'middle' 
                    : (lx > center ? 'start' : 'end');

                axesSvg += `
                    <text x="${lx.toFixed(1)}" y="${ly.toFixed(1)}" text-anchor="${align}" font-size="9" fill="${dims[i].color}" font-weight="600" class="radar-label" data-dim="${dims[i].id}">
                        ${dims[i].name.replace(' IQ', '')} (${score})
                    </text>
                `;
            }

            // Radar Polygon
            const polygonSvg = `
                <polygon points="${radarPoints.join(' ')}" fill="rgba(59, 130, 246, 0.25)" stroke="#3b82f6" stroke-width="2.5" class="radar-polygon"/>
            `;

            // Score Dots
            let dotsSvg = '';
            for (let i = 0; i < total; i++) {
                const angle = (Math.PI * 2 / total) * i - (Math.PI / 2);
                const score = domainScores[dims[i].id] || 60;
                const rScore = (score / 100) * radius;
                const ptX = center + rScore * Math.cos(angle);
                const ptY = center + rScore * Math.sin(angle);

                dotsSvg += `
                    <circle cx="${ptX.toFixed(1)}" cy="${ptY.toFixed(1)}" r="4.5" fill="${dims[i].color}" stroke="#ffffff" stroke-width="1.5" class="radar-dot" data-name="${dims[i].name}" data-score="${score}">
                        <title>${dims[i].name}: ${score}/100</title>
                    </circle>
                `;
            }

            container.innerHTML = `
                <svg width="100%" height="100%" viewBox="0 0 ${size} ${size}" class="radar-chart-svg">
                    ${ringsSvg}
                    ${axesSvg}
                    ${polygonSvg}
                    ${dotsSvg}
                    <circle cx="${center}" cy="${center}" r="3" fill="#94a3b8"/>
                </svg>
            `;
        }

        // Attempt History & Comparison View (Section 33 & 34)
        showHistoryView() {
            const history = global.StorageEngine.getHistory();
            const listEl = document.getElementById('history-attempts-list');
            const compSection = document.getElementById('comparison-results-section');
            if (compSection) compSection.classList.add('hidden');

            if (!listEl) return;

            if (history.length === 0) {
                listEl.innerHTML = `
                    <div class="empty-state">
                        <p>No assessment attempts recorded on this device yet.</p>
                        <button type="button" class="btn btn-primary" onclick="window.app.showView('view-home')">Take Your First Assessment</button>
                    </div>
                `;
                this.showView('view-history');
                return;
            }

            listEl.innerHTML = history.map((attempt, idx) => {
                const dateStr = new Date(attempt.date).toLocaleDateString('en-US', {
                    year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
                });
                return `
                    <div class="history-item-card" data-id="${attempt.id}">
                        <div class="h-left">
                            <span class="h-attempt-badge">Attempt #${history.length - idx}</span>
                            <h4>${attempt.userProfile.name} • ${attempt.profileTitle}</h4>
                            <div class="h-meta">${dateStr} &bull; ID: <code>${attempt.id}</code></div>
                        </div>
                        <div class="h-score">
                            <div class="h-score-val">${attempt.industryReadinessIndex}</div>
                            <div class="h-score-label">Readiness Index</div>
                        </div>
                        <div class="h-actions">
                            <button type="button" class="btn btn-sm btn-secondary btn-view-attempt" data-id="${attempt.id}">View Report</button>
                            <button type="button" class="btn btn-sm btn-accent btn-compare-attempt" data-id="${attempt.id}">Compare</button>
                            <button type="button" class="btn btn-sm btn-danger btn-delete-attempt" data-id="${attempt.id}">Delete</button>
                        </div>
                    </div>
                `;
            }).join('');

            // Attach listeners
            listEl.querySelectorAll('.btn-view-attempt').forEach(btn => {
                btn.addEventListener('click', () => {
                    const id = btn.getAttribute('data-id');
                    const rep = global.StorageEngine.getAssessmentById(id);
                    if (rep) {
                        this.currentReport = rep;
                        this.renderReportView(rep);
                        this.showView('view-report');
                    }
                });
            });

            listEl.querySelectorAll('.btn-compare-attempt').forEach(btn => {
                btn.addEventListener('click', () => {
                    const id = btn.getAttribute('data-id');
                    this.executeComparison(id);
                });
            });

            listEl.querySelectorAll('.btn-delete-attempt').forEach(btn => {
                btn.addEventListener('click', () => {
                    const id = btn.getAttribute('data-id');
                    if (confirm("Delete this attempt permanently from local device?")) {
                        global.StorageEngine.deleteAssessment(id);
                        this.showHistoryView();
                    }
                });
            });

            this.showView('view-history');
        }

        executeComparison(selectedId) {
            const history = global.StorageEngine.getHistory();
            if (history.length < 2) {
                alert("You need at least two completed assessment attempts to compare score movement and 'What Changed?'.");
                return;
            }

            const current = global.StorageEngine.getAssessmentById(selectedId);
            // find earlier attempt
            const other = history.find(h => h.id !== selectedId) || history[1];

            const comp = global.StorageEngine.compareAttempts(current, other);
            if (!comp) return;

            const compSection = document.getElementById('comparison-results-section');
            if (!compSection) return;

            compSection.innerHTML = `
                <div class="comparison-card">
                    <div class="comp-header">
                        <h3>ATTEMPT COMPARISON: WHAT CHANGED?</h3>
                        <p class="comp-sub">Comparing <strong>${current.id}</strong> (${new Date(current.date).toLocaleDateString()}) vs <strong>${other.id}</strong> (${new Date(other.date).toLocaleDateString()})</p>
                    </div>

                    <div class="comp-hero-delta">
                        <div class="delta-box ${comp.indexDelta >= 0 ? 'pos' : 'neg'}">
                            <span class="d-label">Industry Readiness Movement</span>
                            <span class="d-val">${comp.indexDelta >= 0 ? '+' : ''}${comp.indexDelta} Points</span>
                        </div>
                        <div class="delta-box">
                            <span class="d-label">Cadence Shift</span>
                            <span class="d-val">${comp.timeDelta >= 0 ? '+' : ''}${comp.timeDelta}s avg</span>
                        </div>
                        <div class="delta-box">
                            <span class="d-label">Consistency Movement</span>
                            <span class="d-val">${comp.consistencyDelta >= 0 ? '+' : ''}${comp.consistencyDelta} pts</span>
                        </div>
                    </div>

                    <div class="comp-narrative">
                        <h4>Diagnostic Analysis: What Changed in Your Decision Patterns?</h4>
                        <p>${comp.whatChangedNarrative}</p>
                    </div>

                    <div class="comp-domains-list">
                        <h4>Domain Movement Highlights</h4>
                        <div class="delta-row-grid">
                            ${comp.domainDeltas.slice(0, 8).map(d => `
                                <div class="delta-pill ${d.delta >= 0 ? 'pos' : 'neg'}">
                                    <span>${d.meta.name}:</span>
                                    <strong>${d.previous} → ${d.current} (${d.delta >= 0 ? '+' : ''}${d.delta})</strong>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            `;
            compSection.classList.remove('hidden');
            compSection.scrollIntoView({ behavior: 'smooth' });
        }

        // Theme and A11y Settings
        applyTheme(theme) {
            this.settings.theme = theme;
            document.documentElement.setAttribute('data-theme', theme);
            global.StorageEngine.saveSettings(this.settings);

            const themeBtn = document.getElementById('btn-toggle-theme');
            if (themeBtn) {
                themeBtn.innerHTML = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
                themeBtn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`);
            }
        }

        toggleTheme() {
            const nextTheme = this.settings.theme === 'dark' ? 'light' : 'dark';
            this.applyTheme(nextTheme);
        }

        applyTextSize(size) {
            this.settings.textSize = size;
            document.documentElement.setAttribute('data-text-size', size);
            global.StorageEngine.saveSettings(this.settings);
        }

        showView(viewId) {
            document.querySelectorAll('.app-view').forEach(v => v.classList.remove('active-view'));
            const target = document.getElementById(viewId);
            if (target) {
                target.classList.add('active-view');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        setupPWA() {
            window.addEventListener('beforeinstallprompt', (e) => {
                e.preventDefault();
                this.deferredPrompt = e;
                const pwaBtn = document.getElementById('btn-install-pwa');
                if (pwaBtn) pwaBtn.classList.remove('hidden');
            });

            // Register Service Worker for 100% offline functionality
            if ('serviceWorker' in navigator) {
                window.addEventListener('load', () => {
                    navigator.serviceWorker.register('./sw.js').then(reg => {
                        console.log('360 IQ ServiceWorker registered offline');
                    }).catch(err => {
                        console.log('SW registration optional/bypassed:', err);
                    });
                });
            }
        }

        installPWA() {
            if (this.deferredPrompt) {
                this.deferredPrompt.prompt();
                this.deferredPrompt.userChoice.then(() => {
                    this.deferredPrompt = null;
                });
            } else {
                alert("To download this app to your device for offline use:\n\n1. In Chrome / Edge: Click the install icon in the URL address bar or 'Install App' in menu.\n2. On Android: Tap menu (⋮) -> 'Add to Home screen' or 'Install App'.\n3. On iOS: Tap Share -> 'Add to Home Screen'.\n\nThe app runs 100% offline without internet.");
            }
        }

        setupEventListeners() {
            // Profile inputs change
            ['input-user-name', 'select-age-group', 'select-current-stage', 'select-domain', 'select-experience'].forEach(id => {
                document.getElementById(id)?.addEventListener('change', () => this.updateAdvisorPreview());
                document.getElementById(id)?.addEventListener('input', () => this.updateAdvisorPreview());
            });

            // Header navigation buttons
            document.getElementById('btn-nav-home')?.addEventListener('click', () => this.showView('view-home'));
            document.getElementById('btn-nav-my-report')?.addEventListener('click', () => this.generateAndShowReport());
            document.getElementById('btn-nav-history')?.addEventListener('click', () => this.showHistoryView());
            document.getElementById('btn-nav-settings')?.addEventListener('click', () => this.showView('view-settings'));
            document.getElementById('btn-nav-about')?.addEventListener('click', () => this.showView('view-about'));
            document.getElementById('btn-toggle-theme')?.addEventListener('click', () => this.toggleTheme());
            document.getElementById('btn-install-pwa')?.addEventListener('click', () => this.installPWA());

            // Assessment Question Navigation
            document.getElementById('btn-question-prev')?.addEventListener('click', () => this.prevQuestion());
            document.getElementById('btn-question-next')?.addEventListener('click', () => this.nextQuestion());

            // Assessment Complete -> Generate Report
            document.getElementById('btn-reveal-my-report')?.addEventListener('click', () => this.generateAndShowReport());

            // Report Actions
            document.getElementById('btn-report-download-pdf')?.addEventListener('click', () => {
                if (this.currentReport && global.PDFEngine) global.PDFEngine.downloadPDF(this.currentReport);
            });
            document.getElementById('btn-report-share')?.addEventListener('click', () => {
                if (this.currentReport && global.PDFEngine) global.PDFEngine.shareReport(this.currentReport);
            });
            document.getElementById('btn-report-retake')?.addEventListener('click', () => {
                this.showView('view-home');
            });
            document.getElementById('btn-report-history')?.addEventListener('click', () => {
                this.showHistoryView();
            });

            // Settings Listeners
            document.getElementById('toggle-setting-sound')?.addEventListener('change', (e) => {
                global.soundEngine.setEnabled(e.target.checked);
            });
            document.getElementById('select-setting-text-size')?.addEventListener('change', (e) => {
                this.applyTextSize(e.target.value);
            });
            document.getElementById('btn-export-history-json')?.addEventListener('click', () => {
                global.StorageEngine.exportJSON();
            });
            document.getElementById('btn-reset-history')?.addEventListener('click', () => {
                if (confirm("Reset all previous assessment attempts? Your profile settings will remain.")) {
                    global.StorageEngine.clearHistory();
                    alert("Assessment history cleared.");
                }
            });
            document.getElementById('btn-delete-all-data')?.addEventListener('click', () => {
                if (confirm("DELETE ALL DATA: This will erase all offline assessments, profiles, and preferences stored on this device. Proceed?")) {
                    global.StorageEngine.deleteAllData();
                    alert("All local data has been permanently deleted.");
                    window.location.reload();
                }
            });

            // Keyboard accessibility shortcuts (1, 2, 3, 4 or A, B, C, D to pick options; Enter/Arrow to navigate)
            window.addEventListener('keydown', (e) => {
                const assessmentView = document.getElementById('view-assessment');
                if (!assessmentView || !assessmentView.classList.contains('active-view')) return;

                if (['1', 'a', 'A'].includes(e.key)) this.selectOption('A');
                else if (['2', 'b', 'B'].includes(e.key)) this.selectOption('B');
                else if (['3', 'c', 'C'].includes(e.key)) this.selectOption('C');
                else if (['4', 'd', 'D'].includes(e.key)) this.selectOption('D');
                else if (e.key === 'ArrowRight' || e.key === 'Enter') {
                    const q = this.activeQuestions[this.currentIndex];
                    if (q && this.answers[q.id]) this.nextQuestion();
                } else if (e.key === 'ArrowLeft') {
                    this.prevQuestion();
                }
            });
        }
    }

    global.AppController = AppController;
    window.addEventListener('DOMContentLoaded', () => {
        window.app = new AppController();
        window.app.init();
    });
})(window);
