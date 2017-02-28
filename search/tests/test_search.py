from mock import patch

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, LiveServerTestCase

from search import signals
from jmbo.models import ModelBase


class TestIndexUpdateHandlers(TestCase):
    @patch("search.signals.handle_index_update")
    def test_add_to_index(self, handler):
        assert True

    def test_remove_from_index(self):
        assert True

    def test_handle_index_update(self):
        assert True


class TestModelSignalProcessor(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.instance = ModelBase.objects.create()
        cls.processor = signals.ModelBaseSignalProcessor(None, None)
        cls.content_type = ContentType.objects.get_for_model(
            cls.instance.__class__
        )
        cls.callback_params = {
            "content_type_id": cls.content_type.id,
            "pk": cls.instance.pk
        }
        cls.empty_kwargs = {}

    @patch("search.tasks.update_index")
    def test_handle_save(self, task):
        self.processor.handle_save(None, self.instance, **self.empty_kwargs)
        task.assert_called_once()
        task.assert_called_with(
            callback = signals.ADD_CALLBACK,
            callback_params = self.callback_params,
            **self.empty_kwargs
        )

    @patch("search.tasks.update_index")
    def test_handle_delete(self, task):
        self.processor.handle_delete(None, self.instance, **self.empty_kwargs)
        task.assert_called_once()
        task.assert_called_with(
            callback = signals.DELETE_CALLBACK,
            callback_params = self.callback_params,
            **self.empty_kwargs
        )
