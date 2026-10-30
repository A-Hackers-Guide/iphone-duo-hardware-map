# `/usr/local/bin/keystorectl`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,474,864 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 40 (Size: 5232)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (23)

- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_DarwinFoundation2.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3, weak)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.apfs.crypto.internal.debug</key>
	<true/>
	<key>com.apple.apfs.wvek</key>
	<true/>
	<key>com.apple.applekeystored</key>
	<true/>
	<key>com.apple.frontboard.shutdown</key>
	<true/>
	<key>com.apple.keystore.absinthe</key>
	<true/>
	<key>com.apple.keystore.access-keychain-keys</key>
	<true/>
	<key>com.apple.keystore.allow.background-processing-assertions</key>
	<true/>
	<key>com.apple.keystore.auth-token</key>
	<true/>
	<key>com.apple.keystore.aux.auth</key>
	<true/>
	<key>com.apple.keystore.bak</key>
	<true/>
	<key>com.apple.keystore.class.wku</key>
	<true/>
	<key>com.apple.keystore.config.bind_kek_to_kb</key>
	<true/>
	<key>com.apple.keystore.config.set.escrow_period</key>
	<true/>
	<key>com.apple.keystore.config.set.inactivity_reboot</key>
	<true/>
	<key>com.apple.keystore.config.set.user_uuid</key>
	<true/>
	<key>com.apple.keystore.convenience-bio</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.keystore.device.remote-session</key>
	<true/>
	<key>com.apple.keystore.device.smart-card</key>
	<true/>
	<key>com.apple.keystore.device.verify</key>
	<true/>
	<key>com.apple.keystore.devicebackup</key>
	<true/>
	<key>com.apple.keystore.domain.select</key>
	<true/>
	<key>com.apple.keystore.enable_cache_flow</key>
	<true/>
	<key>com.apple.keystore.escrow.create</key>
	<true/>
	<key>com.apple.keystore.fairplay</key>
	<true/>
	<key>com.apple.keystore.fdr-access</key>
	<true/>
	<key>com.apple.keystore.filevault</key>
	<true/>
	<key>com.apple.keystore.icsc_srp</key>
	<true/>
	<key>com.apple.keystore.info</key>
	<true/>
	<key>com.apple.keystore.lockassertion</key>
	<true/>
	<key>com.apple.keystore.lockassertion.global_assertion</key>
	<true/>
	<key>com.apple.keystore.lockassertion.restore_from_backup</key>
	<true/>
	<key>com.apple.keystore.lockassertion.time_machine</key>
	<true/>
	<key>com.apple.keystore.obliterate-d-key</key>
	<true/>
	<key>com.apple.keystore.opts</key>
	<true/>
	<key>com.apple.keystore.se.passcode_derivation</key>
	<true/>
	<key>com.apple.keystore.se.secret_drop</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.keystore.stash.access</key>
	<true/>
	<key>com.apple.keystore.stash.persist</key>
	<true/>
	<key>com.apple.mobileactivationd.spi</key>
	<true/>
	<key>com.apple.private.apfs.oti</key>
	<true/>
	<key>com.apple.private.applecredentialmanager.allow</key>
	<true/>
	<key>com.apple.private.applekeystored</key>
	<true/>
	<key>com.apple.private.exclaves.kernel-domain</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.xpc.launchd.system-job-bootstrap</key>
	<true/>
	<key>com.apple.rootless.install</key>
	<true/>
	<key>com.apple.rootless.volume.Preboot</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleKeyStoreTestUserClient</string>
		<string>AppleAPFSUserClient</string>
		<string>AppleCredentialManagerUserClient</string>
	</array>
</dict>
</plist>
```

## Objective-C (1 classes, 0 protocols)

Classes: `_TtC11keystorectl13AKSUserClient`

## Strings (3,568)

First 2,500 of 3,568.
```
SEInfo() failed with error: 
persistent.current_day.graceperiod_entries: %u\n
regress-backoff
/Library/MobileBluetooth
 (skip)
_unlock_result
tombstone
Cannot spawn process: %s
extracted.kb
ERROR: failed to remove_kek\n
/Library/Assistant
state,uuid
sikp
missing user uuid (-i)\n
%s kcv: %02x%02x%02x\n
satori_t_decrypt
attest error
is-class-a-available
%s:%spid:%d,%s:%s%s%s%s%s%u:%s No matches returned%s\n
cmd_reference_attest_test
scrt sik pub
0433782bfbfa6dff9715c16e6565781d2251c48c131c55ccff7a41e623135f8bfc2a29a636b07003a4efe4e87da0109adcd19cbd64cee050640cccfc4804955894
replay-get-info-diagnostic
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not create container dev path%s\n
/.overprovisioning_file
secondsUntilReboot
AsymmetricBackupBag
aks_remote_session_reset_all() expect:0, got:%d\n
acl2_set_class
continuity-peer %s: peer not ready (status must be unlock_token_valid to modify)\n
h:w:q
kAKSReturnReadOnly
lu
set-volume-keybag
pass
  * state: %s (0x%x)\n
Map volume to persona
capabilities: %llx 
wheel
verifyAclConstraintInternal
last-passcode-unlock
XXX plz file a radar
key_type_asym_ec_p384
VEK created with uuid %s\n
04b669e15d9303ccff37144a9cefc76ef4a953188f5c5c860710f23336027d75a72e03fe8a7beaebe5fe8ba7dfaec6fc4c373a152b770698573e7fedc30bce9978c8a0d81c0079a6e2e59ef83a3e6e98b937a8e346754aced1f1e1f6577a69e955
/Library/Calendar
ACMCredential - ACMCredentialDataContinuityUnlock
ACMCredentialGetProperty
satori_ecies_transcode
create_public_bag
ghsvlf
\t-v <vek_blob>
%s maps to invalid operation, consult with system_key_string_to_operation()\n
r
CLASS NONE
requirement
set system
stage-stash: 0x%x\n
no key provided
memento-blob-state: 0x%x (%s)\n
/usr/local/bin/nftool
osko
PS
pka_p256_set_class
acl2_wrap
sleeping for %llu seconds\n
must be root..
  Mean Unlocked: No data
crypto_encryptText_version1
LibCall_ACMRequirementDelete
unlock to unwrap escrow records\n
aks_get_bag_uuid returned %x\n
uuid(%d): %s\n
DEVICE_AUTHENTICATION_BIO_ARM
first thread: %d, timeout:%u\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s key_type_asym_pka_p256 failed: %s%s\n
0484c964a69d4156409ff7a143e324039c8013f17d9e7a9caee5c1f4d1e74979802f8b142f33f1966d951bd1b699bf87f9edb0867d112a39e40ea97f34b20b0f73
cob
crypto_deriveKeyAndEncryptData
Attempting to load keybag file %s\n
session: %i, uid: %i\n
digest
acl3_verify
error getting %i config: %x\n
LibCall_ACMPing
Portable
pass-sm-slot %d:\n
setting configuration for passcode to expire in 10 secs\n
OR senderImagePath contains \"securityd_service\"
xtd
se-secret cached
failed to load file %s\n
1
DAK system key test success!\n
continuity-peer %s: success (token wiped with status %d)\n
fdr
Could not get backup handle, this is new style backup. result = %d (%s)\n
max-unlock-attempts
%s/%s/%s/%s
aks_se_get_reset_token(%d) failed -> 0x%x\n
\tinfo: %s, fua: %d
/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/keystorectl/cmd_fv_test.c
    %02d:00 - %u unlocks (UTC)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid charging: %llu%s\n
aks_system_key_gid
/Library/mad/activation_records
guct
public-ota-backup-bag
%s:%spid:%d,%s:%s%s%s%s%s%u:%s missing config entry%s\n
<disk> <uid> [<persona_uid>]
, se recovery is required
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c
ACMParseAclAndCopyConstraintCharacteristics
%s:%spid:%d,%s:%s%s%s%s%s%u:%s error %d%s\n
acl2_sign
writing value to register:\n  register_id = %s\n  flags       = %X\n  value (hex) = 
reboot
0416c849504cfa56ddf445aa2ce89c8c26267dd4e86effe465cd770f3ae097bf0e59442271c549cb117f5afc97febbc868ed767323bea5194b7a428059a3a5ff6c718a44acb55d61eeab7aa750e888c04b9bd05a0b9a4480a80a65d147e3b58273
has-capabilities
Util_DeallocRequirement
debug all
04e278e6984daef7c760dede4e31aeec3bb725dc204f47bb5669e6677ac349e88ba3625497031803f264ebb8dc02bc653267308981b82d25b5e758e987dd190f1e
seconds-since-passcode-change: %llu\n
quickly try to wrap/unwrap with all keys, only report success
SESSION_STATE_AUTHENTICATED
DEVICE_AUTHENTICATION_CREATE_SESSION_TOKEN
Unwrapping VEK with KEK
xart_id_hibernation
keybag supports last known good password
%d: unwrapped key doesn't match original key, class: %d -> %d\n
cleanup
Couldnt create persona\n
dak pub:
kAKSReturnTimeout
kSKSReturnMustMigrate
wrap an item for backup
%24s, line:%5u, size:%5u\n
pka_p384_verify
aks_ref_key_ecies_transcode failed 0x%x\n
ao_pka_create
f:h:p:
acg:o:h:pst:R:
kAKSReturnMustMigrate
applekeystored
SMDK
error: sealed hash slot is locked\n
Delete Context 1
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to parse uuid%s\n
mdm bootstrap token
key-scanner
fairplay
/Library/BulletinBoard
originator peer_status: unlockstate (%d), unwrapped_escrowstate (%d), wrapped_escrowstate (%d)\n
satori_p256_ecdh_1
check if ownership exists for a kek group uuid
SE input SEPUID bound
/Library/ManagedAssets
iter
bc
LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unexpected return value for waitpid (rc=%d)%s\n
state,flags
LibCall_ACMContextDelete
fv_get_booted_from_volume_uuid
aks_remote_session(DEVICE_AUTHENTICATION_ORIGINATOR|DEVICE_AUTHENTICATION_UNLOCK_WITH_ESCROW)@%d expect:0, got:%x)\n
error: must provide a register UUID\n
stash_commit
cant retrieve SIK pub
persistent.previous_day.unlocks_auxiliary: %u\n
/Library/SpringBoard
cpg
DeserializeVerifyPolicy
uuid: %s, 
/Library/SyncedPreferences
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unsupported kek flags (0x%x)%s\n
CCCCCCCCCCCCCCCC
digest:
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Bad input %d %zd %d %zd%s\n
xart_id_fv_explicit_stashed_kek
create-key
sym_unwrap
stash_load
Test_encryption for class %c:\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s statfs error: %s\n%s\n
/Library/Caches
CLASS A
ACMContextGetData
Previous Day:
test-kfv
perform escrow unlock\n
is NOT
k:v:s:o:
Unmap volume
unlock_token_passcode_disabled
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n
okd
mua
\n---*---*---*--- %d\n
error: aks_keybag_persona_list verify failed\n
ao_pka_attest_sw
unknown subcommand: %s\n
us
Test 1: When device is unlocked - you should be able to create/read/write a file.\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s swizz is invalid%s\n
2FA31400-BAFF-4DE7-AE2A-C3AA6E1FD340
info
key_type_asym_ed25519
sidp %s: success\n
AKPU
failed to get user info
/Library/ApplePushService
check,ephemeral
FBSSystemService
Undefined
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n
failed to load bag from disk: %s\n
[%s] (%llu %hu %ld %lld) %s\n
void *SecurityLibrary(void)
xart_id_monotonic_counter_sync
unexpected operation 
ACMCredential - ACMCredentialDataPassphraseExtractable
UIDPlus
_get_config_data
kSKSReturnDecodeError
SiKACapability
fv-create-token
xart_id_keybag_sandman
sbdp
sfa
Stash
continuity_peer_operation
, has last known good recovery blob
pub
crypto_decryptText_version1
Using cmd 0x%x\n
No command specified, use -c <command>
lock cx %s -> (%s)\n
sik pub
gidap
osa
filevault_purge_group
successful
uuid string must be 37 char (got %zd)\n
%s: %d\n
perform DEVICE_AUTHENTICATION_SETUP - register & arm\n
%d: ERROR: failed to lock keybag\n
sks-chaos
kSKSReturnUnsupported
eb
wait in main for threads to join\n
All done. (%d)\n
local-key
sign-key
starting recovery attempt %d of %lld\n
c:d:k:o:s:t:v:
icsc
UID
(two phase) 
kAKSReturnSuccess
kSKSReturnBadPassword
GM
etk
bag-with-escrow-record
04e094603a53de54e50765dacc6b814454b69587cc3c33bb390b27a61620d8e1fb0625d34eb48323b309daf6df045eb46a51414f2ee68674a446cdf2fc26fa758f
CKU
kAKSPasscodeThresholdMessage
kc-unwrap
aonm
unexpected Sesssion info state 
create-bag
ed_create
compute_key curve25519
, stored in xART
/Library/IdentityServices
sas
unlockWithOneness
aks_encrypt(acl3)
no ps slots.
failed with error %d\n
Invalid hex key '%s'\n
kAKSFirstUnlockEvent
<user>
cc_cmp_safe
uuid a: 
cmd_lu
OR senderImagePath contains \"MobileKeyBag\" OR senderImagePath contains \"MobileSystemServices\"
/usr/local/bin/apfsctl
    Biometric unlocks: %u\n
