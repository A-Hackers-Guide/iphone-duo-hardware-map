# `/usr/libexec/driverkitd`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,403,168 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 40 (Size: 5488)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (23)

- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices (compatibility version 1.0.0, current version 1084.40.7, weak)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0)`
- `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libauthinstall.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libimage4.dylib (compatibility version 1.0.0, current version 374.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/swift/libswiftCompression.dylib (compatibility version 1.0.0, current version 18.0.0, weak)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDarwin.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.kernel.get-kext-info</key>
	<true/>
	<key>com.apple.private.sandbox.profile:embedded</key>
	<string>com.apple.driverkitd</string>
	<key>com.apple.private.security.iocatalog-management</key>
	<true/>
	<key>com.apple.private.security.kext-collection-management</key>
	<true/>
	<key>com.apple.private.security.storage.driverkitd</key>
	<true/>
	<key>com.apple.private.spawn-driver</key>
	<true/>
	<key>com.apple.private.xpc.launchd.job-manager</key>
	<string>com.apple.driverkitd</string>
	<key>com.apple.runningboard.launch_dexts</key>
	<true/>
</dict>
</plist>
```

## Objective-C (57 classes, 8 protocols)

Classes: `RunningBoardSupport`, `_TtC10driverkitd11OSExtension`, `_TtC10driverkitd12RealDistNote`, `_TtC10driverkitd12RealizedInfo`, `_TtC10driverkitd14UncachedBundle`, `_TtC10driverkitd15ApprovalManager`, `_TtC10driverkitd15DriverExtension`, `_TtC10driverkitd15DriverKitDaemon`, `_TtC10driverkitd15KernelExtension`, `_TtC10driverkitd15LPNAgentManager`, `_TtC10driverkitd16ApplicationCache`, `_TtC10driverkitd16DriverBinManager`, `_TtC10driverkitd16ExtensionManager`, `_TtC10driverkitd16KernelCollection`, `_TtC10driverkitd16RealKernelClient`, `_TtC10driverkitd17EmbeddedSIPStatus`, `_TtC10driverkitd17RealOSEnvironment`, `_TtC10driverkitd18ApplicationManager`, `_TtC10driverkitd18KernelStateManager`, `_TtC10driverkitd18NullLaunchServices`, `_TtC10driverkitd18RealBundleResolver`, `_TtC10driverkitd18RealDaemonLauncher`, `_TtC10driverkitd18RealLaunchServices`, `_TtC10driverkitd19RealCodeSigningInfo`, `_TtC10driverkitd20RealDeviceProperties`, `_TtC10driverkitd21RealXPCEventPublisher`, `_TtC10driverkitd22ActivationStateManager`, `_TtC10driverkitd22NullDeveloperKitClient`, `_TtC10driverkitd22NullLPNEventSubscriber`, `_TtC10driverkitd22NullSystemPolicyClient`, `_TtC10driverkitd22RealDeveloperKitClient`, `_TtC10driverkitd22RealFeatureFlagsClient`, `_TtC10driverkitd22RealLPNEventSubscriber`, `_TtC10driverkitd23DextLaunchThreadManager`, `_TtC10driverkitd23NullCoreAnalyticsClient`, `_TtC10driverkitd23NullRunningBoardSupport`, `_TtC10driverkitd23RealCodeSigningResolver`, `_TtC10driverkitd23RealCoreAnalyticsClient`, `_TtC10driverkitd24ApplicationRequestSource`, `_TtC10driverkitd24RealizedKernelCollection`, `_TtC10driverkitd25ActiveDriversStateManager`, `_TtC10driverkitd25MinimalDeveloperKitClient`, `_TtC10driverkitd25NullIOUserResourcesClient`, `_TtC10driverkitd25RealApprovalsXPCPublisher`, `_TtC10driverkitd25RealIOUserResourcesClient`, `_TtC10driverkitd26AllowAllSystemPolicyClient`, `_TtC10driverkitd26ApprovalStateUpdateRequest`, `_TtC10driverkitd26DriverKitDaemonSideEffects`, `_TtC10driverkitd27RestoreOSFeatureFlagsClient`, `_TtC10driverkitd28ApprovalSettingsStateManager`, `_TtC10driverkitd30AllowARVOnlySystemPolicyClient`, `_TtC10driverkitd33DriverKitDaemonXPCRequestDelegate`, `_TtC10driverkitd36DriverKitDaemonAppXPCRequestDelegate`, `_TtC10driverkitd7XPCUtil`, `_TtC10driverkitdP33_622D3D8EFA33E5821DB6E6A2F22719EA19StateManagerWrapper`, `_TtCC10driverkitd12RealizedInfo8LoadInfo`, `_TtCC10driverkitd23DextLaunchThreadManager27DextLaunchDebuggingMetadata`

Protocols: `NSObject`, `NSXPCListenerDelegate`, `OS_dispatch_source`, `OS_dispatch_source_mach_recv`, `OS_os_transaction`, `OS_xpc_object`, `_TtP10driverkitd29DriverKitDaemonClientProtocol_`, `_TtP10driverkitd32DriverKitDaemonAppClientProtocol_`

## Strings (1,230)

```
_TtC10driverkitd21RealXPCEventPublisher
_TtC10driverkitd26AllowAllSystemPolicyClient
_TtC10driverkitd15DriverExtension
OS_os_transaction
_TtC10driverkitd18RealBundleResolver
OS_xpc_object
NSObject
_TtC10driverkitd25ActiveDriversStateManager
_TtCC10driverkitd12RealizedInfo8LoadInfo
_TtC10driverkitd18NullLaunchServices
_TtC10driverkitd12RealDistNote
_TtC10driverkitd16ExtensionManager
_TtC10driverkitd18RealDaemonLauncher
_TtP10driverkitd32DriverKitDaemonAppClientProtocol_
_TtC10driverkitd18KernelStateManager
_TtC10driverkitd17EmbeddedSIPStatus
_TtC10driverkitd22NullLPNEventSubscriber
_TtC10driverkitd7XPCUtil
_TtC10driverkitd11OSExtension
_TtC10driverkitd16KernelCollection
_TtCC10driverkitd23DextLaunchThreadManager27DextLaunchDebuggingMetadata
RunningBoardSupport
_TtP10driverkitd29DriverKitDaemonClientProtocol_
OS_dispatch_source
_TtC10driverkitd18RealLaunchServices
_TtC10driverkitd22RealFeatureFlagsClient
_TtC10driverkitd23DextLaunchThreadManager
_TtC10driverkitd22RealLPNEventSubscriber
_TtC10driverkitd22NullDeveloperKitClient
_TtC10driverkitd24ApplicationRequestSource
_TtC10driverkitd14UncachedBundle
_TtC10driverkitd23NullCoreAnalyticsClient
_TtC10driverkitd24RealizedKernelCollection
_TtC10driverkitd16DriverBinManager
_TtC10driverkitd17RealOSEnvironment
_TtC10driverkitd15LPNAgentManager
_TtC10driverkitd28ApprovalSettingsStateManager
_TtC10driverkitd25MinimalDeveloperKitClient
_TtC10driverkitd23RealCoreAnalyticsClient
_TtC10driverkitd16ApplicationCache
_TtC10driverkitd26ApprovalStateUpdateRequest
_TtC10driverkitd16RealKernelClient
_TtC10driverkitd22NullSystemPolicyClient
_TtC10driverkitd15ApprovalManager
_TtC10driverkitd20RealDeviceProperties
_TtC10driverkitd18ApplicationManager
_TtC10driverkitd26DriverKitDaemonSideEffects
_TtC10driverkitd22RealDeveloperKitClient
_TtC10driverkitd27RestoreOSFeatureFlagsClient
NSXPCListenerDelegate
_TtC10driverkitd22ActivationStateManager
_TtC10driverkitd19RealCodeSigningInfo
_TtC10driverkitd23NullRunningBoardSupport
_TtC10driverkitd12RealizedInfo
_TtC10driverkitd30AllowARVOnlySystemPolicyClient
_TtC10driverkitd36DriverKitDaemonAppXPCRequestDelegate
_TtC10driverkitd23RealCodeSigningResolver
OS_dispatch_source_mach_recv
_TtC10driverkitd33DriverKitDaemonXPCRequestDelegate
_TtC10driverkitd15DriverKitDaemon
_TtC10driverkitdP33_622D3D8EFA33E5821DB6E6A2F22719EA19StateManagerWrapper
_TtC10driverkitd25NullIOUserResourcesClient
_TtC10driverkitd25RealApprovalsXPCPublisher
_TtC10driverkitd25RealIOUserResourcesClient
_TtC10driverkitd15KernelExtension
@16@0:8
B24@0:8#16
@40@0:8:16@24@32
^{_NSZone=}16@0:8
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v28@?0I8Q12@\"<OS_xpc_object>\"20
@24@0:8:16
B16@0:8
v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}12
Q16@0:8
@32@0:8:16@24
v24@0:8@?16
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
B24@0:8:16
v48@0:8@16@24@32@?40
v24@0:8@?<v@?@\"NSString\"@\"NSError\">16
v32@0:8@16@?24
B24@?0q8@\"<OS_xpc_object>\"16
@\"NSDictionary\"8@?0
B32@0:8@16@24
v16@?0@?<v@?q>8
Vv16@0:8
@\"NSString\"16@0:8
@40@0:8@16@24@32
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
B24@0:8@16
B24@0:8@\"Protocol\"16
v8@?0
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40
v16@0:8
v16@?0@\"<OS_xpc_object>\"8
v12@?0i8
#16@0:8
Internal error: Bin entry %s was inserted with incorrect bin number %s
Failed to read directory %s: %s. Attempting to create directory
Bundle at %s not in manager
kernel reports daemon is not active: %s
Could not copyfile:\nfrom: %s\nto: %s\nerror: %s\nerrno: %s
Failed to use entry %s: %s
invalid dextbin info, failed to read plist: %s
Available URLs: %s
invalid application cache, failed to read plist: %s
Retrieving applications from LaunchServices
Hardware %s third party drivers
Application %s has unexpected unique identifier, expected %s
Attempting to copy out driver extension:\n  installIdentifier: %s\n               from: %s\n                 to: %s
State refresh (id: %s, reason: %s): Notifying %s of state update
Failed to submit job: %{public}@
An error occurred while loading dext personalities: %s
Loading application cache, decoding data
Failed to handle queued request %s: %s
Failed to unload driver %s: %s
Found two applications with the same unique identifier %s:\n%s\n%s
Codeless info %s did not contain identifier for key %s
Bundle at %s does not have a bundle identifier
State refresh (id: %s, reason: %s): starting
Failed to write application cache: %s
Writing new application cache contents
Could not report driver install: could not resolve driver bundle at\n %s
Skipping bundle at %s since containing application was removed
contentsOfFile failed to read approvals database: %s
Failed to send notification to xpc event subscriber %llu
Found stale staged driver %s belonging to an uninstalled app
Saving dextbin info, encoding
%s
Loading dextbin info, reading plist file from %s
Bundle at %s is invalid
Skipping bundle at %s, already inserted into approvals database
Loading dextbin info, decoding plist
Authenticated: %s with result: %s
Failed to write approval database during state update: %s
Drivers with identifiers %s (%s), %s (%s) have the same unique identifier
Replacing old dextbin info contents
Failed to reuse existing bin entry: %s. Creating new bin entry
Difficulty removing %s: %s
Skipping addBreadcrumbForDextWithIdentifier for %s %ld
Validated: %s
Skipping third party driver %s at %s during first approvals database update pass
Job submitted but not running: %d
Omitting driver %s: does not have a bundle
Third party driver boot arg %s enabled
Codeless info %s did not contain data for key %s
Skipping bundle at %s, already inserted into new bin with UUID %s
Will remove untracked file %s, since it is not the expected Info.plist at %s
contentsOfFile failed to read plist: %s
Saving appproval db, encoding
Loading application cache from %s
Using cached application list
Removed untracked path %s
invalid approvals database, failed to read plist: %s
Loading approvals database, decoding data
State refresh (id: %s, reason: %s): completed
%{public}s
contentsOfFile failed to read application cache: %s
Third party drivers are disabled
Found actively used drivers that are missing:\n%s
Will remove untracked directory %s
State refresh (id: %s, reason: %s): %s updated state, will notify subscriber: %s
State refresh (id: %s, reason: %s): %s updated state:\n%s
unexpected error checking if daemon is active %s
Codeless info %s did not contain path for key %s
Failed to create active list: %s
Writing new dextbin info contents
Could not create directory %s: %s (errno %s)
Skipping removeBreadcrumbForDextWithIdentifier for %s
Writing new approval db contents
Loading approvals database from %s
Replacing old application cache contents
Can't save dextbin info: %s
Failed to stage driver %s from app %s
Could not insert bundle at %s into manager: %s
Omitting third party driver %s at %s: app is not installed
Failed to create directory %s: %s
Copying old active bin entry %s with bin number %s
Replacing old approval db contents
State refresh (id: %s, reason: %s): %s did not update state
Drivers that should be unloaded:\n%s
Internal error: found multiple realized infos for %s in manager
OSBundleIsInterface
AppleSecurityExtension
Inserted new driver 
matchesIncludeFilter
IOUserServerName
Received update notification for 
error: tried to insert an invalid ext in restricted lookup table: %{public}s
Error occured while reading kextinfo from kernel: 
' on IOUserResources: 
Img4 format not .im4p (%d), attempting to decode as .img4
== Driver Extensions by URL:\n
Ignoring kext at %{public}s with incompatible architecture.
Serialization failed.
ApprovalSettingsStateManagerQueue
force-try failed
system kext collection
Error occurred while using kclist: 
Found no registered drivers with identifier 
ExtensionRealizing
Launching driver extension failed: 
com.apple.developer.driverkit
Swapping big-endian fat header.
 was inserted with incorrect UUID 
