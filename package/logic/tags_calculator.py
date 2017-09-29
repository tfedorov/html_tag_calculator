import re

_pattern = re.compile(
    "<(abbr|acronym|address|applet|area|base|basefont|bdo|big|blockquote|body|br|button|caption|center|cite|code|col|colgroup|dd|del|dir|div|dfn|dl|dt|em|fieldset|font|form|frame|frameset|h[1-6]|head|hr|html|iframe|img|input|ins|isindex|kbd|label|legend|link|map|menu|meta|noframes|noscript|object|ol|optgroup|option|param|pre|samp|script|select|small|span|strike|strong|style|sub|sup|table|tbody|td|textarea|tfoot|th|thead|title|xmp|tr|tt|u|li|ul|var|s|a|b|i|q|p)*?[ >]")


def calculate(content):
    result = {}
    matches = _pattern.finditer(content)
    for m in matches:
        tag = m.group(1)
        current_tag_num = result.get(tag, 0);
        result[tag] = current_tag_num + 1
    return result
