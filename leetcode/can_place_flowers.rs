fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
    let mut placed = 0;
    let mut copy: Vec<i32> = flowerbed.clone();

    if copy.len() == 1 {
        if copy[0] == 0 {
            return true;
        } else if n == 0 {
            return true;
        } else {
            return false;
        }
    }

    for iter in 0..copy.len() {
        if iter == 0 {
            if copy[iter] == 0 && copy[iter + 1] == 0 {
                copy[iter] = 1;
                placed += 1
            };
        } else if iter == copy.len() - 1 {
            if copy[iter - 1] == 0 && copy[iter] == 0 {
                copy[iter] = 1;
                placed += 1;
            }
        } else if copy[iter - 1] == 0 && copy[iter] == 0 && copy[iter + 1] == 0 {
            copy[iter] = 1;
            placed += 1;
        }
    }

    if placed >= n {
        return true;
    } else {
        return false;
    }
}

fn main() {
    let vector: Vec<i32> = vec![1, 0, 0, 0, 0, 1];
    let test: i32 = 2;
    println!("{}", can_place_flowers(vector, test));
}
