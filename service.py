PROFILE_FIELDS_HOOK = "profile.fields"


class FortniteService:
    def __init__(self, module):
        self.module = module

    def register_hooks(self):
        self.module.register_hook_provider(PROFILE_FIELDS_HOOK, self.build_profile_fields)

    def unregister_hooks(self):
        self.module.unregister_hook_provider(PROFILE_FIELDS_HOOK)

    def build_profile_fields(self, ctx, member, user_data, server_data):
        account_id = user_data.get("fortnite")
        if not account_id:
            return []

        nickname = self.module.get_fortnite_username_to_profile(account_id) or str(account_id)
        return [{"name": "Профиль Fortnite", "value": nickname}]
