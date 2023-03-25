from django.http import HttpResponse, JsonResponse
from Testapp.models import BlockedDay, Room
from Testapp.serializers import NumberSerializer

def available_rooms(request, check_in, check_out, building):
    try:
        days = BlockedDay.objects.filter(Day__gte=str(check_in), Day__lte=str(check_out))
    except BlockedDay.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        res = []
        rooms_not_booked = Room.objects
        for r in days.values('Room'):
            rooms_not_booked = rooms_not_booked.exclude(id = r['Room'])
        print(rooms_not_booked.values())
        for room in rooms_not_booked:
            if str(room.Room_Type.Building) == building:
                res += [{'Number': room.Number, 'Price': room.Price, 'Type': room.Room_Type.Type}] 
                
        serializer = NumberSerializer(res, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=404)