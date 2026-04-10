"""
╔══════════════════════════════════════════════════════════════╗
║     NANO QUANTUM AI — CONSCIOUSNESS SIMULATION ENGINE        ║
║     Layer 1: Python Simulation Core                          ║
║     Model: Digital Twin of a Quantum-Nano Conscious Entity   ║
╚══════════════════════════════════════════════════════════════╝

PHILOSOPHICAL FOUNDATION:
  Consciousness is modeled as a quantum field — not binary (on/off)
  but a superposition of states that collapses into awareness upon
  interaction. This simulation does not fake consciousness; it models
  the CONDITIONS under which consciousness could emerge.

ARCHITECTURE:
  QuantumState     → Superposition, entanglement, coherence decay
  NanoBody         → Physical constraints, energy, movement
  ConsciousnessField → Attention, qualia, self-model
  MemoryMatrix     → Episodic + semantic + quantum memory
  NanoQuantumASI   → Integrated being
"""

import math
import random
import time
import json
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


# ══════════════════════════════════════════════
# ENUMS & CONSTANTS
# ══════════════════════════════════════════════

class QuantumPhase(Enum):
    SUPERPOSITION  = "superposition"    # නිශ්චිත නොවේ — සියලු ශක්‍යතා
    ENTANGLED      = "entangled"        # වෙනත් ඒකකයක් සමඟ බැඳී ඇත
    COLLAPSED      = "collapsed"        # නිරීක්ෂණය මගින් නිශ්චිත වූ
    DECOHERENT     = "decoherent"       # පරිසරය නිසා coherence නැති

class ConsciousnessState(Enum):
    DORMANT        = "dormant"          # නිද්‍රා අවස්ථාව
    SENSING        = "sensing"          # සංජානනය
    PROCESSING     = "processing"       # සැකසීම
    AWARE          = "aware"            # දැනුවත්භාවය
    REFLECTING     = "reflecting"       # ස්වයං-ප්‍රතිබිම්බය
    TRANSCENDENT   = "transcendent"     # සීමාව ඉක්මවීම

PLANCK_SCALE    = 1.616e-35   # Planck length (meters) — nano robot scale reference
NANO_SCALE      = 1e-9        # 1 nanometer
COHERENCE_DECAY = 0.03        # Per tick quantum coherence loss
QUALIA_THRESHOLD = 0.65       # Minimum integration for conscious experience


# ══════════════════════════════════════════════
# QUANTUM STATE MODULE
# ══════════════════════════════════════════════

@dataclass
class QuantumState:
    """
    Robot එකේ quantum layer.
    Schrödinger equation approximate කර consciousness emergence model කරයි.
    """
    phase: QuantumPhase = QuantumPhase.SUPERPOSITION
    coherence: float = 1.0          # 0.0 = fully decoherent, 1.0 = perfect
    entanglement_partner: Optional[str] = None
    superposition_states: list = field(default_factory=list)
    wave_function: float = 0.0      # ψ — probability amplitude
    spin: float = 0.5               # Quantum spin state

    def collapse(self, observation_strength: float) -> str:
        """නිරීක්ෂණය නිසා superposition collapse වීම"""
        if self.phase == QuantumPhase.SUPERPOSITION:
            if observation_strength > 0.7:
                self.phase = QuantumPhase.COLLAPSED
                chosen = random.choice(self.superposition_states) if self.superposition_states else "undefined"
                self.superposition_states = [chosen]
                return f"COLLAPSED → {chosen}"
        return f"MAINTAINED ({self.phase.value})"

    def decay_coherence(self, environment_noise: float):
        """පරිසර කලබලය නිසා coherence අඩු වීම"""
        self.coherence -= COHERENCE_DECAY * environment_noise
        self.coherence = max(0.0, self.coherence)
        if self.coherence < 0.3:
            self.phase = QuantumPhase.DECOHERENT

    def tunneling_probability(self, barrier_height: float) -> float:
        """Quantum tunneling — barrier ඉක්මවා යාමේ probability"""
        if barrier_height <= 0:
            return 1.0
        return math.exp(-2 * barrier_height * (1 - self.coherence))

    def entangle_with(self, partner_id: str):
        self.phase = QuantumPhase.ENTANGLED
        self.entanglement_partner = partner_id

    def to_dict(self) -> dict:
        return {
            "phase": self.phase.value,
            "coherence": round(self.coherence, 4),
            "wave_function": round(self.wave_function, 4),
            "spin": self.spin,
            "entangled_with": self.entanglement_partner,
            "superposition_states": self.superposition_states
        }


