from _pytest.capture import capsys, CaptureResult

from context_managers.hello_world_context_manager import HelloWorldContextManager, hello_world_context_manger_method


class TestHelloWorldContextManagerClass:
    def test_hello_world_context_manager_class(self, capsys):
        with HelloWorldContextManager() as hello_world:
            assert "Hello, World!" == hello_world

        captured: CaptureResult = capsys.readouterr()
        assert captured.out == "Entering the context\nExiting the context\n"

    def test_hello_world_context_manager_function(self, capsys):
        with hello_world_context_manger_method() as hello_world:
            assert "Hello, World!" == hello_world

        captured: CaptureResult = capsys.readouterr()
        assert captured.out == "Entering the context\nExiting the context\n"
