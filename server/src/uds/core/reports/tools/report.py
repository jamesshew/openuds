# -*- coding: utf-8 -*-

#
# Copyright (c) 2015 Virtual Cable S.L.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#    * Neither the name of Virtual Cable S.L. nor the names of its contributors
#      may be used to endorse or promote products derived from this software
#      without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
.. moduleauthor:: Adolfo Gómez, dkmaster at dkmon dot com
'''
from __future__ import unicode_literals

from django.utils.translation import ugettext, ugettext_lazy as _
from uds.core.reports import stock

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, SubReport, Rect
from uds.core.reports.tools.geraldo_graphics import UDSImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.lib import colors

import logging

logger = logging.getLogger(__name__)

__updated__ = '2015-06-21'


class UDSGeraldoReport(Report):
    author = 'UDS Enterprise'
    title = 'UDS Report'

    print_if_empty = True
    page_size = A4
    margin_left = 0.5 * cm
    margin_top = 0.5 * cm
    margin_right = 0.5 * cm
    margin_bottom = 0.5 * cm

    class band_page_header(ReportBand):
        height = 1.8 * cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.5 * cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),

            SystemField(expression=_('Page %(page_number)d of %(page_count)d'), top=0.1 * cm,
                        width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            UDSImage(filename=stock.getStockImagePath(stock.LOGO), left=0.0 * cm, top=0.0 * cm, width=2.0 * cm, height=2.0 * cm),
        ]
        borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 0.5 * cm
        elements = [
            Label(text=_('Generated by UDS'), top=0.1 * cm),
            SystemField(expression=_('Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s'), top=0.1 * cm,
                        width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
        ]
        borders = {'top': True}

    @staticmethod
    def viewSize():
        return (
            UDSGeraldoReport.page_size - UDSGeraldoReport.mar
        )
