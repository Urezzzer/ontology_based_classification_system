import json

from sqlalchemy.exc import IntegrityError
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import copy

from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

from tables import *

db.create_all()


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@app.route('/', methods=['POST', 'DELETE', 'GET', 'PUT'])
def index():
    """ Объект - структура вида:
    { "object": [
        {
            "id": ...,
            "feature_name": "...",
            "type": ...,
            "value": ...
        },
        ...
    ]
    }"""

    _object = json.loads(request.data.decode('utf-8'))['object']
    classification = {}
    coincidence = {}
    classes = []
    features = []

    for _class in db.session.query(Class).all():
        classes.append(object_as_dict(_class))
    for _feature in db.session.query(Feature).all():
        features.append(object_as_dict(_feature))

    class2feature = copy.deepcopy(classes)
    for i in range(len(class2feature)):
        if 'features' not in class2feature[i].keys():
            class2feature[i]['features'] = []
        for _class, _feature in db.session.query(Class, Feature). \
                filter(Class.id == ClassToFeature.class_id). \
                filter(Feature.id == ClassToFeature.feature_id).all():
            if classes[i] == object_as_dict(_class):
                class2feature[i]['features'].append(object_as_dict(_feature))

    class2feature2value = copy.deepcopy(class2feature)
    for i in range(len(classes)):
        for j in range(len(class2feature2value[i]['features'])):
            k = features.index(class2feature2value[i]['features'][j])
            if 'values' not in class2feature2value[i]['features'][j].keys():
                class2feature2value[i]['features'][j]['values'] = []
            for _class, _feature, _value in db.session.query(Class, Feature, FeatureToPossibleIntervalValue). \
                    filter(ClassToFeatureToIntervalValue.value_id == FeatureToPossibleIntervalValue.id). \
                    filter(ClassToFeatureToIntervalValue.class_id == Class.id). \
                    filter(Feature.id == FeatureToPossibleIntervalValue.feature_id).all():
                if classes[i] == object_as_dict(_class) and features[k] == object_as_dict(_feature):
                    class2feature2value[i]['features'][j]['values'].append(object_as_dict(_value))
            for _class, _feature, _value in db.session.query(Class, Feature, FeatureToPossibleIntValue). \
                    filter(ClassToFeatureToIntValue.value_id == FeatureToPossibleIntValue.id). \
                    filter(ClassToFeatureToIntValue.class_id == Class.id). \
                    filter(Feature.id == FeatureToPossibleIntValue.feature_id).all():
                if classes[i] == object_as_dict(_class) and features[k] == object_as_dict(_feature):
                    class2feature2value[i]['features'][j]['values'].append(object_as_dict(_value))
            for _class, _feature, _value in db.session.query(Class, Feature, FeatureToPossibleStrValue). \
                    filter(ClassToFeatureToStrValue.value_id == FeatureToPossibleStrValue.id). \
                    filter(ClassToFeatureToStrValue.class_id == Class.id). \
                    filter(Feature.id == FeatureToPossibleStrValue.feature_id).all():
                if classes[i] == object_as_dict(_class) and features[k] == object_as_dict(_feature):
                    class2feature2value[i]['features'][j]['values'].append(object_as_dict(_value))

    classes = []
    explaination = []

    for _class in class2feature2value:
        classification[_class['class_name']] = {}
        coincidence[_class['class_name']] = {}

        feature_list = []
        for _feature in _class['features']:
            classification[_class['class_name']][_feature['feature_name']] = False
            coincidence[_class['class_name']][_feature['feature_name']] = False
            for _value in _feature['values']:
                for _object_feature in _object:
                    if _feature['id'] == _object_feature['id']:
                        coincidence[_class['class_name']][_feature['feature_name']] = True
                        if _feature['type'] == 0:
                            if _value['value_beg'] <= _object_feature['value'] <= _value['value_end']:
                                classification[_class['class_name']][_feature['feature_name']] = True
                        elif _value == _object_feature['value']:
                            classification[_class['class_name']][_feature['feature_name']] = True

            if coincidence[_class['class_name']][_feature['feature_name']] and \
                not classification[_class['class_name']][_feature['feature_name']]:
                feature_list.append(_feature['feature_name'])

        if feature_list:
            explaination.append({'class_name': _class['class_name'], 'feature_list': feature_list})
        if classification[_class['class_name']] == \
                coincidence[_class['class_name']]:
            classes.append(_class['class_name'])

    return json.dumps(
        {'object': _object, 'classification': classification, 'coincidence': coincidence, \
        'predicted_classes': classes, 'explaination': explaination},
        ensure_ascii=False)


