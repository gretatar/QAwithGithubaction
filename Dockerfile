FROM python:3.13-slim
WORKDIR /app
# Copy only the app source for a small runtime image.
COPY src ./src
COPY test ./test

# Copy dependencies first to leverage Docker layer caching.
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "src/app.py"]