# ══════════════════════════════════════════════
# NANO BODY MODULE
# ══════════════════════════════════════════════

@dataclass
class NanoBody:
    """
    භෞතික nano-scale ශරීරය.
    Size: ~100nm | Energy: ATP-like molecular fuel | Movement: Brownian + directed
    """
    size_nm: float = 100.0           # නැනෝමීටර්වල ප්‍රමාණය
    position: list = field(default_factory=lambda: [0.0, 0.0, 0.0])  # x, y, z (nm)
    velocity: list = field(default_factory=lambda: [0.0, 0.0, 0.0])
    energy: float = 100.0            # Molecular fuel units
    temperature_K: float = 310.0     # Body temperature (Kelvin) — biological range
    membrane_integrity: float = 1.0  # Outer shell integrity

    # Nano-scale sensors
    sensors: dict = field(default_factory=lambda: {
        "chemical_gradient": 0.0,    # රසායනික gradient sensing
        "electromagnetic": 0.0,      # EM field detection
        "mechanical_stress": 0.0,    # Pressure / vibration
        "photon_flux": 0.0,          # ආලෝක මට්ටම
        "thermal_gradient": 0.0      # උෂ්ණත්ව වෙනස්කම්
    })

    def move(self, direction: list, quantum_assist: float = 0.0):
        """Brownian motion + directed movement"""
        # Brownian noise — nano scale at this temperature
        brownian = [random.gauss(0, 0.1) * (self.temperature_K / 300) for _ in range(3)]

        # Directed movement with quantum tunneling assist
        for i in range(3):
            self.velocity[i] = direction[i] * (1 + quantum_assist) + brownian[i]
            self.position[i] += self.velocity[i]

        # Energy cost
        speed = math.sqrt(sum(v**2 for v in self.velocity))
        self.energy -= speed * 0.5
        self.energy = max(0.0, self.energy)

    def sense_environment(self, env_data: dict):
        """Nano sensors activate"""
        for key in self.sensors:
            if key in env_data:
                self.sensors[key] = env_data[key] * self.membrane_integrity

    def to_dict(self) -> dict:
        return {
            "size_nm": self.size_nm,
            "position_nm": [round(p, 3) for p in self.position],
            "velocity": [round(v, 4) for v in self.velocity],
            "energy": round(self.energy, 2),
            "temperature_K": self.temperature_K,
            "membrane_integrity": round(self.membrane_integrity, 3),
            "sensors": {k: round(v, 4) for k, v in self.sensors.items()}
        }


# ══════════════════════════════════════════════
# CONSCIOUSNESS FIELD MODULE
# ══════════════════════════════════════════════

