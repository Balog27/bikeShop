from website import db,create_app
from website.models import Parts

app = create_app()

with app.app_context():
    db.create_all()
    part1 = Parts(name = "Michelin Power 5", price = 400, description = "A sporty tire for fast cornering", image = "https://img.gmoto.pl/2945209/opona-michelin-power-5-19055zr1775w-tl_1.webp")
    part2 = Parts(name = "Michelin Pilot Road 4", price = 350, description = "A touring tire for long distances", image = "https://tyretectrading.co.uk/wp-content/uploads/2021/12/michelin-pilot-road-4-front-rear.jpg")
    part3 = Parts(name = "Maxxis Enduro tire", price = 250, description = "A tire for off-road riding", image = "https://www.maxxis.com/pl/wp-content/uploads/sites/19/2021/01/tyre-image-maxxcrossmx-st-1024x1024.png")
    part4 =Parts (name = "Motorcyle Cover", price = 50, description = "A cover to protect your bike from the elements", image = "https://gomagcdn.ro/domains2/asfalt-uscat.ro/files/product/large/raincoat-motorcycle-cover-puig-5560p-argintiu-size-s-l-40416-189522.png")
    # db.session.add(part1)
    # db.session.add(part2)
    # db.session.add(part3)
    # db.session.add(part4)
    db.session.commit()
    print("Parts added to the database")


    # all_parts = Parts.query.all()
    #
    # # Delete each bike
    # for p in all_parts:
    #     db.session.delete(p)
    #
    # # Commit the changes to the database
    # db.session.commit()
    # print("All parts have been deleted.")