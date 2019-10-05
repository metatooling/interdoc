=====
Usage
=====

Hello world.



The project has been edited



.. raw:: html

    <script src="//cdn.jsdelivr.net/npm/medium-editor@latest/dist/js/medium-editor.min.js"></script>
    <script src="//cdn.jsdelivr.net/gh/metatooling/medium-button/src/medium-button.js"></script>
    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/medium-editor@latest/dist/css/medium-editor.min.css" type="text/css" media="screen" charset="utf-8">

    <script>
     var editor = new MediumEditor('body p', {
         toolbar: {
           buttons: ['b', 'h2', 'warning', 'pop']
         },
         extensions: {
             // compact
             'b':  new MediumButton({label:'BOLD', start:'<b>', end:'</b>'}),
             'h2': new MediumButton({label:'h2', start:'<h2>', end:'</h2>'}),

            // expanded
            'warning': new MediumButton({
               label: '<i class="fa fa-exclamation-triangle"></i>',
               start: '<div class="warning">',
               end:   '</div>'
            }),

         // with JavaScript
            'pop': new MediumButton({
               label:'POP',
               action: function(html, mark, parent){
               alert(html)
                         return html
                       }
             })


         }
     })

    </script>
