# `/usr/lib/libmis.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 701,808 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 38 (Size: 5840)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (21)

- `/usr/lib/libmis.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime (compatibility version 1.0.0, current version 340.0.14, weak)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libCoreEntitlements.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (24 classes, 3 protocols)

Classes: `BoxedMISProfile`, `MISAgentClient`, `MISDBManager`, `MISEntitlementsModel`, `MISLaunchWarningDatabase`, `MISLaunchWarningQueryResult`, `MISOnlineAuthEntry`, `MISOnlineAuthMigrationState`, `MISProfile`, `MISProfileDBClient`, `MISProfileModel`, `MISTeamIDEntryForUI`, `MISTrustedProfileEntry`, `MISTrustedTeamIDEntry`, `MobileIdentityService`, `OnlineAuthMetrics`, `SQLDB`, `_TtC3mis12SQLStatement`, `_TtC3mis13XPCConnection`, `_TtC3mis15LaunchWarningDB`, `_TtC3mis17LaunchWarningMark`, `_TtC3mis17LegacyUserTrustDB`, `_TtC3mis25LegacyUserTrustOperations`, `_TtC3mis29LaunchWarningClientOperations`

Protocols: `NSCopying`, `NSObject`, `OS_xpc_object`

## Strings (1,190)

```
v56@0:8q16q24q32q40@48
B24@0:8#16
v36@0:8@16@24B32
^v24@0:8@16
C16@0:8
v32@0:8@16@24
v32@0:8@16@?24
v16@?0^v8
@32@0:8:16@24
B24@0:8@\"Protocol\"16
v28@0:8@16i24
i32@0:8@16@24
@\"MISDBManager\"
i24@0:8@?16
B36@0:8@16i24^@28
^{CEQueryContext=}
@\"NSDictionary\"
v20@0:8B16
@40@0:8@16@24B32B36
v24@?0^v8@\"NSDictionary\"16
B60@0:8@16@24i32q36q44^@52
i24@0:8@16
B36@0:8q16i24^@28
B36@0:8@16B24@?28
B24@0:8@16
v16@?0@\"<OS_xpc_object>\"8
v16@0:8
v24@0:8@16
@\"NSMutableDictionary\"
@64@0:8@16@24@32@40C48C52C56C60
C
d16@0:8
@\"NSString\"16@0:8
i16@0:8
@16@0:8
@24@0:8@16
v20@0:8C16
B16@0:8
@36@0:8q16B24@28
^{_NSZone=}16@0:8
@32@0:8@16@24
Vv16@0:8
B32@0:8@16@24
@40@0:8:16@24@32
v20@0:8i16
Q16@0:8
@\"MISTrustedTeamIDEntry\"
B40@0:8@16@24^@32
B28@0:8i16^@20
i
?
@\"NSData\"
B
^{sqlite3=}
@\"MISProfileModel\"
B32@0:8@16^@24
q16@0:8
@\"NSDate\"
@24@0:8^@16
B16@?0@8
B44@0:8@16@24B32^@36
v28@0:8q16i24
@\"NSString\"
@28@0:8@16B24
d
@36@0:8@16I24^@28
@32@0:8@16^@24
@36@0:8I16@20^@28
B36@0:8B16@20^@28
v80@0:8q16q24q32q40q48q56q64q72
@24@0:8:16
B24@0:8:16
@\"NSArray\"
@32@0:8^{sqlite3_stmt=}16@24
#16@0:8
q
i40@0:8@16@?24@?32
i28@0:8@?16B24
Q24@0:8@16
@\"NSURL\"
B40@0:8q16@24^@32
i24@0:8^v16
@24@0:8^{_NSZone=}16
@60@0:8@16@24i32q36q44B52B56
v24@0:8q16
q24@0:8@16
^{CEQueryContext=}16@0:8
@\"NSObject<OS_dispatch_semaphore>\"
B32@0:8q16q24
@\"MISEntitlementsModel\"
@\"NSDictionary\"8@?0
path != NULL
1
@uuid
BEGIN TRANSACTION
MobileIdentityService
CREATE TABLE profiles ( uuid TEXT NOT NULL PRIMARY KEY, team_id TEXT NOT NULL, install_time TEXT DEFAULT CURRENT_TIMESTAMP, name TEXT NOT NULL, expires INTEGER, is_for_all_devices INTEGER, is_apple_internal INTEGER, is_local INTEGER, is_bet
/private/var/db/MobileIdentityData
adaea588-c074-4b87-b8ea-26cb685b3443
team
@team_id
SELECT uuid\nFROM profiles\nWHERE team_id = ?1 AND is_for_all_devices = 1
!
SELECT team_id, signature\nFROM sep_trusted_team_ids\nWHERE team_id = ?1
SELECT trusted_team_ids.team_id, signature\nFROM profiles\nLEFT JOIN trusted_team_ids\nON profiles.team_id = trusted_team_ids.team_id\nWHERE uuid = ?1
No code signature found.
SELECT cms_blob FROM xml_profiles_cache WHERE uuid = @uuid
SELECT COUNT(*) FROM %@
GetLocalLaunchWarningData
type
CREATE TABLE IF NOT EXISTS team_id_info ( team_id TEXT NOT NULL, team_name TEXT NOT NULL,  PRIMARY KEY (team_id) )
/Library/MobileDevice/ProvisioningProfiles
This provisioning profile is malformed.
begin transaction
resource added
logResourceError
bool
CREATE TABLE certificate_provisioning_cache ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, leaf_pk INTEGER NOT NULL, UNIQUE(uuid, leaf_pk), CONSTRAINT fk_certificate_leaf  FOREIGN KEY (leaf_pk)  REFERENCES certificates(pk)  ON 
09fcf192-750c-4a39-9a0e-cfe6faa82275
Name
SELECT cms_blob as blob FROM xml_profiles_cache
rollback transaction
SELECT 1\nFROM profiles\nWHERE uuid = ?1 AND is_local = 1
SELECT DISTINCT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE profiles.uuid = ?1
85255e8b-352b-4d58-8e09-81203580f434
@expires
SELECT value FROM settings WHERE name = ?1
app
2
WITH filteredProfileUUIDs(uuid) AS (%@) SELECT profiles.uuid, profiles.team_id, profiles.name, profiles.expires, profiles.is_for_all_devices, profiles.is_apple_internal, profiles.is_local, profiles.is_beta, profiles.is_der FROM filteredProf
SELECT 1\nFROM banned_cdhashes\nWHERE cdhash = ?1
lwid
SELECT uuid\nFROM profiles\nWHERE team_id = ?1
SkipProfileIdentifierPolicy
B8@?0
Ping
HasAuxiliarySignature
91c408d9-0fbe-44c4-aa74-37c7f734e159
d1576fca-f736-46eb-8ac5-d5b4db7503ac
TeamIdentifier
Platform
UniversalFileOffset
ALTER TABLE profiles ADD COLUMN is_der INTEGER DEFAULT (0)
10
A signed resource has been added, modified, or deleted.
@predicate
CopySingle
ValidateSignatureOnly
SignerType
ON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = 0,\n    last_success_monotonic_time = -1,\n    last_success_reset_count = -1
mis
profile_cms_blob
CdHash
current_rtc_reset_count
com.apple.mis.onlineauth.indeterminate_detected
@is_der
INSERT INTO banned_cdhashes (cdhash)\nVALUES (?1)\nON CONFLICT DO NOTHING
ReportIndeterminateSoon
tvOS
univ
SELECT 1\nFROM online_auth\nWHERE\n    (uuid = ?1 AND cdHash = ?2 AND is_rejected = 1) OR\n    (uuid = ?1 AND is_rejected = 1 AND is_rejected_by_whole_profile = 1)
MISTeamIDEntryForUI(%@, %@, %d, %d)
OnlineCheckType
6
LaunchWarning.db
MigrationPhase
CreationDate
lastSuccessMonotonicTime
9
profile_is_for_all_devices
%@.%@
, user_override, pk FROM launch_warning WHERE cdhash_type = ?1 AND cdhash = ?2
fbe71da1-0834-4d49-9b41-d3fa7f9e4d4f
@is_beta
CREATE TABLE xml_profiles_cache ( uuid TEXT NOT NULL PRIMARY KEY, cms_blob BLOB NOT NULL, CONSTRAINT fk_xml_profile_cache_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )
number%@
Trust
AuthListBannedUpps.plist
NULL
cdha
bool%@
MIS XPC failure: 
?2 > last_success_monotonic_time + (grace_period
8ae887e0-8d30-448a-b10d-0312c5b71f05
deviceUDID
CREATE TABLE IF NOT EXISTS trusted_team_ids ( team_id TEXT PRIMARY KEY, signature BLOB )
The executable contains an invalid signature.
The executable was signed with invalid entitlements.
iOS
Encountered XPC_TYPE_ERROR: 
?1 != last_success_reset_count OR 
This provisioning profile has expired.
DER-Encoded-Profile
3
hoursSinceLastSuccess
DELETE FROM online_auth WHERE cdhash = ?1
This provisioning profile does not have a valid signature (or it has a valid, but untrusted signature).
The provisioning profile's App Audience is not suitable for this device.
INSERT INTO xml_profiles_cache VALUES (@uuid, @cms_blob)
lastSuccessResetCount
SigningID
i16@?0^{__SecPolicy=}8
11
UPDATE online_auth SET last_success_monotonic_time = last_success_monotonic_time + ?1 
The signature was not valid.
INSERT INTO profiles VALUES (@uuid, @team_id, NULL, @name, @expires, @is_for_all_devices, @is_apple_internal, @is_local, @is_beta, @cms_blob, @is_der)
pk
INSERT INTO legacy_profile_grace_periods (uuid, grace_period)\nVALUES (?1, ?2)\nON CONFLICT(uuid) DO UPDATE SET grace_period = ?2
SELECT DISTINCT signing_identity FROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nLEFT JOIN trusted_team_ids ON trusted_team_ids.team_id = profiles.team_id\nWHERE trusted_team_ids.team_id IS NOT NULL
3d98340d-a43f-4263-8645-51937b4bffd0
SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth
OSX
@name
setDatabasePermissionsInternal
UseSoftwareSigningCert
SELECT uuid FROM certificate_provisioning_cache JOIN certificates ON certificates.pk = leaf_pk WHERE certificates.leaf = @cert
b9e61602-b1a2-4b73-b0f9-54cc3fff4244
com.apple.mis.warning
@cms_blob
security.codesigning.config
TeamName
visionOS
SELECT DISTINCT profiles.uuid\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1
mis.LaunchWarningDB
%y%m%d%H%M%SZ
SELECT uuid FROM profiles WHERE uuid = @uuid
*
Running this application requires Developer Mode to be enabled.
SELECT\n    DISTINCT profiles.team_id,\n    team_id_info.team_name,\n    trusted_team_ids.team_id IS NOT NULL,\n    trusted_team_ids.signature IS NOT NULL\nFROM profiles\nLEFT JOIN trusted_team_ids ON trusted_team_ids.team_id = profiles.tea
minutesSinceBoot
%F
DeveloperCertificates
@p%u
ExpectedHash
LogResourceErrors
string
The identity used to sign the executable is no longer valid.
beta-reports-active
Internal
AuxiliarySignature
@wildcard
AllowLaunchWarnings
invalid
Unknown reply type: 
profile_team_id
CREATE TABLE IF NOT EXISTS online_auth_migration_state (  id INTEGER NOT NULL PRIMARY KEY CHECK (id = 1),  last_migration_monotonic_time INTEGER NOT NULL,  last_migration_sources_bitmask INTEGER NOT NULL,  last_seen_os_build TEXT NOT NULL )
Attempted to modify an immutable provisioning profile.
MISOnlineAuthEntry(%@, %@, gracePeriod: %i, lastSuccessMonotonicTime: %lli, lastSuccessResetCount: %lli, isRejected: %i, isRejectedByWholeProfile: %i)
Predicates
SELECT COUNT(*) FROM profiles
An unexpected error was encountered (0x%X)
PRAGMA journal_mode = WAL
LaunchWarningsOnInstall
UPDATE profiles SET is_beta = 1 WHERE uuid = @uuid
AddRTCResetCountOffset
An error occured while accessing the profile database.
@leaf_pk
CREATE TABLE IF NOT EXISTS sep_trusted_team_ids (\n    team_id TEXT PRIMARY KEY,\n    signature BLOB NOT NULL\n)
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 1, ?3)\nON CONFLICT(uui
97b12f3c-1687-4883-93e0-f3ac1292a654
PPQCheck
CopyAll
LocalProvision
droppedProfileUninstalled
INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, -1, 0, ?1)\nON CONFLICT(id) DO UPDATE SET last_seen_os_build = ?1
INSERT INTO trusted_team_ids (team_id, signature)\nVALUES (?1, ?2)\nON CONFLICT(team_id) DO UPDATE SET signature = ?2
profile_is_apple_internal
SELECT cms_blob FROM profiles WHERE is_der = 0
DELETE FROM trusted_team_ids WHERE team_id = ?1
AuthListBannedCdHashes.plist
UnauthoritativeLaunch
CREATE TABLE certificates ( pk INTEGER PRIMARY KEY AUTOINCREMENT, leaf BLOB UNIQUE NOT NULL)
CREATE UNIQUE INDEX certificate_leaf_index ON certificates (leaf)
SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth\nWHERE 
SELECT COUNT(*)\nFROM online_auth\nWHERE uuid =  ?1 AND is_rejected = 1 AND is_rejected_by_whole_profile = 1
cbfd2102-86b1-4895-990f-dbaece4c63f2
B16@?0r^{MISMatchedProfile=^{__CFString}^{__CFString}BBBBB@}8
CDHash
ProfileID
SELECT COUNT(1)\nFROM profiles\nWHERE team_id = ?1
) AND is_rejected = 0
InternalBuild
begin immediate transaction
v8@?0
mis.MISOnlineAuthMigrationState
init()
DELETE FROM profiles WHERE uuid = @uuid
c7854afa-6894-4864-8d3c-15f6ccc6728d
The provisioning profile requires online authorization.
%@_%s
ReleaseType
@signing_identity
The application's signature is valid but it does not match the expected hash.
v16@?0@\"NSObject<OS_xpc_object>\"8
UPDATE online_auth SET grace_period = ?2\nWHERE uuid = ?1
An unknown error has occurred.
MISTrustedTeamIDEntry(%@, %@)
SigningTime
SELECT DISTINCT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE team_id = ?1
ProvisioningCDHashes
IsNativeForPlatform
lwov
Unable to allocate memory.
An error occured while communicating with the agent.
com.apple.mis
@is_for_all_devices
%@-wal
INSERT OR REPLACE INTO settings (name, value) VALUES (?1, ?2)
LaunchWarningData
SELECT last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\nFROM online_auth_migration_state\nWHERE id = 1
The application does not have a valid signature.
ExpirationDate
db_utils.m
amfi_emulate_device_udid
CREATE TABLE IF NOT EXISTS banned_cdhashes (  cdhash BLOB NOT NULL )
hoursSinceLastMigration
DELETE FROM online_auth WHERE uuid = ?1 AND cdhash = ?2
No team ID found for profile UUID: 
profile_expires
resource modified
MISTrustedProfileEntry(%@, %@, %@)
SELECT team_id, signature\nFROM trusted_team_ids\nWHERE team_id = ?1
294be08b-487f-4020-a986-011dbc7a4fc8
Invalid arguments or option combination.
%02x
INSERT INTO certificate_provisioning_cache VALUES (NULL, @uuid, @leaf_pk)
profile_is_local
profile_is_beta
NoExecute
ON CONFLICT(uuid, cdhash) DO NOTHING
AppAudience
Offset
INSERT OR IGNORE INTO entitlements_provisioning_cache VALUES (NULL, @uuid, @predicate, @wildcard)
PRAGMA foreign_keys = ON
B40@?0^{__CFString=}8^{__CFString=}16B24B28B32B36
MessageType
Version
DetachedSignature
Attempted to install a Beta profile over lockdown connection.
cdHash
, profileUUID = 
WHERE cdhash = ?2
8c9a3b2d-c2a3-47f5-b7fc-ae7bcdc79cbf
AGP.plist
profileUUID
SignerCertificate
(%lu,@p%lu)
 from misagent when migrating data
