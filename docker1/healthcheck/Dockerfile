FROM nginx:1.17.7
RUN apt-get update && apt-get install -y wget
HEALTHCHECK --interval=5m --timeout=3s CMD wget -q --method=HEAD localhost/system-status.txt || exit 1
