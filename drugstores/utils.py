def get_schedule_representation(data):
    open_list = [
        data.schedule.monday_open,
        data.schedule.tuesday_open,
        data.schedule.wednesday_open,
        data.schedule.thursday_open,
        data.schedule.friday_open,
        data.schedule.saturday_open,
        data.schedule.sunday_open
    ]
    close_list = [
        data.schedule.monday_close,
        data.schedule.tuesday_close,
        data.schedule.wednesday_close,
        data.schedule.thursday_close,
        data.schedule.friday_close,
        data.schedule.saturday_close,
        data.schedule.sunday_close
    ]

    """проверка на круглосуточную работу аптеки"""
    open_set = set(open_list)
    close_set = set(close_list)
    if (
            len(open_set) == 1
            and len(close_set) == 1
            and open_set.pop() is None
            and close_set.pop().strftime('%H:%M') == '23:59'
    ):
        return 'круглосуточно'

    """проверка на одинаковую работу аптеки все дни"""
    open_set = set(open_list)
    close_set = set(close_list)
    if (
            len(open_set) == 1
            and len(close_set) == 1
    ):
        return f'ежедневно {open_set.pop().strftime("%H:%M")}-{close_set.pop().strftime("%H:%M")}'

    return 'Не удалось объединить расписание в одну строку'
