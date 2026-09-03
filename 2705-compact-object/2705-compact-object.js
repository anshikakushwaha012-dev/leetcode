/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        let result = [];
        for (let value of obj) {
            if (Boolean(value)) {
                result.push(compactObject(value));
            }
        }
        return result;
    }
    if (typeof obj === "object" && obj !== null) {
        let result = {};

        for (let key in obj) {
            if (Boolean(obj[key])) {
                result[key] = compactObject(obj[key]);
            }
        }
        return result;
    }
    return obj;
};