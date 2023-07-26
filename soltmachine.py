import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3


Symbol_count = {
    "@":2,
    "#":4,
    "%":6,
    "$":8    
}
Symbol_values = {
    "@":6,
    "#":5,
    "%":4,
    "$":3   
} 
def check_winnning(columns,lines,bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
            
    return winnings,winnings_lines

def get_spin_machine(rows,cols,Symbols):
    all_symbols = []
    for Symbol, Symbol_count in Symbols.items():
        for _ in range(Symbol_count):
            all_symbols.append(Symbol)
           
    cols = [] 
    for _ in range(COLUMNS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value  = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        cols.append(column)
    
    return cols

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()
    
    
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number. ")
    
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"  + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Enter the valid number of Lines.")
        else:
            print("Please enter a number. ")
            
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=  MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number. ")
    
    return amount

def spins(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet  = bet * lines 
        
        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break 

    
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")
    
    slot = get_spin_machine(ROWS,COLUMNS,Symbol_count)
    print_slot_machine(slot)
    winnings,winning_lines = check_winnning(slot,lines,bet,Symbol_values)
    print(f"you won ${winnings}. ")
    print(f"you won on lines : ",*winning_lines)
    return winnings - total_bet


def main():
    balance = deposit() 
    while True:
        print(f"current balance is ${balance} ")
        answer = input ("press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spins(balance)

    print(f"you left with ${balance}. ")

main()
