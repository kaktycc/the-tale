
import smart_imports

smart_imports.all()


class _BaseRequestTests(utils_testcase.TestCase):

    def setUp(self):
        super(_BaseRequestTests, self).setUp()

        game_logic.create_test_map()

        self.account_1 = self.accounts_factory.create_account()
        self.account_2 = self.accounts_factory.create_account()

        group_edit = utils_permissions.sync_group('edit achievement', ['achievements.edit_achievement'])

        group_edit.user_set.add(self.account_2._model)

        self.achievement_1 = prototypes.AchievementPrototype.create(group=relations.ACHIEVEMENT_GROUP.MONEY, type=relations.ACHIEVEMENT_TYPE.MONEY, barrier=0, points=10,
                                                                    caption='achievement_1', description='description_1', approved=True)
        self.achievement_2 = prototypes.AchievementPrototype.create(group=relations.ACHIEVEMENT_GROUP.MONEY, type=relations.ACHIEVEMENT_TYPE.MONEY, barrier=2, points=10,
                                                                    caption='achievement_2', description='description_2', approved=False)
        self.achievement_3 = prototypes.AchievementPrototype.create(group=relations.ACHIEVEMENT_GROUP.TIME, type=relations.ACHIEVEMENT_TYPE.TIME, barrier=3, points=10,
                                                                    caption='achievement_3', description='description_3', approved=True)

        self.collection_1 = collections_prototypes.CollectionPrototype.create(caption='collection_1', description='description_1', approved=True)
        self.kit_1 = collections_prototypes.KitPrototype.create(collection=self.collection_1, caption='kit_1', description='description_1', approved=True)
        self.item_1_1 = collections_prototypes.ItemPrototype.create(kit=self.kit_1, caption='item_1_1', text='text_1_1', approved=True)
        self.item_1_2 = collections_prototypes.ItemPrototype.create(kit=self.kit_1, caption='item_1_2', text='text_1_2', approved=True)

        self.account_achievements_1 = prototypes.AccountAchievementsPrototype.get_by_account_id(self.account_1.id)
        self.account_achievements_1.achievements.add_achievement(self.achievement_1)
        self.account_achievements_1.save()


class AchievementsIndexTests(_BaseRequestTests):

    def setUp(self):
        super(AchievementsIndexTests, self).setUp()
        self.test_url = utils_urls.url('accounts:achievements:')

    def test_anonymouse(self):
        self.check_html_ok(self.request_html(self.test_url), texts=[('pgf-last-achievements', 0),
                                                                    ('pgf-all-achievements', 0),
                                                                    ('pgf-no-last-achievements', 0)] + [group.text for group in relations.ACHIEVEMENT_GROUP.records])

    def test_logined_redirect(self):
        self.request_login(self.account_2.email)
        self.check_redirect(self.test_url, utils_urls.url('accounts:achievements:', account=self.account_2.id))

    def test_logined(self):
        self.request_login(self.account_2.email)
        test_url = utils_urls.url('accounts:achievements:', account=self.account_2.id)
        self.check_html_ok(self.request_html(test_url), texts=[('pgf-last-achievements', 1),
                                                               ('pgf-all-achievements', 1),
                                                               ('pgf-no-last-achievements', 1)] + [group.text for group in relations.ACHIEVEMENT_GROUP.records])

    def test_account_specified(self):
        self.request_login(self.account_1.email)
        test_url = utils_urls.url('accounts:achievements:', account=self.account_2.id)
        self.check_html_ok(self.request_html(test_url), texts=[('pgf-last-achievements', 1),
                                                               ('pgf-all-achievements', 1),
                                                               ('pgf-no-last-achievements', 1)] + [group.text for group in relations.ACHIEVEMENT_GROUP.records])

    def test_last_achievements(self):
        self.request_login(self.account_1.email)
        test_url = utils_urls.url('accounts:achievements:', account=self.account_1.id)
        self.check_html_ok(self.request_html(test_url), texts=[('pgf-last-achievements', 1),
                                                               self.achievement_1.caption,
                                                               ('pgf-all-achievements', 1),
                                                               ('pgf-no-last-achievements', 0)] + [group.text for group in relations.ACHIEVEMENT_GROUP.records])


