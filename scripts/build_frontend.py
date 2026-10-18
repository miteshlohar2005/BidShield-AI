import os
import re

def build():
    with open('frontend/index.html', 'r', encoding='utf-8') as f:
        original = f.read()

    seed_match = re.search(r'(<script type="application/json" id="pp-seed">[\s\S]*?</script>)', original)
    if not seed_match:
        raise ValueError("Could not find pp-seed in original index.html")
    pp_seed_html = seed_match.group(1)

    engine_match = re.search(r'(/\* ENGINE START[\s\S]*?/\* ENGINE END \*/)', original)
    if not engine_match:
        raise ValueError("Could not find PPEngine in original index.html")
    engine_js = engine_match.group(1)

    with open('scripts/template.html', 'r', encoding='utf-8') as tf:
        tpl = tf.read()

    final_html = tpl.replace('__PP_SEED__', pp_seed_html).replace('__ENGINE_JS__', engine_js)

    with open('frontend/index.html', 'w', encoding='utf-8') as out_f:
        out_f.write(final_html)

    print("Successfully built frontend/index.html!")

if __name__ == '__main__':
    build()