Handled queued request 
No elision list for `%{public}s`
 was already specified.
com.apple.message.fat
CollectionRealizing
Cannot realize extra load info from 32-bit collection.
XPC Event %{public}s: Pending subscriber %llx replied with error %{public}s
distnoted event, dictionary contents:\n%{public}s
Invalid ownership (
DextLaunch
\nUserspace Architecture: 
kind: %{public}s
Driver Extension Server Tag
Kext Unload Notification
^[0-9]{4}-[0-9]{4}$
com.apple.kernelmanagement.dextLaunch
migrateAuxKCForVolumeGroupUUID failed: 
Kernel request failed: 
Unknown extension type for 
com.apple.driverkitd
distnoted event caught with unexpected payload; xpc handler called for xpc object of type `%{public}s`
KMError while getting scoped approval state: %{public}s
Attempt by unentitled pid %d to access interface
(NOT AN ERROR) Kernel requested shutdown. Goodbye!
Launching driver extension via running board: %{public}s
CheckCodeSignValidity
anchor apple generic
com.apple.message.teamid
kOSBundleDextUniqueIdentifier
Failed to find existing bin entry for 
XPC Event %{public}s: Removing subscriber %llx
State refresh
Invalid Request: 
packageInstallerError
Failed to get signature type: Unable to create SecRequirement for checking Developer ID: %lu
kextsOutOfOSImageFeatureFlags: %{public}s
Could not get path of main executable.
Found multiple codeless kexts with the same identifiers, will use the known one: \n\tknown path: %{public}s \n\tduplicated path: %{public}s
Duplicate extension error :
Subscribed to service: %{public}s
Decompression buffer size %d (try %d)
Binary does not have valid magic
Dictionary<String, String>
GT
Connection with client pid %d interrupted.
Failed to process MIG message.
Not compressed; returning existing data. (%d)
com.apple.message.hash
matchesExludeFilter
driverkitd/DriverKitDaemon.swift
Invalid check in token port: 
Img4 error: format neither im4p nor img4 (%d)
KextsOutOfOSImage
Driver Extension Server Name
CPU Type is not a number?
Error occurred while demuxing request %{public}s: %{public}s
Using unique id %{public}s to pick dext matching bundle identifier %{public}s
multiple candidates found for 
(kernel): %{public}s
SPKernelExtensionPolicy is unavailable, AllowARVOnlySystemPolicyClient cannot notify unsupported kexts at: %{public}s
Discovered LPN agent: %{public}s
Skipping dext bundle validation on ARV at %{public}s
Error occurred while building a collection: 
Unexpected call to createLaunchContext(identity:)
Unexpected call to applicationRecord(fromAuditToken:)
Dext Daemon Launch
Wanted version of 
Validating extension failed: 
, cannot check code signature.
Encountered error while scanning load commands for arch 
 must have valid Apple copyright string
init()
 has an invalid or missing version.
dependenciesAuthenticated
Driver Bin Changed
Could not get contents of main executable.
%{public}s is marked as LPN agent but is not a platform dext
Error occurred while handling request \"%{public}s\": %{public}s
subscribe(serviceName:scope:type:)
_InfoPlistDigest
Incoming app request for scoped approval state from pid %d
No authentication enabled, trusted
contentsOfFile failed on `%{public}s` for `%{public}s`, errno: %{darwin.errno}d
Another collection at 
\n\nRepositories: 
Initializing with settings: %{private}s
An error occurred while loading 
/private/var/tmp/com.apple.driverkitd/driver-approvals.plist
com.apple.driverkitd.daemonInit
Request enqueued at 
DaemonExtensionPaths
UserDriverExtensionsDirectory
ApprovalsError while getting approval state: %{public}s
\n\nKernel Architecture: 
,\nrequiredIdentifiers: 
_PrelinkInfoDictionary
error: tried to insert an invalid codeless kext in restricted lookup table: %{public}s
The codeless exceptions configuration is not provided, skip codeless forceloading
Incompatible architecture: 
Failed to create event dictionary for: %{public}s
DriverBinManager
Binary is fat.
OSBundleUsageDescription
com.apple.KernelManagementPingServer
com.apple.kernelmanagerd.KernelRequestSource
Cannot add subscriber with different state manager queue
IOKitPersonalities
Could not get contents of 
%{public}s found in built-in deny list
Apple prefix trusted
Rejected by exclude list
 does not contain a bundle identifier
com.apple.message.issuercn
Kext Load Request
Set first party driver 
Exception list trusted
optionalIdentifiers
Arithmetic Error: 
' should have type 
Could not create bundle for 
Could not create extension from bundle at 
Could not find extension for non-identifier lookup
Could not find extension with identifier 
com.apple.dext-lpn
Incoming request for approval state
Unable to get log flags and messages.
Failed to enter sandbox: 
Could not determine running userspace architecture.
Could not find: 
com.apple.driverkitd.kernel-requests
 linked against 
MS decoder error: 
DarwinOS error: 
Authenticating extension failed: 
Encountered error: %{public}s
3rd-party kext without Apple root
com.apple.message.kextexecpath
 to get executable for 
boot kernel collection
Prelink info has no _PrelinkInfoDictionary
Fileset entry found for %{public}s, but not included in prelink info
Get Kexts in Collection
unable to create extension from '%{public}s', unrecognised package type '%{public}s'
Realize dext %{public}s
kextsOutOfOS
OSBundleRequired
Trusted Apple kext in collection
File age limit of %d seconds from boot args is too small (minimum %d seconds), using default %d seconds
' has invalid properties: 
Found multiple drivers with identifier 
Could not find entry with device tree path 
driverkitd/DaemonSupport.swift
IOUserServerCDHash
dependenciesValidated
Collision: replacing %{public}s
_NullBootstrapPort
Could not get creation date for dext core at %{public}@: %{public}@
\nAuxiliary Bundle Paths: 
Unable to resolve dependencies: 
missing bundle after lookup
%{public}s matches %{public}s.
Created directory at 
 has no predicate
ProgramArguments
 is a symlink to 
runninglistError
consistencyCheck
EQ
 in approvals database
com.apple.KernelManagement
Set third party driver from bin entry 
Loading extension failed: 
buildManifestNotFoundError
Arithmetic overflow detected while computing offset for the end of the slice\nSlice architecture: 
 is too large\nArithmetic overflow detected while adding with 
installSessionIdentifier
Get Kernel Requests
XPC Event %{public}s: Unexpected reply from previously pending subscriber %llx
SoftResourceLimits
Received an unexpected null/empty response for request: 
 not approved to load. Please approve using System Settings.
 is not approved to load. Please approve using System Settings.
ActivationStateManager
Active Drivers:\n
Skipping FS validation for kext already in collection 
Safe boot error: 
warning: libcompression not linked; returning existing data.
' should be one of the values: 
com.apple.kernel.
Unexpected call to %s
com.apple.kernel
activate()
DeniedIdentifiers
ExtensionAuthentication
Fatal error
Finished extension FS validation with result: %{public}s
 is not a directory
Trying to overwrite existing entry with uuid 
Unrecognized predicate 
SPKernelExtensionPolicy is unavailable, AllowAllSystemPolicyClient cannot notify unsupported kexts at: %{public}s
Could not determine running architecture.
AllExtensionsPaths
dext-core-age-limit
Recovery environment specific error: 
collectionLinkage
com.apple.driverkitd.NSXPCAppRequestSource
Ptrauth ABI mismatch: binary is built against version 
unknown collection
Could not find configuration data in executable section for architectures 
dumpState(withReplyBlock:)
Daemon has activated
OSBundleWiredSize
incompatibleArchitecture
, but found that the directory does not exist
driverkitd/XPCEventPublisher.swift
Applications Uninstalled: 
Skipping %{public}s, manager settings does not contain a path to it
developerToolsError
Unrecognized identifier: %s
Failed to read bundle at 
Invalid cdhash value '
Prelink info section has no _PrelinkKCID
Codeless Personalities
driverkitd.NSXPCRequestSource
Unknown MIG message received.
Unable to bridge xpc event dictionary
Could not list contents of dext cores directory: %{public}@
OSBundleRetainCount
com.apple.message.kextpath
 contains no executable.
 approval state to default 
Bundle or the bundle id is nil: %{public}s
,\noptionalIdentifiers: 
Unable to stage extension: 
An unknown error occurred while building the cache.
ApprovalsManager
driverkitd/Utilities.swift
LT
 and unique identifier 
Loading extension(s): 
inserted dext, then could not look it up
Falling back to arch %{public}s
kextsInKDK
Invalid UTF-8 elision list for `%{public}s`
No identifier in kernel request for dext launch
ApplicationCache
' should have type String with a maximum length of 
Could not create enumerator for 
OSKextStrictExceptionHashList
CFBundleIdentifierKernel
Unable to find '__info' section.
Subscribed Services: 
No codeless bundle needs to be force loaded.
incompatibleVersion
KernelFileSetLoadRequest
/Library/Extensions/AppleKIS.kext
Successfully triggered IOKit matching for: %{public}s
Successfully inserted extension: %{public}s
Unable to create SecStaticCodeRef at 
com.apple.message.architecture
SPKernelExtensionPolicy is unavailable, NullSystemPolicyClient cannot notify unsupported kexts at: %{public}s
Request to strictly match a dext of bundle identifier 
com.apple.LaunchServices.applicationRegistered
signing information did not contain a signing identifier
Data compressed with %{public}s
Scoped %lu of %lu cached approval entries to install session %{private}s: [%{private}s]
Did not find dext with bundle identifier 
, but needed arch 
Binary not large enough to accomodate fat header
AppleKernelExternalComponent
OSKextExcludeList
Invalid identifier and version 
== Driver Approval Database:\n
 is not in the allowed list of user server names: 
%{public}s is marked as LPN agent but has no personalities
Bundle URL %{public}s is a valid symlink to %{public}s
. Should only appear in one of the directories reserved for driver extensions: 
Tried to force load extensions from bundles on disk into Manager's lookup table. But the settings flags indicate that the Lookup Tables are restricted
_JetsamPropertiesIdentifier
Error while enqueuing update to approval state: %{public}s
: should not be group/other writable
Communicating with kernel failed: 
Binary not large enough to accomodate 32-bit header
Header was already determined to be 64-bit.
Unexpected call to createLaunchRequest(context:)
Unable to read extension: 
globalError
unable to read Mach-O header as a 32-bit or 64-bit Mach-O header
Could not determine running kernel architecture.
Could not get unstaged real path for %{public}s, cannot determine if absent executables are okay
OSBundleDependencies
com.apple.security.get-task-allow
Registered event handler for: %{public}s
Received MIG message
Other validation error: 
ExtensionValidation
DextRecord Error: 
Unsupported Error: 
setHandler(queue:handler:)
Could not copy signing information
Can't save dextbin info, resetting driver bin
 is not a driver extension.
Received unload notification for 
Can't resolve code signing info of extension without a bundle
getBuildVersion(for:)
Could not initialize ExtensionManager
    Staged bundle: 
Bundle contains symlink pointing outside of itself: 
Starting driverkitd (%{public}s)
Could not determine if absent executables are allowed for %{public}s: %{public}s
driverkitd.KMDoublyLinkedListNode
\nApproval State: 
UserSystemExtensionsDirectory
Received unload notification for bundle ID %{public}s
BuildManifestNotFoundError: 
DeveloperTools Error: 
Could not insert new entry to database
trying to insert a dext in KernelManagerDaemonLoadableExtTable: %{public}s
OSBundleLoadSize
Error reading the AppleKextExcludeList: 
Could not parse binary: 
Error while managing resource: 
Slice offset lies outside the binary\nSlice architecture: 
 for architecture 
LE
Error encountered executing subprocess: 
insufficientPermissions
Artifact is not a valid fat Mach-O
(NOT AN ERROR) Starting driverkitd (%{public}s)
Cannot use resolveSignatureOrGenerateAdHocOne with adhoc strategy
driverkitd/DriverBinInfo.swift
registering handler for xpc event stream: `%{public}s`
incoming connection from pid %d
 not large enough to accomodate all fat headers with total size 
These properties should be absent: '
3rd-party kext with devid+ certificate
Arbitrarily picking first dext with bundle idenfier %{public}s
Looking for the %{public}s
finding bundles at additional paths: %{public}s
Error interacting with logging system: 
' must be a valid kext version
Will skip code sign validation of dext in the ARV at %{public}s
distnoted event, could not make info object
distnoted app uninstallation event, processing bundle: %{public}s
NSError while decoding update to approval state: %{public}s
 is a symlink with an invalid parent directory. Symlinks are allowed from these parent directories: 
com.apple.driverkitd state at 
subprocessFailed
System/Library/CoreServices/SystemVersion.plist
KernelManagement_executables-514.40.8
Cannot insert more than one of the same kind of collection.
Filesystem error: 
systemExtensionWaitForUninstallTermination
openat_authenticated_np() failed at path %{public}s with (errno %d)
Invalid match specification '
Staged application 
OSBundleCompatibleVersion
 does not have a personality dictionary.
Error occurred while dumping kernelmanagerd state: 
No keys can have the prefix 'com.apple.kernel.'
Could not find bundle for driver 
DaemonCheckIn
com.apple.km.driverkit.install
    Driver Extensions:\n
Error while getting scoped approval state: %{public}s
== DriverBinManager\n
No dext cores found, nothing to clean up
No dexts with bundle identifier %{public}s matched unique id %{public}s
Attempted to load an AppleKextExcludeList which wasn't a kext?
Force update for activation
com.apple.kpi.iokit
/Library/Extensions/Astris-IOUSBHostFamily.kext
listener(_:shouldAcceptNewConnection:)
) should be (0:0) on 
excludedIdentifiers
<unknown security error>
 is too large\nArithmetic overflow detected while multiplying with 