class AchievementsGroupTests(_BaseRequestTests):

    def setUp(self):
        super(AchievementsGroupTests, self).setUp()
        self.test_url = utils_urls.url('accounts:achievements:group', relations.ACHIEVEMENT_GROUP.MONEY.slug)

    def test__for_no_user(self):
        self.check_html_ok(self.request_html(self.test_url), texts=[self.achievement_1.caption,
                                                                    relations.ACHIEVEMENT_GROUP.MONEY.text,
                                                                    (self.achievement_2.caption, 0),
                                                                    (self.achievement_3.caption, 0),
                                                                    ('pgf-owned', 0),
                                                                    ('pgf-group-progress', 0),
                                                                    ('pgf-add-achievement-button', 0),
                                                                    ('pgf-edit-achievement-button', 0)])

    def test_logined_redirect(self):
        self.request_login(self.account_1.email)
        self.check_redirect(self.test_url, utils_urls.url('accounts:achievements:group', relations.ACHIEVEMENT_GROUP.MONEY.slug, account=self.account_1.id))

    def test__for_normal_user(self):
        self.request_login(self.account_1.email)
        test_url = utils_urls.url('accounts:achievements:group', relations.ACHIEVEMENT_GROUP.MONEY.slug, account=self.account_1.id)
        self.check_html_ok(self.request_html(test_url), texts=[self.achievement_1.caption,
                                                               relations.ACHIEVEMENT_GROUP.MONEY.text,
                                                               (self.achievement_2.caption, 0),
                                                               (self.achievement_3.caption, 0),
                                                               'pgf-owned',
                                                               'pgf-group-progress',
                                                               ('pgf-add-achievement-button', 0),
                                                               ('pgf-edit-achievement-button', 0)])

    def test__for_editor(self):
        self.request_login(self.account_2.email)
        test_url = utils_urls.url('accounts:achievements:group', relations.ACHIEVEMENT_GROUP.MONEY.slug, account=self.account_2.id)
        self.check_html_ok(self.request_html(test_url), texts=[self.achievement_1.caption,
                                                               relations.ACHIEVEMENT_GROUP.MONEY.text,
                                                               self.achievement_2.caption,
                                                               ('pgf-owned', 0),
                                                               'pgf-group-progress',
                                                               (self.achievement_3.caption, 0),
                                                               'pgf-add-achievement-button',
                                                               'pgf-edit-achievement-button'])


class AchievementsNewTests(_BaseRequestTests):

    def setUp(self):
        super(AchievementsNewTests, self).setUp()
        self.test_url = utils_urls.url('accounts:achievements:new')

    def test_login_required(self):
        self.check_redirect(self.test_url, accounts_logic.login_page_url(self.test_url))

    def test_edit_rights_required(self):
        self.request_login(self.account_1.email)
        self.check_html_ok(self.request_html(self.test_url), texts=['accounts.achievements.no_edit_rights'])

    def test_success(self):
        self.request_login(self.account_2.email)
        self.check_html_ok(self.request_html(self.test_url), texts=[('accounts.achievements.no_edit_rights', 0)])


class AchievementsCreateTests(_BaseRequestTests):

    def setUp(self):
        super(AchievementsCreateTests, self).setUp()
        self.test_url = utils_urls.url('accounts:achievements:create')

    def get_post_data(self):
        return {'caption': 'caption_create',
                'description': 'description_create',
                'order': 666,
                'barrier': 777,
                'type': relations.ACHIEVEMENT_TYPE.DEATHS,
                'group': relations.ACHIEVEMENT_GROUP.DEATHS,
                'points': 20,
                'item_1': self.item_1_1.id,
                'item_2': '',
                'item_3': ''}

    def test_login_required(self):
        with self.check_not_changed(prototypes.AchievementPrototype._db_all().count):
            self.check_ajax_error(self.post_ajax_json(self.test_url, self.get_post_data()),
                                  'common.login_required')

    def test_edit_rights_required(self):
        self.request_login(self.account_1.email)
        with self.check_not_changed(prototypes.AchievementPrototype._db_all().count):
            self.check_ajax_error(self.post_ajax_json(self.test_url, self.get_post_data()),
                                  'accounts.achievements.no_edit_rights')

    def test_form_errors(self):
        self.request_login(self.account_2.email)
        with self.check_not_changed(prototypes.AchievementPrototype._db_all().count):
            self.check_ajax_error(self.post_ajax_json(self.test_url, {}),
                                  'accounts.achievements.create.form_errors')

    def test_success(self):
        self.request_login(self.account_2.email)
        with self.check_delta(prototypes.AchievementPrototype._db_all().count, 1):
            response = self.post_ajax_json(self.test_url, self.get_post_data())

        achievement = prototypes.AchievementPrototype._db_get_object(3)

        self.check_ajax_ok(response, data={'next_url': utils_urls.url('accounts:achievements:group', achievement.group.slug)})

        self.assertEqual(achievement.caption, 'caption_create')
        self.assertEqual(achievement.description, 'description_create')
        self.assertEqual(achievement.type, relations.ACHIEVEMENT_TYPE.DEATHS)
        self.assertEqual(achievement.group, relations.ACHIEVEMENT_GROUP.DEATHS)
        self.assertEqual(achievement.barrier, 777)
        self.assertEqual(achievement.points, 20)
        self.assertFalse(achievement.approved)
        self.assertEqual(achievement.item_1.id, self.item_1_1.id)
        self.assertEqual(achievement.item_2, None)
        self.assertEqual(achievement.item_3, None)


