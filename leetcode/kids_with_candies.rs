fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
    let most = candies.iter().max().unwrap_or(&0);
    let mut is_most = Vec::new();
    for kid in 0..candies.len() {
        if candies[kid] + extra_candies >= *most {
            is_most.push(true);
        } else {
            is_most.push(false);
        }
    }

    return is_most;
}

fn main() {
    let result = kids_with_candies([2, 3, 5, 1, 3].to_vec(), 3);
    println!("{:?}", result);
}
