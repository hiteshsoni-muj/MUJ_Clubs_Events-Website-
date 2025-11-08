from django.shortcuts import render, redirect

# Registration view
def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        # later we’ll save this to the database
        return redirect('club_list')
    return render(request, "events/register.html")

# Club list view
def club_list(request):
    clubs = [
        {"name": "Olympism Club", "events": [
            {"name": "Inter-College Sports Meet", "date": "Nov 10", "location": "Main Ground"}
        ]},
        {"name": "Aperture", "events": [
            {"name": "Photography Contest", "date": "Nov 12", "location": "Auditorium"}
        ]},
    ]
    return render(request, "events/club_list.html", {"clubs": clubs})