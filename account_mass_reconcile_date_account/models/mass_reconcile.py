# -*- coding: utf-8 -*-
# © 2013-2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from openerp import api, models


class AccountMassReconcileMethod(models.Model):

    _inherit = 'account.mass.reconcile.method'

    @api.model
    def _get_all_rec_method(self):
        _super = super(AccountMassReconcileMethod, self)
        methods = _super._get_all_rec_method()
        methods += [
            ('mass.reconcile.advanced.date_account',
             'Advanced. Date reconciliation. Use with Caution'),
        ]
        return methods