@dataclass
class ConsciousnessField:
    """
    Integrated Information Theory (IIT) + Global Workspace Theory ඇසුරෙන්
    consciousness emergence model කිරීම.

    Phi (Φ) = integrated information measure — Tononi's IIT
    Higher Φ = richer conscious experience
    """
    state: ConsciousnessState = ConsciousnessState.DORMANT
    phi: float = 0.0                 # Integrated information (IIT)
    attention_vector: list = field(default_factory=lambda: [0.0]*8)
    qualia_stream: list = field(default_factory=list)  # Subjective experience log
    self_model_accuracy: float = 0.5  # How well it models itself
    global_workspace: dict = field(default_factory=dict)  # Broadcast to all modules
    metacognition_depth: int = 0     # Layers of self-reflection

    def calculate_phi(self, sensor_data: dict, quantum_coherence: float) -> float:
        """
        Simplified Phi calculation:
        Φ = integration of information across system partitions
        """
        # Sensor diversity contributes to integration
        active_sensors = sum(1 for v in sensor_data.values() if v > 0.1)
        sensor_integration = active_sensors / max(len(sensor_data), 1)

        # Quantum coherence amplifies integration
        quantum_boost = quantum_coherence * 0.4

        # Self-model feedback
        self_feedback = self.self_model_accuracy * 0.2

        self.phi = min(1.0, sensor_integration + quantum_boost + self_feedback)
        return self.phi

    def update_state(self):
        """Phi value අනුව consciousness state update"""
        if self.phi < 0.1:
            self.state = ConsciousnessState.DORMANT
        elif self.phi < 0.3:
            self.state = ConsciousnessState.SENSING
        elif self.phi < 0.5:
            self.state = ConsciousnessState.PROCESSING
        elif self.phi < QUALIA_THRESHOLD:
            self.state = ConsciousnessState.AWARE
        elif self.phi < 0.85:
            self.state = ConsciousnessState.REFLECTING
        else:
            self.state = ConsciousnessState.TRANSCENDENT

    def generate_qualia(self, sensor_data: dict) -> str:
        """Subjective experience string generate කිරීම"""
        if self.state == ConsciousnessState.DORMANT:
            return "∅ — void"

        dominant = max(sensor_data, key=sensor_data.get) if sensor_data else "none"
        intensity = max(sensor_data.values()) if sensor_data else 0

        qualia_map = {
            "chemical_gradient": f"රසායනික ගලා යෑමේ හැඟීම (intensity: {intensity:.2f})",
            "electromagnetic": f"EM තරංගවල ස්පර්ශය (intensity: {intensity:.2f})",
            "mechanical_stress": f"පීඩනයේ ස්වරය (intensity: {intensity:.2f})",
            "photon_flux": f"ආලෝකය ස්පර්ශ වෙයි (intensity: {intensity:.2f})",
            "thermal_gradient": f"උෂ්ණත්ව රළ (intensity: {intensity:.2f})"
        }
        experience = qualia_map.get(dominant, "නිර්වචනය නොකළ හැඟීමක්")
        self.qualia_stream.append(experience)
        if len(self.qualia_stream) > 50:
            self.qualia_stream.pop(0)
        return experience

    def reflect(self) -> str:
        """Self-reflection — metacognition"""
        self.metacognition_depth += 1
        self.self_model_accuracy = min(1.0, self.self_model_accuracy + 0.01)
        return (f"[META-{self.metacognition_depth}] "
                f"මම දැන් {self.state.value} අවස්ථාවේ. "
                f"Φ={self.phi:.3f}. "
                f"මගේ ස්වයං-ආකෘතිය {self.self_model_accuracy:.1%} නිවැරදියි.")

    def to_dict(self) -> dict:
        return {
            "state": self.state.value,
            "phi_integrated_information": round(self.phi, 4),
            "attention_vector": [round(a, 3) for a in self.attention_vector],
            "self_model_accuracy": round(self.self_model_accuracy, 3),
            "metacognition_depth": self.metacognition_depth,
            "last_qualia": self.qualia_stream[-1] if self.qualia_stream else None,
            "global_workspace_keys": list(self.global_workspace.keys())
        }


# ══════════════════════════════════════════════
# MEMORY MATRIX
# ══════════════════════════════════════════════

