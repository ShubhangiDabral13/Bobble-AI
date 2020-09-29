def area_rect(coord):
    l, m, n, o = coord

    #Return the area.
    return (n-l)*(o-m)


def cover_area_rect(rects):
    return (min(r[0] for r in rects),
            min(r[1] for r in rects),
            max(r[2] for r in rects),
            max(r[3] for r in rects))


def remove_rect(bb, rects):
    if not rects:
        return []

    (x1, y1, x2, y2) = rects[0]

    rs = rects[1:]
    (l1, m1, l2, m2) = bb

    if l1 == l2 or m1 == m2:
        return []

    if l1 >= x2 or l2 <= x1 or y1 >= m2 or y2 <= m1:
        return remove_rect(bb, rs)

    return [(max(l1, x1), max(m1, y1), min(l2, x2), min(m2, y2))] + remove_rect(bb, rs)


def calculate_area(cr, rects):
    if not rects:
        return 0

    rc = rects[0]
    rs = rects[1:]

    x1, y1, x2, y2 = cr
    p1, q1, p2, q2 = rc

    t = (x1, q2, x2, y2)
    b = (x1, y1, x2, q1)
    l = (x1, q1, p1, q2)
    r = (p2, q1, x2, q2)

    return area(rc) + sum(calculate_area(x, remove_rect(x, rs)) for x in [t, b, l, r])


m = int(input())
area_rectangle = []
for i in range(0, m):
    k = list(map(int, input().strip().split(" ")))
    area_rectangle.append(k)

print(calc(covering_area_rect(area_rectangle), area_rectangle))
