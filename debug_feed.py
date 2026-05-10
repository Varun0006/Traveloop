from app import create_app
from app.models.trip import Trip
from app.models.interaction import Like, Comment

app = create_app('development')
with app.app_context():
    try:
        trips_query = Trip.query.filter_by(is_public=True).order_by(Trip.created_at.desc())
        pagination = trips_query.paginate(page=1, per_page=9)
        for trip in pagination.items:
            print("Trip:", trip.title)
            print("Image URL:", trip.image_url)
            print("Username:", trip.user.username)
            print("Like count:", trip.likes.count())
            print("Comment count:", trip.comments.count())
            print("---")
        print("Success!")
    except Exception as e:
        import traceback
        traceback.print_exc()
