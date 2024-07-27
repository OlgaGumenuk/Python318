from jinja2 import Template

field = """
{% macro input_func(name, placeholder, type="text") -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{%- endmacro -%}

<p>{{ input_func('firstname', 'Имя') }}</p>
<p>{{ input_func('lastname', 'Фамилия') }}</p>
<p>{{ input_func('address', 'Адрес') }}</p>
<p>{{ input_func('phone', 'Телефон') }}</p>
<p>{{ input_func('email', 'Почта') }}</p>

"""

tm = Template(field)
msg = tm.render()

print(msg)