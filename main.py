import argparse
import socket


def find_free_port(start_port=7860, max_port=9000):
    """Find an available port starting from start_port up to max_port."""
    for port in range(start_port, max_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise OSError(f"No free port found between {start_port} and {max_port}")


def main():
    parser = argparse.ArgumentParser(
        description="Smart Contract Assistant - AI Q&A for Smart Contracts"
    )
    parser.add_argument(
        "--mode",
        choices=["ui", "api"],
        default="ui",
        help="Launch mode: 'ui' for Gradio interface, 'api' for FastAPI server (default: ui)",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port to bind to (default: auto-select starting at 7860)",
    )

    args = parser.parse_args()

    # إذا المستخدم ما حددش بورت، نلاقي بورت فاضي تلقائي
    port_to_use = args.port if args.port else find_free_port(7860, 9000)

    if args.mode == "ui":
        print(f"🚀 Launching Smart Contract Assistant (Gradio UI) on port {port_to_use}...")
        from ui.gradio_app import create_app, APP_THEME, APP_CSS

        app = create_app()
        app.launch(
            server_name=args.host,
            server_port=port_to_use,
            share=False,
            theme=APP_THEME,
            css=APP_CSS,
        )

    elif args.mode == "api":
        print(f"🚀 Launching Smart Contract Assistant (FastAPI) on port {port_to_use}...")
        import uvicorn

        uvicorn.run(
            "server.server:app",
            host=args.host,
            port=port_to_use,
            reload=True,
        )


if __name__ == "__main__":
    main()