not recoverable
fv_set_protection,disable
vek group
UIK migrated
failed to attest
failed to create escrow bag for target handle %d\n
ks
kSKSReturnBadDeviceKey
kSKSReturnPolicyInvalid
aks_encrypt(acl2)
succeeded
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid soc: %llu%s\n
/Library/Carrier Bundles
performCommand
  (no options shows analytics summary)\n
failed to fetch measurement\n
  * handle: %d lock_state: %s (s: %d es: %d) items: %ld\n
lockdownModeEnabled
ag
ec_p384_create
  * recovery_countdown: %llu, backoff: %llu, passcode attempts: (%u of %u), passcode threshold: %d\n
  Special State Usage:
persistent.recent_sessions[UNLOCKED]:
%*s.. created version: %d, class: %d, type: %d\n
unlock_token_passcode_policy
Util_WriteToBuffer
escrow-register   [-k <keyset>] <passcode>
cmd_test_kks
new key bulk count=%u(kext side)
/tmp/testB
ioKitTransport
starting perf test for handle %d\n
satori_ecies_encrypt
%s:%spid:%d,%s:%s%s%s%s%s%u:%s result = %x%s\n
Getting backup bag uuid for volume %s.\n
unexpectedly (proposed) can retrieve pub
signing key:\n
ps-o-gen
keystorectl.m
failed to create token -> 0x%x\n
sika version: %lld\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Returned Preboot volume is not a string%s\n
/Library/CoreFollowUp
skg
ACMContextAddCredentialWithScope
fv_set_booted_from_volume_uuid
se-reset-token: 
cmd_oneness
ec_p384_verify
attest_encrypt
unregistered 1
persisting stash
requested:
remoteSessionVersion
escrow-authorize
uuid: 
lock-cx keybag
/Library/Accounts
ACMContextGetInfo
using handle %d\n
Cx expiring
verify_decrypt_csk %s\n
keybag uuid
_MKBPAYLOAD
, subject to passcode service
lastPasscodeUnlock
/Library/TCC
\tSize Distribution:
OTABackupBag
error: all sealed hash registers are in use\n
%i,%u,%u,%u,%lld,%lld,%lld,
load_keybag from file %s succeeded (handle=%d)\n
enabled test keys: %x\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s incorrect attestation data%s\n
kek-stash-commit
aks_fv_commit_stashed_kek: %d\n
has-kek-protected-volume-bag
uuid not found\n
keystorectl/ASN1Utils.swift
thread 0 is up again\n
aks_unwrap_key(ck)
sandman blob migrated
se stash state: %s (%d)\n
l:r:
attest_wrap
aks_event_test
kAKSCacheFlowEnabled
test-ephemeral-policy
trying invalid escrow secret\n
  Median Locked: %llu.%02llu minutes\n
user-volume
persona-delete
; used: %d
_securityd
/protected/trustd
Backup bag uuid %s\n
2,3 dak committed/proposed validation failed. automatic_bump: %d, daks_equal: %d
failed to save escrow bag to %s\n
04c59992135415da4dabec15da13c8e72d319b7a5271665656187334a094046bd384a855daea43ab371b2fce48ccfa69eb85901d465beea90351eeff7a1e14c7ab
kAKSReturnXartError
unwrap a key using aks_unwrap_key
test-policy-delay
, been passcode unlocked
se-rm-support-is-set: %d - > 0x%x\n
sidp_operation
persistent.previous_day.unlocks_from_grace: %u\n
aks_system_key_sik
unlock keybag [with password] [-h handle] [-d] [-a] [-v)]
/.ssh
/Library/CoreBrightness
 dir: %s %i\n
Could not open backup bag, result = %d (%s)\n
D-key migrated
attempting two phase passcode change\n
Running fv test against TDM entry 0x%llx\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected version %d%s\n
ACMRequirementGetProperty
owners:
testing
usage : kext-option [--set | -s] [--get | -g] [[--verbosity-level | -v] <level>] [[--log-scope | -l] <mask>] [[--feature | -f] <flags>]\nBitmask for level:\nDefault(none)          0000 \nClass D file creation  0001 \nCalling Rate           
Delete Context 2
failed to allocate array
passcodeRequired
test runtime %llu us pid %d\n
aks_apfs_container_disk_for_path
aks_get_internal_info_for_key
failed to open connection to %s: %d\n
error: register ID must be a valid string-formatted UUID\n
040409dd721195dde7001c1e44187d339df0614bdee99174a595f28c3fa657b0280771c97c0968166ea7d4e7dae4f3096a68362bb1c8f9e76349cf7e419b472d3c
%s:%spid:%d,%s:%s%s%s%s%s%u:%s result: %d, encrypted: %d%s\n
lock-cx
** session list (sorted by creation time)
kid
aks_get_lock_state
supports-rm
/Library/Logs
%s:%spid:%d,%s:%s%s%s%s%s%u:%s escrow blob parse error %d%s\n
ts
description
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sbooted from uuid is not set%s\n
test-threshold-notification
key_type_asym_pka_p256
macos_root
, staged manifest
kind
%*s.. simple test\n
048ba8d6a0d4f3462506b542ac3f30af0fb4f1baf12449b0fc25a69e2b21032b14b12b55a46917346a046f0554f991d0fd2b12c14922fc3e84f0bbcf72108700a9
r_swizz
%s:%spid:%d,%s:%s%s%s%s%s%u:%s no nvram?%s\n
test failed: %d\n
   asymmetric bag count = %u\n
Recovery is not required?\n
Using secret %s
%s:%spid:%d,%s:%s%s%s%s%s%u:%s beacon verified successfully%s\n
kAKSReturnEncodeError
akstest_check_class
tecdhs
Need handle
drop-memento-secret
bak gid public key:
_payload_hash
change system keybag password
DEVICE_AUTHENTICATION_SETUP
rti
Got the volume uuid
bag load
%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n
cf
ow
AppleEffaceableStorage
dump sealed hashes
sik col failed
%s:%spid:%d,%s:%s%s%s%s%s%u:%s uuid not found%s\n
Controller Characteristics
ht
pcpv5bd
LibCall_ACMContextVerifyPolicyWithPreflight_Block
aks_decrypt(acl2)
no src (-s) or dst (-d) class specified!
satori_p256_create_2
os_bound_options
dak bump failed
:shrug:
, smdk entangled
/Library/ControlCenter
h:
%s %s%s (0x%x)\n
saved escrow bag to %s\n
event-listen
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected escrow record pub key size%s\n
fv_set_protection,unbind
cap
LibCall_ACMSecSetBiometryAvailability
blob_encrypt
acl3_sign
migrate%s for keybag handle %d and manifest(length: %d) returned %s (%x)\n
failed %x\n
04fd10411852877f45cad486487c8114359bcfc212669f46bf70ec9f37cc29e523c93e9d6b5dca675caf5a8775fb24932ccdb761ceadfc10020efecc5f49e6061c
backoff[console,other]: %d, %d; 
ephemeralDataMode
ACMGetEnvironmentVariable
aks_load_bag
true
cmd_reference_sealed
direct
kAKSReturnSessionInvalid
locked
Command result = %d\n
type
AKSIdentitySetPrimary failed\n
%s: 
unlock with token should still fail on target\n
unwrapped key for %s:\n
aks_unload(escrow)
aks_assert_hold(no timeout)
cmd_set_volume_persona
Save unwrapped key at %s\n
escrow_password
  -s    Show analytics summary\n
