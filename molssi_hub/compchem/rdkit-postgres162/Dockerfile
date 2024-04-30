FROM postgres:16.2

LABEL maintainer="Jessica A. Nash, \
                  Molecular Sciences Software Institute"

RUN apt update && \
    apt install -y --no-install-recommends postgresql-16-rdkit && \
    rm -rf /var/lib/apt/lists/*