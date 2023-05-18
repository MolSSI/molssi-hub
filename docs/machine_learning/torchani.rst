{% set title = torchani.get("name") %}
.. _ torchani:

*************
{{title}}
*************

{% block content %}
    {{ torchani.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in torchani.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI-AI Container Hub Specifications
======================================

{% block hub_specifications %}
    {% for dc in torchani.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ torchani.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ torchani.docker_run_command }}

{% block note %}
{% if torchani.gpu_note != "" %}
.. note::

        {{ torchani.gpu_note }}
{% endif %}
{% endblock note %}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in torchani.image_specifications %}
        {% for key, value in dc.items() %}
            {% if key != "Extras" %}
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