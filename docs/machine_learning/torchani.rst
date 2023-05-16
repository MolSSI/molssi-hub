{% set page_name = TorchANI.get("name") %}
.. _{{ page_name }}:

*************
{{page_name}}
*************

{% block content %}
    {{ TorchANI.description }}
{% endblock content %}

Source Specifications
=====================

{% block specifications %}
    {% for dc in TorchANI.source_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock specifications %}

MolSSI-AI Container Hub Specifications
======================================

{% block hub_specifications %}
    {% for dc in TorchANI.hub_specifications %}
        {% for key, value in dc.items() %}
            * **{{ key }}**: {{ value }}
        {% endfor %}
    {% endfor %}
{% endblock hub_specifications %}

* **Image pull command**:

    .. code-block:: bash

        {{ TorchANI.docker_pull_command }}

* **Container run command**:

    .. code-block:: bash

        {{ TorchANI.docker_run_command }}

.. note::

        {{ TorchANI.gpu_note }}

Image Specifications
====================

{% block image_specifications %}
    {% for dc in TorchANI.image_specifications %}
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