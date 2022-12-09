"""
...
"""




def valid_ip(ip_address: str) -> bool:
    """
    Makes a crude attempt at validating the given IP address.
    """
    dots = 0
    for char in ip_address:
        if char == '.':
            dots += 1
    return True if dots==3 else False




footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.thingy.dev/" target="_blank">Thingy</a></p>
</div>
"""
