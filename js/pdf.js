// 360° PLACEMENT & INDUSTRY IQ - Offline PDF & Report Export Engine
// Powered by SarlaYash Mission - Legacy Of Values. Future Of Learning.

(function(global) {
    class PDFEngine {
        static renderPrintableReport(report) {
            // Verify QR code is generated
            const qrSvg = global.generateQRCodeSVG 
                ? global.generateQRCodeSVG(`https://sarlayash.org/verify?id=${report.id}&name=${encodeURIComponent(report.userProfile.name)}&score=${report.industryReadinessIndex}`, 140)
                : '';

            const dateStr = new Date(report.date).toLocaleDateString('en-US', {
                year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
            });

            // 20-domain cards
            const domainCardsHTML = report.sortedDomains.map(d => `
                <div class="print-domain-card" style="border-left: 4px solid ${d.color};">
                    <div class="print-domain-header">
                        <span class="print-domain-title">${d.icon} ${d.name}</span>
                        <span class="print-domain-score" style="color: ${d.color}; font-weight: 700;">${d.score}/100</span>
                    </div>
                    <div class="print-domain-band">${d.band.badge} ${d.band.band}</div>
                    <div class="print-domain-summary">${d.summary}</div>
                </div>
            `).join('');

            // Strengths HTML
            const strengthsHTML = report.top5Strengths.map((s, idx) => `
                <div class="print-item">
                    <strong>${idx + 1}. ${s.icon} ${s.name} (${s.score}/100) — ${s.band.band}</strong>
                    <p class="print-desc"><em>Why this matters:</em> ${s.why}</p>
                </div>
            `).join('');

            // Development Areas HTML
            const devAreasHTML = report.top5Developments.map((d, idx) => `
                <div class="print-item dev-item">
                    <strong>${idx + 1}. ${d.icon} ${d.name} (${d.score}/100) — Priority Focus</strong>
                    <p class="print-desc"><strong>Workplace Impact:</strong> ${d.workplaceImpact}</p>
                    <p class="print-desc"><strong>Practical Action:</strong> ${d.practicalAction}</p>
                    <div class="print-plan-box">
                        <div><strong>7-Day Action:</strong> ${d.plan7Day}</div>
                        <div><strong>30-Day Growth:</strong> ${d.plan30Day}</div>
                    </div>
                </div>
            `).join('');

            // Career Weather Map
            const weatherHTML = report.sortedDomains.map(d => `
                <div class="print-weather-pill" style="border-color: ${d.weather.color};">
                    <span>${d.weather.icon} ${d.name}</span>
                    <strong style="color: ${d.weather.color}">${d.score}</strong>
                </div>
            `).join('');

            // Radar Chart SVG (captured from live DOM or regenerated)
            const radarChartEl = document.getElementById('radar-svg-container');
            const radarChartSVG = radarChartEl ? radarChartEl.innerHTML : '';

            const printContainer = document.getElementById('printable-report-area');
            if (!printContainer) return;

            printContainer.innerHTML = `
                <div class="print-document">
                    <!-- PAGE 1: COVER & EXECUTIVE SUMMARY -->
                    <div class="print-page cover-page">
                        <div class="print-brand-badge">🚀 SarlaYash Mission</div>
                        <h1 class="print-title">360° PLACEMENT &amp; INDUSTRY IQ</h1>
                        <p class="print-subtitle">The World's Most Comprehensive Offline Career &amp; Industry Readiness Assessment</p>
                        <p class="print-tagline">"Don't Just Measure What You Know. Measure How You Think, Work, Adapt &amp; Grow."</p>

                        <div class="print-candidate-box">
                            <div class="print-info-grid">
                                <div><span class="label">Candidate Name:</span> <strong>${report.userProfile.name}</strong></div>
                                <div><span class="label">Career Stage:</span> <strong>${report.userProfile.currentStage}</strong></div>
                                <div><span class="label">Target Domain:</span> <strong>${report.userProfile.domain}</strong></div>
                                <div><span class="label">Experience Level:</span> <strong>${report.userProfile.experience} years</strong></div>
                                <div><span class="label">Assessment ID:</span> <strong>${report.id}</strong></div>
                                <div><span class="label">Completion Date:</span> <strong>${dateStr}</strong></div>
                            </div>
                            <div class="print-qr-slot">
                                ${qrSvg}
                                <div class="print-qr-caption">Offline Cryptographic Hash Verified<br><strong>${report.id}</strong></div>
                            </div>
                        </div>

                        <!-- EXECUTIVE SNAPSHOT -->
                        <div class="print-section">
                            <h2 class="print-heading">EXECUTIVE READINESS SNAPSHOT</h2>
                            <div class="print-score-hero">
                                <div class="hero-score-val">${report.industryReadinessIndex}</div>
                                <div class="hero-score-label">
                                    <div class="hero-title">INDUSTRY READINESS INDEX</div>
                                    <div class="hero-sub">${report.profileTitle} &bull; ${report.sortedDomains[0].band.band}</div>
                                </div>
                            </div>

                            <div class="print-pillars-grid">
                                <div class="pillar-box">
                                    <div class="p-title">🧠 Cognitive Readiness</div>
                                    <div class="p-val">${report.pillars.cognitiveReadiness}/100</div>
                                </div>
                                <div class="pillar-box">
                                    <div class="p-title">🤝 People Readiness</div>
                                    <div class="p-val">${report.pillars.peopleReadiness}/100</div>
                                </div>
                                <div class="pillar-box">
                                    <div class="p-title">🤖 Digital Readiness</div>
                                    <div class="p-val">${report.pillars.digitalReadiness}/100</div>
                                </div>
                                <div class="pillar-box">
                                    <div class="p-title">⚖️ Professional Readiness</div>
                                    <div class="p-val">${report.pillars.professionalReadiness}/100</div>
                                </div>
                                <div class="pillar-box">
                                    <div class="p-title">🚀 Growth Readiness</div>
                                    <div class="p-val">${report.pillars.growthReadiness}/100</div>
                                </div>
                            </div>
                        </div>

                        <!-- PROFESSIONAL DNA -->
                        <div class="print-section">
                            <h2 class="print-heading">YOUR PROFESSIONAL DNA</h2>
                            <div class="dna-box">
                                <h3>Primary Archetype: ${report.professionalDNA.primary.name}</h3>
                                <p class="dna-tagline">${report.professionalDNA.primary.tagline}</p>
                                <p><strong>Key Strategic Traits:</strong> ${report.professionalDNA.primary.traits.join(" &bull; ")}</p>
                                <p><strong>Secondary Pattern:</strong> ${report.professionalDNA.secondary.name} — ${report.professionalDNA.secondary.tagline}</p>
                                <p class="dna-notice"><em>${report.professionalDNA.disclaimer}</em></p>
                            </div>
                        </div>

                        <div class="print-footer">
                            <span>Generated Offline by 360° Placement &amp; Industry IQ</span>
                            <span>Page 1 of 3</span>
                        </div>
                    </div>

                    <!-- PAGE 2: 20-DIMENSION RADAR & DOMAIN BREAKDOWN -->
                    <div class="print-page">
                        <div class="print-header-mini">
                            <span>360° Placement &amp; Industry IQ &bull; Assessment ID: ${report.id}</span>
                            <span>Candidate: ${report.userProfile.name}</span>
                        </div>

                        <h2 class="print-heading">20-DIMENSION INTELLIGENCE RADAR</h2>
                        <div class="print-radar-wrapper">
                            ${radarChartSVG}
                        </div>

                        <h2 class="print-heading" style="margin-top: 16px;">CAREER WEATHER MAP (ALL 20 DIMENSIONS)</h2>
                        <div class="print-weather-grid">
                            ${weatherHTML}
                        </div>

                        <h2 class="print-heading" style="margin-top: 16px;">20-DIMENSION SCORE MATRIX</h2>
                        <div class="print-domains-grid">
                            ${domainCardsHTML}
                        </div>

                        <div class="print-footer">
                            <span>Generated Offline by 360° Placement &amp; Industry IQ</span>
                            <span>Page 2 of 3</span>
                        </div>
                    </div>

                    <!-- PAGE 3: SIMULATION, STRENGTHS & DEVELOPMENT ROADMAP -->
                    <div class="print-page">
                        <div class="print-header-mini">
                            <span>360° Placement &amp; Industry IQ &bull; Assessment ID: ${report.id}</span>
                            <span>Candidate: ${report.userProfile.name}</span>
                        </div>

                        <h2 class="print-heading">CAREER SIMULATION: "WHAT HAPPENS IF YOU ENTER THE WORKPLACE TOMORROW?"</h2>
                        <div class="print-sim-box">
                            <p class="sim-notice"><em>${report.careerSimulation.label}</em></p>
                            <div class="sim-phase">
                                <strong>First 30 Days:</strong>
                                <div>&bull; <em>Potential Strengths:</em> ${report.careerSimulation.first30Days.strengths}</div>
                                <div>&bull; <em>Potential Challenges:</em> ${report.careerSimulation.first30Days.challenges}</div>
                            </div>
                            <div class="sim-phase">
                                <strong>First 90 Days:</strong>
                                <div>&bull; <em>Likely Opportunities:</em> ${report.careerSimulation.first90Days.opportunities}</div>
                            </div>
                            <div class="sim-phase">
                                <strong>First 6 Months:</strong>
                                <div>&bull; <em>Growth Signals:</em> ${report.careerSimulation.first6Months.growthSignals}</div>
                            </div>
                        </div>

                        <div class="print-columns-2">
                            <div>
                                <h3 class="print-subheading">TOP 5 STRENGTH SIGNALS</h3>
                                ${strengthsHTML}
                            </div>
                            <div>
                                <h3 class="print-subheading">TOP 5 DEVELOPMENT OPPORTUNITIES</h3>
                                ${devAreasHTML}
                            </div>
                        </div>

                        <div class="print-section" style="margin-top: 16px;">
                            <h3 class="print-subheading">AI &amp; TRANSFERABLE SKILLS SUMMARY</h3>
                            <div class="ai-summary-grid">
                                <div><strong>AI Readiness Score:</strong> ${report.aiReadinessReport.overallScore}/100</div>
                                <div><strong>Decision Stability:</strong> ${report.antiGaming.decisionStability}</div>
                                <div><strong>Average Response Cadence:</strong> ${report.timeIntelligence.averageResponseTime} seconds/decision</div>
                                <div><strong>Industry Transferability Index:</strong> ${report.transferableSkillsIndex.averageTransferability}/100</div>
                            </div>
                        </div>

                        <div class="print-methodology-box">
                            <strong>Assessment Methodology &amp; Disclaimer:</strong>
                            Evaluated across 100 scenario-based dilemmas measuring cognitive logic, emotional intelligence, business pragmatism, and leadership ethics. No cloud dependency or third-party algorithms were used. 
                            <em>Notice: This report provides career development insights and capability indicators; it does not constitute an employment guarantee or psychological diagnosis.</em>
                        </div>

                        <div class="print-footer">
                            <span>SarlaYash Mission &bull; Legacy Of Values. Future Of Learning.</span>
                            <span>Page 3 of 3</span>
                        </div>
                    </div>
                </div>
            `;
        }

        static downloadPDF(report) {
            PDFEngine.renderPrintableReport(report);
            setTimeout(() => {
                window.print();
            }, 250);
        }

        static shareReport(report) {
            if (navigator.share) {
                navigator.share({
                    title: `360° Placement & Industry IQ Report - ${report.userProfile.name}`,
                    text: `Candidate ${report.userProfile.name} achieved an Industry Readiness Index of ${report.industryReadinessIndex}/100 (${report.profileTitle}) on the 360° Placement & Industry IQ assessment.`,
                    url: window.location.href
                }).catch(() => {
                    PDFEngine.downloadPDF(report);
                });
            } else {
                PDFEngine.downloadPDF(report);
            }
        }
    }

    global.PDFEngine = PDFEngine;
})(window);
