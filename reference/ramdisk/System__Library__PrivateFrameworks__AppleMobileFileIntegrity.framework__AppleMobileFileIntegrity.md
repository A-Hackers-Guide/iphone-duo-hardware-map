# `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity`

From the upgrade restore ramdisk (141-29011-104.dmg). 266,016 bytes.

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
setObject:forKey:
setSettingsShouldBeVisibleInternal:
Ti,N,V_developerModeChangedToken
appendString:
bytes
getSEPStateWithError:
initWithAMFIErrorCode:withURL:
initWithMISError:withURL:
profileInstalledToken
validateWithError:
T@\"NSMutableDictionary\",&,N,V_pairableHosts
TB,N,V_invalidated
settingsShouldBeVisibleInternal
isEqualToString:
length
profileData
resume
_monitorQueue
_profileRemovedToken
setMonitorQueue:
removeTrustforTeamID:withReply:
computedCdHash:withLength:
connection
stringWithUTF8String:
Ti,N,V_profileRemovedToken
_error
addObject:
callbackQueue
getStagedProfileWithError:
null
setObject:forKeyedSubscript:
areEntitlementsValidated
errorWithDomain:code:userInfo:
setPairableHostBrowser:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_monitorQueue
setInvalidated:
setChangeBlock:
dispatchMetrics:
getStagedProfileWithReply:
handlePairableHostBecameUnavailableWithIdentifier:
_offset
handlePairableHostDiscovered:
isSignerType
TB,N,V_settingsShouldBeVisibleInternal
_invalidated
_isValid
countByEnumeratingWithState:objects:count:
setMonitoringStarted:
signTeamID:withSignType:withLAContext:withError:
synthesizeError
computeCurrentVisibility
pushKey:
removeManagedStateWithReply:
TB,R,N,V_isValid
code
initWithMachServiceName:options:
initiateDataMigration
invalidate
monitorQueue
numberWithUnsignedLongLong:
sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:withSigningYear:withExecutableFormat:withHasRestrictedEntitlements:
TI,R,N,V_signerType
_profileInstalledToken
identifier
_cdhash
_monitoringStarted
newConnection
popKey
teamIDWithProfileUUID:
_signerType
defaultManager
initWithDomain:code:userInfo:
signTeamID:withSignType:withLAContext:withReply:
unsignedLongLongValue
isValid
TB,N,V_monitoringStarted
available
dictionaryWithObjects:forKeys:count:
getSEPStateWithReply:
initWithURL:
intValue
removeTrustforTeamID:
.cxx_destruct
initWithURL:withFlags:
pairableHosts
removeObjectForKey:
setTrustForTeamID:withSignature:withSignType:withReply:
startMonitoringVisibilityChangesOnQueue:withBlock:
_settingsShouldBeVisibleInternal
auxiliarySignatureWithTeamID:
initWithURL:withFileOffset:withFlags:
setManagedState:withReply:
setSupervisedState:withReply:
startBrowsing
visibilityDidChange:
_profileID
appendFormat:
getBytes:length:
initWithURL:withFileOffsetAsNumber:withFlags:
pairableHostBrowser
recomputeVisibility
commitProfileForUuid:
initWithData:encoding:
setPairableHosts:
T@\"NSError\",R,N,V_error
initiateDataMigrationWithReply:
_profileData
longLongValue
objectForKey:
profileAuxSig
setDeveloperModeChangedToken:
stageProfileForUuid:
dealloc
T@\"NSString\",R,N
numberWithBool:
removeLastObject
signerType
stringWithString:
synchronousRemoteObjectProxyWithErrorHandler:
T@?,C,N,V_changeBlock
Ti,N,V_profileInstalledToken
changeBlock
setProfileInstalledToken:
setProfileRemovedToken:
_bootargs
error
monitoringStarted
registerChangeHandlerOnTargetQueue:handler:
commitProfileForUuid:withReply:
_callbackQueue
cStringUsingEncoding:
initWithURL:withFileOffset:
initiateDeveloperModeDaemons
setCallbackQueue:
stageProfileForUuid:withReply:
initiateDeveloperModeDaemonsWithReply:
removeManagedState
setDemoState:
setDemoState:withReply:
setError:
settingsShouldBeVisible
_pairableHosts
generic
T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue
UTF8String
_changeBlock
profileRemovedToken
setTrustForTeamID:withSignature:withSignType:
TB,R,N,V_areEntitlementsValidated
invalidated
removeAllObjects
_developerModeChangedToken
_validated
init
setRemoteObjectInterface:
teamIDSupportsAuxiliarySignature:
T@\"RPPairableHostBrowser\",&,N,V_pairableHostBrowser
_url
enumerateKeysAndObjectsUsingBlock:
profileID
registerHostDiscoveredHandlerOnQueue:handler:
_areEntitlementsValidated
_flags
count
developerModeChangedToken
path
setSupervisedState:
T@\"NSData\",R,N
cancel
interfaceWithProtocol:
_pairableHostBrowser
_profileAuxSig
domain
fileExistsAtPath:
keyContext
setManagedState:
@32@0:8@16Q24
I16@0:8
@\"NSData\"
@32@0:8q16@24
i16@0:8
B32@0:8[64C]16*24
v88@0:8@16@24@32@40@48@56B64@68@76B84
v24@0:8@?<v@?@\"NSError\">16
v44@0:8@\"NSString\"16I24@\"LAContext\"28@?<v@?@\"NSData\"@\"NSError\">36
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
@?
@?16@0:8
B
@\"NSURL\"
@\"NSString\"
v20@0:8I16
v44@0:8@16@24I32@?36
v24@0:8@?<v@?{?=III{?=C{?=I[32C]}}}@\"NSError\">16
@\"NSError\"
v28@0:8I16@?20
v24@0:8@?<v@?@\"NSString\"@\"NSError\">16
@44@0:8@16I24@28^@36
@\"NSXPCConnection\"
@\"NSObject<OS_dispatch_queue>\"
v24@0:8@?16
v20@0:8i16
@\"RPPairableHostBrowser\"
@36@0:8@16@24i32
v32@0:8@\"LAContext\"16@?<v@?@\"NSError\">24
@24@0:8^@16
@\"NSMutableArray\"
v28@0:8I16@?<v@?@\"NSError\">20
{?=III{?=C{?=I[32C]}}}24@0:8^@16
@20@0:8I16
@16@0:8
v20@0:8B16
@\"NSMutableDictionary\"
@28@0:8@16i24
@28@0:8i16@20
v44@0:8@\"NSString\"16@\"NSData\"24I32@?<v@?@\"NSError\">36
@36@0:8@16@24I32
B16@0:8
v24@0:8@16
@36@0:8@16Q24i32
B24@0:8^@16
@\"NSNumber\"
I
Q
v44@0:8@16I24@28@?36
i
v16@0:8
v32@0:8@16@?24
@24@0:8@16
The file is adhoc signed but contains restricted entitlements
$or
Internal error
v24@?0@\"NSData\"8@\"NSError\"16
-[AMFIConnection getStagedProfileWithError:]_block_invoke
Request is not a dictionary
developer-mode
Constraint category is disallowed for specified LWCR category
com.apple.amfi.developer_mode_visibility_monitor
get-task-allow
com.apple.local-signing
AMFI
security.mac.amfi.developer_mode_status
is-sip-protected
B24@?0Q8^v16
code-signing-flags
Unexpected Type
v65@?0{?=III{?=C{?=I[32C]}}}8@\"NSError\"57
-[AMFIConnection removeTrustforTeamID:]_block_invoke
com.apple.private.security.clear-library-validation
com.apple.developer.endpoint-security.
amfid.validation.metrics
default
$and
AMFIProfileCommitProfile
-[AMFIConnection setTrustForTeamID:withSignature:withSignType:]_block_invoke
com.apple.private.icloud-account-access
MISProvisioningProfileInstalled
Device has a passcode set
com.apple.private.signing-identifier
is-main-binary
signing-identifier
team-identifier-for-current-process
Query Array
-[AMFIDeveloperModeSettingVisibilityManager computeCurrentVisibility]
com.apple.hid.manager.user-access-keyboard
com.apple.private.host-exception-port-override
com.apple.private.cs.debugger
Caller requested validation with an invalid option
Unable to retrieve certificate chain
Unable to create code directory hash
has_restricted_entitlements
-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostDiscovered:]
filename
sip-enabled
entitlements
validation-category
B24@?0r*8^v16
v16@?0@\"NSError\"8
-[AMFIDeveloperModeSettingVisibilityManager handlePairableHostBecameUnavailableWithIdentifier:]
com.apple.developer.driverkit.
com.apple.security.cs.allow-relative-library-loads
The signature on the file is invalid
Unable to retrieve signing identifier
IODeviceTree:/options
com.apple.amfi.nsxpc
-[AMFIConnection initiateDataMigration]_block_invoke
sliceOffset
launch-type
$or-array
Sub dictionary violated a precondition set by the parent dictionary
comp
ccat
com.apple.system-task-ports.control
is_apple
TeamName
com.apple.hid.manager.user-access-privileged
com.apple.developer.networking.networkextension
platform
Dictionary does not specify any constraints
v32@?0@8@16^B24
cpuType
%
task_for_pid-allow
The best matching profile is not validly signed
Unable to retrieve code path information
Unable to retrieve executable path
on-system-volume
Unknown Key
info-plist-hash
in-tc-with-constraint-category
v12@?0i8
executable_format
team-identifier
B16@?0^v8
 -> %@
 -> 
