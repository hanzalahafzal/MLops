from unittest.mock import patch
import app


def test_summarize_text_logic():
    mock_response = [{"summary_text": "This is a simulated summary."}]
    with patch.object(app, "summarization_pipeline", return_value=mock_response):
        result = app.summarize_text("Test input text block.")
        assert result == "This is a simulated summary."