Test 3: When device is locked and grace period has passed - you shouldn't be able to create/read/write a file until grace period (10s) ends.\n
ConfigFlags = %lld (
, 
gid col succeeded unexpectedly
Need to pass handle
verifying: pub_len: %zu, nonce_len: %zu, sig_len: %zu\n
aks_system_key_exi
token
04642aa30145b032642e90c6093a7437d982a78e32bd45eb0f2ade62c26ee028fb7e21594a902f7058cf4ba7faab9c4be948d1e33524f84bb0a0ca91fb65e95acf
volume-backup-test
akstest_unwrap_ek
ephemeral-policy(kext side expiration)
backoff %llu falls within range of %d\n
Backup handle = %d. Old style backup\n
Use escrow\n
fv-unwrap-vek
aks_recover_with_escrow_bag(remove passcode)
 unlocked: %llus\n
Enabling backup for volume %s, with password %s, to bag %s.\n
persistent.last_unlock_timestamp: %llu\n
ccec_verify failed
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_system_key_get_public failed: %d%s\n
LibCall_BuildCommand
lock succeeded\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s supported verbs: list, verify, kek-stash-load, transfer, remove, change, last, sidp, kek-stash-create, kek-stash-commit%s\n
aks_fv_get_last_known_gp_state %s\n
/Library/Backup
acl5_create
/sep-firmware.img4
unlock in progress
%s:%spid:%d,%s:%s%s%s%s%s%u:%s icloud recovery key%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s user uuid unexpectedly match new kek uuid%s\n
\t-k <kek_blob>
    PKI token unlocks: %u\n
2-6h
%s:%spid:%d,%s:%s%s%s%s%s%u:%s gid match failed %d %d %d%s\n
aks_remote_session_step()@%d expect:0, got:%x\n
[<escrow_file> [<escrow_password>]]
AKSGetAnalyticsInternal() failed
CX
aks_system_key_oik
Print backup bag uuid for persona volume <uuid>
_bind_unmanaged_vek
decrypted
Could not load wrapped data file %s\n
keybag not found
pka attest intermediate key
kSKSReturnBusy
memento-blob-failed-unlock-attempts: %u\n
dacl
AKSIdentityCreate failed\n
open
sym_create
done
load_keybag from file %s succeeded\n
modify-peer
continuity-peer %s: success (secret regenerated)\n
kAKSReturnNoPermission
i20@?0i8^{regress_item=[32C][168C]ii}12
volatile_state.current_state: %u\n
fv-new-vek
, has filevault recovery blob
sbt
set-failed
Historical Data:
%s:%spid:%d,%s:%s%s%s%s%s%u:%s acm failed%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s string fail%s\n
icloud recovery key
unmanaged-system-wrapped
flags: %s (0x%x)\n
internal: 0x%x sub_type: %d\n
reference-keys subcommands:\n
%d: ERROR: failed with %x and expected %x to wrap class: %d\n
u:h:
set system succeeded %d\n
passcode validated
never been unlocked
unlock_token_not_available
sbiv
assertion timedout
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Warning: AppleKeyStoreTest kext not loaded. Unable to run persona class D key tests%s\n
peer_state.flags: !peer_is_originator\n
aks_remote_session(DEVICE_AUTHENTICATION_UNLOCK_WITH_ESCROW)@%d expect:0, got:%x)\n
compute_key ec_p384
import pfk(kext side)
cmd_set_system
persistent.current_day.session_count[UNLOCKED]: %u\n
aks_remote_session(|DEVICE_AUTHENTICATION_ESCROW)@%d expect:0, got:%x)\n
%d: aks_unwrap_keys... with original passcode\n
<1m
persistent.recent_sessions[LOCKED]:
Test 1: When device is locked - you should be able to open file descriptor to a new file and write to it - but once the descriptor is closed - you shouldn't be able to read/write to it.\n
error: state locked\n
HasPKA
is-owner
usage: ltk-decode <blob>\n
peer_state.flags: !peer_is_registered\n
AppleKeyStoreTest
AppleKeyStoreTest connection OK
/Library/Logs/CrashReporter
test_fv
dkk
getConfiguration(
/MobileSoftwareUpdate
/Library/UserConfigurationProfiles
pchkpke
acl3_wrap
aks_event_test2
Could not get backup uuid for handle %d, result = %d (%s)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s please set the passcode -p%s\n
recovery blob 10m target iterations: %llu\n
Oct 13 2026
get keybag lock state
%s/%s/%s
test
aks_assert_hold(undefined)
b00dd00b
failed to validate passcode for handle %d (%x)\n
persistent.previous_day.unlocks_from_assert: %u\n
failed to get configuration: 
mediaKeyUseCount
crypto_generateKeyFromSharedInfo_version1
acl2_encrypt
eh:p:
kSKSReturnUnrecoverable
dump internal state to syslog (privileged)
volume-unmap
failed to fetch vek blob
oskc2
prp
sik mismsatch
rdisk
kSKSReturnBadData
inactivityWindowSeconds
recovery list: {
pka_p384_set_class
  -S    Show stash stats\n
%d: aks_unwrap_keys... old generation with original passcode (class 12 should fail with e00002bc)\n
usage: -r (reboot)
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to get blob state%s\n
akstest_new_key
Using secret %s\n
failed to lock bag: %x\n
ec_ecies_decrypt
acl4_attest_verify
/mobile
ACMCredential - ACMCredentialDataPasscodeValidated2
ACMCredential - ACMCredentialDataBiometryMatchAttempted
ACMRequirementGetSubrequirements
unlock bag (will arm peer after register)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s key_type_asym_ed25519 failed: %s%s\n
failed to decode blob: 
failed with error: 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s booted from uuid is already set%s\n
aks_assert_hold(timeout)
importing pub:
-f
get backup handle for handle
test-persona
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get bsd name for media object%s\n
unlock_token_passcode_changed
xart_id_sdak
change in progress: %s\n
set-healthy: 0x%x\n
acm_mem_alloc_info
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys disable%s\n
invalid handle %s\n
uik col succeeded unexpectedly
cmd_lower_iteration_count
yukone_uik_attestation
valid args: -t 'only enable tracing bit', \n
test-syncbag
rtkit
** end session list
orig passcode
key_type_hidden_asym
dg:h:r:t:
error: unknown aks_sealed_hashes_set error: %#x\n
check-s-key for keybag handle %d returned %d (%x)\n
Loaded vek blob from %s, %zu bytes\n
Internal
Inactivity window: 
mmap
signing key (aku):\n
acl4 testing
042f5f5781360c93d71dadb5dc9b5c11ad6cb8f99fb22e9c3e1dbb3e12fdd99138f398bf758088c4663192168618c36d8bbb4ae06bd566799bf32fc73a3ad7694dc8382becc42ea34600dd2abc8586c9f788973aa558c428c159dcab49779fc7ae
aks_fv_sidp_status %s\n
DEVICE_AUTHENTICATION_ESCROW
xart_id_tracker
<data>
Bbish:
standalone
/containers
failed to get internal info for lock time: 
negative test failed with %x\n
adh:mrv
Create ACM cred 2
  [%d]: %u\n
kSKSReturnNotReady
primaryGroupUUID
ec_p256_wrap
048db72ca4e7f2acfcfc1174a966c99db5bf5880464d9ab5d7208c5986fba033b2a0569478dc22594a1f8306fc035393e075944b34a14d264d395470ac93d3ce47
ACMRequirement - ACMRequirementDataAccessGroups
export_keybag to file %s succeeded\n
attest_sign
create sync keybag for target=%d succeeded\n
aks_se_get_reset_sig() failed -> 0x%x\n
usage: keystorectl continuity-peer <subcommand> [options]\n\nsubcommands:\n  modify-peer     - modify peer secret and optionally status\n                    for key peers (-k 1): regenerate secret, recalculate KCV,\n                      op
%s:%spid:%d,%s:%s%s%s%s%s%u:%s drop_handle -> 0x%x\n%s\n
=== Analytics Raw Dump ===
/Library/MediaStream
kb cmk slot
    pdk is present: %s\n
persistent.previous_day.unlocks_normal: %u\n
system-with-passcode
ready
ro
ACMCredential - ACMCredentialDataBiometryMatched
something aint right %d,%d\n
validate LTKs\n
    Normal unlocks: %u\n
kSKSReturnNoSpace
<filename> [handle]
user_enabled
expired
sac
%d: aks_unwrap_keys... new generation\n
success!
0497d96db825ab3624e27a5aa1ad759374ed720657d6667d68ae484192ce24b3e92c76220511d267a7453fdbda2b06a3f0a6e7035273f040d26542d3b3c23207bf0b4641e0a2a90910a666f70282da9a4fbac9519bf86c5608142dd999a1f664c4
046073817f64d31798f7efec68c74f90c12c3f49ecc870fad2048ed478b1da91b893d144ec144b8e66b6dcaaf5ac5f8494fdae73742f276831ee194677e4a7a3127d48df3d4232b9a901f8cd8326215824848002913b576cb5229644ab316f52f9
fv-new-kek
com.apple.foo2
%s:%spid:%d,%s:%s%s%s%s%s%u:%s key_type_asym_ec_p256 failed: %s%s\n
%02X
commit
persistent.current_day.total_unlocks: %u\n
e-apfs
CFDataRef localSecCertificateCopyData(SecCertificateRef)
04114432270050b02472a747ffe2ac727ac38794b0c7e30100a8b083f3033629650755ab32eddec541c4714701b97b8bf667345494f775ecf6ee00efef1aa45cb8
uuid_only
escrow-create
unwrap a backup item
volume-cookie
ses
testing assert type: %d\n
aks_assert_hold
keybag created with password: %s\n
\t-u <uuid>
No flags set (0x%X)
fv recovery
dak collection succeeded unexpectedly
2,3 uik committed/proposed validation failed. automatic_bump: %d, keys_equal: %d
persistent.current_day.unlocks_pki: %u\n
keybag: %s %p %lu\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kACMPolicyBootPolicy: %d, policySatisfied: %s%s\n
kAKSReturnACMError
odel
unlockWithEscrow
ACMRequirement - ACMRequirementDataRatchet
ACMGlobalContextCredentialGetProperty
system keys test success!\n
aks_system_key_operation_obliterate
persistent.recent_sessions_index[UNLOCKED]: %u\n
keybag.kb
get-lock-state
aks_remote_session(%x)@%d expect:0, got:%x\n
confirm unlock successful\n
  Unlocked: No data
signature verified successfully
pwers
aks_create_bag
aks_get_system
wrong passcode
valid options (-p <passphrase>, -h # (handle)\n--grace-period <value>\n--back-off <value>\n--max-unlock-attempts <value>\n--escrow-passcode-period <value>\n--escrow-token-period <value>\n--user-uuid <value>\n--kek <value>\n--reboot [on|off]
fv-test
%i .. session id: %i
LibSerialization.c
aks_create_bag(device)
checked failed attempts
unexpectedly succeeded to verify attestation (proposed)
/Library/mad
createAuthorization
error: aks_create_bag failed\n
AKSIdentityChangePasscode failed\n
ephemeral data mode
pass sm ps slots:
enabled
Could not load input file %s, result = %d (%s)\n
%*s.. setting persist on an active token\n
sks-log-filter
aks_set_system(device)
consumed last ARTM otut
save bag to: bag-with-escrow-record-removed\n
blob_set_class
persistent.current_day.total_locks: %u\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s chip_id: %x, ecid: %llx%s\n
memento-supported: %s\n
get-dcrt
last known good
%s:%spid:%d,%s:%s%s%s%s%s%u:%s missing nonce %d%s\n
04c2c95534f6d2aa9eece6f03ce4400f357dc5bd1a469e8e07b87ab52a7b91ece6981c53b1678db253db0685be467179acb63212b6435757d791f36d169da072c7a78a07be20d984471cf25aadc9c8ab706269a86718aec9a790457665a27c0d6f
max attempts: %llu\n
current backoff: %llu\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Truncated path %s%s\n
failed-unlock-attempts[console,other]: %d, %d; 
peer records dirty
acm_check
>12h
oneness automatic mode: %s\n
kAKSBackgroundPoliciesInvalidated
has-ref-count
boot-policy
/root
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
handle %d's se reset sig: 
<UNKNOWN>
verified
EscrowPasscodePeriod
xart_id_keybag
meb8m10m
aks_unload_bag
done.\n
read bytes: %zu\n
%s: %s: context = %p.\n
nonces match!
compute_key curve25519 class f
sik public key:
register backup bag, unregister if only handle
%s:%spid:%d,%s:%s%s%s%s%s%u:%s sep specific tests%s\n
LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
wrapped.csk
oke
sllt
unknown option '%c'\n
EC1C2AD9-B618-4ED6-BD8D-50F361C27507
Backup uuid for handle %d = %s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get C string for name%s\n
mobile
LibCall_ACMSEPControl
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n
lastPasscodeAuth
\t-o <param options>
Failed to create/open file
Lockdown mode enabled: 
%d: Changing to alt passcode...\n
Day #%u Statistics:\n
Could not load backup bag
cmd_regress_user_uuid
ACMContextGetDataEx
pka_p384_sign_verify
sep-debug-args
failed to parse uuid\n
persistent.current_day.assertdelay_entries: %u\n
extended state: %s (%d)\n
get_volume_uuid
%d: ERROR: failed to unlock keybag...\n
ERROR: -r (force-group-seed-roll) is only supported with bag-style unlock\n
requires sizeof(T) bytes
persistent.previous_day.unlocks_by_hour:
load key
refcount: %d 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to verify secret %s (us: %llu)%s\n
/backup
2 arguments required
continuity-peer
skck
os
preV5BagsDisallowed
wipe id not found in dict
Invalid handle '%s'\n
recycle vnode\n
lock keybag [-d (device) -n (now)]
%s:%spid:%d,%s:%s%s%s%s%s%u:%s UhOh! - PBKDF2 calibration maxxed out%s\n
kSKSReturnIPCError
keybag-uuid
ire
ACMContextVerifyPolicy
memento-blob-se-slot: %u\n
change secret failed: %x\n
Incorrect passcode. Please provide the right passcode.\n
assertion_set
payload not found in dict
sik collection: 
si
aks_remote_session_authentication_setup_test
%d seconds locked (%llu), cx seconds remaining (%llu)\n
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
aks_wrap_key(ak)
swtag
BSD Name
Writing KEK to %s\n
%s maps to invalid type, consult with system_key_string_to_type()\n
meb6m8m
pcmks
acl
o
persistent.recent_sessions_index[LOCKED]: %u\n
%s: mode=%o, u/g=%i:%i class=%i%s\n
04d7598478b1d0dbf952b2978d0d39a638e7f994dbd3570ecd3681bbc547d1e5dcb44975b9ea1f5b2339067f88b0e765cf84d7031512a9d28fb670f33e9acb47a3
decode_extended_header_blob
/logs/BurnIn
createdTimestamp
kAKSReturnSMDKError
Run regression tests
aks_kext_set_options
doesnt support rm
decode_escrow_record
rko
success deleting xart leak for %s\n
Current Day:
failed to get blob state\n
OtherGeneration
loaded
test_classB
kAKSReturnTrySeEnroll
** end peer list
valid options -B, -b, -s, -h #,-i, [password] (session,handle,info)\n
create: 0x%x\n
satori_ecies_verify
vek
, group seed
ACMContextCreateWithFlags
failed to import public key
InactivityRebootEnabled
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c
aks_save_bag(escrow)
on
HardwarePlatform
ACMCredential - ACMCredentialDataSecureIntent
satori_p256_delete_1
ota-test
DEV
memento-blob-max-unlock-attempts: %u\n
Util_SafeDeallocParameters
yes
pka_ecies_encrypt
acl2_create
acl2_delete
%d: rewrap all keys to new generation...\n
ga: verify
/Library/adi
-apfs_shared_datavolume
aks_assert_hold(mix and match)
sks heap stats:
pka_p384_encrypt
DEVICE_AUTHENTICATION_CREATE_AUTHORIZATION
ss
AKSIdentityListForVolume failed\n
pinfo
LibCall_ACMKernelControl_Block
aks_oneness_heartbeat %s -> (%s)\n
destroy-s-key
failed to sign (type:%d, gen:%d) = 0x%x\n
persistent.recent_sessions_filled[UNLOCKED]: %d\n
sys_enabled
i16@?0^v8
v5 restricted
uik attestation (p384)
DEVICE_AUTHENTICATION_REGISTER
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n
ecdhs
%s: %s: operation = %p, operationLength = %zu.\n
aks_system_key_generation_proposed
v24@?0@\"NSArray\"8@\"NSError\"16
failedUnlockAttempts
pcsbm
perform unlock with escrow secret to arm the token!\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeGetUnlockRecord: %s\n%s\n
SESSION_STATE_INIT
read is not aes aligned! (%zu)\n
pka_p256_encrypt
Failed to set backup bag: %x
for sep tracing set boot-arg sep_tracing=1 and reboot (requires DEBUG firmware)
failed to parse regkey blob\n
   backup bag count = %u\n
unlocked escrow bag
oc
perform DEVICE_AUTHENTICATION_REGISTER - verify registration & prepare for arming\n
aks_generation(%d) failed: %d\n
stash_verify
feature
cmd_sik_block_invoke
volume-backup-disable
fv_new_kek,device,external
Creating kek
event4: %s (0x%x), dict: %p, count: %d\n
_ipc_msg_protect
somewhere on mars
LibCall_ACMContexAddCredentialWithScope
LibCall_ACMSecContextCopyCredentialsArrayEx
Sync
acl2 testing
check_xart_lockers
 Recent Session Standard Deviation:
system-key
aks_unload(backup)
aks-log-filter
kAKSReturnInvalidSeed
keystorectl/keystorectl.swift
LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
acm_check_touch
check credential is present\n
pka_ecies_decrypt
no options specified\n
skni
ccgcm_finalize
test_keybag_persona_list
test volume keybag mapping
   device bag count = %u\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s ipc digest failed%s\n
s
pls specify <src> <dst>\n
drain backup keys to file
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Error: keybag_persona_list() failed%s\n
LibSer_ACMDeserializeEnvironmentVariableType
%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mis-match during load%s\n
Could not get backup handle for handle %d, result = %d (%s)\n
  Unlocked: %llu.%02llu minutes\n
shared-data-volume
generation
get-config
un
verifying lack of credential\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeListUUIDsOfUnlockRecords failed%s\n
kb  mk slot
/private/var/mobile
cant operate (%s, %s): = 0x%x\n
check-s-key
trying to take a oneness assertion\n
usage: keystorectl sidp <subcommand>\n\nsubcommands:\n  delete      - delete all SMDK blobs and force recovery\n  init        - reload SIDP state from disk\n  status      - check if SIDP is initialized\n  obliterate  - obliterate SIDP state
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to find username%s\n
ovk
fv_decrypt_vek
unexpectedly succeeded to sign with CIK
absinthe wrapped key(kext side)
serial
backup-staat-klaar
Can't see user uuid more than once\n
unregistered 5
Getting keybag uuid for handle %d\n
handle: %d, type: %d, timeout: %llu, drop: %s\n
/Library/CallHistoryDB
event1: 0x%x, dict: %p\n
/db/com.apple.xpc.launchd
tag
ACMLib
public_key = 
gidp
reset-peers
usage: create [-h handle] [-c key-class] [-t type]
aks_create_escrow_blob
ACMContextGetExternalForm
LibCall_ACMContextVerifyPolicyEx
%s: %s (len=%u): operation:
pka_p256_delete
/Library/DeviceRegistry
LibCall_ACMGlobalContextVerifyPolicyEx
enabling stash
kv
test keys enabled: %s\n
%d: removing passcode!\n
/logs/AppleSupport
akstest_last_user
 error => %@ 
sr
AKS_MIGRATE_FILE 
your device is locked out, recovery not possible\n
currently in a backoff sleeping for %lld seconds\n
/sbin/umount
CLASS B
ACMContextRemoveCredentialsByType
handle: %d, current state: %d\n
%d: aks_wrap_keys... while locked\n
got drained key (volume:%s, bag:%s, inode: %llu, rev: %u, type: %u, mode: %u, size: %u)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_get_icsc_srp result: %d%s\n
transfer ownership: %s\n
EBC6C064-0000-11AA-AA11-00306543ECAC
error
/Documents/Pearl
get-measurement
requires input divisble by sizeof(T)
   high water mark = %u\n
aks_apfs_container_disk_for_physical_device
DEVICE_AUTHENTICATION_RESET_ESCROW
%s:%spid:%d,%s:%s%s%s%s%s%u:%s only supports: -s%s\n
wrapped key:
sb
unable to create refkey\n
cache flow
loading as handle: %d
   locked: %llus\n
%*s.. lock/unlock test\n
no passcode set
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n
skos
escrow blobs begin
xart_id_cs
ed_validate_key
042f598ba5d759552c3e45c357949dc6d4fa0bdc495648f7ece7bebe09d61de1702e3f60e8d1b9cd41e944f294ab16e5a74c914c6f94adf7849efc1e2b86396a6b
dump-file
Protocol Characteristics
cd_hash
acl1_delete
dead
%s: %s: constraintState = %p.\n
rachet_locked
Testing backup for volume %s\n
jqvw
dak committed/proposed validation failed. static_dak: %d, daks_equal: %d
kAKSReturnInternalError
failed with %x\n
gid attestation
, has auto recovery blob
acm_mem_free_info
aclRequiresPasscodeInternal
Measuring aks_get_device_state() perf
}
%s: %s\n
  [%02d]: %u\n
04c0b0ca571e34fa0635d2ba32614f2ee0599a0d6d67bd2bfcca4d2d35195755a87fcb65e37e4f9ad0d6473346c6c8392c45477ca1a7ee8953c8e494e830faf7fb8361499f154693b6f624bec2ca3a7cd0b838f57942c377c32f2c033b17145659
export keybag
, se entangled
ACMCredential - ACMCredentialDataAP
usage: attest -r ref-key-blob [-d] [-t attestation authority] [-h refkeyhandle] [-g system key generation]
drained %zu keys\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeSetUnlockRecord: %s%s\n
DK
xart_id_memento_expiry_state
XARTPolicy
%s:%spid:%d,%s:%s%s%s%s%s%u:%s acm set failed%s\n
04f65385f4f6c4b56688baec350bffba5da183f701136cdfbf6a8b9aefb34614cafa4baa9039ffb7a066992815339787d0142dfa5ae0378389fab8ebdf47f1609536a754f8a3bdb61ee1570e94d9a34adb8a5053ff5f2473d016eeac738b23be43
Unwrapped backup bag in userland.\n
aks_apfs_preboot_disk
unexpeted lack of credential in the acmref\n
loaded primary user to %d. Please use primary user's passcode for recovery\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s sorry, one beacon per customer%s\n
aks_fv_apfs_get_blob_by_uuid
fv_rewrap_kek
pd
0488cf0085a4deaeae1b6160840b0d83261fd7bbfd43de6d018255099e0629ae35369b166ae9d5f8ae50d452e2a8aed89da975fb10700594c9f275ef0e385f60192a23a4df2133c62599e80a91a495326d5aa85028542da34c6311677f5e7bcd96
LibCall_ACMContextUnloadToImage
processAclInternal
change is pending: %s\n
pka_p256_verify
kAKSReturnIOError
aks_system_key_sek
unlocked since boot
%s:%spid:%d,%s:%s%s%s%s%s%u:%s drop(uid=0) -> 0x%x\n%s\n
1-5m
acl3_encrypt
loaded bag data from file %s succeeded\n
F
assertion set: %s\n
[handle [secret]]
ouw
LibCall_ACMContextCreate
lock_state
eh:g:k:m:
key_type_asym_curve25519_wrap
congrats, you managed to delete gid, wait, what?
off
key error
/logs
loaded cookie from file %s, (len=%zd)\n
assert tests (multi-threaded)
,2 dak committed/proposed validation failed. automatic_bump: %d, daks_equal: %d
cmd_se_delete_rt
sidp %s: failed -> 0x%x\n
WARN: make sure to delete the token using 'keystorectl fv-delete-verifier %s' command to avoid xART resource leaks\n
persistent.previous_day.session_sum[UNLOCKED]: %u\n
KAKSReturnUnrecoverable
aks_unwrap_key
/Library/MobileInstallation
ssst
Class getFBSSystemServiceClass(void)_block_invoke
%*s.. commit during lock\n
pub2_len:%zd != pub3_len:%zd
aks_system_key_dcik
BoardId
Getting volume cookie for handle %d, persona %s\n
drop-memento-secret: 0x%x\n
key: %s %p %lu\n
Restricted
reset passcode with escrow
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n
ACMRequirement - ACMRequirementDataSecureIntent
ACMContextReplacePassphraseCredentialsWithScope
test last user (kext side)
p:
043b567d70625125e925a869be7547dc9d32e89c3f272b9653a0b7df6a37964970e13e8f6acc4be4777979738fa7b2244056d89e39a3da364734c14da1c76ae7a9efb369ee1083cf2bdfec27a88a51880218a9c96d14254283417076288736d9dc
%s: %s: requirePasscode = %p.\n
se-slot-version: v%d\n
04da5ad79948894f123dfa5ee25abbd5b72018c146ee16a5160f8d8342cd675afa247e584127a1dbae2f6a53642534e22374f947a5aaf3b69e006e916b459df496
remote-session-key-set
  Median Unlocked: No data
aks_fv_new_kek
sms
Util_CreateRequirement
DAK committed
sig: 
using scrt: %s\n
last-mesa-unlock
0
drop-secret
04d2eb1b83d390fbc75593037c80f3481aa93cf81a1ee5c7fd5d39d197472d2bc36109afd0c95c5a7ccdc8b5f7e602b428897802cae242fc2f2b4ea47e1aa1f359
_MKBWIPEID
04b442a2ba16adba781f9429660f48e534a0d3fb82b6d487b87dd2c93117c07a2c46c4d68d5626d2d1b34c79d5a2a5878a1d8aa1237bb92931d6635beabe500616250aec58d3e40e033d991fb72e2490c445ef694c645442d87795b26594102bb5
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_change_secret_epilogue-> %x%s\n
044b1079dccbf83fdd85d5fdf7c18ce493d1f4a014f98b8ddc44f463a8a646d3ce86963d8b09079c996edc9750e22877048a8e201ee2edd367895cb80ab2fd33b0cdc3616e1f97fcc1cf9cc73c0a807dc8868c4c4c533c67de05e87a0dfe90f9c6
prederived create
  * uid: %u, uuid: %s\n
1-2h
    No data
cmd_is_class_a_available
kSKSReturnNotCapable
aks_system_key_aik
pms
has-vek-protected-volume-bag
failed to get blobs\n
device bag migrated
gk cached once
ec_ecies_verify
persistent.current_day.unlocks_biometric: %u\n
classM
src || !srcLen
aks_create_bag(escrow, with auth)
is_key
dbh
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
\theap size:      %llu\n
aks_ref_key_ecies_decrypt failed 0x%x\n
acl3_create
unlock_public_bag
%s: %s: called.\n
ltk-decode
/Library/terminus
secondsSinceLock
aks_lock_device
Usage: %s analytics [-s] [-d] [-S] [-k] [-h]\n
alt_regress_passcode
aks_wrap_key failed, result = %d (%s)\n
load escrow bag
%s/mobile
[[-f file] [-h handle] [-p secret]] <manifest|img4object>
unlock_token_passcode_required
/wireless
sbo
unregistered 4
/dev/
kSKSReturnBadSignature
fv_encode_vek_blob
aks_create_bag(escrow, inapt auth)
sm slots
failed to write restore bag to disk %s\n
peer_state.flags: peer_is_originator\n
kSKSReturnSEPolicyError
B16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_enable_cache_flow result: %d%s\n
0452777bb4d2ef5bab309e5725036267f11f04b26444889e3484a94770c8010b7aa1730c8fa4381a734a817fb5ed3a660df22ece3ec5e92c042a9eca4499cba5afe75cb9e0ee847f74ab7789fb748064b0c7772020ad582330a2f11323fbd15e20
get-option failed\n
ps-missing
no action specified!
failed to allocate read_buf!\n
v28@?0i8r^v12Q20
  -c class:   key class (e.g., AK, CK, DK, AKU etc.)
kAKSReturnBadData
failed to retrieve blob state\n
LibCall_ACMGetAclAuthMethod_Block
ACMContextCreateWithExternalForm
Can't find EffaceableStorage kext!
aks_remote_session_token()@%d expect:0, got:%x\n
xart_id_fairplay
AKSIdentityListRecoveryUsersForVolume failed\n
pka_p256_sign_verify
  -k    Show keybag stats\n
acl4_delete
aks_remote_session(DEVICE_AUTHENTICATION_RESET_ESCROW)@%d expect:0, got:%x)\n
key_type_asym_pka_p384
set cx window %s -> (%s)\n
<subcmd> -p <ltk-hex> -k <0|1> [-H handle]
%d: aks_unwrap_keys... with no passcode\n
--predicate
045802cf78fc60eda23f88c0adee7afa56454a14280b4b8532245f2251d484f3ff0abd1e2146deee7ed5b7bba30fffd4155f3fe6f6f68801df294c4e482734f837
042c9361dafd065ade333644f68e09592d718e165ae2d8622b316bd4586f8f3833df89da423a5d845ebb1c04af7918beb6a1c26e6e48adf79a33c48c6e46f2fc45
akstest_unwrap_key
aks_unlock_device
ERROR: did not update password appropriately
sig:
042f5129d5e7417b76f7bb7dc1bf3be4f18045f367a0bcce1fe48b836659c325735243775cb4d0a95af20c30c3e5f0a8d632fcdaf79d3d2a3f9ff4c1e04ac55985
kt
; 
blob_init
%*s.. setting persist on a non-active token\n
originator, 
aks_change_secret
acl4_attest
kSKSReturnNotFound
regress-user-uuid
%d: change is pending: %s\n
Writing VEK key to %s\n
%s: %s: returning, err = %ld.\n
Test 2:  When device is unlocked - you should be able to open file descriptor to a new file and write to it - and should still be able to read/write to it when the device is locked (with the descriptor still open) - but shouldn't able to re
xart_id_platform_config
    Assert delay entries: %u\n
Delete persona
volume-map
Unable to find class %s
xart_id_keybag_stash
) failed with error 
ACMRequirement - ACMRequirementDataPushButton
ACMHandleWithPayload
EscrowBag
iv
create data protected file of the specified class
  Locked: %llu.%02llu minutes\n
