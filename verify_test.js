const fs = require('fs');
const path = require('path');

console.log("=== RUNNING END-TO-END VERIFICATION TEST SUITE ===");

// 1. Verify files exist
const requiredFiles = [
    'index.html',
    'manifest.json',
    'sw.js',
    'data/questions.json',
    'js/questions-data.js',
    'js/sound.js',
    'js/qrcode.js',
    'js/scoring.js',
    'js/storage.js',
    'js/pdf.js',
    'js/app.js',
    'css/styles.css',
    'css/print.css',
    'assets/icon.svg'
];

requiredFiles.forEach(file => {
    const fullPath = path.join(__dirname, file);
    if (!fs.existsSync(fullPath)) {
        throw new Error(`Missing required file: ${file}`);
    }
    const stat = fs.statSync(fullPath);
    console.log(`[OK] File verified: ${file} (${stat.size} bytes)`);
});

// 2. Validate questions.json
const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'data/questions.json'), 'utf8'));
console.log(`\nValidating questions.json: Total ${questions.length} questions...`);

if (questions.length !== 100) {
    throw new Error(`Expected exactly 100 questions, got ${questions.length}`);
}

const levels = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
const dimensions = new Set();
let microScenariosCount = 0;

questions.forEach((q, idx) => {
    if (q.id !== idx + 1) throw new Error(`Q id mismatch at ${idx}: got ${q.id}`);
    if (q.options.length !== 4) throw new Error(`Q${q.id} options length != 4`);
    levels[q.difficulty]++;
    Object.keys(q.dimensionWeights).forEach(d => dimensions.add(d));
    if (q.microScenario) microScenariosCount++;
});

console.log("[OK] Difficulty distribution:", levels);
if (levels[1] !== 20 || levels[2] !== 20 || levels[3] !== 20 || levels[4] !== 20 || levels[5] !== 20) {
    throw new Error("Difficulty levels not evenly divided 20 per level!");
}

console.log(`[OK] Micro-scenarios attached: ${microScenariosCount} adaptive branches.`);
console.log(`[OK] Unique dimensions covered: ${dimensions.size} dimensions.`);

// 3. Test Scoring Simulation via Node environment
// Mock browser environment for scoring test
const windowMock = {};
global.window = windowMock;

const scoringCode = fs.readFileSync(path.join(__dirname, 'js/scoring.js'), 'utf8');
eval(scoringCode);

const mockProfile = {
    name: "Dr. Evelyn Reed",
    ageGroup: "26-30",
    currentStage: "Working Professional",
    domain: "Technology",
    experience: "3-5"
};

const mockAnswers = {};
const mockTimeLogs = {};
const mockMicroAnswers = {};

questions.forEach(q => {
    // Pick realistic answers (alternating B and A)
    const pick = (q.id % 2 === 0) ? 'B' : 'A';
    mockAnswers[q.id] = pick;
    mockTimeLogs[q.id] = 32; // optimal response time
    if (q.microScenario) {
        mockMicroAnswers[q.id] = 'A';
    }
});

const report = windowMock.ScoringEngine.evaluateAssessment(
    mockProfile,
    questions,
    mockAnswers,
    mockTimeLogs,
    mockMicroAnswers
);

console.log("\n--- SIMULATION SCORING REPORT VERIFICATION ---");
console.log(`Report ID: ${report.id}`);
console.log(`Industry Readiness Index: ${report.industryReadinessIndex}/100`);
console.log(`Career Stage Profile: ${report.profileTitle}`);
console.log(`Cognitive Readiness: ${report.pillars.cognitiveReadiness}/100`);
console.log(`People Readiness: ${report.pillars.peopleReadiness}/100`);
console.log(`Digital Readiness: ${report.pillars.digitalReadiness}/100`);
console.log(`Professional Readiness: ${report.pillars.professionalReadiness}/100`);
console.log(`Growth Readiness: ${report.pillars.growthReadiness}/100`);

if (report.industryReadinessIndex < 0 || report.industryReadinessIndex > 100) {
    throw new Error("Industry Readiness Index out of 0-100 range!");
}

console.log(`Top 5 Strengths: ${report.top5Strengths.map(s => s.name).join(", ")}`);
console.log(`Top 5 Development Opportunities: ${report.top5Developments.map(d => d.name).join(", ")}`);
console.log(`Professional DNA Primary: ${report.professionalDNA.primary.name}`);
console.log(`Anti-Gaming Consistency Score: ${report.antiGaming.consistencyScore}/100`);
console.log(`Anti-Gaming Authenticity Score: ${report.antiGaming.authenticityScore}/100`);
console.log(`Time Intelligence Decision Speed Index: ${report.timeIntelligence.decisionSpeedIndex}/100`);

// 4. Test QR Code Generator
const qrcodeCode = fs.readFileSync(path.join(__dirname, 'js/qrcode.js'), 'utf8');
eval(qrcodeCode);

const qrSvg = windowMock.generateQRCodeSVG(`https://sarlayash.org/verify?id=${report.id}&score=${report.industryReadinessIndex}`, 140);
if (!qrSvg || !qrSvg.includes('<svg')) {
    throw new Error("QR Code SVG generation failed!");
}
console.log(`[OK] QR Code generated successfully (SVG length: ${qrSvg.length} characters)`);

// 5. Test Comparison Logic
const storageCode = fs.readFileSync(path.join(__dirname, 'js/storage.js'), 'utf8');
eval(storageCode);

// create previous attempt report
const previousReport = {
    ...report,
    id: "SY-360-IQ-2026-PREV01",
    date: new Date(Date.now() - 86400000 * 14).toISOString(),
    industryReadinessIndex: report.industryReadinessIndex - 8,
    domainScores: { ...report.domainScores, leadership_iq: report.domainScores.leadership_iq - 12 }
};

const comparison = windowMock.StorageEngine.compareAttempts(report, previousReport);
console.log("\n--- ATTEMPT COMPARISON VERIFICATION ---");
console.log(`Index Delta: ${comparison.indexDelta >= 0 ? '+' : ''}${comparison.indexDelta} points`);
console.log(`What Changed Narrative: ${comparison.whatChangedNarrative}`);

console.log("\n[SUCCESS] ALL VERIFICATION SUITE TESTS PASSED PERFECTLY!");
