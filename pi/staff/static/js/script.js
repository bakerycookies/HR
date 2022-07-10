// All the script here will extends to all pages

// Script to auto hide the bootstrap alert after Js
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function() {
        $(this).remove();
    });
}, 3000);