compute_key pka_p256
Multiple Day Data (derived from recent %u unlocked and %u locked session samples)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid type%s\n
, (%s)
%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n
Encryption Type
oiko
ad
ed_verify
    From assert delay: %u\n
, not recoverable
SecCertificateCopyData
fstat
validate sik pub
kSKSReturnSMDKError
xart_id_pass_sm
ACMGetAclAuthMethod
041b4c86c171c3487d1c4ac94f5c1e52a78d2d35042d2048a7be390f7298582ab1149a604fd3f4ec9230a9af8e765073ad91bc5c5712f13fe47ab2a8e9c00d6e47
aks_fv_stash_kek_with_secret: %d\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get C string%s\n
pgu
pdpi
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to get dcrt%s\n
<group_uuid>
%s%s\n
acl5_delete
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_fv_unwrap_vek_with_opts(aks_fv_unwrap_vek_opts_use_stashed_kek) = %d%s\n
cchkdf
acl3_set_class
aks_se_get_reset_pubkey() failed -> 0x%x\n
Failed to get data protection class for given path %s with errno %s (%d)\n
sm
pad
Usage: kc-unwrap -k <hex_wrapped_key> -c <class> [-h <handle>]
yukone_key_a_attestation
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fstatfs error: %s\n%s\n
inactivity reboot is not enabled
LibCall_ACMTRMSaveState
peer_status: unlockstate (%d), unwrapped_escrowstate (%d), wrapped_escrowstate (%d)\n
satori_ecies_create
0x%x:%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
pkofn
FVWrapping
Loaded vek blob from %s, %zu bytes
Free Blocks:%lld blocks of size:%d\n
primary group uuid
, se healthy
perform unlock with escrow secret\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to set nonce 0x%x%s\n
drop-aux-auth
unlock-with-sync-keybags
DEVICE_AUTHENTICATION_UNLOCK_WITH_ESCROW
/root/Library/Lockdown
xart_id_oik
sam
set-option failed\n
root
meb20m60m
lbl
false
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid value%s\n
kc-wrap
persistent.previous_day_valid: %d\n
persistent.previous_day.total_locks: %u\n
04a164dc59a2abb4f5231f13697a1e5160ad57126aebd7e7361b716c829fd723b0d04d34710e1a1b7f2bd072f02e94259d783b728f3a67a1108d8b186fe340bc7b
kSKSReturnBadArgument
fv_new_kek
cant retrieve pub
acl4_verify
decode_peer_info
%i  - operation: %s
slot%d: state: %s, failed-unlock-attempts: %d, run-time-state: %s\n
blob_wrap
lock
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c
C
%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n
lpu
attest_delete
  -c class:           key class (e.g., AK, CK, DKU etc.)
