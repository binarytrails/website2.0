
function changeCubeClass(className)
{
    cube = document.getElementById("cube");
    cube.className = className;
}

// https://github.com/sevaivanov/short/tree/master/js/meow
function meow(title, markdownMessage)
{
    var converter = new showdown.Converter();
    htmlMessage = converter.makeHtml(markdownMessage);

    $('#meow-head p').html(title);
    $('#meow-body p').html(htmlMessage);
    $('#meow-background').fadeIn("fast",function()
    {
        $('#ok-button,#meow-close-button').click(function(){
            $('#meow-background').hide();
        });
    });
}