dependenciesValid
Staging directory 
kernelCollectionBuild
unapprovedToLoad
com.apple.applicationservice.matching
Could not create SecRequirement for 
Binary not large enough to accommodate magic
App connection from pid %d resolved to an application record with no install session identifier; failing closed
EnvironmentVariables
/Library/StagedExtensions
Failed to trigger launch for %{public}s: %{public}s
Error occurred checking UUIDs: 
warning: libImg4Linked not linked
Server name: %{public}s
KMError while getting approval state: %{public}s
\t%{public}s
 was never attached
IODeviceTree:/product
, but needed version 
Got invalid service port.
/private/var/tmp/com.apple.driverkitd/applications.plist
Application record is missing driver extension paths
Cannot determine UUID
Pending Requests 
Approval database changed
com.apple.driverkitd.DriverApprovalsChanged
DriverkitExtensionLoad
App server name: %{public}s
<no-bundle-identifier>
_BundleCollectionType
SystemVolumeSystemKernelCollection
Received LPN agent event for service: %{public}s
inserting a valid codeful kernel extension in restricted lookup table: %{public}s
AkelExtensionLoad
Cannot use adhoc strategy on this platform
OSBundleRequireExplicitLoad
App with install session identifier 
 is in exclude list: 
Unable to get real path of symlink at 
Skipping FS validation for kext 
Using file age limit from boot args: %d seconds
No unique identifier available to disambiguate between dexts of bundle identifier %{public}s
\nBundle Identifiers: 
CPU Subtype is not a number?
Platform binary trusted
 has invalid or missing package type
