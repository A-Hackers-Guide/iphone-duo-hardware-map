# `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

From the upgrade restore ramdisk (141-29011-104.dmg). 539,536 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 4488)
Flags         = NoUndefs, DyldLink, TwoLevel, AppExtensionSafe
```

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary (compatibility version 0.0.0, current version 0.0.0, reexport)`
- `/System/Library/PrivateFrameworks/Bom.framework/Bom (compatibility version 2.0.0, current version 195.0.0)`
- `/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation (compatibility version 1.0.0, current version 793.1.10, weak)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (11 classes, 6 protocols)

Classes: `AITransactionLog`, `MIAppReference`, `MIBOMWrapper`, `MICandidateAppContainer`, `MICandidateContainer`, `MIHelperServiceFrameworkClient`, `MIInstallOptions`, `MIInstallerClient`, `MIPlaceholderConstructor`, `MIStagedUpdateMetadata`, `NSData`

Protocols: `MobileInstallationHelperServiceProtocol`, `MobileInstallerDelegateProtocol`, `MobileInstallerProtocol`, `NSCoding`, `NSCopying`, `NSSecureCoding`

## Strings (1,298)

```
ApplicationSINFDataType
%d%@1
Failed to remove %s : %s
Failed to clean up temp offloaded bundle at %@ : %@
APIInternalError
Failed to write Info.plist file to %@
Not including icon content because IFCaptureIconContent is not available
extractPKZip
-[MIHelperServiceFrameworkClient purgeInstallCoordinationPromiseStagingDirectoryForUUID:keepStagingDirectory:error:]
provisioningProfileInstallFailureIsFatal
Bundle
Staged Update Placeholder
removefile for %s failed
_CopySafeHarborsForContainerClass_block_invoke
Start (Asynch)
-[MIInstallOptions initWithLegacyOptionsDictionary:]
v36@?0B8@\"NSArray\"12@\"LSRecordPromise\"20@\"NSError\"28
%@
Got error while enumerating CONTAINER_CLASS_INTERNAL_DAEMON_DATA looking for the %@ container: %@
Failed to locate app bundle in container with identifier %@ at %@
Attempting to offload %@ at %@
-[MIInstallerClient _invalidateObject]
com.apple.developer.browser.app-installation
Transaction log must be initialized before use. Please call +[AITransactionLog initializeWithLog:].
[uuid:%@ identity:%@ domain:%lu uid:%u]
Install (Patch Update)
iTunesMetadata
Uninstall (Application)
com.apple.install_uuid
-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:]
keychain-access-groups
immutable_open
stashMode
PackageType
Destruction
MobileInstallationUpdateiTunesMetadataForInstallCoordination_block_invoke
com.apple.mock.Playgrounds
ErrorDetail
v32@?0@8@16^B24
Unable to set F_SINGLE_WRITER on %s %s
-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:error:]_block_invoke
Library
Skipping offload of network extension app %@ at %@
MissingPackagePath
MobileInstallationSetAppLaunchState called on unsupported OS for %@
Could not extract archive
-[MIHelperServiceFrameworkClient _remoteObjectProxyWithErrorHandler:]
-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:]_block_invoke
Failed to read iTunesMetadata for app with identifier %@ from %@ : %@
-[MIInstallerClient init]_block_invoke_2
Not all delegate messages received: %@
Failed to set test mode: %@
MobileInstallationRegisterContentsOnOSModuleAtURL_block_invoke
@a
PersonaUniqueStringForInstall
-[MIHelperServiceFrameworkClient setTestingEnabled:error:]_block_invoke
MobileInstallationInstallParallelPlaceholderForStagedUpdate
Info.plist
Enumerating containers of class %llu returned error %@
-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_3
MobileInstallationMakeStagedUpdateLiveForIdentifier
MobileInstallationRemoveSafeHarborForContainerClassWithIdentity
com.apple.developer.driverkit
_PathForContainerClass
B24@?0^{?=QqQ*Q*QIIIIIIISBC}8^B16
Updating key %@ in DataMigration's prefs from %@ to %@ to force migration
com.apple.private.mobileinstall.xpc-services-enabled
referenceUUID
com.apple.
GeoJSON
Uninstall (User Data Only)
[%@/%llu]
Returned error %@
MobileInstallationAppLaunchEnabled
-[MIPlaceholderConstructor _transferAndUpdateInstallSessionIDsToPlaceholder:error:]
-[MIHelperServiceFrameworkClient allStagingLocationsWithinSubsystem:error:]_block_invoke
Start
Failed to create destination lproj directory at \"%@\"
Encountered error while enumerating %@ to copy strings
bom_fatal_error_handler
com.apple.developer.web-browser-engine.networking
Q
-[MIPlaceholderConstructor _writeIconToPlaceholder:infoPlistIconContent:error:]
userInitiated
tmp
-[MIInstallerClient uninstallIdentifiers:withOptions:completion:]_block_invoke_3
-[MIHelperServiceFrameworkClient stagingLocationForUserContentWithinSubsystem:error:]_block_invoke
MIIsValidPersonaLifecycleEventType
_CopySafeHarborsForContainerClass
Property %s did not match
MobileInstallationUnregisterContentsForDiskImageAtURL_block_invoke
WKWatchOnly
%d: %@ (%@:%ld %@)
iTunesArtwork
Error
MIGetBooleanEntitlement
%s : %s
Failed to create copier
Ignoring non-existent purge directory: %@
_AppContainsNetworkExtension
true
v8@?0
ApplicationSINF
_ProcessDataContainer
com.apple.private.mobileinstall.upgrade-enabled
-[MIPlaceholderConstructor _writeInfoPlistToPlaceholder:substitutingIconContent:withError:]
MobileInstallationCheckCapabilitiesMatch_block_invoke
Install (Parallel Placeholder)
-[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:]
-[MIHelperServiceFrameworkClient removeMacAppWithBundleID:atURL:error:]
Got post-traversal for directory %s
Preferences
Failed to enumerate %@ : %@
MobileInstallationUpdateSinfDataForInstallCoordination_block_invoke
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:]
_PurgeExpendableDataContainerContent
Client ignored error %@
DataProtectionClass
mobile
Entitlement %@ contains non-string values; ignoring.
installIntent
WaitForStorageDeletion
LSInstallType
application-identifier
com.apple.developer.superseded-application-identifiers
-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]_block_invoke
Failed to write updated migration prefs to %@ : %@
+[MIAppReference validateAppReference:withError:]
Bundle at %@ has no icon
App with identifier %@ at %@ has sideLoadedDeviceBasedVPP = YES in its metadata so it's not restorable
MobileInstallationCopyDiskUsageForLaunchServices
com.apple.private.webkit.pushbundle
Install (Demote To Placeholder)
Failed to remove migration prefs file at %@ : %@
Attempting to offload user apps...
com.apple.developer.on-demand-install-capable
com.apple.developer.embedded-web-browser-engine
com.apple.developer.home
-[MIPlaceholderConstructor _initWithSource:byPreservingFullInfoPlist:forBundleType:error:]
MobileInstallationCancelUpdateForStagedIdentifiersWithError
_
%d: %@
Unknown
MobileInstallationCopyInstalledDeveloperAppsForLaunchServices
identity
PlaceholderBundleTypePlugInKit
com.apple.MobileInstallationHelperService
v12@?0i8
data-protection-class
-[MIPlaceholderConstructor materializeIntoBundleDirectory:error:]
MobileInstallationCopyAppInfoForLaunchServicesWithWrapperURL
MobileInstallationRemoveSafeHarborForContainerClassWithIdentity_block_invoke
com.apple.AppClips
couldn't allocate a string
The options parameter is currently unused and must be nil
The provided placeholder type of %@ does not match the path extension for the bundle at %@
-[MIPlaceholderConstructor _copyStringsToPlaceholder:onlyDirectories:error:]
Placeholder for %@ used %lld bytes, but removing the app freed only %lld bytes
Developer
iTunesArtworkData
_RemovefileErrorCallback
SecCodeCopySigningInformation for %@ returned error %d
systemAppInstall
Offloading Apple apps...
App with identifier %@ at %@ does not have an itemID in its metadata so it's not restorable
Got unexpected error: %@
-[MIInstallerClient setTestMode:]
MIAcquireReferenceForInstalledAppWithError
com.apple.private.rating-rank-eligibility-domain
PreservePlaceholderAsParallel
Intent
Customer
Swallowing caught exception: %@
com.apple.developer.web-browser
fsync failed for %s : %s (%d)
Failed to capture icon content for placeholder from bundle at %@ : %@
PlaceholderBundleTypeApp
Attempting purge of mobile user's data containers' tmp and Library/Caches directories
Archive at %@ contains a total of %llu files which account for a total of %llu uncompressed bytes
-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:]
Found network extension %@ in app %@
PlaceholderEntitlements.plist
fstat failed for %s : %s
+[MIBOMWrapper extractZipArchiveAtURL:toURL:withError:extractionProgressBlock:]
Freed %lld bytes by removing %s
-[MIInstallerClient getTestModeEnabled:outError:]
com.apple.lsd
renamex_np failed to swap placeholder at %@ with live app %@ : %s
MobileInstallationUpdateiTunesMetadataForInstallCoordinationWithWrapperURL
Failed to issue write barrier for %s : %s (%d)
MIEnumerateContainersOfClass_block_invoke
MinimumOSVersion
App with identifier %@ at %@ is missing the altDSID in its metadata so it's not restorable
MobileInstallationUpdateSinfDataForInstallCoordinationWithWrapperURL
beta-reports-active
allowLocalProvisioned
Got error while enumerating CONTAINER_CLASS_SYSTEM_DATA looking for the %@ container: %@
Skipping offload of LSApplicationLaunchProhibited app %@ at %@
_MICommonCopyGroupEntitlement
ProvisioningProfiles
AutoInstallWatchApp
MobileInstallationStageApplicationUpdate
(container_error_copy_unlocalized_description returned NULL)
Removed LaunchServices database to force rebuild
Could not create error response dictionary
com.apple.developer.marketplace.app-installation
MCMMetadataIdentifier
Reached goal of %lld bytes after freeing %lld bytes
Failed to enumerate app bundle containers: %@
Skipping offload of TestFlight app %@ at %@
MobileInstallationUnregisterContentsOnOSModuleAtURL_block_invoke
MobileInstallationCopySafeHarborsForContainerClass
InternalDaemon
System
_ShouldContinueAfterIncrementingFreed
Failed to set owner for %s : %s
Shared
Freed %lld bytes by purging tmp in container class %llu for identifier %@
No options dictionary specified!
stagedIdentifier
MobileInstallationRegisterSafeHarborForContainerClassWithIdentity_block_invoke
Apply Staged Update
DowngradeToPlaceholder
SkipWatchAppInstall
-[MIInstallerClient revertIdentity:withOptions:completion:]_block_invoke_3
com.apple.developer.default-data-protection
Extensions
Watch
LegacyErrorString
Got expected error: %@
-[MIInstallerClient endTestMode:]
PlugIns
allowDistributorChange
Freed %lld bytes by purging Library/Caches in container class %llu for identifier %@
B20@?0@\"NSURL\"8C16
Warning, couldn't kill %@ error: %@
Failed to serialize iTunesMetadata dictionary: %@
-[MIHelperServiceFrameworkClient stagingLocationForSystemContentWithinSubsystem:error:]_block_invoke
The persona parameter must be specified
ErrorDescription
.com.apple.mobile_container_manager.metadata.plist
CF_MIEmergencyOffloadVersion
Failed to determine if purge directory exists at %@ : %@
_IsRestorableAppBasedOnMetadata
Failed to check test mode: %@
Install (Promote From Placeholder)
v24@?0@\"LSRecordPromise\"8@\"NSError\"16
Install (New)
Failed to clean up bundle directory at %@ on failure : %@
BOMCopier signaled fatal file error on %s : %s
alternateIconName
IsUserInitiated
-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:fromURL:returningResultInfo:completion:]_block_invoke_3
com.apple.developer.default-data-protection-if-available
SBIconMasqueradeIdentifier
LastSystemVersion
com.apple.migration.plist
v20@?0B8@\"NSError\"12
com.apple.developer.not-executable
AITransactionLog.m
Failed to count the files and bytes in archive : %d (%s)
skipWatchAppInstall
Failed to get legacy error string from NSError's userInfo
bundleIdentifier
swift-playgrounds
-[MIStagedUpdateMetadata isEqual:]
sinfDataType
ProvisioningProfileInstallFailureIsFatal
+ %lld; Freed %lld bytes, need %lld bytes
-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke_3
Failed to end test mode: %@
Warning, couldn't get pid of %@ error: %@
com.apple.security.system-container
MCMMetadataInfo
Failed to count files and bytes in the archive at %@ : %@
MIPurgeExpendableAppsAndDataForRestore
Did not find %@ key in DataMigration prefs set, or it was not set to a string value
MobileInstallationRevertApplicationWithIdentityAndAssertionBlockWithError
bom_fatal_file_error_handler
B16@?0r*8
App with identifier %@ at %@ is missing the purchasing Apple ID in its metadata so it's not restorable
%s is no longer implemented
Failed to set mode to 0%o for %s : %s
Install (Placeholder)
PerformAPFSClone
v24@?0@\"MIBundleMetadata\"8@\"NSError\"16
bom_file_error_handler
Failed to get XPC connection
waitForDeletion
MobileInstallationICLRecordsUninstallForInstallCoordinationWithError
com.apple.developer.memory.transfer-send
Found DataMigration prefs key %@ set to %@ which is different from the current build version %@; not modifying DataMigration prefs
com.apple.WebKit.PushBundles
StaticDiskUsage
LSCounterpartIdentifiers
v24@?0@\"MIStagedUpdateMetadata\"8@\"NSError\"16
MobileInstallationRegisterPlaceholderForReference
com.apple.private.security.no-container
com.apple.developer.memory.transfer-accept
com.apple.private.extensionkit.builtinsystempersona
_ForceDataMigrationNextBoot
com.apple.Posters
Bundle at %@ has no icon (no Icon Info.plist content)
PlaceholderBundleTypeEmbeddedWatchApp
com.apple.developer.wrapper-bundle
PluginKitPlugin
Placeholder
StashMode
NULL
MobileInstallationInstallApp
v24@?0@\"MIAppReference\"8@\"NSError\"16
ServiceConnectionInterrupted
com.apple.private.security.no-sandbox
Install (Unknown Type)
UIRequiredDeviceCapabilities
Success
Failed to get the path to containers of class %llu in %@
iTunesMetadata.plist
Failed to materialize placeholder into %@ : %@
+[MIBOMWrapper _countFilesAndBytesInArchiveAtURL:withBOMCopier:totalFiles:totalUncompressedBytes:error:]
Found non-boolean value for boolean entitlement %@: %@ ; assuming %s.
_ResetLaunchServicesDatabase
TransactionLog
embedded.mobileprovision
Called with dataVolumeRootPath=\"%s\"; purgeTmpAndCaches:%c; effort:%llu; bytesToFree:%lld
Removed data migration prefs to force migration on next boot
Failed to assume _installd identity: %@
Invalid MIPersonaLifecycleEventType %@ when reporting persona lifecycle event
v24@?0@\"ICLSinfInfo\"8@\"NSError\"16
containers
-[MIPlaceholderConstructor _entitlementsForPath:error:]
Returning %lld freed bytes (goal was %lld bytes)
uid
-[MIHelperServiceFrameworkClient _synchronousRemoteObjectProxyWithErrorHandler:]
LSApplicationLaunchProhibited
%@ installationRequestorAuditToken: %@
com.apple.developer.web-browser-engine.host
v16@?0@\"NSDictionary\"8
End
NSExtension
_AppURLInContainer
MobileInstallationRegisterSafeHarbor
com.apple.security.system-group-containers
com.apple.developer.associated-appclip-app-identifiers
Uninstall (Placeholder)
-[MIPlaceholderConstructor _copyStringsToPlaceholder:onlyDirectories:error:]_block_invoke
-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:validationData:error:]_block_invoke
Could not mark %s static: %s
preservePlaceholderAsParallel
AllowInstallLocalProvisioned
Offloading non-Apple apps...
App with identifier %@ is already a placeholder at %@
Fail
Application
B32@?0@\"NSURL\"8@\"NSString\"16@\"NSDictionary\"24
MobileInstallationClearUninstalled_block_invoke
Failed to construct SecStaticCode for %@ : %d
EXAppExtensionAttributes
stagedDiskUsage
com.apple.developer.web-browser-engine.rendering
%s (%s) : %s
_installd
AppGroup
Failed to get CFBundleExecutable key from Info.plist of %@
_ProcessApp
Install (Placeholder Update)
InfoPlist.strings
Failed to copy InfoPlist.strings from \"%@\" to \"%@\"
Connection was interrupted before all delegate messages were received
com.apple.security.application-groups
InfoPlist.loctable
AppClips
developerInstall
v24@?0@8@\"NSError\"16
app reference has unknown domain
WKCompanionAppBundleIdentifier
Connection was invalidated before all delegate messages were received
_OffloadApps
_ProcessBundleContainer
MobileInstallationUnregisterContentsOnRoot_block_invoke
SystemGroup
NSApplicationRequiresArcade
isUserInitiated
-[MIInstallerClient revertForLSWithIdentifier:withOptions:completion:]_block_invoke_3
-[MIInstallerClient dieForTesting]_block_invoke
Unknown type %ld passed for identifier; contains %@
MobileInstallationRegisterSafeHarborForContainerClassWithIdentity
Failed to create metadata from plist data: %@
com.apple.private.security.container-required
com.apple.developer.parent-application-identifiers
isSystemAppInstall
MobileInstallationUpdateSystemAppState_block_invoke
Data
PlaceholderBundleTypeExtensionKit
_PurgeDirectory_block_invoke_2
MIFinalizeReferenceForInstalledAppWithError
Failed to rename %s to %s : %s
Unknown Phase
provisioningProfiles
FATAL ERROR: failed to locate and reset the LS database; purging apps is not possible
MIInvalidateReferenceForInstalledAppWithError
Failed to traverse %@ : %@
-[MIPlaceholderConstructor _materializeConstructors:intoBundle:error:]
com.apple.private.security.system-application
BOMCopier signaled file error on %s : %s
Caches
BundleMetadata.plist
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:]
-[MIHelperServiceFrameworkClient removeDeveloperAppAtURL:error:]
Construction
Warning, couldn't initialize xpc connection to %@
com.apple.security.system-groups
Proxy returned error: %@
isDeveloperInstall
com.apple.Playgrounds
com.apple.developer.accessory-transport-extension
Unable to set F_NOCACHE accessing file %s %s
v16@?0@\"NSError\"8
com.apple.developer.app-management-domain
-[MIInstallerClient installURL:identity:targetingDomain:withOptions:returningResultInfo:completion:]_block_invoke_3
MobileInstallationRegisterContentsForDiskImageAtURL_block_invoke
WKRunsIndependentlyOfCompanionApp
%s is not available on this platform!
MobileInstallationWatchKitInstallerSnapshotWKApp_block_invoke
platform-application
Failed to load Info.plist from %@
Unknown PlaceholderBundleType value %lu
app
Dictionary serialization of MIInstallOptions.installationRequestorAuditToken is not available; dropping this option.
MobileInstallationReconcileContentsOnKnownOSModules_block_invoke
com.apple.developer.networking.networkextension
app reference has nil app identity
Containers
Unknown: %ld
installationRequestorAuditToken
-[MIHelperServiceFrameworkClient installMacDeveloperAppAtURL:toURL:targetURLType:error:]
_SendError
Re-throwing exception: %@
Bundle ID supplied to revert was nil.
write() returned %zd but we expected %lu when writing to %s
Found no keys in Info.plist in bundle at %@
AlternateIconName
-[MIInstallOptions legacyOptionsDictionary]
_PurgeDirectory
previous-application-identifiers
com.apple.developer.swift-playgrounds-app
Don't know how to create a path to containers of type %llu
-[MIPlaceholderConstructor _loadInfoPlistContentWithError:]
App with identifier %@ at %@ is missing the purchaser ID in its metadata so it's not restorable
com.apple.install_session_uuid
BOMCopier signaled fatal error: %s
v24@?0@\"MIStagingLocation\"8@\"NSError\"16
MIEnumerateContainersOfClass
Failed to read migration prefs from %@ : %@
MobileInstallationRegisterContentsOnRoot_block_invoke
-[MIInstallOptions isEqual:]
false
Failed to read metadata dictionary from %@ : %@
Executable
Skipping offload of presumed profile-validated app %@ at %@
com.apple.developer.wifi-infrastructure
com.apple.private.pluginkit.persona
com.apple.developer.homekit
open failed for %s : %s
Uninstall (Parallel Placeholder)
Attempting to purge container class %llu for identifier %@ at %@
v24@?0@\"NSDictionary\"8@\"NSError\"16
-[MIInstallerClient pidForTesting]_block_invoke
MobileInstallationUninstallAppWithIdentity
%s is unavailable on this platform
com.apple.Faces
Failed to write %lu bytes to %s : %s
CF_MIPlaceholderConstructorVersion
Unknown install target type: %lu
com.apple.mobile.installd
MobileInstallationSetAppLaunchState
com.apple.developer.web-browser-engine.webcontent
com.apple.appinstallation
appex
PackageExtractionFailed
Offload
Failed to parse current build version \"%@\"; removing %@ from DataMigration prefs to force migration
Freed %lld bytes by offloading app %@
App with identifier %@ at %@ has deviceBasedVPP = YES in its metadata so it's not restorable
app reference is nil
lproj
Failed to create placeholder constructor for app %@ at %@ : %@
Skipping offload of marketplace %@ at %@
MobileInstallationGetAllStagedUpdateIdentifiers
com.apple.developer.usernotifications.critical-alerts
installTargetType
lsInstallType
performAPFSClone
personaUniqueString
_PurgeDirectory_block_invoke
MobileInstallationLookupUninstalled_block_invoke
Stage (New Update)
LinkedParentBundleID
Reducing space saved by offloading %@, %lld, by %lld bytes used for the placeholder
v24@?0@\"NSArray\"8@\"NSError\"16
v24@?0@\"NSSet\"8@\"NSError\"16
linkedParentBundleID
com.apple.emergencyoffload.temp
Failed to getclass of file %s: %s
SBAppTags
autoInstallOverride
_PurgeExpendableDataContainerContentForContainerClass
Failed to get current build version
Failed to write updated bundle metadata to %@ : %@ [ignoring]
open_dprotected_np failed for %s for class %d : %s
geoJSONData
MobileInstallationLookupSystemAppState_block_invoke
Warning: MobileInstallationAppLaunchEnabled called on unsupported OS.
seatbelt-profiles
domain
Unknown placeholder type %lu
PlaceholderBundleTypeEmbeddedAppClip
\xf7
sinfData
q24@?0@8@16
com.apple.private.extensionkit.builtinanypersona
Entitlement %@ does not contain supported types; ignoring.
com.apple.mobileinstallation_client
Unknown Persona
Not including icon content in Info.plist because IFTopLevelAppBundlePlistKeys is not available
%{public}@/%{public}@:%lu:%lu:%lu:%u:%{public}@
%s:%s:%s:%ld:%s:%s
MobileInstallationHelperServiceProtocol
MIInstallerClient
NSSecureCoding
AITransactionLog
MIPlaceholderConstructor
MIBOMWrapper
MIAppReference
MobileInstallationAdditions
MobileInstallerDelegateProtocol
MICandidateContainer
MobileInstallerProtocol
MIStagedUpdateMetadata
NSCoding
MIHelperServiceFrameworkClient
MIInstallOptions
NSCopying
MICandidateAppContainer
setExportedInterface:
setInstallTargetType:
setTestModeForIdentifierPrefix:testMode:validationData:error:
_metadata
_performAPFSClone
arrayWithObjects:count:
pushReplacementInfoForApp:replacingApp:withCompletion:
setInstallBuildVersion:
stageItemAtURL:toStagingLocation:options:completion:
TQ,N,V_installIntent
initWithLegacyOptionsDictionary:
setByAddingObject:
supportsSecureCoding
validateAppIdentity:withError:
installerWithProgressBlock:
T@\"NSError\",&,N,V_delegatesCompleteError
TB,N,V_basicIOSPlaceholderForWatchOSLessThanSix
_allowLocalProvisioned
isEqual:
performPlaceholderInstallActions
setRemoteObjectInterface:
userInfo
_constructPlaceholdersForDirectory:itemsWithPathExtension:appendingToArray:bundleType:error:
enrollPersona:forApps:inDomain:withCompletion:
geoJSONData
setInstallForMigrator:
T@\"NSArray\",C,N,V_appExtensionPlaceholderConstructors
_bundleURL
T@\"MIStoreMetadata\",C,N,V_iTunesMetadata
_systemAppInstall
fileSystemRepresentation
provisioningProfileInstallFailureIsFatal
setDelegatesComplete:
stagingLocationForUserContentWithinSubsystem:error:
MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:
developerInstall
hash
setEmbeddedAppClipPlaceholderConstructors:
TB,N,V_isWatchKitExtension
TI,N,V_sinfDataType
_skipWatchAppInstall
isSystemAppInstall
metadataFromURL:error:
T@?,C,N,V_appDictionaryEnumBlock
currentHandler
infoPlistContent
setWaitForDeletion:
_bundleDirectoryName
_stagedIdentifier
preservePlaceholderAsParallel
revertIdentity:withOptions:completion:
T@\"NSData\",&,N,V_installSessionUUID
_installUUID
setTestModeForIdentifierPrefix:testMode:error:
_includeWatchAppPlaceholders
_infoPlistKeysToLoad
_linkedParentBundleID
linkedParentBundleID
materializeIntoBundleDirectory:error:
sortedArrayUsingComparator:
_log
makeSymlinkFromAppDataContainerToBundleForIdentifier:forPersona:completion:
initWithEmbeddedWatchAppSource:byPreservingFullInfoPlist:error:
T@\"NSString\",C,N,V_linkedParentBundleID
TQ,N,V_installTargetType
_infoPlistContent
purgeInstallCoordinationPromiseStagingDirectoryForUUID:keepStagingDirectory:error:
installerWithAppBundleRecordEnumerator:
installerWithProgressBlock:releaseTerminationAssertionBlock:
isEqualToString:
setPerformPlaceholderInstallActions:
skipWatchAppInstall
stringWithUTF8String:
_iTunesMetadata
allObjects
setObject:forKeyedSubscript:
stagingLocationForSystemContentWithinSubsystem:error:
setInstallDate:
_defaultLog
_embeddedAppClipPlaceholderConstructors
addPersona:toApp:inDomain:withCompletion:
migrateMobileContentWithCompletion:
T@\"MIAppIdentity\",R,N,V_identity
TB,N,V_preserveFullInfoPlist
TB,N,V_waitForDeletion
_identifier
_materializeConstructors:intoBundle:error:
estimatedSize
setTestFlags:withError:
stagedIdentifier
T@\"NSDictionary\",C,N,V_entitlements
delegatesComplete
isWatchKitExtension
markBundleAsPlaceholder:withError:
serviceName
setAppReplacementStatus:forApp:replacingApp:completion:
setIncludeAppClipPlaceholders:
setPersonaUniqueString:
_populateEmbeddedWatchAppPlaceholderConstructorsWithError:
acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:completion:
T@?,C,N,V_releaseTerminationAssertBlock
_bundleIdentifier
_populateAppExtensionPlaceholderConstructorsWithError:
cloneSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:
triggerRegistrationForDiskImageContentForOptions:withCompletion:
rootURL
_watchKitExtensionPlaceholderConstructor
updateSystemAppStateForIdentifier:appState:completion:
.cxx_destruct
_allowDistributorChange
installTypeSummaryString
invalidate
isLaunchProhibited
referencesForBundleWithIdentifier:inDomain:withCompletion:
setConnection:
setStashMode:
_placeholderType
copyWithZone:
count
setInstallLocation:
setStagedDiskUsage:
setTestModeForIdentifierPrefix:testMode:validationData:
sinfData
unsignedIntegerValue
autoInstallOverride
deviceBasedVPP
mutableCopy
setITunesMetadata:
installerWithAppDictionaryEnumerator:
registerPlaceholderForReference:completion:
T@\"NSArray\",C,N,V_embeddedWatchAppPlaceholderConstructors
installationRequestorAuditToken
T@\"NSDictionary\",&,N,V_infoPlistContent
_uid
extractZipArchiveAtURL:toURL:withError:
firstNetworkExtension
placeholderType
setAppExtensionPlaceholderConstructors:
setData:forExtendedAttributeNamed:onURL:error:
T@?,C,N,V_progressBlock
appDictionaryEnumBlock
objectForKeyedSubscript:
progressBlock
cancelUpdateForStagedIdentifiers:completion:
queue
setExportedObject:
setProgressBlock:
_entitlementsForPath:error:
includeWatchAppPlaceholders
stringWithFileSystemRepresentation:length:
_initWithLog:
fetchInfoForContainerizedAppWithBundleID:options:completion:
setEligibilityTestOverrides:withError:
setProvisioningProfileInstallFailureIsFatal:
_writeInfoPlistToPlaceholder:substitutingIconContent:withError:
TB,N,V_provisioningProfileInstallFailureIsFatal
_populateEmbeddedAppClipPlaceholderConstructorsWithError:
installMacDeveloperAppAtURL:toURL:targetURLType:error:
containsObject:
_provisioningProfiles
connection
encodeBool:forKey:
purchaserID
unregisterContentsOnOSModuleAtURL:completion:
allocWithZone:
setInstallType:
T@\"NSURL\",&,N,V_appURL
_synchronousRemoteObjectProxyWithErrorHandler:
iTunesMetadata
setTestMode:
installURL:identity:targetingDomain:withOptions:returningResultInfo:completion:
wipeStagingRootAndSetUpPerUserDataDirWithCompletion:
T@\"MIPlaceholderConstructor\",R,N
setInstallationRequestorAuditToken:
T@\"NSString\",C,N,V_stagedIdentifier
reportProgress:
TQ,N,V_lsInstallType
dataForExtendedAttributeNamed:length:fromURL:error:
legacyOptionsDictionary
setStagedIdentifier:
setTestingEnabled:
uid
T@\"NSString\",C,N,V_bundleIdentifier
checkCapabilities:withOptions:completion:
lookupSystemAppStateWithOptions:completion:
setXpcConnection:
TQ,N,V_installLocation
invalidateReference:withCompletion:
unregisterContentsOnRoot:deferUntilNextBoot:completion:
TQ,N,V_stagedDiskUsage
_basicIOSPlaceholderForWatchOSLessThanSix
_userInitiated
createSafeHarborWithIdentifier:forPersona:containerType:andMigrateDataFrom:completion:
initWithMachServiceName:options:
installUUID
T@\"NSString\",R,N
waitForDeletion
TB,N,V_installForMigrator
_provisioningProfileInstallFailureIsFatal
allowDistributorChange
enumerateKeysAndObjectsUsingBlock:
getTestModeEnabled:outError:
T@\"NSData\",C,N,V_geoJSONData
Tq,R,N
_copyStringsToPlaceholder:onlyDirectories:error:
copyItemAtURL:toURL:error:
itemExistsAtURL:error:
raiseException
updateSinfForIXWithIdentifier:withOptions:sinfData:completion:
_loadInfoPlistContentWithError:
TB,N,V_skipWatchAppInstall
fetchInfoForFrameworkAtURL:options:completion:
removeDeveloperAppAtURL:error:
unsignedLongLongValue
xpcConnection
scanCharactersFromSet:intoString:
_appURL
_delegatesCompleteCondMutex
_preservePlaceholderAsParallel
_sinfData
numberWithUnsignedInteger:
serializeToURL:error:
T@?,C,N,V_appBundleRecordEnumBlock
addObject:
isPlaceholder
sideLoadedDeviceBasedVPP
isUserInitiated
TB,N,V_includeAppClipPlaceholders
addEntriesFromDictionary:
initForStagedIdentifier:diskUsage:
setSkipBlacklist:
updateiTunesMetadataForIXWithIdentifier:metadata:completion:
_countFilesAndBytesInArchiveAtURL:withBOMCopier:totalFiles:totalUncompressedBytes:error:
_includeAppClipPlaceholders
_stashMode
removeSafeHarborForIdentity:ofType:withOptions:completion:
_waitForDeletion
T@\"NSString\",R,C,N
_invalidateObject
bundleURL
T@\"NSDictionary\",R,C,N,V_metadata
personaUniqueString
rebuildBuiltInContentMappingWithCompletion:
setLsInstallType:
endTestModeWithCompletion:
identifier
init
initWithBundleID:
removePersona:fromApp:inDomain:withCompletion:
_geoJSONData
dataWithBytesNoCopy:length:freeWhenDone:
diskUsageForURL:
getPidForTestingWithCompletion:
setGeoJSONData:
revertForLSWithIdentifier:withOptions:completion:
setIsWatchKitExtension:
stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:
T@\"NSArray\",C,N,V_embeddedAppClipPlaceholderConstructors
T@\"NSDictionary\",R,C,N
URLForDirectory:inDomain:appropriateForURL:create:error:
domain
referenceUUID
removeObjectForKey:
setPreservePlaceholderAsParallel:
setPreserveTargetBundleName:
basicIOSPlaceholderForWatchOSLessThanSix
waitForSystemAppMigratorToComplete:
_waitForPendingDelegateMessages
decodeBoolForKey:
initWithFormat:arguments:
logScenario:step:success:forBundleID:description:
releaseTerminationAssertBlock
_introspectWithError:
clearTestFlags:withCompletion:
createDirectoryAtURL:withIntermediateDirectories:mode:class:error:
setPreserveFullInfoPlist:
synchronousRemoteObjectProxyWithErrorHandler:
TQ,N,V_stashMode
_appBundleRecordEnumBlock
setTestFlags:withCompletion:
setTestModeWithCompletion:
MI_URLByAppendingPathComponents:lastIsDirectory:
TB,N,V_preserveTargetBundleName
now
endAppReplacementWithStatus:forApp:completion:
sharedInstance
unregisterContentsForDiskImageAtURL:completion:
extractZipArchiveAtURL:toURL:withError:extractionProgressBlock:
code
installIntent
setPersonas:forApp:inDomain:withCompletion:
_installIntent
createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:
delegateMessageDeliveryCompleteWithError:
hasPrefix:
removeMacAppWithBundleID:atURL:error:
setSinfData:
installLocation
_installForMigrator
setEligibilityTestOverrides:withCompletion:
setPlaceholderType:
skipBlacklist
MI_writeAtomicallyToURL:withMode:owner:group:error:
UUID
appURL
bundleID
dataWithBytes:length:
errorWithDomain:code:userInfo:
logStep:byParty:phase:success:forBundleID:persona:description:
pidForTesting
allStagedUpdatesWithCompletion:
validateAppReference:withError:
initWithSource:byPreservingFullInfoPlist:error:
stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:
bundleAtURLIsPlaceholder:
description
length
remoteObjectProxyWithErrorHandler:
setEntitlements:
setInvalidationHandler:
uninstallIdentifiers:withOptions:completion:
unsignedIntValue
altDSID
countByEnumeratingWithState:objects:count:
diskUsageForLaunchServicesWithBundleIDs:options:withError:
installForMigrator
longLongValue
setTestingEnabled:error:
stagingLocationForUserContentWithinSubsystem:completion:
TB,N,V_performPlaceholderInstallActions
uninstallRecordArrayToDictionary:
userInitiated
TB,N,V_allowDistributorChange
allStagingLocationsWithinSubsystem:completion:
enumerateAppDictionary:error:
finalizeStagedInstallForIdentifier:returningResultInfo:completion:
moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:
setAllowDistributorChange:
setBasicIOSPlaceholderForWatchOSLessThanSix:
_preserveFullInfoPlist
TB,N,GisSystemAppInstall,V_systemAppInstall
bundleDirectoryName
decodeObjectOfClass:forKey:
initWithContainerURL:identifier:metadata:
numberWithUnsignedInt:
_logScenario:step:success:forBundleID:persona:description:
addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:
allowLocalProvisioned
embeddedWatchAppPlaceholderConstructors
setDeveloperInstall:
setProvisioningProfiles:
setWithArray:
entitlements
iTunesArtworkData
lookupUninstalledWithOptions:completion:
performAPFSClone
MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:error:
_connection
watchKitExtensionPlaceholderConstructor
MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:
clearUninstalledIdentifiers:withOptions:completion:
registerContentsForDiskImageAtURL:completion:
_transferAndUpdateInstallSessionIDsToPlaceholder:error:
migrationPlistURL
removeItemAtURL:error:
setSystemAppInstall:
dealloc
setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:
appBundleRecordEnumBlock
_performPlaceholderInstallActions
createDirectoryAtURL:withIntermediateDirectories:mode:error:
setAppDictionaryEnumBlock:
stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:
systemAppInstall
_installSessionUUID
setReleaseTerminationAssertBlock:
MI_dictionaryWithContentsOfURL:options:error:
TI,R,N,V_uid
_installTargetType
decodeObjectOfClasses:forKey:
initWithServiceName:
setAllowLocalProvisioned:
sortUsingComparator:
fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
setBundleDirectoryName:
encodeObject:forKey:
isDeveloperInstall
raiseExceptionWithCompletion:
UTF8String
_sharedConnection
setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:
stagingLocationForURL:withinStagingSubsystem:usingUniqueName:completion:
storeListOfAppsRequiringPreInstallConsent:completion:
TB,N,GisDeveloperInstall,V_developerInstall
isAppleApp
setBundleIdentifier:
sinfDataType
TQ,N,V_autoInstallOverride
dictionaryWithCapacity:
_initWithSource:byPreservingFullInfoPlist:forBundleType:error:
endTestMode:
getTestModeWithCompletion:
stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:
T@\"NSURL\",&,N,V_bundleURL
_appExtensionPlaceholderConstructors
_developerInstall
allStagingLocationsWithinSubsystem:error:
reconcileContentsOnKnownOSModules:completion:
setWithObjects:
path
setInstallIntent:
setLaunchProhibited:forApp:withCompletion:
T@\"NSString\",R,C,N,V_identifier
acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:withCompletion:
interfaceWithProtocol:
setClasses:forSelector:argumentIndex:ofReply:
_sinfDataType
characterSetWithRange:
clearTestFlags:withError:
defaultManager
dieForTesting
isDataContainerEmpty:ofContainerType:completion:
resume
T@\"NSData\",C,N,V_iTunesArtworkData
_copyInfoPlistLoctableToPlaceholder:error:
arrayWithCapacity:
delegatesCompleteError
resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:
triggerRegistrationForContainerizedContentForOptions:withCompletion:
TB,R
_alternateIconName
_xpcConnection
alternateIconName
appBundleIDsWithPersona:inDomain:withCompletion:
encodeWithCoder:
setInfoPlistContent:
setLinkedParentBundleID:
setIncludeWatchAppPlaceholders:
setInstallUUID:
finalizeReference:withCompletion:
T@\"NSUUID\",R,N,V_referenceUUID
_entitlements
_identity
finalizeReference:completion:
metadataFromPlistData:error:
preserveTargetBundleName
removeAppReplacementStateForApp:completion:
scanInt:
T@\"NSString\",C,N,V_alternateIconName
T@\"NSString\",&,N,V_bundleDirectoryName
TB,N,V_preservePlaceholderAsParallel
URLByAppendingPathComponent:isDirectory:
_appDictionaryEnumBlock
_installLocation
defaultWorkspace
volumeUUIDForURL:completion:
TB,N,V_performAPFSClone
_skipBlacklist
bundleIdentifier
dictionaryWithContentsOfURL:error:
TB,N,V_skipBlacklist
_stagedDiskUsage
cloneItemAtURL:toURL:onBehalfOf:completion:
registerContentsOnRoot:deferUntilNextBoot:completion:
setDelegatesCompleteError:
stagingLocationForSystemContentWithinSubsystem:completion:
updatePlaceholderMetadataForApp:installType:failureReason:underlyingError:failureSource:completion:
UUIDString
_personaUniqueString
_referenceUUID
fetchListOfAppsRequiringPreInstallConsent:
appExtensionPlaceholderConstructors
initWithCoder:
installSessionUUID
_installationRequestorAuditToken
enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:
initWithReferenceUUID:identity:domain:uid:
prepareReplacementOfApp:byApp:extensionBundleIDs:withCompletion:
setPerformAPFSClone:
T@\"NSString\",C,N,V_personaUniqueString
compare:
embeddedAppClipPlaceholderConstructors
includeAppClipPlaceholders
removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:
setBundleURL:
setITunesArtworkData:
T@\"NSData\",C,N,V_sinfData
TB,N,V_allowLocalProvisioned
TB,N,V_includeWatchAppPlaceholders
setWithObject:
stageInstallURL:identity:targetingDomain:withOptions:completion:
T@\"MIPlaceholderConstructor\",&,N,V_watchKitExtensionPlaceholderConstructor
_rootURL
installTargetType
itemDoesNotExistAtURL:
propertyListDataWithError:
reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:
setInterruptionHandler:
_embeddedWatchAppPlaceholderConstructors
metadataFromPlistAtURL:error:
referencesForBundleWithIdentifier:inDomain:completion:
setAppBundleRecordEnumBlock:
setAutoInstallOverride:
enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:
stagedDiskUsage
bytes
logStep:byParty:phase:success:forBundleID:description:
uninstallIdentity:withOptions:completion:
_domain
TB,N,GisUserInitiated,V_userInitiated
_writeIconToPlaceholder:infoPlistIconContent:error:
lsInstallType
setAlternateIconName:
waitForSystemAppMigratorWithCompletion:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
_delegatesCompleteError
fetchDiskUsageForIdentifiers:withOptions:completion:
personasForBundleID:inDomain:withCompletion:
TQ,N,V_placeholderType
T^{?=[8I]},N,V_installationRequestorAuditToken
_preserveTargetBundleName
fetchInfoForContainerizedAppWithIdentity:inDomain:options:completion:
TB,N,V_delegatesComplete
_autoInstallOverride
bundleRecordArrayToInfoDictionaryArray:
pathExtension
stashMode
MI_writeToURL:format:options:error:
numberWithInt:
registerContentsOnOSModuleAtURL:completion:
setWatchKitExtensionPlaceholderConstructor:
_delegatesCompleteCond
provisioningProfiles
setAppURL:
snapshotWKAppInCompanionAppID:toURL:options:completion:
invalidateReference:completion:
setSkipWatchAppInstall:
appleID
getAppMetadataForApp:completion:
registerSafeHarborAtPath:forIdentity:ofType:withOptions:completion:
systemAppMigratorHasCompleted:
_delegatesComplete
listSafeHarborsOfType:forPersona:withOptions:completion:
metadata
setQueue:
updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:
enumerateAppBundleRecord:error:
_lsInstallType
_progressBlock
boolValue
handleFailureInMethod:object:file:lineNumber:description:
installParallelPlaceholderForStagedIdentifier:fromURL:returningResultInfo:completion:
stringWithFormat:
createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:
personasForBuiltInBundleID:withCompletion:
TQ,R,N,V_domain
T@\"NSData\",&,N,V_installUUID
T@\"NSXPCConnection\",&,N,V_connection
TB,R,N
_iTunesArtworkData
initializeWithLog:
installURL:identity:targetingDomain:options:returningResultInfo:completion:
MI_writeAtomicallyToURLMatchingCurrentFileMetadata:format:error:
T@\"NSURL\",R,N,V_rootURL
setSinfDataType:
setUserInitiated:
_queue
itemID
numberWithUnsignedLongLong:
scannerWithString:
setInstallSessionUUID:
T@\"NSArray\",C,N,V_provisioningProfiles
_remoteObjectProxyWithErrorHandler:
createAppSnapshotWithBundleID:snapshotToURL:onlyV1AppIfPresent:placeholderOnly:completion:
itemExistsAtURL:
releaseTerminationAssertion
setSystemAppMigrationComplete:
_releaseTerminationAssertBlock
identity
lastPathComponent
linkedBundleIDsForAppIdentity:withCompletion:
preserveFullInfoPlist
stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:completion:
T@\"NSXPCConnection\",&,N,V_xpcConnection
_isWatchKitExtension
copy
setEmbeddedWatchAppPlaceholderConstructors:
v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">32
v60@0:8@16@24Q32@40B48@?52
@?
v56@0:8@\"NSString\"16@\"MIAppIdentity\"24Q32@\"NSDictionary\"40@?<v@?@\"NSError\">48
B40@0:8@16Q24^@32
B24@0:8@16
I
v32@0:8Q16@?<v@?@\"MIStagingLocation\"@\"NSError\">24
B24@0:8^@16
B48@0:8@16S24I28I32i36^@40
v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSError\">28
v64@0:8@\"NSString\"16Q24Q32@\"NSError\"40Q48@?<v@?@\"NSError\">56
v24@0:8@\"NSCoder\"16
v48@0:8Q16@24@32@?40
v36@0:8B16@20@?28
v44@0:8@\"NSString\"16@\"NSURL\"24B32@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">36
v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32
v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32
v40@0:8@\"NSString\"16Q24@?<v@?@\"NSSet\"@\"NSError\">32
@24@0:8@16
@\"NSString\"
v20@0:8I16
v60@0:8@16Q24B32@36@44@52
q16@0:8
@\"MIPlaceholderConstructor\"
v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32
v40@0:8Q16@\"MIAppIdentity\"24@?<v@?@\"NSError\">32
@32@0:8@16^@24
B16@0:8
v32@0:8Q16@?<v@?@\"NSSet\"@\"NSError\">24
@32@0:8@?16@?24
v36@0:8@16i24@?28
B40@0:8@16^@24^@32
v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"MIStagedUpdateMetadata\"@\"NSError\">48
v32@0:8@\"ICLRegistrationOptions\"16@?<v@?@\"NSError\">24
v24@0:8^{?=[8I]}16
v56@0:8@16@24Q32@40@?48
v32@0:8@\"NSDictionary\"16@\"NSError\"24
v32@0:8@\"ICLBundleRecord\"16@\"NSError\"24
v44@0:8@16@24B32@?36
B32@0:8Q16^@24
v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24
v40@0:8@\"NSObject\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
v48@0:8@\"NSString\"16@\"NSURL\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40
v52@0:8@16Q24B32@36@44
v36@0:8B16@\"MIAppIdentity\"20@?<v@?@\"NSError\">28
v48@0:8@\"NSSet\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40
v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSError\">24
v32@0:8@16@?24
v48@0:8@\"NSURL\"16@\"MIStagingLocation\"24@\"MIInstallOptions\"32@?<v@?@\"NSURL\"B@\"NSError\">40
v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24
B
v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40
v48@0:8@\"<MILocationProtocol>\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40
v32@0:8Q16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSError\">40
v48@0:8@\"NSString\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40
v32@0:8Q16@?<v@?@\"NSError\">24
v24@0:8@?<v@?i>16
B32@0:8^B16^@24
@\"NSObject<OS_dispatch_queue>\"
v68@0:8Q16Q24Q32B40@44@52@60
v40@0:8@\"MIAppIdentity\"16@\"MIAppIdentity\"24@?<v@?@\"NSError\">32
v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32
Q
B40@0:8@16@24^@32
B36@0:8@16B24^@28
@\"NSURL\"
v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSError\">40
v32@0:8@\"MIAppReference\"16@?<v@?@\"NSError\">24
@88@0:8@16@24@32@40{?=[8I]}48^@80
v36@0:8@16B24@?28
v48@0:8@16@24Q32@?40
v32@0:8@\"NSString\"16@?<v@?@\"MIBundleMetadata\"@\"NSError\">24
@\"NSXPCConnection\"
v80@0:8@\"MIStagingLocation\"16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72
@\"NSError\"
@\"NSUUID\"
v60@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40B48@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">52
v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24
v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"ICLSinfInfo\"@\"NSError\">40
@44@0:8@16B24Q28^@36
v72@0:8@16@24{?=[8I]}32@?64
v24@0:8@\"NSDictionary\"16
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
@44@0:8@16@24Q32I40
v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28
v40@0:8@\"NSString\"16Q24@?<v@?@\"NSDictionary\"@\"NSError\">32
v48@0:8@\"NSString\"16@\"NSSet\"24Q32@?<v@?@\"NSError\">40
v24@0:8@16
v48@0:8@16@24B32B36@?40
v40@0:8@16Q24@32
@40@0:8@16@24@32
v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32
v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSError\">24
@\"MIAppIdentity\"
@48@0:8@16Q24@32^@40
@\"MIStoreMetadata\"
v32@0:8@16@24
@16@0:8
@96@0:8@16@24@32@40@48{?=[8I]}56^@88
v40@0:8@16@24@?32
v56@0:8@\"NSString\"16@\"NSString\"24Q32@\"NSURL\"40@?<v@?@\"NSError\">48
v40@0:8Q16@24@?32
v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32
v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\">28
v48@0:8Q16@\"MIAppIdentity\"24@\"MIAppIdentity\"32@?<v@?@\"NSError\">40
@32@0:8@16Q24
B44@0:8@16S24I28I32^@36
v32@0:8@\"MIAppReference\"16@?<v@?@\"LSRecordPromise\"@\"NSError\">24
@36@0:8@16B24^@28
@48@0:8@16@24Q32^@40
v24@0:8@\"NSError\"16
v64@0:8@16Q24Q32@40Q48@?56
B52@0:8@16S24I28I32i36B40^@44
v48@0:8Q16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v24@0:8@?<v@?B@\"NSError\">16
v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSSet\"@\"NSError\">24
v48@0:8@16@24@32@?40
v36@0:8@\"NSString\"16B24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">28
v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
v24@0:8@?<v@?@\"NSError\">16
@24@0:8^{_NSZone=}16
Q16@0:8
@\"NSArray\"
v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16
v48@0:8@\"MIAppIdentity\"16@\"MIAppIdentity\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24
@32@0:8Q16^@24
v20@0:8B16
@\"NSData\"
v72@0:8@\"NSURL\"16@\"NSURL\"24{?=[8I]}32@?<v@?@\"NSError\">64
v48@0:8@\"MIAppIdentity\"16Q24@\"NSData\"32@?<v@?@\"MIAppReference\"@\"NSError\">40
B48@0:8@16Q24@32^@40
v24@0:8@?16
v48@0:8@16Q24@32@?40
v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">32
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32
v60@0:8Q16Q24Q32B40@44@52
v16@0:8
B56@0:8@16^{_BOMCopier=}24^Q32^Q40^@48
v40@0:8@16Q24@?32
i16@0:8
v40@0:8@\"NSString\"16Q24@\"NSDictionary\"32
v24@0:8Q16
@\"NSDictionary\"
@24@0:8@\"NSCoder\"16
B32@0:8@16^@24
v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSError\">40
v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40
@24@0:8@?16
^{?=[8I]}
v80@0:8@16@24@32{?=[8I]}40@?72
@\"NSObject<OS_os_log>\"
B48@0:8@16@24^@32@?40
v40@0:8@\"NSURL\"16Q24@?<v@?B@\"NSError\">32
@?16@0:8
{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}
B56@0:8@16@24@32Q40^@48
v32@0:8@\"NSURL\"16@?<v@?@\"NSUUID\"@\"NSError\">24
v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32
B28@0:8B16^@20
^{?=[8I]}16@0:8
I16@0:8
v32@0:8Q16@?24
```
