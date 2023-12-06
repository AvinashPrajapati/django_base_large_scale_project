from django.shortcuts import redirect
# from _member.models import Member

# def is_member_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         user = request.user
#         member_obj=None
#         try:
#             member_obj = Member.objects.get(user=request.user)
#         except Exception as e:
#             print("not a member :",e)
#         if member_obj:
#             if not member_obj.is_expired():
#                 return view_func(request, *args, **kwargs)
#             else:
#                 member_obj.is_member = False
#                 member_obj.save()
#                 return redirect("_member:payment_platform")
#         else:
#             return redirect("_member:payment_platform")
#     return wrapper