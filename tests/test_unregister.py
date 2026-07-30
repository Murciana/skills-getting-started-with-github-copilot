from fastapi.testclient import TestClient

from src.app import activities, app


def test_unregister_participant_removes_email():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    original_participants = list(activities[activity_name]["participants"])

    try:
        response = client.post(
            f"/activities/{activity_name}/unregister?email={email}",
            timeout=5,
        )

        assert response.status_code == 200
        assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
        assert email not in activities[activity_name]["participants"]
    finally:
        activities[activity_name]["participants"] = original_participants
