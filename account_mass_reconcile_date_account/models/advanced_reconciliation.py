# -*- coding: utf-8 -*-
# © 2013-2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from openerp import api, models


class MassReconcileAdvancedTransactionRef(models.TransientModel):

    _name = 'mass.reconcile.advanced.date_account'
    _inherit = 'mass.reconcile.advanced'

    @api.multi
    def _skip_line(self, move_line):
        """
        When True is returned on some conditions, the credit move line
        will be skipped for reconciliation. Can be inherited to
        skip on some conditions. ie: ref or partner_id is empty.
        """
        return not (move_line.get('date') )

    @api.multi
    def _matchers(self, move_line):
        return (('date', move_line['date']),)

    @api.multi
    def _opposite_matchers(self, move_line):
        yield ('date', move_line['date'])
#        yield ('ref', ((move_line['ref'] or '').lower().strip(),
#                       move_line['name'].lower().strip()))