@app.route('/editor/', methods=['POST', 'DELETE', 'GET', 'PUT'])
def editor():
    return 'Editor Page!'


@app.route('/get_knowledge/', methods=['GET'])
def get_knowledge():
    classes = []
    features = []

    for _class in db.session.query(Class).all():
        classes.append(object_as_dict(_class))
    for _feature in db.session.query(Feature).all():
        features.append(object_as_dict(_feature))

    possible_value2feature = copy.deepcopy(features)
    for i in range(len(possible_value2feature)):
        if 'values' not in possible_value2feature[i].keys():
            possible_value2feature[i]['values'] = []
        for _feature, _value in db.session.query(Feature, FeatureToPossibleStrValue). \
                filter(Feature.id == FeatureToPossibleStrValue.feature_id).all():
            if features[i] == object_as_dict(_feature):
                possible_value2feature[i]['values'].append(object_as_dict(_value))
        for _feature, _value in db.session.query(Feature, FeatureToPossibleIntValue). \
                filter(Feature.id == FeatureToPossibleIntValue.feature_id).all():
            if features[i] == object_as_dict(_feature):
                possible_value2feature[i]['values'].append(object_as_dict(_value))
        for _feature, _value in db.session.query(Feature, FeatureToPossibleIntervalValue). \
                filter(Feature.id == FeatureToPossibleIntervalValue.feature_id).all():
            if features[i] == object_as_dict(_feature):
                possible_value2feature[i]['values'].append(object_as_dict(_value))

    class2feature = copy.deepcopy(classes)
    for i in range(len(class2feature)):
        if 'features' not in class2feature[i].keys():
            class2feature[i]['features'] = []
        for _class, _feature in db.session.query(Class, Feature). \
                filter(Class.id == ClassToFeature.class_id). \
                filter(Feature.id == ClassToFeature.feature_id).all():
            if classes[i] == object_as_dict(_class):
                class2feature[i]['features'].append(object_as_dict(_feature))

    class2feature2value = copy.deepcopy(class2feature)
    for i in range(len(classes)):
        for j in range(len(class2feature2value[i]['features'])):
            k = features.index(class2feature2value[i]['features'][j])
            if 'values' not in class2feature2value[i]['features'][j].keys():
                class2feature2value[i]['features'][j]['values'] = []
            for _class, _feature, _value in db.session.query(Class, Feature, FeatureToPossibleIntervalValue). \
                    filter(ClassToFeatureToIntervalValue.value_id == FeatureToPossibleIntervalValue.id). \
                    filter(ClassToFeatureToIntervalValue.class_id == Class.id). \
                    filter(Feature.id == FeatureToPossibleIntervalValue.feature_id).all():
                if classes[i] == object_as_dict(_class) and features[k] == object_as_dict(_feature):
                    class2feature2value[i]['features'][j]['values'].append(object_as_dict(_value))
            for _class, _feature, _value in db.session.query(Class, Feature, FeatureToPossibleIntValue). \
                    filter(ClassToFeatureToIntValue.value_id == FeatureToPossibleIntValue.id). \
                    filter(ClassToFeatureToIntValue.class_id == Class.id). \
                    filter(Feature.id == FeatureToPossibleIntValue.feature_id).all():
                if classes[i] == object_as_dict(_class) and features[k] == object_as_dict(_feature):
                    class2feature2value[i]['features'][j]['values'].append(object_as_dict(_value))
            for _class, _feature, _value in db.session.query(Class, Feature, FeatureToPossibleStrValue). \
                    filter(ClassToFeatureToStrValue.value_id == FeatureToPossibleStrValue.id). \
                    filter(ClassToFeatureToStrValue.class_id == Class.id). \
                    filter(Feature.id == FeatureToPossibleStrValue.feature_id).all():
                if classes[i] == object_as_dict(_class) and features[k] == object_as_dict(_feature):
                    class2feature2value[i]['features'][j]['values'].append(object_as_dict(_value))

    return json.dumps({'possible_value2feature': possible_value2feature,
                       'class2feature2value': class2feature2value},
                      ensure_ascii=False)


