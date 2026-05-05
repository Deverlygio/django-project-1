import re

with open('store/templates/store/shop_list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire problematic section with correct syntax
old_section = '''                <select class="form-select" id="category" name="category">
                    <option value="">All Categories</option>
                    {% for cat_value, cat_label in categories %}
                    <option value="{{ cat_value }}" {% if selected_category==cat_value %}selected{% endif %}>{{
                        cat_label }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-3">
                <label for="store" class="form-label">Store</label>
                <select class="form-select" id="store" name="store">
                    <option value="">All Stores</option>
                    {% for store in stores %}
                    <option value="{{ store.id }}" {% if selected_store==store.id|stringformat:'s' %}selected{% endif
                        %}>{{ store.name }}</option>
                    {% endfor %}
                </select>'''

new_section = '''                <select class="form-select" id="category" name="category">
                    <option value="">All Categories</option>
                    {% for cat_value, cat_label in categories %}
                    <option value="{{ cat_value }}" {% if selected_category == cat_value %}selected{% endif %}>{{ cat_label }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-3">
                <label for="store" class="form-label">Store</label>
                <select class="form-select" id="store" name="store">
                    <option value="">All Stores</option>
                    {% for store in stores %}
                    <option value="{{ store.id }}" {% if selected_store == store.id|stringformat:'s' %}selected{% endif %}>{{ store.name }}</option>
                    {% endfor %}
                </select>'''

if old_section in content:
    content = content.replace(old_section, new_section)
    with open('store/templates/store/shop_list.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('✓ All template issues fixed')
else:
    print('Section not found, trying regex approach...')
    # Try with flexible whitespace
    pattern = r'<select class="form-select" id="category".*?</select>\s*</div>\s*<div class="col-md-3">.*?<select class="form-select" id="store".*?</select>'
    
    if re.search(pattern, content, re.DOTALL):
        print('Pattern found, replacing...')
        # Apply simpler fixes
        content = re.sub(r'selected_category==cat_value', 'selected_category == cat_value', content)
        content = re.sub(r'selected_store==store\.id', 'selected_store == store.id', content)
        content = re.sub(r'%}>\{\{(\s+)cat_label', '%}}>{{ cat_label', content)
        content = re.sub(r'%}\n\s*%}>{{ store.name', '%}}>{{ store.name', content)
        
        with open('store/templates/store/shop_list.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('✓ Applied regex fixes')
    else:
        print('Pattern not found')
