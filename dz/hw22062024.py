from jinja2 import Template


pages = [
    {'link': '/index', 'page': 'Главная'},
    {'link': '/news', 'page': 'Новости'},
    {'link': '/about', 'page': 'О компании'},
    {'link': '/shop', 'page': 'Магазин'},
    {'link': '/contacts', 'page': 'Контакты'}
]

link = """
<ul>{% for p in pages -%}
{% if p.page == "Главная" %}
<li><a href="{{ p['link'] }} class='active'">{{ p['page'] }}</a></li>
{% else -%}
<li><a href="{{ p['link'] }}">{{ p['page'] }}</a></li>    
{% endif -%}
{% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(pages=pages)
print(msg)