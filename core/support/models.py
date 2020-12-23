import os

from django.db import models
from django.conf import settings
from django.urls import reverse

from oddslingers.model_utils import BaseModel
from oddslingers.utils import get_short_uuid
from poker.models import PokerTable


class TicketSource:
    ADMIN = 0
    EMAIL = 1
    SUPPORT_PAGE = 2
    TABLE_REPORT_BUG = 3
    TABLEBEAT_EXC = 4
    BOTBEAT_EXC = 5

TICKET_SOURCE_LABELS = {
    TicketSource.ADMIN: 'Admin Created',
    TicketSource.EMAIL: 'Email to support@oddslingers.com',
    TicketSource.SUPPORT_PAGE: 'Support Page Submition',
    TicketSource.TABLE_REPORT_BUG: 'Report Bug on a Table',
    TicketSource.TABLEBEAT_EXC: 'Tablebeat Exception',
    TicketSource.BOTBEAT_EXC: 'Botbeat Exception',
}


class SupportTicket(BaseModel):
    subject = models.CharField(max_length=256, blank=True, null=True)

    status = models.CharField(
        choices=(('open', 'open'), ('closed', 'closed')),
        max_length=16,
        default='open',
    )
    source = models.IntegerField(
        choices=((key, name) for key, name in TICKET_SOURCE_LABELS.items()),
        default=TicketSource.ADMIN,
    )

    table = models.ForeignKey(
        PokerTable,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    # TODO: assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, ...)

    opened = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    closed = models.DateTimeField(blank=True, null=True)

    @property
    def dir(self):
        return os.path.join(settings.SUPPORT_TICKET_DIR,
                            get_short_uuid(self.id))

    def create_dir(self):
        os.makedirs(self.dir, exist_ok=True)

    @property
    def artifacts(self):
        if not os.path.exists(self.dir):
            return []

        return os.listdir(self.dir)

    def __str__(self):
        return (f'Ticket #{self.short_id}: {self.subject[32:]}... '
                f'({self.reported_by})')

    @property
    def user_url(self):
        return (
            f'{settings.DEFAULT_HTTP_PROTOCOL}://{settings.DEFAULT_HOST}'
            f'/support/#{self.short_id}')

    @property
    def admin_url(self):
        return (
            f'{settings.DEFAULT_HTTP_PROTOCOL}://{settings.DEFAULT_HOST}'
            f'/admin/support/supportticket/{self.id}/change/')

    @property
    def artifacts_zip_url(self):
        return (
            f'{settings.DEFAULT_HTTP_PROTOCOL}://{settings.DEFAULT_HOST}'
            f'{reverse("SupportTicketDownload", args=[self.short_id])}')

    @property
    def autogenerated(self):
        """is ticket from a robot/automatic process, or is from a human"""
        if self.source in (TicketSource.ADMIN,
                           TicketSource.SUPPORT_PAGE,
                           TicketSource.EMAIL,
                           TicketSource.TABLE_REPORT_BUG):
            return False
        return True