class AchievementsEditTests(_BaseRequestTests):

    def setUp(self):
        super(AchievementsEditTests, self).setUp()
        self.test_url = utils_urls.url('accounts:achievements:edit', self.achievement_1.id)

    def test_login_required(self):
        self.check_redirect(self.test_url, accounts_logic.login_page_url(self.test_url))

    def test_edit_rights_required(self):
        self.request_login(self.account_1.email)
        self.check_html_ok(self.request_html(self.test_url),
                           texts=(('accounts.achievements.no_edit_rights', 1)))

    def test_wrong_format(self):
        self.request_login(self.account_2.email)
        self.check_html_ok(self.request_html(utils_urls.url('accounts:achievements:edit', 'bla')),
                           texts=(('accounts.achievements.achievement.wrong_format', 1)))

    def test_success(self):
        self.request_login(self.account_2.email)
        self.check_html_ok(self.request_html(self.test_url), texts=[('pgf-error-page-message', 0)])


class AchievementsUpdateTests(_BaseRequestTests):

    def setUp(self):
        super(AchievementsUpdateTests, self).setUp()
        self.test_url = utils_urls.url('accounts:achievements:update', self.achievement_2.id)

    def get_post_data(self):
        return {'caption': 'caption_edited',
                'description': 'description_edited',
                'order': 666,
                'barrier': 777,
                'type': relations.ACHIEVEMENT_TYPE.DEATHS,
                'group': relations.ACHIEVEMENT_GROUP.DEATHS,
                'approved': True,
                'points': 6,
                'item_1': self.item_1_1.id,
                'item_2': self.item_1_2.id,
                'item_3': ''}

    def get_post_data__without_update(self):
        return {'caption': 'caption_edited',
                'description': 'description_edited',
                'order': 666,
                'barrier': self.achievement_2.barrier,
                'type': self.achievement_2.type,
                'group': relations.ACHIEVEMENT_GROUP.DEATHS,
                'approved': self.achievement_2.approved,
                'points': self.achievement_2.points,
                'item_1': '',
                'item_2': '',
                'item_3': ''}

    def test_login_required(self):
        with self.check_not_changed(prototypes.GiveAchievementTaskPrototype._db_all().count):
            self.check_ajax_error(self.post_ajax_json(self.test_url, self.get_post_data()), 'common.login_required')

    def test_edit_rights_required(self):
        self.request_login(self.account_1.email)
        with self.check_not_changed(prototypes.GiveAchievementTaskPrototype._db_all().count):
            self.check_ajax_error(self.post_ajax_json(self.test_url, self.get_post_data()),
                                  'accounts.achievements.no_edit_rights')

        self.achievement_1.reload()
        self.assertEqual(self.achievement_1.caption, 'achievement_1')
        self.assertEqual(self.achievement_1.description, 'description_1')

    def test_form_errors(self):
        self.request_login(self.account_2.email)
        with self.check_not_changed(prototypes.GiveAchievementTaskPrototype._db_all().count):
            self.check_ajax_error(self.post_ajax_json(self.test_url, {}),
                                  'accounts.achievements.update.form_errors')

        self.achievement_1.reload()
        self.assertEqual(self.achievement_1.caption, 'achievement_1')
        self.assertEqual(self.achievement_1.description, 'description_1')

    def test_success(self):
        self.request_login(self.account_2.email)
        with self.check_delta(prototypes.GiveAchievementTaskPrototype._db_all().count, 1):
            response = self.post_ajax_json(self.test_url, self.get_post_data())

        self.achievement_2.reload()

        self.check_ajax_ok(response, data={'next_url': utils_urls.url('accounts:achievements:group', self.achievement_2.group.slug)})

        self.assertEqual(self.achievement_2.caption, 'caption_edited')
        self.assertEqual(self.achievement_2.description, 'description_edited')
        self.assertEqual(self.achievement_2.type, relations.ACHIEVEMENT_TYPE.DEATHS)
        self.assertEqual(self.achievement_2.group, relations.ACHIEVEMENT_GROUP.DEATHS)
        self.assertEqual(self.achievement_2.barrier, 777)
        self.assertTrue(self.achievement_2.approved)
        self.assertEqual(self.achievement_2.points, 6)
        self.assertEqual(self.achievement_2.item_1.id, self.item_1_1.id)
        self.assertEqual(self.achievement_2.item_2.id, self.item_1_2.id)
        self.assertEqual(self.achievement_2.item_3, None)

    def test_success__not_changed(self):
        self.request_login(self.account_2.email)

        with self.check_not_changed(prototypes.GiveAchievementTaskPrototype._db_all().count):
            response = self.post_ajax_json(self.test_url, self.get_post_data__without_update())

        self.achievement_2.reload()

        self.check_ajax_ok(response, data={'next_url': utils_urls.url('accounts:achievements:group', self.achievement_2.group.slug)})

        self.assertEqual(self.achievement_2.caption, 'caption_edited')
        self.assertEqual(self.achievement_2.description, 'description_edited')
        self.assertEqual(self.achievement_2.type, relations.ACHIEVEMENT_TYPE.MONEY)
        self.assertEqual(self.achievement_2.group, relations.ACHIEVEMENT_GROUP.DEATHS)
        self.assertEqual(self.achievement_2.barrier, 2)
        self.assertFalse(self.achievement_2.approved)
        self.assertEqual(self.achievement_2.points, 10)

        self.assertEqual(self.achievement_2.item_1, None)
        self.assertEqual(self.achievement_2.item_2, None)
        self.assertEqual(self.achievement_2.item_3, None)
