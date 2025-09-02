class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {

        string result; 

        for (string s : strs){
            string length = std::to_string(s.size());
            result += length; 
            result += "#";
            result += s;
        }
        return result;
        
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        
        int idx = 0;

        vector<string> result;

        while (idx < s.size()){

            string size;
            while(s[idx] != '#'){
                size += s[idx];
                idx++;
            }
            cout << "size: " << size << "\n";
            int s_size = stoi(size);
            idx += 1;
            string curr_string;
            for (int i = idx; i < idx + s_size; i++){
                curr_string += s[i];
            }
            idx += s_size;
            result.push_back(curr_string);

        }
        return result;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));