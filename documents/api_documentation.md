# English-Hindi Dictionary 

### Generating Dictionary Information
You can return characteristics such as the Romanised Hindi and Devanagari script counterparts for the English input provided by using the "Generate" interface.
Enter a word, such as `water`, into the box and click "Generate". The page will then display the information it has for that word. Supported input forms at this time are "book", "tea", "water", and "you".
For example:
````
'water','pānī','पानी','noun','m','a liquid that descends from the clouds as rain, forms streams, lakes, and rivers'
````
The endpoint to access this interface directly is `http://localhost:5000/generate_form`.

You can also connect using curl, for example: `curl "http://localhost:5000/generate?input_form=water`
