.. _pyscf221_base_mamba141_jupyter:

*********************************************************
{{ pyscf221_base_mamba141_jupyter.hub_specifications[0]["Github"].split("/")[-1] }}
*********************************************************

{% set title = pyscf221_base_mamba141_jupyter.get("name") %}

{{title}}
=========================================================

{% block content %}
    {{ pyscf221_base_mamba141_jupyter.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in pyscf221_base_mamba141_jupyter.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI-AI Container Hub Specifications
======================================

{% block hub_specifications %}
    {% for dc in pyscf221_base_mamba141_jupyter.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ pyscf221_base_mamba141_jupyter.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ pyscf221_base_mamba141_jupyter.docker_run_command }}

{% block note %}
{% if pyscf221_base_mamba141_jupyter.note != "" %}
.. note::

        {{ pyscf221_base_mamba141_jupyter.note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in pyscf221_base_mamba141_jupyter.image_specifications %}
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