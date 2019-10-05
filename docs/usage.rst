=====
Usage
=====

The code for adding this functionality to your docs is on `this
page <https://raw.githubusercontent.com/metatooling/interdoc/master/docs/usage.rst>`__.
Keep in mind this is at the proof-of-concept stage.



To add this logic in any other repository, just copy this into it.


The code for adding this functionality to your docs is on `this page <https://raw.githubusercontent.com/metatooling/interdoc/master/docs/usage.rst>`__. Keep in mind this is at the proof-of-concept stage.



.. raw:: html

    <script src="//cdn.jsdelivr.net/npm/medium-editor@latest/dist/js/medium-editor.min.js"></script>
    <script src="//cdn.jsdelivr.net/gh/metatooling/medium-button/src/medium-button.js"></script>
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/medium-editor@latest/dist/css/medium-editor.min.css" type="text/css" media="screen" charset="utf-8">

    <script>
    var editor = new MediumEditor('body p');


     editor.subscribe('focus', function(data, editable) { if (!editable.hasAttribute('data-original')) {
     editable.dataset.original = editable.innerText};
                                                        });

     editor.subscribe('blur', function(data, editable) {
     old_html = editable.dataset.original;
     new_html = editable.innerHTML;
     if (old_html == new_html) {
         return;
     }
     index = editable.dataset.mediumEditorEditorIndex;
     var xhr = new XMLHttpRequest();
     xhr.open("POST", 'https://cors-anywhere.herokuapp.com/https://sleepy-harbor-00552.herokuapp.com/', true);
     xhr.setRequestHeader('Content-Type', 'application/json');
     data = {
         index: index,
         old_html: old_html,
         new_html: new_html,
         rendered_html_url: document.URL,
         rendered_rst_url: document.evaluate('//a[@class="fa fa-github"]', document, null, XPathResult.ANY_TYPE, null).iterateNext().href
    };
    xhr.send(JSON.stringify(data))});

    </script>