v8@?0
com.apple.security.
com.apple.private.cs.automator-plugins
com.apple.private.tcc.allow
cdhash
team_identifier
platform-identifier
AMFIProfileGetScheduledProfile
com.apple.developer.driverkit
com.apple.sha1.code_directory.usage
platform-identifier-for-current-process
AMFISupervisedModeSetState
AMFIMDMModeRemove
LWCRVerificationError
security-mode-change-enable
-[AMFIConnection setDemoState:]_block_invoke
MISProvisioningProfileRemoved
AppleMobileFileIntegrityError
Caller provided an option that is not supported for the requested platform
$optional
Flag value is invalid for this fact/category combination
-[AMFIConnection setSupervisedState:]_block_invoke
com.apple.security.cs.allow-unsigned-executable-memory
com.apple.security.cs.allow-dyld-environment-variables
com.apple.security.cs.allow-jit
Profile matching service is unavailable
Caller requested validation of an unknown platform
Caller provided invalid parameters
IODeviceTree:/chosen
-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke
com.apple.system-task-ports
version
on-authorized-authapfs-volume
AMFIProfileScheduleTrust
v24@?0@\"NSString\"8@\"NSError\"16
v16@?0@\"RPPairableHost\"8
com.apple.system-task-ports.token.control
$lte
Unexpected type for key
_createAuxiliarySignature
Error: %s, Context: 
-[AMFIConnection removeManagedState]_block_invoke
Error
com.apple.security.cs.disable-executable-page-protection
This file does not meet dyld_sim policy for this platform
security.mac.amfi.developer_mode_resolved
Unexpected type for array
Too many elements in array
AMFIMDMModeEnroll
AppleMobileFileIntegrity
com.apple.uikitsystemapp.nonui-client
An internal error has occured
Profile requested is not currently staged
The best matching profile does not provision the certificates used to sign this file
@\"NSDictionary\"8@?0
apple-internal
AMFIProfileRemoveTeamIDTrust
_getProfileAuxiliarySignature
flags
An unknown error was encountered
$gt
Array
AMFIDemoModeSetState
The entitlements in this file are malformed
$query
com.apple.private.security.
Unknown Category for validation
_getTeamIDAuxiliarySignature
The best matching profile is not valid for this device
No matching profile found
com.apple.MobileFileIntegrity.framework
$lt
Too many keys for dictionary
AMFIProfileSetTeamIDTrustWithOptions
-[AMFIConnection getSEPStateWithError:]_block_invoke
-[AMFIConnection commitProfileForUuid:]_block_invoke
security.mac.amfi.developer_mode_status.changed
%2.2x
com.apple.private.codesignkit.signer-source-host
is-kernel-proc
$gte
$flag-check
Key not supported for the specified category
AMFIProfileRequiresReboot
The best matching profile does not match the entitlements of this file
The file is adhoc signed or signed by an unknown certificate chain
signing_timestamp
Unexpected key
Constraint is too deeply nested
Query Tuple
PreboardUPP
-[AMFIConnection setManagedState:]_block_invoke
An unknown error has occured
com.apple.rootless.
com.apple.developer.endpoint-security
The best matching profile has expired
signing_identifier
/private/var/tmp/show_dev_mode
No Constraint provided
$in
com.apple.private.tcc.manager
com.apple.security.cs.disable-library-validation
B16@?0r^{MISMatchedProfile=^{__CFString}^{__CFString}BBBBB@}8
Constraint too large
$and-array
reqs
LocalAuthentication
-[AMFIConnection initiateDeveloperModeDaemons]_block_invoke
is-init-proc
cdhash-full
-[AMFIConnection stageProfileForUuid:]_block_invoke
cpuSubType
com.apple.swift-playgrounds.local-signing-key
LocalAuthentication call failed
bundle_identifier
os-environment
Success
vers
-[AMFIDeveloperModeSettingVisibilityManager startMonitoringVisibilityChangesOnQueue:withBlock:]
-[AMFIDeveloperModeSettingVisibilityManager invalidate]
The file is unsigned
%s: attempting to schedule profile: %@
[%s] unable to stage profile: %@
[%s] missing Team ID: %@
[%s] Started monitoring for visibility changes
found no local signing keys in keychain
[%s] must capture reboot requirement
[%s] no reboot requirement: %@
[%s] unable to commit profile: %@
[%s] unable to set state: %@
Unexpected option(s) in dictionary: %@ for: %@
unexpected public key length: %lu
added local signing public key to AMFI
[%s] PreBoard flow disabled
[%s] team ID must be provided
[%s] unable to remove trust for team ID: %@
[%s] unable to remove MDM: %@
boot-args allow process with invalid signature: %@
found local signing key as a system key
found untrusted object in the keychain
unable to allocate a CFMutableDictionaryRef for the keyQuery
unable to add public key to AMFI: %d (%s)
[%s] unknown trust type: %u
[%s] unable to set trust for team ID: %@
[%s] missing profile: %@ | %u
[%s] Invalidated
unable to find local signing key on the system
unable to add public key to AMFI
SecKeyCreate error: %ld
unable to extract public key from local signing private key
Unexpected MISError (0x%x): %@
[%s] auxiliary signature exists: %@
[%s] missing Team Name: %@
unable to find local signing key in keychain: %d
successfully created local signing private key in keychain
[%s] attempting to remove trust for team ID: %@
Error cannot evaluate unknown platform (%d) for: %@
Invalid slice offset (%@) for: %@
Unable to extract signer type? path: '%@', info: '%@'
SecKeyCreate error: <unknown>
Dropping validation metrics because queue is full
[%s] missing profile: %@
[%s] setting demo state: %u
[%s] enabling MDM state
Invalid options combination cpuType: (%@) cpuSubType: (%@) sliceOffset: (%@) for: %@
MIS Validation successful, but unexpected info? path: '%@', options: %@, info: %@, cdhash: %@
[%s] Reporting developer mode settings visible because nearby pairable hosts were found
[%s] Nearby discovered pairable host disappeared: %@
[%s] setting supervised state: %u
[%s] unable to enable MDM: %@
[%s] auxiliary signature unsupported: %@
[%s] Discovered nearby pairable host: %@
Invalid cpu sub type (%@) for: %@
unable to allocate a SecAccessControlRef for the key access control
unable to allocate a CFNumberRef for the system boundary
[%s] must capture scheduled profile
[%s] attempting to commit profile: %@
[%s] attempting to remove staged profile
SecKeyCreate error: %ld (%s)
unable to extract public key bytes from public key: %d
[%s] unable to acquire staged profile: %@
[%s] xpc error: %@
[%s] data migration error: %@
[%s] Reporting developer mode settings not visible
successfully copied local signing private key
SecItemCopyMatching returned unknown object
successfully copied local signing private key from keychain
[%s] profile UUID must be provided
[%s] Not monitoring for pairable hosts since RemotePairingDevice is not loaded.
dyld_sim policy is not allowed on iOS: %@
found multiple (%ld) local signing keys in keychain
unable to allocate a CFNumberRef for the key size
[%s] request for profile: %@
[%s] attempting to set trust for team ID: %@ | %u
[%s] removing MDM state
%@ not valid: 0x%x: %@
the local signing private key is not available: %d
[%s] Reporting developer mode settings visible because AMFIShouldShowDeveloperModeSettings returned true
Invalid cpu type (%@) for: %@
Invalid flags (%@) for: %@
unable to allocate a CFMutableDictionaryRef for the key parameters
[%s] developer mode daemons error: %@
[%s] unable to check for reboot: %@ | %u
[%s] unable to create aux-sig: %@ | %@ (not-fatal)
```
