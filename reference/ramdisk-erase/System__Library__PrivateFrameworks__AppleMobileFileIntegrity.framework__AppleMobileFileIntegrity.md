# `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 266,016 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 4056)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libmis.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (7 classes, 1 protocols)

Classes: `AMFIConnection`, `AMFIDeveloperModeSettingVisibilityManager`, `AMFIError`, `AMFIFMKLog`, `AMFIPathValidator_ios`, `LWCRTypeErrorContext`, `ValidationMetrics`

Protocols: `AMFIProtocol`

## Strings (528)

```
AMFIConnection
AMFIDeveloperModeSettingVisibilityManager
AMFIPathValidator_ios
AMFIError
ValidationMetrics
AMFIFMKLog
LWCRTypeErrorContext
AMFIProtocol
invalidated
setError:
setRemoteObjectInterface:
removeTrustforTeamID:withReply:
connection
developerModeChangedToken
handlePairableHostBecameUnavailableWithIdentifier:
initWithURL:withFileOffsetAsNumber:withFlags:
pushKey:
stringWithUTF8String:
unsignedLongLongValue
dealloc
_error
_isValid
areEntitlementsValidated
errorWithDomain:code:userInfo:
setSupervisedState:
signTeamID:withSignType:withLAContext:withError:
T@?,C,N,V_changeBlock
TB,N,V_monitoringStarted
TI,R,N,V_signerType
_monitorQueue
interfaceWithProtocol:
keyContext
_changeBlock
_profileInstalledToken
initWithData:encoding:
initWithMachServiceName:options:
null
profileRemovedToken
identifier
isEqualToString:
T@\"NSMutableDictionary\",&,N,V_pairableHosts
monitoringStarted
newConnection
setMonitoringStarted:
_settingsShouldBeVisibleInternal
.cxx_destruct
_callbackQueue
stageProfileForUuid:withReply:
startMonitoringVisibilityChangesOnQueue:withBlock:
T@\"NSError\",R,N,V_error
numberWithBool:
defaultManager
generic
isValid
setCallbackQueue:
_pairableHostBrowser
_pairableHosts
_profileAuxSig
cancel
commitProfileForUuid:
initiateDeveloperModeDaemons
teamIDSupportsAuxiliarySignature:
Ti,N,V_profileRemovedToken
profileData
visibilityDidChange:
T@\"NSData\",R,N
UTF8String
T@\"RPPairableHostBrowser\",&,N,V_pairableHostBrowser
_profileData
dictionaryWithObjects:forKeys:count:
getSEPStateWithError:
initWithURL:withFlags:
profileInstalledToken
recomputeVisibility
removeTrustforTeamID:
Ti,N,V_profileInstalledToken
removeManagedStateWithReply:
removeObjectForKey:
setManagedState:
_monitoringStarted
countByEnumeratingWithState:objects:count:
resume
setDeveloperModeChangedToken:
stringWithString:
synchronousRemoteObjectProxyWithErrorHandler:
validateWithError:
setChangeBlock:
getBytes:length:
initWithURL:withFileOffset:
removeManagedState
sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningYear:withExecutableFormat:withHasRestrictedEntitlements:
teamIDWithProfileUUID:
intValue
_developerModeChangedToken
_invalidated
initiateDeveloperModeDaemonsWithReply:
setManagedState:withReply:
TB,R,N,V_areEntitlementsValidated
appendString:
count
enumerateKeysAndObjectsUsingBlock:
removeLastObject
setDemoState:withReply:
setPairableHosts:
longLongValue
addObject:
TB,N,V_settingsShouldBeVisibleInternal
initiateDataMigrationWithReply:
T@\"NSString\",R,N
_profileID
bytes
getStagedProfileWithReply:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue
numberWithUnsignedLongLong:
pairableHostBrowser
settingsShouldBeVisible
synthesizeError
Ti,N,V_developerModeChangedToken
appendFormat:
cStringUsingEncoding:
fileExistsAtPath:
getSEPStateWithReply:
registerHostDiscoveredHandlerOnQueue:handler:
handlePairableHostDiscovered:
initWithAMFIErrorCode:withURL:
initWithMISError:withURL:
initWithURL:
_validated
TB,N,V_invalidated
settingsShouldBeVisibleInternal
_areEntitlementsValidated
auxiliarySignatureWithTeamID:
computeCurrentVisibility
getStagedProfileWithError:
initiateDataMigration
_flags
popKey
removeAllObjects
setPairableHostBrowser:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_monitorQueue
_url
isSignerType
monitorQueue
setObject:forKeyedSubscript:
setSettingsShouldBeVisibleInternal:
changeBlock
code
computedCdHash:withLength:
pairableHosts
profileID
setSupervisedState:withReply:
setTrustForTeamID:withSignature:withSignType:
setTrustForTeamID:withSignature:withSignType:withReply:
_cdhash
TB,R,N,V_isValid
_profileRemovedToken
dispatchMetrics:
signerType
commitProfileForUuid:withReply:
_offset
init
initWithURL:withFileOffset:withFlags:
objectForKey:
path
setDemoState:
setObject:forKey:
callbackQueue
initWithDomain:code:userInfo:
stageProfileForUuid:
startBrowsing
setInvalidated:
_signerType
length
registerChangeHandlerOnTargetQueue:handler:
setProfileInstalledToken:
setProfileRemovedToken:
signTeamID:withSignType:withLAContext:withReply:
_bootargs
domain
profileAuxSig
setMonitorQueue:
available
error
invalidate
@32@0:8@16Q24
B24@0:8^@16
I16@0:8
@\"NSError\"
@\"NSData\"
@28@0:8i16@20
v88@0:8@16@24@32@40@48@56B64@68@76B84
v28@0:8I16@?<v@?@\"NSError\">20
@?
v32@0:8@16@?24
@\"NSObject<OS_dispatch_queue>\"
Q
{?=III{?=C{?=I[32C]}}}24@0:8^@16
@36@0:8@16@24I32
@20@0:8I16
@36@0:8@16Q24i32
I
@\"NSString\"
v24@0:8@?<v@?@\"NSError\">16
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
v24@0:8@?<v@?@\"NSString\"@\"NSError\">16
B16@0:8
i16@0:8
v20@0:8i16
@\"RPPairableHostBrowser\"
@24@0:8@16
@36@0:8@16@24i32
@16@0:8
v20@0:8B16
v24@0:8@?16
@\"NSMutableArray\"
v44@0:8@16I24@28@?36
v24@0:8@?<v@?{?=III{?=C{?=I[32C]}}}@\"NSError\">16
v32@0:8@\"LAContext\"16@?<v@?@\"NSError\">24
@?16@0:8
B32@0:8[64C]16*24
@\"NSNumber\"
@32@0:8q16@24
v20@0:8I16
@24@0:8^@16
@\"NSXPCConnection\"
v24@0:8@16
i
@28@0:8@16i24
v44@0:8@16@24I32@?36
v44@0:8@\"NSString\"16I24@\"LAContext\"28@?<v@?@\"NSData\"@\"NSError\">36
v44@0:8@\"NSString\"16@\"NSData\"24I32@?<v@?@\"NSError\">36
v16@0:8
B
@\"NSMutableDictionary\"
@\"NSURL\"
v28@0:8I16@?20
@44@0:8@16I24@28^@36
Unexpected type for key
$query
TeamName
An internal error has occured
This file does not meet dyld_sim policy for this platform
is-sip-protected
$gt
AMFIProfileRemoveTeamIDTrust
_createAuxiliarySignature
com.apple.rootless.
platform-identifier-for-current-process
PreboardUPP
AMFIProfileScheduleTrust
Request is not a dictionary
%2.2x
The best matching profile does not provision the certificates used to sign this file
Unable to retrieve code path information
Unable to retrieve executable path
team-identifier
reqs
LWCRVerificationError
com.apple.security.
AMFISupervisedModeSetState
AppleMobileFileIntegrity
-[AMFIConnection getSEPStateWithError:]_block_invoke
-[AMFIConnection commitProfileForUuid:]_block_invoke
com.apple.system-task-ports.token.control
Caller requested validation of an unknown platform
Caller provided an option that is not supported for the requested platform
The best matching profile is not valid for this device
com.apple.sha1.code_directory.usage
signing_timestamp
developer-mode
LocalAuthentication
cpuType
com.apple.hid.manager.user-access-keyboard
Profile matching service is unavailable
The best matching profile is not validly signed
B16@?0r^{MISMatchedProfile=^{__CFString}^{__CFString}BBBBB@}8
Unexpected key
Constraint category is disallowed for specified LWCR category
B16@?0^v8
security.mac.amfi.developer_mode_status.changed
bundle_identifier
AMFI
No Constraint provided
cdhash-full
Unknown Category for validation
vers
Query Tuple
Error
platform-identifier
Constraint is too deeply nested
AMFIProfileCommitProfile
B24@?0Q8^v16
-[AMFIConnection initiateDeveloperModeDaemons]_block_invoke
v65@?0{?=III{?=C{?=I[32C]}}}8@\"NSError\"57
-[AMFIConnection stageProfileForUuid:]_block_invoke
amfid.validation.metrics
$or-array
AMFIProfileSetTeamIDTrustWithOptions
_getTeamIDAuxiliarySignature
IODeviceTree:/chosen
-[AMFIConnection getStagedProfileWithError:]_block_invoke
com.apple.security.cs.allow-unsigned-executable-memory
-[AMFIConnection setSupervisedState:]_block_invoke
-[AMFIDeveloperModeSettingVisibilityManager computeCurrentVisibility]
@\"NSDictionary\"8@?0
/private/var/tmp/show_dev_mode
on-authorized-authapfs-volume
launch-type
Success
Too many keys for dictionary
com.apple.private.tcc.manager
Unable to retrieve signing identifier
default
team-identifier-for-current-process
$flag-check
Array
 -> %@
com.apple.developer.endpoint-security.
The file is unsigned
Unable to create code directory hash
has_restricted_entitlements
code-signing-flags
$and-array
Sub dictionary violated a precondition set by the parent dictionary
Dictionary does not specify any constraints
flags
com.apple.private.signing-identifier
com.apple.developer.driverkit
security.mac.amfi.developer_mode_resolved
info-plist-hash
signing-identifier
$in
AMFIProfileRequiresReboot
com.apple.local-signing
cdhash
Unknown Key
B24@?0r*8^v16
AMFIDemoModeSetState
_getProfileAuxiliarySignature
IODeviceTree:/options
com.apple.amfi.nsxpc
com.apple.uikitsystemapp.nonui-client
com.apple.security.cs.allow-dyld-environment-variables
is_apple
sip-enabled
$or
Flag value is invalid for this fact/category combination
AMFIProfileGetScheduledProfile
AMFIMDMModeEnroll
cpuSubType
is-kernel-proc
security-mode-change-enable
v16@?0@\"RPPairableHost\"8
com.apple.private.codesignkit.signer-source-host
com.apple.swift-playgrounds.local-signing-key
Caller requested validation with an invalid option
The file is adhoc signed or signed by an unknown certificate chain
team_identifier
v16@?0@\"NSError\"8
v24@?0@\"NSData\"8@\"NSError\"16
com.apple.system-task-ports
com.apple.developer.driverkit.
com.apple.developer.networking.networkextension
Unable to retrieve certificate chain
is-init-proc
platform
AMFIMDMModeRemove
-[AMFIConnection removeTrustforTeamID:]_block_invoke
v12@?0i8
get-task-allow
The best matching profile does not match the entitlements of this file
apple-internal
in-tc-with-constraint-category
$lte
-[AMFIDeveloperModeSettingVisibilityManager invalidate]
-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostDiscovered:]
com.apple.security.cs.disable-library-validation
com.apple.MobileFileIntegrity.framework
security.mac.amfi.developer_mode_status
Constraint too large
is-main-binary
os-environment
sliceOffset
The best matching profile has expired
Unexpected type for array
Error: %s, Context: 
 -> 
-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke
-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostBecameUnavailableWithIdentifier:]
com.apple.private.cs.debugger
The file is adhoc signed but contains restricted entitlements
Key not supported for the specified category
com.apple.security.cs.allow-jit
$optional
$and
-[AMFIConnection setDemoState:]_block_invoke
-[AMFIConnection removeManagedState]_block_invoke
MISProvisioningProfileInstalled
%
Device has a passcode set
com.apple.private.host-exception-port-override
Profile requested is not currently staged
No matching profile found
executable_format
MISProvisioningProfileRemoved
LocalAuthentication call failed
signing_identifier
entitlements
-[AMFIConnection initiateDataMigration]_block_invoke
AppleMobileFileIntegrityError
com.apple.private.security.clear-library-validation
The entitlements in this file are malformed
filename
Too many elements in array
-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke
v8@?0
An unknown error has occured
task_for_pid-allow
com.apple.system-task-ports.control
com.apple.private.tcc.allow
com.apple.private.icloud-account-access
An unknown error was encountered
$gte
com.apple.amfi.developer_mode_visibility_monitor
com.apple.private.security.
version
$lt
Unexpected Type
Internal error
ccat
Query Array
com.apple.security.cs.disable-executable-page-protection
The signature on the file is invalid
on-system-volume
validation-category
v24@?0@\"NSString\"8@\"NSError\"16
com.apple.developer.endpoint-security
com.apple.private.cs.automator-plugins
Caller provided invalid parameters
comp
v32@?0@8@16^B24
-[AMFIConnection setManagedState:]_block_invoke
-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]
com.apple.hid.manager.user-access-privileged
com.apple.security.cs.allow-relative-library-loads
unable to find local signing key in keychain: %d
[%s] Discovered nearby pairable host: %@
successfully copied local signing private key
found no local signing keys in keychain
unable to add public key to AMFI: %d (%s)
Unexpected MISError (0x%x): %@
[%s] PreBoard flow disabled
[%s] unable to set state: %@
unable to allocate a SecAccessControlRef for the key access control
[%s] request for profile: %@
[%s] unable to enable MDM: %@
Invalid options combination cpuType: (%@) cpuSubType: (%@) sliceOffset: (%@) for: %@
found multiple (%ld) local signing keys in keychain
successfully created local signing private key in keychain
SecKeyCreate error: %ld (%s)
[%s] unable to check for reboot: %@ | %u
[%s] auxiliary signature unsupported: %@
Invalid flags (%@) for: %@
unexpected public key length: %lu
[%s] Not monitoring for pairable hosts since RemotePairingDevice is not loaded.
the local signing private key is not available: %d
[%s] missing Team ID: %@
[%s] attempting to remove staged profile
Invalid slice offset (%@) for: %@
Invalid cpu type (%@) for: %@
MIS Validation successful, but unexpected info? path: '%@', options: %@, info: %@, cdhash: %@
[%s] unable to acquire staged profile: %@
[%s] attempting to commit profile: %@
[%s] unable to remove trust for team ID: %@
[%s] developer mode daemons error: %@
[%s] Nearby discovered pairable host disappeared: %@
unable to allocate a CFMutableDictionaryRef for the key parameters
[%s] unable to commit profile: %@
[%s] unable to create aux-sig: %@ | %@ (not-fatal)
Invalid cpu sub type (%@) for: %@
%@ not valid: 0x%x: %@
unable to add public key to AMFI
unable to allocate a CFMutableDictionaryRef for the keyQuery
SecItemCopyMatching returned unknown object
unable to allocate a CFNumberRef for the key size
SecKeyCreate error: %ld
[%s] team ID must be provided
Unable to extract signer type? path: '%@', info: '%@'
found local signing key as a system key
found untrusted object in the keychain
[%s] no reboot requirement: %@
[%s] attempting to remove trust for team ID: %@
Error cannot evaluate unknown platform (%d) for: %@
[%s] Invalidated
[%s] profile UUID must be provided
[%s] must capture scheduled profile
[%s] missing profile: %@
[%s] enabling MDM state
[%s] Reporting developer mode settings visible because nearby pairable hosts were found
unable to find local signing key on the system
added local signing public key to AMFI
%s: attempting to schedule profile: %@
[%s] xpc error: %@
successfully copied local signing private key from keychain
[%s] unknown trust type: %u
[%s] removing MDM state
[%s] data migration error: %@
Unexpected option(s) in dictionary: %@ for: %@
unable to allocate a CFNumberRef for the system boundary
[%s] must capture reboot requirement
[%s] unable to stage profile: %@
[%s] attempting to set trust for team ID: %@ | %u
[%s] Started monitoring for visibility changes
[%s] Reporting developer mode settings not visible
boot-args allow process with invalid signature: %@
SecKeyCreate error: <unknown>
unable to extract public key from local signing private key
unable to extract public key bytes from public key: %d
Dropping validation metrics because queue is full
[%s] auxiliary signature exists: %@
[%s] Reporting developer mode settings visible because AMFIShouldShowDeveloperModeSettings returned true
dyld_sim policy is not allowed on iOS: %@
[%s] missing Team Name: %@
[%s] unable to set trust for team ID: %@
[%s] setting supervised state: %u
[%s] setting demo state: %u
[%s] unable to remove MDM: %@
[%s] missing profile: %@ | %u
```
