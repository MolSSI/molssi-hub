.. _torchani223_mamba141_ase322:

*********************************************************
{{ torchani223_mamba141_ase322.hub_specifications[0]["Source"].split("/")[-1] }}
*********************************************************

{% set title = torchani223_mamba141_ase322.get("name") %}

{{title}}
=========================================================

{% block content %}
    {{ torchani223_mamba141_ase322.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in torchani223_mamba141_ase322.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI Container Hub Specifications
===================================

{% block hub_specifications %}
    {% for dc in torchani223_mamba141_ase322.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ torchani223_mamba141_ase322.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ torchani223_mamba141_ase322.docker_run_command }}

{% block note %}
{% if torchani223_mamba141_ase322.note != "" %}
.. note::

        {{ torchani223_mamba141_ase322.note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in torchani223_mamba141_ase322.image_specifications %}
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