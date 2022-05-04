from sqlalchemy import UniqueConstraint, ForeignKeyConstraint

from app import db

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return str({'id': self.id, 'name': self.class_name})


class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return str({'id': self.id, 'name': self.feature_name, 'type': self.type})

class ClassToFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey("class.id", ondelete='CASCADE'))
    feature_id = db.Column(db.Integer, db.ForeignKey("feature.id", ondelete='CASCADE'))
    __table_args__ = (UniqueConstraint('feature_id', 'class_id', name='c_f'),)

    def __repr__(self):
        return str({'class_id': self.class_id, 'feature_id': self.feature_id})


class FeatureToPossibleIntValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey("feature.id", ondelete='CASCADE'), nullable=False)
    value = db.Column(db.REAL(), nullable=False)
    __table_args__ = (UniqueConstraint('feature_id', 'value', name='_feat_v'),)

    def __repr__(self):
        return str({'id': self.id, 'feature_id': self.feature_id, 'value': self.value})


class FeatureToPossibleStrValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey("feature.id", ondelete='CASCADE'), nullable=False)
    value = db.Column(db.String(80), nullable=False)
    __table_args__ = (UniqueConstraint('feature_id', 'value', name='_feat_v'),)

    def __repr__(self):
        return str({'id': self.id, 'feature_id': self.feature_id, 'value': self.value})


class FeatureToPossibleIntervalValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey("feature.id", ondelete='CASCADE'), nullable=False)
    value_beg = db.Column(db.REAL(), nullable=False)
    value_end = db.Column(db.REAL(), nullable=False)
    __table_args__ = (UniqueConstraint('feature_id', 'value_beg', 'value_end', name='_feat_v_v'),)

    def __repr__(self):
        return str(
            {'id': self.id, 'feature_id': self.feature_id, 'value_beg': self.value_beg, 'value_end': self.value_end})


class ClassToFeatureToStrValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer(), db.ForeignKey("class.id", ondelete='CASCADE'), nullable=False)
    value_id = db.Column(db.Integer(), db.ForeignKey("feature_to_possible_str_value.id", ondelete='CASCADE'),
                         nullable=False)
    __table_args__ = (UniqueConstraint('class_id', 'value_id', name='_feat_v'),)

    def __repr__(self):
        return str({'id': self.id, 'value_id': self.value_id})


class ClassToFeatureToIntValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer(), db.ForeignKey("class.id", ondelete='CASCADE'), nullable=False)
    value_id = db.Column(db.Integer(), db.ForeignKey("feature_to_possible_int_value.id", ondelete='CASCADE'),
                         nullable=False)
    __table_args__ = (UniqueConstraint('class_id', 'value_id', name='_feat_v'),)

    def __repr__(self):
        return str({'id': self.id, 'value_id': self.value_id})


class ClassToFeatureToIntervalValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer(), db.ForeignKey("class.id", ondelete='CASCADE'), nullable=False)
    value_id = db.Column(db.Integer(), db.ForeignKey("feature_to_possible_interval_value.id", ondelete='CASCADE'),
                         nullable=False)
    __table_args__ = (UniqueConstraint('class_id', 'value_id', name='_feat_v'), )

    def __repr__(self):
        return str({'id': self.id, 'value_id': self.value_id})
