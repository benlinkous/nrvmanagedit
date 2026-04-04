#!/usr/bin/env python3
"""
Zero Trust Online Verification — Teaser Search Backend
=======================================================
Runs free tools (Sherlock + Holehe) to generate teaser results.
Full report triggers the paid AI pipeline.

Install:
    pip3 install flask sherlock-project holehe --break-system-packages

Run:
    python3 teaser_backend.py
    Then open http://localhost:5000
"""

import os
import json
import subprocess
import asyncio
import re
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__, static_folder='.')

# ══════════════════════════════════════════════════════════════════════════════
# TEASER SEARCH — runs free tools only, zero API cost
# ══════════════════════════════════════════════════════════════════════════════

def run_sherlock(username: str) -> dict:
    """Run Sherlock username search and return summary."""
    try:
        result = subprocess.run(
            ["sherlock", username, "--timeout", "10", "--print-found"],
            capture_output=True, text=True, timeout=60
        )
        output = result.stdout

        # Parse found sites
        found_sites = []
        for line in output.split('\n'):
            if '[+]' in line:
                site = line.split('[+]')[1].strip().split(':')[0].strip()
                found_sites.append(site)

        # Categorize sites
        dating_keywords = ['tinder', 'hinge', 'bumble', 'match', 'okcupid', 'pof', 
                          'zoosk', 'badoo', 'plenty', 'eharmony', 'coffee', 'feeld',
                          'grindr', 'her', 'scruff']
        social_keywords = ['instagram', 'facebook', 'twitter', 'tiktok', 'snapchat',
                          'linkedin', 'pinterest', 'tumblr', 'reddit']

        dating_found = [s for s in found_sites if any(d in s.lower() for d in dating_keywords)]
        social_found = [s for s in found_sites if any(s_k in s.lower() for s_k in social_keywords)]
        other_found = [s for s in found_sites if s not in dating_found and s not in social_found]

        return {
            "success": True,
            "total_found": len(found_sites),
            "dating_platforms": len(dating_found),
            "social_platforms": len(social_found),
            "other_platforms": len(other_found),
            "dating_found": dating_found,
            "social_found": social_found,
            "sample_sites": found_sites[:3],  # Only show 3 for teaser
        }

    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Search timed out"}
    except FileNotFoundError:
        return {"success": False, "error": "Sherlock not installed"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def run_holehe(email: str) -> dict:
    """Run Holehe email check and return summary."""
    try:
        result = subprocess.run(
            ["holehe", email, "--only-used"],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout

        found_sites = []
        for line in output.split('\n'):
            if '[+]' in line:
                site = line.replace('[+]', '').strip()
                found_sites.append(site)

        dating_keywords = ['tinder', 'hinge', 'bumble', 'match', 'okcupid', 'badoo', 'zoosk']
        dating_found = [s for s in found_sites if any(d in s.lower() for d in dating_keywords)]

        return {
            "success": True,
            "total_found": len(found_sites),
            "dating_platforms": len(dating_found),
            "dating_found": dating_found,
            "sample_sites": found_sites[:3],
        }

    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Search timed out"}
    except FileNotFoundError:
        return {"success": False, "error": "Holehe not installed"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def generate_teaser(query: str, query_type: str) -> dict:
    """
    Run appropriate free tools and return teaser data.
    query_type: 'username' | 'email' | 'name'
    """
    teaser = {
        "query": query,
        "query_type": query_type,
        "timestamp": datetime.now().isoformat(),
        "platforms_searched": 400,
        "results": {}
    }

    if query_type == "username":
        sherlock_data = run_sherlock(query)
        teaser["results"]["sherlock"] = sherlock_data

        if sherlock_data.get("success"):
            total = sherlock_data["total_found"]
            dating = sherlock_data["dating_platforms"]

            # Build risk signals
            signals = []
            if dating > 0:
                signals.append(f"Active on {dating} dating platform{'s' if dating > 1 else ''}")
            if total > 10:
                signals.append(f"Significant online presence detected ({total} platforms)")
            if total < 3:
                signals.append("Minimal digital footprint — unusual for active adult")

            teaser["summary"] = {
                "platforms_found": total,
                "dating_platforms": dating,
                "risk_signals": signals,
                "risk_level": "HIGH" if dating > 1 else "MEDIUM" if dating > 0 or total < 3 else "LOW",
                "sample_platforms": sherlock_data.get("sample_sites", []),
                "hidden_count": max(0, total - 3),
            }

    elif query_type == "email":
        holehe_data = run_holehe(query)
        teaser["results"]["holehe"] = holehe_data

        if holehe_data.get("success"):
            total = holehe_data["total_found"]
            dating = holehe_data["dating_platforms"]

            signals = []
            if dating > 0:
                signals.append(f"Email registered on {dating} dating platform{'s' if dating > 1 else ''}")
            if total > 5:
                signals.append(f"Email active across {total} services")

            teaser["summary"] = {
                "platforms_found": total,
                "dating_platforms": dating,
                "risk_signals": signals,
                "risk_level": "HIGH" if dating > 1 else "MEDIUM" if dating > 0 else "LOW",
                "sample_platforms": holehe_data.get("sample_sites", []),
                "hidden_count": max(0, total - 3),
            }

    elif query_type == "name":
        # Name search uses Sherlock with cleaned version
        clean_name = query.lower().replace(' ', '')
        sherlock_data = run_sherlock(clean_name)
        teaser["results"]["sherlock"] = sherlock_data

        if sherlock_data.get("success"):
            total = sherlock_data["total_found"]
            dating = sherlock_data["dating_platforms"]

            signals = []
            if dating > 0:
                signals.append(f"Potential matches on {dating} dating platform{'s' if dating > 1 else ''}")
            if total > 0:
                signals.append(f"{total} potential profile matches found")

            teaser["summary"] = {
                "platforms_found": total,
                "dating_platforms": dating,
                "risk_signals": signals,
                "risk_level": "MEDIUM" if dating > 0 else "LOW",
                "sample_platforms": sherlock_data.get("sample_sites", []),
                "hidden_count": max(0, total - 3),
            }

    return teaser


# ══════════════════════════════════════════════════════════════════════════════
# ROUTES
# ══════════════════════════════════════════════════════════════════════════════

@app.route('/')
def index():
    return send_from_directory('.', 'teaser_frontend.html')

@app.route('/api/teaser', methods=['POST'])
def teaser_search():
    data = request.json
    query = data.get('query', '').strip()
    query_type = data.get('type', 'username')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    if len(query) < 2:
        return jsonify({"error": "Query too short"}), 400

    result = generate_teaser(query, query_type)
    return jsonify(result)

@app.route('/api/order', methods=['POST'])
def place_order():
    """Handle order for full report."""
    data = request.json
    query = data.get('query')
    query_type = data.get('type')
    tier = data.get('tier', 'standard')
    email = data.get('email')

    # In production: save to database, send notification email, trigger pipeline
    order = {
        "order_id": f"ZT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "query": query,
        "type": query_type,
        "tier": tier,
        "email": email,
        "status": "received",
        "timestamp": datetime.now().isoformat()
    }

    # Save order to file (replace with database in production)
    orders_file = "orders.json"
    orders = []
    if os.path.exists(orders_file):
        with open(orders_file) as f:
            orders = json.load(f)
    orders.append(order)
    with open(orders_file, 'w') as f:
        json.dump(orders, f, indent=2)

    print(f"\n🔔 NEW ORDER: {order['order_id']} — {tier} — {query}")

    return jsonify({
        "success": True,
        "order_id": order["order_id"],
        "message": "Order received. You will receive your report within 24 hours."
    })

@app.route('/api/orders', methods=['GET'])
def list_orders():
    """View all orders (your dashboard)."""
    if os.path.exists("orders.json"):
        with open("orders.json") as f:
            return jsonify(json.load(f))
    return jsonify([])


if __name__ == '__main__':
    print("\n" + "="*50)
    print("  Zero Trust Online Verification")
    print("  Teaser Search Backend")
    print("="*50)
    print("  Running at: http://localhost:5000")
    print("  Orders saved to: orders.json")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
