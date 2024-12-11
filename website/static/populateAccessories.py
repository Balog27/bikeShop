from website import db,create_app
from website.models import Accessories

app = create_app()

with app.app_context():
    db.create_all()
    accessories1 = Accessories(name="MSG Helmet", price=300, description="A sturdy flip-up helmet", image="https://cdn.shopify.com/s/files/1/0978/1676/files/MIDAMV-1MattBlack7_400x400.jpg?v=1710839556")
    accessories2 = Accessories(name = "SGI Helemt", price = 500, description = "A racing helmet", image = "https://www.sgi-moto.co.za/cdn/shop/files/SECADARKSTAR1_1200x1200.png?v=1686132380")
    accessories3 =Accessories(name = "Motocard Gloves", price = 50, description = "A pair of leather gloves", image = "https://cf-cdn.motocard.com/cdn-cgi/image/w=550,h=550,fit=cover,f=auto/products/images/20054/rukka-virium_20_ce_gore_tex_gore_grip_black_black_999-1-M-2005420810.jpg?v=b58155735495c1360e0dceacf321f83e")
    accessories4 = Accessories(name = "Borleni Jacket", price = 400, description = "A leather jacket", image = "https://m.media-amazon.com/images/I/41WJHba1LcL._SL500_.jpg")
    accessories5 = Accessories(name = "Spada Gloves", price = 100, description = "A pair of racing gloves", image = "https://m.media-amazon.com/images/I/51E3YpfgBxL._AC_UF1000,1000_QL80_.jpg")
    accessories6 = Accessories(name="Borleni Racing Jacket", price=800, description="A leather jacket",image="https://m.media-amazon.com/images/I/712fflwzDqL._AC_UF894,1000_QL80_.jpg")

    db.session.add(accessories1)
    db.session.add(accessories2)
    db.session.add(accessories3)
    db.session.add(accessories4)
    db.session.add(accessories5)
    db.session.add(accessories6)

    db.session.commit()
    print("Accessories added to the database")

    # all_accessories = Accessories.query.all()
    #
    # # Delete each bike
    # for a in all_accessories:
    #     db.session.delete(a)
    #
    # # Commit the changes to the database
    # db.session.commit()
    # print("All accessories have been deleted.")