@app.route('/delete_class/', methods=['DELETE'])
def delete_class():
    """Принимает class_id"""
    class_id = json.loads(request.data.decode('utf-8'))['class_id']
    ClassToFeature.query.filter_by(class_id=class_id).delete()
    ClassToFeatureToIntervalValue.query.filter_by(class_id=class_id).delete()
    ClassToFeatureToIntValue.query.filter_by(class_id=class_id).delete()
    ClassToFeatureToStrValue.query.filter_by(class_id=class_id).delete()
    Class.query.filter_by(id=class_id).delete()
    db.session.commit()
    return json.dumps({'success': not bool(Class.query.filter_by(id=class_id).all())}, ensure_ascii=False)


@app.route('/delete_feature/', methods=['DELETE'])
def delete_feature():
    """Принимает feature_id"""
    feature_id = json.loads(request.data.decode('utf-8'))['feature_id']
    ClassToFeature.query.filter_by(feature_id=feature_id).delete()
    FeatureToPossibleStrValue.query.filter_by(feature_id=feature_id).delete()
    FeatureToPossibleIntValue.query.filter_by(feature_id=feature_id).delete()
    FeatureToPossibleIntervalValue.query.filter_by(feature_id=feature_id).delete()
    Feature.query.filter_by(id=feature_id).delete()
    db.session.commit()
    return json.dumps({'success': not bool(Feature.query.filter_by(id=feature_id).all())}, ensure_ascii=False)


@app.route('/update_class/', methods=['PUT'])
def update_class():
    """Принимает class_id и новое имя класса"""
    class_id = json.loads(request.data.decode('utf-8'))['class_id']
    class_name = json.loads(request.data.decode('utf-8'))['class_name']
    try:
        _class = Class.query.filter_by(id=class_id).first()
        _class.class_name = class_name
        db.session.commit()
        value = object_as_dict(Class.query.filter_by(class_name=class_name).first())
        success = bool(value)
    except AttributeError:
        success = 'Класса с таким id нет'
        value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/update_feature/', methods=['PUT'])
def update_feature():
    """Принимает feature_id и новое имя признака"""
    feature_id = json.loads(request.data.decode('utf-8'))['feature_id']
    feature_name = json.loads(request.data.decode('utf-8'))['feature_name']
    type = json.loads(request.data.decode('utf-8'))['type']
    try:
        _feature = Feature.query.filter_by(id=feature_id).first()
        _feature.feature_name = feature_name
        _feature.type = type
        db.session.commit()
        value = object_as_dict(Feature.query.filter_by(feature_name=feature_name, type=type).first())
        success = bool(value)
    except AttributeError:
        success = 'Признака с таким id нет'
        value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/insert_class/', methods=['POST'])
def insert_class():
    """Принимает имя класса"""
    try:
        class_name = json.loads(request.data.decode('utf-8'))['class_name']
        db.session.add(Class(class_name=class_name))
        db.session.commit()
        value = object_as_dict(Class.query.filter_by(class_name=class_name).first())
        success = bool(value)
    except IntegrityError:
        success = 'Такой класс уже есть'
        value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/insert_feature/', methods=['POST'])
def insert_feature():
    """Принимает имя признака"""
    try:
        feature_name = json.loads(request.data.decode('utf-8'))['feature_name']
        type = json.loads(request.data.decode('utf-8'))['type']
        db.session.add(Feature(feature_name=feature_name, type=type))
        db.session.commit()
        value = object_as_dict(Feature.query.filter_by(feature_name=feature_name, type=type).first())
        success = bool(Feature.query.filter_by(feature_name=feature_name, type=type).all())
    except IntegrityError:
        success = 'Такой признак уже есть'
        value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/delete_feature2class/', methods=['DELETE'])
def delete_feature2class():
    """Удаляет связь между классом и признаком
        Вход: class_id и feature_id"""
    class_id = json.loads(request.data.decode('utf-8'))['class_id']
    feature_id = json.loads(request.data.decode('utf-8'))['feature_id']
    ClassToFeature.query.filter_by(class_id=class_id, feature_id=feature_id).delete()
    db.session.commit()
    return json.dumps({'success': not bool(ClassToFeature.query.filter_by(class_id=class_id,
                                                                          feature_id=feature_id).all())},
                      ensure_ascii=False)


