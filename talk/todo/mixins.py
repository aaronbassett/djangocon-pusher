# -*- coding: utf-8 -*-

from django.conf import settings
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete
from pusher import Pusher


class SelfPublishModel(object):

    def _publish(self, action):
        serializer = self.serializer_class(instance=self)
        data = serializer.serialize()

        pusher = Pusher(
            app_id=settings.PUSHER_APP_ID,
            key=settings.PUSHER_KEY,
            secret=settings.PUSHER_SECRET
        )

        pusher.trigger(self.channel_name, action, data)

    def save(self, *args, **kwargs):
        if not self.pk:
            action = u"created"
        else:
            action = u"updated"

        self._publish(action)
        super(SelfPublishModel, self).save(*args, **kwargs)


@receiver(pre_delete)
def _self_publish_model_delete(sender, instance, **kwargs):
    if isinstance(instance, SelfPublishModel):
        instance._publish(u"deleted")
