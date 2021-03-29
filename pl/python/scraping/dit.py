import requests
import bs4

resp = requests.get("https://www.dit.uoi.gr/members.php")

soup = bs4.BeautifulSoup(resp.text, features="lxml")
dit_uoi_members = []

for tab in soup.findAll("table"):
    for tr in tab.findAll("tr"):
        cells = tr.findAll("td")
        name = cells[0].text.strip()
        email_tel = cells[2].findAll("a")
        email = email_tel[0].text.strip()
        tel = email_tel[1].text.strip()

        dit_uoi_members.append((name, email, tel))

for name, email, tel in dit_uoi_members:
    print(f"e-mail:{email}, ΟΝΟΜΑ:{name}, ΤΗΛΕΦΩΝΟ:{tel}")


dit_uoi_members.sort(key=lambda m: m[0])
print("#" * 40)

for name, email, tel in dit_uoi_members:
    if email == "":
        email = "ΜΗ ΚΑΤΑΧΩΡΗΜΕΝΟ"
    if tel == "":
        tel = "ΜΗ ΚΑΤΑΧΩΡΗΜΕΝΟ"
    print(email, name, tel)