from datetime import datetime

def to_tracking_detail(rows: list) -> list:
    list_tracking_detail: list = []
    for row in rows:
        list_tracking_detail.append(TrackingDetail(row))
    return list_tracking_detail


class TrackingDetail:

    __id: int
    __id_tracking_fk: int
    __detail_head: str
    __detail_text: str
    __detail_time: int
    __audit_time: int

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__id_tracking_fk = row[1]
        self.__detail_head = row[2]
        self.__detail_text = row[3]
        self.__detail_time = row[4]
        self.__audit_time = row[5]

    def is_equals(self, detail_head: str, detail_text: str, detail_time: int) -> bool:
        if detail_head != self.__detail_head:
            return False
        if detail_text != self.__detail_text:
            return False
        if detail_time != self.__detail_time:
            return False
        return True

    def msg_to_user(self, format_date: str) -> str:
        date_time = datetime.fromtimestamp(self.__detail_time)
        return f'''Actualización del pedido:
            {self.__detail_head}
            {self.__detail_text}
            {date_time.strftime(format_date)}
            '''
