
/**
 * @param {string} searchValue
 */
String.prototype.find = function (searchValue) {
    let counter = 0
    f = searchValue.split(" ")
    for (var element of f) {
        counter++
        var conditions = this.toLowerCase().indexOf(element.toLowerCase()) >= 0
        if(!conditions) {break}
        var push = conditions && counter === f.length
    }
    return push
}