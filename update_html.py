# Ajouter des styles pour les images
styles_to_add = """
        .about-image {
            width: 100%;
            height: 400px;
            border-radius: 12px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            object-fit: contain;
            background: white;
        }
        
        .product-image {
            width: 100%;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f9f9f9;
            overflow: hidden;
        }
        
        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            padding: 10px;
        }
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Vérifier et ajuster les styles
if 'object-fit: contain' not in html:
    # Ajouter après le style product-image existant
    html = html.replace(
        '.product-image img {',
        '.product-image img {\n            object-fit: contain !important;\n            padding: 10px;'
    )
    
    html = html.replace(
        '.about-image {',
        '.about-image {\n            object-fit: contain !important;'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Styles CSS optimisés pour images")

