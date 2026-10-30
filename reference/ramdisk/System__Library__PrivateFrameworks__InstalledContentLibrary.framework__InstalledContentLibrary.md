# `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,032,800 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 36 (Size: 5432)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (18)

- `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libmis.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (76 classes, 15 protocols)

Classes: `ICLAppExtensionRecord`, `ICLAppRecord`, `ICLBundlePersonaRecord`, `ICLBundleRecord`, `ICLFeatureFlags`, `ICLFrameworkRecord`, `ICLHelperServiceClient`, `ICLInstallationDaemonClient`, `ICLPlaceholderRecord`, `ICLRegistrationOptions`, `ICLSinfInfo`, `ICLStashedAppRecord`, `ICLSystemAppPlaceholderRecord`, `ICLUninstallRecord`, `ICLWorkspace`, `MIAppExtensionBundle`, `MIAppIdentity`, `MIAppLaunchProhibition`, `MIAppReplacementState`, `MIBundle`, `MIBundleContainer`, `MIBundleContainerToken`, `MIBundleMetadata`, `MICapabilitiesManager`, `MICodeSigningInfo`, `MICodeSigningVerifier`, `MIContainer`, `MIContainerQueryResult`, `MIContainerToken`, `MIDaemonConfiguration`, `MIDataContainer`, `MIDataProtectionChangeOperation`, `MIDriverKitBundle`, `MIEmbeddedWatchBundle`, `MIExecutableBundle`, `MIExtensionKitBundle`, `MIFileManager`, `MIFileManagerCopyfileContext`, `MIFilesystemScanner`, `MIGlobalConfiguration`, `MIGroupContainer`, `MIInstallationIdentity`, `MIInstalledInfoGatherer`, `MIKeychainAccessGroupTracker`, `MILaunchServicesDatabaseGatherer`, `MILocation`, `MILocationSystemDefinedBase`, `MILocationSystemDefinedCommon`, `MILocationUserDefined`, `MILocationUserDefinedDirectory`, `MIMCMContainer`, `MIMachOImageSlice`, `MIPersonaAssociation`, `MIPersonaAttributes`, `MIPersonaContainerSet`, `MIPluginDataContainer`, `MIPluginKitBundle`, `MIRelocatedBundleContainer`, `MISignatureAgnosticHasher`, `MIStagingLocation`, `MIStagingRootAbsolute`, `MIStagingRootVolumeUUID`, `MIStashMetadata`, `MIStashedBundleContainer`, `MIStoreMetadata`, `MIStoreMetadataContentDescriptor`, `MIStoreMetadataDistributor`, `MIStoreMetadataSubGenre`, `MISystemAppState`, `MITestManager`, `MIUserManagement`, `NSData`, `NSDictionary`, `NSMutableDictionary`, `NSString`, `NSURL`

Protocols: `MIAppIdentityPersonaResolver`, `MIBundleMetadataProvider`, `MIFilesystemScannerDelegate`, `MILocationProtocol`, `MIPersonaAssociationLocalResolver`, `MIStagingRootProtocol`, `MIUserManagementDaemonContainerResolver`, `MobileInstallationHelperServiceProtocol`, `MobileInstallerDelegateProtocol`, `MobileInstallerProtocol`, `NSCoding`, `NSCopying`, `NSFastEnumeration`, `NSObject`, `NSSecureCoding`

## Strings (5,029)

First 2,500 of 5,029.
```
InDiagnosticsMode
ProfileValidated
HasAppGroupContainers
-[MIFileManager enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:]_block_invoke
Failed to get ACL from %@ : %@
iad-conversion-date
Failed to find LC_CODE_SIGNATURE load command in %@
MIReduceAvailableMemoryForValidationForTesting
AppexBundleContainsClassOrStoryboard
-[MIExecutableBundle hasExecutableSliceForPlatform:error:]
com.apple.MobileInstallation.BundleMaxLinkedSDKVersion
Skipping block device encountered at %s
distributorInfo
Unexpectedly asked to validate thinning on a non-app bundle %@
PrivateFrameworks
Failed to read %@
Couldn't fetch list of supported device families.
Info.plist
WKAppBundleIdentifier
Updated bundle %@ no longer references keychain group %@
Missing location type
Failed to write current build info to %@ : %@
Failed to construct MIContainer instance with container %@ : %@
-[ICLUninstallRecord isEqual:]
-[MIFileManager clearPlaceholderStatusForBundle:withError:]
WatchKit 2 app extension's NSExtension.NSExtensionAttributes.WKAppBundleIdentifier value does not match WatchKit app's bundle ID (found \"%@\"; expected \"%@\").
NSExtensionPrincipalClassProhibited
Failed to enumerate %@
Removing reference in %@ for %@
Siri Intents Appex bundle at %@ with id %@ specifies a value in the IntentsRestrictedWhileLocked key's array value in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist that is not a listed in the the IntentsS
UILaunchImages
-[MIExecutableBundle hasOnlyAllowedWatchKitAppInfoPlistKeysForWatchKitVersion:error:]
<%@ status:%lu isNew:%c container:%@>
Failed to remove profile for app identifier %@: %@
Siri Intents Appex bundle at %@ with id %@ does not define an IntentsSupported key with an array value containing strings in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist.
codeInfoIdentifier
MILocationUserDefined
ParentIdentifiers
Info.plist from bundle at path %@ had none of the keys that we expect; %@
app
Failed to get all bundles within app %@
BundleMetadata.plist
Failed to create URL for %s
init(internal:)
CreatePlaceholderOption
Multiple message payload provider extensions found in app but only one is allowed (found %@ ; already found %@)
IsOnMountedDiskImage
AppleID
linkedChildBundleIDs
8.2
stashOriginalInstallTimestamp
com.apple.security.application-groups
Failed to create URL for last build info file.
lstat failed for %s
Cannot set installation identity for bundle that uses a static identity: %@
Skipping app with no bundle executable at %@ : %@
sinfs
The \"NSPrivacyTrackingDomains\" key in the app's Info.plist must have an array value. An entry was found of non-array type %@.
Failed to create bundle for %@ : %@
Error fetching group containers for %@ for persona %@ : %@
This is the MobileInstallation test exception sentinel reason
The SINF provided for the bundle at %@ does not have a matching key in the FairPlay keybag.
TooManyAlternativeAppNames
ApplicationDSID
There is nothing to generate UUID
CFBundlePackageType
PUICApplicationColors
IsSwiftPlaygroundsApp
Failed to find container of class %llu with identity %@/%@
Unknown
Failed to resolve persona for %@
-[MIMCMContainer infoValueForKey:error:]
com.apple.MobileContainerManager.AdvanceCopy
InstallingEmbeddedProfile
Rejecting %@ with base %@ because real component counts don't make sense (reals %@ ; %@)
Property %s did not match
Unknown WatchKit version enum value %hhu
Extension cache does not have an entry for %@
Couldn't get appIdentifier EA from \"%s\"
Skipping hardlinked file at %s
Found unknown personas in %@ associated with %@; overriding association to %@
MIPlaceholderArchitectures
__swift5_entry
is.workflow.my.app
Skipping character device encountered at %s
targetDirectoryURL
LSRequiredFeatureFlags
StashOriginalInstallTimestamp
-[ICLBundleRecord isEqual:]
MIAppReplacementStatusRefused
Watch
Entitlement %@ contains non-string values; ignoring.
Rejecting %@ -> %@, as it is points outside or to the base %@
UninstalledAppInfoArray
ErroneousContainerCleanupDone
com.apple.developer.web-browser
B32@?0i8i12I16I20I24B28
hasOrEverHasHadIAP
Failed to release sandbox token %lld for %@ : %s
com.apple.mobilemail
getpwuid_r failed for uid %d : %s
Failed to deserialize SystemAppState from %@ : %@
MinimumProductVersion
DTSDKBuild
MultipleWatchKitAppexBundles
17.0
IllegalBundleShortVersionString
Couldn't set installType EA on \"%s\": %s
Could not locate platform for %@ string value \"%@\"
v32@?0@\"NSString\"8@\"NSDictionary\"16^B24
com.apple.installd.testMode
sourceAppIdentity
Attempted to set container with mismatched identifier %@ on %@
XPCService
AppexBundleUnknownExtensionPointIdentifier
-[MIDaemonConfiguration init]
com.apple.WatchPlaceholder
Unable to deserialize iTunesMetadata.plist data
_CreateAndPushContinuation
<No container description>
BackupSystemAppInstallState.plist
betaTesterType
] does not match the expected location type 
Failed to verify code signature for this system app, %@. Because of that, we don't have entitlements or signing info so we'll assume that it requires a container.
+[MILaunchServicesDatabaseGatherer _createDataContainersAndSetDataProtectionForBundle:forPersona:error:]
-[MIUserManagement systemPersonaUniqueStringWithError:]_block_invoke
Failed to get FD to bundle executable at %s
systemgroup.com.apple.installcoordinationd
v24@?0@\"NSUUID\"8@\"NSError\"16
B16@?0@\"MIMCMContainer\"8
Updated bundle %@ added ref for keychain group %@
AppexBundleIllegalExtensionPointVersionString
CompatibilityState
Readlink failed: %s
downloaderID
Could not get current build string; assuming this is an upgrade
isDeletable
counterpartIdentifiers
MIMachOSupportedArchitecturesForPlaceholderInfoPlist
v8@?0
sinf subpath %@ is absolute
LSInstallType
-[MIInstalledInfoGatherer _populatePlaceholderRecordValues:signingInfo:]
IsContainerized
MICreateSHA256Digest
DTXcodeBuild
MISSignerType is MISSignerTypeLegacyVPN which is not supported by MI; returning MICodeSignerTypeUnknown
fsync failed for %s : %s (%d)
copyfile after clonefile failed for %s to %s: %s
/System/Library/Frameworks/JavaScriptCore.framework
UILaunchImageMinimumOSVersion
InstalledContentLibrary.MIAppLaunchProhibition
MIDaemonConfiguration
Found non-boolean value for boolean entitlement %@: %@ ; assuming %s.
ACL={ %@ } 
softwareVersionBundleId
Failed to get build version
LC_CODE_SIGNATURE command's data offset is less than the size of the mach header in %@
No root sinf found to replicate at %@
NSPrivacyTrackingDomains
com.apple.private.extensionkit.builtinanypersona
-[MIBundleContainer stashBundleContainerContents:error:]
-[MIFileManager _moveItemAtURL:toURL:failIfSrcMissing:error:]
MGCopyAnswer for kMGOCompatibleAppVariants returned NULL
WatchOnlyAppContainerNotInstallable
v24@?0@\"NSArray\"8@\"NSError\"16
dev=%d ino=%llu mode=0%ho nlink=%hu uid=%u gid=%u rdev=%d size=%lld atime=%lf mtime=%lf ctime=%lf birthtime=%lf blksize=%d blocks=%lld flags=0x%x 
-[ICLHelperServiceClient _synchronousRemoteObjectProxyWithErrorHandler:]
Could not iterate slices in macho %@
isSwiftPlaygroundsApp
Logs/MobileInstallation
MIInstallerErrorDomain
Failed to malloc %zd bytes for extended attribute key %s: %s
-[MIMCMContainer _doInitWithContainer:error:]
lstat succeeded but st_dev was -1 for %s
Failed to move %@ to %@
-[MILaunchServicesDatabaseGatherer performGatherWithError:]
System App Extension
initialODRSize
-[MIPluginDataContainer setParentBundleID:]
Failed to query staged container status %@ : %@
+[MIContainer containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:created:error:]
PlugIns
SerializedPlaceholderPath
MIBundleHasMinimumOSApplicableToProductVersion
BackedUpState
-[MIGlobalConfiguration internalSupersededAppAdditionsPlistURL]
MIGetBooleanEntitlement
com.apple.developer.parent-application-identifiers
Rejecting \"%s\" because its realpath \"%@\" points outside or to the base %@
Failed to create MIStoreMetadataSubGenre instance
Library/Logs
Exempting %@ from System App XPC Service & Extension bundle ID conflict checks because the parent bundle has the System App entitlement
Could not get family ID from SINF at %@: %ld
Failed to copyfile %s to %s
Could not read ACL text for file %@: %s
Failed to get bundle URL for plugin data container %@: %@
Failed to delete existing transient container for %@
WatchSimulator
com.apple.mobileme.fmf1
_ReadFile
Failed to hash watchkit app executable for %@ at %@
Skipping socket encountered at %s
copyfile failed in source hierarchy while copying %s to %s: %s (%d)
UIBackgroundModes
DeviceNotSupportedByThinning
The appex bundle at %@ does not have a bundle executable at %@. App extensions must have an executable.
Internal
Got unexpected bundle type for persona discovery: %@
LSEligibilityInstallPredicate
com.apple.WK
Failed to get sandbox extension for installcoordinationd's daemon container
Found multiple personas associated with %@; persona resolution is ambiguous. Found: %@
signatureVersion
System/Library/AppSignatures
com.apple.web-browser-engine.content
Failed to get bundle URL for system app with id %@
System/Cryptexes/App
Attempted to set nil data on \"%s\" for EA named %s
Lacking other hints, because the root of the bundle %@ has only a Contents directory, assuming this is a MacOS app
sandbox_extension_consume for %s failed: %s.
%s is not enabled
re6Zb+zwFKJNlkQTUeT+/w
appex
watchsimulator
default
-[MIExecutableBundle watchKitAppExecutableHashWithError:]
_removefile_error_callback
iTunesMetadata.plist was not a dictionary; found class %@
Appex bundle at %@ with id %@ does not specify an Apple extension point as the value of the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist; found: %@
com.apple.AskPermissionUI
MIReplicateRootSinf
AppleTVOS
swift-playgrounds
Could not get the length for extended attribute list for %s: %s
Skipping macho file not runnable failure during test mode
sinf subpath %@ points outside of bundle
Scanned %lu items in frameworks dir %@
com.apple.
Not removing sinf because we failed to get sinf replication paths: %@
MIUninstallProfilesForAppIdentifier
com.apple.developer.superseded-application-identifiers
MIAssumeIdentity
Failed to locate a bundle with extension %@ in directory %@
-[MIBundle infoPlistHashWithError:]
v32@?0@8@16^B24
Documents
Could not readlink %s : %s
Settings.bundle
Failed to create verifier for executable %@
+[MICodeSigningVerifier validateWatchKitV1StubExecutableBundle:error:]
domain
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_DEFAULT
%lu
App %@ is forbidden from providing an extension of type %@
iPhoneSimulator
MIContainerManagerErrorDomain
com.apple.web-browser-engine.rendering.development
SinfReplicationPaths
MultipleMessagePayloadProviderExtensionsFound
The \"NSPrivacyTrackingDomains\" key in the app's Info.plist must have an array value containing strings. An entry was found in that array of non-string type: %@
-[MIFilesystemScanner _scanBundleContainersWithClass:withError:ignoredErrorOccurredOnOneOrMoreItems:]
FreeProfileValidated
Failed to rollback to old SINF data for identifier %@: %@
ReleaseType
Failed to unlink no longer needed install map at %@ : %@
_DiskImageApplicationsDirectories
Caches
Temporary
_checkIdentifierForConflict
Failed to open %s: %s
Could not find appropriate set for app %@
System App
Failed to mkdir %s
Failed to determine if %@ exists: %s
Expected to find only one or more platform slices for %@ in executable at %@ but also found other platforms: %@
System App XPC Service
_hasNoConflictWithSystemAppBundleIDs
-[MIFileManager urlsForItemsInDirectoryAtURL:ignoringSymlinks:error:]_block_invoke
+[MIStashMetadata metadataFromURL:error:]
profileValidationType
InternalSupersededAppAdditions.plist
Failed to readlink %s
File %s has open file descriptors; cloning
gameCenterEnabled
HasCriticalAlerts
%@ contains a placeholder watch app, so an executable hash is not possible.
InvalidSinf
-[MIFileManager _insecureCachedAppIdentifierIfMarkedWithEAFlag:bundleURL:allowPlaceholders:error:]
, sourceAppIdentity=
-[MIContainer _replaceExistingContainer:replacementReason:waitForDeletion:error:]
NonAllowedAppexTypeFoundInMessagesStubApp
No bundle found in container %@; skipping.
Failed to get keychain access groups for old bundle %@
-[MIDataProtectionChangeOperation _runChangeOperationWasLocked:withError:]_block_invoke_2
staticDiskUsage
Mach header specified unknown filetype %u
ProfileType
More than one Siri Intents UI app extension in the app %@ declares the value %@ in the IntentsSupported array in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist.
/System/Library/PrivateFrameworks/FindMyDeviceUI.framework
Failed to gather launch services info for app extension %@ in bundle %@ : %@
+[MILaunchServicesDatabaseGatherer _createDataContainerAndSetDataProtectionForBundle:forPersona:error:]
MIExecutableBundle.m
-[MIFileManager _copyItemAtURL:toURL:failIfSrcMissing:alwaysClone:ignoreErrors:error:]
genreID
InstallSessionID
Failed to decode stash metadata from %@
-[MIBundle _validateWithError:]
Failed to get PluginKit bundles for app %@: %@
AllowPatchInstallationWithoutSinf
Failed to get bundle URL for %@ from built in app map
isContainerized
DriverKitBundleIDSuffixContainsPeriod
Failed to read UM's persona generation identifier when resolving persona
CoreServices app
/System/Library/Frameworks/IOKit.framework
Failed to release sandbox token %lld for container %@
NSExtensionMainStoryboard
Extended attribute list for %s returned length 0, expected length %zd
v32@?0@\"NSURL\"8@\"NSURL\"16^B24
ratingRankEligibilityDomain
Failed to set owner for %s : %s
parallelPlaceholderURL
Failed to set code signing info with MCM for %@, isPlaceholder: %c
+[MIContainer tempContainerWithIdentifier:forPersona:ofContentClass:constructor:error:]
Failed to create MIExtensionKitBundle instance for %@ : %@
returning: %@
Failed to get keychain access groups in app extension %@
+[MIAppIdentity validateAppIdentity:withError:]
MIInstallProfileAtURL
Failed to get app launch prohibition state from %@ : %@
Appex bundle at %@ with id %@ does not define an EXAppExtensionAttributes dictionary in its Info.plist
Failed to seek to %lld in %@ : %s
com.apple.web-browser-engine.networking.development
InstalledContentLibrary
The app extension at \"%@\" has the entitlement \"%@\" which is not allowed for an extension targeting the extension point \"%@\".
genre
Failed to unlink temporary directory at %s : %s
Unable to resolve persona for location of identity %@
removefile_state_set REMOVEFILE_STATE_ERROR_CONTEXT failed: %s
<%@ 0x%p uniqueInstallID=%@ installSessionID=%@
Setting protection class of %s to %d
keyCount=%lu 
Failed to save parent bundle ID on plugin data container %@ : %@
-[MIBundle isApplicableToCurrentDeviceCapabilitiesWithError:]
com.apple.developer.usernotifications.critical-alerts
getxattr for xattr named %s on \"%s\" returned %zd (expected %zu)
Found no entitlements for %@ at %@
ApplicationType
Failed to find __LINKEDIT segment in %@
Appex bundle at %@ with id %@ does not have a legal value for the NSExtensionPointIdentifier key in the NSExtension dictionary in its Info.plist; found: %@
hasAppGroupContainers
0123456789abcdef
com.apple.MobileContainerManager.DataContainerClass
%@ is missing its bundle executable. Please check your build settings to make sure that a bundle executable is produced at the path \"%@\".
DataProtectionClass
In test mode, forcing code signing enforcement to be enabled
Failed to save bundle metadata for %@. Error: %@
UniqueInstallID
MIReserveMemoryForValidation
Delegate unexpectedly was nil
-[MIFileManager realPathForURL:allowNonExistentPathComponents:isDirectory:error:]
rank
redownloadParams
ValidatedByProfile
Failed to construct path to installcoordinationd daemon container
Failed to delete container_object_t for %@
Removing created container for which we were unable to create an object to represent: %@
MIAppReplacementStatusInProgress
App
UILaunchImageName
mkpath_np of %@ failed: %s
Failed to get app extensions in app %@
kMISValidationInfoSignerType is not set or is not a number for %@
PluginOwnerBundleID
Failed to get URL for container %@
v24@?0@\"NSString\"8@\"ICLAppExtensionRecord\"16
com.apple.MobileInstallation.WorkaroundBundleSymlinkName
Attempted to set container %@ with content class %llu on %@ which represents a container with class %llu
14.0
_DiscoverPersonasFromBundleContainer
Skipping device thinning check because of a set default
Journal
+[ICLWorkspace _connectionToInstallationDaemonWithError:]
RequiredOSVersion
UIRequiredDeviceCapabilties requested value '%@' that is not a boolean for key '%@'. Only boolean values are supported. Forcing mismatch.
lstat of %s failed: %s
Could not get signature version from %@
installSessionID
MIInstallationDomainUserPrivate
Developer
This bundle is a placeholder and so does not have an executable, so executable image slices are not available.
Creating new link at %@
Failed to seek to %lld from current offset in %@ : %s
-[MIFilesystemScanner _scanAppsDirectory:withError:]_block_invoke
Found emergency offloaded app %@ from OS build %@
Failed to enumerate matching profile for app identifier %@: %@
com.apple.watchkit
GeoJSONCaptureFailed
Unable to get hashes for executable %@
Removing transient bundle container: %@
Failed to create bundle object for system app %@ at %@
%@ does not have any app extensions that implement any of the required extension points for its configuration. Based on its configuration, this app must have at least one app extension that implements one of these extension points: %@.
com.apple.web-browser-engine.networking
Failed to retrieve realpath for base path %@ 
Failed to get plugin data containers for app extension %@ in bundle %@ for persona %@ : %@
-[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:]
Failed to remove previous symlink at %@ : %@
_writeSinfData
CodeInfoIdentifier
LastBuildInfo.plist
com.apple.iTunesStore.downloadInfo
distributorAccountID
com.apple.install_session_uuid
app identity is nil
-[MIInstalledInfoGatherer _sandboxEnvironmentForDataContainer:]
NSExtensionPrincipalClass
hasSystemContainer
_installd
+[MIInstallationIdentity installationIdentityForBundle:settingIfNotSet:error:]
+[MIContainer containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:constructor:created:error:]
identity
-[MIBundleContainer captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
Failed to create a continuation
NSExtensionContextClass
Failed to write iTunesMetadata to %@
Could't remove placeholder EA on \"%s\"
PluginKitPlugin
uniqueInstallID
Ignoring WatchKit 1 app extension with identifier %@
@\"MIBundleContainer\"24@?0@\"MIMCMContainer\"8^@16
(%@-%@)
PersonaMigrationFromUMComplete
personaUniqueString
-[MIGlobalConfiguration _bundleIDMapForBundlesInDirectory:withExtension:loadingAdditionalKeys:]
Updating MCM with signing info for %@ : %@; options %@
The app extension at \"%@\" specifies the entitlement \"%@\" = \"%@\" where the value does not match the parent app bundle's CFBundleIdentifier, \"%@\". This entitlement, if set, must have a value that matches the bundle identifier of the p
MI_ALLOW_SWITCHING_PERSONAS_ON_INTERNAL_BUILD
-[ICLHelperServiceClient stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:]_block_invoke
Unique ID provided, %@, wasn't of expected length %zu
Failed to make staged container live %@
Failed to set value %@ for key %@ for container %@
id
__DATA segment exceeds bounds in %@
driverKitExtensionURLs
distributorID
-[MIDataContainer setContentProtectionClass:]
No bundle container found for identifier %@
Appex bundle at %@ with id %@ defines either an NSExtensionMainStoryboard or NSExtensionPrincipalClass key, which is not allowed for the extension point %@
Expected to create/fetch only one container for %@ with persona %@, but got %ld
-[MIDriverKitBundle currentOSVersionForValidationUsingPlatform:withError:]
serializedContainerRepresentation
-[MIStoreMetadata initWithDictionary:]
Failed to read app replacement state from [
App with id %@ is not in the system app map even though it's type system
Unable to determine application type for %@
-[ICLInstallationDaemonClient _sharedConnectionWithError:]
-[MIFileManager removeItemAtURL:keepParent:error:]
_ClearExtendedAttributes_block_invoke
container_operation_delete_array returned NULL but did not set an error
Uninstalling profiles for %@
stashedAtTimestamp
App %@ is denylisted; returning failure for capabilities match.
Got non-dictionary response from MCM: %@
..
-[MIFileManager _realPathWhatExistsInPath:isDirectory:]
Failed to decode the nameTranscriptions dictionary.
UserManagement
host
sMITestMode
com.apple.mis.warning
v32@?0@\"NSString\"8@\"NSString\"16^B24
AppBlacklisted
XRSimulator
UIRequiredDeviceCapabilties in Info.plist has a key that is not a string.
-[MIBundleContainer _configureBundleWithError:]
-[MIBundle bundleInfoPlistSupportedPlatforms]
Could not create certificate from data for %@
Could not determine architectures in the executable at \"%s\" because the file is malformed.
Could not create MISProfileRef from profile data of length %lu
Serialized container did not encode an identifier
-[MIBundleContainerToken initWithCoder:]
com.apple.SharedWebCredentialViewService
embedded.provisionprofile
ApplicationSINFCaptureFailed
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_BACKGROUND
Asked for data containers for %@ but none is needed.
Failed to load sinf file %@ : %@
Failed to find runnable executable slice for \"%s\". The architectures in the file could not be determined.
launchProhibited
betaBuildGroupID
Failed to fetch alternative bundle at %@ : %@
v32@?0@\"NSString\"8@\"NSURL\"16^B24
No WatchKit extension found
Failed to create MIContainer instance for %@
-[MISystemAppState _onQueue_setSystemAppStateList:]
codeSigningInfoNotAuthoritative
bundleContainerURL parameter was not a valid URL
Could not get downloader DSID from SINF at %@: %ld
isEligibleForWatchAppInstall
application-identifier
Failed to get the path to the executable for bundle at %@
+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]_block_invoke
com.apple.developer.browser.app-installation
Failed to clear apps associated with persona %@
NSExtensionPointVersion
Appex bundle at %@ with id %@ defines an EXPrincipalClass key in the EXAppExtensionAttributes dictionary in its Info.plist with a zero length string.
/private
TEST MODE: Returning fake launch warning data for %@
Updating app extension data containers with their parent bundle ID
-[MIBundle hasAtLeastOneExtensionImplementingExtensionPointIn:error:]
IntentsAppexIntentsRestrictedNotSubset
UninstallParallelPlaceholder
Got exception while serializing MIBundleMetadata to %@ : %@
-[ICLHelperServiceClient volumeUUIDForURL:error:]_block_invoke
Entry %hu in %s did not include name information even though we requested it.
-[MIBundle siriIntents]
-[MIGlobalConfiguration _bundleIDMapForBundlesInDirectory:withExtension:loadingAdditionalKeys:]_block_invoke
+[MIBundleContainer appBundleContainerForIdentifier:temporary:inDomain:constructor:withError:]
extensionOwnerBundleID
Unknown MIInstallationDomain: %lu
%@ was grandfathered but has no-sandbox entitlement
No WatchKit 2.0 placeholder found for app %@
mkdir of %@ failed: %s
_CreateErrorForMachOBestSliceEBADARCH
label
managementDeclarationIdentifier
TraverseDirectoryWithPostTraversal
-[MIBundle validatePluginKitMetadataWithError:]
POSIX error %d (%s)
B24@?0^{?=QqQ*Q*QIIIIIIISBC}8^B16
localizedDistributorName
lseek to %lld failed: %s
CFFIXED_USER_HOME
Successfully created the sentinel file for running in test mode: %@
/var
_GetContinuationFD
Failed to read stash metadata from %@
AppexBundleMissingEXPrincipalClassString
Multiple signer organizations found for %@; picking the first one of %@
Failed to locate personal persona: UserManagement returned %lu personas but none of them had isPersonalPersona = YES
Bundle at path %@ did not have a CFBundleIdentifier in its Info.plist
-[MIDaemonConfiguration installcoordinationdUserDataLibraryDirectory]
com.apple.geoservices.mapdata
AppleInternal
Interface-notification
MissingBundleNameString
lstat() failed for %@: %s
Appex bundle at \"%@\" with identifier \"%@\" contains a '.' in the portion after the parent app's prefix (prefix: \"%@\" ; dot in: \"%@\").'
DownloaderID
Failed to get primary persona unique string
-[MIContainer recreateDefaultStructureWithError:]
-[MIPluginKitBundle _validateXPCServiceWithOverlaidDictionary:error:]
Failed to search for apps in %@ : %@
-[MIAppExtensionBundle validateHasCorrespondingEntitlements:error:]
-[MIFileManager setModificationDateToNowForURL:error:]
itemID
No stash was found in bundle container %@ with index %lu (at %@)
This app has the %@ key set in its Info.plist, which identifies it as a shell app surrounding a Watch-only app; these are not installable.
com.apple.installd.MIKeychainAccessGroupTracker
InvalidSymlink
Failed to open executable at %s
Deleting old link at %@ because it's not needed or not correct anymore
Dictionary parameter was nil or not a dictionary
stagingSubsystem
Failed to remove keychain items %@
isResolved
There is nothing to be made live
Framework
nameTranscriptions
DriverKit extension
com.apple.developer.networking.networkextension
com.apple.developer.default-data-protection
[f]setxattr failed for path %s fd %d
Failed to retrieve realpath for suspicious path %@
betaExternalVersionIdentifier
Removing bad SINF for identifier %@
CFBundleSupportedPlatforms
%@ 
-[MIContainer _deriveContainerStatusWithError:]
Skipping device family check because of a set default
+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]
bundleIdentifier
originalInstallDate
-[ICLStashedAppRecord isEqual:]
Couldn't get data from xattr named %s on \"%s\"
Invalid type for metadata property %@
Client provided invalid persona for %@
B12@?0i8
Any
Failed to enumerate stashed container
MIInstallProfileWithData
_CodeSignature/CodeResources
<%@ identity:%@/%@ isTransient:%c containerClass:%llu>
Appex bundle at %@ with id %@ does not have a string value for the NSExtensionContextClass key in the NSExtension dictionary in its Info.plist
appReplacementSourceBundleIdentifier
com.apple.family
-[MIFileManager itemExistsAtURL:error:]
PluginKit plugin with identifier %@ already found at path %@; ignoring discovered plugin at %@
-[MIDriverKitBundle validateBundleMetadataWithError:]
CFBundleInfoPlistURL
>
Ignoring %@ at %@ because it doesn't work on this OS version
-[MIKeychainAccessGroupTracker _onQueue_discoverReferences]_block_invoke
Unknown filesystem object type %u encountered at %s
_CopyEAList
UserManager returned an empty persona list
Info.plist missing at %@
driverkit
Failed to supersede container %@ with %@
__LINKEDIT segment found after LC_CODE_SIGNATURE load command in %@
/
Pref set to ignore code signing enforcement boot-args
%d: %@
LibMISErrorNumber
Failed to remove execute permissions from bundle executable at %s : %s
Expected to find PERSONAL persona data container in %@
com.apple.installd.appIdentifier
-[MIMCMContainer recreateDefaultStructureWithError:]
/System/Library/PrivateFrameworks/Pasteboard.framework
@\"MIDataContainer\"32@?0@\"NSString\"8^B16^@24
previous-application-identifiers
containerURL
Failed to create MIStashedBundleContainer instance for %@
Ignoring copyfile error at %d while copying %s to %s: %s (%d)
iad-impression-date
[system-defined]
EXAppExtensionAttributes
MICopyCurrentBuildVersion_block_invoke
-[MIBundle _filterExtensionBundlesNotInCacheIfNeeded:]
Extension cache does not define an NSExtension dictionary in its Info.plist: %@
%@ with identifier %@ is already installed, so we can't install %@ with that same identifier.
Failed to lstat %@ : %s
Failed to remove attribute %s from %s: %s
Failed to get entry for bundle %@ in %@ personas %@ : %@
Made container live for %@ at %@
Failed to get identifier for the container
AppexBundleIllegalExtensionAttributesDict
RequiredOS
Failed to copy the OS build version
Failed to remove the file at %@ : %@
Failed to make new data container for app %@ live: %@
Skipping purging of transient container because it is staged: %@
void *UserManagementLibrary(void)
Invalid mach_header.magic in %@ : 0x%08x
AppexBundleIllegalExtensionViewControllerHostClass
-[MIBundleContainer cloneContentFromStashedBundleContainer:error:]
softwareVersionExternalIdentifier
MILocationSystemDefinedBase is currently unsupported
 that expects paths on a volume with UUID [
Expected to read %zu bytes but got %ld bytes when reading %@
Failed to write SYSTEM persona extension marker on plugin data container %@: %@
Allowing patch installation without sinf present in options
This app was not built to support this device family; app is compatible with %@ but this device supports %@
directory
v20@?0I8^B12
Failed to fetch SYSTEM persona extension marker info from plugin data container %@: %@
Failed to recreate structure for %@
There is nothing to purge
MIDiskImageManager
UISupportedInterfaceOrientations
Could not get code info identifier from %@
WatchKit 2 app extension's NSExtension.NSExtensionAttributes.WKAppBundleIdentifier value is missing (should be WatchKit app's bundle ID).
_UIApplicationMain
MIInstallationDomainSystemShared
HasSystemGroupContainers
Staging destination path was too long: %s (%zu)
private
storefrontCountryCode
RatingRankEligibilityDomain
IsMarketplace
SigningInfoSource
+[MIBundle _URLOfFirstBundleInDirectory:withExtension:error:]
disk image app
write() returned %zd but we expected %lu when writing to %s
MIAppReplacementStatusMax
rename of %s to %s failed: %s
WKApplication
Library/Logs/MobileInstallation
Cleaning up test mode state for %d
-[MILaunchServicesDatabaseGatherer _setForEntry:]
Invalid type for metadata property %@ in %@
subGenres
Consumed sandbox token %lld for container at %@
Failed to allocate %lld bytes : %s
\"
-[MIFileManager diskUsageForURL:]_block_invoke
storeCohort
+[MIStoreMetadata metadataFromPlistData:error:]
Restoring backed up system app state following a restore: %@
Failed to determine if we're running in test mode: %@
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
This app has the same bundle ID (\"%@\") as a known deletable system app but is missing the required entitlement \"%@\" = true (boolean).
Failed to remove app replacement state at [
com.apple.installd.umAccessQueue
-[MIInstallationIdentity initWithSessionID:uniqueID:]
Failed to load Info.plist from bundle at path %@; %@
-[MIGlobalConfiguration migrationPlistURL]
com.apple.social.SLYahooAuth
com.apple.private.mobileinstall.upgrade-enabled
ACL=<not found> 
localizedDistributorName dictionary does not have expected type
SC_Info/Manifest.plist
dext
volumeUUID
EnvironmentVariables
com.apple.private.extensionkit.builtinsystempersona
B16@?0^{container_object_s=}8
Failed to load Info.plist from bundle %@
Preserving compressed bit on %s
-[MIFileManager dataProtectionClassOfItemAtURL:class:error:]
Suspicious path %@ does not contain base path %@ as a prefix
-[MIInstallationIdentity _writeToBundle:error:]
Bundle at path %@ has missing or invalid CFBundleExecutable in its Info.plist
Unsigned Placeholder
-[MIBundleContainer captureBundleByMoving:withError:]
-[MIBundleContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:]
-[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
iAdConversionDate
NSExtensionPointIdentifier
signerOrganization
24B
com.apple.susuiservice
com.apple.mobileinstallation.companion_placeholder
-[MIDataContainer _oldCompatiblityLinkDestination]
IntentsAppexMissingIntentsSupported
MIAppReplacementStatusUnknown
removefile_state_set REMOVEFILE_STATE_ERROR_CALLBACK failed: %s
_IsDictionaryWithKeyStringAndValueArrayOfString_block_invoke
Internal error: totalProcessedEntryCount (%u) was less than reprocessCount (%u)
Failed to delete temp container %@: %@
The app extension stub app %@ must have at least one app extension, but none were found.
InstallQOSOverride
ExtensionDataContainerParentIDUpdateVersion
Removing matching profile for %@: %@
Discovered %@ app without bundle container %@
MIInstallationDomainMax
Could not get current build info; assuming this is an upgrade
MultipleFileProviderAppexBundles
Appex bundle at \"%@\" with identifier \"%@\" does not have expected identifier prefix \"%@\"
Stashed previous version of %@
xpc
container_copy_sandbox_token returned NULL!
System/Library/disableSystemAppDeletion
secondaryGenreId
_GetAttrBuffer
Failed to construct CFBundle for moved bundle at %@: %@
, 
com.apple.message-payload-provider
Missing required internal content variant
2.0
com.apple.developer.marketplace.app-installation
-[MIFileManager copyVolumeInfo:forURL:error:]
-[MIPluginDataContainer setAssociatedBuiltInBundleURL:]
ValidatedByFreeProfile
MissingBundleIdentifier
NSUserActivityTypes
B20@?0i8r*12
com.apple.install_uuid
installDate
Unexpectedly received a nil rawContainer (MIMCMContainer)
LSCounterpartIdentifiers
/System/Library/Frameworks/System.framework
B24@?0*8Q16
WatchKit %@ app has disallowed Info.plist key: %@
-[MIBundleMetadata serializeToURL:error:]
CLKComplicationSupportedFamilies
app identity has nil personaUniqueString
-[MIInstalledInfoGatherer _groupContainersDictionaryForPersona:]
Failed to sanitize source file path %@
Could not get data length for extended attribute key %s: %s
Extension point identifier was not set for app extension with bundle ID \"%@\".
Failed to read app launch prohibition from [
-[MISignatureAgnosticHasher performHashWithError:]_block_invoke
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:]
-[MIExecutableBundle _hasNonContainerizingEntitlement:checkSeatbeltProfiles:]
kMISValidationInfoValidatedByProfile was not set for %@ but kMISValidationInfoSignerType was set to MISSignerTypeProfile
Executable at %@ did not match stub hash for cputype %d cpusubtype %d: %@ != %@
!
isMissingRequiredSINF
com.apple.MusicUIService
com.apple.developer.web-browser-engine.networking
-[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:]
Expected key to be a valid string.
Failed to symlink %s -> %s
Bundle at path %@ had an invalid CFBundleIdentifier in its Info.plist: %@
WKWatchKitApp
unknown bundle type
_ContainerURL
-[MIExecutableBundle isWatchOnlyApp]
assetToken
sinfInfo
applicationType
subgenres
[user-defined-directory/
Did not find last build info; we must be upgrading from pre-8.0 or this is an erase install.
Failed to scan %@ in %@ : %@
distributorDomain
mkdir failed for %s: %s
The base path %@ and/or suspicious path %@ were nil
Failed to discover associated personas for bundle in container %@ : %@
System/Library
-[MIFileManager _dataForExtendedAttributeNamed:length:onURL:orFD:error:]
Failed to get app extension bundles for bundle %@ : %@
com.apple.MobileInstallation.AssociatedBuiltInBundleURL
Failed to create a CFBundle instance from bundle at %@
Failed to stat path %s : %s
Executable at %s contained no image slices
-[MIFileManager createTemporaryDirectoryInDirectoryURL:error:]
Failed to get bytes at beginning of %@: %@
marketplaceItemID
NSExtensionViewControllerHostClass
UPPValidated
-[ICLWorkspace getAppLaunchProhibition:forBundleContainerURL:error:]
-[MIExecutableBundle lsInstallTypeWithError:]
plist
Failed to rollback iTunesMetadata: %@
SystemExtensions
com.apple.DocumentsApp
com.apple.private.webkit.pushbundle
com.apple.security.system-groups
v24@?0r*8^B16
stagingRoot
StaticDiskUsage
Failed to create sentinel file at %@ for running in test mode: %@
Skipping compatibility symlink because app was linked with SDK version 0x%08x
INIntentsSupported
AppexBundleIllegalXPCServiceDict
-[ICLWorkspace bundleRecordsForLaunchServicesWithWrapperURL:forBundleIdentifier:withError:]
-[MIBundle setBundleParentDirectoryURL:error:]
This method is not valid for MIDriverKitBundle
getattrlist failed for %@: %s
} 
INAlternativeAppNames
Failed to issue write barrier for %s : %s (%d)
The app extension at \"%@\" targets the extension point \"%@\" but is missing the corresponding required \"%@\" = TRUE (boolean) entitlement.
Assuming unknown built-in app %@ should be associated with primary persona
AppLaunchProhibition.plist
-[MIFileManager setOwnerOfURL:toUID:gid:error:]
Using trusted hashes from stub at %@
background
IsPlaceholder
Failed to clear code signing cache: %llu
Library/MobileInstallation
Could not get MID-based SINF status at %@: %ld
+[MILaunchServicesDatabaseGatherer entryForBundle:inContainer:forPersonas:withError:]
RunLoopType
releaseDate
isBeta
Deserialized SystemAppState dictionary from %@ did not contain only string keys and number values
UIRequiredDeviceCapabilities
-[MIRelocatedBundleContainer makeContainerLiveWithError:]
-[MIExtensionKitBundle validateBundleMetadataWithError:]
Ignoring failure to set protection class to %d on %@ (mode 0%o): %@
com.apple.AppStore
Unknown location type [
IntentsAppexIntentsSupportedDuplicated
-[MIDaemonConfiguration localSigningIsUnrestricted]_block_invoke
bundleID
-[MIExecutableBundle relativeExecutablePath]
com.apple.Home.HomeExtension
Updated app extension data containers with parent bundle IDs
-[MIUserManagement _onQueue_refreshPersonaInformationWithError:]
softwareVersionBundleID
Failed to get installType from bundle %@ : %@. Placeholder will have installed system app state.
CFBundleResourceSpecification
q
Failed to preserve existing stashed version of app %@ at %@
itemId
storefront
Failed to unset previous symlink name attribute on container %@: %@
fts_open failed for %@ : %s
-[MIExecutableBundle _makeContainersLive:ifRequired:error:]
DTCompiler
-[MIBundleContainer bundleMaxLinkedSDKVersion]
Attempt to clone %s to %s failed with EXDEV; falling back to copyfile
-[MIFileManager markBundleAsPlaceholder:withError:]
kMISValidationInfoSignerType was set to unknown value %ld
MILocationUserDefinedDirectory
+[MIBundle bundlesInParentBundle:subDirectory:matchingPredicate:error:]
com.apple.private.rating-rank-eligibility-domain
+[MILaunchServicesDatabaseGatherer _gatherPluginDataContainersForAppExtension:parentBundleID:personaUniqueStrings:parentBundleTypeIsApp:updatingAppExtensionParentID:associatedPersonas:error:]
InstalledContentLibrary.MILocationSystemDefinedBase
placeholderFailureUnderlyingError
Failed to retrieve any containers for identifier: %@ groupIdentifier: %@ container type: %llu persona: %@
Existing container was nil but replacement reason was not NewContainer; given %ld
LSApplicationLaunchProhibited
Could not get contents of watch placeholder directory in %@
AppexBundleIDSuffixContainsPeriod
MI_Transient_Bundle_Cleanup
+[MIFileManager _sanitizeFilePathForVarOrTmpSymlink:error:]
Failed to write serialized MIStashedBundleMetadata to %@
-[MIBundle _validateAppNSPrivacyTrackingDomainsWithError:]
StashedVersionInfo
Library/ExtensionKit/Extensions
-[MIExecutableBundle bundleSignatureVersionWithError:]
Failed to get XPC connection
categories
Refusing to write 
Got unknown value %u for %s extended attribute on %@
Failed to deserialize container data for token %@
Extensions
-[MIBundle validateAppMetadataWithError:]
-[MIUserManagement primaryPersonaUniqueStringWithError:]_block_invoke
Failed to create helper log directory at \"%@\": %@
com.apple.developer.memory.transfer-accept
_ProcessContinuation
setattrlist failed for file %s
-[MIBundle _filterExtensionBundles:forValidationFlags:]
IsNoLongerCompatible
-[ICLWorkspace enumerateCryptexContentWithBlock:error:]_block_invoke
-[MITestManager setIsRunningInTestModeForProcessWithPID:withError:]
_CopyfileStatusCallback
-[MIMCMContainer regenerateDirectoryUUIDWithError:]
Resolved persona for %@, from %@ to %@
Appex bundle at %@ with id %@ does not define an extension point in its Info.plist
Expected executable at \"%@\" %@to have a __swift5_entry section
-[MIGlobalConfiguration _ixDataStorageHomeURLWithError:]
Could not get install type because no bundle container relation is set on %@
Unknown location type
Failed to set up daemon container for persona %@: %@
TeamIdentifier
CodeSignerType
+[MICodeSigningInfo signingIdentifierForAuditToken:error:]
referrerApp
%@/%@
LSEligibilityPredicatesValidAtEraseInstallDataMigration
Clearing test flags 0x%llx (0x%llx -> 0x%llx)
-[MIFileManager realPathForURL:ifChildOfURL:]
+[MICodeSigningVerifier validateWatchKitV2StubExecutableBundle:error:]
isWebNotificationBundle
System
Failed to remove extended attribute named %@ from %s: %s
+[MILaunchServicesDatabaseGatherer _createPluginDataContainersForAppexBundle:forPersona:setParent:didUseProvidedPersona:containedInAppBundle:]
Failed to get system persona unique string
Failed to get parent bundle ID for plugin data container %@ : %@
-[MIContainer setDataProtectionClass:forSecondOrThirdPartyApp:]
Failed to compute hash for Info.plist at %@
-[MIKeychainAccessGroupTracker init]
TMPDIR
com.apple.private.security.no-container
symlink failed for %s -> %s: %s
Got exception while serializing MIStashedBundleMetadata to %@ : %@
Failed to rename %s to %s : %s
Installation domain %@ does not map to a container class.
Couldn't get length for xattr named %s on \"%s\"
Skipping FIFO encountered at %s
Data for extended attribute key %s was empty
-[MIPluginDataContainer setSystemOrAnyPersonaExtension:]
Frameworks
-[MIBundle thinningMatchesCurrentDeviceWithError:]
Failed to find a valid architecture for %@ at %@ : %@
uname() failed
-[MIBundleContainer cloneContentFromStashedBundleContainer:error:]_block_invoke
%s EA was not set to expected value from \"%s\"
Discovered persona %@ type %lu mount %@
-[MIFilesystemScanner _scanFrameworkDirectory:withError:]
Failed to remove iTunesMetadata: %@
Failed to set SDK version in cache on %@ : %@
Failed to get data container for containerized app %@ for persona %@ : %@
shortItemName
ratingLabel
isOnMountedDiskImage
Failed to get watchkit plugin for %@: %@
CFBundleIdentifier
WatchKitAppInvalidInfoPlistKey
Unable to determine SDK version for executable at %@
-[MIFileManager itemDoesNotExistAtURL:]
Unable to compute hash for stub %@
Detected upgrade from %@ (%@) to %@ (%@)
Invalid mach_header.sizeofcmds in %@
-[MIPluginDataContainer parentBundleID]
Could not read SINF at %@ for identifier %@: %@
-[MIKeychainAccessGroupTracker _keychainAccessGroupsForBundle:error:]
com.apple.social.SLGoogleAuth
com.apple.installd.placeholder
Failed to get filtered Info.plist with keys %@ from bundle %@
associatedPersonas
/System/Library/PrivateFrameworks/AirPlayDiagnostics.framework
Load command %d exceeds bounds in %@
Failed to read sinf at %@ : %@
-[MIContainer _doInitWithContainer:error:]
ITSWatchOnlyContainer
+[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:created:error:]
StashMetadata.plist
-[MIFileManager _bulkSetPropertiesForPath:existingFD:UID:GID:mode:flags:dataProtectionClass:removeACL:error:]
open() failed for %@: %s
com.apple.MobileInstallation.ParentBundleID
embedded watch app
groupContainers
PathArgument
Validating %@ as removable system app
-[MIBundleContainer stashBundleContainerContents:error:]_block_invoke
Failed to create temp dir at path %s
invalid symlink at %s
-[MIUserManagement isKnownPersonaUniqueString:error:]_block_invoke
shareURL
ApplicationVerificationFailed
Ignoring extension with identifier %@ due to missing extension cache entry; continuing
Failed to get data container for bundle %@ for persona %@ : %@
Operation to update protection classes for %@ to class %d failed with error %@
System/Library/AppPlaceholders
CF_MIEmergencyOffloadVersion
GeoJSON
com.apple.app-migration
Could not determine architectures in the executable at \"%s\".
Failed to read persona attributes from UM
v32@?0@\"NSString\"8@\"MIPersonaAttributes\"16^B24
Device capabilities do not match requirements: %@
-[MIInstalledInfoGatherer _populateBundleRecordValues:signingInfo:error:]
isNoLongerCompatible
WatchKit %@ app had an Info.plist key that was not a string.
-[MIFileManager removeExtendedAttributeNamed:fromURL:error:]
system app placeholder
-[MIAppIdentity _eligiblePersonaForBundle:error:]
Exempting %@ from System App bundle ID conflict check because it has the System App entitlement
bundleShortVersionString
Appex bundle at %@ with id %@ does not define an NSExtension dictionary in its Info.plist
Expected to find one or more platform slices for %@ in executable at %@ but only found other platforms: %@
-[MIExecutableBundle hasNoConflictsWithOtherInstalledEntitiesForSigningInfo:forPersona:error:]
regular file
copyfile hit ENOTSUP in source hierarchy while copying %s to %s; src mode: 0%o
, osBuildVersion=
Failed to read %zu bytes : %s
-[MIFilesystemScanner _scanAppsDirectory:withError:]
(container_get_error_description returned NULL)
com.apple.mobileinstallation.stash
Couldn't open bundle \"%s\" for setting extended attributes: %s
purchaseDate
nameTranscription dictionary does not have expected type
environmentVariables
UIRequiredDeviceCapabilties requested key '%@' that did not return a boolean value. Only boolean values are supported. Forcing mismatch.
com.apple.SharingViewService
-[MICodeSigningVerifier _getMICodeSignerTypeFromMISInfoDict:codeSignerType:profileType:error:]
Failed to extract signer identity from %@
Validating executable at %@
User
+[MIBundle bundleIsInDenyList:]
AppexBundleIllegalExtensionPointIdentifierString
<%@ platform:%@ sdkVersion:%u minOSVersion:%u>
appletvos
Failed to open %s : %s
IntentsSupported
Failed to check for upgrade container for identifier %@ : %@
-[MIExecutableBundle _dataContainerCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]
-[MIGlobalConfiguration hasInternalContent]_block_invoke
Scanned %lu items in container type %ld
AppexBundleMissingExtensionPointIdentifierString
Executable at %@ did not contain a slice built for platform %@ (found only platform %@).
Appex bundle at %@ with ID %@ does not have a CFBundleVersion key with a non-zero length string value in its Info.plist
-[MIFileManager mountPointForURL:error:]
-[MICodeSigningVerifier _loadSystemDetachedSignatureForBundleID:error:]
LegacyErrorString
AppManagementDomain
-[MIKeychainAccessGroupTracker _removeGroupsWithError:error:]
CodeSigningInfoNotAuthoritative
options dictionary parameter was not specified
@a
open of %s failed: %s
-[MIFileManager aclTextFromURL:error:]
Failed to get home dir path size: %s
PersonalPersonaPlaceholderString
iTunesMetadataCaptureFailed
MOBILEINSTALLATION_TEST_LAUNCH_WARNING_DATA
 with a source app identity to [
isPlaceholder
NSExtensionContextHostClass
-[MISignatureAgnosticHasher performHashWithError:]
sinf subpath %@ contains illegal '..' segment
Appex bundle at %@ with id %@ does not have a legal value for the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist; found: %@
The suspicious path %@ contains '..' paths, which are invalid
MessagesStubAppMissingAppExtension
<%@ : path = %@ identifier = %@ type = %@>
Exiting before replacing transient bundle container: %@
Path
-[MIPersonaAttributes dealloc]
Failed get container URL from %@
-[MIFileManager diskUsageForURL:]
Unknown QOS class value specified: %@; ignoring
%s
Failed to allocate hash read buffer: %s
Contents
Failed to get keychain access groups for app %@
Signpost
Could not get purchaser DSID from SINF at %@: %ld
Failed to clone stashed item %@ to %@
-[MIFileManager stageURLByMoving:toItemName:inStagingDir:settingUID:gid:dataProtectionClass:breakHardlinks:hasSymlink:error:]_block_invoke_2
_Bool TraverseDirectoryWithPostTraversal(const char *, TraverseDirectoryOptions, TraverseDirectoryAdditionalFetchProperties, NSError *__autoreleasing *, __strong TraverseDirectoryItemBlock, __strong TraverseDirectoryPostTraversalBlock)
Invalid staging content type: %lu
-[MIBundle currentOSVersionForValidationUsingPlatform:withError:]
v32@?0@\"ICLBundleRecord\"8@\"NSArray\"16@\"NSError\"24
com.apple.developer.accessory-transport-extension
Failed to setclass(%d) on file %s: %s
FIFO
MICreateCFBundleEnforcingInfoPlistSize
Got value for %s extended attribute on %@ with unexpected length %lu
Failed to get stash metadata from %@ : %@
-[MIInstalledInfoGatherer _populateBundleRecord:error:]
Found WatchKit app at %@ but it was not a WatchKit 2 app. Is it missing its app extension?
Failed to link %s to %s
-[MIFileManager logAccessPermissionsForURL:]
%s was called with a NULL path parameter.
sourceURL
getpwuid_r succeeded but no user was found with uid %d
MIRestoreIdentity
-[MIInstalledInfoGatherer _fixUpForBuiltInAppParallelPlaceholder]
-[MIExecutableBundle hasExecutableSliceForCPUType:subtype:error:]
Failed to find any app with bundle ID %@
-[MIBundle getIsBuiltForMacPlatform:error:]
6.0
targetUID
iAdImpressionDate
macosx
-[MIMCMContainer purgeContentWithError:]
MissingSINF
-[ICLSinfInfo isEqual:]
com.apple.mobileme.fmip1
com.apple.private.mobileinstall.xpc-services-enabled
acl_init() failed: %s
-[MIDataProtectionChangeOperation performChangeOperation]
The system version is lower than the minimum OS version specified for bundle at %@. Have %@; need %@
com.apple.developer.homekit
+[MIBundleContainer enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBlock:]
com.apple.developer.not-executable
Proxy returned error: %@
variantID
HasMIDBasedSINF
-[MIExecutableBundle _validateWithError:]
Failed to get data containers for identifier %@ : %@
-[MIFileManager extendedAttributesFromURL:includeCompression:error:]_block_invoke
Failed to decode app launch prohibition from [
got error while processing entry %hu in %s : %s
LinkedParentBundleID
DownloaderDSID
Appex bundle at %@ with id %@ does not define either an NSExtensionMainStoryboard or NSExtensionPrincipalClass key with a string value in the NSExtension dictionary in its Info.plist
malloc failed for %ld bytes: %s
Failed to fetch signature version for executable at %@ with libMIS error %@
copyfile of %@ to %@ failed: %s
Invalid type for metadata property '%@'.
-[MIPluginDataContainer isSystemOrAnyPersonaExtension]
Could not get the product version from MobileGestalt.
teamIdentifier
Did not find at least one executable slice with CPU type %d and subtype %d in bundle %@
Install type not set in bundle metadata for %@
-[MIFileManager _itemIsType:withDescription:atURL:error:]
-[MIStoreMetadata initWithCoder:]
Expected '%@' array element to be a dictionary.
MobileInstallationDemotionCompleteErrorOccurred
-[MIFilesystemScanner _scanExtensionKitDirectory:withError:]_block_invoke
Failed to allocate memory for deleting containers
LSEligibilityUninstallPredicate
-[MIExecutableBundle codeSigningInfoByValidatingResources:performingOnlineAuthorization:ignoringCachedSigningInfo:checkingTrustCacheIfApplicable:skippingProfileIDValidation:error:]
References
readlink failed for %s: %s
-[MIAppIdentity resolvePersonaWithError:]
CFBundleIcons
DTXcode
Failed to get DriverKit support version: %s
Failed to create stash base directory at %@
bundleContainerURL
/System/Library/PrivateFrameworks/PassKitUIFoundation.framework
Invalid
IMPORTANT: Detected Internal release type but os_variant_allows_internal_security_policies returned false
com.apple.MobileInstallationHelperService
 osBuildVersion=
+[MIContainer _allContainersForIdentifier:persona:options:error:]
LSRequiresIPhoneOS
-[MIExecutableBundle onlyHasExecutableSlicesForPlatform:error:]
Serialized container encoded invalid class: %llu
MIMachOFileIterateImageSlices
sourceApp
Failed to locate last path element in %s
-[MIPluginKitBundle overlaidInfoPlistWithError:]
NSExtensionPointName
EXPrincipalClass
Failed to clean up %s EA on \"%s\": %s
Failed to determine destination of link at %@ : %@
This app is not compatibile with this device. This app specifies a value for UISupportedDevices in its Info.plist as [%@], but none of the identifiers in this device's compatibility list are present in this app's supported devices. This dev
-[MIAppExtensionBundle validateHasNoDotInBundleIDSuffix:]
containerClass
Failed to realpath %s : %s at %s
Failed to get data containers for containerized app %@ for persona %@ : %@
The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these platform
AppReplacementState.plist
Failed to get signing identifier from SecTask for pid %d
initiated
AppexBundleMissingNSExtensionDict
MIWatchKitVersion_1_0 == version || MIWatchKitVersion_2_0 == version
lstat returned an error when trying to determine type for %s
CPUSubtype
open failed for %s : %s
tmp
App Extension
Could not extract signer identity for %@
com.apple.managed_drm_id
InvalidSupportedDevices
-[MIMCMContainer initWithSerializedContainer:matchingWithOptions:error:]
UIRequiredDeviceCapabilties in Info.plist does not have an array or dictionary value.
com.apple.fieldtest
-[MIExecutableBundle dataProtectionClass]
Failed to remove underlying transient container for %@ : %@
An error occurred when reclaiming disk after replacing a container of class %ld with identifier %@ : %@
isMarketplace
Failed to consume daemon container sandbox token: %d (%s)
Don't know how to check bundle %@ for conflicts.
com.apple.developer.wrapper-bundle
Failed to convert app identifier EA data (%@) to string from \"%s\"
-[MIDaemonConfiguration codeSigningEnforcementIsDisabled]_block_invoke
Found unexpected value for entitlement %@: %@; falling back to persona %@
Allowing possibly ad-hoc signed binary at path %@
Failed to remove the source contents at %@ after a successful swap : %@
CPUType
Failed to open %s
unspecified
signerIdentity
FunctionName
-[MIFileManager _stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:]_block_invoke
supportPageURL
Failed to construct MIContainer object for all %llu containers; last error is underlying error
Unexpectedly received existing container %@ when request was to create a new container for %@
Appex bundle at %@ with id %@ does not define a NSExtensionPointIdentifier key with a string value in the NSExtension dictionary in its Info.plist
Expected value to be a valid array.
fstat failed for %s : %s
__TEXT
-[MIExecutableBundle enumerateDylibsWithBlock:]
stat of %s failed: %s
socket
macho_best_slice_in_fd failed
Failed to decode app replacement state from [
-[MIContainer dealloc]
Failed to write uninstalled list to %@ : %@
dateStashed
Failed to get group container path for group 'systemgroup.com.apple.installcoordinationd'; container_system_group_path_for_identifier returned %llu
-[MITestManager _onQueue_clearTestFlags:]
WatchKitAppIllegalInfoPlistKey
Array of supported device families returned from MobileGestalt was not an array of numbers; got: %@
Failed to resolve persona %@
CFBundleDevelopmentRegion
beta-reports-active
v20@?0I8I12I16
SystemAppInstallState.plist
com.apple.developer.on-demand-install-capable
Verifying signature of %@ with options %@
rating
Unable to get primary persona unique string from UserManagement
-[MIExecutableBundle fairPlaySinfInfoWithError:]
-[MIAppExtensionBundle validateBundleMetadataWithError:]
InstallDeviceClasses
_sinfURLsForBundle
MIInstallationDomain was not set to either MIInstallationDomainSystemShared or MIInstallationDomainUserPrivate: %lu
Failed to lchown %s : %s
Failed to read file at %@: %s
+[MIMCMContainer _containerForIdentifier:contentClass:forPersona:transient:create:error:]
ICLWorkspaceErrorDomain
getmntinfo_r_np failed: %s
InstalledAppInfoArray
codeSignerType
%s is unavailable on this platform
Couldn't get %s EA from \"%s\": %s
Failed to get list of extended attributes: %@
autoInstallOverride
com.apple.security.system-group-containers
Failed to remove ACL
Got unknown value %u for Sinf data type to set on %@
Failed to construct MIMCMContainer instance with container %@ : %@
com.apple.WebKit.PushBundles
extendedAttributes=%@ 
Attempting to restore an identity without having first assumed an identity
B36@?0i8r^{mach_header=IiiIIII}12Q20Q28
Made safe harbor container active for %@ at %@
/System/Library/PrivateFrameworks/AdminLite.framework
iPhoneOS
Could not install embedded profile: 0x%08x (%@)
com.apple.intents-service
ParallelPlaceholderPath
bundleVersion
MissingBundleVersion
Failed to move application at %@ into container path %@
temp.XXXXXX
copyfile hit ENOTSUP at %d while copying %s to %s; src mode: 0%o
Executable stub at %@ not signed by Apple.
Failed to serialize app replacement state for [
Invalid LC_CODE_SIGNATURE command in %@
Failed to getclass of file %s: %s
hasSystemGroupContainers
System/Cryptexes/OS
Unable to determine if bundle executable is present at \"%@\".
Failed to set symlink name attribute on container %@: %@
%d: %@ (%@:%ld %@)
-[MIExecutableBundle watchKitAppBundleForWKVersionOrEarlier:error:]
Could not get contents of Watch directory in %@
Failed to get Info.plist URL from %@; falling back to assumed path
-[MIKeychainAccessGroupTracker _keychainAccessGroupsForApp:error:]
CoreOS
com.apple.Posters
DriverKit extension bundle at \"%@\" with identifier \"%@\" does not have expected identifier prefix \"%@\"
Failed to read iTunesMetadata.plist from %@
-[MIExecutableBundle validateSinfWithError:]
seatbelt-profiles
factoryInstall
lseek to %lld from current offset failed: %s
-[MIMCMContainer _refreshContainerMetadataWithError:]
compatibilityState
MigrationInfo.plist
-[MIFileManager modificationDateForURL:error:]
Object returned from _CFPropertyListCreateFiltered was not a dictionary, was type %@
The executable at \"%s\" does not contain any code that is runnable on this device.
DeviceBasedVPP
dateOriginallyInstalled
Multiple WatchKit app extensions found in app but only one is allowed (found %@ ; already found %@)
Rejecting %@ with base %@ because base component count is greater than child component count (reals %@ ; %@)
Stub %@ does not have required section %@
-[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:personas:enumerator:error:]_block_invoke
artistName
+[MIStoreMetadata metadataFromPlistAtURL:error:]
Could not get build version from last build info dictionary; assuming this is an upgrade
B20@?0@\"NSURL\"8C16
-[MIGlobalConfiguration lastBuildInfoFileURL]
MI_App_References
InstalledContentLibrary.MILocationUserDefinedDirectory
Updating sinfs with %lu bytes of data at URLs: %@
com.apple.Diagnostics.Canary
enterpriseInstallURL
iAdAttribution
EXExtensionPointIdentifier
Failed to lstat %@ : %s (%d) (may require significant memory usage to validate this app)
apfs
Cannot set installation identity for non-app bundle %@
Failed to create %@ instance for %@
Unexpectedly got nil persona for %@
Expected to move %s to %s but got EXDEV; falling back to copyfile
UMUserManager
Returned %zu bytes of validation memory after testing
com.apple.MobileContainerManager.ParentBundleID
FairPlay check for SINF validity in %@ returned error %d
Realpathed %@ ; appending non-existing components %@
Read entry length %u for entry %hu but that put us off the end of the buffer
framework
MacOS
Trying to fetch watchkit version for non-watchkit app %@
Failed to remove move source after copy at %s : %@
+[MIUserManagement sharedInstance]_block_invoke_2
hasCriticalAlerts
Unexpectedly found a second watch app, \"%@\", in this app's \"%@\" directory when we had already found \"%@\" in that directory. An iOS app may only have one embedded watch app.
dirfd of %s failed: %s
Failed to get data for EA key \"%@\": %@
Unknown:%d,%d
v40@?0r^{mach_header=IiiIIII}8Q16Q24^B32
ICLSoftLinking.h
*I
-[MIExecutableBundle compatibilityState]
SignatureVersion
void *ExtensionFoundationLibrary(void)
-[MIFileManager _removeACLAtPath:isDir:error:]
Failed to iterate mach-o slices for input file: %s
Failed to discover dylibs in directory %@
IllegalXPCServiceRunLoopType
-[ICLWorkspace bundleRecordsWithFrameworkURL:options:withError:]_block_invoke
UIApplicationDelegateClass
Could not determine architectures in the executable at \"%s\" because the file is not a mach-o format file.
Failed to read plist from %@
not 
HasSettingsBundle
Ignoring %@ %@ because it is not applicable to this device's capabilities: %@
DiskUsageBytes
Failed to get container path for %@
UISupportedDevices
More than one Siri Intents app extension in the app %@ declares the value %@ in the IntentsSupported array in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist.
-[MIInstalledInfoGatherer _stashedAppRecordForStashedContainer:]
Validating %@ as sub-bundle of removable system app
-[MIExecutableBundle _installEmbeddedProvisioningProfileAtURL:withProgress:]
WatchKit version enum value %hhu is no longer supported
%@.sinf
Appex bundle at %@ with id %@ defines a value for the \"XPCService\" key in its Info.plist that is not a dictionary.
IntentsRestrictedWhileLocked
IntentsAppexIntentsRestrictedFormat
-[MIGlobalConfiguration allowDeletableSystemApps]_block_invoke
CFBundlePrimaryIcon
PUICApplicationPrimaryColor
-[MIFileManager enumerateExternalVolumesWithBlock:]
MIFetchInfoForUID
watchos
Failed to retrieve value for key %@ from the underlying xpc object
-[MIGlobalConfiguration allowsInternalSecurityPolicy]_block_invoke
Siri Intents in the WatchKit app %@ are not a subset of the Siri Intents in the companion app %@
link failed for %s to %s: %s
Could not create symlink containing %s at %s: %s
setxattr for %s on %s failed
supportsAppMigration
WKRunsIndependentlyOfCompanionApp
AppexBundleMissingEXAppExtensionAttributesDict
System/Library/ExtensionKit/Extensions
com.apple.AppClips
Failed to copy %@ to %@
+[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersonas:inContainer:withError:]_block_invoke
Failed to create queue
AppexBundleIllegalPackageTypeValue
Extra info about \"%@\": 
Could not load detached signature data for %@ from %@
HasSystemContainer
MIBundleSupportedArchitecturesForPlaceholderInfoPlist
Found empty entitlements for %@ at %@
Failed to scan for bundle containers of content class %ld
-[MIMCMContainer diskUsage]
DTSDKName
Failed to set ACL on %s: %s
Live container is already present %@; continuing
-[MIFileManager setDataProtectionClassOfItemAtURL:toClass:ifPredicate:error:]
Expected Info.plist file at %@ but found something that was not a file (found mode 0%o).
Failed to get keychain access groups for %@
INTERNAL-ONLY BEHAVIOR: allowing bundle at %@ despite its ad-hoc signature because boot-args allow it to be runnable.
Failed to renameatx_np() for source fd %d path \"%@\" to destination fd %d path \"%@\" with flags 0x%x, Error: %s
referrerURL
_ParseContentDescriptors
Failed to read container error path
com.apple.mobile.installd
MIIsApplicableToCurrentDeviceFamilyWithError
com.apple.mobileinstallation.placeholder
futimes() failed for %@: %s
com.apple.installd
xrsimulator
-[MIFileManager installTypeFromExtendedAttributeOnBundle:error:]
-[MIFileManager _setData:forExtendedAttributeNamed:onURL:orFD:error:]
Failed to set data protection class %d on %@: %@
MinimumOSVersion
_StageURLByMovingProcessItem
Failed to fetch data containers for app extension at %@: %@; skipping it
kind
AdHocSigned
2.9.9
ReconcilingLSOperations
B48@?0^{__CFString=}8^{__CFString=}16^{__CFDictionary=}24B32B36B40B44
+[MICodeSigningInfo getValue:forEntitlement:fromProcessWithAuditToken:error:]
OSMinimumDriverKitVersion
CapabilitiesMatch
-[MITestManager _onQueue_setIsRunningInTestModeForProcessWithPID:withError:]
Executable at %s contained no identifiable architectures
iad-attribution
-[ICLAppExtensionRecord isEqual:]
Attempting to assume an identity of 0/0, which should be the default for the helper service
-[MIContainer initWithToken:options:error:]
-[MICodeSigningInfo initWithDictionaryRepresentation:fromSource:]
Found container %@ with no bundle; skipping.
-[ICLWorkspace enumerateBuiltInSystemContentWithBlock:error:]_block_invoke_3
System/Developer
com.apple.siri
Deserialized container object had identity %@/%@ but the token was for %@/%@
Failed to update container manager with code signing info for %@ : %@
InvalidWatchKitApp
Failed to clonefile %s to %s
Ignoring copyfile error in source hierarchy while copying %s to %s: %s (%d)
BuildMachineOSBuild
WKWatchOnly
B24@?0@\"MIContainer\"8^B16
entitlements
UIPrerenderedIcon
AppexBundleIllegalExtensionContextClass
SAD canary file exists. No system apps will be deletable
System/Library/CoreServices
+[MIMCMContainer deleteContainers:waitForDeletion:error:]
-[MIPluginKitBundle _validateNSExtensionWithOverlaidDictionary:error:]
-[MIExecutableBundle watchKitAppRunsIndependentlyOfCompanion]
-[MIFileManager _markEAFlag:forAppIdentifier:insecurelyCachedOnBundle:error:]
appleID
Got nil linkDestination and oldLinkDestination; not doing anything
Appex bundle at %@ with id %@ specifies a value (%@) for the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist that does not correspond to a known extension point.
ManifestCaptureFailed
Unexpectedly was not passed personas for app bundle %@ in container %@
__DATA
XROS
TestFileForSync
AppexBundleIllegalEXPrincipalClassString
Appex bundle at %@ with id %@ does not define the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist.
com.apple.mobilenotes
Ignoring app extension at %@ due to validation issue(s): %@. See previous log messages for details.
App extension with identifier %@ already found at path %@; ignoring discovered appex at %@
Failed to create container query for querying containers for identifier %@
Could not stat %@ : %@
[%@/%@/%@]
MIAppReplacementStatusCompleted
Executable at %@ did not contain a slice built for platform %@.
Unknown platform: %u
Failed to get executable bundle in container %@
DriverKitBundleIDNotPrefixed
-[MIFileManager createDirectoryAtURL:withIntermediateDirectories:mode:class:error:]
getxattr for installType EA on %s returned %zd (expected %zu)
IMPORTANT: Detected Internal release type but os_variant_has_internal_content returned false
failed to open %s : %s
Unable to compute relative executable path from base URL: \"%@\" executable URL: \"%@\"
data-protection-class
Failed to create app bundle from %@
/tmp/
Expected an array of string.
lsInstallType
s
Failed to allocate an attribute buffer!
Unhandled bundle type %hhu
com.apple.Faces
com.apple.developer.web-browser-engine.webcontent
isTransient
com.apple.MobileInstallation.SystemAppStateQueue
-[MITestManager clearIsRunningInTestModeForProcessWithPID:withError:]
-[MIFileManager setPermissionsForURL:toMode:error:]
gMfFfUYLxpniCKUmtjSz0XLrXGs=
md5
altDSID
+[MICodeSigningVerifier _validateStubSignature:withSigningID:error:]
Could not get access to staging directory
-[MIExecutableBundle _discoverWatchAppBundleAsPlaceholder:error:]
Preserved existing stashed version for %@
Failed to gather launch services info for %@ : %@
LSInstallByDefault
Failed to get ACL: %@
genreId
MaxWKVersion
-[MIContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:]
MIConsumeSandboxExtension
Failed to move clone replaced file from %@ to %@
+[MISystemAppState _systemAppStateFromURL:]
isUpdatedSystemApp
personasRecordMap
+[MICodeSigningVerifier _validateSignatureAndCopyInfoForURL:withOptions:error:]
internal app
The SINF provided for the bundle at %@ is not valid so this application will not run.
[f]getxattr failed for xattr named %s path %s fd %d
itemName
com.apple.web-browser-engine.content.development
%4d/%4d\t 0%08o\t %@\t ACL=%@
Failed to create an instance of MILocationUserDefined because the app bundle URL supplied was not for an app: [
Failed to decode plist from %@
ProductVersion
Failed to create container query for querying containers for identifier: %@ groupIdentifiers: %@ containerType: %llu
installBuildVersion
com.apple.MobileInstallation
Failed to set staged update container attribute for identifier %@ 
PersonaBundleIDPurgeCompleteInUM
Failed get container URL for %@ when trying to clone content from %@
-[MISignatureAgnosticHasher _hashSliceUsingFD:atOffset:withSize:machHeaderAndCommands:dictionaryKey:error:]
com.apple.mobile.installation
App with id %@ is not in the internal app map even though it's type internal
cZflGJ39lJHTCPy35/N14Q
-[MIContainerToken initWithCoder:]
SerializedPlaceholder.ipa
<%@<%p> installDate=%@, originalInstallDate=%@ installBuildVersion=%@, installType=%lu, placeholderFailureReason=%lu, placeholderFailureUnderlyingError=%@, placeholderFailureUnderlyingErrorSource=%lu, watchKitAppExecutableHash=%@, autoInsta
WatchKitAppExtensionInDisallowedLocation
Failed to fetch container URL from %@
-[MIExecutableBundle _hasNoConflictWithSystemAppsForSigningInfo:error:]
Verifying resources using detached signature for %@
InstalledContentLibrary.MILocationUserDefined
applicationDSID
title
Error when introspecting %@
Hashed more (%lld) than slice length %llu in %@
B16@?0@\"NSURL\"8
WatchKit 2 app contains a non-WatchKit extension at %@. WatchKit apps specifying a MinimumOSVersion earlier than 3.0 must have non-WatchKit extensions embedded within the WatchKit extension.
Ignoring symlink at %s
lstat for path \"/\" failed, which should never happen!
_DiscoverPersonasForBuiltInBundle
Bundle at path %@ has %lu %@ in its Info.plist, maximum of %lu allowed
%s is not a %@ (mode 0%ho)
extendedAttributes=<not found> 
Expected a valid dictionary.
Code signing enforcement is disabled.
installerEpoch
-[MIStashMetadata serializeToURL:error:]
-[MIKeychainAccessGroupTracker _onQueue_removeReferencesForBundle:error:]
-[MIExecutableBundle makeExecutableWithError:]
Failed to setclass(%d) on directory %@: %s
MIIsBuildUpgrade
Identifier %@ is a %@, so we can't install %@ with that same identifier.
is-purchased-redownload
Failed to write serialized MIBundleMetadata to %@
PackageInspectionFailed
Ignoring key INIntentsSupported for %@ because not all elements are strings: %@
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:]
stashedVersions
-[ICLBundlePersonaRecord isEqual:]
%@.supp
MI_Persona_BundleID_Relayering
InstallBuildVersion
com.apple.web-browser-engine.rendering
iTunesMetadata.plist captured from %@ has distributorInfo set; this is not allowed. Found distributorInfo: %@
-[MIBundleContainer initWithToken:options:error:]
Failed to malloc %zd bytes for extended attribute list for %s: %s
Interface-glance
-[MIBundleContainer initWithContainerURL:expectAppWithin:error:]
Failed to open file %s : %s
Failed to get XPC services in app %@
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_UTILITY
Unknown error: 0x%x
Failed to get iTunesMetadata from %@ : %@
B16@?0@\"MIBundleContainer\"8
com.apple.installd.validatedByFreeProfile
Did not find any placeholder entitlements in %@
Already have entry for app %@; keeping it instead of %@
i
+[MIMCMContainer defaultDirectoriesForContainerType:error:]
-[MICapabilitiesManager checkCapabilities:withOptions:error:]
DriverKit extension bundle at \"%@\" with identifier \"%@\" contains a '.' in the portion after the parent app's prefix (prefix: \"%@\" ; dot in: \"%@\").'
fApr4oevAMrl65iFf3wAhUqJIOk=
Failed to set container after fetching existing container found when making container live for %@
AppleTVSimulator
Destination %@ exists and is a directory
_HasMoreThanThisOpenFileDescriptor
/System/Library/PrivateFrameworks/AppleSauce.framework
MICopyExtensionCacheEntryWithPlatform
Failed to construct path to installd daemon container
IllegalXPCServiceServiceType
Appex bundle at %@ with id %@ has an illegal value for the CFBundlePackageType key in its Info.plist: %@
27.9999
opendir of %s failed: %s
Couldn't get installType EA from \"%s\": %s
private/var/staged_system_apps
com.apple.TrustMe
Failed to construct URLs: dataContainerURL: %@, tempURL: %@
Appex bundle at %@ with id %@ defines an EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist with a value that is not a string.
CFBundleDisplayName
DeviceFamilyNotSupported
BundleContainer can't be created for container type %llu
Unable to compute hash for executable %@
appManagementDomain
SkipThinningCheck
Failed to write %lu bytes to %s : %s
Found empty placeholder entitlements in %@
removefile of %@ failed: %s
Install type extended attribute not found on %@
Attempted to iterate directories starting at a path that was too long: %s
[%@/%@]
DTPlatformName
-[MIGlobalConfiguration OSBuildVersionWithError:]
-[MIExecutableBundle needsDataContainer]
-[ICLWorkspace bundleRecordsWithFrameworkURL:options:withError:]
-[MIExecutableBundle _discoverWatchAppBundleAsPlaceholder:error:]_block_invoke
FSIOC_FD_ONLY_OPEN_ONCE returned unexpected result %d errno %d (%s) for path %s
container_query_create_from_container() returned NULL for deserialized container object
Container
isOnDemandInstallCapable
Failed to clear staged update container attribute for identifier %@ 
appletvsimulator
-[MIRelocatedBundleContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:]
system
frameworkBundleURL parameter was not a valid URL
Key missing or invalid type when decoding MILocationUserDefinedDirectory from plist dictionary
Could not get MID-based SINF status from SINF at %@: %ld
Lacking other hints, because the root of the bundle %@ does not have only a Contents directory, assuming this is not a MacOS app
FTS returned error for %s : %s
v24@?0@\"NSSet\"8@\"NSError\"16
1.0
 on a volume with UUID [
PlaceholderFailureReason
Attempting to reserve %zu bytes of validation memory for testing
/System/Library/PrivateFrameworks/FactoryTest.framework
Couldn't set app identifier EA on \"%s\": %s
MIRecordCurrentBuildVersion
Failed to locate an attrBuf
developerName
Failed to create CFBundle for %@
com.apple.private.security.no-sandbox
-[MIFileManager setOwnershipAtURL:toUID:gid:error:]_block_invoke
_CheckRealpathHasBasePrefix
Appex bundle at %@ with id %@ does not define a NSExtensionPointName key with a string value in the NSExtensionAttributes dictionary in the NSExtension dictionary in its Info.plist
Failed to get value for key %@ on data container %@ : %@
init()
-[MIPluginDataContainer associatedBuiltInBundleURL]
Matched thinning based on defaults override %@
Failed to read ExtensionKit based app extensions for bundle %@: %@
Appex bundle at %@ with ID %@ does not have a CFBundleDisplayName key with a non-zero length string value in its Info.plist
Appex bundle at %@ with id %@ has an illegal value for the ServiceType key in the XPCService dictionary in its Info.plist
v32@?0@\"NSURL\"8@\"NSString\"16@\"NSError\"24
CFBundleGetInfoDictionary failed for bundle at %@
Failed to create SecTask from audit token for pid %d
Removing keychain access groups: %@
com.apple.private.security.system-application
CFBundleExecutable
CFBundleLocalizations
opendir of %@ failed: %s
marketplaceDomain
-[MIUserManagement clearLegacyBundleIDMappingWithError:]_block_invoke_2
SimultaneousInstallsNumber
com.apple.developer.default-data-protection-if-available
com.apple.developer.memory.transfer-send
acl_copy_ext_native returned size %zd which was more than we had allocated (%zd)
-[MIFileManager debugDescriptionForItemAtURL:]
-[MIContainer _isStagedUpdateContainer:withError:]
stagingContentType
-[MIKeychainAccessGroupTracker _onQueue_updateReferencesWithOldBundle:newBundle:error:]
MIInstallationDomainUnknown
%4d/%4d\t 0%08o\t %@
MIMachOFileIterateImageSlicesFD
macho_for_each_slice_in_fd failed for %s
InvalidiTunesMetadataPlist
Appex bundle at %@ with id %@ has an illegal value for the RunLoopType key in the XPCService dictionary in its Info.plist
Appex bundle at %@ with id %@ does not have a string value for the NSExtensionViewControllerHostClass key in the NSExtension dictionary in its Info.plist
com.apple.developer.app-management-domain
MIMachOFileMatchesMyArchitecture
Root sinf URL points outside of bundle
com.apple.MobileContainerManager.SafeHarborInfo
Container for identifier %@ is not a data container; found class %ld.
XPC!
com.apple.Preferences
CFBundleNumericVersion
_hasNoConflictWithNonContainerizedSystemApp
accountInfo
OriginalInstallDate
+[MIContainer groupContainerURLsForBundleIdentifier:forPersona:error:]
Appex bundle at %@ with id %@ specifies a value (%@) for the NSExtensionPointIdentifier key in the NSExtension dictionary in its Info.plist that does not correspond to a known extension point.
-[MIBundleContainer bestEffortRollbackiTunesMetadata:error:]
removefile hit error for %s : %s
[%@, %@]
PurchaserID
__DATA segment has too many sections in %@
%@, linkedParentBundleID=%@ linkedChildBundleIDs=%@
-[MIRelocatedBundleContainer purgeContentWithError:]
Could not get install type because bundle metadata could not be read from %@
XPCServices
Appex bundle at %@ with id %@ does not define a NSExtensionPointVersion key with a string value in the NSExtensionAttributes dictionary in the NSExtension dictionary in its Info.plist
Failed to get container URL
Could not locate bundle in stashed bundle container at %@
Failed to get app replacement state from %@ : %@
Serialized container did not encode containerURL
removefile hit error for %s but we failed to get the error number
iphoneos
Appex bundle at %@ with id %@ does not have a string value for the NSExtensionContextHostClass key in the NSExtension dictionary in its Info.plist
Siri Intents Appex bundle at %@ with id %@ defines an IntentsRestrictedWhileLocked key in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist, but that key's value is not an array of strings.
MissingBundleExecutable
CFBundleIconFiles
-[MIFileManager _traverseUntilFirstAvailableParentOfURL:withBlock:]
Couldn't stat %@: %s
libMIS returned launch warning for %@
v32@?0@\"NSString\"8@\"NSArray\"16^B24
The Info.plist at %@ is too large. Found %lld bytes on disk, but maximum allowed size is %lld bytes.
Returning cached code signing info for %@
LaunchServicesOperations
Failed to set EA named %s on \"%s\": %s
Serialized container did not encode the MobileContainerManager serialization of the container
Failed to find app bundle in container %@ : %@
v32@?0@\"NSURL\"8@\"NSUUID\"16^B24
contentDescriptors
Decoded a nil app replacement state from [
user app
secondaryGenreID
-[MIContainer markContainerAsStagedUpdateWithError:]
Failed to get installType from bundle %@ : %@
-[MIExtensionKitBundle _validateDelegateClassWithError:]
IncorrectArchitecture
SystemAppPlaceholder
Failed to retrieve system group container: %llu
Failed to remove sinf at %@ : %@
Discovered %@ app without data container %@
Failed to read placeholder entitlements file from %@
Link needed in data container because bundle was linked against SDK version 0x%08x
-[MIKeychainAccessGroupTracker _onQueue_discoverReferences]
Failed to remove app launch prohibition at [
v16@?0@\"NSError\"8
com.apple.developer.driverkit
-[MIFileManager destinationOfSymbolicLinkAtURL:error:]
com.apple.installcoordinationd
StashedAtTimestamp
-[MIAppExtensionBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
StageCreationFailed
_sinfSubPaths
Reserved %zu bytes of validation memory for testing
Applications
familyID
Entitlements
symlink
 without a source app identity to [
Failed to discover installed apps: %@
iTunesArtwork
MobileInstallationDemotionCompleteNotification
_EnumerateExtendedAttributes
/System/Library/AppPlaceholders
__LINKEDIT
IsOnDemandInstallCapable
Failed to retrieve container subdirectories for class %llu
hasMIDBasedSINF
This app has the same bundle ID (\"%@\") as a known deletable system app, but was signed with no entitlements at all and thus is missing the required entitlement \"%@\" = true (boolean).
removexattr on %s for %s failed
Error returned while calculating size under %@ : %@
Unexpectedly was not passed personas when scanning appex %@ in %@
Bundle URL missing in info for %@
-[MIGlobalConfiguration helperLogDirectory]
MultipleWatchKitTwoApps
com.apple.developer.home
Existing link is fine, leaving it there.
pthread_setugid_np failed for uid %d gid %d; error %d (%s)
-[MIFilesystemScanner _scanExtensionKitDirectory:withError:]
hasParallelPlaceholder
Appex bundle at %@ with id %@ does not define a NSExtensionAttributes key with a dictionary value in the NSExtension dictionary in its Info.plist
<%@ containerPath:%@>
Multiple file provider app extensions found in app but only one is allowed (found %@ ; already found %@)
-[MIMCMContainer dealloc]
Failed to wipe container for identifier %@
Failed to gather stashed app record info for %@ : %@
MissingBundleDisplayNameString
com.apple.CloudKit.ShareBear
Not pushing signing info to MCM because state was %lu
Siri Intents app extension is present in the WatchKit app %@ but there are no Siri Intents in the companion app %@
Could not append element \"%s\" of length %zd to path \"%s\" because it would make the path longer than MAXPATHLEN
Serialized container did not encode bundleURL for bundle in container %@
-[MITestManager _onQueue_clearIsRunningInTestModeForProcessWithPID:withError:]
com.apple.Home.HomeUIService
-[MIExecutableBundle watchKitV2AppBundleWithError:]
CFBundleShortVersionString
Found entry in subgenre array that was not a dictionary: %@
-[MIDataContainer makeSymlinkToBundleInContainerIfNeeded:]
BundleContainer
SignerIdentity
/System/Library/PrivateFrameworks/GPUSupport.framework
CFBundleVersion
-[MIBundleContainer _writeRawiTunesMetadataData:error:]
_ParseAttributeBuf
Waiting for %zu bytes to become available (%zu/%zu currently available) to validate %@
NSExtension
Failed to calculate hash on watchkit app executable for %@. Error: %@
platform-application
Could not extract signer organizations for %@
Key missing or invalid type when decoding MILocationUserDefined from plist dictionary
SupportedDevices
Unknown app bundle type: %d for %@
B16@?0r*8
\v
-[MIContainer _setContainer:error:]
Unknown container status: %lu
isInstallationHoldActive
SourceFileLine
UILaunchImageSize
IsDeletable
Couldn't set %s EA on \"%s\": %s
isFactoryInstall
AppInstallDate
-[MIExecutableBundle _dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]
+[MIBundleContainer purgeTransientBundleContainersWithError:]
CompanionPlaceholderCaptureFailed
developerID
-[MIStoreMetadataDistributor initWithDictionary:]
SYS_initgroups failed; error %d (%s)
Failed to allocate a continuation!
Install session ID requested for bundle that was not an app or app extension: %@
placeholderFailureReason
MIInstallationDomainDefault
com.apple.PhotosViewService
iphonesimulator
Could not load profile at path %@
Failed to get metadata from %@ : %@
Data length is more than 4 KB for extended attribute key %s: length is %zd bytes
parentIdentifiers
AlternateIconName
Calculating keychain group references took %.02f seconds
AppexBundleIllegalExtensionPointNameString
Ignoring Watch app at %@ because it's not compatible with a known watchOS version
Code signing identifier (%@) does not match bundle identifier (%@) for %@
keychain-access-groups
HOME
IsUpdatedSystemApp
Header magic indicates non-native-endian slice; that's not allowed.
read failed for %s, got %lld bytes
gameCenterEverEnabled
v24@?0@\"NSDictionary\"8@\"NSError\"16
nil url passed to -removeItemAtURL:error:
Failed to get keychain access groups in XPC service %@
Media/ApplicationArchives
_DataForEAKey
Already have an entry in hashes dictionary for key %@
Failed to read SAFE_HARBOR_CONTAINER_ATTRIBUTE_KEY with %@
+[MIContainer enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:]_block_invoke
%@, associatedPersonas=%@
HasParallelPlaceholder
PersonaBundleIDMigration
alternateIconName
YES
MacOSX
-[MIFilesystemScanner _scanFrameworkDirectory:withError:]_block_invoke
Failed to verify code signature of %@ : 0x%08x (%@)
Found subgenre dictionary that did not contain both required '%@' and '%@' keys: %@
Could not stat %s: %s
UIAppFonts
com.apple.developer.wifi-infrastructure
watchKitAppExecutableHash
SignerOrganization
app extension
-[MIMCMContainer setDataProtectionClass:forSecondOrThirdPartyApp:error:]
-[MIExecutableBundle executableImageSlicesWithError:]
Found WatchKit 2.0 app at %@ but it does not have a WKWatchKitApp or WKApplication key set to true in its Info.plist
-[MIAppExtensionBundle _updateInfoForContainerSet:newlyCreated:error:]
Failed to resolve staging root for unknown staging content type
Failed to determine if we're running in test mode : %@
Attempted to set a zero-length or nil app identifier on \"%s\"
-[MIFileManager deviceForURLOrFirstAvailableParent:error:]_block_invoke
+[MILaunchServicesDatabaseGatherer enumerateAppExtensionsInBundle:forPersonas:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:]
DSPersonID
Recorded current system version as %@ (%@)
WKCompanionAppBundleIdentifier
com.apple.fileprovider-nonui
-[MIExecutableBundle _codeSigningInfoFromMCM]
Validating as built-in: %@
_CallBlockForBaseItem
Failed to delete partially created container %@ : %@
-[MIContainer setInfoValue:forKey:error:]
com.apple.MobileContainerManager.StagedUpdateContainer
hasIdentifiedBundle
InstallCoordination
-[MIAppIdentity _doInitWithBundleID:personaUniqueString:location:]
-[MIExecutableBundle bestEffortRollbackSinfData:]
com.apple.installd.appclip
-[MIStagingRootAbsolute resolveRootWithError:]_block_invoke
VuGdqp8UBpi9vPWHlPluVQ
Expected non-NULL extensionHandle for %@
firstBytes=%@ 
Testing
Failed to find executable bundle in container %@ : %@
-[MIFileManager validateSymlinksInURLDoNotEscapeURL:error:]_block_invoke
-[MICodeSigningVerifier performValidationWithError:]
Scanned %lu apps in %@
com.apple.private.security.container-required
/private/
Failed to make app extension %@ executable: %@
StoreKit
Failed to clone existing container item at path %@ to stash path %@
Data for key %s returned length 0, expected length %zd
deviceBasedVPP
Messages stub apps may only have a single message payload provider app extension, but this stub app has an extension %@ of type %@
FamilyID
Failed to get container URL from %@
RoleUserMigration.plist
%@ is not expected to contain watch app executables
Unknown Process Name
Appex bundle at %@ with id %@ defines an EXPrincipalClass key in the EXAppExtensionAttributes dictionary in its Info.plist with a value that is not a string.
-[MITestManager _onQueue_setIsRunningInTestModeForProcessWithPID:withError:]_block_invoke
Failed to clear test mode %@ when %d exited
Failed to create sinf directory at %@ : %@
Failed to find a candidate buffer to scavenge!
Removed safe harbor attribute for %@ at %@
AppexBundleIllegalExtensionContextHostClass
-[ICLHelperServiceClient _remoteObjectProxyWithErrorHandler:]
WatchKit 2 app extension's NSExtension.NSExtensionAttributes dictionary is not present. It must contain a WKAppBundleIdentifier key set to the WatchKit app's bundle ID.
_InstallProvisioningProfile
dylib
-[MIBundleContainer compatibilityLinkDestination]
Failed to lchmod %s : %s
MIMCMContainer's superclass -init returned a nil self
-[MIExecutableBundle checkExecutableExistsIfRequiredWithError:]
skipping mount point or trigger at %s/%s
com.apple.MobileInstallation.SystemOrAnyPersonaExtensionMarker
(%@|%@)
com.apple.itunesstored
-[MIExecutableBundle setSinfDataType:withError:]
IsEligibleForWatchAppInstall
-[MISystemAppState _onQueue_retrieveSystemAppStateRestoringBackedUpState:]
Failed to get installation identity for %@ : %@
-[MIExecutableBundle validatePluginKitMetadataWithError:]
@\"NSError\"24@?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16
Could not get ACL for file %@: %s
LaunchWarningData
com.apple.MapsExternalComponents
MobileInstallation
Discovered app extension without data containers %@
-[MIFileManager secureRenameFromSourceURL:toDestinationURL:destinationStatus:error:]
com.apple.iOS6Updater
Unknown value for DataProtectionClass entitlement: %@; defaulting to class %d
%@.supf
xattr named %s not present on \"%s\"
-[ICLWorkspace diskUsageForLaunchServicesWithBundleIDs:options:withError:]
Unable to check if %@ with bundle identifier %@ is already installed.
-[MIContainer removeUnderlyingContainerWaitingForDeletion:error:]
-[MIInstalledInfoGatherer bundleRecordWithError:]
Unknown MIAppReplacementStatus: %lu
com.apple.installd.installType
InvalidStubExecutable
IsWebNotificationBundle
/var/
Platform %@ (%u) does not have a simulator equivalent; returning PLATFORM_UNKNOWN
Expected '%@' element to have a string value for '%@'.
OS Module app
-[MIExecutableBundle estimatedMemoryUsageToValidate]
PlaceholderEntitlements.plist
Could't set placeholder EA on \"%s\": %s
Failed to write serialized app replacement state to [
Failed to read bundle metadata from %@
SupportsAppMigration
-[MIMCMContainer replaceExistingContainer:error:]
Current build version (%@ / %@) equal to last version recorded (%@ / %@); skipping upgrade
MISetSinfDataType
-[MIInstallationIdentity writeToBundle:error:]
Setting test flags 0x%llx (0x%llx -> 0x%llx)
IntentsAppexIntentsSupportedNotASubset
ApplicationMoveFailed
<%@: dataContainerURL: %@ groupContainerURLs: %@ environmentVariables: %@>
-[MIBundleContainer transferExistingStashesFromContainer:error:]
-[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:]
MIAppReplacementStatusNotApplicable
Failed to get code signing info for %@: %llu
Could not extract dictionary from %@: %@
Failed to sanitize destination file path %@
InstalledContentLibrary.MIAppReplacementState
system app
Failed to get Info.plist path
-[MIDaemonConfiguration daemonUserDataLibraryDirectory]
ServiceType
-[MIDataProtectionChangeOperation _runChangeOperationWasLocked:withError:]_block_invoke
subgenre
clonefile failed for %s to %s: %s
-[MIFileManager createSymbolicLinkAtURL:withDestinationURL:error:]
-[MIFileManager volumeUUIDForURL:error:]
_PopulateAttrBuf
bundleShortVersion
AppexBundleIDNotPrefixed
Unable to find class %s
No SinfReplicationPaths array in manifest %@
SinfReplicationPaths key value in manifest %@ was not an array
SC_Info
ValidatedByUPP
Failed to get CFBundleIdentifier from bundle %@
-[MIExecutableBundle updateMCMWithCodeSigningInfoAsAdvanceCopy:withError:]
Allowing possibly ad-hoc signed binary at path %@ because we're running in test mode
(container_error_copy_unlocalized_description returned NULL)
com.apple.intents-ui-service
groupContainerURLs
-[MIBundleContainer _bundleExtensionForContainerClassWithError:]
-[ICLHelperServiceClient stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:]_block_invoke
MIReleaseSandboxExtensionHandle
com.apple.MobileContainerManager.PlaceholderEntitlements
-[MIExecutableBundle updateAndValidateSinf:withRollback:error:]
purchaserID
%@ was grandfathered but has seatbelt-profiles entitlement
com.apple.developer.web-browser-engine.host
-[MIMCMContainer setInfoValue:forKey:error:]
-[MIMCMContainer supersedeExistingContainer:error:]
-[MITestManager _onQueue_setTestFlags:]
Could not get extended attribute list for %s: %s
-[ICLHelperServiceClient resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:]_block_invoke
fgetattrlist for %s failed: %s
MIGetSinfDataType
-[ICLPlaceholderRecord isEqual:]
Built in framework is expectedly missing its bundle executable.
-[MIFileManager _stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:]
statfs failed for %@: %s
Rejecting %@ -> %s, as absolute symlinks are not allowed
true
com.apple.developer.web-browser-engine.rendering
Failed to save stash metadata
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_USER_INITIATED
RequireEligibilityForInDevelopmentApps
Failed to get sandbox extension for installd's daemon container
Fetch framework info at %@ requested with options %@
-[MIExecutableBundle watchKitVersionWithError:]
MI_Full_Fidelity_Icons
Not allowed to mark placeholder as validatedByFreeProfile for %@
<%@<%p> dateStashed=%@ dateOriginallyInstalled=%@>
<%@ container=%@ persona=%@ path=%@>
-[ICLAppRecord isEqual:]
iTunesMetadata.plist
/tmp
Failed to discover personas for built-in app %@ : %@
MIUninstallProfilesForAppIdentifier_block_invoke
Manifest.plist
Returning previously obtained code signing info for %@
Could not create bundle for WatchKit app at %@
UIDeviceFamily
/System/Library/Frameworks/CoreGraphics.framework
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_USER_INTERACTIVE
There is nothing to be replaced
CoreServices
MIMachOSimPlatformForPlatform
Failed to write serialized app launch prohibition to [
location
com.apple.private.pluginkit.persona
GroupContainers
-[MIFileManager standardizeOwnershipAtURL:toUID:GID:removeACLs:setProtectionClass:foundSymlink:error:]_block_invoke
com.apple.TestFlight
hasSettingsBundle
LSUpgradeInstallConsent
protectedMetadata
_IsDictionaryWithKeyStringAndValueArrayOfString
Failed to save bundle URL on plugin data container %@: %@
+[MIBundleMetadata metadataFromURL:error:]
Failed to create MIExecutableBundle instance for %@ : %@
SkipDeviceFamilyCheck
app identity has nil bundle identifier
com.apple.mobilesms.compose
installType
Posted downgrade notification with userInfo %@
Value of key %@ on %@ was not a number
false
Failed to set mode to 0%o for %s : %s
options parameter was not a dictionary
%@ was grandfathered but has container required entitlement
Validating sinf for %@
Appex bundle at %@ with ID %@ has a CFBundleShortVersionString key with a non-string value in its Info.plist
Can't figure out set for app type %@
is-auto-download
#)
Error getting disk usage for %@ (%ld): %@
-[ICLWorkspace getAppReplacementState:forBundleContainerURL:error:]
Unexpected staging mode: %d
Executable stub at %@ had unexpected signing identifier '%@'; expected %@.
Class getUMUserManagerClass(void)_block_invoke
-[MIContainer clearStagedUpdateContainerStatusWithError:]
com.apple.MobileContainerManager.Entitlements
CLKComplicationPrincipalClass
Removing orphaned transient bundle container %@
Failed to stat %s : %s
_WatchKitStub/WK
Failed to read manifest at %@ : %@
DriverKit
downloaderDSID
7.0
MismatchedCapabilities
-[MIAppExtensionBundle extensionCacheEntryWithError:]
SinfReplicationPaths array contains values other than strings; ignoring manifest at %@
Locally signed apps are unrestricted because boot-args are set
Found zero associated personas for app %@; assuming primary persona
failed to stat %s : %s
MismatchedBundleIDSigningIdentifier
WatchOS
AppexBundleMissingClassOrStoryboard
copyfile failed for %s to %s: %s
accountID
com.apple.MobileInstallation.bundleURL
-[MIKeychainAccessGroupTracker _onQueue_addReferencesForBundle:error:]
Failed to locate system persona: UserManagement returned %lu personas but none of them had isSystemPersona = YES
Failed to scan content: %@
com.apple.developer.swift-playgrounds-app
com.apple.accessory-transport-extension
keySample={ 
isAutoDownload
Failed to discover code signing info for app: %@
This bundle does not have an executable, so executable image slices are not available.
SupportedDeviceFamilies
-[MIFileManager setInstallType:inExtendedAttributeOnBundle:error:]
Scanned %lu items in ExtensionKit extensions dir %@
amfi_interface_query_bootarg_state returned error %s
Failed to verify code signature for this internal, disk image, or core services app, %@. Because of that, we don't have entitlements or signing info so we'll assume that it does NOT require a container.
BundleIDConflictWithOtherIdentifier
v16@?0@\"ICLAppExtensionRecord\"8
Setting simultaneous installations allowed to %ld
serializedPlaceholderURL
com.apple.security.system-container
Failed to get the real path of /var
v24@?0@\"NSString\"8@\"ICLBundleRecord\"16
sideLoadedDeviceBasedVPP
stat of %@ failed: %s
categories is not an array of strings: %@
MILoadFilteredPlist
_MICommonCopyGroupEntitlement
Session ID provided, %@, wasn't of expected length %zu
xros
Rejecting %@ with base %@ (reals %@ ; %@) because components diverge at %@ != %@
This platform does not support location type 
Object returned from _CFBundleCreateFilteredInfoPlist was not a dictionary, was type %@
Failed to discover bundles in directory %@
Failed to create URL for internal superseded app additions plist.
CFBundleInfoDictionaryVersion
hasMessagesExtension
The persona unique string %@ does not correspond to any known persona on this system.
MILoadInfoPlistFromBundleWithError
Library
No extended attributes found on %s
app identity has nil location
PercentComplete
Failed to decode bundle metadata from %@
Derived profile validation type %lu does not match the corresponding code signer type %lu
_OSModuleApplicationsDirectories
ThinnedAppVariantID
placeholderFailureUnderlyingErrorSource
PrincipalClass
Did not validate all slice hashes on executable %@; unchecked hashes: %@
MIRemoveSinf
FakeCodeSigningNotDisabled
Failed to read iTunesMetadata from %@ : %@
interactive
Failed to read %@. Error: %@
ExecutableTwiddleFailed
DTPlatformBuild
Appex bundle at %@ with ID %@ does not have a CFBundleName key with a non-zero length string value in its Info.plist
Could not find installed app with identifier %@ in domain %lu
Non transient container can't be marked as a staged container
Failed to create connection to %@
-[MIAppExtensionBundle associatedPersonasUsingParentPersona:error:]
com.apple.MobileInstallation.ContentProtectionClass
Failed to create symlink at path %@ to %@ : %@
DriverKitExtensionPaths
Failed to set ACL on dir %s: %s
copyfile failed at %d while copying %s to %s: %s (%d)
Failed to save content protection class value on data container %@ : %@
open_dprotected_np failed for %s for class %d : %s
Failed to validate binary at %@: %@. This binary may not work properly.
-[MIExecutableBundle watchKitPluginWithError:]
com.apple.developer.associated-appclip-app-identifiers
.
File %s is multiply linked; cloning
AltDSID
BuildVersion
identifier
Failed to clear staged update container status for %@ after making it live : %@
[f]getxattr failed to get length for xattr named %s path %s fd %d
-[MIMCMContainer reclaimDiskSpaceWithError:]
-[MIRelocatedBundleContainer regenerateDirectoryUUIDWithError:]
systemgroup.com.apple.mobile.installationhelperlogs
Entitlement %@ does not contain supported types; ignoring.
-[MILaunchServicesDatabaseGatherer initWithOptions:personaUniqueStringForBundles:enumerator:]
Failed to retrieve any shared data containers for %@
The value of the UISupportedDevices key in this app's Info.plist key must contain only string values.
%@
-[MIPluginKitBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
NSExtensionAttributes
AppexBundleUnexpectedSwiftSectionInExecutable
DeviceOSVersionTooLow
iTunesArtworkCaptureFailed
Failed to retrieve depth of %@
Failed to get info dictionary from MISValidateSignatureAndCopyInfo when verifying %@
__watchkit
-[MIDataContainer supersedeExistingContainer:error:]
Client-provided persona %@ is not among available personas on the system.
-[MIUserManagement personasAreKnownForUniqueStrings:error:]_block_invoke
Failed to create URL for migration info file.
Failed to refresh persona information during init: %@
lstat of %@ failed
Failed to get keychain access groups for new bundle %@
[FAIL] 
dataContainerURL
_DiscoverPersonas
ratingRank
App with id %@ is not in the core services app map even though it's type core services
CFBundleSignature
+[MICodeSigningVerifier _validateBundleExecutable:againstStubAt:trustedHashes:sectionName:signingIdentifier:error:]
-[MIContainer purgeContentWithError:]
AppexBundleUnreadableExecutable
Failed to destroy aborted temp container for app %@ : %@
linkedParentBundleID
Underlying errno set by container manager is %s
IsAdHocSigned
%@ was grandfathered but has no-container entitlement
DTPlatformVersion
-[MIBundleContainer _stashedBundleContainerForIndex:error:]
MILocationSystemDefinedCommon
Embedded watch apps don't get reported to Launch Services: %@
embedded.mobileprovision
Attr named %s not present on %@
App extension with identifier %@ already located; keeping that instead of new one found at %@
Failed to write sinf to %@ : %@
WatchKitAppExtensionAttributesInvalidAppBundleID
-[ICLWorkspace enumerateBuiltInSystemContentWithBlock:error:]
mobile
MIRestoreAvailableMemoryForValidationAfterTesting
bundleURL
%@ is in the deny list
/System/Cryptexes/OS/
Failed to chmod %s : %s
No WatchKit 2.0 app bundle or placeholder found for app %@
Failed to get the real path of /tmp
read failed for %s : %s
redownload-params
Failed to serialize app launch prohibition [
relativeStagingBaseDirectory
EXExtensionPointCatalog
Class getEXExtensionPointCatalogClass(void)_block_invoke
purchasedRedownload
getattrlistbulk failed on entry %u in %s : %s
Failed to create container for %@
Failed to make safe harbor container live %@
utility
user
-[MIDataProtectionChangeOperation _runChangeOperationWasLocked:withError:]
-[MIExecutableBundle setLaunchWarningData:withError:]
CFBundleName
Failed to get existing container when replacement found the live container was already present for %@
com.apple.developer.embedded-web-browser-engine
isB2BCustomApp
InstalledContentLibrary.MILocationSystemDefinedCommon
softlink:o:path:/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
softlink:r:path:/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
[FAIL] Done scanning bundle at %@
%s: container_copy_sandbox_token returned NULL!
%s: Expected non-NULL extensionHandle for %@
Done scanning plugins in bundle at %@
MarkDriverKitExtensionsExecutable
ScanBundle
Done scanning framework at %@
getpwnam_r failed for user %s : %s
getpwnam_r succeeded but no user was found with name %s
pthread_setugid_np failed to restore root privs from %u/%u; error %d (%s); aborting because this thread is in a bad state.
Got validation memory usage of %zu bytes which is greater than our available memory of %zu bytes (while validating %@); hoping for the best
[FAIL] Done scanning plugins in bundle at %@
[FAIL] Done marking DriverKit extensions in bundle as executable at %@
%s: Attempting to restore an identity without having first assumed an identity
Got memory size to return, %zu, which would result in %zu available, which is more than the maximum of %zu bytes; capping at max available
%s: Unexpectedly got nil persona for %@
Generating ICL bundle record for %@
GenerateDict
Done marking DriverKit extensions in bundle as executable at %@
Failed to get installcoordinationd daemon container: %@
Failed to get home dir path size: %s
Expected at least %zu bytes of memory for validation but found %zu bytes
Expected headroom in installd (%zu) must be less than expected jetsam limit (%zu) in installd
Unexpectedly called base class implementation of %s
%s: Attempt to clone %s to %s failed with EXDEV; falling back to copyfile
ScanPlugins
%s: Attempting to assume an identity of 0/0, which should be the default for the helper service
%s: Failed to release sandbox token %lld for %@ : %s
%@Done generating ICL bundle record for %@
Mark DriverKit extensions in bundle as executable at %@
Done scanning bundle at %@
Failed to get installd daemon container: %@
%s: Failed to release sandbox token %lld for container %@
%s: Expected to move %s to %s but got EXDEV; falling back to copyfile
Scanning bundle at %@
Scanning framework at %@
[FAIL] Done scanning framework at %@
Got memory size to return %zu which is greater than our available memory of %zu bytes; capping at max available
%s: Platform %@ (%u) does not have a simulator equivalent; returning PLATFORM_UNKNOWN
Scanning plugins in bundle at %@
MIStagingRootAbsolute
MIPersonaAssociationLocalResolver
MILocationSystemDefinedCommon
MIStashMetadata
MIAppIdentityPersonaResolver
MIMCMContainer
MIDataProtectionChangeOperation
ICLWorkspace
MICapabilitiesManager
MIStoreMetadataSubGenre
MIPersonaAssociation
ICLAppExtensionRecord
MIInstallationIdentity
ICLBundlePersonaRecord
MIGlobalConfiguration
MICodeSigningVerifier
MIAppReplacementState
MobileInstallationAdditions
ICLFrameworkRecord
MIEmbeddedWatchBundle
MIFilesystemScannerDelegate
MISystemAppState
MIDaemonConfiguration
ICLSystemAppPlaceholderRecord
ICLRegistrationOptions
MIAppLaunchProhibition
MILocationUserDefined
MobileInstallationHelperServiceProtocol
MIUserManagement
MISignatureAgnosticHasher
MIAppIdentity
MIRelocatedBundleContainer
MIGroupContainer
MILocationSystemDefinedBase
MIBundleMetadata
MICodeSigningInfo
NSObject
MITestManager
MIExecutableBundle
MIFileManager
MIStoreMetadataContentDescriptor
MIStoreMetadataDistributor
MIPluginDataContainer
MIContainer
NSFastEnumeration
MIInstalledInfoGatherer
ICLStashedAppRecord
MIPersonaContainerSet
MIBundleMetadataProvider
MIStoreMetadata
MIPluginKitBundle
MobileInstallerDelegateProtocol
MobileInstallerProtocol
ICLInstallationDaemonClient
MIMachOImageSlice
NSSecureCoding
MILocation
MIUserManagementDaemonContainerResolver
MIStagingRootVolumeUUID
MIContainerQueryResult
ICLFeatureFlags
MIPersonaAttributes
MIDriverKitBundle
MIBundleContainerToken
ICLSinfInfo
ICLBundleRecord
NSCoding
MILocationUserDefinedDirectory
InstalledContentLibrary
NSCopying
ICLPlaceholderRecord
MIBundle
MIKeychainAccessGroupTracker
ICLAppRecord
MIExtensionKitBundle
MIFileManagerCopyfileContext
MILaunchServicesDatabaseGatherer
ICLUninstallRecord
MIStashedBundleContainer
MIStagingRootProtocol
MIFilesystemScanner
MIContainerToken
MIBundleContainer
MIDataContainer
MIStagingLocation
MIAppExtensionBundle
ICLHelperServiceClient
MILocationProtocol
serializeToURL:error:
setExecutableImageSlices:
_scanBundleContainersWithClass:withError:ignoredErrorOccurredOnOneOrMoreItems:
initWithTargetUID:
setInfoValue:forKey:error:
_parentIdentifiers
bundleForURL:error:
raiseExceptionWithCompletion:
setMarketplaceItemID:
unknownArchNameStringForArchName:
T@\"NSString\",C,N,V_enterpriseInstallURL
allowDeletableSystemApps
installTypeFromExtendedAttributeOnBundle:error:
setContainerURL:
transientBundleCleanupEnabled
_frameworks
_scanExtensionKitLocations:withError:
getBytes:length:
serializedPlaceholderURL
MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:
TB,N,V_verifyTrustCachePresence
_populateBundleRecordValues:signingInfo:error:
setSerializedPlaceholderURL:
stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:completion:
status
T@\"NSSet\",R,C,N,V_systemAppPlaceholderAppExtensionBundleIDs
.cxx_destruct
developerID
fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
iAdConversionDate
isInstallationHoldActive
_personaUniqueStringForBundles
enumerateDylibsWithBlock:
makeSymlinkFromAppDataContainerToBundleForIdentifier:forPersona:completion:
setDeveloperName:
xpcServiceBundlesWithError:
T@\"NSDictionary\",C,N,V_personasRecordMap
T@\"NSString\",C,N,V_identifier
fileURLWithPath:isDirectory:relativeToURL:
setOwnerOfURL:toUID:gid:error:
volumeUUIDForLocation:error:
T@\"NSCountedSet\",&,N,V_refs
T@\"NSString\",C,N,V_iAdAttribution
T@\"NSString\",C,N,V_shortItemName
_doInitWithBundleID:personaUniqueString:location:
_markDriverKitExtensionsExecutableInBundle:withError:
containerForPersona:
fileURLWithPathComponents:
setExtensionOwnerBundleID:
Ti,N,V_cpuType
_wk2AppBundleError
betaExternalVersionIdentifier
dataWithContentsOfURL:options:error:
initInternal
setPersonaGenerationIdentifier:
_bundleIDMapForBundlesInDirectory:withExtension:
frameworks
validateWatchKitV2StubExecutableBundle:error:
release
T@\"NSString\",C,N,V_betaBuildGroupID
installsAppleAppExtensionsNotInExtensionCache
setRelativeStagingBaseDirectory:
TB,R,N,V_allowDeletableSystemApps
_options
containersForBundleIdentifier:contentClass:forPersona:create:fetchTransient:created:error:
encodedData
itemID
T@\"NSArray\",C,N,V_driverKitExtensionURLs
isEqualWithLocationSystemDefinedCommon:
setPlatform:
setSourceApp:
signerOrganization
T@\"NSString\",C,N,V_bundleShortVersionString
_distributorInfo
_validateBundleExecutable:againstStubAt:trustedHashes:sectionName:signingIdentifier:error:
appInfoForBundleID:onAttachedEntityType:
relativePath
sectionName
setPerformOnlineAuthorization:
setSubGenres:
roleUserMigrationMarkerFilePath
setPermissionsForURL:toMode:error:
TB,N,V_isDeletable
_synchronousRemoteObjectProxyWithErrorHandler:
dictionaryWithObjects:forKeys:count:
updateSinfForIXWithIdentifier:withOptions:sinfData:completion:
_downloaderDSID
absoluteURL
appBundleContainerWithIdentifier:forPersona:createIfNeeded:created:error:
currentUserLaunchServicesOperationStorageBaseURL
initialODRSize
setData:forExtendedAttributeNamed:onFD:fdLocation:error:
setKind:
setWithArray:
autorelease
fileHandleForReadingFromURL:error:
initWithBundleInContainer:withExtension:error:
stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:
unsignedIntegerValue
_codeSigningEnforcementIsDisabled
```
