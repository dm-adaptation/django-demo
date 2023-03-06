from .models import User


def fun_get_users():
    users = User.objects.all()
    total_rows = users.count()
    print('查询到' + str(total_rows) + '条记录')
    for user in users:
        print(user.name)
    print('')
