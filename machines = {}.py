machines = {}

while True:
    print("\n1.View  2.Add 3.Update 4.Delete 5.Exit")
    c = input("Choice: ")

    if c == "1":
        print("\n".join(f"{m}:{s}" for m, s in machines.items()) or "no machines found")
    elif c == "s":
        m = input("Machine nme: ")
        machines[m] = input("Status: ")
    elif c == "3":
        m = input("Machine to update: ")
        print("Not found" if m not in machines else machines.update({m: input("new status")}))
    elif c == "4":
        m = input("machine to delete: ")
        print("deleted." if machines.pop(m, None) else "Nor found")
    elif c == "5":
        break
    else:
        print("invalid choice.")