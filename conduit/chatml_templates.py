from jinja2 import Template
from conduit.memory.short_term import MemoryManager

memory = MemoryManager()

CHATML_CHAT_TEMPLATE = """{% for message in messages %}{{ '<|im_start|>' + message['role'] + '\n' + message['content'] + '\n<|im_end|>\n' }}{% endfor %}<|im_start|>assistant\n"""

template = Template(CHATML_CHAT_TEMPLATE)


def chat_prompt(user, system):

    history = memory.get() or []

    messages = [{"role": "system", "content": system}]

    messages.extend(history)

    messages.append({"role": "user", "content": user})

    return template.render(messages=messages)
