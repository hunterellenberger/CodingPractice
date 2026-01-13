fn reverse_vowels(s: String) -> String {
    let mut s: String = s;
    let vowels: String = String::from("aeiouAEIOU");
    let mut vowels_in_string: Vec<char> = vec![];

    for c in s.chars() {
        if vowels.contains(c) {
            vowels_in_string.push(c);
        }
    }

    for c in 0..s.len() {
        if vowels.contains(s.chars().nth(c).unwrap()) {
            s.remove(c);
            s.insert(c, vowels_in_string.pop().expect("CHARACTER"));
        }
    }

    return s;
}

fn main() {
    let string = String::from("IceCreAm");
    let reverse = reverse_vowels(string);
    println!("{reverse}")
}
