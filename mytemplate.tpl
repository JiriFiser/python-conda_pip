{% extends 'full.tpl'%}
{% block any_cell %}
{% if 'h' in cell['metadata'].get('tags', []) %}
    <div>
    <input type="button" 
           onclick="this.parentNode.getElementsByClassName('hsolution')[0].style.visibility='visible'"   
           value="Řešení">
    <div style="visibility: hidden" class="hsolution">
        {{ super() }}
    </div>
    </div>
{% else %}
    {{ super() }}
{% endif %}
{% endblock any_cell %}
