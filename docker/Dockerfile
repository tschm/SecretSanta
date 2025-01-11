# Use a more specific Python slim image to reduce size
FROM python:3.12-slim

# Set environment variables in one layer
ENV PATH="/home/user/.local/bin:$PATH" \
    UV_SYSTEM_PYTHON=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Create non-root user first to minimize layer rebuild
RUN useradd -m -u 1000 user

# Copy uv binary and make it executable in one layer
COPY --from=ghcr.io/astral-sh/uv:0.5.17 /uv /bin/uv
RUN chmod +x /bin/uv

# Set working directory and switch to user early
WORKDIR /app

# Copy and install requirements first to leverage caching
# You need to be root if you install into the "system"
COPY --chown=user:user ./requirements.txt requirements.txt
RUN uv pip install -r requirements.txt

USER user

# Copy application code
COPY --chown=user:user . .

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:7860/ || exit 1

# Expose port
EXPOSE 7860

# Use exec form of ENTRYPOINT with CMD for proper signal handling
ENTRYPOINT ["marimo"]
CMD ["run", "app.py", "--host", "0.0.0.0", "--port", "7860"]
