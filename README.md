# 🚀 AngioStream: Real-Time Stream AI Fraud Detection Engine

AngioStream is an enterprise-grade, high-throughput financial transaction fraud detection engine built to intercept and mitigate high-risk malicious activities with sub-millisecond evaluation latency.

## 🌟 Key Features
- **High-Throughput Stream Ingestion:** Designed to simulate continuous high-frequency transaction data streams processing at a stable 10 TPS.
- **Stateless AI Evaluation Logic:** Features automated real-time statistical anomaly detection mechanisms to flag instant velocity changes, amount spikes, and suspicious geolocation mismatches.
- **Autonomous Threat Mitigation:** Implements an optimized "Auto-Block" loop, dynamically defending the financial ledger from fraudulent actions within a sub-10ms target loop.
- **Architectural Scalability:** Structured mimicking modern microservices architectures utilizing decoupled ingestors, localized in-memory cache states, and optimized auditing layers.

## 🛠️ Tech Stack & Concepts
- **Core Language:** Python (Asyncio / Advanced Event Loops)
- **Architecture Patterns:** Event-Driven Architecture (EDA), Stream Processing, Pessimistic Locking Concepts
- **Data Engineering:** High-frequency logging, structured financial auditing, in-memory validation simulation

## 📊 Core Detection Rules Applied
1. **Amount Spike Detection:** Intercepts any high-volume transactions instantly matching Anti-Money Laundering (AML) risk thresholds (> $5000).
2. **Velocity & Geolocation Check:** Flags rapid consecutive transactions from blacklisted or structurally mismatched geolocations.
3. **Fixed High-Risk Patterns:** Evaluates historical telemetry to auto-block known structural system vulnerabilities.
