FROM ubuntu:latest
LABEL authors="alexcooke"

ENTRYPOINT ["top", "-b"]