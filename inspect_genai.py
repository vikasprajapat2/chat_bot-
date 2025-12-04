import google.generativeai as genai
import inspect

print('genai module attributes:')
for name in dir(genai):
    if not name.startswith('_'):
        print(name)

# Try to inspect GenerativeModel if present
if hasattr(genai, 'GenerativeModel'):
    print('\nGenerativeModel methods:')
    print([m for m in dir(genai.GenerativeModel) if not m.startswith('_')])

# Try to list models if available
if hasattr(genai, 'list_models'):
    print('\nCalling list_models()...')
    models = genai.list_models()
    print(models)
else:
    print('\nNo list_models() in genai module')
