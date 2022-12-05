events = ["on_connect", "on_disconnect", "on_error", "on_gateway_error", "on_ready", "on_resumed", "on_shard_connect", "on_shard_disconnect", "on_shard_ready", "on_shard_resumed", "on_socket_event_type", "on_socket_raw_receive", "on_socket_raw_send", "on_guild_channel_delete", "on_guild_channel_create", "on_guild_channel_update", "on_guild_channel_pins_update", "on_private_channel_update", "on_private_channel_pins_update", "on_thread_create", "on_thread_join", "on_thread_member_join", "on_thread_member_remove", "on_thread_remove", "on_thread_update", "on_thread_delete", "on_raw_thread_member_remove", "on_raw_thread_update", "on_raw_thread_delete", "on_webhooks_update", "on_guild_join", "on_guild_remove", "on_guild_update", "on_guild_available", "on_guild_unavailable", "on_application_command_permissions_update", "on_automod_action_execution", "on_automod_rule_create", "on_automod_rule_update", "on_automod_rule_delete", "on_guild_emojis_update", "on_guild_integrations_update", "on_integration_create", "on_integration_update", "on_raw_integration_delete", "on_invite_create", "on_invite_delete", "on_member_join", "on_member_remove", "on_member_update", "on_raw_member_remove", "on_raw_member_update", "on_member_ban", "on_member_unban", "on_presence_update", "on_user_update", "on_guild_scheduled_event_create", "on_guild_scheduled_event_delete", "on_guild_scheduled_event_update", "on_guild_scheduled_event_subscribe", "on_guild_scheduled_event_unsubscribe", "on_raw_guild_scheduled_event_subscribe", "on_raw_guild_scheduled_event_unsubscribe", "on_stage_instance_create", "on_stage_instance_delete", "on_stage_instance_update", "on_guild_stickers_update", "on_guild_role_create", "on_guild_role_delete", "on_guild_role_update", "on_voice_state_update", "on_application_command", "on_application_command_autocomplete", "on_button_click", "on_dropdown", "on_interaction", "on_message_interaction", "on_modal_submit", "on_message", "on_message_delete", "on_message_edit", "on_bulk_message_delete", "on_raw_message_delete", "on_raw_message_edit", "on_raw_bulk_message_delete", "on_reaction_add", "on_reaction_remove", "on_reaction_clear", "on_reaction_clear_emoji", "on_raw_reaction_add", "on_raw_reaction_remove", "on_raw_reaction_clear", "on_raw_reaction_clear_emoji", "on_typing", "on_raw_typing", "on_command_error", "on_slash_command_error", "on_user_command_error", "on_message_command_error", "on_command", "on_slash_command", "on_user_command", "on_message_command", "on_command_completion", "on_slash_command_completion", "on_user_command_completion", "on_message_command_completion"]

for _ in events:
   __ = _.capitalize()
   with open(f"discordbot/cogs/listeners/{_}.py", "w") as f:
      f.write(f"""import disnake
from disnake.ext import commands

from utils.color import color

class {__}(commands.Cog):
      def __init__(self, bot: commands.Bot):
         self.bot = bot
         
      @commands.Cog.listener() 
      async def {_}(self):
         ...
                        """)