obliterate-really-please
Create persona
puu
deserializeParameters
escrow secret
SE
cx window
aks_unlock_device() -> 0x%x
%*s.. change passcode and transition through unlock/lock/unlock\n
h:ds:a:t:
Failed to load backup bag
bridgeOS
satori_ecies_options
persistent.previous_day.unlocks_continuity: %u\n
23:34:36
LibCall_ACMContextLoadFromImage
all done
create-file
LibCall_ACMContexRemoveCredentialsByTypeAndScope
acl4_set_class
key_class = %d\n
successful attestation of refkey using type:%s generation:%s\n
persistent.current_day_number: %u\n
persistent.current_day.unlocks_normal: %u\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to fetch vek blob%s\n
kSKSReturnTrySeEnroll
get-sig
  Median Locked: No data
missing sig, please use -S
fv-set-protection
ehks
allow tests keys
  Median Unlocked: %llu.%02llu minutes\n
apfs set: %d\n
secret: %s %p %lu\n
lt
%s: %s: returning.\n
%s: %s (len=%u): acl:
pls specify <src>\n
post-roll-keybag
unexpectedly succeeded to get CIK public key
delete-reset-token
cmd_fv_users
kSKSReturnNoMemory
drain-backup-keys
oska
key_type_asym_kyber768
M
) failed with error: 
LibCall_ACMGlobalContextCredentialGetProperty_Block
aks_verify_password
intermediate_create
kSKSReturnPolicyError
proposed
/.exclave
ogss
msg_cache_device_state_class_a_available
kSKSReturnBootedVolumeAlreadySet
0123456789abcdef
ACMCredential - ACMCredentialDataUserOutputDisplayed
cdgi:Llmp:P:stu:U:vx
force-no-create
%d: aks_unwrap_keys... locked\n
test-edu-mode
recovery slot fua cached
remove_kek
acmh
create-bag (empty passcode)
satori_ecies_decrypt
  Hourly Distribution:
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Not a Volume Object for %s%s\n
aks_kext_get_options
%d: ERROR: failed with %x to wrap class: %d -> %d\n
obliterate
5-15m
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options not supported%s\n
imported
mementoExpiryState
ACMRequirement - ACMRequirementDataSecureStateWithAttributes
ecies_t_decrypt
yukone_keybag
invalid hex public key '%s'\n
grace-period
%s:%spid:%d,%s:%s%s%s%s%s%u:%s platform_get_chip_id failed: %d%s\n
    secret is present: %s\n
