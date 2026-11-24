from app import main


def test_greeting(capsys):
    main()
    assert "Hello, Jenkins!" in capsys.readouterr().out


def test_webhook_message(capsys):
    main()
    assert "Testing Webhook" in capsys.readouterr().out