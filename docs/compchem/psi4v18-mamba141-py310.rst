{% set title = psi4v18_mamba141_py310.get("name") %}
.. _psi4v18_mamba141_py310:

*************
{{title}}
*************

{% block content %}
    {{ psi4v18_mamba141_py310.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in psi4v18_mamba141_py310.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI-AI Container Hub Specifications
======================================

{% block hub_specifications %}
    {% for dc in psi4v18_mamba141_py310.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ psi4v18_mamba141_py310.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ psi4v18_mamba141_py310.docker_run_command }}

{% block note %}
{% if psi4v18_mamba141_py310.gpu_note != "" %}
.. note::

        {{ psi4v18_mamba141_py310.gpu_note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in psi4v18_mamba141_py310.image_specifications %}
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