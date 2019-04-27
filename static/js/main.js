var form = $("#rebus_form")
var sizeTag = form.find("input[name='size']")
function append_img_input() {
    var sizeStr = sizeTag.val()
    var newSize = parseInt(sizeStr.substring(sizeStr.indexOf("-")+1))+1
    sizeTag.val(sizeStr.substring(0,sizeStr.indexOf("-"))+"-"+newSize)
    form.append("<input type = \"file\" name=\""+sizeTag.val()+"\" multiple=\"false\" autocomplete=\"off\" required/>")
}
function append_text_input() {
    var sizeStr = sizeTag.val()
    var newSize = parseInt(sizeStr.substring(sizeStr.indexOf("-")+1))+1
    sizeTag.val(sizeStr.substring(0,sizeStr.indexOf("-"))+"-"+newSize)
    form.append("<input type = \"text\" name=\""+sizeTag.val()+"\" required/>")
}
function add_word() {
    var sizeStr = sizeTag.val()
    var newSize = parseInt(sizeStr.substring(0,sizeStr.indexOf("-")))+1
    sizeTag.val(newSize+sizeStr.substring(sizeStr.indexOf("-")))
}