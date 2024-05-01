.. _rdkit_postgres162:

*********************************************************
{{ rdkit_postgres162.hub_specifications[0]["Source"].split("/")[-1] }}
*********************************************************

{% set title = rdkit_postgres162.get("name") %}

{{title}}
=========================================================

{% block content %}
    {{ rdkit_postgres162.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in rdkit_postgres162.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI Container Hub Specifications
===================================

{% block hub_specifications %}
    {% for dc in rdkit_postgres162.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ rdkit_postgres162.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ rdkit_postgres162.docker_run_command }}

{% block note %}
{% if rdkit_postgres162.note != "" %}
.. note::

        {{ rdkit_postgres162.note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in rdkit_postgres162.image_specifications %}
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