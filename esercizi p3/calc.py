import argparse

def calcolatrice(n1, n2, operazione):
    if operazione == "add":
        return n1 + n2
    elif operazione == "sot":
        return n1 - n2
    elif operazione == "mol":
        return n1 * n2
    elif operazione == "div":
        return n1 / n2
        
parser = argparse.ArgumentParser(description="Semplice calcolatrice per le 4 operazioni")
parser.add_argument("n1", type=float, help="Primo numero")
parser.add_argument("n2", type=float, help="Secondo numero")
parser.add_argument("operazione", type=str, help="Tipo operazione", choices = ["add", "sot", "mol", "div"])
parser.add_argument("-v", "--verbose", help="Restuisce output verboso")

args = parser.parse_args()
risultato = calcolatrice(args.n1, args.n2, args.operazione)
if args.verbose:
    print(f"Il risultato di '{args.operazione}' è {risultato}")
    print("Verbose: %s" %args.verbose)
else:
    print('risultato = %s' %risultato)