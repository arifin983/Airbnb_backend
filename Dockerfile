# Set the python version as a build-time argument
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION} as base

# Create a virtual environment
RUN python -m venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install OS dependencies for Python packages
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Use a build stage to install dependencies
FROM base as builder

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt /tmp/requirements.txt

# Install the Python project requirements
RUN pip install -r /tmp/requirements.txt

# Copy the project code into the container
COPY ./src /code

# Set the working directory to the project code
WORKDIR /code

# Collect static files if needed
# RUN python manage.py collectstatic --no-input

# Set the Django default project name
ARG PROJ_NAME="backend"

# Create a bash script to run the Django project with Daphne (ASGI)
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "daphne -b 0.0.0.0 -p \$RUN_PORT ${PROJ_NAME}.asgi:application\n" >> ./paracord_runner.sh

# Make the bash script executable
RUN chmod +x paracord_runner.sh

# Final stage for running the container
FROM base

# Copy the installed dependencies and code from the builder stage
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /code /code

# Run the Django project via the runtime script
CMD ./paracord_runner.sh
