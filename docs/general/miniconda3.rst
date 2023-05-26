{% set title = miniconda3.get("name") %}
.. _miniconda3:

**************************
{{title}}
**************************

{% block content %}
    {{ miniconda3.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in miniconda3.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI-AI Container Hub Specifications
======================================

{% block hub_specifications %}
    {% for dc in miniconda3.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ miniconda3.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ miniconda3.docker_run_command }}

{% block note %}
{% if miniconda3.note != "" %}
.. note::

        {{ miniconda3.note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in miniconda3.image_specifications %}
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