amfi
/private/var/
PreHashedSecret
stash bag %s valid on disk\n
\t-c <command>
recovery blob iterations: %llu\n
global-assertion
[-j] | [-e] | [-f]
fv_set_protection,enable
processAclCommandInternal
len = %d\n
stash_enable
/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/keystorectl/cmd_system_key.c
InactivityRebootSet
AKSGetAnalyticsInternal
escrow-token-period
kAKSReturnNotFound
absinthe
create %d threads\n\n
aks_assert_hold(unlock NULL)
Writing VEK to %s\n
04bcd62fb223396d45a963114143ed1fbd8c8363b191b514b67c883279b77765d5911bc097ecfdd05fb6b1456af1a23a7cfa77be175fed50f55b896a19ec9feb1c
set-system
peer records flush
force-create
sym_encrypt
usage: %s stash [create|load|verify|destroy|commit|enable|persist|regress [-h handle] [-p passcode] [-m mode]\n
kAKSInactivityReboot
group: %s
passcodeChangeTime
DAK cert validation with scrt passed\n
bak
get-info
remote-session successful\n
success.
debug %d
load or unload an applekeystored test instance
/Managed Preferences
unit of work failed, precise reason is unavailable.
Cannot wait for pid: %s
 kcv: 
ephemeral
st
got config for %i\n
letmein
attest_verify
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s class A for (%s) available: %llu%s\n
04681011140b5f62c95058460b2ca65ef5e10107349e7b988cf9ba4b8c9aca50af9bd9c18eba37f7487106dddec3bf5f815d0f81d1d5fef18a61d6d3b1f14dce62b9bb48fe3c61e86d455c31ce1a21e386c30738bac931d6adb32b8bf59634569c
volume-backup-enable
fv_kek_global_policy_eval
/log
ec_p256_verify
%*s.. unlock/persist/lock\n
DeserializeVerifyAclConstraint
aks_assert_promote
run some random tests
backoff[console,other]: 
meb24h48h
BackupBag
sym_set_class
passcode
factory_data: %s\n
aks_sik_optional_params img4m_len: %zu; params_len: %zu\n
/Library/Fonts
mbe
oecd
-scanner_disabled
missing passcode\n
persistent.previous_day.unlocks_biometric: %u\n
/Library/Preferences
guid
ACMContextGetDataProperty
%s: %s: command = %u.\n
se nonce is set
perform remote authorize\n
key_type_hidden_sym
error result: %d\n
  * more_state: %s (0x%llx)\n
CommonUtil.c
delete
YES
--set requires an argument\n
akstest_new_ek
memcmp,vek,vek2
ACMRequirement - ACMRequirementDataPasscodeValidated
ex: keystorectl test 'random password'\n
event3: %s (0x%x), dict: %p, count: %d\n
tdm entry id: 0x%llx\n
current sep measurement
save_public_bag
    %s: %u\n
/Library/Voicemail
cmd_change_password
os_bound_sign
escrow-passcode-period
aks_assert_drop on %i (%x)\n
  0 days available
register-backup-bag
aks_absinthe_generate w/challenge result: %d\n
Loaded data from %s, len = %zu\n
group seed proposed
PasscodeServiceSlots() failed with error: 
ACMGlobalContextRemoveCredentialsByType
creating keybag...
primary user uuid
ec_p384_validate_key
 | 
lower-iteration-count
srcd
H:p:k:s:
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sresult: %d; oti: %d; passcode_reset: %d; of: 0x%x; nf: 0x%x%s\n
aks_verify_password noacm
load-keybag
aks_assert_hold(default timeout)
invalid type '%s'\n
aks_unwrap_key failed, result = %d (%s)\n
IOService
, xART policy is enforced
user
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to generate valid kek group uuid after 16 attempts%s\n
aks_encrypt(acl1)
check bag still locked\n
%*s.. updated to class: %d\n
generation state: %d, %s (%d)\n
UUID
pcdb
pdpt
kSKSReturnIOError
/root/Library/Preferences
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek failed to unwrap vek; mix-n-match?%s\n
foo
diagnostic info is captured in 
aks_decrypt(acl1)
%d: ERROR: failed with %x and expected %x to unwrap class: %d -> %d\n
persistent.previous_day.day_number: %u\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s interval returned: %llu%s\n
aks_system_key_fik
%s:%spid:%d,%s:%s%s%s%s%s%u:%s institutional recovery key%s\n
kSKSReturnInvalidSeed
WKU
aks_create_bag(escrow, valid auth)
047c84e7e694f75610bd2f5ae51c562dc47aea54237f2986b5033fe3878f5c4c8d56000c3b1bbed077e00c2fe83287123aa7b4caa1017f4cdc66b6cf55e520d7793dd423068c59f6a58211f03fe34b21875863f0352c24b53139c4903e11ff7e30
bak_verify_beacon
IODeviceTree:/filesystems
unlock with token should fail on target\n
acl4_sign
got rewrapped key (volume:%s, inode: %llu, rev: %u, type: %u, mode: %u size: %u)\n
%d: switching handles from %d to %d\n
stash_enabled
invalid dst class '%s'\n
uik bump failed
passcode changed
, stash unlocked
missing path to diagnostic\n
failed to verify attestation
blob_verify
os_bound_set_class
acl5_verify
eos
049c6ed789c842c4ab78e14a587f68872893549ca16ff3e4188d105213700a86cef70c90fbf56ccef73d3a68ce25f5f448ea0c72a14bc95bebe58a6bf51a8866e9032548e02a434185cbd3fe4a0b837c8489674e60438978b8cb3c8e3807ce387b
sesHat
Enable backup for personal volume <uuid>
ed_sign
ccecies_encrypt_gcm result: %d\n
set-healthy
load backup bag
persona-create
oskgp
ACMRequirement - ACMRequirementDataKofNWithAttributes
LibCall_ACMSecSetBuiltinBiometry
uik attestation
dst || !dstCapacity
ACMRequirementGetProperties
attest_set_class
, has memento blob
/Library/CrashReporter
os_bound_verify
invalidate keybag = %x\n
thread %i returned error\n
group seed
sleeping 11 seconds...
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unkonwn state %d%s\n
generate
04bd653aaa98ae3d119536feb2f4379401517a4982b663993d8d957a243bf463ae99eafa7d7042d6d2f58d2dd02738671b722e9349a4bc835f8f3317134d15f4a12e04e3f20810edc896c3856f7d65e52d258452d9cffa3dd4b3b8eab81a139bf9
operate on system keys
/Library/Trial
usage: keystorectl oneness [options] [handle]\n\nPerform oneness heartbeat or set up oneness assertion.\n\noptions:\n  -a              - set up oneness assertion (creates key bag, signing keys, peer setup)\n  -h <handle>     - lock device k
personal recovery key
/Library/SoftwareUpdate
invalid array count
LibCall_ACMKernelControl
sik col succeeded unexpectedly
persistent.current_day.unlocks_continuity: %u\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_bak_op_get_swizzler failed: %d%s\n
kSKSReturnInternalError
usage: %s [-q] [-v] [-w] <cmd>\n\nsupported commands:\n
ock
Use create-sync-keybag\n
pre-derived
/Library/AddressBook
fv_apfs_remove_blob
kext-has-test
Physical Interconnect Location
inactivityRebootEnabled
fv_get_blob_state,vek
id
unexpected token status 
cmd_test_ephemeral_policy
call to load
04810ff0e369786dda2a860652921d537c096d02c2cc54157e4dac96d0eb1d3e423ec0efb28ade13e0c907b3a79c0834a0a5add6a6474cf18947e4c64d6b66a921
satori_p256_create_1
/Library
meb72hinf
keybag version
current 24h window (ongoing):
gswt
sesu
bag state
new_password
x
LibCall.c
ref_key attest tests
aks_absinthe_collection w/random result: %d\n
,2 uik committed/proposed validation failed. automatic_bump: %d, keys_equal: %d
%s: %s: maxGlobalCredentialAge = %u.\n
fv_capabilities_set
Failed to save unwrapped data at %s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_remote_session(DEVICE_AUTHENTICATION_RESET_ESCROW)@%d expect:0, got:%x)%s\n
%s: %lld\n
type: %s (0x%x)\n
verbose: %d, quick: %d, pka: %d, sika: %d, sep: %d, dont_skip_bats_breakers: %d\n
AKS_MIGRATE_DIR 
  * event for %d\n
persistent.current_day.session_sum[LOCKED]: %u\n
decode_pfk_bulk_entry
export-keybag
%s:%spid:%d,%s:%s%s%s%s%s%u:%s verify failed %i%s\n
    ---
failed to get blobs
fv_create_pdk
AKSIdentityGetPrimary failed\n
migrate
regress-fs
04e777eaeac19300d7f43cbd5bbbb892e1384264cebbddee51c310865be145e0c347a167fd25a595eb48e55b69b049050a3659707fb136cd1040a79b4f824f8813bf2b35acbc6ecc5e065933aea572d3703f2466504fa2dcb602ea9337a30ee7cc
ERROR: unlock device with acm is unsupported\n
cant collect(%s, %s): = 0x%x\n
fv_new_vek,default
REQUIRE_func
Loaded backup bag from %s, len = %zu\n
aks_system_key_operation_commit
ACMContextCopyData
aks_set_system
xart_id_fv_implicit_cached_kek
bfu
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null KEK, file radar%s\n
dak pubs len mismatch %zd vs %zd
Hex dump of raw bytes:\n
kAKSReturnLibError
Unsupported version 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unsupported kek len: %zu (imported from CoreStorage?)%s\n
session_reset: 0x%x\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_bak_op_get_beacon failed: %d, flags=0x%hx%s\n
HasSEP
set-config
%s:%spid:%d,%s:%s%s%s%s%s%u:%s init failed %i%s\n
fv_new_vek,device,external
DAK cert validation with ucrt failed, checking scrt...\n
0494970def35a57bb5235222366df1d2f6f394c27fce15e3643deefec8768367ab0e27efd3a4cf6699acf325a0922dedb6b254262f97bab0ae92a327782f16d4ede32524cef2abdfa0a9896d1b5d32868486025cab84c9516ee786e2961771b6d4
create keybag succeeded\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s please specify a user with -U <uid> -u <uuid> -n <name>%s\n
decode_session_info
%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOServiceGetMatchingService failed to find %s%s\n
type: %s, 
ACMRequirement - ACMRequirementDataKeyRef
failed to get a handle back\n
%d: change in progress: %s\n
%d: aks_unwrap_keys... while locked\n
fv_set_protection,bind
validate failed: 0x%x\n
compute_key ec_p256
uik proposed col failed
new pfk(kext side)
 Recent Session Min/Max:
create-sync-keybag
guuid
mkey
aks_apfs_preboot_volume_path
uuuid
crypto_generateRandomSaltLazily
Tests for class A:\n
04e7d653946de333589fd1a4bdfee657cc54ef7896cfdb4f926b8927d07d8ce096be858ba37e83522db7a81c2f013bea7b815661abd6561c525a9fe3d587061b63
aks_fv_apfs_get_default_disk
kAKSReturnIPCDecode
checkCCError
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode kek%s\n
failure
set_nvram_with_opts
aks_system_key_bak
load keybag from file, and optionally make global as [handle].
oneness
\t-f <kek_blob_out_filename>
heap tracker start:
  -d    Show detailed dump\n
pub:
[<handle> [<escrow_file> [<escrow_password> [new_passcode]]]]
mkk
ACMRequirement - ACMRequirementDataPassphraseEntered
error: thread creation failed!\n
test volume keybag persona
aks_remote_session(DEVICE_AUTHENTICATION_UNLOCK_WITH_TOKEN)@%d expect:%x, got:%x)\n
invalidate sync keybags succeeded\n
run remote-unlock against self
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
future-bumped
aks_lock_bag()@%d expect:0, got:%x\n
cmd_cat
error: value cannot exceed 48 bytes\n
missing xart_id (-i id)\n
  Locks: %u, Unlocks: %u\n
persistent.previous_day.total_unlocks: %u\n
    Mean Unlocked: No data
cmd_drop_aux_auth
04af85e17f6d5151ee5519ee54e3289a8c8ffc01c39a88c21cff8cf54573783042b58b440fbb5a66f59b720c703e9feb786d41faca3663dae14ab0e309365fcc9d
WC protected
unload-keybag
%s:%spid:%d,%s:%s%s%s%s%s%u:%s non sep tests%s\n
failed-unlock-attempts[console,other]: 
meb0m2m
psst
key_type_sym
 (acm)
se-rm-support-is-set
oskc
ACMContextCredentialGetPropertyEx
error: aks_lock_device failed\n
unlock with escrow record should fail on target\n
blob_delete
effective:
state,type
lpa
etp
LibCall_ACMTRMLoadState_Block
set up v1 keys\n
pka_p256_wrap
error: aks_get_lock_state failed\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to find preboot volume for disk %s (%d:%s)%s\n
/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/ipc.c
%s:%spid:%d,%s:%s%s%s%s%s%u:%s vek_buf_size: %zu, kek_buf_size: %zu%s\n
success\n
sw_create
reset-stuff
skt
Using flags 0x%x\n
trying valid escrow secret\n
%d: ERROR: failed to set passcode...\n
Passcode not supplied.\n
attempting to load primary user for recovery\n
unable to recover, please restore your device from backup\n
recovery is not required\n
  Mean Locked: No data
