"""Entry point: ``python -m higgsfield_unlimited_mcp`` and the
``higgsfield-unlimited-mcp`` console script.

CLI flags are parsed here, *before* any config load, so ``--help`` works
without credentials and command-line flags always take precedence over the
``MCP_*`` environment variables.
"""

from __future__ import annotations

import argparse

from .server import run


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="higgsfield-unlimited-mcp",
        description=(
            "Higgsfield Unlimited MCP server. stdio by default (desktop clients); "
            "use --transport streamable-http to expose a remote MCP endpoint."
        ),
    )
    parser.add_argument(
        "--transport",
        choices=("stdio", "sse", "streamable-http"),
        default=None,
        help=(
            "Transport to serve (default: stdio, or $MCP_TRANSPORT). "
            "streamable-http serves MCP at /mcp; sse at /sse."
        ),
    )
    parser.add_argument(
        "--host",
        default=None,
        help=(
            "Bind address for HTTP transports (default: 127.0.0.1, or "
            "$MCP_HTTP_HOST; use 0.0.0.0 to accept network connections)."
        ),
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port for HTTP transports (default: 8000, or $MCP_HTTP_PORT).",
    )
    args = parser.parse_args()
    run(transport=args.transport, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
