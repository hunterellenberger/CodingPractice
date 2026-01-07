fn merge_alternately(word1: String, word2: String) -> String {
    let mut solution: String = String::from("");
    for c in 0..word1.len() {
        solution.push(word1.chars().nth(c).expect("STRING"));

        if word2.chars().nth(c).is_some() {
            solution.push(word2.chars().nth(c).expect("STRING"));
        }
    }

    if word1.len() < word2.len() {
        if word2.len() % 2 == 0 {
            for c in word1.len()..word2.len() {
                solution.push(word2.chars().nth(c).expect("STRING"));
            }
        } else {
            for c in word1.len()..word2.len() {
                solution.push(word2.chars().nth(c).expect("STRING"));
            }
        }
    }
    return solution;
}

fn main() {
    let solution = merge_alternately("f".to_string(), "beebaeca".to_string());
    println!("{}", solution);
}
