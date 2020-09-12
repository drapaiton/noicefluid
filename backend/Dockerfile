FROM python:3.8.5-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG REQUIREMENTS_FILENAME=base

# [Optional] Allow the vscode user to pip install globally w/o sudo
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
# RUN mkdir -p ${PIP_TARGET} \
#   && chown vscode:root ${PIP_TARGET} \
#   && echo "if [ \"\$(stat -c '%U' ${PIP_TARGET})\" != \"vscode\" ]; then chown -R vscode:root ${PIP_TARGET}; fi" \
#   | tee -a /root/.bashrc /home/vscode/.bashrc /root/.zshrc >> /home/vscode/.zshrc 

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update \
#   && export DEBIAN_FRONTEND=noninteractive \
#   && apt-get -y install --no-install-recommends \
#   nodejs gettext libpq-dev

RUN apt-get update && apt-get install -y \
  gettext \
  libpq-dev

# [Optional] If your package.json rarely change, uncomment this section to add them to the image.

COPY requirements /tmp/pip-tmp/
RUN pip install --upgrade pip \
  && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/${REQUIREMENTS_FILENAME}.txt \
  && rm -rf /tmp/pip-tmp

# give the vscode user permissions to modify the src folder
WORKDIR /code
COPY ./src/ /code/
# RUN chown vscode:root /code -R