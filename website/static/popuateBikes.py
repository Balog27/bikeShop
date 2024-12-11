from website import create_app, db
from website.models import Bikes
from website.models import Review
from datetime import datetime

app = create_app()

with app.app_context():
    # Ensure the database tables are created


    # Add a new bike entry
    new_bike = Bikes(name="Mountain Bike", price=500, description="A sturdy mountain bike", image="https://i5.walmartimages.com/seo/Hyper-Bicycles-Men-s-29-Explorer-Dual-Suspension-Mountain-Bike-Red_d885e90f-d5fa-4c8d-b79a-801ed6ae5bb2.38883fa729039ce5aaf1ffd4395718b7.jpeg")
    new_bike2 = Bikes(name = "Suzuki SV 650", price = 5000, description = "A naked bike with 80 hp", image = "https://s1.cdn.autoevolution.com/images/moto_gallery/SUZUKI-SV650-6208_2.jpg")
    new_bike3 = Bikes(name = "Kawasaki H2R", price = 70000, description = "A supercharged bike with 300 hp", image = "https://www.motocicletekawasaki.ro/storage/backend/product/184313/main_images/kawasaki-ninja-h2r-j_0wEwN_1727942243.webp")
    new_bike4 = Bikes(name = "Ducati Panigale V4", price = 30000, description = "A racing bike with 220 hp", image = "https://www.motorcyclenews.com/wp-images/4710/2023-ducati-panigale-v4r-11.jpg")
    new_bike5 = Bikes(name = "Yamaha R1", price = 25000, description = "A racing bike with 200 hp", image = "https://www.motoboom.ro/image/cache/catalog/0_motoboom/2024/YAMAHA/motociclete/Yamaha%20R1/2024-Yamaha-YZF1000R1-EU-Midnight_Black-Studio-001-03-650x1.jpg")
    new_bike6 = Bikes(name = "Yanaha R6", price = 15000, description = "A racing bike with 120 hp", image = "https://cdn2.yamaha-motor.eu/prod/product-assets/2024/YZF600R6RCOMP/2024-Yamaha-YZF600R6RCOMP-EU-Tech_Black-Studio-001-03_Mobile.jpg")
    new_bike7 = Bikes(name = "GSX R 1000", price = 20000, description = "A racing bike with 180 hp", image = "https://www.barracuda-moto.ro/media/catalog/category/gsxr1000-2005.jpg")
    new_bike8 = Bikes(name = "BMW S1000RR", price = 25000, description = "A racing bike with 200 hp", image = "https://www.cycleworld.com/resizer/habncXl5xZ5-PSrszyGjOPq25vA=/616x0/smart/cloudfront-us-east-1.images.arcpublishing.com/octane/A25E4DK5IK3A6VDPETJHSSMHXY.jpg")
    new_bike9 = Bikes(name = "Yamaha MT-09", price = 10000, description ="A powerful naked bike", image = "https://www.motoboom.ro/image/cache/catalog/0_motoboom/2024/YAMAHA/motociclete/MT-09/2024-Yamaha-MT09-EU-Midnight_Cyan-360-Degrees-001-03-650x1.jpg")
    new_bike10 = Bikes(name = "Yamaha MT-07", price = 7000, description = "A naked bike with 75 hp", image = "https://gomagcdn.ro/domains/motomus.ro/files/product/original/yamaha-mt-07-434710.jpg")
    new_bike11 = Bikes(name = "Yamaha MT-03", price = 5000, description = "A naked bike with 40 hp", image = "https://www.motoboom.ro/image/cache/catalog/0_motoboom/2023/YAMAHA%20MOTOCICLETE/MT-03/2023-Yamaha-MT320-EU-Midnight_Black-Studio-001-03-650x1.jpg")
    new_bike12 = Bikes(name = "Yamaha MT-15", price = 4000, description= "A beginners bike with 15 hp", image = "https://cdn.bikedekho.com/processedimages/yamaha/mt-15-2-0/source/mt-15-2-06613f885e681c.jpg")
    new_bike13 = Bikes(name = "Aprilia RS 660", price = 12000, description = "A racing bike with 100 hp", image = "https://cocmotors.ro/hickaksy/2021/02/CocMotors-Aprilia-RS660-Lava-Red-2021.jpg")

    new_review = Review(rating = 5, description = "Great bike", user_id = 1, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")
    new_review2 = Review(rating = 4, description = "Good bike", user_id = 2, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")
    new_review3 = Review(rating = 3, description = "Ok bike",  user_id = 5, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")
    new_review4 = Review(rating = 4.5,description = "Great bike", user_id = 3, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")
    new_review5 = Review(rating = 2, description = "Bad bike",  user_id = 4, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")
    new_review6 = Review(rating = 1, description = "Terrible bike", user_id = 6, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")
    new_review7 = Review(rating = 5, description = "Good bike", user_id = 7, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 1, product_type = "bike")

    # db.session.add(new_review)
    # db.session.add(new_review2)
    # db.session.add(new_review3)
    # db.session.add(new_review4)
    # db.session.add(new_review5)
    #db.session.add(new_review6)
    #print("added")
    # db.session.add(new_review7)

    new_review8 = Review(rating = 5, description = "Great bike", user_id = 1, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 2, product_type = "bike")
    new_review9 = Review(rating = 4, description = "Good bike", user_id = 2, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 2, product_type = "bike")
    new_review10 = Review(rating = 3, description = "Ok bike",  user_id = 5, date = datetime.strptime("2021-05-01", "%Y-%m-%d"), product_id = 2, product_type = "bike")
    #
    # db.session.add(new_review8)
    # db.session.add(new_review9)
    # db.session.add(new_review10)

    db.session.add(new_bike)
    db.session.add(new_bike2)
    db.session.add(new_bike3)
    db.session.add(new_bike4)
    db.session.add(new_bike5)

    db.session.add(new_bike6)

    db.session.add(new_bike7)
    db.session.add(new_bike8)
    db.session.add(new_bike9)
    db.session.add(new_bike10)
    db.session.add(new_bike11)
    db.session.add(new_bike12)
    db.session.add(new_bike13)
    db.session.commit()

    # all_bikes = Bikes.query.all()
    #
    # # Delete each bike
    # for bike in all_bikes:
    #     db.session.delete(bike)
    #
    # # Commit the changes to the database
    # db.session.commit()
    # print("All bikes have been deleted.")