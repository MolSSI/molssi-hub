{% set title = debian_bullseye_slim_dev.get("name") %}
.. _debian_bullseye_slim_dev:

**************************
{{title}}
**************************

{% block content %}
    {{ debian_bullseye_slim_dev.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in debian_bullseye_slim_dev.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI-AI Container Hub Specifications
======================================

{% block hub_specifications %}
    {% for dc in debian_bullseye_slim_dev.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ debian_bullseye_slim_dev.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ debian_bullseye_slim_dev.docker_run_command }}

{% block note %}
{% if debian_bullseye_slim_dev.note != "" %}
.. note::

        {{ debian_bullseye_slim_dev.note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in debian_bullseye_slim_dev.image_specifications %}
        {% for key, value in dc.items() %}
            {% if dc[key] is string or dc[key] == "" %}
                * **{{ key }}**: {{ value }}
            {% else %}
                * **{{ key }}**:
                {% for key2 in dc[key] %}
                    {% for key3, val3 in key2.items() %}
                        + *{{ key3 }}*: {{ val3 }}
                    {% endfor %}
                {% endfor %}
            {% endif %}
        {% endfor %}
    {% endfor %}
{% endblock image_specifications %}