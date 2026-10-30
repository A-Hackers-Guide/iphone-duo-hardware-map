# `/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 539,536 bytes.

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
Unknown
Updating key %@ in DataMigration's prefs from %@ to %@ to force migration
Failed to create placeholder constructor for app %@ at %@ : %@
MobileInstallationInstallParallelPlaceholderForStagedUpdate
v32@?0@8@16^B24
MinimumOSVersion
ErrorDetail
com.apple.developer.superseded-application-identifiers
AppGroup
-[MIHelperServiceFrameworkClient stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:]_block_invoke
Swallowing caught exception: %@
Placeholder
InfoPlist.loctable
%@ installationRequestorAuditToken: %@
Failed to determine if purge directory exists at %@ : %@
Offloading Apple apps...
-[MIInstallerClient setTestMode:]
Preferences
seatbelt-profiles
Apply Staged Update
SBAppTags
-[MIPlaceholderConstructor materializeIntoBundleDirectory:error:]
sinfDataType
Skipping offload of presumed profile-validated app %@ at %@
Found non-boolean value for boolean entitlement %@: %@ ; assuming %s.
Found DataMigration prefs key %@ set to %@ which is different from the current build version %@; not modifying DataMigration prefs
_ProcessBundleContainer
_AppURLInContainer
Failed to enumerate %@ : %@
v20@?0B8@\"NSError\"12
v12@?0i8
Failed to write %lu bytes to %s : %s
Customer
B16@?0r*8
Failed to traverse %@ : %@
com.apple.emergencyoffload.temp
-[MIInstallerClient finalizeStagedInstallForIdentifier:returningResultInfo:completion:]_block_invoke_3
MissingPackagePath
MobileInstallationUnregisterContentsForDiskImageAtURL_block_invoke
TransactionLog
couldn't allocate a string
APIInternalError
beta-reports-active
open_dprotected_np failed for %s for class %d : %s
Failed to rename %s to %s : %s
Uninstall (Parallel Placeholder)
BOMCopier signaled fatal error: %s
installationRequestorAuditToken
Failed to enumerate app bundle containers: %@
Warning, couldn't get pid of %@ error: %@
com.apple.private.extensionkit.builtinsystempersona
-[MIPlaceholderConstructor _writeInfoPlistToPlaceholder:substitutingIconContent:withError:]
Could not mark %s static: %s
_ForceDataMigrationNextBoot
MobileInstallationUnregisterContentsOnRoot_block_invoke
installTargetType
MobileInstallationCopyInstalledDeveloperAppsForLaunchServices
MobileInstallationReconcileContentsOnKnownOSModules_block_invoke
com.apple.security.system-container
fstat failed for %s : %s
MIAcquireReferenceForInstalledAppWithError
MobileInstallationSetAppLaunchState
com.apple.private.mobileinstall.upgrade-enabled
app reference has unknown domain
Unknown placeholder type %lu
-[MIHelperServiceFrameworkClient removeDeveloperAppAtURL:error:]
MobileInstallationRegisterContentsForDiskImageAtURL_block_invoke
application-identifier
Attempting to offload user apps...
AutoInstallWatchApp
isUserInitiated
Failed to get current build version
_ResetLaunchServicesDatabase
MobileInstallationUpdateiTunesMetadataForInstallCoordinationWithWrapperURL
com.apple.security.application-groups
WKCompanionAppBundleIdentifier
waitForDeletion
isSystemAppInstall
Failed to locate app bundle in container with identifier %@ at %@
com.apple.developer.driverkit
MCMMetadataInfo
Failed to capture icon content for placeholder from bundle at %@ : %@
removefile for %s failed
MobileInstallationUpdateSinfDataForInstallCoordination_block_invoke
bom_file_error_handler
v24@?0@\"NSSet\"8@\"NSError\"16
Got expected error: %@
_CopySafeHarborsForContainerClass
Unable to set F_SINGLE_WRITER on %s %s
Failed to serialize iTunesMetadata dictionary: %@
-[MIInstallerClient dieForTesting]_block_invoke
com.apple.developer.usernotifications.critical-alerts
Failed to get XPC connection
v36@?0B8@\"NSArray\"12@\"LSRecordPromise\"20@\"NSError\"28
PlaceholderEntitlements.plist
bom_fatal_error_handler
Connection was invalidated before all delegate messages were received
-[MIInstallerClient installURL:identity:targetingDomain:withOptions:returningResultInfo:completion:]_block_invoke_3
com.apple.Faces
NSApplicationRequiresArcade
PlaceholderBundleTypeEmbeddedAppClip
sinfData
Found network extension %@ in app %@
v24@?0@\"NSArray\"8@\"NSError\"16
No options dictionary specified!
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:]
MobileInstallationUpdateSystemAppState_block_invoke
Failed to write Info.plist file to %@
_ProcessDataContainer
MobileInstallationRegisterSafeHarbor
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:]
Install (Demote To Placeholder)
Bundle at %@ has no icon (no Icon Info.plist content)
bundleIdentifier
StashMode
com.apple.private.security.no-sandbox
DataProtectionClass
com.apple.developer.wifi-infrastructure
Transaction log must be initialized before use. Please call +[AITransactionLog initializeWithLog:].
(container_error_copy_unlocalized_description returned NULL)
Failed to create copier
_PurgeDirectory
com.apple.lsd
MCMMetadataIdentifier
Info.plist
MobileInstallationCopyDiskUsageForLaunchServices
MobileInstallationRegisterSafeHarborForContainerClassWithIdentity
com.apple.developer.networking.networkextension
Entitlement %@ contains non-string values; ignoring.
MobileInstallationGetAllStagedUpdateIdentifiers
com.apple.private.security.no-container
com.apple.developer.swift-playgrounds-app
PerformAPFSClone
ProvisioningProfileInstallFailureIsFatal
Unknown install target type: %lu
App with identifier %@ is already a placeholder at %@
com.apple.private.security.container-required
Fail
domain
_ShouldContinueAfterIncrementingFreed
MobileInstallationCheckCapabilitiesMatch_block_invoke
-[MIHelperServiceFrameworkClient installMacDeveloperAppAtURL:toURL:targetURLType:error:]
-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:validationData:error:]_block_invoke
autoInstallOverride
%d%@1
Failed to materialize placeholder into %@ : %@
Invalid MIPersonaLifecycleEventType %@ when reporting persona lifecycle event
\xf7
Uninstall (User Data Only)
-[MIHelperServiceFrameworkClient allStagingLocationsWithinSubsystem:error:]_block_invoke
Developer
com.apple.private.security.system-application
Install (Patch Update)
-[MIPlaceholderConstructor _copyStringsToPlaceholder:onlyDirectories:error:]_block_invoke
Could not extract archive
ApplicationSINF
Failed to remove migration prefs file at %@ : %@
Not all delegate messages received: %@
%@
End
PlugIns
-[MIStagedUpdateMetadata isEqual:]
MIPurgeExpendableAppsAndDataForRestore
q24@?0@8@16
renamex_np failed to swap placeholder at %@ with live app %@ : %s
MobileInstallationSetAppLaunchState called on unsupported OS for %@
Shared
Could not create error response dictionary
Not including icon content in Info.plist because IFTopLevelAppBundlePlistKeys is not available
-[MIHelperServiceFrameworkClient updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:]
iTunesMetadata
Got unexpected error: %@
com.apple.private.mobileinstall.xpc-services-enabled
-[MIHelperServiceFrameworkClient setTestModeForIdentifierPrefix:testMode:error:]_block_invoke
Offload
com.apple.developer.web-browser-engine.networking
Containers
IsUserInitiated
AlternateIconName
Freed %lld bytes by purging Library/Caches in container class %llu for identifier %@
mobile
Skipping offload of LSApplicationLaunchProhibited app %@ at %@
-[MIInstallerClient revertIdentity:withOptions:completion:]_block_invoke_3
com.apple.WebKit.PushBundles
com.apple.appinstallation
System
Unknown Persona
MIEnumerateContainersOfClass
Staged Update Placeholder
preservePlaceholderAsParallel
Failed to set test mode: %@
MobileInstallationMakeStagedUpdateLiveForIdentifier
MobileInstallationCopyAppInfoForLaunchServicesWithWrapperURL
com.apple.developer.not-executable
com.apple.developer.marketplace.app-installation
SystemGroup
v24@?0@\"MIStagedUpdateMetadata\"8@\"NSError\"16
Client ignored error %@
MobileInstallationUnregisterContentsOnOSModuleAtURL_block_invoke
MobileInstallationRegisterSafeHarborForContainerClassWithIdentity_block_invoke
Ignoring non-existent purge directory: %@
iTunesMetadata.plist
v24@?0@\"LSRecordPromise\"8@\"NSError\"16
-[MIPlaceholderConstructor _transferAndUpdateInstallSessionIDsToPlaceholder:error:]
_PathForContainerClass
Skipping offload of network extension app %@ at %@
tmp
Install (Placeholder)
-[MIHelperServiceFrameworkClient _synchronousRemoteObjectProxyWithErrorHandler:]
-[MIHelperServiceFrameworkClient removeMacAppWithBundleID:atURL:error:]
[%@/%llu]
systemAppInstall
BundleMetadata.plist
MobileInstallationUninstallAppWithIdentity
_
%s : %s
+[MIBOMWrapper extractZipArchiveAtURL:toURL:withError:extractionProgressBlock:]
Attempting purge of mobile user's data containers' tmp and Library/Caches directories
_SendError
WKRunsIndependentlyOfCompanionApp
bom_fatal_file_error_handler
ApplicationSINFDataType
Reached goal of %lld bytes after freeing %lld bytes
LastSystemVersion
v16@?0@\"NSError\"8
-[MIInstallOptions isEqual:]
previous-application-identifiers
identity
-[MIInstallerClient _invalidateObject]
Warning, couldn't kill %@ error: %@
Failed to get CFBundleExecutable key from Info.plist of %@
Failed to clean up bundle directory at %@ on failure : %@
Failed to parse current build version \"%@\"; removing %@ from DataMigration prefs to force migration
Returned error %@
provisioningProfileInstallFailureIsFatal
_AppContainsNetworkExtension
v24@?0@\"ICLSinfInfo\"8@\"NSError\"16
Warning: MobileInstallationAppLaunchEnabled called on unsupported OS.
com.apple.Playgrounds
com.apple.developer.default-data-protection
com.apple.private.extensionkit.builtinanypersona
com.apple.
immutable_open
com.apple.developer.wrapper-bundle
lproj
Reducing space saved by offloading %@, %lld, by %lld bytes used for the placeholder
Archive at %@ contains a total of %llu files which account for a total of %llu uncompressed bytes
SkipWatchAppInstall
_PurgeDirectory_block_invoke_2
embedded.mobileprovision
ErrorDescription
com.apple.developer.app-management-domain
com.apple.Posters
com.apple.developer.web-browser-engine.webcontent
personaUniqueString
App with identifier %@ at %@ is missing the purchaser ID in its metadata so it's not restorable
Failed to set owner for %s : %s
CF_MIPlaceholderConstructorVersion
PlaceholderBundleTypeExtensionKit
-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:]
_PurgeExpendableDataContainerContentForContainerClass
MobileInstallationCopySafeHarborsForContainerClass
MIEnumerateContainersOfClass_block_invoke
Unable to set F_NOCACHE accessing file %s %s
Failed to remove %s : %s
Unknown: %ld
Start (Asynch)
iTunesArtworkData
Install (New)
%d: %@
com.apple.mobileinstallation_client
Data
appex
stashMode
Connection was interrupted before all delegate messages were received
v24@?0@8@\"NSError\"16
com.apple.private.webkit.pushbundle
LinkedParentBundleID
Warning, couldn't initialize xpc connection to %@
Property %s did not match
-[MIInstallerClient pidForTesting]_block_invoke
v24@?0@\"MIAppReference\"8@\"NSError\"16
Attempting to purge container class %llu for identifier %@ at %@
MIGetBooleanEntitlement
data-protection-class
app reference is nil
MobileInstallationRegisterPlaceholderForReference
com.apple.developer.accessory-transport-extension
-[MIInstallerClient uninstallIdentifiers:withOptions:completion:]_block_invoke_3
com.apple.security.system-group-containers
_PurgeExpendableDataContainerContent
com.apple.AppClips
PluginKitPlugin
containers
com.apple.install_session_uuid
Proxy returned error: %@
+ %lld; Freed %lld bytes, need %lld bytes
Enumerating containers of class %llu returned error %@
_OffloadApps
MIFinalizeReferenceForInstalledAppWithError
%s is no longer implemented
MobileInstallationRemoveSafeHarborForContainerClassWithIdentity_block_invoke
MobileInstallationAppLaunchEnabled
FATAL ERROR: failed to locate and reset the LS database; purging apps is not possible
referenceUUID
InfoPlist.strings
-[MIPlaceholderConstructor _copyStringsToPlaceholder:onlyDirectories:error:]
Skipping offload of TestFlight app %@ at %@
%s (%s) : %s
-[MIPlaceholderConstructor _entitlementsForPath:error:]
-[MIHelperServiceFrameworkClient purgeInstallCoordinationPromiseStagingDirectoryForUUID:keepStagingDirectory:error:]
%s is not available on this platform!
skipWatchAppInstall
performAPFSClone
-[MIInstallerClient init]_block_invoke_2
MobileInstallationRevertApplicationWithIdentityAndAssertionBlockWithError
MobileInstallationICLRecordsUninstallForInstallCoordinationWithError
false
stagedIdentifier
iTunesArtwork
Failed to read migration prefs from %@ : %@
-[MIInstallerClient endTestMode:]
com.apple.developer.homekit
Bundle
v24@?0@\"MIStagingLocation\"8@\"NSError\"16
App with identifier %@ at %@ does not have an itemID in its metadata so it's not restorable
Destruction
Failed to assume _installd identity: %@
allowDistributorChange
com.apple.developer.parent-application-identifiers
Don't know how to create a path to containers of type %llu
Failed to count the files and bytes in archive : %d (%s)
Intent
true
provisioningProfiles
DowngradeToPlaceholder
Returning %lld freed bytes (goal was %lld bytes)
AppClips
Failed to count files and bytes in the archive at %@ : %@
NSExtension
v8@?0
AllowInstallLocalProvisioned
keychain-access-groups
Failed to load Info.plist from %@
Failed to copy InfoPlist.strings from \"%@\" to \"%@\"
LegacyErrorString
PlaceholderBundleTypeEmbeddedWatchApp
Dictionary serialization of MIInstallOptions.installationRequestorAuditToken is not available; dropping this option.
-[MIInstallerClient revertForLSWithIdentifier:withOptions:completion:]_block_invoke_3
MobileInstallationInstallApp
Encountered error while enumerating %@ to copy strings
MIInvalidateReferenceForInstalledAppWithError
com.apple.security.system-groups
LSCounterpartIdentifiers
LSInstallType
_ProcessApp
Failed to end test mode: %@
MobileInstallationLookupSystemAppState_block_invoke
MobileInstallationRegisterContentsOnOSModuleAtURL_block_invoke
uid
SBIconMasqueradeIdentifier
BOMCopier signaled file error on %s : %s
Removed LaunchServices database to force rebuild
Failed to write updated bundle metadata to %@ : %@ [ignoring]
Start
Install (Unknown Type)
-[MIPlaceholderConstructor _materializeConstructors:intoBundle:error:]
MobileInstallationCancelUpdateForStagedIdentifiersWithError
MobileInstallationRegisterContentsOnRoot_block_invoke
com.apple.developer.on-demand-install-capable
com.apple.private.pluginkit.persona
WKWatchOnly
Not including icon content because IFCaptureIconContent is not available
B32@?0@\"NSURL\"8@\"NSString\"16@\"NSDictionary\"24
Failed to read iTunesMetadata for app with identifier %@ from %@ : %@
Failed to clean up temp offloaded bundle at %@ : %@
MobileInstallationRemoveSafeHarborForContainerClassWithIdentity
Failed to get legacy error string from NSError's userInfo
com.apple.developer.memory.transfer-send
fsync failed for %s : %s (%d)
MobileInstallationWatchKitInstallerSnapshotWKApp_block_invoke
Failed to set mode to 0%o for %s : %s
Bundle at %@ has no icon
%d: %@ (%@:%ld %@)
ProvisioningProfiles
Got post-traversal for directory %s
-[MIPlaceholderConstructor _initWithSource:byPreservingFullInfoPlist:forBundleType:error:]
developerInstall
Attempting to offload %@ at %@
com.apple.developer.default-data-protection-if-available
Failed to check test mode: %@
[uuid:%@ identity:%@ domain:%lu uid:%u]
Freed %lld bytes by removing %s
Did not find %@ key in DataMigration prefs set, or it was not set to a string value
v24@?0@\"MIBundleMetadata\"8@\"NSError\"16
MobileInstallationStageApplicationUpdate
Failed to read metadata dictionary from %@ : %@
Unknown Phase
The provided placeholder type of %@ does not match the path extension for the bundle at %@
App with identifier %@ at %@ is missing the purchasing Apple ID in its metadata so it's not restorable
Placeholder for %@ used %lld bytes, but removing the app freed only %lld bytes
%s is unavailable on this platform
com.apple.private.rating-rank-eligibility-domain
Uninstall (Placeholder)
-[MIInstallerClient enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:]_block_invoke_3
MobileInstallationUpdateiTunesMetadataForInstallCoordination_block_invoke
LSApplicationLaunchProhibited
isDeveloperInstall
app
-[MIInstallerClient installParallelPlaceholderForStagedIdentifier:fromURL:returningResultInfo:completion:]_block_invoke_3
Error
platform-application
com.apple.developer.memory.transfer-accept
open failed for %s : %s
Failed to issue write barrier for %s : %s (%d)
extractPKZip
Install (Placeholder Update)
Failed to construct SecStaticCode for %@ : %d
BOMCopier signaled fatal file error on %s : %s
Called with dataVolumeRootPath=\"%s\"; purgeTmpAndCaches:%c; effort:%llu; bytesToFree:%lld
Re-throwing exception: %@
MIIsValidPersonaLifecycleEventType
_CopySafeHarborsForContainerClass_block_invoke
EXAppExtensionAttributes
-[MIPlaceholderConstructor _loadInfoPlistContentWithError:]
com.apple.mock.Playgrounds
write() returned %zd but we expected %lu when writing to %s
CF_MIEmergencyOffloadVersion
B24@?0^{?=QqQ*Q*QIIIIIIISBC}8^B16
StaticDiskUsage
-[MIPlaceholderConstructor _writeIconToPlaceholder:infoPlistIconContent:error:]
Failed to create metadata from plist data: %@
com.apple.developer.web-browser-engine.host
.com.apple.mobile_container_manager.metadata.plist
Uninstall (Application)
alternateIconName
WaitForStorageDeletion
_PurgeDirectory_block_invoke
B20@?0@\"NSURL\"8C16
com.apple.mobile.installd
v24@?0@\"NSDictionary\"8@\"NSError\"16
com.apple.developer.embedded-web-browser-engine
Entitlement %@ does not contain supported types; ignoring.
com.apple.migration.plist
v16@?0@\"NSDictionary\"8
_MICommonCopyGroupEntitlement
linkedParentBundleID
com.apple.developer.browser.app-installation
Executable
PackageExtractionFailed
-[MIHelperServiceFrameworkClient createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:]
Freed %lld bytes by offloading app %@
MobileInstallationClearUninstalled_block_invoke
UIRequiredDeviceCapabilities
-[MIInstallOptions legacyOptionsDictionary]
Skipping offload of marketplace %@ at %@
com.apple.developer.associated-appclip-app-identifiers
app reference has nil app identity
@a
PlaceholderBundleTypeApp
Got error while enumerating CONTAINER_CLASS_SYSTEM_DATA looking for the %@ container: %@
MobileInstallationLookupUninstalled_block_invoke
App with identifier %@ at %@ has deviceBasedVPP = YES in its metadata so it's not restorable
userInitiated
Removed data migration prefs to force migration on next boot
Application
_installd
The options parameter is currently unused and must be nil
The persona parameter must be specified
Stage (New Update)
SecCodeCopySigningInformation for %@ returned error %d
geoJSONData
PackageType
NULL
Freed %lld bytes by purging tmp in container class %llu for identifier %@
com.apple.developer.web-browser-engine.rendering
com.apple.developer.home
Found no keys in Info.plist in bundle at %@
-[MIHelperServiceFrameworkClient stagingLocationForSystemContentWithinSubsystem:error:]_block_invoke
Construction
+[MIAppReference validateAppReference:withError:]
Failed to getclass of file %s: %s
Failed to create destination lproj directory at \"%@\"
Extensions
lsInstallType
PersonaUniqueStringForInstall
Caches
_IsRestorableAppBasedOnMetadata
Bundle ID supplied to revert was nil.
PlaceholderBundleTypePlugInKit
Watch
allowLocalProvisioned
PreservePlaceholderAsParallel
_RemovefileErrorCallback
Got error while enumerating CONTAINER_CLASS_INTERNAL_DAEMON_DATA looking for the %@ container: %@
Offloading non-Apple apps...
com.apple.developer.web-browser
Install (Parallel Placeholder)
-[MIHelperServiceFrameworkClient stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:]_block_invoke
-[MIHelperServiceFrameworkClient setTestingEnabled:error:]_block_invoke
installIntent
Q
Unknown PlaceholderBundleType value %lu
stagedDiskUsage
-[MIInstallOptions initWithLegacyOptionsDictionary:]
App with identifier %@ at %@ has sideLoadedDeviceBasedVPP = YES in its metadata so it's not restorable
MobileInstallationUpdateSinfDataForInstallCoordinationWithWrapperURL
Unknown type %ld passed for identifier; contains %@
InternalDaemon
Install (Promote From Placeholder)
+[MIBOMWrapper _countFilesAndBytesInArchiveAtURL:withBOMCopier:totalFiles:totalUncompressedBytes:error:]
-[MIHelperServiceFrameworkClient _remoteObjectProxyWithErrorHandler:]
App with identifier %@ at %@ is missing the altDSID in its metadata so it's not restorable
-[MIHelperServiceFrameworkClient stagingLocationForUserContentWithinSubsystem:error:]_block_invoke
GeoJSON
-[MIInstallerClient getTestModeEnabled:outError:]
swift-playgrounds
com.apple.install_uuid
Failed to get the path to containers of class %llu in %@
Library
Failed to write updated migration prefs to %@ : %@
AITransactionLog.m
com.apple.MobileInstallationHelperService
ServiceConnectionInterrupted
Success
%{public}@/%{public}@:%lu:%lu:%lu:%u:%{public}@
%s:%s:%s:%ld:%s:%s
MIInstallOptions
MobileInstallerDelegateProtocol
AITransactionLog
MIAppReference
MobileInstallationAdditions
MIPlaceholderConstructor
MobileInstallerProtocol
NSCopying
MobileInstallationHelperServiceProtocol
MIInstallerClient
MIStagedUpdateMetadata
NSSecureCoding
MIBOMWrapper
MIHelperServiceFrameworkClient
MICandidateAppContainer
NSCoding
MICandidateContainer
longLongValue
registerContentsOnOSModuleAtURL:completion:
setSkipWatchAppInstall:
code
fetchListOfAppsRequiringPreInstallConsent:
hasPrefix:
installTypeSummaryString
setTestMode:
altDSID
bundleID
isAppleApp
setAppReplacementStatus:forApp:replacingApp:completion:
uninstallIdentifiers:withOptions:completion:
userInfo
initWithContainerURL:identifier:metadata:
metadataFromPlistData:error:
migrateMobileContentWithCompletion:
MI_URLByAppendingPathComponents:lastIsDirectory:
T@\"NSDictionary\",R,C,N,V_metadata
enumerateKeysAndObjectsUsingBlock:
setInstallIntent:
TQ,N,V_installLocation
length
metadataFromURL:error:
stagingLocationForUserContentWithinSubsystem:completion:
systemAppInstall
unregisterContentsOnRoot:deferUntilNextBoot:completion:
dealloc
TB,N,V_performPlaceholderInstallActions
_performPlaceholderInstallActions
handleFailureInMethod:object:file:lineNumber:description:
stringWithUTF8String:
T@\"NSXPCConnection\",&,N,V_connection
TB,N,V_basicIOSPlaceholderForWatchOSLessThanSix
TB,N,V_preserveTargetBundleName
TB,N,GisDeveloperInstall,V_developerInstall
TB,N,V_allowDistributorChange
dataForExtendedAttributeNamed:length:fromURL:error:
dictionaryWithCapacity:
autoInstallOverride
MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:
removeDeveloperAppAtURL:error:
setWaitForDeletion:
setWithObject:
_defaultLog
referenceUUID
createSafeHarborWithIdentifier:forPersona:containerType:andMigrateDataFrom:completion:
installURL:identity:targetingDomain:options:returningResultInfo:completion:
resolveStagingBaseWithSandboxExtensionForVolumeUUID:withinStagingSubsystem:completion:
_sinfData
allStagingLocationsWithinSubsystem:completion:
dataWithBytes:length:
mutableCopy
setLinkedParentBundleID:
enumerateAppBundleRecord:error:
_iTunesMetadata
_initWithLog:
_isWatchKitExtension
errorWithDomain:code:userInfo:
infoPlistContent
linkedBundleIDsForAppIdentity:withCompletion:
setConnection:
delegatesCompleteError
reconcileContentsOnKnownOSModules:completion:
setPersonas:forApp:inDomain:withCompletion:
unregisterContentsForDiskImageAtURL:completion:
T@\"NSURL\",&,N,V_appURL
TB,N,V_delegatesComplete
_allowLocalProvisioned
_infoPlistContent
uninstallRecordArrayToDictionary:
unsignedIntegerValue
T@\"NSString\",C,N,V_alternateIconName
_installationRequestorAuditToken
iTunesMetadata
installMacDeveloperAppAtURL:toURL:targetURLType:error:
sideLoadedDeviceBasedVPP
sinfData
installURL:identity:targetingDomain:withOptions:returningResultInfo:completion:
makeSymlinkFromAppDataContainerToBundleForIdentifier:forPersona:completion:
revertForLSWithIdentifier:withOptions:completion:
T@\"MIPlaceholderConstructor\",R,N
_delegatesCompleteCond
_invalidateObject
metadata
setBundleIdentifier:
T@\"NSString\",C,N,V_bundleIdentifier
T@?,C,N,V_appDictionaryEnumBlock
embeddedWatchAppPlaceholderConstructors
installUUID
MI_writeToURL:format:options:error:
T@\"NSData\",C,N,V_iTunesArtworkData
addPersona:toApp:inDomain:withCompletion:
lastPathComponent
_remoteObjectProxyWithErrorHandler:
appExtensionPlaceholderConstructors
personaUniqueString
resume
setReleaseTerminationAssertBlock:
updateSystemAppStateForIdentifier:appState:completion:
T@\"NSString\",R,C,N,V_identifier
T^{?=[8I]},N,V_installationRequestorAuditToken
_installUUID
_referenceUUID
registerContentsOnRoot:deferUntilNextBoot:completion:
registerPlaceholderForReference:completion:
scannerWithString:
TQ,N,V_lsInstallType
_materializeConstructors:intoBundle:error:
setInstallSessionUUID:
setPlaceholderType:
updateiTunesMetadataForIXWithIdentifier:metadata:completion:
_loadInfoPlistContentWithError:
T@\"NSString\",C,N,V_linkedParentBundleID
_sinfDataType
_bundleIdentifier
_bundleURL
setAlternateIconName:
setInstallLocation:
_entitlementsForPath:error:
_identifier
_installTargetType
logScenario:step:success:forBundleID:description:
removeItemAtURL:error:
_stashMode
characterSetWithRange:
createDirectoryAtURL:withIntermediateDirectories:mode:class:error:
setSinfData:
setXpcConnection:
_includeWatchAppPlaceholders
setInstallTargetType:
T@\"NSArray\",C,N,V_provisioningProfiles
_linkedParentBundleID
_queue
defaultWorkspace
delegateMessageDeliveryCompleteWithError:
iTunesArtworkData
getPidForTestingWithCompletion:
initWithLegacyOptionsDictionary:
_appExtensionPlaceholderConstructors
_geoJSONData
_lsInstallType
finalizeReference:withCompletion:
scanInt:
setUserInitiated:
UUID
_identity
addEntriesFromDictionary:
setRemoteObjectInterface:
MI_writeAtomicallyToURLMatchingCurrentFileMetadata:format:error:
setInstallType:
TB,N,V_skipWatchAppInstall
_populateAppExtensionPlaceholderConstructorsWithError:
diskUsageForURL:
initializeWithLog:
registerSafeHarborAtPath:forIdentity:ofType:withOptions:completion:
setIncludeWatchAppPlaceholders:
T@\"NSURL\",&,N,V_bundleURL
encodeBool:forKey:
invalidateReference:withCompletion:
removeObjectForKey:
revertIdentity:withOptions:completion:
_performAPFSClone
estimatedSize
itemExistsAtURL:error:
markBundleAsPlaceholder:withError:
setClasses:forSelector:argumentIndex:ofReply:
updatePlaceholderMetadataForApp:installType:failureReason:underlyingError:failureSource:completion:
T@\"NSData\",&,N,V_installSessionUUID
installationRequestorAuditToken
URLByAppendingPathComponent:isDirectory:
_embeddedAppClipPlaceholderConstructors
isLaunchProhibited
sinfDataType
updateWrappedAppAt:forInstalledBundleIdentifier:containerURL:installationRecords:onBehalfOf:error:
setInstallUUID:
T@\"NSURL\",R,N,V_rootURL
_synchronousRemoteObjectProxyWithErrorHandler:
_systemAppInstall
installForMigrator
linkedParentBundleID
performAPFSClone
setEmbeddedWatchAppPlaceholderConstructors:
lookupSystemAppStateWithOptions:completion:
materializeIntoBundleDirectory:error:
setIsWatchKitExtension:
stagingURLWithSandboxExtensionForSystemContentWithinSubsystem:completion:
T@\"NSString\",C,N,V_personaUniqueString
_provisioningProfileInstallFailureIsFatal
appBundleRecordEnumBlock
TB,R
allObjects
embeddedAppClipPlaceholderConstructors
removePersona:fromApp:inDomain:withCompletion:
setProvisioningProfiles:
allStagedUpdatesWithCompletion:
delegatesComplete
itemID
numberWithUnsignedInt:
setExportedInterface:
setTestModeForIdentifierPrefix:testMode:error:
_installIntent
firstNetworkExtension
numberWithUnsignedInteger:
raiseException
rebuildBuiltInContentMappingWithCompletion:
setBasicIOSPlaceholderForWatchOSLessThanSix:
setEligibilityTestOverrides:withError:
setITunesMetadata:
placeholderType
rootURL
TB,N,V_allowLocalProvisioned
defaultManager
diskUsageForLaunchServicesWithBundleIDs:options:withError:
initForStagedIdentifier:diskUsage:
invalidate
setInterruptionHandler:
_userInitiated
dieForTesting
releaseTerminationAssertion
setProgressBlock:
setTestModeForIdentifierPrefix:testMode:validationData:
TB,R,N
clearUninstalledIdentifiers:withOptions:completion:
personasForBundleID:inDomain:withCompletion:
setInstallBuildVersion:
setTestModeForIdentifierPrefix:testMode:validationData:error:
T@\"NSArray\",C,N,V_embeddedWatchAppPlaceholderConstructors
entitlements
fetchDiskUsageForIdentifiers:withOptions:completion:
preserveFullInfoPlist
setLaunchWarningForApp:withUniqueInstallIdentifier:warningData:completion:
UUIDString
createAppSnapshotWithBundleID:snapshotToURL:onlyV1AppIfPresent:placeholderOnly:completion:
propertyListDataWithError:
stageInstallURL:identity:targetingDomain:withOptions:completion:
_watchKitExtensionPlaceholderConstructor
acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:completion:
compare:
itemExistsAtURL:
endTestMode:
setStashMode:
skipBlacklist
MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:error:
invalidateReference:completion:
isPlaceholder
setEligibilityTestOverrides:withCompletion:
synchronousRemoteObjectProxyWithErrorHandler:
_appURL
_releaseTerminationAssertBlock
decodeObjectOfClasses:forKey:
fetchInfoForFrameworkAtURL:options:completion:
getAppMetadataForApp:completion:
T@\"NSError\",&,N,V_delegatesCompleteError
T@\"NSString\",&,N,V_bundleDirectoryName
TI,R,N,V_uid
setSkipBlacklist:
stagedIdentifier
init
metadataFromPlistAtURL:error:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
T@\"NSString\",R,C,N
clearTestFlags:withError:
copy
initWithBundleID:
initWithReferenceUUID:identity:domain:uid:
isWatchKitExtension
performPlaceholderInstallActions
T@\"NSArray\",C,N,V_embeddedAppClipPlaceholderConstructors
TB,N,V_includeAppClipPlaceholders
_installForMigrator
bundleAtURLIsPlaceholder:
bytes
setTestingEnabled:
stageItemAtURL:toStagingLocation:options:completion:
_allowDistributorChange
pidForTesting
setAppDictionaryEnumBlock:
setExportedObject:
setLaunchProhibited:forApp:withCompletion:
currentHandler
enrollPersona:forApps:inDomain:withCompletion:
finalizeReference:completion:
systemAppMigratorHasCompleted:
watchKitExtensionPlaceholderConstructor
TB,N,V_waitForDeletion
decodeBoolForKey:
initWithServiceName:
legacyOptionsDictionary
setSystemAppMigrationComplete:
supportsSecureCoding
removeMacAppWithBundleID:atURL:error:
reportPersonaLifecycleEventForUniqueString:eventType:withCompletion:
allStagingLocationsWithinSubsystem:error:
T@\"MIAppIdentity\",R,N,V_identity
_log
clearTestFlags:withCompletion:
enumerateAppDictionary:error:
finalizeStagedInstallForIdentifier:returningResultInfo:completion:
isSystemAppInstall
setSystemAppInstall:
stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:completion:
isUserInitiated
_delegatesComplete
cancelUpdateForStagedIdentifiers:completion:
enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:
setGeoJSONData:
setInstallDate:
createWrappedAppForInstalledBundleIdentifier:containerURL:inTargetDirectory:installationRecords:bundleDirectoryName:onBehalfOf:error:
_preservePlaceholderAsParallel
installerWithAppBundleRecordEnumerator:
removeDataSeparatedAppsWithBundleIDs:fromPersona:withCompletion:
stagingLocationForUserContentWithinSubsystem:error:
_domain
TB,N,V_includeWatchAppPlaceholders
progressBlock
setPreserveFullInfoPlist:
setTestingEnabled:error:
T@\"NSData\",C,N,V_geoJSONData
setAllowDistributorChange:
setInstallForMigrator:
setTestFlags:withError:
T@\"NSDictionary\",&,N,V_infoPlistContent
appDictionaryEnumBlock
setAllowLocalProvisioned:
waitForSystemAppMigratorWithCompletion:
T@\"NSArray\",C,N,V_appExtensionPlaceholderConstructors
T@\"MIPlaceholderConstructor\",&,N,V_watchKitExtensionPlaceholderConstructor
validateAppReference:withError:
_metadata
installParallelPlaceholderForStagedIdentifier:fromURL:returningResultInfo:completion:
personasForBuiltInBundleID:withCompletion:
userInitiated
waitForSystemAppMigratorToComplete:
setWithObjects:
uid
_installSessionUUID
dataWithBytesNoCopy:length:freeWhenDone:
developerInstall
fetchInfoForContainerizedAppWithBundleID:options:completion:
initWithMachServiceName:options:
numberWithUnsignedLongLong:
TB,N,GisSystemAppInstall,V_systemAppInstall
objectForKeyedSubscript:
setStagedIdentifier:
stagingLocationForInstallLocation:withinStagingSubsystem:usingUniqueName:error:
_writeInfoPlistToPlaceholder:substitutingIconContent:withError:
_basicIOSPlaceholderForWatchOSLessThanSix
_includeAppClipPlaceholders
encodeWithCoder:
isDeveloperInstall
setAppExtensionPlaceholderConstructors:
setAutoInstallOverride:
setByAddingObject:
T@\"NSXPCConnection\",&,N,V_xpcConnection
_appDictionaryEnumBlock
createDirectoryAtURL:withIntermediateDirectories:mode:error:
lookupUninstalledWithOptions:completion:
_developerInstall
checkCapabilities:withOptions:completion:
setLsInstallType:
setWithArray:
TB,N,V_performAPFSClone
TQ,N,V_installTargetType
_copyInfoPlistLoctableToPlaceholder:error:
setEmbeddedAppClipPlaceholderConstructors:
setEntitlements:
bundleRecordArrayToInfoDictionaryArray:
getTestModeWithCompletion:
itemDoesNotExistAtURL:
setInfoPlistContent:
unregisterContentsOnOSModuleAtURL:completion:
updateSinfForIXWithIdentifier:withOptions:sinfData:completion:
_personaUniqueString
_uid
createWrappedAppForInstalledBundleIdentifier:containerURL:atTargetURL:installationRecords:onBehalfOf:error:
installerWithProgressBlock:
isEqual:
stagingLocationForSystemContentWithinSubsystem:error:
initWithEmbeddedWatchAppSource:byPreservingFullInfoPlist:error:
appBundleIDsWithPersona:inDomain:withCompletion:
countByEnumeratingWithState:objects:count:
registerContentsForDiskImageAtURL:completion:
setInstallationRequestorAuditToken:
T@\"NSString\",C,N,V_stagedIdentifier
releaseTerminationAssertBlock
setDelegatesCompleteError:
extractZipArchiveAtURL:toURL:withError:
installTargetType
logStep:byParty:phase:success:forBundleID:description:
setIncludeAppClipPlaceholders:
.cxx_destruct
TB,N,GisUserInitiated,V_userInitiated
TI,N,V_sinfDataType
arrayWithCapacity:
cloneItemAtURL:toURL:onBehalfOf:completion:
domain
setDelegatesComplete:
dictionaryWithContentsOfURL:error:
installSessionUUID
pathExtension
setPerformPlaceholderInstallActions:
sortUsingComparator:
stringWithFormat:
TB,N,V_installForMigrator
_entitlements
bundleIdentifier
initWithFormat:arguments:
validateAppIdentity:withError:
extractZipArchiveAtURL:toURL:withError:extractionProgressBlock:
TB,N,V_provisioningProfileInstallFailureIsFatal
TQ,N,V_placeholderType
_preserveTargetBundleName
enumerateInstalledAppsWithOptions:usingLegacyDictionary:completion:
MI_dictionaryWithContentsOfURL:options:error:
referencesForBundleWithIdentifier:inDomain:completion:
sharedInstance
_provisioningProfiles
_transferAndUpdateInstallSessionIDsToPlaceholder:error:
isEqualToString:
logStep:byParty:phase:success:forBundleID:persona:description:
setTestModeWithCompletion:
unsignedIntValue
Tq,R,N
UTF8String
fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
removeAppReplacementStateForApp:completion:
serializeToURL:error:
setBundleDirectoryName:
T@\"NSString\",R,N
includeAppClipPlaceholders
setTestFlags:withCompletion:
wipeStagingRootAndSetUpPerUserDataDirWithCompletion:
listSafeHarborsOfType:forPersona:withOptions:completion:
setAppURL:
T@\"NSUUID\",R,N,V_referenceUUID
_rootURL
_skipBlacklist
_writeIconToPlaceholder:infoPlistIconContent:error:
identity
stagingLocationForURL:withinStagingSubsystem:usingUniqueName:completion:
MI_writeAtomicallyToURL:withMode:owner:group:error:
TQ,N,V_autoInstallOverride
decodeObjectOfClass:forKey:
moveItemInStagingLocation:atRelativePath:toDestinationURL:onBehalfOf:completion:
setObject:forKeyedSubscript:
setProvisioningProfileInstallFailureIsFatal:
initWithSource:byPreservingFullInfoPlist:error:
preserveTargetBundleName
allowLocalProvisioned
arrayWithObjects:count:
setData:forExtendedAttributeNamed:onURL:error:
setPerformAPFSClone:
setQueue:
stringWithFileSystemRepresentation:length:
stagedDiskUsage
_appBundleRecordEnumBlock
TQ,N,V_stashMode
_waitForDeletion
fileSystemRepresentation
purgeInstallCoordinationPromiseStagingDirectoryForUUID:keepStagingDirectory:error:
raiseExceptionWithCompletion:
referencesForBundleWithIdentifier:inDomain:withCompletion:
setPersonaUniqueString:
uninstallIdentity:withOptions:completion:
allocWithZone:
interfaceWithProtocol:
purchaserID
remoteObjectProxyWithErrorHandler:
stashMode
unsignedLongLongValue
_countFilesAndBytesInArchiveAtURL:withBOMCopier:totalFiles:totalUncompressedBytes:error:
setDeveloperInstall:
fetchInfoForContainerizedAppWithIdentity:inDomain:options:completion:
setPreservePlaceholderAsParallel:
reportProgress:
TB,N,V_skipBlacklist
_delegatesCompleteError
encodeObject:forKey:
installIntent
path
TB,N,V_preserveFullInfoPlist
installerWithProgressBlock:releaseTerminationAssertionBlock:
prepareReplacementOfApp:byApp:extensionBundleIDs:withCompletion:
provisioningProfileInstallFailureIsFatal
pushReplacementInfoForApp:replacingApp:withCompletion:
_copyStringsToPlaceholder:onlyDirectories:error:
_stagedDiskUsage
setInvalidationHandler:
TQ,R,N,V_domain
_autoInstallOverride
_infoPlistKeysToLoad
_logScenario:step:success:forBundleID:persona:description:
_progressBlock
alternateIconName
provisioningProfiles
queue
_alternateIconName
_constructPlaceholdersForDirectory:itemsWithPathExtension:appendingToArray:bundleType:error:
includeWatchAppPlaceholders
triggerRegistrationForContainerizedContentForOptions:withCompletion:
TQ,N,V_installIntent
boolValue
count
endAppReplacementWithStatus:forApp:completion:
T@\"NSData\",C,N,V_sinfData
T@\"NSDictionary\",C,N,V_entitlements
_waitForPendingDelegateMessages
numberWithInt:
setAppBundleRecordEnumBlock:
setPreserveTargetBundleName:
storeListOfAppsRequiringPreInstallConsent:completion:
TB,N,V_preservePlaceholderAsParallel
_populateEmbeddedAppClipPlaceholderConstructorsWithError:
acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:withCompletion:
connection
T@?,C,N,V_releaseTerminationAssertBlock
_delegatesCompleteCondMutex
addDataSeparatedAppsWithBundleIDs:toPersona:withCompletion:
isDataContainerEmpty:ofContainerType:completion:
now
TB,N,V_isWatchKitExtension
initWithCoder:
setDataSeparatedAppsWithBundleIDs:withPersona:withCompletion:
installLocation
T@\"NSDictionary\",R,C,N
TQ,N,V_stagedDiskUsage
basicIOSPlaceholderForWatchOSLessThanSix
hash
setSinfDataType:
sortedArrayUsingComparator:
bundleURL
description
serviceName
skipWatchAppInstall
containsObject:
_skipWatchAppInstall
setStagedDiskUsage:
scanCharactersFromSet:intoString:
xpcConnection
_embeddedWatchAppPlaceholderConstructors
_iTunesArtworkData
_installLocation
_introspectWithError:
getTestModeEnabled:outError:
triggerRegistrationForDiskImageContentForOptions:withCompletion:
_populateEmbeddedWatchAppPlaceholderConstructorsWithError:
_sharedConnection
geoJSONData
preservePlaceholderAsParallel
snapshotWKAppInCompanionAppID:toURL:options:completion:
stagingLocationForSystemContentWithinSubsystem:completion:
addObject:
copyItemAtURL:toURL:error:
stagingURLWithSandboxExtensionForUserContentWithinSubsystem:completion:
URLForDirectory:inDomain:appropriateForURL:create:error:
deviceBasedVPP
endTestModeWithCompletion:
stagingLocationForURL:withinStagingSubsystem:usingUniqueName:error:
T@?,C,N,V_appBundleRecordEnumBlock
_bundleDirectoryName
migrationPlistURL
allowDistributorChange
waitForDeletion
_preserveFullInfoPlist
bundleDirectoryName
identifier
lsInstallType
appleID
T@\"MIStoreMetadata\",C,N,V_iTunesMetadata
removeSafeHarborForIdentity:ofType:withOptions:completion:
setITunesArtworkData:
MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:
_connection
_stagedIdentifier
_xpcConnection
setBundleURL:
installerWithAppDictionaryEnumerator:
T@\"NSData\",&,N,V_installUUID
_initWithSource:byPreservingFullInfoPlist:forBundleType:error:
_placeholderType
cloneSerializedPlaceholderForInstalledAppWithBundeID:personaUniqueString:atResultURL:withCompletion:
copyWithZone:
setWatchKitExtensionPlaceholderConstructor:
volumeUUIDForURL:completion:
T@?,C,N,V_progressBlock
appURL
@32@0:8@16Q24
I
@\"NSObject<OS_os_log>\"
@\"MIAppIdentity\"
v48@0:8Q16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSArray\"@\"NSError\">40
v48@0:8@\"NSString\"16@\"NSURL\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v48@0:8@\"NSString\"16@\"NSSet\"24Q32@?<v@?@\"NSError\">40
v48@0:8@16@24@32@?40
v56@0:8@\"NSString\"16@\"NSString\"24Q32@\"NSURL\"40@?<v@?@\"NSError\">48
v24@0:8@\"NSError\"16
v60@0:8@16@24Q32@40B48@?52
v20@0:8I16
@\"NSData\"
@\"NSArray\"
B24@0:8^@16
@\"NSError\"
@\"MIPlaceholderConstructor\"
@16@0:8
v32@0:8@\"NSURL\"16@?<v@?@\"NSUUID\"@\"NSError\">24
v44@0:8@16@24B32@?36
v36@0:8@16i24@?28
i16@0:8
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?@\"NSError\">32
v48@0:8@\"NSString\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40
@24@0:8^{_NSZone=}16
v32@0:8@\"NSDictionary\"16@\"NSError\"24
{_opaque_pthread_cond_t=\"__sig\"q\"__opaque\"[40c]}
@?
B56@0:8@16@24@32Q40^@48
v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32
v40@0:8@\"MIAppIdentity\"16@\"MIAppIdentity\"24@?<v@?@\"NSError\">32
v60@0:8Q16Q24Q32B40@44@52
v72@0:8@\"NSURL\"16@\"NSURL\"24{?=[8I]}32@?<v@?@\"NSError\">64
v40@0:8Q16@24@?32
@\"NSDictionary\"
B40@0:8@16^@24^@32
v48@0:8@\"MIAppIdentity\"16Q24@\"NSDictionary\"32@?<v@?@\"NSError\">40
B28@0:8B16^@20
B24@0:8@16
v32@0:8Q16@?<v@?@\"NSError\">24
@\"MIStoreMetadata\"
@32@0:8@?16@?24
B44@0:8@16S24I28I32^@36
@36@0:8@16B24^@28
v48@0:8@\"NSSet\"16@\"NSString\"24Q32@?<v@?@\"NSError\">40
@\"NSXPCConnection\"
v48@0:8@16@24B32B36@?40
v48@0:8@\"NSString\"16@\"NSURL\"24B32B36@?<v@?@\"NSDictionary\"@\"NSError\">40
v48@0:8@16@24Q32@?40
v56@0:8@\"NSString\"16@\"MIAppIdentity\"24Q32@\"NSDictionary\"40@?<v@?@\"NSError\">48
v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSData\"32@?<v@?@\"ICLSinfInfo\"@\"NSError\">40
v20@0:8B16
v36@0:8@\"NSSet\"16B24@?<v@?@\"NSError\">28
v40@0:8@\"NSString\"16@\"MIStoreMetadata\"24@?<v@?@\"NSError\">32
v48@0:8@\"MIAppIdentity\"16@\"NSData\"24@\"NSData\"32@?<v@?@\"NSError\">40
v32@0:8Q16@?<v@?@\"MIStagingLocation\"@\"NSError\">24
@40@0:8@16@24@32
v40@0:8@\"NSString\"16Q24@?<v@?@\"NSDictionary\"@\"NSError\">32
v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32
v16@0:8
v48@0:8@\"<MILocationProtocol>\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40
v48@0:8Q16@24@32@?40
v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24
Q16@0:8
v24@0:8@\"NSDictionary\"16
@?16@0:8
{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}
v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24
v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSError\">24
v80@0:8@16@24@32{?=[8I]}40@?72
v48@0:8@\"NSURL\"16Q24@\"NSString\"32@?<v@?@\"MIStagingLocation\"@\"NSError\">40
Q
v60@0:8@16Q24B32@36@44@52
v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24
@24@0:8@\"NSCoder\"16
B48@0:8@16Q24@32^@40
^{?=[8I]}16@0:8
I16@0:8
B
v48@0:8@16Q24@32@?40
v24@0:8@?<v@?i>16
v64@0:8@16Q24Q32@40Q48@?56
B48@0:8@16@24^@32@?40
B56@0:8@16^{_BOMCopier=}24^Q32^Q40^@48
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32
v32@0:8Q16@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">24
v40@0:8@\"NSString\"16Q24@\"NSDictionary\"32
v32@0:8@16@24
v60@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40B48@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">52
v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24
B40@0:8@16Q24^@32
v24@0:8^{?=[8I]}16
v40@0:8@16Q24@32
v80@0:8@\"MIStagingLocation\"16@\"NSString\"24@\"NSURL\"32{?=[8I]}40@?<v@?@\"NSError\">72
v32@0:8Q16@?<v@?@\"NSSet\"@\"NSError\">24
B32@0:8^B16^@24
B52@0:8@16S24I28I32i36B40^@44
v56@0:8@\"NSURL\"16@\"MIAppIdentity\"24Q32@\"MIInstallOptions\"40@?<v@?@\"MIStagedUpdateMetadata\"@\"NSError\">48
@88@0:8@16@24@32@40{?=[8I]}48^@80
^{?=[8I]}
@\"NSURL\"
v72@0:8@16@24{?=[8I]}32@?64
v52@0:8@16Q24B32@36@44
v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">32
v40@0:8@\"MIAppIdentity\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32
v40@0:8@\"NSURL\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"@\"NSError\">32
v48@0:8Q16@\"MIAppIdentity\"24@\"MIAppIdentity\"32@?<v@?@\"NSError\">40
v32@0:8@\"MIAppReference\"16@?<v@?@\"NSError\">24
@48@0:8@16@24Q32^@40
B32@0:8@16^@24
@48@0:8@16Q24@32^@40
v40@0:8@16Q24@?32
v32@0:8@16@?24
v48@0:8@\"NSURL\"16@\"MIStagingLocation\"24@\"MIInstallOptions\"32@?<v@?@\"NSURL\"B@\"NSError\">40
v36@0:8B16@20@?28
v36@0:8B16@\"MIAppIdentity\"20@?<v@?@\"NSError\">28
@\"NSString\"
v32@0:8Q16@?24
@44@0:8@16@24Q32I40
@44@0:8@16B24Q28^@36
v24@0:8@\"NSCoder\"16
B40@0:8@16@24^@32
@96@0:8@16@24@32@40@48{?=[8I]}56^@88
B32@0:8Q16^@24
v68@0:8Q16Q24Q32B40@44@52@60
v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16
v40@0:8@\"NSArray\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
v32@0:8@\"ICLRegistrationOptions\"16@?<v@?@\"NSError\">24
@\"NSUUID\"
v64@0:8@\"NSString\"16Q24Q32@\"NSError\"40Q48@?<v@?@\"NSError\">56
v48@0:8@\"MIAppIdentity\"16Q24@\"NSData\"32@?<v@?@\"MIAppReference\"@\"NSError\">40
v32@0:8@\"MIAppIdentity\"16@?<v@?@\"NSSet\"@\"NSError\">24
v40@0:8@16@24@?32
v36@0:8@\"NSDictionary\"16B24@?<v@?@\"NSError\">28
v40@0:8@\"NSObject\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
v48@0:8@\"MIAppIdentity\"16@\"MIAppIdentity\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40
B16@0:8
@24@0:8@?16
v24@0:8@?16
B48@0:8@16S24I28I32i36^@40
v24@0:8@?<v@?B@\"NSError\">16
v40@0:8Q16@\"MIAppIdentity\"24@?<v@?@\"NSError\">32
v24@0:8@16
v40@0:8@\"NSURL\"16Q24@?<v@?B@\"NSError\">32
v36@0:8@16B24@?28
@\"NSObject<OS_dispatch_queue>\"
@32@0:8@16^@24
B36@0:8@16B24^@28
v56@0:8@16@24Q32@40@?48
v24@0:8@?<v@?@\"NSError\">16
v36@0:8@\"NSString\"16B24@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">28
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSError\">40
v40@0:8@\"NSString\"16Q24@?<v@?@\"NSSet\"@\"NSError\">32
@24@0:8@16
v32@0:8@\"ICLBundleRecord\"16@\"NSError\"24
v44@0:8@\"NSString\"16@\"NSURL\"24B32@?<v@?B@\"NSArray\"@\"LSRecordPromise\"@\"NSError\">36
v32@0:8@\"MIAppReference\"16@?<v@?@\"LSRecordPromise\"@\"NSError\">24
v36@0:8@\"NSString\"16i24@?<v@?@\"NSError\">28
v32@0:8@\"NSString\"16@?<v@?@\"MIBundleMetadata\"@\"NSError\">24
v24@0:8Q16
@32@0:8Q16^@24
v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSURL\"@\"NSString\"@\"NSError\">32
q16@0:8
v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"@\"NSError\">24
```
