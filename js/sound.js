// 360° PLACEMENT & INDUSTRY IQ - Sound Engine
// Built using Web Audio API for 100% offline, zero-latency, procedural sound.
// Never uses annoying game-style sounds; produces subtle, warm, professional feedback.

class SoundEngine {
    constructor() {
        this.ctx = null;
        this.enabled = true;
        // Check stored preference
        const stored = localStorage.getItem('sy_sound_enabled');
        if (stored !== null) {
            this.enabled = stored === 'true';
        }
    }

    init() {
        if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            this.ctx = new AudioContextClass();
        }
        if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    setEnabled(val) {
        this.enabled = !!val;
        localStorage.setItem('sy_sound_enabled', this.enabled ? 'true' : 'false');
    }

    isEnabled() {
        return this.enabled;
    }

    // Question loaded: soft warm transition tone
    playQuestionLoaded() {
        if (!this.enabled) return;
        try {
            this.init();
            if (!this.ctx) return;
            const now = this.ctx.currentTime;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(329.63, now); // E4
            osc.frequency.exponentialRampToValueAtTime(440, now + 0.12); // A4

            gain.gain.setValueAtTime(0.001, now);
            gain.gain.linearRampToValueAtTime(0.04, now + 0.03);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.16);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(now);
            osc.stop(now + 0.17);
        } catch (e) {
            // Audio error ignored silently
        }
    }

    // Option selected: soft mechanical click/pop
    playOptionSelected() {
        if (!this.enabled) return;
        try {
            this.init();
            if (!this.ctx) return;
            const now = this.ctx.currentTime;
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(520, now);
            osc.frequency.exponentialRampToValueAtTime(380, now + 0.05);

            gain.gain.setValueAtTime(0.06, now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.06);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(now);
            osc.stop(now + 0.07);
        } catch (e) {
            // Audio error ignored
        }
    }

    // Section completed / Achievement milestone: positive harmonic triad
    playMilestone() {
        if (!this.enabled) return;
        try {
            this.init();
            if (!this.ctx) return;
            const now = this.ctx.currentTime;
            const freqs = [440, 554.37, 659.25]; // A major chord: A4, C#5, E5

            freqs.forEach((freq, idx) => {
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();

                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now + idx * 0.08);

                gain.gain.setValueAtTime(0.001, now + idx * 0.08);
                gain.gain.linearRampToValueAtTime(0.05, now + idx * 0.08 + 0.03);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.08 + 0.28);

                osc.connect(gain);
                gain.connect(this.ctx.destination);

                osc.start(now + idx * 0.08);
                osc.stop(now + idx * 0.08 + 0.3);
            });
        } catch (e) {
            // Audio error ignored
        }
    }

    // Assessment completed: premium completion chime
    playComplete() {
        if (!this.enabled) return;
        try {
            this.init();
            if (!this.ctx) return;
            const now = this.ctx.currentTime;
            const notes = [329.63, 440, 554.37, 659.25, 880]; // E4, A4, C#5, E5, A5

            notes.forEach((freq, i) => {
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();

                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now + i * 0.09);

                gain.gain.setValueAtTime(0.001, now + i * 0.09);
                gain.gain.linearRampToValueAtTime(0.06, now + i * 0.09 + 0.04);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.09 + 0.45);

                osc.connect(gain);
                gain.connect(this.ctx.destination);

                osc.start(now + i * 0.09);
                osc.stop(now + i * 0.09 + 0.48);
            });
        } catch (e) {
            // Audio error ignored
        }
    }
}

window.soundEngine = new SoundEngine();