verifying acmref arg requirement\n
unexpectedly succeeded to collect CIK
t
<subcmd>
Disable backup for persona volume <uuid>
%i  - local pub: (%i) 
vgsg
ACMContextRemoveCredentialsByTypeAndScope
HiddenKey
sym_delete
acl1_set_class
unlock_escrow
b:d:n:op:P:u:U:
fv_apfs_get_blobs
sepuid-bound
xart-policy
/usr/local/bin/keybagdTest
kSKSReturnLibError
failed to fetch vek blob\n
LibCall_ACMContextCredentialGetProperty
LibCall_ACMContextSetData
LibCall_ACMSecContextGetUnlockSecret
mapping volume %s to keybag %d, persona %s\n
insufficient args\n
sleeping for %ds\n
ed_wrap
040865f4e06e1bd2955d804335ea2072b5700398c2e5dad08f85ebd252cf5da6641b84a3ac21538f4203f9544a1777fe30a35a6cab808c683939491d118f7d2758f87bb723ee6913a6c06bc5a094c38315150444cfc0604f8ac7c3fe08036e32b8
042620c97898c20fe4bd26915ca90827da3573d1cf817303342025c52604e98cf256c4f046d4fe3d27534899cbbcd17e6a954e3e2c2a23e9cd81d08178cbbd6cfae0808116966412f3fc64eae9f80327c619ce3a199148ca05f68c682c3d1328a2
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid uuid length %zu%s\n
/Library/Caches/com.apple.xbs/D5DF64C7-7AB0-4EDA-A642-E9E1BEAFC1CA/TemporaryDirectory.cfNP0O/Sources/AppleKeyStore/msg.c
%s failed (%x)\n
se state: %s (%d)\n
AppleKeyStoreTest connection FAILED
init
%s:%spid:%d,%s:%s%s%s%s%s%u:%s swizzler set%s\n
blob exists
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get parent IO object for %d%s\n
, recovery required
Measuring aks_get_lock_state() perf
change
%s:%spid:%d,%s:%s%s%s%s%s%u:%s key_type_asym_ec_p384 failed: %s%s\n
aks_absinthe_collection result: %d\n
sep measurement
VEK unwrapped
wrap to session
_networkd
aks_get_internal_state
no-effaceable-storage
k:e:
acl5_attest_verify
persistent.current_day.day_number: %u\n
04d059d6c5be9aa104a1659eedb2d4ae6190f203d81337b7079dd8ebc8d517424afa63e7df368ee62b90041ae71d84d92e94b03204dfe47a58b7c56f94e0f13ffe
%s:%spid:%d,%s:%s%s%s%s%s%u:%s skipping: not apfs%s\n
failed to get lock state: 
thread %d sleep %d seconds\n
cant retrieve DAK pub\n
%d: ERROR: failed with %x to unwrap class: %d -> %d\n
uik deletion failed
flushing apfs crypto cache for '%s'\n
volatile_state.loaded: %d\n
Cannot wait for %s: %s\n
fv-delete-verifier
h:p:f
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bak_verify_beacon failed: %d%s\n
mount_apfs
kAKSReturnInvalidPersona
aks_system_key_haven
getLengthOfParameters
ccrng
escrow
satori_p256_sign_1
attempting to unlock with NULL passcode\n
Device is locked: yes
ckon
LibCall_ACMContextCopyData
regress_passcode
%d: aks_unwrap_keys... with alt passcode\n
current user doesn't have a filevault recovery blob\n
passcode (again): 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s please specify a user with -U <uid> -u <uuid> -n <name> or pass in a hex blob with -b%s\n
xart_id_dak
pct
ocww
missing old passcode (-P)\n
transfer
/usr/bin/trace -i
unsupported subcommand %s\n
kAKSReturnBadPassword
[-f filename] [-h special handle] [-n] [-p passcode] [-s] [-t <keybag type>] [-x]
aks_wrap_key(akpu)
old new uids cant be same
user-uuid
change password: %s\n
rs
EscrowTokenPeriod
invalid src class '%s'\n
E
AppleKeyStore
_cmd_stash_kek
%s:%spid:%d,%s:%s%s%s%s%s%u:%s doing aks_change_secret_epilogue()%s\n
   escrow bag count = %u\n
persist
kAKSReturnDecodeError
/root/Library/MobileContainerManager
/Library/DataAccess
dump_bytes_internal
puers
aks
get-uuid failed: %x\n
%d: attempt to rewrap akpu keys\n
missing mountpoint\n
sidp %s: not ready/initialized\n
PS protected
username: %s (%d) is %sadmin\n
/root/Library
rk_create_with_encrypt (key_type_sym)
this is some shared info
volatile_state.previous_state: %u\n
persistent.previous_day.assertdelay_entries: %u\n
045fc43567ec2ba1dd0aa76af17e2b5f5a244663b91c6618e408833d16ed8c3b2a1a442148ed099890b179e9bb5d4ac9e420f847bce03c96eee0985bae96a49c79
InactivityRebootPendingDisable
kAKSReturnUnsupported
failed attempts: %d\n
read failed!\nerror code = %d\n
escrow-reset
, xART policy is cached
/log/com.apple.xpc.launchd
meb4m6m
ssukp
crypto_deriveKeyAndDecryptData
fv_decode_kek_blob_opts
aks_recover_with_escrow_bag(change passcode)
ec_p256_set_class
os_bound_delete
%d: aks_unwrap_keys... old generation\n
help
se-rm-support: %d - > 0x%x\n
gsk:a:vS:
sfao
acm_create
memento slot
ec_p256_create
%d: generating keys...\n
successfully verified user (us: %llu)\n
-k <hex_wrapped_key> -c <class> [-h <handle>]
crypto_encryptText
LibCall_ACMContextCreateWithExternalForm
second
[-h handle] [-g generation-option] <old> <new>
, passcode threshold
Unknown keybag type (
DeallocCredentialList
%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid implicit stash%s\n
aks_set_system(no passcode)
dkey flags
validate succeeded unexpectedly\n
regress
ec_p256_sign
%s:%spid:%d,%s:%s%s%s%s%s%u:%s cat'ing %s%s\n
%d locking keybag\n
%d: current_generation: %u\n
aks_set_jcop_supports_updated_kud_policy() -> %d\n
    From grace period: %u\n
cmd_set_volume_keybag
dst passcode: 
Verification OK
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to spawn %s (rc=%d)%s\n
aks_system_key_uik
/Library/SMS
Unabled to parse uuid string %s\n
Error: did not update password appropriately
aks_set_configuration()@%d expect:0, got:%x\n
kAKSReturnNoMemory
/preferences
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n
fv_new_vek
xart_id_exi
remote-key
%s:%spid:%d,%s:%s%s%s%s%s%u:%s you pass a bad password for your device%s\n
acl4_encrypt
set special handle %d: %d\n
  Mean Unlocked: %llu.%02llu minutes\n
GracePeriodSet
remove
b:drt:R
test escrow recovery
group seed wrapping type
escrow-unlock
passcode unlocked
/Media/iTunes_Control
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n
aks_parse_escrow_blob
7 day inactivity reboot
failed to encode params\n
blob_sign
collection(%s, %s): succcess\n
04757eb1a0095ad69e99fa5ec2bb39ab6ba2ef474b8898695d6648306c9627e4561aeb591a7c6761829d45cd2a4d3d710880d5fd806eec80cef3cc1f4eaa00f25b
missing nonce, please use -a
slmu
iteration %i failed\n
ed_encrypt
%s result: (%d):%s\n
completed in %lld mins %lld seconds\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unexpected IO property type%s\n
meb10minf
oect
pcma
flp:P
%s:%spid:%d,%s:%s%s%s%s%s%u:%s dst kek required, pass in a hex blob with -b%s\n
kern.hv_vmm_present
apfs
change in progress
aks_apfs_preboot_mount_point
calling get config
unexpected aks_sks_heap_stats_s size
aks_unlock_bag(device)
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
sleeping 60 seconds.
Hex dump string of file content:\n
kek group
aks_decrypt(acl3)
    Mean Unlocked: %llu.%02llu minutes\n
sik collection
%i  - remote pub: (%i) 
/Applications
fv_set_protection,remove
cxw
NULL
XART
aks_remote_peer_get_state()@%d expect:0, got:%x\n
aks_remote_session(DEVICE_AUTHENTICATION_ORIGINATOR|DEVICE_AUTHENTICATION_UNLOCK_WITH_TOKEN)@%d expect:0, got:%x)\n
messing around
aks_wrap_key
fv(kext side)
get cx window %s (%llu) -> (%s)\n
04e039a4afde157c99bb1b25f6817c999a8fea07486649d4760ab8753b07bfa7319c63fedf306d66d4022e05e5f64164ae24424b3eafe3e5da928bd88d286a33eb
sym_verify
back-off
backup bag uuid: %s\n
[<handle> [<passcode> [<escrow_file> [<escrow_password>]]]]
<handle> <infile> <outfile>
[-l] [-m mode] [-r reg_id] [-v value]
xart-policy-enforced
** peer list
aks_create_bag(backup)
fail.
kSKSReturnIPCDecode
FBSShutdownOptions
tsi
%s:%spid:%d,%s:%s%s%s%s%s%u:%s purging %s%s\n
unknown
created key set: %s\n\n
invalid -m option %s
ec_p256_validate_key
failed attempts: %d, backoff: %llu\n
AppleTDMAKSServices
mes
ri
requires root! careful will destroy your session bag\n
second thread: %d/%d, out of %d attempts\n
remote_session_step_all(): %x\n
spka
osgn
verifyAclConstraintForOperationCommandInternal
ACMRequirement - ACMRequirementDataUserOutputDisplayed
acm_transport
 committed
recovery failed (%d, 0x%x), please try again using a different passcode\n
B
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unsupported vek type for sys enable%s\n
acm_add_passcode
    Continuity unlocks: %u\n
persistent.previous_day.session_count[LOCKED]: %u\n
ga: create bag
, has xART policy
DEVICE_AUTHENTICATION_RESET_SESSION
slpu
pcub
content-protect: %s\n
ah:p:s:?
test-mapping
AppleAPFSVolume
oece
Util_ReadFromBuffer
LibCall_ACMContextRemoveCredentialsByValueAndScope
seed = 
effaced
unknown, please file radar
aks_kc_backup_wrap_key failed, result = %d (%s)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s APFSVolumeRemoveUnlockRecord: %s%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek and unmanaged vek device protection mismatch vek:%x, kek:%x%s\n
_enable_user_kek
success
not-future-bumped
pka_p256_sign
failed to delete xart leak for %s\n
unload session bags
fv-rewrap-verifier
<NA>
Time since lock: %llu seconds (%.2f hours)
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to get sealed hashes%s\n
persistent.current_day.unlocks_by_hour:
iOS
failed to open userclient via %s: %d\n
vuid
LibCall_ACMTRMLoadState
CCCryptorFinal result: %d\n
bad_passcode
%s:%spid:%d,%s:%s%s%s%s%s%u:%s password for device bag successfully changed to '%s'%s\n
set-nonce
proto
<disk>
unlocked via escrow bag
kern.bootargs
volume bag lock state
ed_set_class
fetch analytics
%i  - state: %s; os: %s
aks_delete_xart_leak
xart_id_fv_smdk
sst
ACMContextSetData
aks_kc_backup_unwrap_key failed %d (%s)\n
aks_assert_hold on %i (%x)\n
special handle %d: %d\n
kAKSLockStateChangeEvent
aks_system_key_generation_committed
swift
/Library/WebClips
aks-client-queue
sym_decrypt
password1
this is a super long passcode
Unmapping %s
boot-args
persistent.previous_day.session_count[UNLOCKED]: %u\n
class: %d inode: %llu rev: %u keysize: %u type: %u, mode: %u\n
[-d | -r] [ -t <tdm_id> ] -b <blob>  ie: ascii_hex
Measuring aks_get_extended_device_state() perf
signed key (cku):\n
  -h    Show this help\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s drop_uid -> 0x%x\n%s\n
