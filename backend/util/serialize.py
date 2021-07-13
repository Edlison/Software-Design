# @Author  : Edlison
# @Date    : 7/12/21 21:10


def _serialize_model(model):
    """
    :param model: 传入的是一个db.Model对象.
    :type model: db.Model
    :return:
    :rtype: dict
    """
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def serialize_model_list(models):
    """
    将数组中每一个元素，生成对应字典。
    :param o: 传入的是一个对象数组.
    :type o: list
    :return: l
    :rtype: list
    """
    l = []
    for each in models:
        l.append(_serialize_model(each))
    return l
