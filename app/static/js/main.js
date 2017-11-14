$(function() {
    $('#get_posts_basic').bind('click', function(e)
    {
        if ($('#user_id').val().trim().length == 0)
        {
            alert("Invalid Stackoverflow User ID");
            $('#user_id').focus();
            return;
        }
        $('#main-form').attr('action', "/basic");
        $('#main-form').submit();
    });
});