Unable to resolve dext with identifier 
,\nrequiredPaths: 
System policy error: 
missingDeveloperKit
Failed to get signature type: Unable to create SecRequirement for checking Apple root: %lu
requiresExplicitLoad
Collection had no prelink UUID key?
com.apple.kernelmanagement.dextcorecleanup
Could not find the system version plist (%{public}s)
driverExtensionPaths
PlatformExtensionPaths
 without the needed unique identifier
Subscriber graph contains a cycle after adding 
Slice ends at an offset outside the binary\nSlice architecture: 
Properties under 
 has no identifier
Could not write to FileHandle %{public}s: %{public}s (contents: '%{public}s')
com.apple.DriverKitExtensionServer
Skip the codeless kext that is not in the force load list: %{public}s
OSBundleDextStateActive
realizedInfo for (%{public}s) may not contain info on uuid or bundleArch
FS validation skipped
Kernel requested shutdown. Goodbye!
Could not initialize Config
appInstallSessionIdentifier
Cannot force launch driver on release builds.
Error while encoding approval state for reply: %{public}s
KernelStateManager not set
Found %{public}d dexts with bundle identifier %{public}s
unable to load extension: %{public}s: %{public}s
, Slice offset: 
ReadPrelinkInfo
Processing pending requests from the kernel, if any
KDK-Installer Error: 
kdkInstallerError
NSHumanReadableCopyright
driverkitd/main.swift
/Library/Extensions
Failed to force load codeless kexts: %{public}s
Unexpected call to %s for %s
CFBundleIdentifier
Terminate IOServices
unapprovedToLoadMultiple
Img4 payload length: %d
 with a size in the range [
com.apple.root.installed
com.apple.message.signaturetype
IOPersonalityPublisher
/System/Library/Extensions
/Library/Extensions/AppleKIS.kext/Contents/PlugIns/AppleRSMHost.kext
No unstagedURL found for %{public}s, cannot determine if absent executables are okay
.xpc.connection.
CodelessSearchPaths
 with user server name 
driverkitd/StateManagement.swift
/private/var/tmp/com.apple.driverkitd/DriverExtensions
Kext Request Arguments
3rd-party kext with Apple root
 requires arguments, but none were provided
BootKernelCollection
_NeedsSystemThreadGroup
Third-party kext in collection
install session identifier for calling application
LPN agent event missing event name
New approval update request
Activation state changed
anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] and certificate leaf[field.1.2.840.113635.100.6.1.13] and certificate leaf[field.1.2.840.113635.100.6.1.18]
Binary not large enough to accommodate headers
com.apple.km.driverkit.approval
Invalid state transition for 
Other validation Error: %{public}s
Received update notification for bundle ID %{public}s, unique ID %{public}s
error: tried to insert an invalid codeful kernel extension in the restricted lookup table: %{public}s
Boot Collection: 
Skipping %{public}s, cannot map
Code signature error: 
Already added subscriber 
com.apple.message.subjectcn
_DextCheckInPort
Kext Request Info Keys
XPC Event %{public}s: Pending subscriber %llx replied with unexpected type %{public}s
ForceLoadCodelessIdentifiers
com.apple.dext.asan
invalidProperties
Audit token did not resolve to an application record
, resulting in approval state update
Ignoring load notification: %{public}s
reporting %d newly unsupported kexts to syspolicyd after AKEL update:
ApplicationManager
KernelStateManager
signing information did not contain an executable url
Decompressed data: %d bytes.
com.apple.message.version
Application record is missing unique install identifier
 has an invalid format.
