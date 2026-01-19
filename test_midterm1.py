def bubble_sort_desc(arr):
    n = len(arr)
    a = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
def parse_tuple(s):
    s = s.strip()
    if s.startswith("(") and s.endswith(")"):
        s = s[1:-1]
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    if not parts:
        raise ValueError("Empty input.")
    return tuple(int(p) for p in parts)
def can_knight_reach(knight, start, end):
    if len(start) != len(end):
        raise ValueError("start and end must have the same length.")
    list_numbers = [abs(s - e) for s, e in zip(start, end)]
    list_numbers = bubble_sort_desc(list_numbers)
    knight_sorted = bubble_sort_desc(list(knight))
    return list_numbers == knight_sorted
def main():
    print("Enter knight, start, end as comma-separated integers.")
    print("Examples:")
    print("  knight: 2, 1, 7")
    print("  start : 3, 5, 9")
    print("  end   : 8, 11, 13\n")
    knight_str = input("knight: ")
    start_str  = input("start : ")
    end_str    = input("end   : ")
    try:
        knight = parse_tuple(knight_str)
        start  = parse_tuple(start_str)
        end    = parse_tuple(end_str)
    except ValueError as exc:
        print(f"Input error: {exc}")
        return
    result = can_knight_reach(knight, start, end)
    print(result)
main()
