year = "1499 1500 1501"
century = '15'

years = year.split()

ans = 0
for i in range(len(years)):
    if ((int(years[i]) > (int(century)*100-99)) & (int(years[i]) <= (int(century)*100))):
        ans += 1
print(ans)