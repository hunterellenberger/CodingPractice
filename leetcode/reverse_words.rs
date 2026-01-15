fn reverse_words(s: String) -> String {
    let svec: Vec<char> = s.chars().collect();
    let mut reverse: Vec<String> = vec![String::from("")];
    let mut return_string: String = String::from("");
    let space: char = ' ';
    let mut iter = 0;
    let mut vec_string = 0;

    // If space check if next character is space. If is remove original space
    // If letter check if next is space. If so set wordEnd true

    while iter < svec.len() {
        if iter == svec.len() - 1 && svec[iter] != space {
            reverse[vec_string].push(svec[iter]);
            iter += 1;
        } else if svec[iter] != space && svec[iter + 1] != space {
            reverse[vec_string].push(svec[iter]);
            iter += 1;
        } else if svec[iter] != space && svec[iter + 1] == space {
            reverse[vec_string].push(svec[iter]);
            reverse.push(String::from(""));
            vec_string += 1;
            iter += 1;
        } else {
            iter += 1;
        }
    }

    if reverse[reverse.len() - 1] == "" {
        reverse.pop();
    }

    for _element in 0..reverse.len() {
        return_string.push_str(&reverse.pop().expect("STRING"));
        return_string.push_str(&String::from(" "));
    }

    return_string.pop();
    return return_string;
}

fn main() {
    let word: String = String::from("  hello world  ");
    let reverse: String = reverse_words(word);
    println!("{reverse}");
}
