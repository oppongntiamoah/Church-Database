from apps.account.models import Config

@register.simple_tag(takes_context=True)
def config(context):
    request = context.get("request")
    return "It Works!"
