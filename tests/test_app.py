from fastapi.testclient import TestClient

from src.app import activities, app

client = TestClient(app)


def test_unregister_removes_participant():
    original_participants = activities["Chess Club"]["participants"].copy()
    activities["Chess Club"]["participants"].append("test@example.com")

    try:
        response = client.delete("/activities/Chess Club/unregister?email=test@example.com")

        assert response.status_code == 200
        assert "test@example.com" not in activities["Chess Club"]["participants"]
    finally:
        activities["Chess Club"]["participants"] = original_participants


def test_unregister_returns_400_for_missing_participant():
    response = client.delete("/activities/Chess Club/unregister?email=missing@example.com")

    assert response.status_code == 400
