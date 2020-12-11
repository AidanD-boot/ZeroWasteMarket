from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app,db
from app.forms import RegistrationForm, LoginForm
from app.models import User,Supplier,Produce,Listing,Keyword,Content,Producetokeyword


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')

@app.route('/browse')
def browse():
    p = Produce.query.all()
    l = Listing.query.all()
    return render_template('browse.html',listings=l,produce=p,title='Browse')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user! UwU')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/popdb')
def popdb():

    #adding tuples to db

    k1 = Keyword(name='green')
    k2 = Keyword(name='yellow')
    k3 = Keyword(name='red')
    k4 = Keyword(name='white')
    k5 = Keyword(name='tan')
    k6 = Keyword(name='orange')
    k7 = Keyword(name='brown')
    k8 = Keyword(name='black')
    k9 = Keyword(name='vegetable')
    k10 = Keyword(name='starch')
    k11 = Keyword(name='squash')
    k12 = Keyword(name='gourd')
    k13 = Keyword(name='legume')
    k14 = Keyword(name='maize')
    k15 = Keyword(name='spicy')
    k16 = Keyword(name='sweet')
    k17 = Keyword(name='tart')
    k18 = Keyword(name='leafy')
    k19 = Keyword(name='grain')
    k20 = Keyword(name='cereal')
    k21 = Keyword(name='cabbage')

    s1 = Supplier(name='Griggs Farm', address='599 Boston Rd', zipcode=1821, city='Billerica', state='MA')
    s2 = Supplier(name='Krochmal Farms', address='31 Jennie\'s Way', zipcode=1876, city='Tewksbury', state='MA')
    s3 = Supplier(name='Great Brook Dairy Farm', address='247 North Rd', zipcode=1741, city='Carlisle', state='MA')
    s4 = Supplier(name='Farmer Daves', address='437 Parker Rd', zipcode=1826, city='Dracut', state='MA')
    s5 = Supplier(name='Jones Farm', address='246 Acton Rd', zipcode=1824, city='Chelmsford', state='MA')
    s6 = Supplier(name='Swenson Farms', address='50 Mill Rd', zipcode=1862, city='Chelmsford', state='MA')
    s7 = Supplier(name='Drew Farm', address='31 Tadmuck Rd', zipcode=1886, city='Westford', state='MA')
    s8 = Supplier(name='Clark Farm', address='185 Concord St', zipcode=1741, city='Carlisle', state='MA')
    s9 = Supplier(name='Parlee Farm', address='135 Pine Hill Rd', zipcode=1824, city='Chelmsford', state='MA')
    s10 = Supplier(name='Wright-Locke Farm', address='78 Ridge St', zipcode=1890, city='Winchester', state='MA')
    s11 = Supplier(name='Indian Creek Farm', address='1408 Trumansburg Rd', zipcode=14850, city='Ithaca', state='NY')
    s12 = Supplier(name='Stick and Stone Farm', address='1605 Trumansburg Rd', zipcode=14850, city='Ithaca', state='NY')
    s13 = Supplier(name='RoseBarb Farms', address='108 Landon Rd', zipcode=14850, city='Ithaca', state='NY')
    s14 = Supplier(name='Three Swallows Farm', address='23 Nelson Rd', zipcode=14850, city='Ithaca', state='NY')
    s15 = Supplier(name='HoneyRock Farm', address='271 Burns Rd', zipcode=14850, city='Ithaca', state='NY')
    s16 = Supplier(name='Kingdom Farms', address='317 Auburn Rd', zipcode=14882, city='Lansing', state='NY')
    s17 = Supplier(name='Straw Pocket Farm', address='1388 Ridge Rd', zipcode=14882, city='Lansing', state='NY')
    s18 = Supplier(name='Dygert Farms', address='260 Central Chapel Rd', zipcode=14817, city='Brooktondale', state='NY')
    s19 = Supplier(name='TC3 Farm', address='100 Cortland Rd', zipcode=13053, city='Dryden', state='NY')

    p1 = Produce(name='Brocolli', imageRef='https://cdn.mos.cms.futurecdn.net/r8NK24bmcMgSib5zWKKQkW.jpg')
    p2 = Produce(name='Spinach', imageRef='https://i.ndtvimg.com/i/2016-11/spinach_620x350_81477995047.jpg')
    p3 = Produce(name='Kale',
                 imageRef='https://post.healthline.com/wp-content/uploads/2020/09/benefits-of-kale-1200x628-facebook-1200x628.jpg')
    p4 = Produce(name='Pumpkin',
                 imageRef='https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/279610_2200-732x549.jpg')
    p5 = Produce(name='Straightneck Squash',
                 imageRef='https://d1nw62gticy6e9.cloudfront.net/uploads/Early-Prolific-Straightneck-Squash-Seeds.jpg')
    p6 = Produce(name='Zucchini',
                 imageRef='https://www.jessicagavin.com/wp-content/uploads/2018/05/zucchini-2-1200.jpg')
    p7 = Produce(name='Green Beans',
                 imageRef='https://images.food52.com/mrPh1x9qA6lTYKO27QJEfDjZ4Y8=/2016x1344/filters:format(webp)/ff7b7650-cacd-42b4-947c-e2e8ba90fa2a--greenbeans.jpg')
    p8 = Produce(name='Lentils',
                 imageRef='https://cdn.loveandlemons.com/wp-content/uploads/2019/12/how-to-cook-lentils.jpg')
    p9 = Produce(name='Peas', imageRef='https://www.almanac.com/sites/default/files/image_nodes/peas-and-pea-pods.jpg')
    p10 = Produce(name='Potatoes',
                  imageRef='https://cdn.cheapism.com/images/081516_national_potato_day_recipes_slide_0_f.max-800x600.jpg')
    p11 = Produce(name='Corn',
                  imageRef='https://www.simplyhappyfoodie.com/wp-content/uploads/2018/04/instant-pot-corn-on-the-cob-1-500x500.jpg')
    p12 = Produce(name='Soybean',
                  imageRef='https://www.johnnyseeds.com/dw/image/v2/BBBW_PRD/on/demandware.static/-/Sites-jss-master/default/dw3c4875f3/images/products/vegetables/02553_01_tohya.jpg?sw=1120')
    p13 = Produce(name='Oats',
                  imageRef='https://post.healthline.com/wp-content/uploads/2020/03/oats-oatmeal-732x549-thumbnail.jpg')
    p14 = Produce(name='Barley',
                  imageRef='https://cdn-prod.medicalnewstoday.com/content/images/articles/295/295268/barley-grains-in-a-wooden-bowl.jpg')
    p15 = Produce(name='Flour',
                  imageRef='https://www.world-grain.com/ext/resources/Article-Images/2020/05/WholeWheatFlour_Photo-adobe-stock_E.jpg?t=1590171823&width=1080')
    p16 = Produce(name='Turnip', imageRef='https://upload.wikimedia.org/wikipedia/commons/d/d3/Turnip_2622027.jpg')
    p17 = Produce(name='Lettuce',
                  imageRef='https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/03/romaine-lettuce-1296x728-body.jpg?w=1155&h=1528')
    p18 = Produce(name='Green Peppers',
                  imageRef='https://edge.bonnieplants.com/www/tiny/uploads/20200810205434/bonnie-s-green-bell-pepper.jpg')
    p19 = Produce(name='Chili Peppers', imageRef='https://scitechdaily.com/images/Chili-Peppers.jpg')
    p20 = Produce(name='Cucumber',
                  imageRef='https://www.shethepeople.tv/wp-content/uploads/2019/05/cucumber-e1558166231577.jpg')

    pk1 = Producetokeyword(kproduct=Produce.query.get(1), tag=Keyword.query.get(1))
    pk2 = Producetokeyword(kproduct=Produce.query.get(1), tag=Keyword.query.get(9))
    pk3 = Producetokeyword(kproduct=Produce.query.get(1), tag=Keyword.query.get(21))
    pk4 = Producetokeyword(kproduct=Produce.query.get(2), tag=Keyword.query.get(1))
    pk5 = Producetokeyword(kproduct=Produce.query.get(2), tag=Keyword.query.get(18))
    pk6 = Producetokeyword(kproduct=Produce.query.get(2), tag=Keyword.query.get(9))
    pk7 = Producetokeyword(kproduct=Produce.query.get(3), tag=Keyword.query.get(1))
    pk8 = Producetokeyword(kproduct=Produce.query.get(3), tag=Keyword.query.get(18))
    pk9 = Producetokeyword(kproduct=Produce.query.get(3), tag=Keyword.query.get(9))
    pk10 = Producetokeyword(kproduct=Produce.query.get(4), tag=Keyword.query.get(6))
    pk11 = Producetokeyword(kproduct=Produce.query.get(4), tag=Keyword.query.get(11))
    pk12 = Producetokeyword(kproduct=Produce.query.get(4), tag=Keyword.query.get(12))
    pk13 = Producetokeyword(kproduct=Produce.query.get(4), tag=Keyword.query.get(16))
    pk14 = Producetokeyword(kproduct=Produce.query.get(5), tag=Keyword.query.get(2))
    pk15 = Producetokeyword(kproduct=Produce.query.get(5), tag=Keyword.query.get(11))
    pk16 = Producetokeyword(kproduct=Produce.query.get(5), tag=Keyword.query.get(12))
    pk17 = Producetokeyword(kproduct=Produce.query.get(5), tag=Keyword.query.get(16))
    pk18 = Producetokeyword(kproduct=Produce.query.get(6), tag=Keyword.query.get(1))
    pk19 = Producetokeyword(kproduct=Produce.query.get(6), tag=Keyword.query.get(11))
    pk20 = Producetokeyword(kproduct=Produce.query.get(6), tag=Keyword.query.get(12))
    pk21 = Producetokeyword(kproduct=Produce.query.get(6), tag=Keyword.query.get(16))
    pk22 = Producetokeyword(kproduct=Produce.query.get(7), tag=Keyword.query.get(1))
    pk23 = Producetokeyword(kproduct=Produce.query.get(7), tag=Keyword.query.get(13))
    pk24 = Producetokeyword(kproduct=Produce.query.get(7), tag=Keyword.query.get(9))
    pk25 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(1))
    pk26 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(2))
    pk27 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(3))
    pk28 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(4))
    pk29 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(6))
    pk30 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(7))
    pk31 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(8))
    pk32 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(13))
    pk33 = Producetokeyword(kproduct=Produce.query.get(8), tag=Keyword.query.get(9))
    pk34 = Producetokeyword(kproduct=Produce.query.get(9), tag=Keyword.query.get(1))
    pk35 = Producetokeyword(kproduct=Produce.query.get(9), tag=Keyword.query.get(9))
    pk36 = Producetokeyword(kproduct=Produce.query.get(9), tag=Keyword.query.get(13))
    pk37 = Producetokeyword(kproduct=Produce.query.get(9), tag=Keyword.query.get(16))
    pk38 = Producetokeyword(kproduct=Produce.query.get(10), tag=Keyword.query.get(4))
    pk39 = Producetokeyword(kproduct=Produce.query.get(10), tag=Keyword.query.get(3))
    pk40 = Producetokeyword(kproduct=Produce.query.get(10), tag=Keyword.query.get(2))
    pk41 = Producetokeyword(kproduct=Produce.query.get(10), tag=Keyword.query.get(7))
    pk42 = Producetokeyword(kproduct=Produce.query.get(10), tag=Keyword.query.get(10))
    pk43 = Producetokeyword(kproduct=Produce.query.get(10), tag=Keyword.query.get(16))
    pk44 = Producetokeyword(kproduct=Produce.query.get(11), tag=Keyword.query.get(2))
    pk45 = Producetokeyword(kproduct=Produce.query.get(11), tag=Keyword.query.get(16))
    pk46 = Producetokeyword(kproduct=Produce.query.get(11), tag=Keyword.query.get(20))
    pk47 = Producetokeyword(kproduct=Produce.query.get(11), tag=Keyword.query.get(14))
    pk48 = Producetokeyword(kproduct=Produce.query.get(11), tag=Keyword.query.get(19))
    pk49 = Producetokeyword(kproduct=Produce.query.get(11), tag=Keyword.query.get(9))
    pk50 = Producetokeyword(kproduct=Produce.query.get(12), tag=Keyword.query.get(9))
    pk51 = Producetokeyword(kproduct=Produce.query.get(12), tag=Keyword.query.get(13))
    pk52 = Producetokeyword(kproduct=Produce.query.get(12), tag=Keyword.query.get(1))
    pk53 = Producetokeyword(kproduct=Produce.query.get(13), tag=Keyword.query.get(19))
    pk54 = Producetokeyword(kproduct=Produce.query.get(13), tag=Keyword.query.get(20))
    pk55 = Producetokeyword(kproduct=Produce.query.get(13), tag=Keyword.query.get(10))
    pk56 = Producetokeyword(kproduct=Produce.query.get(13), tag=Keyword.query.get(7))
    pk57 = Producetokeyword(kproduct=Produce.query.get(14), tag=Keyword.query.get(19))
    pk58 = Producetokeyword(kproduct=Produce.query.get(14), tag=Keyword.query.get(20))
    pk59 = Producetokeyword(kproduct=Produce.query.get(14), tag=Keyword.query.get(10))
    pk60 = Producetokeyword(kproduct=Produce.query.get(14), tag=Keyword.query.get(7))
    pk61 = Producetokeyword(kproduct=Produce.query.get(15), tag=Keyword.query.get(19))
    pk62 = Producetokeyword(kproduct=Produce.query.get(15), tag=Keyword.query.get(20))
    pk63 = Producetokeyword(kproduct=Produce.query.get(15), tag=Keyword.query.get(10))
    pk64 = Producetokeyword(kproduct=Produce.query.get(15), tag=Keyword.query.get(4))
    pk65 = Producetokeyword(kproduct=Produce.query.get(16), tag=Keyword.query.get(17))
    pk66 = Producetokeyword(kproduct=Produce.query.get(16), tag=Keyword.query.get(3))
    pk67 = Producetokeyword(kproduct=Produce.query.get(16), tag=Keyword.query.get(4))
    pk68 = Producetokeyword(kproduct=Produce.query.get(16), tag=Keyword.query.get(9))
    pk69 = Producetokeyword(kproduct=Produce.query.get(16), tag=Keyword.query.get(16))
    pk70 = Producetokeyword(kproduct=Produce.query.get(17), tag=Keyword.query.get(1))
    pk71 = Producetokeyword(kproduct=Produce.query.get(17), tag=Keyword.query.get(9))
    pk72 = Producetokeyword(kproduct=Produce.query.get(17), tag=Keyword.query.get(18))
    pk73 = Producetokeyword(kproduct=Produce.query.get(18), tag=Keyword.query.get(1))
    pk74 = Producetokeyword(kproduct=Produce.query.get(18), tag=Keyword.query.get(16))
    pk75 = Producetokeyword(kproduct=Produce.query.get(18), tag=Keyword.query.get(9))
    pk76 = Producetokeyword(kproduct=Produce.query.get(19), tag=Keyword.query.get(15))
    pk77 = Producetokeyword(kproduct=Produce.query.get(19), tag=Keyword.query.get(16))
    pk78 = Producetokeyword(kproduct=Produce.query.get(19), tag=Keyword.query.get(3))
    pk79 = Producetokeyword(kproduct=Produce.query.get(19), tag=Keyword.query.get(9))
    pk80 = Producetokeyword(kproduct=Produce.query.get(20), tag=Keyword.query.get(1))
    pk81 = Producetokeyword(kproduct=Produce.query.get(20), tag=Keyword.query.get(16))
    pk82 = Producetokeyword(kproduct=Produce.query.get(20), tag=Keyword.query.get(9))
    pk83 = Producetokeyword(kproduct=Produce.query.get(20), tag=Keyword.query.get(12))
    pk84 = Producetokeyword(kproduct=Produce.query.get(20), tag=Keyword.query.get(11))

    l1 = Listing(price=2.56, quantity=551, lproduct=Produce.query.get(2), owner=Supplier.query.get(16))
    l2 = Listing(price=3.27, quantity=1059, lproduct=Produce.query.get(1), owner=Supplier.query.get(4))
    l3 = Listing(price=0.59, quantity=710, lproduct=Produce.query.get(2), owner=Supplier.query.get(15))
    l4 = Listing(price=2.59, quantity=535, lproduct=Produce.query.get(9), owner=Supplier.query.get(10))
    l5 = Listing(price=2.04, quantity=682, lproduct=Produce.query.get(6), owner=Supplier.query.get(3))
    l6 = Listing(price=3.3, quantity=1254, lproduct=Produce.query.get(6), owner=Supplier.query.get(7))
    l7 = Listing(price=3.19, quantity=612, lproduct=Produce.query.get(10), owner=Supplier.query.get(5))
    l8 = Listing(price=1.22, quantity=748, lproduct=Produce.query.get(14), owner=Supplier.query.get(4))
    l9 = Listing(price=1.83, quantity=1236, lproduct=Produce.query.get(15), owner=Supplier.query.get(10))

    l11 = Listing(price=2.38, quantity=460, lproduct=Produce.query.get(6), owner=Supplier.query.get(15))
    l12 = Listing(price=3.02, quantity=588, lproduct=Produce.query.get(16), owner=Supplier.query.get(19))
    l13 = Listing(price=2.29, quantity=231, lproduct=Produce.query.get(10), owner=Supplier.query.get(14))
    l14 = Listing(price=1.84, quantity=717, lproduct=Produce.query.get(17), owner=Supplier.query.get(1))

    l16 = Listing(price=0.75, quantity=709, lproduct=Produce.query.get(14), owner=Supplier.query.get(18))
    l17 = Listing(price=0.51, quantity=826, lproduct=Produce.query.get(16), owner=Supplier.query.get(4))
    l18 = Listing(price=1.32, quantity=623, lproduct=Produce.query.get(13), owner=Supplier.query.get(17))

    l20 = Listing(price=1.19, quantity=996, lproduct=Produce.query.get(2), owner=Supplier.query.get(7))
    l21 = Listing(price=1.73, quantity=931, lproduct=Produce.query.get(14), owner=Supplier.query.get(5))
    l22 = Listing(price=0.81, quantity=166, lproduct=Produce.query.get(8), owner=Supplier.query.get(8))
    l23 = Listing(price=2.68, quantity=204, lproduct=Produce.query.get(3), owner=Supplier.query.get(12))
    l24 = Listing(price=3.02, quantity=615, lproduct=Produce.query.get(9), owner=Supplier.query.get(9))
    l25 = Listing(price=1.73, quantity=832, lproduct=Produce.query.get(4), owner=Supplier.query.get(13))
    l26 = Listing(price=1.53, quantity=181, lproduct=Produce.query.get(6), owner=Supplier.query.get(1))
    l27 = Listing(price=0.79, quantity=769, lproduct=Produce.query.get(15), owner=Supplier.query.get(13))

    l29 = Listing(price=3.28, quantity=962, lproduct=Produce.query.get(16), owner=Supplier.query.get(11))
    l30 = Listing(price=1.1, quantity=1198, lproduct=Produce.query.get(20), owner=Supplier.query.get(6))
    l31 = Listing(price=2.44, quantity=259, lproduct=Produce.query.get(10), owner=Supplier.query.get(15))
    l32 = Listing(price=3.04, quantity=180, lproduct=Produce.query.get(16), owner=Supplier.query.get(5))
    l33 = Listing(price=1.8, quantity=330, lproduct=Produce.query.get(1), owner=Supplier.query.get(17))
    l34 = Listing(price=1.94, quantity=353, lproduct=Produce.query.get(1), owner=Supplier.query.get(18))
    l35 = Listing(price=3.22, quantity=890, lproduct=Produce.query.get(11), owner=Supplier.query.get(6))

    l38 = Listing(price=0.87, quantity=1057, lproduct=Produce.query.get(15), owner=Supplier.query.get(15))
    l39 = Listing(price=1.64, quantity=956, lproduct=Produce.query.get(6), owner=Supplier.query.get(5))
    l40 = Listing(price=3.28, quantity=670, lproduct=Produce.query.get(17), owner=Supplier.query.get(6))
    l41 = Listing(price=1.92, quantity=567, lproduct=Produce.query.get(12), owner=Supplier.query.get(1))
    l42 = Listing(price=0.68, quantity=1145, lproduct=Produce.query.get(19), owner=Supplier.query.get(11))
    l43 = Listing(price=2.71, quantity=885, lproduct=Produce.query.get(18), owner=Supplier.query.get(9))
    l44 = Listing(price=0.69, quantity=190, lproduct=Produce.query.get(15), owner=Supplier.query.get(17))
    l45 = Listing(price=2, quantity=1109, lproduct=Produce.query.get(5), owner=Supplier.query.get(2))
    l46 = Listing(price=1.63, quantity=354, lproduct=Produce.query.get(7), owner=Supplier.query.get(13))

    l48 = Listing(price=1.67, quantity=763, lproduct=Produce.query.get(20), owner=Supplier.query.get(5))
    l49 = Listing(price=2.21, quantity=716, lproduct=Produce.query.get(4), owner=Supplier.query.get(19))
    l50 = Listing(price=2.47, quantity=383, lproduct=Produce.query.get(13), owner=Supplier.query.get(8))
    l51 = Listing(price=3.11, quantity=1229, lproduct=Produce.query.get(17), owner=Supplier.query.get(9))
    l52 = Listing(price=2.79, quantity=911, lproduct=Produce.query.get(16), owner=Supplier.query.get(16))
    l53 = Listing(price=2.24, quantity=635, lproduct=Produce.query.get(3), owner=Supplier.query.get(18))
    l54 = Listing(price=2.08, quantity=999, lproduct=Produce.query.get(7), owner=Supplier.query.get(10))
    l55 = Listing(price=2.87, quantity=896, lproduct=Produce.query.get(8), owner=Supplier.query.get(16))
    l56 = Listing(price=0.67, quantity=251, lproduct=Produce.query.get(16), owner=Supplier.query.get(7))
    l57 = Listing(price=2.41, quantity=508, lproduct=Produce.query.get(12), owner=Supplier.query.get(19))
    l58 = Listing(price=3.1, quantity=165, lproduct=Produce.query.get(14), owner=Supplier.query.get(11))
    l59 = Listing(price=3.2, quantity=1068, lproduct=Produce.query.get(19), owner=Supplier.query.get(19))
    l60 = Listing(price=2.98, quantity=846, lproduct=Produce.query.get(19), owner=Supplier.query.get(12))
    l61 = Listing(price=1.91, quantity=481, lproduct=Produce.query.get(1), owner=Supplier.query.get(10))
    l62 = Listing(price=2.37, quantity=1165, lproduct=Produce.query.get(18), owner=Supplier.query.get(12))
    l63 = Listing(price=1.18, quantity=634, lproduct=Produce.query.get(1), owner=Supplier.query.get(16))

    l65 = Listing(price=1.46, quantity=1143, lproduct=Produce.query.get(6), owner=Supplier.query.get(13))
    l66 = Listing(price=1.38, quantity=491, lproduct=Produce.query.get(20), owner=Supplier.query.get(11))
    l67 = Listing(price=0.69, quantity=331, lproduct=Produce.query.get(14), owner=Supplier.query.get(9))
    l68 = Listing(price=3.46, quantity=809, lproduct=Produce.query.get(11), owner=Supplier.query.get(14))

    l70 = Listing(price=3.2, quantity=1083, lproduct=Produce.query.get(5), owner=Supplier.query.get(3))
    l71 = Listing(price=1.21, quantity=318, lproduct=Produce.query.get(14), owner=Supplier.query.get(1))
    l72 = Listing(price=2.29, quantity=544, lproduct=Produce.query.get(6), owner=Supplier.query.get(9))
    l73 = Listing(price=2.11, quantity=207, lproduct=Produce.query.get(6), owner=Supplier.query.get(17))
    l74 = Listing(price=0.64, quantity=882, lproduct=Produce.query.get(9), owner=Supplier.query.get(15))
    l75 = Listing(price=2.59, quantity=185, lproduct=Produce.query.get(18), owner=Supplier.query.get(16))
    l76 = Listing(price=1.57, quantity=1143, lproduct=Produce.query.get(18), owner=Supplier.query.get(10))

    l78 = Listing(price=1.7, quantity=934, lproduct=Produce.query.get(6), owner=Supplier.query.get(10))
    l79 = Listing(price=0.65, quantity=501, lproduct=Produce.query.get(11), owner=Supplier.query.get(19))
    l80 = Listing(price=1.84, quantity=741, lproduct=Produce.query.get(3), owner=Supplier.query.get(10))

    l83 = Listing(price=3.31, quantity=784, lproduct=Produce.query.get(9), owner=Supplier.query.get(14))
    l84 = Listing(price=0.57, quantity=106, lproduct=Produce.query.get(17), owner=Supplier.query.get(8))
    l85 = Listing(price=2.99, quantity=1225, lproduct=Produce.query.get(19), owner=Supplier.query.get(7))
    l86 = Listing(price=1.13, quantity=865, lproduct=Produce.query.get(6), owner=Supplier.query.get(19))
    l87 = Listing(price=1.91, quantity=560, lproduct=Produce.query.get(3), owner=Supplier.query.get(19))
    l88 = Listing(price=3.45, quantity=883, lproduct=Produce.query.get(17), owner=Supplier.query.get(16))
    l89 = Listing(price=2.34, quantity=326, lproduct=Produce.query.get(15), owner=Supplier.query.get(19))
    l90 = Listing(price=2.45, quantity=110, lproduct=Produce.query.get(19), owner=Supplier.query.get(5))
    l91 = Listing(price=1.49, quantity=230, lproduct=Produce.query.get(19), owner=Supplier.query.get(6))
    l92 = Listing(price=2.61, quantity=889, lproduct=Produce.query.get(19), owner=Supplier.query.get(2))
    l93 = Listing(price=0.72, quantity=436, lproduct=Produce.query.get(10), owner=Supplier.query.get(7))
    l94 = Listing(price=1.58, quantity=1231, lproduct=Produce.query.get(10), owner=Supplier.query.get(10))

    l96 = Listing(price=1.19, quantity=582, lproduct=Produce.query.get(12), owner=Supplier.query.get(6))
    l97 = Listing(price=3.4, quantity=972, lproduct=Produce.query.get(3), owner=Supplier.query.get(14))
    l98 = Listing(price=1.95, quantity=1260, lproduct=Produce.query.get(13), owner=Supplier.query.get(15))

    l100 = Listing(price=1.81, quantity=226, lproduct=Produce.query.get(7), owner=Supplier.query.get(12))

    db.session.add_all([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,
                        p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,
                        k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21,
                        pk1,pk2,pk3,pk4,pk5,pk6,pk7,pk8,pk9,pk10,pk11,pk12,pk13,pk14,pk15,pk16,pk17,pk18,pk19,pk20,pk21,pk22,pk23,pk24,pk25,pk26,pk27,pk28,pk29,pk30,pk31,pk32,pk33,pk34,pk35,pk36,pk37,pk38,pk39,pk40,pk41,pk42,pk43,pk44,pk45,pk46,pk47,pk48,pk49,pk50,pk51,pk52,pk53,pk54,pk55,pk56,pk57,pk58,pk59,pk60,pk61,pk62,pk63,pk64,pk65,pk66,pk67,pk68,pk69,pk70,pk71,pk72,pk73,pk74,pk75,pk76,pk77,pk78,pk79,pk80,pk81,pk82,pk83,pk84,
                        l1,l2,l3,l4,l5,l6,l7,l8,l9,l11,l12,l13,l14,l16,l17,l18,l20,l21,l22,l23,l24,l25,l26,l27,l29,l30,l31,l32,l33,l34,l35,l38,l39,l40,l41,l42,l43,l44,l45,l46,l48,l49,l50,l51,l52,l53,l54,l55,l56,l57,l58,l59,l60,l61,l62,l63,l65,l66,l67,l68,l70,l71,l72,l73,l74,l75,l76,l78,l79,l80,l83,l84,l85,l86,l87,l88,l89,l90,l91,l92,l93,l94,l96,l97,l98,l100
                        ])
    db.session.commit()

    return "Database has been populated."

@app.route('/resetDb')
def resetDb():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()
    popdb()
    return "DB reset"