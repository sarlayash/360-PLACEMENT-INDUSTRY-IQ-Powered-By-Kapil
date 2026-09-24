// 360° PLACEMENT & INDUSTRY IQ - Local Storage & History Engine
// 100% Offline Local Persistence with Attempt Comparison & Privacy Safeguards

(function(global) {
    const STORAGE_KEY_HISTORY = 'sy_360_history_v1';
    const STORAGE_KEY_PROFILE = 'sy_360_user_profile_v1';
    const STORAGE_KEY_SETTINGS = 'sy_360_settings_v1';

    class StorageEngine {
        // --- Profile Management ---
        static getSavedProfile() {
            try {
                const data = localStorage.getItem(STORAGE_KEY_PROFILE);
                return data ? JSON.parse(data) : null;
            } catch (e) {
                return null;
            }
        }

        static saveProfile(profile) {
            try {
                localStorage.setItem(STORAGE_KEY_PROFILE, JSON.stringify(profile));
            } catch (e) {
                console.error("Storage saveProfile error", e);
            }
        }

        // --- Settings Management ---
        static getSettings() {
            try {
                const data = localStorage.getItem(STORAGE_KEY_SETTINGS);
                return data ? JSON.parse(data) : {
                    theme: 'dark', // 'dark' | 'light'
                    sound: true,
                    animation: true,
                    textSize: 'normal' // 'normal' | 'large' | 'xlarge'
                };
            } catch (e) {
                return { theme: 'dark', sound: true, animation: true, textSize: 'normal' };
            }
        }

        static saveSettings(settings) {
            try {
                localStorage.setItem(STORAGE_KEY_SETTINGS, JSON.stringify(settings));
            } catch (e) {
                console.error("Storage saveSettings error", e);
            }
        }

        // --- Assessment History ---
        static getHistory() {
            try {
                const data = localStorage.getItem(STORAGE_KEY_HISTORY);
                return data ? JSON.parse(data) : [];
            } catch (e) {
                return [];
            }
        }

        static saveAssessment(report) {
            try {
                const history = StorageEngine.getHistory();
                history.unshift(report); // latest first
                // limit to last 20 attempts
                if (history.length > 20) {
                    history.pop();
                }
                localStorage.setItem(STORAGE_KEY_HISTORY, JSON.stringify(history));
                return true;
            } catch (e) {
                console.error("Storage saveAssessment error", e);
                return false;
            }
        }

        static getAssessmentById(id) {
            const history = StorageEngine.getHistory();
            return history.find(item => item.id === id) || null;
        }

        static deleteAssessment(id) {
            try {
                let history = StorageEngine.getHistory();
                history = history.filter(item => item.id !== id);
                localStorage.setItem(STORAGE_KEY_HISTORY, JSON.stringify(history));
                return true;
            } catch (e) {
                return false;
            }
        }

        static clearHistory() {
            try {
                localStorage.removeItem(STORAGE_KEY_HISTORY);
                return true;
            } catch (e) {
                return false;
            }
        }

        // Section 41: Delete All My Data
        static deleteAllData() {
            try {
                localStorage.removeItem(STORAGE_KEY_HISTORY);
                localStorage.removeItem(STORAGE_KEY_PROFILE);
                localStorage.removeItem(STORAGE_KEY_SETTINGS);
                localStorage.removeItem('sy_sound_enabled');
                return true;
            } catch (e) {
                return false;
            }
        }

        // Attempt Comparison: Attempt 1 vs Attempt 2 vs Attempt 3 (Section 33)
        // Does NOT simply say "better/worse". Shows: "What changed?"
        static compareAttempts(currentReport, previousReport) {
            if (!currentReport || !previousReport) return null;

            const indexDelta = currentReport.industryReadinessIndex - previousReport.industryReadinessIndex;
            
            // Domain movement
            const domainDeltas = [];
            for (let dim in currentReport.domainScores) {
                const curr = currentReport.domainScores[dim] || 0;
                const prev = previousReport.domainScores[dim] || 0;
                const delta = curr - prev;
                domainDeltas.push({
                    dimId: dim,
                    meta: global.getDomainMeta ? global.getDomainMeta(dim) : { name: dim },
                    current: curr,
                    previous: prev,
                    delta: delta,
                    deltaAbs: Math.abs(delta)
                });
            }

            // Top movers
            domainDeltas.sort((a, b) => b.delta - a.delta);
            const biggestGains = domainDeltas.slice(0, 3).filter(d => d.delta > 0);
            const biggestShifts = [...domainDeltas].sort((a, b) => a.delta - b.delta).slice(0, 3).filter(d => d.delta < 0);

            // Pillar shifts
            const pillarDeltas = {};
            for (let p in currentReport.pillars) {
                pillarDeltas[p] = {
                    current: currentReport.pillars[p],
                    previous: previousReport.pillars[p] || 0,
                    delta: currentReport.pillars[p] - (previousReport.pillars[p] || 0)
                };
            }

            // Decision Consistency & Cadence comparison
            const timeDelta = (currentReport.timeIntelligence?.averageResponseTime || 0) - (previousReport.timeIntelligence?.averageResponseTime || 0);
            const consistencyDelta = (currentReport.antiGaming?.consistencyScore || 0) - (previousReport.antiGaming?.consistencyScore || 0);

            // "What Changed?" Analytical Synthesis
            let whatChangedNarrative = "";
            if (indexDelta > 5) {
                whatChangedNarrative = `Your decision heuristics show marked structural maturation. Rather than opting for rapid compromise, your choices in ${biggestGains.map(g => g.meta.name).join(", ")} shifted toward long-term institutional value, system thinking, and empathetic stakeholder alignment.`;
            } else if (indexDelta < -5) {
                whatChangedNarrative = `Your response patterns indicate a distinct shift toward immediate risk mitigation and defensive positioning. Noticeable pivots occurred in ${biggestShifts.map(s => s.meta.name).join(", ")}, reflecting a more cautious, risk-averse posture compared to your earlier attempt.`;
            } else {
                whatChangedNarrative = `Your overall Industry Readiness Index remained stable (within ${Math.abs(indexDelta)} pts), but internal strategic trade-offs evolved: you showed increased focus on ${biggestGains[0]?.meta?.name || 'core execution'} while re-calibrating ${biggestShifts[0]?.meta?.name || 'operational priorities'}.`;
            }

            return {
                currentDate: currentReport.date,
                previousDate: previousReport.date,
                currentId: currentReport.id,
                previousId: previousReport.id,
                indexDelta,
                domainDeltas,
                biggestGains,
                biggestShifts,
                pillarDeltas,
                timeDelta,
                consistencyDelta,
                whatChangedNarrative
            };
        }

        // Export history as JSON
        static exportJSON() {
            const data = {
                exportedAt: new Date().toISOString(),
                brand: "360° PLACEMENT & INDUSTRY IQ Powered By Kapil",
                organization: "SarlaYash Mission",
                history: StorageEngine.getHistory(),
                profile: StorageEngine.getSavedProfile()
            };
            const jsonStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 2));
            const dlAnchor = document.createElement('a');
            dlAnchor.setAttribute("href", jsonStr);
            dlAnchor.setAttribute("download", `360_IQ_Report_History_${new Date().toISOString().slice(0, 10)}.json`);
            document.body.appendChild(dlAnchor);
            dlAnchor.click();
            dlAnchor.remove();
        }
    }

    global.StorageEngine = StorageEngine;
})(window);
