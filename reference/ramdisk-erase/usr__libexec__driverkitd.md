# `/usr/libexec/driverkitd`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,403,168 bytes.

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
_TtC10driverkitd22NullDeveloperKitClient
_TtC10driverkitd18KernelStateManager
_TtC10driverkitd17EmbeddedSIPStatus
_TtC10driverkitd30AllowARVOnlySystemPolicyClient
_TtC10driverkitd25NullIOUserResourcesClient
_TtC10driverkitd22RealLPNEventSubscriber
_TtC10driverkitd15KernelExtension
OS_dispatch_source_mach_recv
_TtC10driverkitd23DextLaunchThreadManager
_TtC10driverkitd16ExtensionManager
_TtC10driverkitd11OSExtension
NSXPCListenerDelegate
_TtCC10driverkitd23DextLaunchThreadManager27DextLaunchDebuggingMetadata
_TtC10driverkitd33DriverKitDaemonXPCRequestDelegate
_TtC10driverkitd22ActivationStateManager
_TtC10driverkitd15DriverExtension
_TtC10driverkitd18ApplicationManager
_TtC10driverkitd25ActiveDriversStateManager
_TtC10driverkitd24RealizedKernelCollection
_TtC10driverkitd25RealIOUserResourcesClient
_TtC10driverkitd19RealCodeSigningInfo
_TtC10driverkitd28ApprovalSettingsStateManager
_TtC10driverkitd22RealDeveloperKitClient
_TtC10driverkitd25RealApprovalsXPCPublisher
_TtC10driverkitd18NullLaunchServices
_TtC10driverkitd18RealLaunchServices
_TtC10driverkitd16KernelCollection
_TtC10driverkitd21RealXPCEventPublisher
_TtC10driverkitd26DriverKitDaemonSideEffects
RunningBoardSupport
NSObject
_TtC10driverkitd16ApplicationCache
_TtC10driverkitd12RealizedInfo
_TtC10driverkitd22NullLPNEventSubscriber
OS_dispatch_source
_TtCC10driverkitd12RealizedInfo8LoadInfo
_TtC10driverkitd27RestoreOSFeatureFlagsClient
_TtC10driverkitd16RealKernelClient
_TtC10driverkitd22NullSystemPolicyClient
_TtC10driverkitd15ApprovalManager
_TtC10driverkitd18RealBundleResolver
_TtC10driverkitd7XPCUtil
OS_xpc_object
_TtC10driverkitd12RealDistNote
_TtC10driverkitd23RealCodeSigningResolver
_TtP10driverkitd29DriverKitDaemonClientProtocol_
_TtC10driverkitd23RealCoreAnalyticsClient
_TtC10driverkitd23NullCoreAnalyticsClient
_TtC10driverkitd22RealFeatureFlagsClient
_TtC10driverkitd16DriverBinManager
_TtC10driverkitd36DriverKitDaemonAppXPCRequestDelegate
_TtC10driverkitd15LPNAgentManager
_TtC10driverkitd15DriverKitDaemon
_TtC10driverkitd26ApprovalStateUpdateRequest
_TtC10driverkitd18RealDaemonLauncher
_TtC10driverkitd24ApplicationRequestSource
OS_os_transaction
_TtC10driverkitdP33_622D3D8EFA33E5821DB6E6A2F22719EA19StateManagerWrapper
_TtC10driverkitd20RealDeviceProperties
_TtP10driverkitd32DriverKitDaemonAppClientProtocol_
_TtC10driverkitd26AllowAllSystemPolicyClient
_TtC10driverkitd14UncachedBundle
_TtC10driverkitd25MinimalDeveloperKitClient
_TtC10driverkitd23NullRunningBoardSupport
_TtC10driverkitd17RealOSEnvironment
v32@0:8@16@?24
@40@0:8:16@24@32
v16@?0@?<v@?q>8
@24@0:8:16
B16@0:8
Vv16@0:8
v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}12
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v24@0:8@?<v@?@\"NSString\"@\"NSError\">16
B32@0:8@16@24
B24@?0q8@\"<OS_xpc_object>\"16
#16@0:8
v48@0:8@16@24@32@?40
@16@0:8
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
B24@0:8:16
Q16@0:8
@32@0:8:16@24
v28@?0I8Q12@\"<OS_xpc_object>\"20
v8@?0
@\"NSString\"16@0:8
B24@0:8@16
v16@0:8
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
@\"NSDictionary\"8@?0
B24@0:8@\"Protocol\"16
B24@0:8#16
@40@0:8@16@24@32
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40
^{_NSZone=}16@0:8
v16@?0@\"<OS_xpc_object>\"8
v12@?0i8
v24@0:8@?16
Failed to write application cache: %s
Failed to create directory %s: %s
State refresh (id: %s, reason: %s): %s did not update state
Retrieving applications from LaunchServices
Found two applications with the same unique identifier %s:\n%s\n%s
Replacing old dextbin info contents
Could not copyfile:\nfrom: %s\nto: %s\nerror: %s\nerrno: %s
Loading dextbin info, reading plist file from %s
Saving appproval db, encoding
contentsOfFile failed to read approvals database: %s
invalid approvals database, failed to read plist: %s
State refresh (id: %s, reason: %s): %s updated state, will notify subscriber: %s
Failed to use entry %s: %s
Could not insert bundle at %s into manager: %s
Found actively used drivers that are missing:\n%s
Failed to reuse existing bin entry: %s. Creating new bin entry
Drivers with identifiers %s (%s), %s (%s) have the same unique identifier
Copying old active bin entry %s with bin number %s
Failed to stage driver %s from app %s
Bundle at %s is invalid
State refresh (id: %s, reason: %s): %s updated state:\n%s
State refresh (id: %s, reason: %s): Notifying %s of state update
Failed to submit job: %{public}@
Failed to read directory %s: %s. Attempting to create directory
Attempting to copy out driver extension:\n  installIdentifier: %s\n               from: %s\n                 to: %s
contentsOfFile failed to read plist: %s
Validated: %s
Replacing old approval db contents
invalid dextbin info, failed to read plist: %s
Bundle at %s not in manager
Third party driver boot arg %s enabled
Application %s has unexpected unique identifier, expected %s
Internal error: Bin entry %s was inserted with incorrect bin number %s
State refresh (id: %s, reason: %s): completed
Job submitted but not running: %d
Codeless info %s did not contain data for key %s
Failed to create active list: %s
Writing new dextbin info contents
Loading dextbin info, decoding plist
Loading approvals database, decoding data
State refresh (id: %s, reason: %s): starting
unexpected error checking if daemon is active %s
Internal error: found multiple realized infos for %s in manager
Loading application cache from %s
Hardware %s third party drivers
Could not create directory %s: %s (errno %s)
Will remove untracked file %s, since it is not the expected Info.plist at %s
Skipping addBreadcrumbForDextWithIdentifier for %s %ld
Writing new approval db contents
Failed to send notification to xpc event subscriber %llu
contentsOfFile failed to read application cache: %s
invalid application cache, failed to read plist: %s
Third party drivers are disabled
Codeless info %s did not contain path for key %s
Difficulty removing %s: %s
Authenticated: %s with result: %s
%{public}s
Found stale staged driver %s belonging to an uninstalled app
Will remove untracked directory %s
Failed to handle queued request %s: %s
kernel reports daemon is not active: %s
Failed to unload driver %s: %s
Omitting driver %s: does not have a bundle
Saving dextbin info, encoding
Failed to write approval database during state update: %s
Bundle at %s does not have a bundle identifier
Skipping bundle at %s since containing application was removed
Drivers that should be unloaded:\n%s
Can't save dextbin info: %s
Could not report driver install: could not resolve driver bundle at\n %s
Removed untracked path %s
Loading application cache, decoding data
Using cached application list
Available URLs: %s
Omitting third party driver %s at %s: app is not installed
Writing new application cache contents
Skipping bundle at %s, already inserted into new bin with UUID %s
Skipping removeBreadcrumbForDextWithIdentifier for %s
An error occurred while loading dext personalities: %s
Replacing old application cache contents
Codeless info %s did not contain identifier for key %s
%s
Skipping bundle at %s, already inserted into approvals database
Skipping third party driver %s at %s during first approvals database update pass
Loading approvals database from %s
Decompressed data: %d bytes.
Could not find bundle for driver 
OSBundleExecutablePath
kOSBundleDextUniqueIdentifier
LT
<no-bundle-identifier>
Kext Resource Request
OSBundleDependencies
 with a size in the range [
Subscribed Services: 
Platform binary trusted
Invalid ownership (
Failed to force load codeless kexts: %{public}s
unable to load extension: %{public}s: %{public}s
unapprovedToLoadMultiple
Cannot use adhoc strategy on this platform
Could not getBuildVersion since no side-effects found
inSignatureExceptionList
OSBundleLibraries
Could not get path of main executable.
LPN agent event missing event name
Could not search for bundles in auxKC: %{public}s
Found multiple codeless kexts with the same identifiers, will use the known one: \n\tknown path: %{public}s \n\tduplicated path: %{public}s
DextRecord Error: 
systemExtensionWaitForUninstallTermination
Could not determine running kernel architecture.
Connection with client pid %d interrupted.
Could not list contents of dext cores directory: %{public}@
Unsupported Error: 
migrateAuxKCForVolumeGroupUUID failed: 
Could not find IOUserResources entry
Can't resolve code signing info of extension without a bundle
Arithmetic overflow detected while computing offset for the end of the slice\nSlice architecture: 
daemonInit()
uniqueInstallIdentifier
 in approvals database
SPKernelExtensionPolicy is unavailable, NullSystemPolicyClient cannot notify unsupported kexts at: %{public}s
incompatibleVersion
init()
/private/var/tmp/com.apple.driverkitd/applications.plist
auxiliaryOptional
/Library/Extensions/AppleKIS.kext
SystemKernelCollection
distnoted event, dictionary contents:\n%{public}s
 does not have a personality dictionary.
missingDependencyRequest
Could not create extension from bundle at 
<Missing Identifier>
com.apple.KernelManagement
BaseSystemKernelCollection
) should be (0:0) on 
com.apple.km.logging
com.apple.message.subjectcn
DaemonExtensionPaths
UserSystemExtensionsDirectory
Received event for unknown service: %{public}s
An error occurred while loading 
unapprovedToLoad
ApplicationCache
 for architecture 
com.apple.KernelManagementPingServer
Bootstrap check in failed: 
Get Kexts in Collection
Trusted Apple kext in collection
Reading exclude list from %{public}s
Missing Developer Kit: 
' has invalid properties: 
Found multiple drivers with identifier 
OSKextSigExceptionHashList
Collision: replacing %{public}s
Error while managing resource: 
NullIOUserResourcesClient: setProperty('%{public}s') called
 was removed from the staging location, removed from manager
com.apple.message.codeless
ReadPrelinkInfo
incoming app connection from pid %d
Failed to create event dictionary for: %{public}s
Application record is missing install session identifier
IOUserServerCDHash
 is in exclude list: 
Warning: %s is already attached
Unable to create SecStaticCodeRef at 
Application record is missing identifier
, but found that the directory does not exist
Prelink info has no _PageableKCID
Dext Daemon Launch
SPKernelExtensionPolicy is unavailable, AllowARVOnlySystemPolicyClient cannot notify unsupported kexts at: %{public}s
signing information did not contain an executable url
IODeviceTree:/product
Request to strictly match a dext of bundle identifier 
Ignoring kext at %{public}s with incompatible architecture.
, but needed version 
XPC Event %{public}s: Pending subscriber %llx replied with error %{public}s
buildManifestNotFoundError
kextsOutOfOS
Finished extension FS validation with result: %{public}s
\n\nKernel Architecture: 
com.apple.LaunchServices.applicationRegistered
 is too large\nArithmetic overflow detected while multiplying with 
3rd-party kext with Apple root
Could not get contents of 
Prelink info has no _PrelinkInfoDictionary
%{public}s is marked as LPN agent but has no personalities
Other validation Error: %{public}s
/Library/Apple/System/Library/Extensions/AppleKextExcludeList.kext
BuildManifestNotFoundError: 
warning: libImg4Linked not linked
Invalid state transition for 
 is not approved to load. Please approve using System Settings.
errorDescription
OSBundleSharedExecutableIdentifier
AppleKernelExternalComponent
 has an invalid or missing version.
requiresExplicitLoad
Pid: %d
Failed to create XPC event publisher 
contentsOfFile failed on `%{public}s`, errno: %{darwin.errno}d
Unable to deserialize log data.
Error occured while running subcommand '
Img4 format not .im4p (%d), attempting to decode as .img4
OSBundleOptionalAuxKC
 is missing linkage metadata
OSBundleWiredSize
Could not write to FileHandle %{public}s: %{public}s (contents: '%{public}s')
Could not find plist 
Invalid cdhash value '
Received LPN agent event for service: %{public}s
Error occurred while using kclist: 
Resource load failed (error 
These properties should be absent: '
com.apple.message.bundlePath
system kext collection
Warning: %{public}s was not found!
finding bundles at additional paths: %{public}s
Arithmetic Error: 
Initialization error: 
XPC Event %{public}s: Unexpected reply from previously pending subscriber %llx
SysExtensionWaitForTerminationError: 
 compatible with version 
System policy error: 
distnoted app uninstallation event, processing bundle: %{public}s
Read elision list from `%{public}s` for `%{public}s`
Daemon Activation
warning: libcompression not linked; returning existing data.
Audit token did not resolve to an application record
incoming connection from pid %d
_JetsamPropertiesIdentifier
com.apple.driverkitd.DriverApprovalsChanged
Skipping %{public}s, manager settings does not contain a path to it
Applications Installed: 
 is not a driver extension.
Unable to get real path of symlink at 
Failed to read configuration file: 
com.apple.security.get-task-allow
forcing checkpoint to %{public}s
Could not find: 
Could not get contents of main executable.
== Activation State Manager\n
com.apple.applicationservice.matching
Driver Bin Changed
ProgramArguments
Couldn't find extension's bundle
FS contents are valid
Tried to force load extensions from bundles on disk into Manager's lookup table. But the settings flags indicate that the Lookup Tables are restricted
Safe boot error: 
Error occurred while building a collection: 
systemExtensionWaitForTermination
_BundleCollectionType
CPU Subtype is not a number?
Error encountered while deserializing: %{public}s
KernelStateManager
Could not create SecRequirement 
' should be a collection of type 
OSBundleDextStateActive
Cannot force launch driver on release builds.
Handled queued request 
Using unique id %{public}s to pick dext matching bundle identifier %{public}s
Deserialization failed: 
No team ID in signing dict and no Apple-prefix in signing identifier.
XPC Event %{public}s: Added new subscriber %llx (%{public}s)
\n\nRepositories: 
No codeless bundle needs to be force loaded.
Filesystem error: 
Binary not large enough to accomodate 32-bit header
Decompression buffer size %d (try %d)
Latest Drivers:\n
Can't find arch %{public}s in binary
/Library/Extensions
Failed to find existing bin entry for 
 requires arguments, but none were provided
Bundle URL %{public}s is a valid symlink to %{public}s
Binary not large enough to accomodate 64-bit header
Will skip code sign validation of dext in the ARV at %{public}s
Invalid DriverBinInfo version: expected 
Kext Unload Notification
Loading extension(s): 
<unknown security error>
EXACTLY ONE OF: 
DaemonCheckIn
com.apple.km.driverkit.launch
Encountered errors while reading executables: %{public}s
DeniedIdentifiers
Launching driver extension via running board: %{public}s
Could not look for bundles in %{public}s
IOService:/IOUserResources
3rd-party kext with devid+ certificate
LimitLoadToSessionType
== DriverBinManager\n
Updated cached state for settings
com.apple.root.installed
Could not initialize Config
Kext Request Predicate
== Application Manager\n
Kext Request Info Keys
ApprovalsDatabasePath
New approval update request
No dexts with bundle identifier %{public}s matched unique id %{public}s
Found codeless bundles matching the ids listed in codeless exceptions: %{public}s
Unable to determine signature for %{public}s, generating adhoc signature... (%{public}s)
. Should not appear in any of the directories reserved for driver extensions: 
Error occurred while dumping kernelmanagerd state: 
Wanted version of 
Could not parse binary: 
Unable to read extension: 
Kernel request failed: 
Serialization failed.
 to get executable for 
Can't save dextbin info, resetting driver bin
Unable to find '__info' section.
 without the needed unique identifier
\t%{public}s
Unexpected call to %s for %s
 is too large\nArithmetic overflow detected while adding with 
OSBundleUsageDescription
contentsOfFile failed on `%{public}s` for `%{public}s`, errno: %{darwin.errno}d
error: tried to insert an invalid codeless kext in restricted lookup table: %{public}s
Insufficient permissions for action: 
Recovery environment specific error: 
Authenticating extension failed: 
consistencyCheck
ApprovalSettingsStateManager
Could not copy signing information
driverkitd.KMDoublyLinkedListNode
Driver Identifier: 
KernelManagement_executables-514.40.8
Falling back to arch %{public}s
Invalid number of keys found, expected one.
, could not find dext
Failed to enter sandbox: 
' should be one of the values: 
Failed to set temp directory
/private/var/tmp/com.apple.driverkitd/driver-approvals.plist
Applications Uninstalled: 
com.apple.private.driverkit.use-system-thread-group
Error interacting with logging system: 
 has no identifier
ApprovalSettingsStateManagerQueue
Could not find extension for non-identifier lookup
%{public}s is marked as LPN agent but is not a platform dext
Dext core missing creation date, skipping: %{public}@
dext-core-age-limit
triggerPanicMedic
duplicateExtension
unable to read Mach-O header as a 32-bit or 64-bit Mach-O header
 containing staged bundle 
Prelink info value for ManagerVersion is not an integer
ReslideSharedCache
Rejected by exclude list
Boot policy error: 
unable to create extension from '%{public}s', unrecognised package type '%{public}s'
Already added subscriber 
multiple candidates found for 
: should not be group/other writable
Dext cores directory does not exist, nothing to clean up
Driver extension %{public}s cannot use the system thread group because it is associated with application %{public}s
Signing information did not contain a cdhash
SPKernelExtensionPolicy is unavailable, AllowAllSystemPolicyClient cannot notify unsupported kexts at: %{public}s
 is not in the allowed list of user server names: 
Launching driver extension: %{public}s
 contains no executable.
Unable to insert extension: %{public}s
Could not find the system version plist (%{public}s)
KcgenFlow apis sequence error: 
' should have type 
driverkitd/main.swift
Cannot add self as subscriber
Unexpected call to createIdentity(serverName:tagString:containingAppBundleID:)
OSKextStrictExceptionHashList
App connection from pid %d resolved to an application record with no install session identifier; failing closed
Invalid bundle signature for 
 and slice size 
com.apple.message.kextname
Get Kernel Requests
(NOT AN ERROR) Launching dext %{public}s %{public}s 0x%llx %{public}s
SysExtensionWaitForUninstallTerminationError: 
driverkitd/Utilities.swift
dependenciesValidated
/System/Library/Extensions
DeveloperTools Error: 
subscribe(serviceName:scope:type:)
com.apple.developer.driverkit
allowThirdPartyDexts
_DextCheckInPort
Attempt by unentitled pid %d to access app interface
User server name 
 is not a valid tag number
_NullBootstrapPort
ExtensionAuthentication
 is a symlink with an invalid parent directory. Symlinks are allowed from these parent directories: 
Sent new drivers
com.apple.message.version
Failed to trigger launch for %{public}s: %{public}s
Successfully triggered IOKit matching for: %{public}s
driverkitd/DriverKitDaemon.swift
%{public}s %{public}s 0x%llx %{public}s
Swift/NativeDictionary.swift
Binary does not have valid magic
Received update notification for bundle ID %{public}s, unique ID %{public}s
Validating extension failed: 
System/Library/CoreServices/SystemVersion.plist
Active Drivers:\n
Driver Extension Server Tag
com.apple.driver.KextExcludeList
 was unapproved, removed from manager
Created directory at 
Unknown MIG message received.
Subscribed to LPN agents: 
Successfully inserted extension: %{public}s
ApprovalsManager
com.apple.rootless
App server name: %{public}s
driverIdentifier
ApprovalsError while getting approval state: %{public}s
com.apple.driverkitd.kernel-requests
Warning: com.apple.driver.KextExcludeList was not found!
Internal error: 
unable to create extension from '%{public}s', Info.plist digest is missing
com.apple.message.bundleID
%{public}s matches %{public}s.
\nApproval State: 
Can't determine owner/permissions for 
OSBundleLoadAddress
Img4 payload length: %d
OSKernelResource
com.apple.message.architecture
Building kernel collection failed: 
anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] and certificate leaf[field.1.2.840.113635.100.6.1.13] and certificate leaf[field.1.2.840.113635.100.6.1.18]
com.apple.DriverKitAppServer
driverkitd/DaemonSupport.swift
missing bundle after lookup
kern.osbuildconfig
dependenciesAuthenticated
Third-party kext in collection
Set third party driver from bin entry 
DarwinOS error: 
/Library/Extensions/Astris-IOUSBHostFamily.kext
Scoped %lu of %lu cached approval entries to install session %{private}s: [%{private}s]
^[0-9]{4}-[0-9]{4}$
Unable to resolve dependencies: 
insufficientPermissions
Registered event handler for: %{public}s
allowing Apple-prefixed bundle '%{public}s' installed from a root
Extension with identifier '
Received MIG message
OSBundleCPUSubtype
 not approved to load. Please approve using System Settings.
Failed to get signature type: Unable to create SecRequirement for checking Developer ID: %lu
Not compressed; returning existing data. (%d)
com.apple.message.teamid
OSBundleRequireExplicitLoad
com.apple.distnoted.matching
Internal error: unexpected extension type?
skipped ARV dext FS content validation
 was inserted with incorrect UUID 
Prelink info has no _BootKCID
SoftResourceLimits
 contains no executable
Cannot add subscriber with different state manager queue
installSessionIdentifier
GE
Unexpected call to applicationRecord(fromAuditToken:)
. Should only appear in one of the directories reserved for driver extensions: 
com.apple.private.driverkit.driver-launch-configuration
Dictionary<String, String>
driverExtensionPaths
Validating extension at %{private}s
Arbitrarily picking first dext with bundle idenfier %{public}s
 was already specified.
 requires a reboot
missingDeveloperKit
Dext bundle for 
Skipping dext bundle validation on ARV at %{public}s
Bundle contains symlink pointing outside of itself: 
Ignoring load notification: %{public}s
Encountered error: %{public}s
Binary not large enough to accommodate headers
NSHumanReadableCopyright
Starting driverkitd (%{public}s)
Picked matching dext for bundle identifier %{public}s: %{public}s
\nBundle Identifiers: 
Failed to process MIG message.
XPC Event Handler %{public}s error: %d
Could not find configuration data in executable section for architectures 
 with user server name 
ExtensionValidation
Approval database changed
Invalid parent directory for 
Set first party driver 
Unable to stage extension: 
CFBundleDisplayName
 Apple Inc. All rights reserved.
Could not initialize ExtensionManager
Trying to overwrite existing entry with uuid 
PlatformExtensionPaths
, which does not have path prefix 
trying to insert a dext in KernelManagerDaemonLoadableExtTable: %{public}s
Cannot insert more than one of the same kind of collection.
Skip the codeless kext that is not in the force load list: %{public}s
com.apple.DriverKitExtensionServer
com.apple.driverkitd.NSXPCAppRequestSource
 has an invalid format.
XPC Event %{public}s: Removing subscriber %llx
XPC Event %{public}s: Pending subscriber %llx
Dext core at %{public}@ removed
packageInstaller Error: 
In exclude list: 
com.apple.driverkitd
kextsOutOfOSImageFeatureFlags: %{public}s
Apple kext with Apple root
Any
CPU Type is not a number?
Apple prefix trusted
Communicating with kernel failed: 
Collection linkage invalid: 
Unexpected call to createLaunchRequest(context:)
Application landscape changed
Invalid identifier and version 
inStrictSignatureExceptionList
realizedInfo for (%{public}s) may not contain info on uuid or bundleArch
auxiliary kext collection
com.apple.dext-lpn
Unexpected daemon queue request 
driverkitd/DriverBinInfo.swift
UserDriverExtensionsDirectory
Error while encoding approval state for reply: %{public}s
No elision list for `%{public}s`
com.apple.kernelmanagement.dextcorecleanup
Unable to get log flags and messages.
Launching driver extension failed: 
unable to create extension from '%{public}s', bundle contains no Info.plist contents
Set of active drivers changed
Realize dext %{public}s
.xpc.connection.
Could not insert new entry to database
 into a restricted lookup table
, but only found version '
packageInstallerError
Failed to set property '
Unexpected call to %s
com.apple.message.issuercn
Could not find entry with driver identifier 
OSBundleCompatibleVersion
Error while getting scoped approval state: %{public}s
Error occurred while demuxing request %{public}s: %{public}s
com.apple.kernelmanagement.dextLaunch
Boot Collection: 
Application record is missing unique install identifier
matchesExludeFilter
unknown collection
Unable to bridge job launch dictionary
xpc event stream handler registered for: `%{public}s`
Attempt by unentitled pid %d to access interface
Unable to deserialize kernel response.
Unable to read contents of file at 
com.apple.driverkitd.daemonInit
Terminate IOServices
DriverKit Reslide Shared Cache
Received update notification for 
invalidProperties
setHandler(queue:handler:)
ActiveDriversStateManager
ApplicationManager
SystemVolumeSystemKernelCollection
Received unload notification for bundle ID %{public}s
inserting a valid codeful kernel extension in restricted lookup table: %{public}s
OSBundleRetainCount
runninglistError
Cannot decompress: Invalid buffer. Returning existing data
Artifact is not a valid fat Mach-O
Unrecognized identifier: %s
/Library/Extensions/AppleKIS.kext/Contents/PlugIns/AppleRSMHost.kext
Cannot realize extra load info from 32-bit collection.
Driver Extension Server Name
KMError while getting scoped approval state: %{public}s
ForcedFullBundleLoad
Extension with identifiers 
unsupportedError
signing information did not contain a signing identifier
CFBundleIdentifier
Inserted new driver 
 was never attached
ExtensionRealizing
Cannot use resolveSignatureOrGenerateAdHocOne with adhoc strategy
boot kernel collection
com.apple.kernel
ForceLoadCodelessIdentifiers
com.apple.driverkitd.NSXPCRequestSource
bundleIdentifier
, refusing to insert 
NSError while decoding update to approval state: %{public}s
State refresh
Kernel requested shutdown. Goodbye!
Launching dext %{public}s %{public}s 0x%llx %{public}s
,\nrequiredPaths: 
com.apple.km.driverkit.approval
[Error] Interval already ended
Could not find extension with identifier 
IOUserServerName
Using file age limit from boot args: %d seconds
Duplicate values for key: '
KDK-Installer Error: 
Duplicate extension error :
    Driver Extensions:\n
dependenciesValid
AuxiliaryKernelCollection
Incoming app request for scoped approval state from pid %d
EnvironmentVariables
com.apple.dext.asan
 which is not contained in a valid platform extensions directory
Bundle or the bundle id is nil: %{public}s
com.apple.message.kextexecpath
    Unique Identifier: 
Cannot determine UUID
_PrelinkInfoDictionary
Incoming request for approval state
Validation Error: %{public}s
 and unique identifier 
Attempted to load an AppleKextExcludeList which wasn't a kext?
%{public}s found in built-in deny list
Received an unexpected null/empty response for request: 
collectionLinkage
Header was already determined to be 64-bit.
 must have valid Apple copyright string
com.apple.kernel.
Could not get unstaged real path for %{public}s, cannot determine if absent executables are okay
Received unload notification for 
DriverkitExtensionLoad
Binary is fat.
(no collection, personalities only)
' should be absent
com.apple.kernelmanagerd.KernelRequestSource
KernelFileSetLoadRequest
Unknown CPU type %d with subtype %d
Error occured while reading kextinfo from kernel: 
anchor apple generic
Failed to read info dictionary for driver 
getBuildVersion(for:)
== Driver Extensions by identifier:\n
Application record is missing driver extension paths
 is a symlink to 
does not support
OSKextExcludeList
Invalid match specification '
Ptrauth ABI mismatch: binary is built against version 
Staging directory 
Unable to bridge xpc event dictionary
_NeedsSystemThreadGroup
Fatal error
Could not determine running userspace architecture.
Could not find variant.
DextLaunch
Figuring out dext launch context: %{public}s
\nAuxiliary Bundle Paths: 
OSBundleLoadSize
,\nrequiredIdentifiers: 
Incompatible architecture: 
LE
com.apple.developer.system-extension.install
DaemonActivation
Daemon has activated
Error occurred triggering Panic Medic: 
, Slice offset: 
Data compressed with %{public}s
Failed to read bundle at 
DaemonInitStarted
ThirdPartyDriverKitStagingDirectory
Bad code signature
FS validation skipped
Invalid check in token port: 
kernelCommunication
com.apple.get-task-allow
, Offset for end of slice: 
com.apple.km.driverkit.install
com.apple.message.signaturetype
Error while enqueuing update to approval state: %{public}s
\nUserspace Architecture: 
requiredIdentifiers
Code signature error: 
Loading extension failed: 
com.apple.LaunchServices.applicationUnregistered
driverkitd/StateManagement.swift
KextsOutOfOSImageFeatureFlags should have only one checkpoint enabled. Found %{public}s
    Application: 
Unrecognized predicate 
Kext Load Notification
Other validation error: 
Binary not large enough to accomodate fat header
kernelmanagerd
OSKernelCPUSubtype
Invalid permissions 
error: tried to insert an invalid ext in restricted lookup table: %{public}s
globalError
, cannot check code signature.
(anchor apple\n    or (anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.9] exists)     or (anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] exists     and certificate leaf[field.1.2.840.113635.100
Decompression error (decoding buffer returned 0 size!); returning existing data.
 not large enough to accomodate all fat headers with total size 
registering handler for xpc event stream: `%{public}s`
BootKernelCollection
 is not a directory
Activation state changed
OSBundleIsInterface
_CodelessKextBundlePath
Connection with client pid %d invalidated.
AuxiliaryExtensionPaths
distnoted event caught with unexpected payload; xpc handler called for xpc object of type `%{public}s`
ActivationStateManager
Subscriber graph contains a cycle after adding 
Adhoc cdhash: %{public}s
Collection had no prelink UUID key?
    Staged bundle: 
Exception list trusted
Error reading the AppleKextExcludeList: 
Img4 error: format neither im4p nor img4 (%d)
 requires an Apple kext
Got invalid service port.
Kext Request Arguments
matchesIncludeFilter
OSBundleAllowUserLoad
inserting a valid codeless kext in restricted lookup table: %{public}s
Force update for activation
(kernel): %{public}s
Pending Requests 
MS decoder error: 
Swapping big-endian fat header.
Updated loaded info for %d extensions.
Encountered error while scanning load commands for arch 
 (unique identifier 
3rd-party kext without Apple root
com.apple.message.kextpath
com.apple.kpi.iokit
_PrelinkBundlePath
No keys can have the prefix 'com.apple.kernel.'
(NOT AN ERROR) Starting driverkitd (%{public}s)
com.apple.message.signingtime
No dext cores found, nothing to clean up
Error getting kernel requests: %{public}s
Looking for the %{public}s
optionalIdentifiers
dependencyResolution
Server name: %{public}s
supports-third-party-drivers
dependenciesAuthentic
_InfoPlistDigest
Found existing approval database entry 
Could not get creation date for dext core at %{public}@: %{public}@
 linked against 
Could not create enumerator for 
inserted dext, then could not look it up
OSBundleRequired
Kext Load Request
Skipping FS validation for kext 
incompatibleArchitecture
Successfully set property '%{public}s' on IOUserResources
/private/var/tmp/com.apple.driverkitd/DriverExtensions
IOKitPersonalities
OSBundleTeamIdentifier
App with install session identifier 
CodelessSearchPaths
(NOT AN ERROR) Kernel requested shutdown. Goodbye!
excludedIdentifiers
Error encountered executing subprocess: 
/Library/Caches/com.apple.xbs/01140AD0-7A8D-4CDD-A311-AE4EC8D7E233/TemporaryDirectory.pQ4EeA/Sources/KernelManagement_executables/core/Errors.swift
Fileset entry found for %{public}s, but not included in prelink info
Codeless Personalities
dumpState(withReplyBlock:)
, check in port 
Format appears to be from the future: 
knoxDownloaderError
systemExtensionsError
Manager version is 
distnoted event, could not make info object
install session identifier for calling application
 approval state to default 
Invalid Request: 
Adhoc signature; forcing no team ID
CheckCodeSignValidity
, but needed arch 
DaemonInitComplete
Prelink info section has no _PrelinkKCID
error: tried to insert an invalid codeful kernel extension in the restricted lookup table: %{public}s
Binary not large enough to accommodate magic
' should have type String with a maximum length of 
Found no registered drivers with identifier 
ProductBuildVersion
force-try failed
Error deriving adhoc signature for %{public}s: %{public}s
Error occurred checking UUIDs: 
listener(_:shouldAcceptNewConnection:)
Error launching dext \"%{public}s\": %{public}s
OSBundleMachOHeaders
,\noptionalIdentifiers: 
' on IOUserResources: 
EQ
kind: %{public}s
dext_asan_sb boot-arg present: %d
Dext Daemon Upgrade
HardResourceLimits
Found %{public}d dexts with bundle identifier %{public}s
Properties under 
com.apple.message.personalitynames
driverkitd/XPCEventPublisher.swift
/Library/StagedExtensions
driverkitd/Validation.swift
An unknown error occurred while building the cache.
Arithmetic overflow detected while adding slice offset 
No unstagedURL found for %{public}s, cannot determine if absent executables are okay
Could not determine running architecture.
, resulting in approval state update
Processing pending requests from the kernel, if any
Unable to resolve dext with identifier 
kdkInstallerError
Slice ends at an offset outside the binary\nSlice architecture: 
Could not find entry with device tree path 
 does not contain a bundle identifier
 has no predicate
Could not find property 
Could not read the system version plist from %{public}s: %{public}s
GT
== Driver Approval Database:\n
IOKit Daemon Exit
com.apple.private.security.driver-management
 has invalid or missing package type
subprocessFailed
CFBundleGetInfoString
openat_authenticated_np() failed at path %{public}s with (errno %d)
KextsOutOfOSImage
Driver Bin Version 
ApprovalSettingsState: 
Request enqueued at 
AllExtensionsPaths
Invalid UTF-8 elision list for `%{public}s`
reporting %d newly unsupported kexts to syspolicyd after AKEL update:
Could not create SecRequirement for 
Discovered LPN agent: %{public}s
No authentication enabled, trusted
Executing dextcore cleanup pass
No unique identifier available to disambiguate between dexts of bundle identifier %{public}s
Another collection at 
Skipping %{public}s, cannot map
finding bundles in repositories: %{public}s
kernelCollectionBuild
com.apple.message.fat
Application cache has wrong version
developerToolsError
Binary not large enough to accomodate fat arch headers
' should have type String with prefix: 
AppleSecurityExtension
== Driver Extensions by URL:\n
Invalid argument: 
activate()
PlatformDriverExtensionsDirectories
KMError while getting approval state: %{public}s
KernelStateManager not set
Skipping FS validation for kext already in collection 
The codeless exceptions configuration is not provided, skip codeless forceloading
Configuration has unrecognized format.
distnoted app installation event, processing bundle: %{public}s
No identifier in kernel request for dext launch
Initializing with settings: %{private}s
' must be a valid kext version
com.apple.message.hash
    Install Session Identifier: 
IOPersonalityPublisher
%{public}s, uuid %{public}s %{public}svalid %{public}sauthentic %{public}sapproved
File age limit of %d seconds from boot args is too small (minimum %d seconds), using default %d seconds
AkelExtensionLoad
Extension with identifier 
Subscribed to service: %{public}s
Staged application 
Could not remove dext core at %{public}@: %{public}@
inserting to insert an unknown but valid extension into restricted lookup table: %{public}s
DriverBinManager
Unknown extension type for 
com.apple.kpi.private
Could not create bundle for 
Unexpected call to createLaunchContext(identity:)
Could not determine if absent executables are allowed for %{public}s: %{public}s
com.apple.driverkitd state at 
,\nexcludedIdentifiers: 
Failed to get signature type: Unable to create SecRequirement for checking Apple root: %lu
Slice offset lies outside the binary\nSlice architecture: 
appInstallSessionIdentifier
driverkitd.NSXPCRequestSource
Error occurred unloading extensions: 
CFBundleIdentifierKernel
kextsInKDK
XPC Event %{public}s: Pending subscriber %llx replied with unexpected type %{public}s
ApplicationCachePath
Unexpected request 
Error occurred while handling request \"%{public}s\": %{public}s
Did not find dext with bundle identifier 
CopyCodeSignInformation
 was uninstalled, removed from manager
CollectionRealizing
, is not a DriverExtension
_setOverrideExecutablePath:
applicationManager
initWithMachServiceName:
path
setInvalidationHandler:
$__lazy_storage_$_kernelCacheUUID
bootCollectionUUID
$__lazy_storage_$_inSafeBoot
context
_table
flags
stateManagerQueue
_activated
publisher
requestQueue
tail
unlock
entitlements
dealloc
builtInPlugInsURL
pendingSubscribers
uuid
$__lazy_storage_$_inDarwinOS
init
setArguments:
setRepeats:
T@\"NSString\",?,R,C
extensionManager
maxCapacity
se
bundleElisions
$__lazy_storage_$_dextASanSandbox
$__lazy_storage_$_variant
_historyItems
cacheLoadAddress
location
queue
respondsToSelector:
createDirectoryAtURL:withIntermediateDirectories:attributes:error:
isEqual:
localizedFailureReason
$__lazy_storage_$_bootArgs
dumpStateWithReplyBlock:
identifier
rss
contents
infoDictionary
loadState
nextObject
recursiveLock
exceptionLists
$__lazy_storage_$_inKcgen
activationStateManager
bundleIdentifier
contextWithIdentity:
scheduleWithBlock:
setDelegate:
_cfBundle
loadInfoDict
pageableCollectionUUID
teamID
dispatchSource
T#,R
hash
performSelector:
setInterface:forSelector:argumentIndex:ofReply:
submitAndStart:
$__lazy_storage_$_enableKextLogging
setExecutionOptions:
_subscribers
$__lazy_storage_$_processInfo
codelessForceLoadLists
localizedInfoDictionary
removeItemAtURL:error:
state
defaultManager
block
head
kextHistory
description
originURL
prev
timestamp
arch
driverExtensionPaths
initWithPlist:domain:
setExportedObject:
settingsQueue
signingIdentifier
timeInfo
activeDriversStateManager
approvalSettingsStateManager
kernelStateManager
kind
$__lazy_storage_$_disableAuxKCAtBoot
class
databasePath
isKindOfClass:
isMemberOfClass:
repoIndex
setDextCheckInPort:
URL
val
attributesOfItemAtPath:error:
daemonCheckInInterval
lockedState
csi
$__lazy_storage_$_enableSerialLogging
_loadInfo
enqueueApprovalStateUpdateWithEntry:replyBlock:
setInterruptionHandler:
subjectCN
predicateFormat
stringFromDate:
debugDescription
mainBundle
vers
$__lazy_storage_$_inBaseSystem
$__lazy_storage_$_nextInfoLocation
auditToken
getApprovalStateForCallingAppWithReplyBlock:
lpnAgents
subscribers
cst
data
pid
$__lazy_storage_$_kcSuffix
settings
validationErrors
approvalManager
unstagedURL
initWithDomain:code:userInfo:
lock
table
TQ,R
currentSize
fileHandleForWritingAtPath:
identifierVsDextLaunchDebugMetadata
issuerCN
superclass
_driverBinInfo
autorelease
connection
self
manager
_setAdditionalEnvironment:
extensions
historyItem
code
digest
identityForDextWithServerName:tagString:containingAppBundleID:
interfaceWithProtocol:
$__lazy_storage_$_infoLocation
.cxx_destruct
loadInfo
isProxy
lpnAgentManager
systemDomain
_cached
ext
contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
exportedInterface
fm
name
replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
cdHash
next
performSelector:withObject:
processPendingRequestsOnActivation
directory
valueForEntitlement:
createFileAtPath:contents:attributes:
setInterval:
driverBinManager
processIdentifier
dkdSignposter
$__lazy_storage_$_inRecovery
$__lazy_storage_$_isAppleInternal
applicationCache
servicePort
setBundleIdentifier:
value
release
bundleURL
conformsToProtocol:
debugMetadataDoublyLinkedList
info
resume
setTimeZone:
initWithIdentifier:
$__lazy_storage_$_hardwareSupportsDrivers
_activeDriverSet
initWithContext:
retain
enumeratorWithOptions:
_setQueue:
bundleArches
daemon
installSessionIdentifier
$__lazy_storage_$_thirdPartyDriverBootArgEnabled
_approvalDB
entry
initWithURL:
bundleRecordForAuditToken:error:
fileExistsAtPath:isDirectory:
T@\"NSString\",R,C
forceLoadedBundlesAlready
listener
setQualityOfService:
uaklPath
zone
$__lazy_storage_$_inRestore
signingTime
$__lazy_storage_$_inMainOS
bundle
listener:shouldAcceptNewConnection:
uniqueInstallIdentifier
executablePath
getApprovalStateForSettingsWithReplyBlock:
subscribedServices
callback
evaluateWithObject:
setExportedInterface:
collection
execute:
launchDriverWithBundleID:userServerName:tag:replyBlock:
$__lazy_storage_$_inFVUnlock
applicationCachePath
performSelector:withObject:withObject:
requests
retainCount
semaphore
```