aks_system_key_gsmak
create and save escrow bag
<uuid> <password> <filename>
aks_fv_unwrap_vek_with_acm
set
either --set or --get is required, and can't both set\n
continuity-peer %s: success (secret regenerated, status changed to %d)\n
persistent.current_day.unlocks_from_grace: %u\n
, escrow unwrap required
csk
/networkd
mec
%d paralel threads calling AKS %d times: avg %llu us\n
load
drain_backup_keys to file %s succeeded\n
04c8c32aad13439fb9d893e3c976de3b44212bde3a740a52469ecc091560873c60a0aef9b4371a9f460e6c25b375475e4a4b1b1554d7495349f90096ed97e7c94a
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n
GK
backup
Test volume backup  - <uuid> needs to be a persona mapped volume
v8@?0
Failure
kAKSReturnNotCapable
osks
passcodeServiceSlots
LibCall_ACMContextUnloadToImage_Block
ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes
ACMSetEnvironmentVariable
failed to creat external ACM form\n
pka attest sw (ec-p384)
043b046c8a5846a510aeba3bf3e97355958647bd633c085e51e79a221d38c6d047b1c7374843754720d1db03b7fa38dc46fcff75273cfe54e682179f8f5aed42b9
provisioned: %s\n
get uuid for keybag by handle
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Escrow blob is too big %zd/%llu%s\n
gskv
bk
uuid b: 
dbg-crypto
debug
04b981bb55a7384d007c9efa29cbbbde79f1aebe57d6dbfe505b7cafb89231c14a67b603b1478851f75e4244b0ed90b78ec109d7a4de757c88124c4ace727f2f2fbe1fd1a82b2c676ecb62f23c9a73e37dedf3ac2b60a92214a2daf5247ae47289
f:h:np:st:x
[-e|-d]
shared allow list:
xart_id_haven
with interleaving unlocks
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to validate attestation%s\n
satori_p256_sign_2
reset-token
30-60m
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKsTestIsClassAAvailable failed: %d%s\n
show time remaining until inactivity reboot
/Keychains
sym_wrap
%d: unlocking keybag\n
%d: aks_unwrap_keys... with original passcode (class 12 should fail with e00002bc)\n
AK
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to get child for scheme for %s%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Could not get snapshot parent volume for %s%s\n
/Library/AggregateDictionary
Class getFBSShutdownOptionsClass(void)_block_invoke
satori_p256_verify_2
Cannot spawn %s: %s\n
get-system
sklkgp
pcclao
LibCall_ACMGlobalContextCredentialGetProperty
content-protect
event2: %s (0x%x), dict: %p, count: %d\n
unload_keybag %d succeeded\n
%s%s
kSKSReturnInvalidPersona
Loaded and unlocked backup bag as handle %d\n
/root/Library/Caches
pcdbm
%s maps to invalid type\n
attest_validate_key
event5: %s (0x%x), dict: %p, count: %d\n
  Mean Locked: %llu.%02llu minutes\n
/Library/DoNotDisturb
cmpg
salt
fv_extract_kek
aks_create_bag(escrow)
%s:%spid:%d,%s:%s%s%s%s%s%u:%s one of the threads failed%s\n
/Library/DeviceRegistry.dontBackUp
max-unlock-attempts: 
wk
bh
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/aeskeywrap.c
unlock old passcode
%s (handle=%d, class=%d, type=%u).\n
ec_ecies_transcode
\t-f <vek_blob_out_filename>
set system(%d => %d) succeeded\n
cag
crypto_generateKeyFromSharedInfo_version2
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode blob%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks_sealed_hashes_set result: %d%s\n
acl1_encrypt
call to create
backup key is the proper size
aks_fv_new_vek
xart_id_keybag_device_handle
ccgcm_update
uuid c: 
disabled
Failed to save wrapped data at %s\n
Backup enable, backup bag saved (%s).\n
AKU
fv-new-verifier
xart_id_system
rawValue
M-key migrated
/usr/libexec/seputil
escrow iterations remaining: %llu\n
IOService:/IOResources/AppleKeyStoreTest
Creating vek
platform_rng
ACMContextRemoveCredentialsByValue
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s %s unlock %s (%d)%s\n
file id: %d wipe id: %d\n
pka_p384_delete
acl4_wrap
unexpectedly succeeded to verify attestation (committed)
Create ACM cred 1
fv_unwrap_vek
mu
uikp
com.apple.foo
this is fun
unload_public_bag
apfsctl
error: peer public key is required (-p)\n
⚒️
REBOOTING
kc-backup-unwrap
get_bsd_name
dnh:
com.apple.bar
persistent.last_lock_timestamp: %llu\n
test-kks
ACMSetEnvironmentVariableWithAccessPolicy
sleeping; waiting for unlock tokens to expire\n
recover
ERROR: failed to verify passcode for keybag
Mapping %s to uid %u\n
Deleting persona %s from keybag %d\n
ps
sav
sls
DeviceBag
aks_decrypt(acl4)
Using TDM entry 0x%llx\n
64C0C6EB-0000-11AA-AA11-00306543ECAC
ACMRequirement - ACMRequirementDataPushButtonWithAttributes
ACMContextRemoveCredentialsByValueAndScope
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kek constraint violation 1%s\n
cmd_get_info
escrow-unlock     [-k <keyset>] <escrow-key-in-hex>
couln't create a refkey
daemon
/db
device is not locked, inactivity reboot timer is not active
ACMContextVerifyPolicyEx
%s: %llu seconds ago\n
\toffset max:     %llu\n
failed to load bag %d\n
continuity-peer %s: failed -> 0x%x (%s)\n
Tests for class B:\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n
kext-option
aks_create_bag(no passcode)
f:o:O:s:t:u:
pka_p384_create
previous 24h window:
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to delete reset token 0x%x%s\n
dump
creating xART bag\n
Bad class: %c.  Specify [a-f]\n
foobar
cmd_applekeystored
kc-backup-get-uuid
/run
/Library/FrontBoard
meb0m20m
cpo
config test failed 
inside thread %d , waiting for wakeup[threadid] : %d\n\n
se-slot: %u\n
jcop updated kud policy
error: unknown mode\n
persistent.previous_day.unlocks_pki: %u\n
kSKSReturnError
reference-keys
aks_remote_session(DEVICE_AUTHENTICATION_ESCROW)@%d expect:%x, got:%x)\n
aks_remote_session(DEVICE_AUTHENTICATION_UNLOCK_WITH_ESCROW)@%d expect:%x, got:%x)\n
keystorectl system-keys -t type -g generation -c -a -p -o operation -h handle -R <ref-key-blob>\n
    %s - %u unlocks (local)\n
  Locked: Min %llu.%02llu, Max %llu.%02llu minutes\n
in edu mode
    -r performs KEK deletion
read-file
thread %d is up\n\n
NO
xart tracker:
create_escrow_bag
0438e3fcf40ffe17f2869f4fca724763c2db50a3b7bbff96358f351a8496db3b3ca7615110a284481c7bcfa5681af59fb44e57b9d0cf71b54691078896a6f2536a82819f4ccf6853c2fbbfb8244a5c648f2f1ab25dbb89fcb538b827819f4f6b3c
%s:%spid:%d,%s:%s%s%s%s%s%u:%s beacon is required for test%s\n
system-key-test
utils
create-key-set    [-k <keyset>]
h:k:
has_key
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n
si2
pdps
LibCall_ACMSetEnvironmentVariable
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed to decode vek%s\n
not enough arguments for %s (has %d, needs %d)\n
cmd_test_persona
acl2_verify
passed
Encrypted buffer contains string.\n
040df07705f9922c60898290a9c0adbe4a9ccee27c6118c6cf56016ab4206724bf24f5854f702fc069a9babd1c7d7cdfeebd343e2e9101099eee9007be9b23be6b44fb4d1bb1ea9befba2c907dc3d1438f994abe3e7862a61639278ff595dd01a0
unlock backup bag
_wireless
GroupSeed
 (force-group-seed-roll)
kAKSReturnNotReady
kAKSReturnInProgress
akstest_rewrap_ek
xart_tracker_decode_data
vbvc
refc
v20@?0i8^{__CFDictionary=}12
Need backup bag, backup secret, class, input file, output file
 (expired) %llu seconds ago
p
/iomfb_bics_daemon
rkm
lockedSecondsAgo
ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Internal Error: Null VEK, file radar%s\n
Disabling backup for volume %s.\n
\t-f <vek_key_out_filename>
04b34836367d1fbf0c575378013ece046436c175a5e905abc5a52facd3c01fedf24290e52e804f22fdd9e502711fab9d9dce40d774acb521711340db86aa289e30
/Library/Logs/AppleSupport
se reset token is set
aks_remote_peer_drop()@%d expect:0, got:%x\n
ec_p256_encrypt
acm error: %d\n
pka_ecies_transcode
recovery succeeded\nmay need to run: pkill -9 SpringBoard; pkill -9 PreBoard\n
cmd_icsc
ref-key-blob-test
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Warning: AppleKeyStoreTest kext not loaded. Unable to run persona fs_new_key/fs_unwrap tests%s\n
perform unlock with token\n
set keybag handle %d for volume %s\n
048ab62440908cdf586d37addff3b6bc19a33dc2797d58cfe75c76f13881edaa910e404073690d5183f4e416245921ba137f1af4ae9a7d24dcf4c7d463fab3a573
disabled 'unlocked'
failed to get membership
/root/Library/Logs
e
Save wrapped key at %s\n
All done. rc: %x pid: %d\n
pub_len:%zd != pub2_len:%zd
unexpectedly (committed) succeeded to attest
%s:%spid:%d,%s:%s%s%s%s%s%u:%s incorrect length%s\n
cmd_fv_users_block_invoke_3
se
%d: aks_unwrap_keys...\n
_factorydata_path_ls
0475c059042e10f9d8ae1dc7caa7702a3680f539aab9a0efce006c472b3eb504f6bb77010a5ae2f8173cbe40faaff7654e909066bd0df5a9b729fcb73e005d0ab5
kc-backup-get-handle
<var>
purpose
LibCall_ACMSEPControl_Block
ACMGlobalContextAddCredential
group seed generation
trace(1) is not present\n
ec_p384_wrap
\t-d
BootPolicy
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Skipping ephemeral policy test since no AppleKeyStoreTest Kext installed%s\n
gid attest public key:
lmu
unexpected peerinfo version 
ACM
LibSer_ACMDeserializeSEPControlCode
LibCall_ACMContextGetData
Usage: kc-wrap -k <hex_key> -c <class> [-h <handle>]
yukone_sik_pub_key
persistent.previous_day.graceperiod_entries: %u\n
/Library/Mail
osc
AKSIdentityDelete failed\n
aks_remote_session(DEVICE_AUTHENTICATION_ESCROW)@%d expect:0, got:%x)\n
handle %d's se reset pub: 
04220820b5a5db9088b9bf3dc6c5ebc7a34d30f36cd44d707fd8d96163eb888e42e58b90c0649ae05cf8bdbe1ca2de9b08c3902658154f4fd3391f1b50fb4a53b0
create-keybag
mkey use count: %d\nckey use count: %d\nuid media key use count: %d\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s IOObject %s is not AppleAPFSVolume%s\n
pcuc
ACMCredential - ACMCredentialDataPassphraseEntered
AKSIdentityMigrateFirst failed\n
list
read failed!\n
log-scope
```