@app.route('/insert_feature2class/', methods=['POST'])
def insert_feature2class():
    """Создает связь между классом и признаком
        Вход: class_id и feature_id"""
    class_id = json.loads(request.data.decode('utf-8'))['class_id']
    feature_id = json.loads(request.data.decode('utf-8'))['feature_id']
    try:
        if bool(Class.query.filter_by(id=class_id).all()) and bool(Feature.query.filter_by(id=feature_id).all()):
            db.session.add(ClassToFeature(class_id=class_id, feature_id=feature_id))
            db.session.commit()
        value = object_as_dict(ClassToFeature.query.filter_by(class_id=class_id,
                                                              feature_id=feature_id).first())
        success = bool(value)
    except IntegrityError:
        success = 'value existed'
        value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/delete_posvalue2feature/', methods=['DELETE'])
def delete_posvalue2feature():
    """Удаляет связь между признаком и возможным значением
        Вход: type - тип признака
        value_id - id значения из таблицы значений типа type"""
    type = json.loads(request.data.decode('utf-8'))['type']
    id = json.loads(request.data.decode('utf-8'))['value_id']
    if type == 0:
        FeatureToPossibleIntervalValue.query.filter_by(id=id).delete()
        ClassToFeatureToIntervalValue.query.filter_by(value_id=id).delete()
        db.session.commit()
        success = not bool(FeatureToPossibleIntervalValue.query.filter_by(id=id).all())
    elif type == 1:
        FeatureToPossibleIntValue.query.filter_by(id=id).delete()
        ClassToFeatureToIntValue.query.filter_by(value_id=id).delete()
        db.session.commit()
        success = not bool(FeatureToPossibleIntValue.query.filter_by(id=id).all())
    elif type == 2:
        FeatureToPossibleStrValue.query.filter_by(id=id).delete()
        ClassToFeatureToStrValue.query.filter_by(value_id=id).delete()
        db.session.commit()
        success = not bool(FeatureToPossibleStrValue.query.filter_by(id=id).all())
    return json.dumps({'success': success}, ensure_ascii=False)


@app.route('/insert_posvalue2feature/', methods=['POST'])
def insert_posvalue2feature():
    """Создает связь между признаком и возможным значением
            Вход: type - тип признака
            feature_id - id признака,
            value или [from, to] - значение признака (в зависимости от типа type)"""
    type = json.loads(request.data.decode('utf-8'))['type']
    feature_id = json.loads(request.data.decode('utf-8'))['feature_id']
    if type == 0:
        value_beg = json.loads(request.data.decode('utf-8'))['from']
        value_end = json.loads(request.data.decode('utf-8'))['to']
        try:
            db.session.add(FeatureToPossibleIntervalValue(feature_id=feature_id,
                                                          value_beg=value_beg,
                                                          value_end=value_end))
            db.session.commit()
            value = object_as_dict(FeatureToPossibleIntervalValue.query.filter_by(feature_id=feature_id,
                                                                                  value_beg=value_beg,
                                                                                  value_end=value_end).first())
            success = bool(value)
        except IntegrityError:
            success = 'value existed'
            value = {}
    elif type == 1:
        value = json.loads(request.data.decode('utf-8'))['value']
        try:
            db.session.add(FeatureToPossibleIntValue(feature_id=feature_id, value=value))
            db.session.commit()
            value = object_as_dict(
                FeatureToPossibleIntValue.query.filter_by(feature_id=feature_id, value=value).first())
            success = bool(value)
        except IntegrityError:
            success = 'value existed'
            value = {}
    elif type == 2:
        value = json.loads(request.data.decode('utf-8'))['value']
        try:
            db.session.add(FeatureToPossibleStrValue(feature_id=feature_id, value=value))
            db.session.commit()
            value = object_as_dict(
                FeatureToPossibleStrValue.query.filter_by(feature_id=feature_id, value=value).first())
            success = bool(value)
        except IntegrityError:
            success = 'value existed'
            value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/update_posvalue2feature/', methods=['PUT'])
