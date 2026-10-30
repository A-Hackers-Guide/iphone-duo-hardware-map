# `/usr/lib/libmis.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 701,808 bytes.

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
true
INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, -1, 0, ?1)\nON CONFLICT(id) DO UPDATE SET last_seen_os_build = ?1
c7854afa-6894-4864-8d3c-15f6ccc6728d
databaseSchemaVersion
3
9
INSERT INTO banned_cdhashes (cdhash)\nVALUES (?1)\nON CONFLICT DO NOTHING
SELECT DISTINCT signing_identity FROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nLEFT JOIN trusted_team_ids ON trusted_team_ids.team_id = profiles.team_id\nWHERE trusted_team_ids.team_id IS NOT NULL
d1576fca-f736-46eb-8ac5-d5b4db7503ac
NoExecute
ROLLBACK TRANSACTION
INSERT INTO online_auth_migration_state (\n    id, last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\n)\nVALUES (1, ?1, ?2, \"\")\nON CONFLICT(id) DO UPDATE SET\n    last_migration_monotonic_time = ?1,\n    l
SignatureVersion
AppAudience
SELECT team_id, signature\nFROM trusted_team_ids\nWHERE team_id = ?1
, profileUUID = 
SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth\nWHERE 
Attempted to install a Beta profile without the proper entitlement.
isRejectedByWholeProfile
UserTrust.db
LaunchWarnings
UPDATE online_auth SET last_success_monotonic_time = last_success_monotonic_time + ?1 
relaxProfileExpiry-%@
OnlineAuthorizationOnAllMatchingProfiles
*
OnlineAuthorization
SignerCertificate
com.apple.misagent
243LU875E5
UniqueDeviceID
ovrr
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?3, ?4, ?5, ?1, ?2, 0, 0)\nON CONFLICT(uui
INSERT INTO team_id_info VALUES (@team_id, @team_name)
SELECT profiles.uuid, trusted_team_ids.team_id, signature\nFROM trusted_team_ids\nLEFT JOIN profiles\nON trusted_team_ids.team_id = profiles.team_id
pk
profile_is_apple_internal
SELECT xml_profiles_cache.uuid, xml_profiles_cache.cms_blob FROM xml_profiles_cache LEFT JOIN profiles ON profiles.uuid = xml_profiles_cache.uuid WHERE profiles.is_for_all_devices = 1 OR profiles.is_local = 1
Status
SELECT team_id\nFROM profiles\nWHERE uuid = ?1
DELETE FROM trusted_team_ids WHERE team_id = ?1
%F
AppleInternalProfile
profile_is_local
invalid
CREATE TABLE IF NOT EXISTS trusted_team_ids ( team_id TEXT PRIMARY KEY, signature BLOB )
LaunchWarningsOnInstall
v24@?0^{sqlite3_stmt=}8@\"NSDictionary\"16
4a20c45a-2a99-4ad8-bdd2-c7ab4b0c1a8d
SELECT COUNT(*) FROM %@
Profile
ValidateSignatureOnly
GetLocalLaunchWarningData
LaunchWarningData
cdht
An error occured while accessing the profile database.
SELECT uuid FROM certificate_provisioning_cache JOIN certificates ON certificates.pk = leaf_pk WHERE certificates.leaf = @cert
profile_cms_blob
MISTrustedTeamIDEntry(%@, %@)
MigrationPhase
Cert
SignerType
%@%@%@
SELECT uuid, team_id, name, expires, is_for_all_devices, is_apple_internal, is_local, is_beta FROM profiles
SELECT uuid\nFROM user_trusted_profiles
2bd82cb4-9549-4f99-b578-506b4a05b00c
SELECT 1 FROM online_auth WHERE 
2006-05-31
8c9a3b2d-c2a3-47f5-b7fc-ae7bcdc79cbf
Name
UPDATE trusted_team_ids SET signature = NULL WHERE team_id = ?1
AuthListBannedUpps.plist
An error occured while communicating with the agent.
Version
@is_for_all_devices
B24@?0^{sqlite3_stmt=}8@\"NSDictionary\"16
resource added
app
8
INSERT INTO legacy_profile_grace_periods (uuid, grace_period)\nVALUES (?1, ?2)\nON CONFLICT(uuid) DO UPDATE SET grace_period = ?2
cdhash_type, cdhash, reason, flags, timestamp, kb_url
ExpirationDate
profile_uuid
v24@?0@\"NSString\"8@\"NSData\"16
WITH filteredProfileUUIDs(uuid) AS (%@) SELECT profiles.uuid, profiles.team_id, profiles.name, profiles.expires, profiles.is_for_all_devices, profiles.is_apple_internal, profiles.is_local, profiles.is_beta, profiles.is_der FROM filteredProf
HasAuxiliarySignature
com.apple.mis.onlineauth.indeterminate_detected
SELECT DISTINCT profiles.uuid\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1
09fcf192-750c-4a39-9a0e-cfe6faa82275
The application does not have a valid signature.
isRejected
CREATE UNIQUE INDEX certificate_leaf_index ON certificates (leaf)
security.codesigning.config
adaea588-c074-4b87-b8ea-26cb685b3443
INSERT INTO team_id_info VALUES (@team_id, @team_name) ON CONFLICT DO NOTHING
SigningFuse
 from misagent adding RTC reset count offset 
DELETE FROM online_auth WHERE cdhash = ?1
SELECT COUNT(*) FROM profiles
e09bc661-bd16-4be0-9800-5235640f3392
cbfd2102-86b1-4895-990f-dbaece4c63f2
1.2.840.113635.100.12.19
@leaf_pk
profile_is_for_all_devices
lastSuccessResetCount
auth
locl
INSERT OR IGNORE INTO signing_identities VALUES (NULL, @uuid, @signing_identity)
PRAGMA foreign_keys = ON
@totalPredicates
SELECT DISTINCT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE team_id = ?1
CopyAll
%@%@%lld
CREATE TABLE IF NOT EXISTS signing_identities ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, signing_identity TEXT NOT NULL, UNIQUE(uuid, signing_identity), CONSTRAINT fk_signing_identity_profile_uuid  FOREIGN KEY (uuid)  REFER
SELECT COUNT(*)\nFROM online_auth\nWHERE uuid =  ?1 AND is_rejected = 1 AND is_rejected_by_whole_profile = 1
Indeterminates.plist
CREATE TABLE IF NOT EXISTS banned_profile_uuids (  uuid TEXT NOT NULL )
legacy_profile_grace_periods
com.apple.mis.onlineauth.migration_completed
SELECT grace_period FROM legacy_profile_grace_periods WHERE uuid = ?1
Attempting to trust team ID, but no installed profiles have that team ID
profile_is_beta
CREATE TABLE IF NOT EXISTS settings ( name TEXT, value TEXT, PRIMARY KEY (name) )
CopySingle
Migrate
SELECT 1\nFROM online_auth\nWHERE\n    (uuid = ?1 AND cdHash = ?2 AND is_rejected = 1) OR\n    (uuid = ?1 AND is_rejected = 1 AND is_rejected_by_whole_profile = 1)
mis
MobileIdentityService
SELECT cms_blob as blob FROM xml_profiles_cache
CREATE TABLE IF NOT EXISTS sep_trusted_team_ids (\n    team_id TEXT PRIMARY KEY,\n    signature BLOB NOT NULL\n)
This provisioning profile is unsupported.
@is_beta
?2 > last_success_monotonic_time + (grace_period
AddMonotonicTimeOffset
, user_override, pk FROM launch_warning WHERE cdhash_type = ?1 AND cdhash = ?2
TeamIdentifier
d
HonorBlocklist
last_migration_sources_bitmask
SELECT team_id FROM profiles WHERE uuid = ?1
No code signature found.
Running this application requires Developer Mode to be enabled.
DELETE FROM settings WHERE name = ?1
OnlineCheckType
SELECT uuid, grace_period FROM legacy_profile_grace_periods
INSERT INTO xml_profiles_cache VALUES (@uuid, @cms_blob)
@is_apple_internal
The requested profile does not exist (it may have been removed).
db_utils.m
UniversalFileOffset
ProvisionsAllDevices
xrOS
cdhd
) AND is_rejected = 0
97b12f3c-1687-4883-93e0-f3ac1292a654
InternalBuild
@name
7
@signing_identity
online_auth_entries
Profile Signing V2
end transaction
ValidatedByProfile
SigningID
lwid
Remove
COMMIT TRANSACTION
ON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = 0,\n    last_success_monotonic_time = -1,\n    last_success_reset_count = -1
univ
hoursSinceLastMigration
AllowAdHocSigning
hoursSinceLastSuccess
SELECT 1\nFROM banned_profile_uuids\nWHERE uuid = ?1
The provisioning profile requires online authorization.
%@-wal
begin transaction
UPDATE online_auth SET grace_period = ?2\nWHERE uuid = ?1
iOS
@expires
profileUUID
RespectUppTrustAndAuthorization
AuthListBannedCdHashes.plist
The signature was not valid.
https://support.apple.com/116947
The executable contains an invalid signature.
The application's signature is valid but it does not match the expected hash.
@wildcard
resource deleted
MessageType
UserTrustedUpps.plist
ForceXML
cdvr
profileCountOnDevice
Rejections.plist
Predicates
MISTeamIDEntryForUI(%@, %@, %d, %d)
TeamID
CREATE TABLE IF NOT EXISTS team_id_info ( team_id TEXT NOT NULL, team_name TEXT NOT NULL,  PRIMARY KEY (team_id) )
@team_id
/Library/MobileDevice/ProvisioningProfiles
CREATE TABLE xml_profiles_cache ( uuid TEXT NOT NULL PRIMARY KEY, cms_blob BLOB NOT NULL, CONSTRAINT fk_xml_profile_cache_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )
,
Trust
team
bool%@
SELECT DISTINCT signing_identities.signing_identity\nFROM signing_identities\nLEFT JOIN profiles ON profiles.uuid = signing_identities.uuid\nWHERE profiles.uuid = ?1
NULL
2
droppedProfileUninstalled
SELECT 1\nFROM banned_cdhashes\nWHERE cdhash = ?1
The provisioning profile is banned.
init()
8ae887e0-8d30-448a-b10d-0312c5b71f05
Unable to allocate memory.
current_rtc_reset_count
3d98340d-a43f-4263-8645-51937b4bffd0
bool
SELECT uuid, cms_blob FROM profiles WHERE is_der = 0 AND (is_for_all_devices = 1 OR is_local = 1)
Attempted to install a Beta profile over lockdown connection.
s
UPDATE profiles SET is_beta = 1 WHERE uuid = @uuid
@p%u
rollback transaction
11
2f319679-66b9-44cf-9cf0-723471de0db9
The executable was signed with invalid entitlements.
The user did not explicitly trust the provisioning profile.
profile_expires
CREATE TABLE certificates ( pk INTEGER PRIMARY KEY AUTOINCREMENT, leaf BLOB UNIQUE NOT NULL)
tvOS
warndata
/private/var/db/MobileIdentityData
SELECT DISTINCT team_id\nFROM profiles\nLEFT JOIN signing_identities ON signing_identities.uuid = profiles.uuid\nWHERE signing_identity = ?1
No team ID found for profile UUID: 
SELECT cms_blob FROM xml_profiles_cache WHERE uuid = @uuid
profile_team_id
ExpectedHash
false
chlw
Got error from misagent when setting trust: error = 
last_migration_monotonic_time
SELECT value FROM settings WHERE name = ?1
application-identifier
UPDATE online_auth SET last_success_reset_count = last_success_reset_count + ?1 
DELETE FROM team_id_info WHERE team_id = ?1
amfi_emulate_device_udid
MISTrustedProfileEntry(%@, %@, %@)
B16@?0r^{MISMatchedProfile=^{__CFString}^{__CFString}BBBBB@}8
SELECT team_id, signature\nFROM sep_trusted_team_ids\nWHERE team_id = ?1
SELECT uuid FROM profiles WHERE uuid = @uuid
%@_%s
IsVirtualDevice
MISOnlineAuthEntry(%@, %@, gracePeriod: %i, lastSuccessMonotonicTime: %lli, lastSuccessResetCount: %lli, isRejected: %i, isRejectedByWholeProfile: %i)
cdha
Unknown reply type: 
AddRTCResetCountOffset
WHERE cdhash = ?2
A file operation failed.
A valid provisioning profile for this executable was not found.
Internal
SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth
Entitlements
@cert
com.apple.mis.warning
SELECT last_migration_monotonic_time, last_migration_sources_bitmask, last_seen_os_build\nFROM online_auth_migration_state\nWHERE id = 1
ReleaseType
A signed resource has been added, modified, or deleted.
SELECT profiles.team_id, profiles.cms_blob, profiles.uuid FROM profiles
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 0, 0)\n
TeamName
Install
UnauthoritativeLaunch
ApplicationIdentifierPrefix
deviceUDID
!
CREATE TABLE IF NOT EXISTS online_auth_migration_state (  id INTEGER NOT NULL PRIMARY KEY CHECK (id = 1),  last_migration_monotonic_time INTEGER NOT NULL,  last_migration_sources_bitmask INTEGER NOT NULL,  last_seen_os_build TEXT NOT NULL )
8f327bd3-89e8-46e5-bcf5-72a260f6dd36
The identity used to sign the executable is no longer valid.
B16@?0^v8
MainExecutablePath
INSERT INTO profiles VALUES (@uuid, @team_id, NULL, @name, @expires, @is_for_all_devices, @is_apple_internal, @is_local, @is_beta, @cms_blob, @is_der)
resu
1
CREATE TABLE profiles ( uuid TEXT NOT NULL PRIMARY KEY, team_id TEXT NOT NULL, install_time TEXT DEFAULT CURRENT_TIMESTAMP, name TEXT NOT NULL, expires INTEGER, is_for_all_devices INTEGER, is_apple_internal INTEGER, is_local INTEGER, is_bet
The code signature version is no longer supported.
com.apple.mis
TimeToLive
lwov
4
b9e61602-b1a2-4b73-b0f9-54cc3fff4244
There was an error communicating with your device.
The provisioning profile's App Audience is not suitable for this device.
INSERT INTO certificate_provisioning_cache VALUES (NULL, @uuid, @leaf_pk)
ValidatedByUniversalProfile
blob
SELECT uuid\nFROM profiles\nWHERE team_id = ?1 AND is_for_all_devices = 1
Encountered XPC_TYPE_ERROR: 
SELECT pk FROM certificates WHERE leaf = @cert
ALTER TABLE profiles ADD COLUMN is_der INTEGER DEFAULT (0)
1.2.840.113635.100.6.2.17
uuid
@uuid
9c0fab7e-93cf-4d83-8340-9ea33b5846cc
DeveloperCertificates
TrustCacheOnly
v8@?0
AppleMobileFileIntegrity
fbe71da1-0834-4d49-9b41-d3fa7f9e4d4f
CREATE TABLE IF NOT EXISTS banned_cdhashes (  cdhash BLOB NOT NULL )
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 1, ?3)\nON CONFLICT(uui
v16@?0^{sqlite3_stmt=}8
begin immediate transaction
91c408d9-0fbe-44c4-aa74-37c7f734e159
Rejected by policy.
UUID
6
@team_name
MIS XPC failure: 
minutesSinceBoot
1cf29dc4-4f08-457d-b9a7-512c89f0e142
ProvisionedDevices
v16@?0@\"NSObject<OS_xpc_object>\"8
DetachedSignature
mis.db
DELETE FROM online_auth WHERE uuid = ?1 AND cdhash = ?2
An unknown error has occurred.
AllowLaunchWarnings
CDHash
mis.MISOnlineAuthMigrationState
48988f8b-9b77-4165-8eb1-038a0745dc87
SELECT COUNT(1)\nFROM profiles\nWHERE team_id = ?1
@is_local
mis.LegacyUserTrustDB
ProfileID
bee84af7-d2ca-44e9-992b-54db447d20fc
The maximum number of apps for free development profiles has been reached.
path != NULL
LogResourceErrors
The cdhash is not in the trust cache.
@cms_blob
B40@?0^{__CFString=}8^{__CFString=}16B24B28B32B36
INSERT INTO trusted_team_ids (team_id, signature)\nVALUES (?1, ?2)\nON CONFLICT(team_id) DO UPDATE SET signature = ?2
Attempted to modify an immutable provisioning profile.
INSERT INTO banned_profile_uuids (uuid)\nVALUES (?1)\nON CONFLICT DO NOTHING
SELECT DISTINCT signing_identity FROM signing_identities
gracePeriod
CREATE TABLE entitlements_provisioning_cache ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, predicate TEXT NOT NULL, wildcard INTEGER NOT NULL, UNIQUE(uuid, predicate), CONSTRAINT fk_predicate_profile_uuid  FOREIGN KEY (uuid)  
CREATE TABLE IF NOT EXISTS launch_warning (\n    pk INTEGER PRIMARY KEY AUTOINCREMENT,\n    cdhash_type INTEGER,\n    cdhash BLOB NOT NULL,\n    reason INTEGER,\n    flags INTEGER,\n    user_override BOOLEAN,\n    timestamp INTEGER,\n    UN
SELECT 1\nFROM profiles\nWHERE uuid = ?1 AND is_for_all_devices = 1
SELECT 1\nFROM profiles\nWHERE uuid = ?1 AND is_local = 1
SELECT cms_blob FROM profiles WHERE is_der = 0
SELECT uuid, predicate FROM entitlements_provisioning_cache WHERE predicate LIKE 'string%' || x'1f' || '*' AND wildcard = 1
AuxiliarySignature
294be08b-487f-4020-a986-011dbc7a4fc8
This provisioning profile cannot be installed on this device.
type
SELECT uuid FROM profiles
%02x
SELECT cms_blob FROM profiles WHERE uuid = @uuid
resource modified
DER-Encoded-Profile
watchOS
INSERT OR IGNORE INTO entitlements_provisioning_cache (uuid, predicate, wildcard) VALUES (?1, ?2, 1)
PPQCheck
mobile
3d2a1eea-d1f8-42ab-af5a-545ce51054a7
UseSoftwareSigningCert
CREATE TABLE IF NOT EXISTS online_auth (  uuid TEXT NOT NULL,  cdhash BLOB NOT NULL,  grace_period INT NOT NULL,  last_success_monotonic_time INT NOT NULL,  last_success_reset_count INT NOT NULL,  is_rejected INT NOT NULL DEFAULT (0),  is_r
ON CONFLICT(uuid, cdhash) DO NOTHING
This provisioning profile does not have a valid signature (or it has a valid, but untrusted signature).
Ping
profile_name
SigningTime
v32@?0@8Q16^B24
SELECT uuid\nFROM profiles\nWHERE team_id = ?1
LocalProvision
v16@?0@\"NSString\"8
ProfileUUID
B8@?0
last_seen_os_build
SELECT trusted_team_ids.team_id, signature\nFROM profiles\nLEFT JOIN trusted_team_ids\nON profiles.team_id = trusted_team_ids.team_id\nWHERE uuid = ?1
%y%m%d%H%M%SZ
AGP.plist
SkipProfileIdentifierPolicy
CREATE TABLE IF NOT EXISTS legacy_profile_grace_periods (  uuid TEXT NOT NULL PRIMARY KEY,  grace_period INT NOT NULL,  CONSTRAINT fk_legacy_profile_grace_period_uuid    FOREIGN KEY (uuid)    REFERENCES profiles(uuid)    ON DELETE CASCADE )
SELECT\n    DISTINCT profiles.team_id,\n    team_id_info.team_name,\n    trusted_team_ids.team_id IS NOT NULL,\n    trusted_team_ids.signature IS NOT NULL\nFROM profiles\nLEFT JOIN trusted_team_ids ON trusted_team_ids.team_id = profiles.tea
OSX
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
apppath
mis.LaunchWarningDB
The application's signature is valid, but a provisioning profile can not be found that matches this version.
CreationDate
ProvisioningCDHashes
65033b0b-6071-4ad2-8509-f8e087b74d5b
cdHash
BEGIN TRANSACTION
 from misagent when migrating data
current_monotonic_time
INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)\nON CONFLICT(u
INSERT OR IGNORE INTO entitlements_provisioning_cache VALUES (NULL, @uuid, @predicate, @wildcard)
com.apple.online-auth-agent.xpc
85255e8b-352b-4d58-8e09-81203580f434
5
%Y%m%d%H%M%SZ
Payload
i16@?0^{__SecPolicy=}8
CREATE TABLE certificate_provisioning_cache ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, leaf_pk INTEGER NOT NULL, UNIQUE(uuid, leaf_pk), CONSTRAINT fk_certificate_leaf  FOREIGN KEY (leaf_pk)  REFERENCES certificates(pk)  ON 
CREATE UNIQUE INDEX entitlements_cache_index ON entitlements_provisioning_cache (uuid, predicate)
SELECT DISTINCT team_id FROM profiles
An unexpected error was encountered (0x%X)
@is_der
lastSuccessMonotonicTime
IsNativeForPlatform
10
SELECT team_id, signature\nFROM trusted_team_ids
beta-reports-active
CopyMatching
ValidatedByLocalProfile
CdHash
AuthoritativeLaunch
string
lastMigrationSource
DELETE FROM profiles WHERE uuid = @uuid
DELETE FROM trusted_team_ids\nWHERE EXISTS (\n    SELECT 1\n    FROM profiles\n    WHERE uuid = ?1 AND profiles.team_id = trusted_team_ids.team_id\n)
PRAGMA journal_mode = WAL
logResourceError
, user_override, pk FROM launch_warning WHERE pk = ?1
Offset
LaunchWarning.db
SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth\nWHERE uuid = ?1 AND cdhash = ?2
INSERT OR REPLACE INTO settings (name, value) VALUES (?1, ?2)
ReportIndeterminateSoon
Invalid arguments or option combination.
This provisioning profile has expired.
INSERT OR IGNORE INTO certificates VALUES (NULL, @cert)
ckty
sgnt
v32@?0@\"NSString\"8Q16^B24
 from misagent adding monotonic time offset 
MIS XPC unexpected response with no data.
?1 != last_success_reset_count OR 
d9d5fa63-7084-4346-bada-96e463ad1771
setDatabasePermissionsInternal
%@.%@
number
CREATE TABLE IF NOT EXISTS user_trusted_profiles (\n    uuid TEXT NOT NULL PRIMARY KEY,\n    team_id TEXT,\n    CONSTRAINT fk_team_id\n        FOREIGN KEY (team_id)\n        REFERENCES sep_trusted_team_ids(team_id)\n        ON DELETE CASCAD
This provisioning profile is malformed.
%@-shm
SELECT team_id, signature FROM trusted_team_ids
ALTER TABLE launch_warning ADD COLUMN kb_url TEXT DEFAULT NULL
Platform
(%lu,@p%lu)
@predicate
v32@?0@8@16^B24
WITH predicates(idx, predicate) AS (VALUES %@), filteredProfileUUIDs(uuid) AS (%@) SELECT * FROM (SELECT profiles.uuid, profiles.team_id, profiles.name, profiles.expires, profiles.is_for_all_devices, profiles.is_apple_internal, profiles.is_
v16@?0^{__CFString=}8
number%@
) * 24 * 60 * 60
visionOS
got non-string when querying UDID
received unhandled event from misagent: %{public}s\n
Query canceled
Checking %{public}@ App Audience, %d, %d
got NULL when querying UDID
Payload is not an array: %{public}s
Couldn't create the legacy profile grace periods table: %s
Error counting cdhashes rejected by profile %{public}s
Error getting legacy profile grace periods: %{public}@
Error getting team ID for profile UUID %{public}s: %{public}@
validation failed because of failing online authorization (%d)
Could not copy signature: 0x%x
Could not extract signer: 0x%x
Error checking if cdHash %{public}s is banned: %{public}@
error installing profile: %{public}s\n
Could not extract cdhash: 0x%x
Ours: %@
Failure creating profile cache key. This shouldn't happen.
Encountered nil UUID when checking trust and authorization
Migration: Couldn't create SecCertificate for %@
Error getting all profile UUIDs %{public}@
Error setting online auth migration state: %{public}@
Skipping a profile because of error %#x.\n
Invalid platform: %du
Encountered record with %ld != 4 entries: %@
Error getting trusted team IDs: %{public}@
Error recording indeterminate entry %{public}s, %{public}s, %{bool}d
Encountered a null or non-string platform identifier.
Error opening DB: %d
Is main executable: %i
Using Provisioning Profile '%@'.
Switched to checking executable url: %s
Error getting auxiliary signature for %{public}s from legacy user trust DB: %{public}@
Failed to create list of provisioning profiles
error getting profile '%{public}s' from fd
cdHash (%p) or matchedProfileIDs (%p) NULL in checkTrustAndAuthorization
Couldn't create certificates index: %s
Error getting online auth entry %{public}s, %{public}s
Error setting last seen OS build: %{public}@
Denying profile %{public}@ due to %{public}@ App Audience
TestFlight platform policy failed, the profile did not include the expected platform %@
MISQL: performing database migration 7 -> 8
Found local launch warning entry: %llu
misagent successfully added RTC reset count offset %ld to %{public}s
Error checking if profile provisions all devices %{public}s: %{public}@
Error getting trusted signing identities: %{public}@
Error getting online auth migration state: %{public}@
Encountered a non-array value for 'Platforms'.
MISAppAprovalState failed to check kMISValidationOptionHonorBlocklist option.
Checking warning state for url: %s
Finalize error (%d) on query: %{public}@
Universal/Local Provisioning Profile '%@' is not viable for validation.
Local Profile '%@' entitlement match list is not a dictionary, but '%@'.
Couldn't fetch trusted team ID info: %s
Prepare error (%d) on query: %{public}@
Failure to convert onlineCheckType. (This should not happen.)
Profile %@ failed to validate entitlements
Performing online authorization.
Checking warning state for bundle: %s
Profile row is not an array: '%{public}s'
MISQL: performing database migration 8 -> 9
Error checking if profileUUID %{public}s is banned: %{public}@
misagent connection error: %{public}s\n
Could not copy code signature (error 0x%x).
unexpected event in handler for referenced item service\n
Critical SQLite error, could not checkpoint
Invalid reason in database: %lld
Error checking if profile is for local provisioning %{public}s: %{public}@
error processing kMISValidationOptionUniversalFileOffset (invalid type?), error 0x%x
MISQL: performing database migration 9 -> 10
Error getting team IDs with signing identity %{public}s: %{public}@
Step error (%d) on query: %{public}@
Ignoring unenforced App Audience: %{public}@ from profile %{public}@
Online authorization rejected (%#llx), %@, %@
Couldn't fetch trusted signing identities from xml_profiles_cache: %s
Couldn't create the online auth migration state table: %s
%{public}s: unexpected object type processing %{public}s errors
cdHash is NULL after successful validation? (This should not happen.)
Unable to open AppleMobileFileIntegrity user client: 0x%x
Couldn't fetch single asterisk wildcard predicates: %s
Performing warning lookup for cdhash type: %u
Error getting profile UUIDs with signing identity %{public}s: %{public}@
MISQL: null version, potential erase or upgrade
Encountered a provisioning profile that does not provision the current platform.
MISDataMigrate error: %{public}@
Online authorization succeeded: %@, %@
Couldn't fetch trusted signing identities from profiles: %s
Error getting user trust for team ID %{public}s: %{public}@
Found in cert cache, but cert type is CertTypeError (this should not happen).
Migration: Unable to create profile for %@
Couldn't insert new types for single asterisk wildcard predicates: %s
Unable to get best cdhash digest algorithm: %{public}s
cdhash is nil in database
Error getting signing identities with team ID %{public}s: %{public}@
Couldn't add is_der to the profiles table: %s
Migrating team ID info: Unable to create profile for %@
Received unhandled event from misagent: %{public}s
Failure creating profile payload data: %@
Wrong profile row count %ld != expected %ld
unrecognized status %d from codesigning library
Could not extract signing time: 0x%x
Error getting user trust for profile UUID %{public}s: %{public}@
Error getting online auth entries: %{public}@
No online authorization (%#llx): %@, %@
Error adding trust for profile UUID %@ with signature %@: %@
SecTrustEvaluateWithError failed: %{public}@
Online authorization ambiguous: %@, %@
appApprovalState returned unknown state %ld!
MISQL: performing database migration 1 -> 2
MISQL: performing database migration 5 -> 6
Entry in trusted_team_ids exists without associated profile: %{public}s
Signers array is empty (this should not happen).
Could not create XPC message for setBlacklistOverride
misagent connection error: %{public}s
validation would have failed due to missing DER entitlements
MISAppAprovalState failed to check kMISAppApprovalStateReportIndeterminateSoon option.
UPP is ready, passing through.
Unable to get best cdhash data: %{public}s
Database failed to initialize.
Profile '%@' has a rejected app.
MISQL: performing database migration 4 -> 5
MISQL: performing database migration 6 -> 7
Setting user override: %{public}s to %{bool}d
Error getting all team IDs %{public}@
Blocking bundle with outstanding launch warning: %@
Could not create signer type number?
Authorization still pending: %@, %@
MISQL: performing database migration 10 -> 11
Error checking for indeterminates: %lld, %lld, %{public}s, %{public}s, %@
Trying to release a CE managed context
TestFlight platform policy failed, the profile did not include the expected platform %@, this would have been a critical failure on a customer build
error, could not lookup %s service
Couldn't create entitlements provisioning cache: %s
MISQL: performing database migration 3 -> 4
Error checking for launch warning mark: %@, %@
Provisioning profile '%@' is banned.
Error removing trust for profile UUID %@: %@
Encountered record with no UUID or Team ID: %@
Couldn't create the banned cdhashes table: %s
Profile row has no (or malformed) UUID: '%{public}s'
Local Profile '%@' has non-matching application-identifier.
Couldn't get signing identity for %@
Error migrating user trust: %{public}@
Failure setting detached signature: %d
error getting profile '%{public}s': %{public}s
Could not validate certificate: 0x%x
Unable to create signing info (%d) for: %{public}s
unable to open file to update permissions: %d, %s
SQL error '%{public}s' (%1d)
Skipping a profile %@
Unable to get full cdhash information for: %{public}s
unable to set filesystem permissions on db: %d, %s
%@ was picked for validation
error processing kMISValidationOptionDetachedSignature (invalid type?), error 0x%x
Unable to table row count for %{public}@: %d
Encountered nil record when checking trust and authorization
MISQL: performing database migration 2 -> 3
unexpected error with online-auth-agent connection\n
Error checking if auxiliary signature is supported for team ID %{public}s: %{public}@
Error setting grace period for %{public}s, %d
Caller specified both unauthoritative and authoritative launch modes.
Couldn't insert into signing identities: %s
Error getting legacy profile grace period for %{public}s
DER policy skipped as we're not validating a main executable
validation failed because of missing DER entitlements
Encountered record of wrong size (%ld) when checking trust and authorization
Error getting teams for trust UI: %{public}@
CE context should not be accelerated
Blob data too small
MISValidateUPP: weird answer 0x%llx encountered.
SecTrustSetVerifyDate failed: %d
Couldn't update is_beta column: %s
Setting override for unknown bundle: %{public}s
Overriding expiry for profile %{public}@ with timestamp %f
MISPing error: %{public}@
Couldn't create certificates table: %s
Error getting profile UUIDs for team ID %{public}s: %{public}@
Error getting auxiliary signature for team ID %{public}s: %{public}@
Error getting all signing identities: %{public}@
This function is not supported, and does not behave as you expect. Use MISProfileValidateSignature.
Couldn't create entitlements index: %s
Couldn't create the online auth table: %s
Invalid entitlements in a provisioning profile
New bundle has outstanding launch warning: %@
Failure creating profile cache key.
Invalid profile iteration outcome?
Could not create XPC message for checkLaunchWarning
Error searching for zero length signatures: %s
Got bundle for %@ -> %@
Error getting signing identities with profile %{public}s: %{public}@
Couldn't create profiles table: %s
Couldn't create the xml profiles table: %s
Looking up local launch warning data for bundle: %{public}s
Successfully set trust: profileUUID = %{public}s, teamID = %{public}s, signature = %{public}s, trust = %{bool}d
Encountered a non-boolean value for 'PPQCheck'.
Couldn't create SecCertificate for %@
DB being loaded from %{public}@
%{public}s: %{public}s
error removing profile: %{public}s\n
Skipping universal/local profile with NULL UUID.
Could not decode CMS message.
Not validly signed for app provisioning (type: %ld).
Authoritative
Skipping profile '%@' because it has no entitlement match list?
AppleMobileFileIntegrity user client call failed: 0x%x
CDHash is banned
Unable to find AppleMobileFileIntegrity service.
Couldn't insert team ID info: %s
error getting unauthoritative profile list: %{public}s\n
Auth agent contact failure (entitlement status %lld)
First certificate is NULL (this should not happen).
validation failed because of missing trust and/or authorization (0x%x)
Failure creating static code: %d
There is no leaf cert (this should not happen).
IndeterminateTelemetry: error fetching indeterminates: %{public}@
unable to allocate profiles array
Profile record creation failed, bailing out!
Couldn't create certificates provisioning cache: %s
Couldn't create the banned profile UUIDs table: %s
Error checking for rejection: %{public}s %{public}s %{public}@
Error deleting online auth entry %{public}s, %{public}s
Couldn't create the signing identities table: %s
Error deleting online auth entry %{public}s
unable to check filesystem permissions on db: %d, %s
Invalid UTF8 string in predicate
Error checking for launch warning: %@, %@
invalid kMISValidationOptionUniversalFileOffset %lld
SecTrustCreateWithCertificates failed: %d
Unable to create code object (%d) for: %{public}s
Error fetching schema version
Error getting trusted profile UUIDs: %{public}@
Error checking for indeterminates: %lld, %lld, %{public}s, %{public}s, %{public}@
Error reading local launch warning data: %@, %@
Couldn't create the trusted team IDs table: %s
Couldn't replace signature with nil: %s
Signing identity %{public}s has more than one team IDs: %{public}s. This will cause issues with user trust.
App audience %{public}@ from profile %{public}@ not matched
Bundle has local launch warning data: %@
Couldn't create the team ID info table: %s
Migration: Unable to get signing identity from %@
misagent successfully migrated data
error getting installed profiles: %{public}s\n
Bundle: %@
Accepting Universal/Local Provisioning Profile '%@'.
Keep going %@
Encountered NULL record!
sysctl security.codesigning.config failed with error code: %d global error: %d
Using emulated device UDID: %{public}@\n
misagent successfully added monotonic time offset %ld to %{public}s
MISProfileGetTypeID is not supported, the results this function returns is wrong and should not be relied on
Error parsing profile payload: %@
_TtC3mis15LaunchWarningDB
_TtC3mis25LegacyUserTrustOperations
OnlineAuthMetrics
MISProfile
MISTrustedTeamIDEntry
MISDBManager
MISAgentClient
NSCopying
_TtC3mis17LegacyUserTrustDB
_TtC3mis13XPCConnection
OS_xpc_object
MISLaunchWarningDatabase
MISOnlineAuthEntry
MISTrustedProfileEntry
MISTeamIDEntryForUI
_TtC3mis17LaunchWarningMark
mis2
MISEntitlementsModel
_TtC3mis12SQLStatement
_TtC3mis29LaunchWarningClientOperations
MISProfileModel
MISLaunchWarningQueryResult
NSObject
MISProfileDBClient
MISOnlineAuthMigrationState
mis
mis1
MobileIdentityService
BoxedMISProfile
SQLDB
_db
queryProfile:
initWithUUID:trustedTeamIDEntry:
kbURL
setIsRejected:
shouldPreventLaunch
trustedSigningIdentities
Ti,N,R,VlastMigrationSourcesBitmask
Ti,N,V_gracePeriod
_gracePeriod
getTeamIDForProfileUUID:error:
legacyProfileGracePeriods
removeObjectForKey:
lastInsertRowID
payload
getOnlineAuthMigrationStateNoThrow
initWithProfileUUID:cdHash:gracePeriod:lastSuccessMonotonicTime:lastSuccessResetCount:isRejected:isRejectedByWholeProfile:
rejectEntryWithProfileUUID:cdHash:isRejectedByWholeProfile:error:
T@\"NSObject<OS_dispatch_semaphore>\",R,N,V_transactionSemaphore
setProfileUUID:
T@\"NSString\",R,N
certs
data
setFlavor:
superclass
arrayWithCapacity:
fileURLWithPath:
getOnlineAuthEntriesNoThrow
lastMigrationMonotonicTime
writeToFile:atomically:
cdHash
createOnlineAuthEntry:error:
createTrustedTeamIDEntryWithProfileUUID:signature:error:
findProfilesWithCertificate:
lastSuccessMonotonicTime
setLocal:
initWithDatabaseURL:asReadOnly:
T@\"MISTrustedTeamIDEntry\",C,N,V_trustedTeamIDEntry
derEntitlementsStorage
reportIndeterminateDetectedWithReason:gracePeriodDays:hoursSinceLastSuccess:profileCountOnDevice:minutesSinceBoot:hoursSinceLastMigration:lastMigrationSource:profileType:
setProvisionsAllDevices:
teamIDSupportsAuxiliarySignature:
lastSeenOSBuild
trustedProfiles
Tq,N,V_lastSuccessResetCount
dataWithContentsOfFile:options:error:
retainCount
_fixedup
allocWithZone:
autorelease
dealloc
TB,N,V_isRejected
banCDHash:error:
fromSQLStatement:withMap:
intValue
queryForExecutableURL:withError:
setGracePeriodWithProfileUUID:gracePeriod:error:
setPayload:
addRTCResetCountOffset:cdHash:error:
isEqualToString:
setLastSeenOSBuildNoThrow:
setSignature:
substringFromIndex:
isKindOfClass:
trusted
derEntitlements
numberWithBool:
_uuid
fixUp
setIsRejectedByWholeProfile:
Expires
Entitlements
ProvisionsAllDevices
TQ,R
allTeamIDs
initWithTeamID:signature:
TC,VLocal
Td,R,N,V_totalSizeMB
addMonotonicTimeOffset:cdHash:error:
allProfiles
deviceUDID
dictionaryWithCapacity:
dictionaryWithObjects:forKeys:count:
length
raw
T@\"NSURL\",R,N,VkbURL
dataWithBytesNoCopy:length:freeWhenDone:
numberWithInt:
performSelector:withObject:withObject:
profileProvisionsAllDevices:
respondsToSelector:
teamID
getCertPrimaryKey:
initWithUUID:withTeamID:withName:withExpiry:isUniversal:isAppleInternal:isLocal:isBeta:
numberWithUnsignedInteger:
self
zone
isProfileInstalled:
allSigningIdentities
connection
objectForKey:
objectForKeyedSubscript:
profileIsForLocalProvisioning:
redactedDescription
setAppleInternal:
TC,VBeta
executeQuery:withBind:withResults:
indeterminateTime
setObject:forKeyedSubscript:
shared
teamName
trustTeamID:signature:error:
release
version
T@\"NSString\",N,R
ceCtx
class
setGracePeriod:
TB,R,N,VisUserOverridden
UUID
dictionaryWithDictionary:
existsIndeterminatesWithProfileUUID:withCDHash:
isRejected
setLastSuccessResetCount:
utdb
T@\"NSString\",C,N,V_teamName
Tq,N,R,VlastMigrationMonotonicTime
setGracePeriodNoThrowWithProfileUUID:gracePeriod:
unsignedIntValue
T@\"NSDictionary\",C,Ventitlements
T@\"NSDate\",&,VExpires
_signature
banProfileUUID:error:
checkOnlineForLaunchWarningForBundle:withError:
fileURLWithPath:isDirectory:
getLaunchWarningDataFromDB:error:
insertSigningIdentities:withProfileUUID:
T@\"NSString\",&,VTeamID
T@\"NSString\",C,N,V_uuid
arrayWithObjects:count:
dataWithBytes:length:
deleteOnlineAuthEntryNoThrowWithCdHash:
executeQuery:withBind:withCancellableResults:
isMemberOfClass:
queryCMSBlobForProfile:forcingXML:handler:
containsObject:
enumerateObjectsUsingBlock:
fileExistsAtPath:
removeProfileWithUuid:error:
setCerts:
setExpires:
queryExecutableURL:error:
setOnlineAuthMigrationStateWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:error:
substringToIndex:
unsignedIntegerValue
untrustTeamID:error:
T@\"NSString\",?,R,C
T@\"NSString\",C,N,V_profileUUID
deleteOnlineAuthEntryNoThrowWithProfileUUID:cdHash:
diagnostics
isIndeterminate:resetCount:
lastPathComponent
objectAtIndexedSubscript:
setHasAuxiliarySignature:
allProfileUUIDs
enumerateKeysAndObjectsUsingBlock:
migrateData:error:
setLastSeenOSBuild:error:
setSetting:toValue:
signature
stringWithString:
stringWithUTF8String:
_trusted
description
longLongValue
T@\"NSURL\",R,N
dbURL
deleteSetting:
hasAuxiliarySignature
teamIDsWithSigningIdentity:
totalSizeMB
T@\"NSArray\",C,Vcerts
_teamName
setBeta:
numberWithUnsignedLongLong:
signingIdentitiesWithTeamID:
isCDHashBanned:
deleteTrustedWithProfileUUID:error:
findProfilesMatchingEntitlements:withCertificate:
trustedTeamIDEntry
T@\"NSString\",R,C
dataWithLength:
stringByAppendingPathComponent:
UTF8String
checkpoint
lock
setCdHash:
setTeamID:
_cdHash
Ti,Vflavor
count
teamsForSettingsTrustUI
T@\"NSData\",C,N,V_signature
TeamID
recordIndeterminateEntryNoThrowWithProfileUUID:cdHash:onConflictDoNothing:
auxiliarySignatureWithTeamID:
setUserOverride:forBundle:withError:
countCDHashesRejectedByProfileNoThrowWithProfileUUID:
onlineAuthEntries
performSelector:withObject:
TB,N,V_isRejectedByWholeProfile
.cxx_destruct
T@\"OnlineAuthMetrics\",N,R
checkOnlineForLaunchWarningForCDHash:cdhashType:withError:
flavor
isEqual:
setUUID:
appendString:
countByEnumeratingWithState:objects:count:
getLegacyProfileGracePeriodNoThrowWithProfileUUID:
initWithDatabaseURL:
insertProfile:
isUserOverridden
migrate
T@\"MISProfileModel\",&,VProfiles
isProfileUUIDBanned:
setupSchema
trustedTeamIDs
unlock
TB,N,V_hasAuxiliarySignature
isTeamIDTrusted:
subarrayWithRange:
_teamID
caseInsensitiveCompare:
emitEntitlementPredicates:predicateHandler:
isRejectedWithProfileUUID:withCDHash:
lastMigrationSourcesBitmask
reportMigrationCompletedWithSourcesBitmask:droppedNoCDHash:droppedProfileUninstalled:droppedOther:fromOsBuild:
stringWithFormat:
existsIndeterminates
profileUUID
setCountLimit:
isRejectedByWholeProfile
T@\"NSString\",&,VUUID
_trustedTeamIDEntry
deleteOnlineAuthEntryWithCdHash:error:
getUserTrustedUUIDsAndReturnError:
hash
mutableBytes
performSelector:
AppleInternal
Local
Tq,R,N,VwarningState
existsIndeterminatesSoon
numberWithLongLong:
ping:
setUserOverride:forBundle:error:
shmURL
initWithTeamID:teamName:trusted:hasAuxiliarySignature:
initWithString:
TB,N,V_trusted
db
dictionaryDescription
existsIndeterminatesSoonWithProfileUUID:withCDHash:
hasSuffix:
setTeamName:
rangeOfString:
setProfiles:
teamIDWithProfileUUID:
transaction:immediate:
T@\"NSString\",&,VName
T^{CEQueryContext=},R
addObject:
findProfilesMatchingPredicates:withCertificate:
lastSuccessResetCount
timeIntervalSince1970
_totalSizeMB
Beta
_lastSuccessMonotonicTime
checkForLaunchWarning:error:
dateWithTimeIntervalSince1970:
setupPermissions
stringByDeletingLastPathComponent
_url
appendFormat:
Name
T@\"NSMutableDictionary\",&,Vpayload
pathComponents
signingIdentitiesWithProfileUUID:
_transactionSemaphore
profilesWithTeamID:
setLastSuccessMonotonicTime:
_isRejectedByWholeProfile
_lastSuccessResetCount
checkForLaunchWarningWithCdhashType:cdhash:error:
getOnlineAuthEntryNoThrowWithProfileUUID:cdHash:
insertEntitlement:forProfile:
path
T@\"NSString\",C,N,V_teamID
T#,R
TC,VAppleInternal
_isRejected
databaseWithURL:
getLegacyProfileGracePeriodsNoThrow
_profileUUID
_weak_db
allCMSBlobs
conformsToProtocol:
fileURLWithPathComponents:
getAuxiliarySignatureWithTeamId:
setEntitlements:
setTrustedTeamIDEntry:
__swift_objectForKeyedSubscript:
isProfileTrusted:
profileUUIDsWithSigningIdentity:
queryForBundle:withError:
recordIndeterminateEntryWithProfileUUID:cdHash:onConflictDoNothing:error:
retain
setUuid:
T@\"MISEntitlementsModel\",&,VEntitlements
Profiles
gracePeriod
stringWithCapacity:
transaction:
_readonly
bytes
copyWithZone:
debugDescription
deleteCharactersInRange:
deleteTrustedWithTeamID:error:
setOnlineAuthMigrationStateNoThrowWithLastMigrationMonotonicTime:lastMigrationSourcesBitmask:
trustProfileUUID:signature:error:
_hasAuxiliarySignature
authorizeEntryWithProfileUUID:cdHash:gracePeriod:currentMonotonicTime:currentResetCount:error:
createTrustedTeamIDEntryWithTeamID:signature:error:
deleteOnlineAuthEntryWithProfileUUID:cdHash:error:
queryAppBundle:error:
setName:
untrustProfileUUID:error:
uuid
isProxy
readSetting:
setObject:forKey:
walURL
warningID
warningState
pathExtension
setLegacyProfileGracePeriodWithProfileUUID:gracePeriod:error:
transactionSemaphore
Tq,N,V_lastSuccessMonotonicTime
T@\"NSURL\",R,N,V_url
init
initWithDB:
initWithWarningState:withUserOverridden:withKBURL:
T@\"NSData\",C,N,V_cdHash
TC,VProvisionsAllDevices
defaultManager
entitlements
setTrusted:
tableRowCount:
@24@0:8@16
i24@0:8^v16
i28@0:8@?16B24
^{sqlite3=}
v56@0:8q16q24q32q40@48
@40@0:8:16@24@32
d
v20@0:8B16
@\"MISEntitlementsModel\"
Vv16@0:8
i16@0:8
B40@0:8q16@24^@32
v16@?0@\"<OS_xpc_object>\"8
@\"NSDictionary\"8@?0
q24@0:8@16
B24@0:8@16
C16@0:8
v24@?0^v8@\"NSDictionary\"16
B32@0:8@16@24
@16@0:8
v28@0:8@16i24
^{CEQueryContext=}16@0:8
@\"MISDBManager\"
i40@0:8@16@?24@?32
@\"NSURL\"
@\"NSString\"16@0:8
v16@0:8
B36@0:8@16i24^@28
@\"NSArray\"
@28@0:8@16B24
@36@0:8q16B24@28
Q16@0:8
v24@0:8q16
@36@0:8I16@20^@28
B28@0:8i16^@20
i32@0:8@16@24
@\"NSString\"
B32@0:8@16^@24
B24@0:8:16
i
B60@0:8@16@24i32q36q44^@52
@32@0:8^{sqlite3_stmt=}16@24
@\"MISTrustedTeamIDEntry\"
v80@0:8q16q24q32q40q48q56q64q72
?
v20@0:8i16
@\"NSData\"
@\"NSDictionary\"
C
Q24@0:8@16
@36@0:8@16I24^@28
q
@64@0:8@16@24@32@40C48C52C56C60
B16@0:8
@24@0:8^{_NSZone=}16
B36@0:8B16@20^@28
@32@0:8:16@24
i24@0:8@16
B
@\"NSMutableDictionary\"
i24@0:8@?16
@\"MISProfileModel\"
v16@?0^v8
B36@0:8q16i24^@28
v28@0:8q16i24
^{CEQueryContext=}
B40@0:8@16@24^@32
^{_NSZone=}16@0:8
v20@0:8C16
@60@0:8@16@24i32q36q44B52B56
@32@0:8@16^@24
@24@0:8^@16
#16@0:8
@24@0:8:16
B24@0:8#16
q16@0:8
B44@0:8@16@24B32^@36
@\"NSDate\"
v24@0:8@16
v32@0:8@16@?24
B36@0:8@16B24@?28
^v24@0:8@16
d16@0:8
B32@0:8q16q24
@40@0:8@16@24B32B36
@32@0:8@16@24
v32@0:8@16@24
@\"NSObject<OS_dispatch_semaphore>\"
B16@?0@8
B24@0:8@\"Protocol\"16
v36@0:8@16@24B32
```
