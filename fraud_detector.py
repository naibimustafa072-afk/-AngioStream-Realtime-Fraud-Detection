"""
AngioStream - Real-Time Distributed AI Fraud Detection Engine
Processed via Gemini 2.0 Flash Simulation Pipeline
"""

import asyncio
import time
import random
import logging

# Configure structured logging for financial auditing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FraudDetector:
    def __init__(self):
        self.cached_transactions = {}
        self.latency_records = []
        self.total_blocked = 0
        self.total_processed = 0

    async def evaluate_transaction(self, tx_data: dict) -> dict:
        """
        Evaluates incoming transaction events in real-time.
        Target processing latency: Sub-10ms (Simulated at 0.07ms)
        """
        start_time = time.time()
        self.total_processed += 1
        
        is_fraud = False
        reason = "Approved"
        
        # Rule 1: High Amount Spike Detection (Anti-Money Laundering Threshold)
        if tx_data['amount'] > 5000:
            is_fraud = True
            reason = "High Amount Spike Detected (> $5000)"
            
        # Rule 2: Suspicious Geolocation Velocity Mismatch
        elif tx_data['location'] == "Unknown":
            is_fraud = True
            reason = "Suspicious Geolocation Velocity Mismatch"
            
        # Rule 3: High-Risk Fixed Pattern Detection
        elif tx_data['amount'] == 747:
            is_fraud = True
            reason = "Flagged High-Risk Fixed Amount Pattern"

        # Simulate sub-millisecond evaluation latency (0.07ms)
        await asyncio.sleep(0.00007) 
        
        latency_ms = (time.time() - start_time) * 1000
        self.latency_records.append(latency_ms)
        
        decision = "AUTO BLOCK" if is_fraud else "APPROVED"
        if is_fraud:
            self.total_blocked += 1
            
        return {
            "transaction_id": tx_data['id'],
            "amount": tx_data['amount'],
            "location": tx_data['location'],
            "decision": decision,
            "reason": reason,
            "latency_ms": round(latency_ms, 4)
        }

async def stream_simulation():
    detector = FraudDetector()
    logging.info("🚀 AngioStream Real-Time Engine Started - Processing at 10 TPS...")
    
    sample_locations = ["United States", "United Kingdom", "Germany", "Unknown", "France", "Japan"]
    
    # Simulating a live batch of high-frequency transactions
    for _ in range(1, 25):
        tx = {
            "id": f"tx_{random.randint(100000, 999999)}",
            "amount": random.choice([45.99, 120.00, 550.50, 747.00, 1200.00, 6200.00, 89.90]),
            "location": random.choice(sample_locations)
        }
        
        result = await detector.evaluate_transaction(tx)
        
        log_msg = (
            f"| ID: {result['transaction_id']} "
            f"| Amount: ${result['amount']:<7} "
            f"| Location: {result['location']:<14} "
            f"| Decision: {result['decision']:<10} "
            f"| Reason: {result['reason']:<40} "
            f"| Latency: {result['latency_ms']}ms |"
        )
        
        if result['decision'] == "AUTO BLOCK":
            logging.warning(log_msg)
        else:
            logging.info(log_msg)
            
        # Maintain stable 10 Transactions Per Second (TPS) throughput
        await asyncio.sleep(0.1)

    logging.info(f"📊 Simulation Finished. Processed: {detector.total_processed} | Blocked Threats: {detector.total_blocked}")

if __name__ == "__main__":
    asyncio.run(stream_simulation())
