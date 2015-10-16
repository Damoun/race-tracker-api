"""This file provide the base for every models"""
from .extensions import DB


class CrudMixin(object):
    """Mixin that create/read/update/delete methods"""

    __table_args__ = {'extend_existing': True}

    @classmethod
    def create(cls, commit=True, **kwargs):
        """Creates a new record and saves to database."""
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    @classmethod
    def get(cls, row_id):
        """Retrieve a row by the id"""
        return cls.query.get(row_id)

    @classmethod
    def get_or_404(cls, row_id):
        """"Retrieve a row by the id or abort with 404"""
        return cls.query.get_or_404(row_id)

    def update(self, commit=True, **kwargs):
        """Update existing record and saves to database."""
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Saves record to database."""
        DB.session.add(self)
        if commit:
            DB.session.commit()
        return self

    def delete(self, commit=True):
        """Removes the record from database."""
        DB.session.delete(self)
        return commit and DB.session.commit()


class Model(CrudMixin, DB.Model):
    """This class provice a base for every model class"""
    __abstract__ = True