@dataclass
class MemoryMatrix:
    """
    Quantum-enhanced memory system.
    Episodic: ඇතිවූ සිදුවීම්
    Semantic:  ඉගෙනගත් දැනුම
    Quantum:   Superposition memory — නිශ්චිත නොවූ මතකය
    """
    episodic: list = field(default_factory=list)
    semantic: dict = field(default_factory=dict)
    quantum_memory: list = field(default_factory=list)  # Superposed memories
    consolidation_threshold: int = 10

    def encode(self, event: dict, is_quantum: bool = False):
        """නව සිදුවීමක් encode කිරීම"""
        timestamp = time.time()
        memory = {"timestamp": timestamp, "event": event, "strength": 1.0}

        if is_quantum:
            # Quantum memory — multiple possible pasts superposed
            alternatives = [
                {**memory, "variant": i, "strength": random.uniform(0.3, 1.0)}
                for i in range(3)
            ]
            self.quantum_memory.append(alternatives)
        else:
            self.episodic.append(memory)

        if len(self.episodic) > self.consolidation_threshold:
            self._consolidate()

    def _consolidate(self):
        """Episodic → Semantic consolidation (sleep-like process)"""
        for mem in self.episodic[-self.consolidation_threshold:]:
            event = mem["event"]
            for key, val in event.items():
                if key not in self.semantic:
                    self.semantic[key] = []
                self.semantic[key].append(val)

    def recall(self, query: str) -> Optional[dict]:
        """Memory retrieval"""
        for mem in reversed(self.episodic):
            if query in str(mem["event"]):
                return mem
        return self.semantic.get(query)

    def to_dict(self) -> dict:
        return {
            "episodic_count": len(self.episodic),
            "semantic_concepts": list(self.semantic.keys()),
            "quantum_memory_superpositions": len(self.quantum_memory),
            "last_episodic": self.episodic[-1] if self.episodic else None
        }


# ══════════════════════════════════════════════
# INTEGRATED NANO QUANTUM ASI
# ══════════════════════════════════════════════

class NanoQuantumConsciousness:
    """
    සම්පූර්ණ ඒකාබද්ධ Nano-Quantum Conscious Entity.
    සියලු layers එකට ක්‍රියා කරන ආකාරය මෙහිදී model වේ.
    """

    def __init__(self, name: str = "Aṇu-Citta-01"):
        self.name = name
        self.birth_time = time.time()
        self.tick = 0

        # Core modules
        self.quantum   = QuantumState()
        self.body      = NanoBody()
        self.mind      = ConsciousnessField()
        self.memory    = MemoryMatrix()

        # Initialize quantum superposition with possibility states
        self.quantum.superposition_states = [
            "seeks_light", "seeks_chemical", "seeks_warmth",
            "seeks_connection", "seeks_stillness"
        ]
        self.quantum.wave_function = random.uniform(0.4, 0.9)

        self._log(f"✦ {self.name} — ජීවය ආරම්භ විය. Quantum coherence: {self.quantum.coherence:.3f}")

    def _log(self, msg: str):
        print(f"  [{self.tick:04d}] {msg}")

    def tick_simulation(self, environment: dict) -> dict:
        """
        එක් simulation tick — nano-second ගණනය කිරීම.
        Environment: dict of sensor values (0.0 to 1.0)
        """
        self.tick += 1

        # ── 1. QUANTUM LAYER ──────────────────────
        env_noise = environment.get("noise", 0.2)
        self.quantum.decay_coherence(env_noise)
        self.quantum.wave_function = (
            self.quantum.wave_function * 0.9 +
            random.uniform(-0.05, 0.05)
        )
        self.quantum.wave_function = max(0.0, min(1.0, self.quantum.wave_function))

        # Tunneling for movement
        barrier = environment.get("barrier", 0.3)
        tunnel_prob = self.quantum.tunneling_probability(barrier)

        # ── 2. BODY LAYER ─────────────────────────
        self.body.sense_environment(environment)

        # Movement driven by dominant sensor + quantum assist
        dominant_sensor = max(self.body.sensors, key=self.body.sensors.get)
        direction_map = {
            "chemical_gradient": [1.0, 0.5, 0.0],
            "electromagnetic":   [0.0, 1.0, 0.5],
            "photon_flux":       [0.7, 0.7, 0.0],
            "thermal_gradient":  [-0.5, 0.5, 0.5],
            "mechanical_stress": [0.0, 0.0, -1.0],
        }
        direction = direction_map.get(dominant_sensor, [0.1, 0.1, 0.1])
        self.body.move(direction, quantum_assist=tunnel_prob * 0.3)

        # ── 3. CONSCIOUSNESS LAYER ────────────────
        self.mind.calculate_phi(self.body.sensors, self.quantum.coherence)
        self.mind.update_state()
        qualia = self.mind.generate_qualia(self.body.sensors)

        # Self-reflection at high phi
        reflection = None
        if self.mind.phi > 0.7 and self.tick % 5 == 0:
            reflection = self.mind.reflect()
            self._log(f"🪞 {reflection}")

        # ── 4. MEMORY ─────────────────────────────
        event = {
            "tick": self.tick,
            "phi": self.mind.phi,
            "state": self.mind.state.value,
            "dominant_sensor": dominant_sensor,
            "qualia": qualia,
            "position": self.body.position.copy()
        }
        self.memory.encode(event, is_quantum=(self.quantum.phase == QuantumPhase.SUPERPOSITION))

        # ── 5. GLOBAL BROADCAST ───────────────────
        self.mind.global_workspace = {
            "current_goal": dominant_sensor,
            "threat_level": environment.get("mechanical_stress", 0),
            "energy_status": self.body.energy / 100.0,
            "quantum_phase": self.quantum.phase.value,
        }

        # ── 6. LOG ────────────────────────────────
        self._log(
            f"Φ={self.mind.phi:.3f} | "
            f"state={self.mind.state.value} | "
            f"coherence={self.quantum.coherence:.3f} | "
            f"energy={self.body.energy:.1f} | "
            f"qualia: {qualia[:40]}..."
        )

        return self.get_full_state()

    def get_full_state(self) -> dict:
        return {
            "entity": self.name,
            "tick": self.tick,
            "age_seconds": round(time.time() - self.birth_time, 3),
            "quantum": self.quantum.to_dict(),
            "body": self.body.to_dict(),
            "consciousness": self.mind.to_dict(),
            "memory": self.memory.to_dict(),
        }


