=====
Usage
=====

You can edit this page to improve the documentation. Just click on the text you want to edit. Then find your pull request `on GitHub <https://github.com/metatooling/interdoc/pulls>`__.

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
     index = editable.dataset.mediumEditorEditorIndex;
     var xhr = new XMLHttpRequest();
     xhr.open("POST", 'https://cors-anywhere.herokuapp.com/https://sleepy-harbor-00552.herokuapp.com/', true);
     xhr.setRequestHeader('Content-Type', 'application/json');
     data = {
         index: index,
         old_html: editable.dataset.original,
         new_html: editable.innerHTML,
         rendered_html_url: document.URL,
         rendered_rst_url: document.evaluate('//a[@class="fa fa-github"]', document, null, XPathResult.ANY_TYPE, null).iterateNext().href
    };
    xhr.send(JSON.stringify(data))});

    </script>