Error deriving adhoc signature for %{public}s: %{public}s
com.apple.private.security.driver-management
Error occured while running subcommand '
allowing Apple-prefixed bundle '%{public}s' installed from a root
Arithmetic overflow detected while adding slice offset 
/Library/Caches/com.apple.xbs/01140AD0-7A8D-4CDD-A311-AE4EC8D7E233/TemporaryDirectory.pQ4EeA/Sources/KernelManagement_executables/core/Errors.swift
Cannot add self as subscriber
Any
== Activation State Manager\n
ForcedFullBundleLoad
Found codeless bundles matching the ids listed in codeless exceptions: %{public}s
Format appears to be from the future: 
Could not find property 
daemonInit()
== Driver Extensions by identifier:\n
Sent new drivers
 was removed from the staging location, removed from manager
skipped ARV dext FS content validation
Invalid parent directory for 
Can't determine owner/permissions for 
 Apple Inc. All rights reserved.
OSBundleLibraries
Read elision list from `%{public}s` for `%{public}s`
Executing dextcore cleanup pass
(NOT AN ERROR) Launching dext %{public}s %{public}s 0x%llx %{public}s
Figuring out dext launch context: %{public}s
 into a restricted lookup table
Unable to deserialize kernel response.
Deserialization failed: 
com.apple.message.kextname
inSignatureExceptionList
Reading exclude list from %{public}s
Resource load failed (error 
systemExtensionsError
errorDescription
Signing information did not contain a cdhash
Binary not large enough to accomodate fat arch headers
OSBundleAllowUserLoad
unsupportedError
Prelink info has no _PageableKCID
ApprovalsDatabasePath
Dext cores directory does not exist, nothing to clean up
 compatible with version 
Failed to read configuration file: 
Could not getBuildVersion since no side-effects found
com.apple.driverkitd.NSXPCRequestSource
OSBundleOptionalAuxKC
Prelink info value for ManagerVersion is not an integer
Manager version is 
 is not a valid tag number
unable to create extension from '%{public}s', bundle contains no Info.plist contents
KextsOutOfOSImageFeatureFlags should have only one checkpoint enabled. Found %{public}s
OSBundleExecutablePath
Encountered errors while reading executables: %{public}s
Could not find entry with driver identifier 
Applications Installed: 
Received event for unknown service: %{public}s
Dext Daemon Upgrade
Dext core missing creation date, skipping: %{public}@
SysExtensionWaitForUninstallTerminationError: 
, refusing to insert 
IOKit Daemon Exit
Validation Error: %{public}s
Daemon Activation
Unable to deserialize log data.
Failed to set temp directory
XPC Event %{public}s: Added new subscriber %llx (%{public}s)
Swift/NativeDictionary.swift
OSBundleLoadAddress
Missing Developer Kit: 
Can't find arch %{public}s in binary
SystemKernelCollection
AuxiliaryKernelCollection
requiredIdentifiers
_PrelinkBundlePath
Application cache has wrong version
[Error] Interval already ended
driverIdentifier
Unable to bridge job launch dictionary
Invalid bundle signature for 
No team ID in signing dict and no Apple-prefix in signing identifier.
com.apple.message.bundlePath
inserting to insert an unknown but valid extension into restricted lookup table: %{public}s
triggerPanicMedic
com.apple.get-task-allow
Pid: %d
XPC Event %{public}s: Pending subscriber %llx
HardResourceLimits
Internal error: unexpected extension type?
Updated cached state for settings
Could not find plist 
ProductBuildVersion
inStrictSignatureExceptionList
 which is not contained in a valid platform extensions directory
DaemonActivation
 is missing linkage metadata
Unable to read contents of file at 
Error occurred unloading extensions: 
Successfully set property '%{public}s' on IOUserResources
Could not create SecRequirement 
Application landscape changed
Error launching dext \"%{public}s\": %{public}s
OSBundleMachOHeaders
com.apple.km.logging
Subscribed to LPN agents: 
Validating extension at %{private}s
FS contents are valid
ReslideSharedCache
Duplicate values for key: '
Warning: com.apple.driver.KextExcludeList was not found!
Could not search for bundles in auxKC: %{public}s
Could not look for bundles in %{public}s
unable to create extension from '%{public}s', Info.plist digest is missing
dependenciesAuthentic
Invalid number of keys found, expected one.
dext_asan_sb boot-arg present: %d
ApplicationCachePath
Invalid permissions 
Could not remove dext core at %{public}@: %{public}@
Unexpected request 
, but only found version '
== Application Manager\n
Adhoc cdhash: %{public}s
Configuration has unrecognized format.
incoming app connection from pid %d
com.apple.developer.system-extension.install
Error encountered while deserializing: %{public}s
 requires a reboot
Could not read the system version plist from %{public}s: %{public}s
 was unapproved, removed from manager
, is not a DriverExtension
 contains no executable
SysExtensionWaitForTerminationError: 
User server name 
Internal error: 
(anchor apple\n    or (anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.9] exists)     or (anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] exists     and certificate leaf[field.1.2.840.113635.100
' should be absent
EXACTLY ONE OF: 
Set of active drivers changed
LimitLoadToSessionType
In exclude list: 
Application record is missing identifier
Prelink info has no _BootKCID
com.apple.distnoted.matching
Dext bundle for 
Couldn't find extension's bundle
%{public}s %{public}s 0x%llx %{public}s
 requires an Apple kext
com.apple.message.codeless
Application record is missing install session identifier
auxiliary kext collection
Driver Bin Version 
Attempt by unentitled pid %d to access app interface
' should be a collection of type 
 (unique identifier 
GE
    Application: 
Unknown CPU type %d with subtype %d
Picked matching dext for bundle identifier %{public}s: %{public}s
Failed to read info dictionary for driver 
, check in port 
/Library/Apple/System/Library/Extensions/AppleKextExcludeList.kext
systemExtensionWaitForTermination
CFBundleGetInfoString
 containing staged bundle 
Extension with identifier '
. Should not appear in any of the directories reserved for driver extensions: 
Warning: %s is already attached
Adhoc signature; forcing no team ID
CopyCodeSignInformation
Apple kext with Apple root
OSKextSigExceptionHashList
OSBundleTeamIdentifier
Insufficient permissions for action: 
 and slice size 
OSKernelCPUSubtype
Updated loaded info for %d extensions.
CFBundleDisplayName
com.apple.DriverKitAppServer
supports-third-party-drivers
com.apple.private.driverkit.use-system-thread-group
Launching dext %{public}s %{public}s 0x%llx %{public}s
DriverKit Reslide Shared Cache
Kext Load Notification
contentsOfFile failed on `%{public}s`, errno: %{darwin.errno}d
,\nexcludedIdentifiers: 
Error occurred triggering Panic Medic: 
Extension with identifier 
Building kernel collection failed: 
IOService:/IOUserResources
uniqueInstallIdentifier
Unable to determine signature for %{public}s, generating adhoc signature... (%{public}s)
Driver extension %{public}s cannot use the system thread group because it is associated with application %{public}s
Could not find IOUserResources entry
Binary not large enough to accomodate 64-bit header
Cannot decompress: Invalid buffer. Returning existing data
OSBundleSharedExecutableIdentifier
OSKernelResource
Latest Drivers:\n
    Install Session Identifier: 
ApprovalSettingsState: 
BaseSystemKernelCollection
Error getting kernel requests: %{public}s
com.apple.driver.KextExcludeList
inserting a valid codeless kext in restricted lookup table: %{public}s
dependencyResolution
com.apple.km.driverkit.launch
    Unique Identifier: 
Unexpected daemon queue request 
packageInstaller Error: 
Boot policy error: 
missingDependencyRequest
com.apple.private.driverkit.driver-launch-configuration
com.apple.LaunchServices.applicationUnregistered
kern.osbuildconfig
Initialization error: 
Unexpected call to createIdentity(serverName:tagString:containingAppBundleID:)
driverkitd/Validation.swift
Failed to set property '
ActiveDriversStateManager
Decompression error (decoding buffer returned 0 size!); returning existing data.
(no collection, personalities only)
DaemonInitComplete
xpc event stream handler registered for: `%{public}s`
XPC Event Handler %{public}s error: %d
Dext core at %{public}@ removed
Extension with identifiers 
kernelCommunication
com.apple.kpi.private
DaemonInitStarted
distnoted app installation event, processing bundle: %{public}s
knoxDownloaderError
' should have type String with prefix: 
com.apple.rootless
bundleIdentifier
Driver Identifier: 
Kext Resource Request
Connection with client pid %d invalidated.
ThirdPartyDriverKitStagingDirectory
Launching driver extension: %{public}s
OSBundleCPUSubtype
Bootstrap check in failed: 
<Missing Identifier>
com.apple.message.bundleID
com.apple.message.personalitynames
Kext Request Predicate
does not support
_CodelessKextBundlePath
%{public}s, uuid %{public}s %{public}svalid %{public}sauthentic %{public}sapproved
Invalid DriverBinInfo version: expected 
Invalid argument: 
Failed to create XPC event publisher 
Could not find variant.
allowThirdPartyDexts
Bad code signature
Warning: %{public}s was not found!
Unable to insert extension: %{public}s
Collection linkage invalid: 
duplicateExtension
NullIOUserResourcesClient: setProperty('%{public}s') called
, Offset for end of slice: 
auxiliaryOptional
Found existing approval database entry 
PlatformDriverExtensionsDirectories
, could not find dext
finding bundles in repositories: %{public}s
KcgenFlow apis sequence error: 
kernelmanagerd
 was uninstalled, removed from manager
forcing checkpoint to %{public}s
com.apple.message.signingtime
AuxiliaryExtensionPaths
, which does not have path prefix 
ApprovalSettingsStateManager
approvalManager
auditToken
callback
listener:shouldAcceptNewConnection:
pendingSubscribers
superclass
$__lazy_storage_$_inRecovery
validationErrors
predicateFormat
$__lazy_storage_$_inFVUnlock
$__lazy_storage_$_thirdPartyDriverBootArgEnabled
_historyItems
digest
repoIndex
initWithContext:
$__lazy_storage_$_enableSerialLogging
activeDriversStateManager
autorelease
createFileAtPath:contents:attributes:
fileHandleForWritingAtPath:
identifier
loadInfoDict
respondsToSelector:
$__lazy_storage_$_kernelCacheUUID
bootCollectionUUID
fm
launchDriverWithBundleID:userServerName:tag:replyBlock:
setExportedObject:
requests
semaphore
setDextCheckInPort:
settings
executablePath
setExecutionOptions:
init
subscribers
block
bundleURL
createDirectoryAtURL:withIntermediateDirectories:attributes:error:
debugMetadataDoublyLinkedList
location
performSelector:
rss
issuerCN
retain
bundleRecordForAuditToken:error:
daemonCheckInInterval
dispatchSource
initWithURL:
$__lazy_storage_$_inBaseSystem
T@\"NSString\",R,C
extensionManager
requestQueue
connection
entitlements
isKindOfClass:
URL
$__lazy_storage_$_hardwareSupportsDrivers
currentSize
databasePath
entry
initWithIdentifier:
$__lazy_storage_$_inMainOS
activationStateManager
applicationCache
uuid
queue
value
$__lazy_storage_$_enableKextLogging
bundleIdentifier
evaluateWithObject:
$__lazy_storage_$_inDarwinOS
codelessForceLoadLists
driverBinManager
performSelector:withObject:withObject:
publisher
self
setBundleIdentifier:
loadState
teamID
attributesOfItemAtPath:error:
head
setInterface:forSelector:argumentIndex:ofReply:
arch
code
exportedInterface
processPendingRequestsOnActivation
stateManagerQueue
pid
contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
infoDictionary
kernelStateManager
name
valueForEntitlement:
cst
_setAdditionalEnvironment:
bundle
uniqueInstallIdentifier
release
applicationCachePath
unstagedURL
csi
$__lazy_storage_$_kcSuffix
$__lazy_storage_$_inKcgen
_activated
dkdSignposter
forceLoadedBundlesAlready
retainCount
identityForDextWithServerName:tagString:containingAppBundleID:
performSelector:withObject:
contents
installSessionIdentifier
removeItemAtURL:error:
TQ,R
_loadInfo
interfaceWithProtocol:
setInvalidationHandler:
$__lazy_storage_$_infoLocation
vers
defaultManager
path
setRepeats:
uaklPath
_driverBinInfo
_subscribers
identifierVsDextLaunchDebugMetadata
replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
submitAndStart:
setInterval:
signingIdentifier
tail
lpnAgentManager
$__lazy_storage_$_nextInfoLocation
bundleElisions
mainBundle
class
conformsToProtocol:
enumeratorWithOptions:
systemDomain
$__lazy_storage_$_dextASanSandbox
builtInPlugInsURL
cacheLoadAddress
initWithMachServiceName:
_table
enqueueApprovalStateUpdateWithEntry:replyBlock:
execute:
lock
dealloc
approvalSettingsStateManager
contextWithIdentity:
description
$__lazy_storage_$_inSafeBoot
kextHistory
localizedInfoDictionary
_cached
context
val
timeInfo
collection
initWithDomain:code:userInfo:
listener
originURL
hash
historyItem
.cxx_destruct
T#,R
dumpStateWithReplyBlock:
getApprovalStateForCallingAppWithReplyBlock:
loadInfo
$__lazy_storage_$_disableAuxKCAtBoot
initWithPlist:domain:
processIdentifier
table
daemon
pageableCollectionUUID
subscribedServices
$__lazy_storage_$_inRestore
stringFromDate:
fileExistsAtPath:isDirectory:
isEqual:
kind
localizedFailureReason
nextObject
resume
directory
setArguments:
zone
applicationManager
isMemberOfClass:
unlock
_setQueue:
se
setQualityOfService:
$__lazy_storage_$_isAppleInternal
$__lazy_storage_$_bootArgs
_activeDriverSet
info
subjectCN
flags
lpnAgents
prev
recursiveLock
scheduleWithBlock:
setDelegate:
ext
$__lazy_storage_$_processInfo
debugDescription
getApprovalStateForSettingsWithReplyBlock:
maxCapacity
next
setExportedInterface:
setTimeZone:
signingTime
state
cdHash
exceptionLists
extensions
lockedState
setInterruptionHandler:
timestamp
settingsQueue
isProxy
$__lazy_storage_$_variant
_approvalDB
driverExtensionPaths
servicePort
_setOverrideExecutablePath:
manager
T@\"NSString\",?,R,C
_cfBundle
bundleArches
data
```