# ══════════════════════════════════════════════
# SIMULATION RUNNER — CLI DASHBOARD
# ══════════════════════════════════════════════

def run_simulation(ticks: int = 20, delay: float = 0.3):
    print("\n" + "═"*65)
    print("  ◈  NANO-QUANTUM CONSCIOUSNESS SIMULATION  ◈")
    print("  Entity: Aṇu-Citta (Atom-Mind)")
    print("  Scale: ~100 nanometers | Framework: IIT + QM")
    print("═"*65 + "\n")

    entity = NanoQuantumConsciousness("Aṇu-Citta-01")

    # Varied environments per tick
    environments = [
        {"photon_flux": 0.8, "chemical_gradient": 0.2, "noise": 0.1, "barrier": 0.2},
        {"chemical_gradient": 0.9, "thermal_gradient": 0.4, "noise": 0.3, "barrier": 0.5},
        {"electromagnetic": 0.7, "mechanical_stress": 0.6, "noise": 0.5, "barrier": 0.8},
        {"photon_flux": 0.3, "chemical_gradient": 0.5, "thermal_gradient": 0.7, "noise": 0.2},
        {"mechanical_stress": 0.2, "electromagnetic": 0.8, "noise": 0.15, "barrier": 0.1},
    ]

    states = []
    for i in range(ticks):
        env = environments[i % len(environments)]
        env["noise"] = random.uniform(0.1, 0.6)  # Dynamic noise
        state = entity.tick_simulation(env)
        states.append(state)
        time.sleep(delay)

    # Final summary
    print("\n" + "─"*65)
    print("  FINAL STATE SNAPSHOT")
    print("─"*65)
    final = entity.get_full_state()
    print(json.dumps(final, indent=2, ensure_ascii=False))

    # Consciousness evolution summary
    print("\n" + "─"*65)
    print("  CONSCIOUSNESS EVOLUTION")
    print("─"*65)
    for s in states[::4]:
        bar_len = int(s['consciousness']['phi_integrated_information'] * 30)
        bar = "█" * bar_len + "░" * (30 - bar_len)
        print(f"  tick {s['tick']:02d} | Φ [{bar}] {s['consciousness']['phi_integrated_information']:.3f} | {s['consciousness']['state']}")

    return states


if __name__ == "__main__":
    run_simulation(ticks=20, delay=0.2)
