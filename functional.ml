(*QUESTIONS*)
let identity x =
  x
;;


let rec reverse (l : 'a list) : 'a list = 
  match l with
  | [] -> []
  | x::xs -> (reverse xs) @ [x]
;; 
  
let palindrome (l: 'a list) : bool  =
  let rev_l = reverse l in 
  let rec compare l1 l2 = 
    match l1, l2 with 
    | [], [] -> true
    | x::xs, y::ys -> 
        if x = y then
          compare xs ys
        else
          false
    | _, _ -> false
  in
  compare l rev_l
        
;;

let rec squeeze l  = 
  let rec aux l1 l2 el =
    match l1 with
    | [] -> l2
    | x::xs -> if x = el
        then aux xs l2 x
        else aux xs (l2@[x]) x
  in
  match l with
  | [] -> [] 
  | y::ys -> aux ys [y] y 
;;


let rec sprinkle l = 
  let rec aux sofar remaining =
    match remaining with
    | [] -> [[]]
    | x::xs -> aux [[x]] xs
;;

let rec countNodes (t : 'a tree) : int = 
  match t with
  | Node (_, c) -> 1 + (List.fold_left (+) 0 (List.map countNodes c));
;;


let rec ironOut (t: int tree) : int list list = 
  match t with
  | Node (x, []) -> [[x]]
  | Node (x, c) -> List.map (fun l -> [x]@l)
                     (List.concat (List.map ironOut c))
;;

let rec fib' lst a b max = if a+b >= max then
    lst@[a; b; a+b]
  else
    fib' (lst@[a]) b (a+b) max 
;;


let fib max = 
  match max with
  | 0 -> []
  | _ -> fib' [] 1 1 max
;;

let pascal max = 
  let sum a b =
    a + b 
  in
  let rec aux prev count =
    
    let l1 = prev @ [0] in
    let l2 = 0::prev in 
    aux [(List.map2 sum l1 l2)]
  in
  match max with
  | 0 -> []
  | 1 -> []
  | 2 -> [[1]]
  | x -> aux [1] 
      
;;

let z = identity 3 ;;
let a = reverse [1;2;3;4];;
let b = palindrome [1;2;3;4;3;2;1] ;;
let c = palindrome [1;2;3;4;5;3;2;1] ;;
let d = squeeze [1;2;2;2;3;3;2;4;4];;
