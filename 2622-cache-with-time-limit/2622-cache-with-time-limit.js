var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    let currentTime = Date.now();

    let exists = this.cache.has(key) &&
                 this.cache.get(key).expiry > currentTime;

    this.cache.set(key, {
        value: value,
        expiry: currentTime + duration
    });

    return exists;
};

TimeLimitedCache.prototype.get = function(key) {
    if (!this.cache.has(key)) {
        return -1;
    }

    let data = this.cache.get(key);

    if (data.expiry <= Date.now()) {
        this.cache.delete(key);
        return -1;
    }

    return data.value;
};

TimeLimitedCache.prototype.count = function() {
    let count = 0;
    let currentTime = Date.now();

    for (let [key, data] of this.cache) {
        if (data.expiry > currentTime) {
            count++;
        }
    }

    return count;
};