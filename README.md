For those who have the steam desktop authenticator enabled, or do not have an authenticator on their mobile device and you went somewhere to play). Run this project and it will send the access code to your steam account and reply only to your TG login.

Example secret mafile

{"shared_secret":"","serial_number":"","revocation_code":"", "uri":"otpauth://totp/Steam:?secret==Steam", "server_time":,"account_name":"", "token_gid":"", "identity_secret":"=", "secret_1":"","status":1, "device_id":"android:", "fully_enrolled":true,"Session":{"SteamID":, "AccessToken":"","SessionID":null}}

Need only shared_secret!


Change code
1. path_secret_maFile = './secret.maFile' path file
2. if user.username == 'UR LOGIN TG':
3. app = ApplicationBuilder().token("707********:AAEAH6kUvEl8txpTNv************** UR TOKEN TG BOT").build()