65033b0b-6071-4ad2-8509-f8e087b74d5b
8f327bd3-89e8-46e5-bcf5-72a260f6dd36
The application's signature is valid, but a provisioning profile can not be found that matches this version.
DELETE FROM settings WHERE name = ?1
ValidatedByUniversalProfile
4
WITH predicates(idx, predicate) AS (VALUES %@), filteredProfileUUIDs(uuid) AS (%@) SELECT * FROM (SELECT profiles.uuid, profiles.team_id, profiles.name, profiles.expires, profiles.is_for_all_devices, profiles.is_apple_internal, profiles.is_
INSERT OR IGNORE INTO signing_identities VALUES (NULL, @uuid, @signing_identity)
s
true
CREATE UNIQUE INDEX entitlements_cache_index ON entitlements_provisioning_cache (uuid, predicate)
3d2a1eea-d1f8-42ab-af5a-545ce51054a7
Install
ProfileUUID
chlw
CREATE TABLE IF NOT EXISTS legacy_profile_grace_periods (  uuid TEXT NOT NULL PRIMARY KEY,  grace_period INT NOT NULL,  CONSTRAINT fk_legacy_profile_grace_period_uuid    FOREIGN KEY (uuid)    REFERENCES profiles(uuid)    ON DELETE CASCADE )
, user_override, pk FROM launch_warning WHERE pk = ?1
 from misagent adding monotonic time offset 
SELECT DISTINCT team_id\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1
UserTrust.db
SELECT pk FROM certificates WHERE leaf = @cert
UniqueDeviceID
INSERT OR IGNORE INTO certificates VALUES (NULL, @cert)
ROLLBACK TRANSACTION
apppath
SELECT profiles.team_id, profiles.cms_blob, profiles.uuid FROM profiles
SELECT team_id\nFROM profiles\nWHERE uuid = ?1
The cdhash is not in the trust cache.
v32@?0@8Q16^B24
cdhash_type, cdhash, reason, flags, timestamp, kb_url
IsVirtualDevice
warndata
end transaction
isRejected
CREATE TABLE IF NOT EXISTS signing_identities ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, signing_identity TEXT NOT NULL, UNIQUE(uuid, signing_identity), CONSTRAINT fk_signing_identity_profile_uuid  FOREIGN KEY (uuid)  REFER
1.2.840.113635.100.12.19
@is_local
Profile
false
cdvr
e09bc661-bd16-4be0-9800-5235640f3392
Rejections.plist
CREATE TABLE IF NOT EXISTS settings ( name TEXT, value TEXT, PRIMARY KEY (name) )
DELETE FROM trusted_team_ids\nWHERE EXISTS (\n    SELECT 1\n    FROM profiles\n    WHERE uuid = ?1 AND profiles.team_id = trusted_team_ids.team_id\n)
2f319679-66b9-44cf-9cf0-723471de0db9
The user did not explicitly trust the provisioning profile.
This provisioning profile cannot be installed on this device.
SELECT cms_blob FROM profiles WHERE uuid = @uuid
9c0fab7e-93cf-4d83-8340-9ea33b5846cc
TrustCacheOnly
v24@?0^{sqlite3_stmt=}8@\"NSDictionary\"16
blob
MIS XPC unexpected response with no data.
legacy_profile_grace_periods
RespectUppTrustAndAuthorization
CREATE TABLE entitlements_provisioning_cache ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, predicate TEXT NOT NULL, wildcard INTEGER NOT NULL, UNIQUE(uuid, predicate), CONSTRAINT fk_predicate_profile_uuid  FOREIGN KEY (uuid)  
SELECT team_id, signature FROM trusted_team_ids
SELECT team_id, signature\nFROM trusted_team_ids
isRejectedByWholeProfile
AuthoritativeLaunch
ProvisionsAllDevices
databaseSchemaVersion
B16@?0^v8
INSERT INTO team_id_info VALUES (@team_id, @team_name)
mobile
gracePeriod
Remove
CopyMatching
SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth\nWHERE uuid = ?1 AND cdhash = ?2
ForceXML
OnlineAuthorization
SELECT uuid, team_id, name, expires, is_for_all_devices, is_apple_internal, is_local, is_beta FROM profiles
resource deleted
 from misagent adding RTC reset count offset 
AppleMobileFileIntegrity
%@%@%lld
INSERT OR IGNORE INTO entitlements_provisioning_cache (uuid, predicate, wildcard) VALUES (?1, ?2, 1)
mis.LegacyUserTrustDB
current_monotonic_time
https://support.apple.com/116947
SELECT grace_period FROM legacy_profile_grace_periods WHERE uuid = ?1
243LU875E5
%@-shm
profileCountOnDevice
d9d5fa63-7084-4346-bada-96e463ad1771
The requested profile does not exist (it may have been removed).
Cert
SELECT uuid, cms_blob FROM profiles WHERE is_der = 0 AND (is_for_all_devices = 1 OR is_local = 1)
4a20c45a-2a99-4ad8-bdd2-c7ab4b0c1a8d
ProvisionedDevices
v16@?0^{sqlite3_stmt=}8
sgnt
v16@?0@\"NSString\"8
CREATE TABLE IF NOT EXISTS launch_warning (\n    pk INTEGER PRIMARY KEY AUTOINCREMENT,\n    cdhash_type INTEGER,\n    cdhash BLOB NOT NULL,\n    reason INTEGER,\n    flags INTEGER,\n    user_override BOOLEAN,\n    timestamp INTEGER,\n    UN
CREATE TABLE IF NOT EXISTS user_trusted_profiles (\n    uuid TEXT NOT NULL PRIMARY KEY,\n    team_id TEXT,\n    CONSTRAINT fk_team_id\n        FOREIGN KEY (team_id)\n        REFERENCES sep_trusted_team_ids(team_id)\n        ON DELETE CASCAD
Profile Signing V2
HonorBlocklist
application-identifier
last_migration_sources_bitmask
UserTrustedUpps.plist
INSERT INTO team_id_info VALUES (@team_id, @team_name) ON CONFLICT DO NOTHING
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
1.2.840.113635.100.6.2.17
Entitlements
Migrate
SELECT uuid, grace_period FROM legacy_profile_grace_periods
Payload
SELECT uuid FROM profiles
AllowAdHocSigning
ValidatedByLocalProfile
8
SELECT team_id FROM profiles WHERE uuid = ?1
The provisioning profile is banned.
last_seen_os_build
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)\nON CONFLICT(u
v32@?0@8@16^B24
v32@?0@\"NSString\"8Q16^B24
SELECT DISTINCT signing_identity FROM signing_identities
Attempting to trust team ID, but no installed profiles have that team ID
ALTER TABLE launch_warning ADD COLUMN kb_url TEXT DEFAULT NULL
SELECT 1\nFROM banned_profile_uuids\nWHERE uuid = ?1
48988f8b-9b77-4165-8eb1-038a0745dc87
Attempted to install a Beta profile without the proper entitlement.
UUID
profile_uuid
SigningFuse
There was an error communicating with your device.
d
com.apple.online-auth-agent.xpc
mis.db
com.apple.misagent
@cert
@is_apple_internal
cdht
A file operation failed.
%@%@%@
ckty
ovrr
SELECT uuid\nFROM user_trusted_profiles
number
SELECT xml_profiles_cache.uuid, xml_profiles_cache.cms_blob FROM xml_profiles_cache LEFT JOIN profiles ON profiles.uuid = xml_profiles_cache.uuid WHERE profiles.is_for_all_devices = 1 OR profiles.is_local = 1
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?3, ?4, ?5, ?1, ?2, 0, 0)\nON CONFLICT(uui
SELECT 1\nFROM profiles\nWHERE uuid = ?1 AND is_for_all_devices = 1
xrOS
ValidatedByProfile
CREATE TABLE IF NOT EXISTS banned_profile_uuids (  uuid TEXT NOT NULL )
bee84af7-d2ca-44e9-992b-54db447d20fc
1cf29dc4-4f08-457d-b9a7-512c89f0e142
ApplicationIdentifierPrefix
OnlineAuthorizationOnAllMatchingProfiles
) * 24 * 60 * 60
2bd82cb4-9549-4f99-b578-506b4a05b00c
cdhd
,
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 0, 0)\n
SELECT 1 FROM online_auth WHERE 
auth
last_migration_monotonic_time
com.apple.mis.onlineauth.migration_completed
profile_name
B24@?0^{sqlite3_stmt=}8@\"NSDictionary\"16
7
lastMigrationSource
INSERT INTO banned_profile_uuids (uuid)\nVALUES (?1)\nON CONFLICT DO NOTHING
2006-05-31
Status
A valid provisioning profile for this executable was not found.
watchOS
COMMIT TRANSACTION
Got error from misagent when setting trust: error = 
INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, ?1, ?2, \"\")\nON CONFLICT(id) DO UPDATE SET\n    last_migration_monotonic_time = ?1,\n    l
DELETE FROM team_id_info WHERE team_id = ?1
This provisioning profile is unsupported.
AppleInternalProfile
LaunchWarnings
%Y%m%d%H%M%SZ
The maximum number of apps for free development profiles has been reached.
UPDATE trusted_team_ids SET signature = NULL WHERE team_id = ?1
v24@?0@\"NSString\"8@\"NSData\"16
UPDATE online_auth SET last_success_reset_count = last_success_reset_count + ?1 
v16@?0^{__CFString=}8
locl
resu
@totalPredicates
AddMonotonicTimeOffset
TimeToLive
relaxProfileExpiry-%@
uuid
SELECT uuid, predicate FROM entitlements_provisioning_cache WHERE predicate LIKE 'string%' || x'1f' || '*' AND wildcard = 1
online_auth_entries
SELECT DISTINCT team_id FROM profiles
TeamID
SignatureVersion
Indeterminates.plist
5
CREATE TABLE IF NOT EXISTS online_auth (  uuid TEXT NOT NULL,  cdhash BLOB NOT NULL,  grace_period INT NOT NULL,  last_success_monotonic_time INT NOT NULL,  last_success_reset_count INT NOT NULL,  is_rejected INT NOT NULL DEFAULT (0),  is_r
Rejected by policy.
MainExecutablePath
@team_name
SELECT profiles.uuid, trusted_team_ids.team_id, signature\nFROM trusted_team_ids\nLEFT JOIN profiles\nON trusted_team_ids.team_id = profiles.team_id
The code signature version is no longer supported.
Error setting online auth migration state: %{public}@
Bundle has local launch warning data: %@
Found in cert cache, but cert type is CertTypeError (this should not happen).
MISDataMigrate error: %{public}@
validation failed because of missing DER entitlements
unable to allocate profiles array
Couldn't insert into signing identities: %s
Couldn't create the online auth migration state table: %s
Error getting all signing identities: %{public}@
Using emulated device UDID: %{public}@\n
Payload is not an array: %{public}s
MISQL: performing database migration 7 -> 8
unrecognized status %d from codesigning library
Not validly signed for app provisioning (type: %ld).
Could not extract signer: 0x%x
Got bundle for %@ -> %@
Failure creating profile cache key. This shouldn't happen.
Error getting profile UUIDs for team ID %{public}s: %{public}@
Couldn't get signing identity for %@
Query canceled
Could not extract signing time: 0x%x
Could not copy code signature (error 0x%x).
Encountered record with %ld != 4 entries: %@
unexpected event in handler for referenced item service\n
Error searching for zero length signatures: %s
Error getting trusted profile UUIDs: %{public}@
Failure creating profile cache key.
Database failed to initialize.
Profile row is not an array: '%{public}s'
Failed to create list of provisioning profiles
Skipping a profile %@
Couldn't create the online auth table: %s
Couldn't fetch single asterisk wildcard predicates: %s
Error recording indeterminate entry %{public}s, %{public}s, %{bool}d
Blocking bundle with outstanding launch warning: %@
SecTrustSetVerifyDate failed: %d
MISQL: performing database migration 1 -> 2
Couldn't add is_der to the profiles table: %s
cdhash is nil in database
misagent connection error: %{public}s
misagent connection error: %{public}s\n
Found local launch warning entry: %llu
Error checking if cdHash %{public}s is banned: %{public}@
Error deleting online auth entry %{public}s
unable to open file to update permissions: %d, %s
Online authorization rejected (%#llx), %@, %@
Error getting all team IDs %{public}@
SQL error '%{public}s' (%1d)
Caller specified both unauthoritative and authoritative launch modes.
Skipping universal/local profile with NULL UUID.
Encountered NULL record!
MISAppAprovalState failed to check kMISValidationOptionHonorBlocklist option.
AppleMobileFileIntegrity user client call failed: 0x%x
Error getting online auth entry %{public}s, %{public}s
Error deleting online auth entry %{public}s, %{public}s
MISQL: performing database migration 3 -> 4
validation would have failed due to missing DER entitlements
Could not create XPC message for checkLaunchWarning
Keep going %@
Invalid profile iteration outcome?
Couldn't create entitlements index: %s
Couldn't create the xml profiles table: %s
error installing profile: %{public}s\n
%@ was picked for validation
Overriding expiry for profile %{public}@ with timestamp %f
validation failed because of missing trust and/or authorization (0x%x)
Provisioning profile '%@' is banned.
MISQL: null version, potential erase or upgrade
TestFlight platform policy failed, the profile did not include the expected platform %@
Error getting profile UUIDs with signing identity %{public}s: %{public}@
Error counting cdhashes rejected by profile %{public}s
error getting installed profiles: %{public}s\n
Bundle: %@
Couldn't create the banned cdhashes table: %s
misagent successfully added monotonic time offset %ld to %{public}s
Ignoring unenforced App Audience: %{public}@ from profile %{public}@
error removing profile: %{public}s\n
validation failed because of failing online authorization (%d)
Universal/Local Provisioning Profile '%@' is not viable for validation.
Couldn't create certificates table: %s
Couldn't create entitlements provisioning cache: %s
Encountered a non-array value for 'Platforms'.
sysctl security.codesigning.config failed with error code: %d global error: %d
Error adding trust for profile UUID %@ with signature %@: %@
Authoritative
Local Profile '%@' entitlement match list is not a dictionary, but '%@'.
Online authorization ambiguous: %@, %@
Error setting grace period for %{public}s, %d
Blob data too small
error getting profile '%{public}s': %{public}s
DER policy skipped as we're not validating a main executable
invalid kMISValidationOptionUniversalFileOffset %lld
Unable to create code object (%d) for: %{public}s
Error fetching schema version
Checking %{public}@ App Audience, %d, %d
Critical SQLite error, could not checkpoint
Migrating team ID info: Unable to create profile for %@
Encountered a provisioning profile that does not provision the current platform.
Step error (%d) on query: %{public}@
MISAppAprovalState failed to check kMISAppApprovalStateReportIndeterminateSoon option.
Performing online authorization.
Error getting all profile UUIDs %{public}@
Error getting team IDs with signing identity %{public}s: %{public}@
Profile '%@' has a rejected app.
Accepting Universal/Local Provisioning Profile '%@'.
Encountered record of wrong size (%ld) when checking trust and authorization
Error checking if profile is for local provisioning %{public}s: %{public}@
Error getting auxiliary signature for team ID %{public}s: %{public}@
error getting profile '%{public}s' from fd
error processing kMISValidationOptionUniversalFileOffset (invalid type?), error 0x%x
Encountered record with no UUID or Team ID: %@
Error getting user trust for profile UUID %{public}s: %{public}@
Signing identity %{public}s has more than one team IDs: %{public}s. This will cause issues with user trust.
Entry in trusted_team_ids exists without associated profile: %{public}s
Profile record creation failed, bailing out!
Migration: Couldn't create SecCertificate for %@
Invalid reason in database: %lld
Profile %@ failed to validate entitlements
Checking warning state for bundle: %s
Setting user override: %{public}s to %{bool}d
Error setting last seen OS build: %{public}@
Error parsing profile payload: %@
Denying profile %{public}@ due to %{public}@ App Audience
Could not validate certificate: 0x%x
SecTrustCreateWithCertificates failed: %d
Online authorization succeeded: %@, %@
Error getting trusted team IDs: %{public}@
unexpected error with online-auth-agent connection\n
Couldn't create profiles table: %s
MISProfileGetTypeID is not supported, the results this function returns is wrong and should not be relied on
%{public}s: unexpected object type processing %{public}s errors
received unhandled event from misagent: %{public}s\n
No online authorization (%#llx): %@, %@
cdHash (%p) or matchedProfileIDs (%p) NULL in checkTrustAndAuthorization
MISQL: performing database migration 5 -> 6
Unable to get best cdhash data: %{public}s
Error migrating user trust: %{public}@
Local Profile '%@' has non-matching application-identifier.
appApprovalState returned unknown state %ld!
MISQL: performing database migration 8 -> 9
Error getting trusted signing identities: %{public}@
Could not create signer type number?
Skipping a profile because of error %#x.\n
Auth agent contact failure (entitlement status %lld)
Couldn't fetch trusted team ID info: %s
%{public}s: %{public}s
got NULL when querying UDID
Failure to convert onlineCheckType. (This should not happen.)
Error checking for launch warning: %@, %@
Couldn't fetch trusted signing identities from profiles: %s
error, could not lookup %s service
misagent successfully migrated data
Error getting teams for trust UI: %{public}@
Error checking for indeterminates: %lld, %lld, %{public}s, %{public}s, %{public}@
cdHash is NULL after successful validation? (This should not happen.)
UPP is ready, passing through.
Couldn't fetch trusted signing identities from xml_profiles_cache: %s
Unable to get full cdhash information for: %{public}s
IndeterminateTelemetry: error fetching indeterminates: %{public}@
Error checking for indeterminates: %lld, %lld, %{public}s, %{public}s, %@
Error checking if profileUUID %{public}s is banned: %{public}@
unable to set filesystem permissions on db: %d, %s
First certificate is NULL (this should not happen).
Could not copy signature: 0x%x
misagent successfully added RTC reset count offset %ld to %{public}s
Unable to create signing info (%d) for: %{public}s
Encountered a non-boolean value for 'PPQCheck'.
Couldn't create the legacy profile grace periods table: %s
Error getting online auth migration state: %{public}@
unable to check filesystem permissions on db: %d, %s
Failure setting detached signature: %d
There is no leaf cert (this should not happen).
Couldn't update is_beta column: %s
error getting unauthoritative profile list: %{public}s\n
Could not extract cdhash: 0x%x
Invalid platform: %du
Couldn't create the team ID info table: %s
MISQL: performing database migration 10 -> 11
MISValidateUPP: weird answer 0x%llx encountered.
Skipping profile '%@' because it has no entitlement match list?
Migration: Unable to create profile for %@
Error getting online auth entries: %{public}@
Could not decode CMS message.
Invalid entitlements in a provisioning profile
Failure creating profile payload data: %@
This function is not supported, and does not behave as you expect. Use MISProfileValidateSignature.
Unable to table row count for %{public}@: %d
Prepare error (%d) on query: %{public}@
Switched to checking executable url: %s
Received unhandled event from misagent: %{public}s
Profile row has no (or malformed) UUID: '%{public}s'
New bundle has outstanding launch warning: %@
Authorization still pending: %@, %@
Unable to open AppleMobileFileIntegrity user client: 0x%x
Is main executable: %i
Couldn't create certificates index: %s
MISQL: performing database migration 2 -> 3
Setting override for unknown bundle: %{public}s
Couldn't create SecCertificate for %@
Error reading local launch warning data: %@, %@
Error checking for launch warning mark: %@, %@
MISQL: performing database migration 4 -> 5
Migration: Unable to get signing identity from %@
MISQL: performing database migration 9 -> 10
Looking up local launch warning data for bundle: %{public}s
Couldn't create the trusted team IDs table: %s
Error getting user trust for team ID %{public}s: %{public}@
SecTrustEvaluateWithError failed: %{public}@
MISQL: performing database migration 6 -> 7
Checking warning state for url: %s
Successfully set trust: profileUUID = %{public}s, teamID = %{public}s, signature = %{public}s, trust = %{bool}d
App audience %{public}@ from profile %{public}@ not matched
Could not create XPC message for setBlacklistOverride
Couldn't insert new types for single asterisk wildcard predicates: %s
DB being loaded from %{public}@
Ours: %@
Using Provisioning Profile '%@'.
Couldn't create the signing identities table: %s
Couldn't create the banned profile UUIDs table: %s
Performing warning lookup for cdhash type: %u
Error checking if auxiliary signature is supported for team ID %{public}s: %{public}@
Error getting legacy profile grace period for %{public}s
error processing kMISValidationOptionDetachedSignature (invalid type?), error 0x%x
Encountered nil UUID when checking trust and authorization
Unable to find AppleMobileFileIntegrity service.
Invalid UTF8 string in predicate
Error getting team ID for profile UUID %{public}s: %{public}@
Error getting signing identities with team ID %{public}s: %{public}@
Error getting legacy profile grace periods: %{public}@
Couldn't insert team ID info: %s
Error getting signing identities with profile %{public}s: %{public}@
Trying to release a CE managed context
got non-string when querying UDID
MISPing error: %{public}@
Unable to get best cdhash digest algorithm: %{public}s
Error checking for rejection: %{public}s %{public}s %{public}@
Encountered a null or non-string platform identifier.
Failure creating static code: %d
TestFlight platform policy failed, the profile did not include the expected platform %@, this would have been a critical failure on a customer build
Error getting auxiliary signature for %{public}s from legacy user trust DB: %{public}@
Encountered nil record when checking trust and authorization
Wrong profile row count %ld != expected %ld
Signers array is empty (this should not happen).
CDHash is banned
Couldn't create certificates provisioning cache: %s
Couldn't replace signature with nil: %s
Error checking if profile provisions all devices %{public}s: %{public}@
CE context should not be accelerated
Error opening DB: %d
Finalize error (%d) on query: %{public}@
Error removing trust for profile UUID %@: %@
_TtC3mis15LaunchWarningDB
MISProfileDBClient
_TtC3mis13XPCConnection
OS_xpc_object
mis1
MobileIdentityService
BoxedMISProfile
NSCopying
mis
MISAgentClient
OnlineAuthMetrics
SQLDB
_TtC3mis17LegacyUserTrustDB
NSObject
MISOnlineAuthMigrationState
mis2
MISProfile
MISProfileModel
MISOnlineAuthEntry
_TtC3mis29LaunchWarningClientOperations
_TtC3mis25LegacyUserTrustOperations
MISEntitlementsModel
MISDBManager
_TtC3mis17LaunchWarningMark
MISLaunchWarningQueryResult
_TtC3mis12SQLStatement
MISLaunchWarningDatabase
MISTrustedTeamIDEntry
MISTrustedProfileEntry
MISTeamIDEntryForUI
appendFormat:
isProfileTrusted:
migrateData:error:
queryExecutableURL:error:
setCdHash:
setUuid:
shared
addObject:
connection
objectAtIndexedSubscript:
unsignedIntegerValue
T@\"NSString\",?,R,C
data
performSelector:withObject:withObject:
setTrusted:
TB,N,V_hasAuxiliarySignature
checkOnlineForLaunchWarningForBundle:withError:
isRejectedWithProfileUUID:withCDHash:
addRTCResetCountOffset:cdHash:error:
certs
setGracePeriodWithProfileUUID:gracePeriod:error:
stringByAppendingPathComponent:
_lastSuccessMonotonicTime
rejectEntryWithProfileUUID:cdHash:isRejectedByWholeProfile:error:
_hasAuxiliarySignature
ceCtx
derEntitlementsStorage
description
executeQuery:withBind:withResults:
findProfilesMatchingPredicates:withCertificate:
queryProfile:
retainCount
Expires
Name
T@\"NSString\",C,N,V_teamID
deleteOnlineAuthEntryWithCdHash:error:
fileURLWithPathComponents:
findProfilesWithCertificate:
setIsRejectedByWholeProfile:
setLegacyProfileGracePeriodWithProfileUUID:gracePeriod:error:
getAuxiliarySignatureWithTeamId:
setCountLimit:
totalSizeMB
trustTeamID:signature:error:
unlock
arrayWithCapacity:
getOnlineAuthEntriesNoThrow
rangeOfString:
setPayload:
tableRowCount:
transactionSemaphore
TB,N,V_isRejected
getOnlineAuthMigrationStateNoThrow
hash
insertEntitlement:forProfile:
isEqualToString:
setIsRejected:
setObject:forKey:
getLegacyProfileGracePeriodsNoThrow
length
T@\"MISTrustedTeamIDEntry\",C,N,V_trustedTeamIDEntry
UUID
_signature
_totalSizeMB
countByEnumeratingWithState:objects:count:
deleteOnlineAuthEntryWithProfileUUID:cdHash:error:
ProvisionsAllDevices
TC,VAppleInternal
isTeamIDTrusted:
profileUUID
reportIndeterminateDetectedWithReason:gracePeriodDays:hoursSinceLastSuccess:profileCountOnDevice:minutesSinceBoot:hoursSinceLastMigration:lastMigrationSource:profileType:
teamIDWithProfileUUID:
Beta
appendString:
setTeamName:
trustProfileUUID:signature:error:
trustedTeamIDs
dealloc
T@\"NSString\",C,N,V_uuid
setGracePeriod:
_url
arrayWithObjects:count:
diagnostics
dictionaryWithDictionary:
lastSuccessResetCount
numberWithBool:
getUserTrustedUUIDsAndReturnError:
kbURL
objectForKeyedSubscript:
recordIndeterminateEntryNoThrowWithProfileUUID:cdHash:onConflictDoNothing:
setLastSeenOSBuild:error:
substringToIndex:
trustedSigningIdentities
T@\"NSString\",&,VName
_trusted
class
legacyProfileGracePeriods
setTrustedTeamIDEntry:
signature
derEntitlements
allCMSBlobs
getCertPrimaryKey:
intValue
recordIndeterminateEntryWithProfileUUID:cdHash:onConflictDoNothing:error:
setGracePeriodNoThrowWithProfileUUID:gracePeriod:
setName:
migrate
TC,VProvisionsAllDevices
TQ,R
_lastSuccessResetCount
setProfiles:
T@\"NSDictionary\",C,Ventitlements
T@\"NSURL\",R,N,VkbURL
dictionaryWithObjects:forKeys:count:
getOnlineAuthEntryNoThrowWithProfileUUID:cdHash:
teamID
unsignedIntValue
uuid
Tq,N,R,VlastMigrationMonotonicTime
_fixedup
stringWithFormat:
release
isProxy
init
initWithTeamID:signature:
insertProfile:
profileIsForLocalProvisioning:
queryAppBundle:error:
setHasAuxiliarySignature:
T@\"MISProfileModel\",&,VProfiles
dataWithLength:
_isRejectedByWholeProfile
_transactionSemaphore
findProfilesMatchingEntitlements:withCertificate:
flavor
setUserOverride:forBundle:withError:
substringFromIndex:
lastSeenOSBuild
Ti,N,R,VlastMigrationSourcesBitmask
existsIndeterminatesWithProfileUUID:withCDHash:
setLastSuccessResetCount:
initWithDatabaseURL:asReadOnly:
T@\"NSString\",R,N
createOnlineAuthEntry:error:
removeProfileWithUuid:error:
stringWithCapacity:
bytes
emitEntitlementPredicates:predicateHandler:
existsIndeterminatesSoon
existsIndeterminatesSoonWithProfileUUID:withCDHash:
Local
T#,R
T@\"NSData\",C,N,V_cdHash
allProfiles
deviceUDID
onlineAuthEntries
profileUUIDsWithSigningIdentity:
setLocal:
T@\"MISEntitlementsModel\",&,VEntitlements
T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_transactionSemaphore
createTrustedTeamIDEntryWithTeamID:signature:error:
defaultManager
ping:
queryForBundle:withError:
signingIdentitiesWithProfileUUID:
teamName
T@\"NSString\",R,C
Ti,Vflavor
databaseWithURL:
hasAuxiliarySignature
queryCMSBlobForProfile:forcingXML:handler:
setBeta:
setExpires:
setObject:forKeyedSubscript:
banCDHash:error:
dbURL
deleteSetting:
mutableBytes
setUserOverride:forBundle:error:
superclass
transaction:immediate:
trusted
raw
Tq,R,N,VwarningState
UTF8String
_profileUUID
authorizeEntryWithProfileUUID:cdHash:gracePeriod:currentMonotonicTime:currentResetCount:error:
initWithTeamID:teamName:trusted:hasAuxiliarySignature:
isProfileUUIDBanned:
T@\"NSString\",C,N,V_teamName
allTeamIDs
fixUp
lastSuccessMonotonicTime
profileProvisionsAllDevices:
self
setLastSeenOSBuildNoThrow:
setLastSuccessMonotonicTime:
_db
T@\"NSString\",C,N,V_profileUUID
_teamName
caseInsensitiveCompare:
count
indeterminateTime
Tq,N,V_lastSuccessMonotonicTime
createTrustedTeamIDEntryWithProfileUUID:signature:error:
dictionaryWithCapacity:
performSelector:
readSetting:
shmURL
trustedTeamIDEntry
initWithString:
dataWithContentsOfFile:options:error:
deleteOnlineAuthEntryNoThrowWithProfileUUID:cdHash:
initWithUUID:trustedTeamIDEntry:
numberWithUnsignedLongLong:
path
setupSchema
signingIdentitiesWithTeamID:
pathExtension
transaction:
untrustProfileUUID:error:
Tq,N,V_lastSuccessResetCount
allSigningIdentities
conformsToProtocol:
stringByDeletingLastPathComponent
hasSuffix:
T@\"NSData\",C,N,V_signature
.cxx_destruct
T@\"NSString\",&,VUUID
Td,R,N,V_totalSizeMB
_uuid
banProfileUUID:error:
db
isKindOfClass:
dictionaryDescription
entitlements
retain
lastInsertRowID
T@\"NSString\",N,R
_readonly
_trustedTeamIDEntry
setFlavor:
setupPermissions
Entitlements
T^{CEQueryContext=},R
fileExistsAtPath:
getTeamIDForProfileUUID:error:
T@\"NSDate\",&,VExpires
trustedProfiles
dataWithBytesNoCopy:length:freeWhenDone:
getLegacyProfileGracePeriodNoThrowWithProfileUUID:
profilesWithTeamID:
setEntitlements:
teamIDsWithSigningIdentity:
Ti,N,V_gracePeriod
objectForKey:
setCerts:
payload
initWithDatabaseURL:
isUserOverridden
setUUID:
isEqual:
numberWithInt:
setAppleInternal:
stringWithUTF8String:
utdb
T@\"OnlineAuthMetrics\",N,R
auxiliarySignatureWithTeamID:
isRejected
numberWithLongLong:
numberWithUnsignedInteger:
reportMigrationCompletedWithSourcesBitmask:droppedNoCDHash:droppedProfileUninstalled:droppedOther:fromOsBuild:
TB,N,V_isRejectedByWholeProfile
T@\"NSString\",&,VTeamID
enumerateObjectsUsingBlock:
initWithProfileUUID:cdHash:gracePeriod:lastSuccessMonotonicTime:lastSuccessResetCount:isRejected:isRejectedByWholeProfile:
timeIntervalSince1970
checkpoint
deleteTrustedWithTeamID:error:
lastPathComponent
setTeamID:
teamsForSettingsTrustUI
checkOnlineForLaunchWarningForCDHash:cdhashType:withError:
warningState
writeToFile:atomically:
Profiles
T@\"NSMutableDictionary\",&,Vpayload
checkForLaunchWarningWithCdhashType:cdhash:error:
T@\"NSURL\",R,N
_isRejected
deleteTrustedWithProfileUUID:error:
isMemberOfClass:
shouldPreventLaunch
teamIDSupportsAuxiliarySignature:
warningID
AppleInternal
setProfileUUID:
addMonotonicTimeOffset:cdHash:error:
autorelease
cdHash
insertSigningIdentities:withProfileUUID:
isIndeterminate:resetCount:
version
allProfileUUIDs
TC,VLocal
executeQuery:withBind:withCancellableResults:
isProfileInstalled:
performSelector:withObject:
setSignature:
stringWithString:
containsObject:
isCDHashBanned:
enumerateKeysAndObjectsUsingBlock:
initWithDB:
pathComponents
TB,R,N,VisUserOverridden
lastMigrationMonotonicTime
respondsToSelector:
setOnlineAuthMigrationStateWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:error:
dataWithBytes:length:
deleteCharactersInRange:
lock
removeObjectForKey:
setOnlineAuthMigrationStateNoThrowWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:
setProvisionsAllDevices:
walURL
_teamID
TC,VBeta
_gracePeriod
_weak_db
existsIndeterminates
fileURLWithPath:isDirectory:
getLaunchWarningDataFromDB:error:
initWithUUID:withTeamID:withName:withExpiry:isUniversal:isAppleInternal:isLocal:isBeta:
allocWithZone:
isRejectedByWholeProfile
redactedDescription
setSetting:toValue:
TeamID
__swift_objectForKeyedSubscript:
copyWithZone:
countCDHashesRejectedByProfileNoThrowWithProfileUUID:
dateWithTimeIntervalSince1970:
fromSQLStatement:withMap:
lastMigrationSourcesBitmask
queryForExecutableURL:withError:
TB,N,V_trusted
checkForLaunchWarning:error:
debugDescription
longLongValue
T@\"NSArray\",C,Vcerts
_cdHash
deleteOnlineAuthEntryNoThrowWithCdHash:
zone
T@\"NSURL\",R,N,V_url
fileURLWithPath:
subarrayWithRange:
gracePeriod
initWithWarningState:withUserOverridden:withKBURL:
untrustTeamID:error:
```
