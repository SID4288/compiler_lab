def eliminate_left_recursion():
    non_terminal = input("Enter the non-terminal: ").strip()
    num_productions = int(input(f"Enter number of productions for {non_terminal}: "))
    
    productions = []
    for i in range(num_productions):
        prod = input(f"Enter production {i+1}: ").strip()
        productions.append(prod)
        
    alphas = []
    betas = []
    
    # Classify productions into recursive (alpha) and non-recursive (beta)
    for prod in productions:
        if prod.startswith(non_terminal):
            alphas.append(prod[len(non_terminal):])
        else:
            betas.append(prod)
            
    print("\nGrammar after removing left recursion:")
    if not alphas:
        # No left recursion detected
        prod_str = " | ".join(productions)
        print(f"{non_terminal} -> {prod_str}")
    elif not betas:
        print("Unable to execute: Missing non-recursive alternative (beta).")
    else:
        # Generate equivalent right-recursive transformations
        new_var = f"{non_terminal}'"
        beta_str = " | ".join([f"{b}{new_var}" for b in betas])
        alpha_str = " | ".join([f"{a}{new_var}" for a in alphas]) + " | epsilon"
        
        print(f"{non_terminal} -> {beta_str}")
        print(f"{new_var} -> {alpha_str}")

if __name__ == "__main__":
    eliminate_left_recursion()