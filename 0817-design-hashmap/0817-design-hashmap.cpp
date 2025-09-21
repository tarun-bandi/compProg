class Bucket {
    vector<pair<int, int>> bucket;

public:
    void add(int key, int value) {
        for (auto &p : bucket) {
            if (p.first == key) {
                p.second = value; // update if key exists
                return;
            }
        }
        bucket.push_back({key, value}); // otherwise insert new
    }

    int find(int key) {
        for (auto &p : bucket) {
            if (p.first == key) return p.second;
        }
        return -1;
    }

    void remove(int key) {
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->first == key) {
                bucket.erase(it);
                return; // remove first occurrence and exit
            }
        }
    }
};

class MyHashMap {
    const int BUCKET_COUNT;
    vector<Bucket> table;

public:
    MyHashMap() : BUCKET_COUNT(40), table(BUCKET_COUNT) {}

    void put(int key, int value) {
        int index = key % BUCKET_COUNT;
        table[index].add(key, value);
    }

    int get(int key) {
        int index = key % BUCKET_COUNT;
        return table[index].find(key);
    }

    void remove(int key) {
        int index = key % BUCKET_COUNT;
        table[index].remove(key);
    }
};