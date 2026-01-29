from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask import render_template

load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.github_webhooks
collection = db.events


@app.route("/")
def home():
    return "Webhook server running"


# 🔥 WEBHOOK ENDPOINT
@app.route("/webhook", methods=["POST"])
def github_webhook():
    payload = request.json
    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "push":
        handle_push(payload)

    elif event_type == "pull_request":
        if payload["action"] == "closed" and payload["pull_request"]["merged"]:
            handle_merge(payload)
        else:
            handle_pull_request(payload)

    return jsonify({"status": "success"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    events = list(
        collection.find({}, {"_id": 0}).sort("timestamp", -1)
    )
    return jsonify(events)

@app.route("/ui")
def ui():
    return render_template("index.html")



def handle_push(payload):
    print("Handling PUSH event")

    data = {
        "author": payload["pusher"]["name"],
        "action": "PUSH",
        "from_branch": None,
        "to_branch": payload["ref"].split("/")[-1],
        "timestamp": payload["head_commit"]["timestamp"]
    }

    collection.insert_one(data)


def handle_pull_request(payload):
    print("Handling PULL REQUEST event")

    pr = payload["pull_request"]

    data = {
        "author": pr["user"]["login"],
        "action": "PULL_REQUEST",
        "from_branch": pr["head"]["ref"],
        "to_branch": pr["base"]["ref"],
        "timestamp": pr["created_at"]
    }

    collection.insert_one(data)

def handle_merge(payload):
    pr = payload["pull_request"]

    data = {
        "author": pr["user"]["login"],
        "action": "MERGE",
        "from_branch": pr["head"]["ref"],
        "to_branch": pr["base"]["ref"],
        "timestamp": pr["merged_at"]
    }

    collection.insert_one(data)


if __name__ == "__main__":
    app.run(debug=True)
