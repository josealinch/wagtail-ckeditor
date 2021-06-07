CKEDITOR.plugins.add( 'customparagraph',
{
    init: function( editor )
    {
        editor.addCommand('addParagraphClassName',{
            exec : function( editor ){    
                var ps = editor.document.$.getElementsByTagName("p");
                for (var i=0; i < ps.length; i++){

                    if(ps[i].className.indexOf("thiny_p") < 0){
                        ps[i].className += "title-blue";
                    }

                }

            }
        });

        editor.ui.addButton( 'ThinyP',{
            label: 'Appends thiny_p class',
            command: 'addParagraphClassName',
            icon: this.path + 'images/icon.gif'
        });
    }
} );