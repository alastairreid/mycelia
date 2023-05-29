-------------------------------------------------------------

{% assign label = page.id | replace_first: "/", "" %}

{% assign refs = site.data.backrefs["notes"][label] %}
{% if refs.size > 0 %}
## Hyphae related to {{page.title}}
{% for p in refs %} <a href="{{ site.baseurl }}/{{ p[0] }}">{{ p[1][0] }}</a>{% if forloop.last %}{% else %},{% endif %} {% endfor %}
{% endif %}

{% for x in page.examples %}
[{{x}}]: {{site.baseurl}}/hyphae/{{x | replace: ' ', '-' | downcase}}
{% endfor %}
{% for x in page.notes %}
[{{x}}]: {{site.baseurl}}/hyphae/{{x | replace: ' ', '-' | downcase}}
{% endfor %}