def update_posvalue2feature():
    """Обновляет связь между признаком и возможным значением
            Вход: type - тип признака
            value_id - id значения из таблицы значений типа type,
            value или [from, to] - новое значение признака (в зависимости от типа type)"""
    type = json.loads(request.data.decode('utf-8'))['type']
    id = json.loads(request.data.decode('utf-8'))['value_id']
    if type == 0:
        new_from = json.loads(request.data.decode('utf-8'))['from']
        new_to = json.loads(request.data.decode('utf-8'))['to']
        try:
            _value = FeatureToPossibleIntervalValue.query.filter_by(id=id).first()
            _value.value_beg = new_from
            _value.value_end = new_to
            db.session.commit()
            value = object_as_dict(FeatureToPossibleIntervalValue.query.filter_by(value_beg=new_from,
                                                                                  value_end=new_to).first())
            success = bool(value)
        except AttributeError:
            success = 'Значение типа {} под индексом {} отсутствует'.format(type, id)
            value = {}
    elif type == 1:
        new_value = json.loads(request.data.decode('utf-8'))['value']
        try:
            _value = FeatureToPossibleIntValue.query.filter_by(id=id).first()
            _value.value = new_value
            db.session.commit()
            value = object_as_dict(FeatureToPossibleIntValue.query.filter_by(value=new_value).first())
            success = bool(value)
        except AttributeError:
            success = 'Значение типа {} под индексом {} отсутствует'.format(type, id)
            value = {}
    elif type == 2:
        new_value = json.loads(request.data.decode('utf-8'))['value']
        try:
            _value = FeatureToPossibleStrValue.query.filter_by(id=id).first()
            _value.value = new_value
            db.session.commit()
            value = object_as_dict(FeatureToPossibleStrValue.query.filter_by(value=new_value).first())
            success = bool(value)
        except AttributeError:
            success = 'Значение типа {} под индексом {} отсутствует'.format(type, id)
            value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


@app.route('/delete_picked_value2feature2class/', methods=['DELETE'])
def delete_picked_value2feature2class():
    """Удаляет связь между классом и значениями его признака
        Вход: type - тип признака
        class_id - id класса
        value_id - id значения из таблицы значений типа type"""
    type = json.loads(request.data.decode('utf-8'))['type']
    value_id = json.loads(request.data.decode('utf-8'))['value_id']
    class_id = json.loads(request.data.decode('utf-8'))['class_id']
    if type == 0:
        ClassToFeatureToIntervalValue.query.filter_by(class_id=class_id, value_id=value_id).delete()
        db.session.commit()
        success = not bool(ClassToFeatureToIntervalValue.query.filter_by(value_id=value_id, class_id=class_id).all())
    elif type == 1:
        ClassToFeatureToIntValue.query.filter_by(class_id=class_id, value_id=value_id).delete()
        db.session.commit()
        success = not bool(ClassToFeatureToIntValue.query.filter_by(value_id=value_id, class_id=class_id).all())
    elif type == 2:
        ClassToFeatureToStrValue.query.filter_by(class_id=class_id, value_id=value_id).delete()
        db.session.commit()
        success = not bool(ClassToFeatureToStrValue.query.filter_by(value_id=value_id, class_id=class_id).all())
    return json.dumps({'success': success}, ensure_ascii=False)


@app.route('/insert_picked_value2feature2class/', methods=['POST'])
def insert_picked_value2feature2class():
    """Добавляет связь между классом и значениями его признака
        Вход: type - тип признака
        class_id - id класса
        value_id - id значения из таблицы значений типа type"""
    type = json.loads(request.data.decode('utf-8'))['type']
    value_id = json.loads(request.data.decode('utf-8'))['value_id']
    class_id = json.loads(request.data.decode('utf-8'))['class_id']
    if type == 0:
        try:
            db.session.add(ClassToFeatureToIntervalValue(value_id=value_id, class_id=class_id))
            db.session.commit()
            value = object_as_dict(
                ClassToFeatureToIntervalValue.query.filter_by(value_id=value_id, class_id=class_id).first())
            success = bool(value)
        except IntegrityError:
            success = 'value existed'
            value = {}
    elif type == 1:
        try:
            db.session.add(ClassToFeatureToIntValue(value_id=value_id, class_id=class_id))
            db.session.commit()
            value = object_as_dict(
                ClassToFeatureToIntValue.query.filter_by(value_id=value_id, class_id=class_id).first())
            success = bool(value)
        except IntegrityError:
            success = 'value existed'
            value = {}
    elif type == 2:
        try:
            db.session.add(ClassToFeatureToStrValue(value_id=value_id, class_id=class_id))
            db.session.commit()
            value = object_as_dict(
                ClassToFeatureToStrValue.query.filter_by(value_id=value_id, class_id=class_id).first())
            success = bool(value)
        except IntegrityError:
            success = 'value existed'
            value = {}
    return json.dumps({'success': success,
                       'value': value}, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
