# `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,032,800 bytes.

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
Failed to read bundle metadata from %@
Settings.bundle
-[MIExecutableBundle _codeSigningInfoFromMCM]
Install type extended attribute not found on %@
MOBILEINSTALLATION_TEST_LAUNCH_WARNING_DATA
v24@?0r*8^B16
initialODRSize
volumeUUID
MICreateCFBundleEnforcingInfoPlistSize
uniqueInstallID
The \"NSPrivacyTrackingDomains\" key in the app's Info.plist must have an array value containing strings. An entry was found in that array of non-string type: %@
Found unexpected value for entitlement %@: %@; falling back to persona %@
Appex bundle at %@ with id %@ does not have a string value for the NSExtensionContextClass key in the NSExtension dictionary in its Info.plist
-[MIFileManager installTypeFromExtendedAttributeOnBundle:error:]
dev=%d ino=%llu mode=0%ho nlink=%hu uid=%u gid=%u rdev=%d size=%lld atime=%lf mtime=%lf ctime=%lf birthtime=%lf blksize=%d blocks=%lld flags=0x%x 
InstalledAppInfoArray
Manifest.plist
open of %s failed: %s
Failed to discover code signing info for app: %@
Interface-glance
Failed to set ACL on dir %s: %s
PUICApplicationColors
DriverKit extension bundle at \"%@\" with identifier \"%@\" contains a '.' in the portion after the parent app's prefix (prefix: \"%@\" ; dot in: \"%@\").'
Decoded a nil app replacement state from [
MILoadInfoPlistFromBundleWithError
-[MIContainer _replaceExistingContainer:replacementReason:waitForDeletion:error:]
Failed to rollback to old SINF data for identifier %@: %@
Extended attribute list for %s returned length 0, expected length %zd
Calculating keychain group references took %.02f seconds
copyfile failed at %d while copying %s to %s: %s (%d)
Could not get signature version from %@
ExtensionDataContainerParentIDUpdateVersion
ParallelPlaceholderPath
v16@?0@\"NSError\"8
com.apple.MobileInstallationHelperService
categories
ErroneousContainerCleanupDone
CFFIXED_USER_HOME
[f]setxattr failed for path %s fd %d
Got exception while serializing MIStashedBundleMetadata to %@ : %@
-[MIMCMContainer regenerateDirectoryUUIDWithError:]
-[MIMCMContainer diskUsage]
The app extension at \"%@\" has the entitlement \"%@\" which is not allowed for an extension targeting the extension point \"%@\".
-[MIFileManager setOwnerOfURL:toUID:gid:error:]
fstat failed for %s : %s
StashedVersionInfo
Entitlements
Multiple signer organizations found for %@; picking the first one of %@
+[MILaunchServicesDatabaseGatherer _gatherPluginDataContainersForAppExtension:parentBundleID:personaUniqueStrings:parentBundleTypeIsApp:updatingAppExtensionParentID:associatedPersonas:error:]
ApplicationType
placeholderFailureReason
-[MIContainer recreateDefaultStructureWithError:]
-[MIFilesystemScanner _scanFrameworkDirectory:withError:]
Code signing enforcement is disabled.
<No container description>
-[MIExecutableBundle hasNoConflictsWithOtherInstalledEntitiesForSigningInfo:forPersona:error:]
Siri Intents app extension is present in the WatchKit app %@ but there are no Siri Intents in the companion app %@
LC_CODE_SIGNATURE command's data offset is less than the size of the mach header in %@
Failed to create container for %@
com.apple.MobileContainerManager.Entitlements
familyID
containerClass
CFBundlePrimaryIcon
bundleShortVersionString
_ParseContentDescriptors
-[MIContainer removeUnderlyingContainerWaitingForDeletion:error:]
TeamIdentifier
Failed to set code signing info with MCM for %@, isPlaceholder: %c
Failed to create app bundle from %@
Preserved existing stashed version for %@
Readlink failed: %s
Unable to compute hash for executable %@
-[MIContainer _isStagedUpdateContainer:withError:]
Appex bundle at %@ with id %@ does not define a NSExtensionAttributes key with a dictionary value in the NSExtension dictionary in its Info.plist
com.apple.MobileInstallation
-[MIFileManager createTemporaryDirectoryInDirectoryURL:error:]
Scanned %lu items in frameworks dir %@
Could not install embedded profile: 0x%08x (%@)
AppexBundleUnexpectedSwiftSectionInExecutable
_DataForEAKey
SupportedDevices
iPhoneSimulator
-[MIPluginKitBundle _validateXPCServiceWithOverlaidDictionary:error:]
environmentVariables
MIBundleHasMinimumOSApplicableToProductVersion
@a
Expected to find one or more platform slices for %@ in executable at %@ but only found other platforms: %@
-[MIExecutableBundle _discoverWatchAppBundleAsPlaceholder:error:]
lseek to %lld from current offset failed: %s
com.apple.MobileInstallation.SystemOrAnyPersonaExtensionMarker
MissingBundleDisplayNameString
Appex bundle at %@ with id %@ does not define an EXAppExtensionAttributes dictionary in its Info.plist
MI_ALLOW_SWITCHING_PERSONAS_ON_INTERNAL_BUILD
Could't set placeholder EA on \"%s\": %s
-[MIFileManager _setData:forExtendedAttributeNamed:onURL:orFD:error:]
isFactoryInstall
FunctionName
-[MIExecutableBundle hasExecutableSliceForCPUType:subtype:error:]
CFBundleDevelopmentRegion
Rejecting %@ -> %s, as absolute symlinks are not allowed
-[MIDataContainer supersedeExistingContainer:error:]
2.0
com.apple.private.mobileinstall.upgrade-enabled
extendedAttributes=<not found> 
ratingLabel
placeholderFailureUnderlyingErrorSource
isMarketplace
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_DEFAULT
Could not load profile at path %@
AppexBundleContainsClassOrStoryboard
rename of %s to %s failed: %s
Invalid LC_CODE_SIGNATURE command in %@
Mach header specified unknown filetype %u
This is the MobileInstallation test exception sentinel reason
CFBundleName
MIMachOSupportedArchitecturesForPlaceholderInfoPlist
Got unknown value %u for Sinf data type to set on %@
Realpathed %@ ; appending non-existing components %@
associatedPersonas
MIUninstallProfilesForAppIdentifier
App %@ is denylisted; returning failure for capabilities match.
-[MIBundleContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:]
StashOriginalInstallTimestamp
iTunesMetadata.plist
iAdConversionDate
com.apple.MobileInstallation.WorkaroundBundleSymlinkName
Failed to get system persona unique string
com.apple.mobileme.fmf1
Failed to verify code signature for this internal, disk image, or core services app, %@. Because of that, we don't have entitlements or signing info so we'll assume that it does NOT require a container.
softwareVersionExternalIdentifier
-[MIUserManagement clearLegacyBundleIDMappingWithError:]_block_invoke_2
Attempting to reserve %zu bytes of validation memory for testing
location
Cleaning up test mode state for %d
containerURL
Serialized container did not encode the MobileContainerManager serialization of the container
INAlternativeAppNames
2.9.9
Failed to get URL for container %@
com.apple.private.pluginkit.persona
/System/Cryptexes/OS/
System/Library/CoreServices
Failed to save stash metadata
-[MIFileManager _bulkSetPropertiesForPath:existingFD:UID:GID:mode:flags:dataProtectionClass:removeACL:error:]
Did not find last build info; we must be upgrading from pre-8.0 or this is an erase install.
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_UTILITY
-[MIExtensionKitBundle _validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:]
-[MIFileManager modificationDateForURL:error:]
[%@, %@]
installerEpoch
com.apple.installd.MIKeychainAccessGroupTracker
The executable at \"%s\" does not contain any code that is runnable on this device.
Got exception while serializing MIBundleMetadata to %@ : %@
Failed to set container after fetching existing container found when making container live for %@
Failed to remove the file at %@ : %@
CFBundleIcons
Failed to lchmod %s : %s
Failed to get installType from bundle %@ : %@. Placeholder will have installed system app state.
-[MIFileManager setModificationDateToNowForURL:error:]
itemID
%@.sinf
private/var/staged_system_apps
com.apple.MobileContainerManager.AdvanceCopy
Failed to clonefile %s to %s
-[MIFileManager enumerateExternalVolumesWithBlock:]
/private/
Appex bundle at %@ with id %@ has an illegal value for the CFBundlePackageType key in its Info.plist: %@
Executable at %@ did not contain a slice built for platform %@.
Unhandled bundle type %hhu
Failed to enumerate stashed container
v24@?0@\"NSUUID\"8@\"NSError\"16
disk image app
compatibilityState
com.apple.web-browser-engine.content.development
-[MITestManager _onQueue_setTestFlags:]
redownloadParams
[user-defined-directory/
xpc
-[MIFilesystemScanner _scanAppsDirectory:withError:]
platform-application
com.apple.install_session_uuid
UniqueInstallID
UILaunchImageSize
uname() failed
Could not readlink %s : %s
Could not load detached signature data for %@ from %@
No bundle container found for identifier %@
/System/Library/PrivateFrameworks/GPUSupport.framework
Failed to retrieve value for key %@ from the underlying xpc object
-[MIExecutableBundle validateSinfWithError:]
Failed to create MIStashedBundleContainer instance for %@
SC_Info/Manifest.plist
IllegalXPCServiceRunLoopType
-[MIExecutableBundle fairPlaySinfInfoWithError:]
UISupportedInterfaceOrientations
Found non-boolean value for boolean entitlement %@: %@ ; assuming %s.
Unable to determine SDK version for executable at %@
v32@?0@\"NSURL\"8@\"NSString\"16@\"NSError\"24
+[MILaunchServicesDatabaseGatherer _createDataContainersAndSetDataProtectionForBundle:forPersona:error:]
getattrlistbulk failed on entry %u in %s : %s
IsSwiftPlaygroundsApp
CFBundleIconFiles
Failed to find app bundle in container %@ : %@
TEST MODE: Returning fake launch warning data for %@
Expected an array of string.
Failed to seek to %lld from current offset in %@ : %s
systemgroup.com.apple.installcoordinationd
Could not iterate slices in macho %@
Failed to write uninstalled list to %@ : %@
8.2
_UIApplicationMain
v24@?0@\"NSDictionary\"8@\"NSError\"16
getattrlist failed for %@: %s
genre
Class getUMUserManagerClass(void)_block_invoke
_PopulateAttrBuf
SC_Info
-[MIPluginKitBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
AppexBundleIllegalExtensionAttributesDict
TestFileForSync
Validating as built-in: %@
Could not get family ID from SINF at %@: %ld
SinfReplicationPaths key value in manifest %@ was not an array
profileValidationType
Got non-dictionary response from MCM: %@
previous-application-identifiers
-[MIAppExtensionBundle validateBundleMetadataWithError:]
private
-[MIFileManager setInstallType:inExtendedAttributeOnBundle:error:]
%4d/%4d\t 0%08o\t %@
Detected upgrade from %@ (%@) to %@ (%@)
LegacyErrorString
Non transient container can't be marked as a staged container
Skipping device family check because of a set default
RequiredOS
malloc failed for %ld bytes: %s
Clearing test flags 0x%llx (0x%llx -> 0x%llx)
MIWatchKitVersion_1_0 == version || MIWatchKitVersion_2_0 == version
Not removing sinf because we failed to get sinf replication paths: %@
hasCriticalAlerts
MinimumProductVersion
InstallQOSOverride
Attr named %s not present on %@
MILocationSystemDefinedCommon
-[MIGlobalConfiguration _ixDataStorageHomeURLWithError:]
com.apple.developer.parent-application-identifiers
referrerURL
Failed to make staged container live %@
+[ICLWorkspace _connectionToInstallationDaemonWithError:]
v24@?0@\"NSString\"8@\"ICLAppExtensionRecord\"16
Failed to get watchkit plugin for %@: %@
Failed to write current build info to %@ : %@
Could not get build version from last build info dictionary; assuming this is an upgrade
-[MIMCMContainer supersedeExistingContainer:error:]
keychain-access-groups
Failed to retrieve realpath for suspicious path %@
+[MIContainer tempContainerWithIdentifier:forPersona:ofContentClass:constructor:error:]
(container_error_copy_unlocalized_description returned NULL)
StaticDiskUsage
com.apple.developer.web-browser-engine.host
Failed to iterate mach-o slices for input file: %s
B16@?0@\"MIMCMContainer\"8
open_dprotected_np failed for %s for class %d : %s
Expected executable at \"%@\" %@to have a __swift5_entry section
App Extension
Could not get ACL for file %@: %s
Failed to get entry for bundle %@ in %@ personas %@ : %@
Invalid type for metadata property '%@'.
Failed to serialize app launch prohibition [
Failed to find __LINKEDIT segment in %@
linkedParentBundleID
-[MIMCMContainer replaceExistingContainer:error:]
-[ICLSinfInfo isEqual:]
There is nothing to purge
HasSystemGroupContainers
Failed to fetch data containers for app extension at %@: %@; skipping it
com.apple.MobileInstallation.ParentBundleID
<%@ status:%lu isNew:%c container:%@>
Unknown QOS class value specified: %@; ignoring
%@ was grandfathered but has container required entitlement
seatbelt-profiles
com.apple.private.extensionkit.builtinanypersona
Serialized container did not encode containerURL
Executable at %@ did not match stub hash for cputype %d cpusubtype %d: %@ != %@
Failed to set up daemon container for persona %@: %@
Bundle at path %@ had an invalid CFBundleIdentifier in its Info.plist: %@
Scanned %lu items in container type %ld
Resolved persona for %@, from %@ to %@
Failed to get iTunesMetadata from %@ : %@
Ignoring Watch app at %@ because it's not compatible with a known watchOS version
acl_init() failed: %s
macho_best_slice_in_fd failed
Could not get current build string; assuming this is an upgrade
Unknown
Failed to get keychain access groups in XPC service %@
fgetattrlist for %s failed: %s
read failed for %s : %s
copyfile hit ENOTSUP at %d while copying %s to %s; src mode: 0%o
TooManyAlternativeAppNames
Failed to resolve persona for %@
LSEligibilityInstallPredicate
Failed to get the real path of /var
Could not find appropriate set for app %@
q
Failed to get all bundles within app %@
The base path %@ and/or suspicious path %@ were nil
MISSignerType is MISSignerTypeLegacyVPN which is not supported by MI; returning MICodeSignerTypeUnknown
framework
-[MIFileManager _removeACLAtPath:isDir:error:]
Failed to realpath %s : %s at %s
-[MIContainer _deriveContainerStatusWithError:]
-[MIDataProtectionChangeOperation _runChangeOperationWasLocked:withError:]
Unable to check if %@ with bundle identifier %@ is already installed.
com.apple.Home.HomeExtension
Failed to locate an attrBuf
Failed to create container query for querying containers for identifier: %@ groupIdentifiers: %@ containerType: %llu
system
PersonaBundleIDPurgeCompleteInUM
DTPlatformBuild
-[MIPersonaAttributes dealloc]
%s EA was not set to expected value from \"%s\"
Found entry in subgenre array that was not a dictionary: %@
>
MGCopyAnswer for kMGOCompatibleAppVariants returned NULL
Don't know how to check bundle %@ for conflicts.
apfs
_DiscoverPersonasForBuiltInBundle
Failed to construct MIContainer instance with container %@ : %@
stagingSubsystem
com.apple.intents-service
isNoLongerCompatible
Attempted to set a zero-length or nil app identifier on \"%s\"
Failed to get XPC connection
Failed to deserialize container data for token %@
Info.plist from bundle at path %@ had none of the keys that we expect; %@
Found zero associated personas for app %@; assuming primary persona
data-protection-class
-[MIFileManager createDirectoryAtURL:withIntermediateDirectories:mode:class:error:]
Updating sinfs with %lu bytes of data at URLs: %@
-[MIRelocatedBundleContainer regenerateDirectoryUUIDWithError:]
Appex bundle at %@ with id %@ does not define a NSExtensionPointName key with a string value in the NSExtensionAttributes dictionary in the NSExtension dictionary in its Info.plist
bundleIdentifier
Library/Logs
_CopyfileStatusCallback
developerID
Attempted to iterate directories starting at a path that was too long: %s
Appex bundle at %@ with id %@ has an illegal value for the RunLoopType key in the XPCService dictionary in its Info.plist
Could not stat %s: %s
removexattr on %s for %s failed
VuGdqp8UBpi9vPWHlPluVQ
-[MIFilesystemScanner _scanExtensionKitDirectory:withError:]_block_invoke
HasAppGroupContainers
managementDeclarationIdentifier
Property %s did not match
Updated bundle %@ no longer references keychain group %@
isPlaceholder
_hasNoConflictWithNonContainerizedSystemApp
-[MIBundleContainer _stashedBundleContainerForIndex:error:]
-[MIContainer _setContainer:error:]
Lacking other hints, because the root of the bundle %@ has only a Contents directory, assuming this is a MacOS app
Failed to get the path to the executable for bundle at %@
Unknown Process Name
Setting simultaneous installations allowed to %ld
Failed to update container manager with code signing info for %@ : %@
hasAppGroupContainers
Destination %@ exists and is a directory
_GetAttrBuffer
mobile
Failed to get container path for %@
-[MIBundle getIsBuiltForMacPlatform:error:]
Failed to get stash metadata from %@ : %@
parallelPlaceholderURL
com.apple.fieldtest
InvalidSinf
Appex bundle at %@ with ID %@ does not have a CFBundleDisplayName key with a non-zero length string value in its Info.plist
storefront
MIUninstallProfilesForAppIdentifier_block_invoke
-[MIDataProtectionChangeOperation performChangeOperation]
NSExtension
-[MIFileManager _dataForExtendedAttributeNamed:length:onURL:orFD:error:]
serializedPlaceholderURL
Failed to get CFBundleIdentifier from bundle %@
isAutoDownload
-[MIGlobalConfiguration allowsInternalSecurityPolicy]_block_invoke
Failed to move %@ to %@
Failed to scan for bundle containers of content class %ld
Failed to retrieve container subdirectories for class %llu
%@.supf
Value of key %@ on %@ was not a number
kMISValidationInfoValidatedByProfile was not set for %@ but kMISValidationInfoSignerType was set to MISSignerTypeProfile
IsMarketplace
com.apple.developer.networking.networkextension
+[MILaunchServicesDatabaseGatherer entryForBundle:inContainer:forPersonas:withError:]
com.apple.iOS6Updater
PUICApplicationPrimaryColor
DataProtectionClass
com.apple.web-browser-engine.rendering
%@, associatedPersonas=%@
B20@?0@\"NSURL\"8C16
Failed to get installType from bundle %@ : %@
dylib
Install type not set in bundle metadata for %@
UILaunchImages
Skipping purging of transient container because it is staged: %@
Failed to create bundle object for system app %@ at %@
WatchKit 2 app extension's NSExtension.NSExtensionAttributes dictionary is not present. It must contain a WKAppBundleIdentifier key set to the WatchKit app's bundle ID.
failed to open %s : %s
MIInstallProfileAtURL
sandbox_extension_consume for %s failed: %s.
 osBuildVersion=
-[MIContainer _doInitWithContainer:error:]
-[MIGlobalConfiguration _bundleIDMapForBundlesInDirectory:withExtension:loadingAdditionalKeys:]
Failed to create temp dir at path %s
Failed to symlink %s -> %s
sideLoadedDeviceBasedVPP
+[MIInstallationIdentity installationIdentityForBundle:settingIfNotSet:error:]
linkedChildBundleIDs
IsContainerized
Failed to read %@
-[MIStoreMetadata initWithCoder:]
Expected key to be a valid string.
MI_Transient_Bundle_Cleanup
%s is not enabled
Failed to convert app identifier EA data (%@) to string from \"%s\"
Failed to delete existing transient container for %@
-[MIMCMContainer reclaimDiskSpaceWithError:]
Failed to get bundle URL for %@ from built in app map
+[MIBundleContainer purgeTransientBundleContainersWithError:]
-[MIBundleContainer bundleMaxLinkedSDKVersion]
Messages stub apps may only have a single message payload provider app extension, but this stub app has an extension %@ of type %@
bundleVersion
com.apple.family
Entitlement %@ does not contain supported types; ignoring.
-[MIBundleContainer stashBundleContainerContents:error:]_block_invoke
Failed to seek to %lld in %@ : %s
<%@: dataContainerURL: %@ groupContainerURLs: %@ environmentVariables: %@>
failed to stat %s : %s
Entitlement %@ contains non-string values; ignoring.
originalInstallDate
iphonesimulator
-[MIFilesystemScanner _scanBundleContainersWithClass:withError:ignoredErrorOccurredOnOneOrMoreItems:]
IllegalBundleShortVersionString
Expected a valid dictionary.
Invalid staging content type: %lu
IntentsAppexIntentsSupportedDuplicated
NSExtensionPointIdentifier
AppexBundleMissingClassOrStoryboard
-[MIExecutableBundle needsDataContainer]
com.apple.developer.not-executable
AppexBundleIDSuffixContainsPeriod
} 
%@/%@
application-identifier
iTunesArtwork
Failed to fetch signature version for executable at %@ with libMIS error %@
_IsDictionaryWithKeyStringAndValueArrayOfString_block_invoke
InstalledContentLibrary.MILocationUserDefined
-[MITestManager _onQueue_clearTestFlags:]
Exempting %@ from System App XPC Service & Extension bundle ID conflict checks because the parent bundle has the System App entitlement
-[MIBundleContainer _writeRawiTunesMetadataData:error:]
-[MIBundle isApplicableToCurrentDeviceCapabilitiesWithError:]
Framework
hasParallelPlaceholder
AppleInternal
clonefile failed for %s to %s: %s
MIMachOFileIterateImageSlices
iad-attribution
CPUSubtype
+[MIContainer groupContainerURLsForBundleIdentifier:forPersona:error:]
dateOriginallyInstalled
LSCounterpartIdentifiers
App with id %@ is not in the system app map even though it's type system
Failed to stat path %s : %s
Failed to get data containers for containerized app %@ for persona %@ : %@
secondaryGenreId
Appex bundle at %@ with id %@ defines an EXPrincipalClass key in the EXAppExtensionAttributes dictionary in its Info.plist with a zero length string.
Failed to read placeholder entitlements file from %@
Failed to find executable bundle in container %@ : %@
InstallBuildVersion
CodeSigningInfoNotAuthoritative
MIBundleSupportedArchitecturesForPlaceholderInfoPlist
LastBuildInfo.plist
Couldn't set installType EA on \"%s\": %s
Executable stub at %@ not signed by Apple.
-[MISystemAppState _onQueue_setSystemAppStateList:]
Appex bundle at %@ with id %@ does not define an extension point in its Info.plist
DTXcode
Couldn't get appIdentifier EA from \"%s\"
Skipping FIFO encountered at %s
+[MICodeSigningVerifier validateWatchKitV1StubExecutableBundle:error:]
-[MILaunchServicesDatabaseGatherer initWithOptions:personaUniqueStringForBundles:enumerator:]
RunLoopType
com.apple.mobileme.fmip1
lstat failed for %s
-[MIFileManager realPathForURL:allowNonExistentPathComponents:isDirectory:error:]
No extended attributes found on %s
-[MIInstallationIdentity initWithSessionID:uniqueID:]
NSExtensionContextHostClass
Failed to copy %@ to %@
Failed to discover personas for built-in app %@ : %@
subGenres
Ignoring WatchKit 1 app extension with identifier %@
Failed to create URL for internal superseded app additions plist.
Failed to rollback iTunesMetadata: %@
Info.plist
Attempted to set container %@ with content class %llu on %@ which represents a container with class %llu
MIInstallationDomainMax
MissingBundleNameString
Attempting to restore an identity without having first assumed an identity
-[MIInstalledInfoGatherer bundleRecordWithError:]
NSExtensionPrincipalClass
com.apple.private.security.system-application
The SINF provided for the bundle at %@ is not valid so this application will not run.
Couldn't get data from xattr named %s on \"%s\"
The executable at \"%s\" does not contain code for any platform and CPU architecture combination that is runnable on this device. The executable has code for these platforms and architectures: %@. This device can run code for these platform
POSIX error %d (%s)
RoleUserMigration.plist
MigrationInfo.plist
Key missing or invalid type when decoding MILocationUserDefinedDirectory from plist dictionary
_ProcessContinuation
com.apple.MobileInstallation.bundleURL
AppexBundleMissingEXAppExtensionAttributesDict
Data for key %s returned length 0, expected length %zd
Appex bundle at %@ with ID %@ does not have a CFBundleName key with a non-zero length string value in its Info.plist
copyfile after clonefile failed for %s to %s: %s
-[MIFileManager standardizeOwnershipAtURL:toUID:GID:removeACLs:setProtectionClass:foundSymlink:error:]_block_invoke
Couldn't get %s EA from \"%s\": %s
Failed to get identifier for the container
Failed to create URL for migration info file.
IncorrectArchitecture
Unable to compute hash for stub %@
com.apple.MobileInstallation.AssociatedBuiltInBundleURL
_MICommonCopyGroupEntitlement
Deleting old link at %@ because it's not needed or not correct anymore
Removed safe harbor attribute for %@ at %@
applicationDSID
Waiting for %zu bytes to become available (%zu/%zu currently available) to validate %@
driverKitExtensionURLs
-[MIExecutableBundle watchKitVersionWithError:]
com.apple.developer.marketplace.app-installation
-[ICLStashedAppRecord isEqual:]
-[MIAppExtensionBundle associatedPersonasUsingParentPersona:didUseParentPersona:error:]
Preserving compressed bit on %s
B20@?0i8r*12
-[MIUserManagement personasAreKnownForUniqueStrings:error:]_block_invoke
-[MIInstalledInfoGatherer _populateBundleRecordValues:signingInfo:error:]
Failed to move application at %@ into container path %@
Failed to get info dictionary from MISValidateSignatureAndCopyInfo when verifying %@
betaBuildGroupID
distributorID
Current build version (%@ / %@) equal to last version recorded (%@ / %@); skipping upgrade
Found container %@ with no bundle; skipping.
<%@ container=%@ persona=%@ path=%@>
Logs/MobileInstallation
-[MIFileManager diskUsageForURL:]
Failed to construct MIMCMContainer instance with container %@ : %@
downloaderDSID
Failed to retrieve any containers for identifier: %@ groupIdentifier: %@ container type: %llu persona: %@
Failed to hash watchkit app executable for %@ at %@
InvalidWatchKitApp
-[MIFileManager setOwnershipAtURL:toUID:gid:error:]_block_invoke
There is nothing to be replaced
+[MIBundle bundleIsInDenyList:]
Failed to determine if we're running in test mode: %@
IllegalXPCServiceServiceType
AppexBundleIllegalExtensionPointNameString
Failed to get ACL from %@ : %@
Failed to locate personal persona: UserManagement returned %lu personas but none of them had isPersonalPersona = YES
MIAssumeIdentity
Failed to read manifest at %@ : %@
Failed to unlink no longer needed install map at %@ : %@
CF_MIEmergencyOffloadVersion
Extensions
Failed to get keychain access groups for app %@
__swift5_entry
AppManagementDomain
embedded.mobileprovision
FairPlay check for SINF validity in %@ returned error %d
EXExtensionPointCatalog
B16@?0@\"MIBundleContainer\"8
Not allowed to mark placeholder as validatedByFreeProfile for %@
sourceApp
RequireEligibilityForInDevelopmentApps
MIDaemonConfiguration
+[MIContainer _allContainersForIdentifier:persona:options:error:]
plist
Failed to retrieve depth of %@
Executable at %s contained no identifiable architectures
MissingSINF
kMISValidationInfoSignerType was set to unknown value %ld
v8@?0
UserManagement
com.apple.TrustMe
SinfReplicationPaths
Library/Logs/MobileInstallation
-[MIFileManager _copyItemAtURL:toURL:failIfSrcMissing:alwaysClone:ignoreErrors:error:]
rating
Failed to get build version
macosx
socket
sinfInfo
FakeCodeSigningNotDisabled
(%@|%@)
Siri Intents Appex bundle at %@ with id %@ does not define an IntentsSupported key with an array value containing strings in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist.
com.apple.developer.usernotifications.critical-alerts
-[MICodeSigningVerifier _loadSystemDetachedSignatureForBundleID:error:]
MessagesStubAppMissingAppExtension
-[MIExecutableBundle watchKitAppBundleForWKVersionOrEarlier:error:]
Could not create symlink containing %s at %s: %s
marketplaceItemID
LSRequiredFeatureFlags
-[MIBundleContainer _configureBundleWithError:]
Failed get container URL for %@ when trying to clone content from %@
Failed to write serialized app launch prohibition to [
Found emergency offloaded app %@ from OS build %@
+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]_block_invoke
-[MIDataProtectionChangeOperation _runChangeOperationWasLocked:withError:]_block_invoke
UIRequiredDeviceCapabilties requested key '%@' that did not return a boolean value. Only boolean values are supported. Forcing mismatch.
AppBlacklisted
WatchKit %@ app had an Info.plist key that was not a string.
Failed get container URL from %@
@\"NSError\"24@?0r*8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}16
MIReplicateRootSinf
MIRestoreAvailableMemoryForValidationAfterTesting
WKAppBundleIdentifier
%@
UIRequiredDeviceCapabilties in Info.plist has a key that is not a string.
_CopyEAList
Unknown platform: %u
%s was called with a NULL path parameter.
xros
Failed to create CFBundle for %@
-[MIInstallationIdentity _writeToBundle:error:]
container_query_create_from_container() returned NULL for deserialized container object
B48@?0^{__CFString=}8^{__CFString=}16^{__CFDictionary=}24B32B36B40B44
HOME
Failed to remove execute permissions from bundle executable at %s : %s
-[MIExecutableBundle onlyHasExecutableSlicesForPlatform:error:]
com.apple.private.security.container-required
Skipping compatibility symlink because app was linked with SDK version 0x%08x
Failed to stat %s : %s
Skipping block device encountered at %s
-[MIPluginDataContainer parentBundleID]
Failed to locate a bundle with extension %@ in directory %@
com.apple.SharingViewService
CFBundleDisplayName
com.apple.MobileInstallation.ContentProtectionClass
Failed to write %lu bytes to %s : %s
isInstallationHoldActive
LSInstallByDefault
Unable to determine if bundle executable is present at \"%@\".
stat of %@ failed: %s
MIReduceAvailableMemoryForValidationForTesting
Fetch framework info at %@ requested with options %@
DTSDKName
BundleIDConflictWithOtherIdentifier
Identifier %@ is a %@, so we can't install %@ with that same identifier.
-[MIFileManager destinationOfSymbolicLinkAtURL:error:]
FIFO
returning: %@
System/Library/AppPlaceholders
Failed to discover dylibs in directory %@
Failed to link %s to %s
Appex bundle at %@ with id %@ does not define either an NSExtensionMainStoryboard or NSExtensionPrincipalClass key with a string value in the NSExtension dictionary in its Info.plist
codeSignerType
com.apple.installd.validatedByFreeProfile
Already have entry for app %@; keeping it instead of %@
No SinfReplicationPaths array in manifest %@
Failed to getclass of file %s: %s
+[MIBundleContainer enumerateAppBundleContainersInDomain:forPersona:isTransient:usingBlock:]
[f]getxattr failed for xattr named %s path %s fd %d
storefrontCountryCode
serializedContainerRepresentation
/System/Library/AppPlaceholders
HasCriticalAlerts
Error fetching group containers for %@ for persona %@ : %@
IsPlaceholder
<%@ identity:%@/%@ isTransient:%c containerClass:%llu>
Failed to make safe harbor container live %@
Matched thinning based on defaults override %@
targetUID
+[MIStoreMetadata metadataFromPlistAtURL:error:]
unknown bundle type
appReplacementSourceBundleIdentifier
Failed to make new data container for app %@ live: %@
Returning previously obtained code signing info for %@
ApplicationVerificationFailed
com.apple.security.system-groups
\v
 without a source app identity to [
CFBundleInfoPlistURL
lsInstallType
DTPlatformName
Failed to fetch alternative bundle at %@ : %@
%@ was grandfathered but has no-container entitlement
Rejecting %@ with base %@ because base component count is greater than child component count (reals %@ ; %@)
Failed to remove extended attribute named %@ from %s: %s
Error when introspecting %@
Failed to get app extensions in app %@
com.apple.Posters
-[ICLHelperServiceClient volumeUUIDForURL:error:]_block_invoke
Install session ID requested for bundle that was not an app or app extension: %@
(container_get_error_description returned NULL)
GeoJSON
InvalidStubExecutable
gameCenterEnabled
Info.plist missing at %@
MIReleaseSandboxExtensionHandle
-[MIPluginKitBundle overlaidInfoPlistWithError:]
FreeProfileValidated
-[ICLWorkspace bundleRecordsWithFrameworkURL:options:withError:]
+[MIUserManagement sharedInstance]_block_invoke_2
Operation to update protection classes for %@ to class %d failed with error %@
MIContainerManagerErrorDomain
com.apple.MobileContainerManager.DataContainerClass
Failed to supersede container %@ with %@
Appex bundle at %@ with id %@ has an illegal value for the ServiceType key in the XPCService dictionary in its Info.plist
xattr named %s not present on \"%s\"
/var
factoryInstall
Failed to construct MIContainer object for all %llu containers; last error is underlying error
-[MIMCMContainer purgeContentWithError:]
Failed to release sandbox token %lld for %@ : %s
-[MIExecutableBundle relativeExecutablePath]
UIApplicationDelegateClass
lstat succeeded but st_dev was -1 for %s
com.apple.iTunesStore.downloadInfo
isBeta
+[MIContainer containerWithIdentifier:forPersona:ofContentClass:createIfNeeded:constructor:created:error:]
Removing keychain access groups: %@
CFBundleIdentifier
+[MICodeSigningVerifier _validateSignatureAndCopyInfoForURL:withOptions:error:]
Failed to scan %@ in %@ : %@
PurchaserID
MIFetchInfoForUID
Read entry length %u for entry %hu but that put us off the end of the buffer
com.apple.security.application-groups
Failed to set ACL on %s: %s
PlaceholderFailureReason
AppexBundleIllegalPackageTypeValue
DriverKitExtensionPaths
Failed to search for apps in %@ : %@
Unknown value for DataProtectionClass entitlement: %@; defaulting to class %d
Could not get code info identifier from %@
MIRestoreIdentity
_InstallProvisioningProfile
-[MIAppExtensionBundle validateHasCorrespondingEntitlements:error:]
/var/
Failed to get executable bundle in container %@
Invalid mach_header.sizeofcmds in %@
AdHocSigned
HasSettingsBundle
statfs failed for %@: %s
Failed to remove keychain items %@
Removing matching profile for %@: %@
removefile_state_set REMOVEFILE_STATE_ERROR_CALLBACK failed: %s
user app
-[MIBundle setBundleParentDirectoryURL:error:]
0123456789abcdef
-[MIExecutableBundle estimatedMemoryUsageToValidate]
variantID
Siri Intents Appex bundle at %@ with id %@ defines an IntentsRestrictedWhileLocked key in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist, but that key's value is not an array of strings.
com.apple.SharedWebCredentialViewService
__LINKEDIT
appex
-[ICLWorkspace bundleRecordsForLaunchServicesWithWrapperURL:forBundleIdentifier:withError:]
-[MIGlobalConfiguration helperLogDirectory]
The app extension stub app %@ must have at least one app extension, but none were found.
IsNoLongerCompatible
ProfileValidated
System App Extension
B16@?0@\"NSURL\"8
AppexBundleIllegalExtensionPointIdentifierString
signerOrganization
No WatchKit 2.0 app bundle or placeholder found for app %@
Could not find installed app with identifier %@ in domain %lu
com.apple.mobileinstallation.placeholder
Can't figure out set for app type %@
MacOS
keySample={ 
parentIdentifiers
unspecified
AllowPatchInstallationWithoutSinf
Attempted to set nil data on \"%s\" for EA named %s
releaseDate
ReleaseType
-[MIMCMContainer setDataProtectionClass:forSecondOrThirdPartyApp:error:]
-[MIPluginKitBundle _validateNSExtensionWithOverlaidDictionary:error:]
Appex bundle at %@ with id %@ does not have a string value for the NSExtensionViewControllerHostClass key in the NSExtension dictionary in its Info.plist
Failed to clear staged update container status for %@ after making it live : %@
mkpath_np of %@ failed: %s
getpwuid_r succeeded but no user was found with uid %d
WatchSimulator
Failed to recreate structure for %@
-[MIKeychainAccessGroupTracker _onQueue_discoverReferences]
Unable to get primary persona unique string from UserManagement
BackedUpState
_hasNoConflictWithSystemAppBundleIDs
Could not determine architectures in the executable at \"%s\".
Failed to create symlink at path %@ to %@ : %@
ProductVersion
-[MIMCMContainer initWithSerializedContainer:matchingWithOptions:error:]
__TEXT
DTPlatformVersion
SerializedPlaceholder.ipa
+[MILaunchServicesDatabaseGatherer enumerateAppExtensionsInBundle:forPersonas:updatingAppExtensionParentID:ensureAppExtensionsAreExecutable:installProfiles:error:enumerator:]
MIInstallProfileWithData
MIAppReplacementStatusMax
com.apple.CloudKit.ShareBear
Executable stub at %@ had unexpected signing identifier '%@'; expected %@.
artistName
Failed to unset previous symlink name attribute on container %@: %@
com.apple.private.extensionkit.builtinsystempersona
-[MIFileManager _traverseUntilFirstAvailableParentOfURL:withBlock:]
contentDescriptors
] does not match the expected location type 
isOnDemandInstallCapable
CLKComplicationSupportedFamilies
CapabilitiesMatch
Failed to wipe container for identifier %@
DTXcodeBuild
+[MICodeSigningVerifier validateWatchKitV2StubExecutableBundle:error:]
distributorInfo
Failed to get keychain access groups in app extension %@
-[MIBundleContainer bestEffortRollbackiTunesMetadata:error:]
com.apple.mobileinstallation.companion_placeholder
Verifying resources using detached signature for %@
, osBuildVersion=
Failed to create %@ instance for %@
Multiple message payload provider extensions found in app but only one is allowed (found %@ ; already found %@)
-[MIExecutableBundle _validateWithError:]
-[MIBundleContainer initWithToken:options:error:]
Uninstalling profiles for %@
DTCompiler
symlink
Invalid type for metadata property %@
LSInstallType
Signpost
com.apple.developer.driverkit
Failed to clone existing container item at path %@ to stash path %@
-[MIContainer initWithToken:options:error:]
/System/Library/Frameworks/IOKit.framework
AppleTVOS
watchos
LSEligibilityPredicatesValidAtEraseInstallDataMigration
Executable at %@ did not contain a slice built for platform %@ (found only platform %@).
Unable to get hashes for executable %@
InstalledContentLibrary.MILocationSystemDefinedCommon
installBuildVersion
Failed to find a candidate buffer to scavenge!
DTSDKBuild
-[MILaunchServicesDatabaseGatherer _scanAppExtensionsInBundle:inBundleContainer:personas:enumerator:error:]_block_invoke
/
Dictionary parameter was nil or not a dictionary
-[MIAppExtensionBundle extensionCacheEntryWithError:]
Failed to remove ACL
referrerApp
LSRequiresIPhoneOS
MacOSX
MIInstallationDomainSystemShared
com.apple.mobile.installd
com.apple.developer.web-browser-engine.networking
sinfs
UIBackgroundModes
com.apple.MobileContainerManager.PlaceholderEntitlements
Suspicious path %@ does not contain base path %@ as a prefix
accountInfo
Object returned from _CFPropertyListCreateFiltered was not a dictionary, was type %@
AppexBundleUnknownExtensionPointIdentifier
LSUpgradeInstallConsent
Found empty placeholder entitlements in %@
com.apple.developer.web-browser-engine.rendering
MissingBundleVersion
Existing container was nil but replacement reason was not NewContainer; given %ld
Appex bundle at %@ with id %@ does not have a string value for the NSExtensionContextHostClass key in the NSExtension dictionary in its Info.plist
com.apple.mis.warning
com.apple.developer.homekit
-[MIFileManager _realPathWhatExistsInPath:isDirectory:]
InDiagnosticsMode
AppInstallDate
-[MIContainer markContainerAsStagedUpdateWithError:]
/System/Library/Frameworks/System.framework
-[MIAppExtensionBundle _updateInfoForContainerSet:newlyCreated:error:]
OS Module app
-[MIBundle siriIntents]
stashedVersions
signerIdentity
counterpartIdentifiers
cZflGJ39lJHTCPy35/N14Q
Unexpectedly was not passed personas when scanning appex %@ in %@
-[MIContainer clearStagedUpdateContainerStatusWithError:]
Library
DownloaderDSID
System/Library/disableSystemAppDeletion
-[MIGlobalConfiguration lastBuildInfoFileURL]
Not pushing signing info to MCM because state was %lu
-[MIBundleContainer stashBundleContainerContents:error:]
-[MIFileManager enumerateURLsForItemsInDirectoryAtURL:ignoreSymlinks:withBlock:]_block_invoke
B24@?0@\"MIContainer\"8^B16
NSExtensionMainStoryboard
IntentsRestrictedWhileLocked
Failed to unlink temporary directory at %s : %s
Failed to get data for EA key \"%@\": %@
Unable to deserialize iTunesMetadata.plist data
Failed to remove app replacement state at [
%@, linkedParentBundleID=%@ linkedChildBundleIDs=%@
s
Creating new link at %@
PluginKitPlugin
Bundle at path %@ did not have a CFBundleIdentifier in its Info.plist
WKWatchKitApp
-[MIDaemonConfiguration daemonUserDataLibraryDirectory]
_DiscoverPersonasFromBundleContainer
launchProhibited
-[MIDataContainer setContentProtectionClass:]
Failed to get FD to bundle executable at %s
Internal
DriverKitBundleIDNotPrefixed
-[MIPluginDataContainer isSystemOrAnyPersonaExtension]
IsEligibleForWatchAppInstall
iTunesMetadataCaptureFailed
Skipping macho file not runnable failure during test mode
UninstallParallelPlaceholder
-[MIContainer purgeContentWithError:]
Unable to resolve persona for location of identity %@
AppexBundleIllegalExtensionPointVersionString
-[MIFileManager urlsForItemsInDirectoryAtURL:ignoringSymlinks:error:]_block_invoke
Couldn't get length for xattr named %s on \"%s\"
Failed to remove attribute %s from %s: %s
v24@?0@\"NSString\"8@\"ICLBundleRecord\"16
nameTranscription dictionary does not have expected type
Failed to get home dir path size: %s
Data length is more than 4 KB for extended attribute key %s: length is %zd bytes
Cannot set installation identity for non-app bundle %@
-[MIMCMContainer dealloc]
XPC!
Failed to get value for key %@ on data container %@ : %@
Existing link is fine, leaving it there.
/System/Library/PrivateFrameworks/PassKitUIFoundation.framework
Unknown MIAppReplacementStatus: %lu
init(internal:)
+[MICodeSigningInfo getValue:forEntitlement:fromProcessWithAuditToken:error:]
-[MIBundle validateAppMetadataWithError:]
!
-[MIDaemonConfiguration installcoordinationdUserDataLibraryDirectory]
-[ICLUninstallRecord isEqual:]
Ignoring failure to set protection class to %d on %@ (mode 0%o): %@
-[ICLWorkspace enumerateCryptexContentWithBlock:error:]_block_invoke
InstallingEmbeddedProfile
appletvos
personasRecordMap
-[MIBundleContainer captureStoreDataFromDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
FSIOC_FD_ONLY_OPEN_ONCE returned unexpected result %d errno %d (%s) for path %s
localizedDistributorName
marketplaceDomain
accountID
Refusing to write 
com.apple.developer.memory.transfer-accept
/tmp
PackageInspectionFailed
app identity has nil personaUniqueString
PlaceholderEntitlements.plist
Appex bundle at %@ with ID %@ does not have a CFBundleVersion key with a non-zero length string value in its Info.plist
_StageURLByMovingProcessItem
Failed to get bundle URL for plugin data container %@: %@
InstallCoordination
com.apple.security.system-container
Could not get extended attribute list for %s: %s
Assuming unknown built-in app %@ should be associated with primary persona
com.apple.MapsExternalComponents
-[MIDriverKitBundle currentOSVersionForValidationUsingPlatform:withError:]
Failed to setclass(%d) on file %s: %s
kMISValidationInfoSignerType is not set or is not a number for %@
BundleMetadata.plist
void *UserManagementLibrary(void)
ValidatedByProfile
Failed to create an instance of MILocationUserDefined because the app bundle URL supplied was not for an app: [
applicationType
setxattr for %s on %s failed
Couldn't set %s EA on \"%s\": %s
Skipping character device encountered at %s
Stub %@ does not have required section %@
Header magic indicates non-native-endian slice; that's not allowed.
ratingRankEligibilityDomain
-[MIInstalledInfoGatherer _groupContainersDictionaryForPersona:]
Could not create bundle for WatchKit app at %@
Found WatchKit app at %@ but it was not a WatchKit 2 app. Is it missing its app extension?
Failed to lstat %@ : %s
Failed to write serialized MIBundleMetadata to %@
EXAppExtensionAttributes
-[MIInstalledInfoGatherer _fixUpForBuiltInAppParallelPlaceholder]
Library/ExtensionKit/Extensions
-[MIExecutableBundle lsInstallTypeWithError:]
-[MIAppExtensionBundle associatedPersonasUsingParentPersona:error:]
Failed to gather launch services info for app extension %@ in bundle %@ : %@
autoInstallOverride
Failed to read UM's persona generation identifier when resolving persona
SYS_initgroups failed; error %d (%s)
__DATA segment exceeds bounds in %@
Made container live for %@ at %@
Failed to discover installed apps: %@
MIInstallerErrorDomain
-[MIExecutableBundle codeSigningInfoByValidatingResources:performingOnlineAuthorization:ignoringCachedSigningInfo:checkingTrustCacheIfApplicable:skippingProfileIDValidation:error:]
-[MIInstalledInfoGatherer _populatePlaceholderRecordValues:signingInfo:]
IsOnMountedDiskImage
Removing bad SINF for identifier %@
CFBundleInfoDictionaryVersion
Failed to sanitize destination file path %@
-[MIInstallationIdentity writeToBundle:error:]
-[MIKeychainAccessGroupTracker init]
MIDiskImageManager
-[ICLBundleRecord isEqual:]
-[MILaunchServicesDatabaseGatherer performGatherWithError:]
enterpriseInstallURL
betaTesterType
bundleContainerURL
BundleContainer
Failed to query staged container status %@ : %@
relativeStagingBaseDirectory
Failed to construct CFBundle for moved bundle at %@: %@
com.apple.geoservices.mapdata
NSExtensionViewControllerHostClass
Validating %@ as sub-bundle of removable system app
Container for identifier %@ is not a data container; found class %ld.
AppexBundleMissingNSExtensionDict
getxattr for installType EA on %s returned %zd (expected %zu)
Data for extended attribute key %s was empty
RatingRankEligibilityDomain
WatchKitAppExtensionInDisallowedLocation
Failed to create container query for querying containers for identifier %@
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURLMatchingCurrentFileMetadata:error:]
Failed to load Info.plist from bundle %@
-[MIExecutableBundle validatePluginKitMetadataWithError:]
Failed to decode bundle metadata from %@
options dictionary parameter was not specified
-[MIGlobalConfiguration allowDeletableSystemApps]_block_invoke
Developer
-[MIFileManager validateSymlinksInURLDoNotEscapeURL:error:]_block_invoke
Failed to get list of extended attributes: %@
Failed to fetch SYSTEM persona extension marker info from plugin data container %@: %@
-[ICLWorkspace diskUsageForLaunchServicesWithBundleIDs:options:withError:]
com.apple.developer.home
MIInstallationDomain was not set to either MIInstallationDomainSystemShared or MIInstallationDomainUserPrivate: %lu
References
getxattr for xattr named %s on \"%s\" returned %zd (expected %zu)
B32@?0i8i12I16I20I24B28
altDSID
host
InstalledContentLibrary.MIAppLaunchProhibition
Failed to read persona attributes from UM
Appex bundle at %@ with id %@ defines an EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist with a value that is not a string.
Bundle at path %@ has missing or invalid CFBundleExecutable in its Info.plist
-[ICLHelperServiceClient _synchronousRemoteObjectProxyWithErrorHandler:]
extensionOwnerBundleID
Failed to remove sinf at %@ : %@
Staging destination path was too long: %s (%zu)
-[MIFileManager secureRenameFromSourceURL:toDestinationURL:destinationStatus:error:]
MaxWKVersion
__LINKEDIT segment found after LC_CODE_SIGNATURE load command in %@
-[MIExecutableBundle enumerateDylibsWithBlock:]
-[MIExecutableBundle watchKitPluginWithError:]
-[MICodeSigningVerifier _getMICodeSignerTypeFromMISInfoDict:codeSignerType:profileType:error:]
AppleID
SupportsAppMigration
-[MIGlobalConfiguration internalSupersededAppAdditionsPlistURL]
-[MIFileManager _stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:]_block_invoke
File %s has open file descriptors; cloning
AltDSID
Failed to create SecTask from audit token for pid %d
App %@ is forbidden from providing an extension of type %@
Failed to create queue
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_BACKGROUND
-[MIGlobalConfiguration hasInternalContent]_block_invoke
swift-playgrounds
temp.XXXXXX
-[MIFileManager _markEAFlag:forAppIdentifier:insecurelyCachedOnBundle:error:]
_sinfSubPaths
-[MIBundleContainerToken initWithCoder:]
Failed to deserialize SystemAppState from %@ : %@
-[MIFileManager dataProtectionClassOfItemAtURL:class:error:]
-[MIFileManager markBundleAsPlaceholder:withError:]
Failed to get bytes at beginning of %@: %@
Failed to allocate an attribute buffer!
+[MIBundle _URLOfFirstBundleInDirectory:withExtension:error:]
-[MIRelocatedBundleContainer makeContainerLiveWithError:]
Failed to create verifier for executable %@
-[MIExecutableBundle setSinfDataType:withError:]
MI_App_References
-[MIFileManager stageURLByMoving:toItemName:inStagingDir:settingUID:gid:dataProtectionClass:breakHardlinks:hasSymlink:error:]_block_invoke_2
-[MIFileManager _itemIsType:withDescription:atURL:error:]
Failed to remove underlying transient container for %@ : %@
Failed to read stash metadata from %@
-[MIBundle bundleInfoPlistSupportedPlatforms]
-[MIKeychainAccessGroupTracker _onQueue_discoverReferences]_block_invoke
Appex bundle at %@ with id %@ does not have a legal value for the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist; found: %@
is.workflow.my.app
com.apple.itunesstored
-[MIGlobalConfiguration migrationPlistURL]
Got unknown value %u for %s extended attribute on %@
com.apple.install_uuid
Unknown container status: %lu
WatchKit 2 app extension's NSExtension.NSExtensionAttributes.WKAppBundleIdentifier value does not match WatchKit app's bundle ID (found \"%@\"; expected \"%@\").
%s is unavailable on this platform
com.apple.installd.testMode
-[MIExecutableBundle _dataContainersCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]
Serialized container did not encode an identifier
-[MIContainer setInfoValue:forKey:error:]
AppleTVSimulator
Unexpectedly got nil persona for %@
Failed to create URL for last build info file.
__watchkit
+[MILaunchServicesDatabaseGatherer _createDataContainerAndSetDataProtectionForBundle:forPersona:error:]
-[MIUserManagement primaryPersonaUniqueStringWithError:]_block_invoke
Failed to save bundle URL on plugin data container %@: %@
Failed to decode stash metadata from %@
DeviceFamilyNotSupported
Failed to clone stashed item %@ to %@
Updated app extension data containers with parent bundle IDs
MIMachOSimPlatformForPlatform
Failed to read app replacement state from [
_ContainerURL
stashedAtTimestamp
bundleShortVersion
27.9999
Could not locate bundle in stashed bundle container at %@
Failed to open %s: %s
Key missing or invalid type when decoding MILocationUserDefined from plist dictionary
Appex bundle at %@ with id %@ defines a value for the \"XPCService\" key in its Info.plist that is not a dictionary.
No stash was found in bundle container %@ with index %lu (at %@)
Unknown location type
v32@?0@\"ICLBundleRecord\"8@\"NSArray\"16@\"NSError\"24
com.apple.mobilenotes
BuildMachineOSBuild
iAdAttribution
Internal error: totalProcessedEntryCount (%u) was less than reprocessCount (%u)
AlternateIconName
isResolved
Failed to get app launch prohibition state from %@ : %@
-[MIBundleContainer captureBundleByMoving:withError:]
futimes() failed for %@: %s
ValidatedByFreeProfile
Siri Intents Appex bundle at %@ with id %@ specifies a value in the IntentsRestrictedWhileLocked key's array value in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist that is not a listed in the the IntentsS
_CreateErrorForMachOBestSliceEBADARCH
DownloaderID
<%@ 0x%p uniqueInstallID=%@ installSessionID=%@
-[MIFilesystemScanner _scanFrameworkDirectory:withError:]_block_invoke
Could not read ACL text for file %@: %s
WatchKit 2 app contains a non-WatchKit extension at %@. WatchKit apps specifying a MinimumOSVersion earlier than 3.0 must have non-WatchKit extensions embedded within the WatchKit extension.
YES
Applications
-[MITestManager clearIsRunningInTestModeForProcessWithPID:withError:]
CompanionPlaceholderCaptureFailed
__DATA segment has too many sections in %@
DeviceNotSupportedByThinning
Executable at %s contained no image slices
Asked for data containers for %@ but none is needed.
-[MIBundle _validateAppNSPrivacyTrackingDomainsWithError:]
-[NSData(MobileInstallationAdditions) MI_writeAtomicallyToURL:withMode:owner:group:protectionClass:withBarrier:error:]
com.apple.web-browser-engine.networking.development
-[MIFileManager removeItemAtURL:keepParent:error:]
v32@?0@\"NSURL\"8@\"NSURL\"16^B24
Derived profile validation type %lu does not match the corresponding code signer type %lu
_OSModuleApplicationsDirectories
Failed to get keychain access groups for %@
Documents
_HasMoreThanThisOpenFileDescriptor
Ignoring extension with identifier %@ due to missing extension cache entry; continuing
/System/Library/Frameworks/CoreGraphics.framework
MIAppReplacementStatusNotApplicable
MIRecordCurrentBuildVersion
MIIsBuildUpgrade
Failed to allocate hash read buffer: %s
Removing created container for which we were unable to create an object to represent: %@
/System/Library/PrivateFrameworks/FactoryTest.framework
\"
Already have an entry in hashes dictionary for key %@
MultipleMessagePayloadProviderExtensionsFound
XRSimulator
Device capabilities do not match requirements: %@
-[MIAppIdentity _doInitWithBundleID:personaUniqueString:location:]
%d: %@
Allowing possibly ad-hoc signed binary at path %@
iTunesMetadata.plist captured from %@ has distributorInfo set; this is not allowed. Found distributorInfo: %@
Unable to find class %s
#)
-[MICodeSigningInfo initWithDictionaryRepresentation:fromSource:]
Failed to load Info.plist from bundle at path %@; %@
Appex bundle at %@ with id %@ specifies a value (%@) for the NSExtensionPointIdentifier key in the NSExtension dictionary in its Info.plist that does not correspond to a known extension point.
-[MIExecutableBundle watchKitAppExecutableHashWithError:]
ManifestCaptureFailed
Client-provided persona %@ is not among available personas on the system.
Path
@\"MIDataContainer\"32@?0@\"NSString\"8^B16^@24
CFBundleExecutable
com.apple.developer.app-management-domain
<%@ containerPath:%@>
copyfile failed for %s to %s: %s
hasOrEverHasHadIAP
com.apple.MobileInstallation.SystemAppStateQueue
-[MIExecutableBundle _discoverWatchAppBundleAsPlaceholder:error:]_block_invoke
_GetContinuationFD
IsUpdatedSystemApp
6.0
UIRequiredDeviceCapabilties in Info.plist does not have an array or dictionary value.
com.apple.mobilesms.compose
Exempting %@ from System App bundle ID conflict check because it has the System App entitlement
-[MITestManager _onQueue_setIsRunningInTestModeForProcessWithPID:withError:]_block_invoke
Failed to write sinf to %@ : %@
Failed to set value %@ for key %@ for container %@
Failed to compute hash for Info.plist at %@
-[MIDaemonConfiguration init]
codeInfoIdentifier
embedded.provisionprofile
Watch
The app extension at \"%@\" targets the extension point \"%@\" but is missing the corresponding required \"%@\" = TRUE (boolean) entitlement.
-[MIContainer setDataProtectionClass:forSecondOrThirdPartyApp:]
Couldn't get installType EA from \"%s\": %s
/System/Library/PrivateFrameworks/FindMyDeviceUI.framework
AppexBundleIllegalExtensionContextHostClass
Could not get contents of watch placeholder directory in %@
MI_Full_Fidelity_Icons
%@ 
Unique ID provided, %@, wasn't of expected length %zu
Cannot set installation identity for bundle that uses a static identity: %@
-[MIMCMContainer _doInitWithContainer:error:]
-[MIMCMContainer infoValueForKey:error:]
Skipping hardlinked file at %s
_removefile_error_callback
Failed to decode app replacement state from [
ITSWatchOnlyContainer
CoreServices app
com.apple.siri
-[MISignatureAgnosticHasher _hashSliceUsingFD:atOffset:withSize:machHeaderAndCommands:dictionaryKey:error:]
SignerOrganization
PrivateFrameworks
Failed to save parent bundle ID on plugin data container %@ : %@
The value of the UISupportedDevices key in this app's Info.plist key must contain only string values.
UIRequiredDeviceCapabilties requested value '%@' that is not a boolean for key '%@'. Only boolean values are supported. Forcing mismatch.
com.apple.WatchPlaceholder
_CreateAndPushContinuation
installDate
/private
copyfile hit ENOTSUP in source hierarchy while copying %s to %s; src mode: 0%o
_EnumerateExtendedAttributes
hasMessagesExtension
+[MIStashMetadata metadataFromURL:error:]
ReconcilingLSOperations
[%@/%@/%@]
Failed to set mode to 0%o for %s : %s
Failed to construct URLs: dataContainerURL: %@, tempURL: %@
Link needed in data container because bundle was linked against SDK version 0x%08x
com.apple.AppStore
Failed to determine destination of link at %@ : %@
Frameworks
IntentsAppexMissingIntentsSupported
Failed to set SDK version in cache on %@ : %@
-[MIFilesystemScanner _scanExtensionKitDirectory:withError:]
-[MIExecutableBundle compatibilityState]
MILocationSystemDefinedBase is currently unsupported
-[MISystemAppState _onQueue_retrieveSystemAppStateRestoringBackedUpState:]
Failed to validate binary at %@: %@. This binary may not work properly.
Failed to get code signing info for %@: %llu
The Info.plist at %@ is too large. Found %lld bytes on disk, but maximum allowed size is %lld bytes.
v24@?0@\"NSArray\"8@\"NSError\"16
Did not find at least one executable slice with CPU type %d and subtype %d in bundle %@
-[MIExecutableBundle setLaunchWarningData:withError:]
v32@?0@\"NSURL\"8@\"NSUUID\"16^B24
Failed to decode app launch prohibition from [
_writeSinfData
Failed to read %@. Error: %@
MismatchedCapabilities
-[MIExecutableBundle dataProtectionClass]
Failed to get container URL
-[MIExtensionKitBundle validateBundleMetadataWithError:]
isContainerized
Siri Intents in the WatchKit app %@ are not a subset of the Siri Intents in the companion app %@
removefile hit error for %s but we failed to get the error number
Failed to refresh persona information during init: %@
UMUserManager
+[MIContainer enumerateContainersWithClass:forPersona:isTransient:identifiers:groupIdentifiers:usingBlock:]_block_invoke
[%@/%@]
iad-impression-date
[FAIL] 
com.apple.developer.superseded-application-identifiers
+[MIBundleContainer appBundleContainerForIdentifier:temporary:inDomain:constructor:withError:]
Failed to remove iTunesMetadata: %@
com.apple.mobilemail
com.apple.social.SLGoogleAuth
Using trusted hashes from stub at %@
Failed to find runnable executable slice for \"%s\". The architectures in the file could not be determined.
DriverKit
System App
..
MILocationUserDefinedDirectory
MICopyCurrentBuildVersion_block_invoke
initiated
+[MIMCMContainer deleteContainers:waitForDeletion:error:]
%@ with identifier %@ is already installed, so we can't install %@ with that same identifier.
Stashed previous version of %@
-[MIKeychainAccessGroupTracker _onQueue_updateReferencesWithOldBundle:newBundle:error:]
Rejecting %@ -> %@, as it is points outside or to the base %@
%4d/%4d\t 0%08o\t %@\t ACL=%@
IsOnDemandInstallCapable
com.apple.security.system-group-containers
-[MIBundleContainer compatibilityLinkDestination]
MIMachOFileIterateImageSlicesFD
-[MISignatureAgnosticHasher performHashWithError:]
utility
entitlements
Could not get contents of Watch directory in %@
com.apple.developer.default-data-protection
com.apple.private.rating-rank-eligibility-domain
Failed to locate last path element in %s
alternateIconName
Expected non-NULL extensionHandle for %@
Failed to create helper log directory at \"%@\": %@
_sinfURLsForBundle
Failed to enumerate %@
No bundle found in container %@; skipping.
StoreKit
Failed to clean up %s EA on \"%s\": %s
Invalid type for metadata property %@ in %@
OriginalInstallDate
Validating sinf for %@
true
-[MIFileManager removeExtendedAttributeNamed:fromURL:error:]
Unknown:%d,%d
genreID
MIConsumeSandboxExtension
Unknown app bundle type: %d for %@
ExecutableTwiddleFailed
-[ICLHelperServiceClient stagingURLWithSandboxExtension:forUserContentWithinSubsystem:error:]_block_invoke
PersonaBundleIDMigration
CFBundleShortVersionString
isTransient
Could not get data length for extended attribute key %s: %s
dateStashed
Found unknown personas in %@ associated with %@; overriding association to %@
, sourceAppIdentity=
Attempted to set container with mismatched identifier %@ on %@
SimultaneousInstallsNumber
label
Failed to decode the nameTranscriptions dictionary.
-[MIBundle currentOSVersionForValidationUsingPlatform:withError:]
Failed to consume daemon container sandbox token: %d (%s)
17.0
%@ was grandfathered but has seatbelt-profiles entitlement
Appex bundle at %@ with ID %@ has a CFBundleShortVersionString key with a non-string value in its Info.plist
Validating executable at %@
Failed to retrieve any shared data containers for %@
v32@?0@\"NSString\"8@\"NSDictionary\"16^B24
Could not get MID-based SINF status from SINF at %@: %ld
The SINF provided for the bundle at %@ does not have a matching key in the FairPlay keybag.
Failed to verify code signature of %@ : 0x%08x (%@)
EXPrincipalClass
BackupSystemAppInstallState.plist
false
v16@?0@\"ICLAppExtensionRecord\"8
Failed to allocate %lld bytes : %s
SinfReplicationPaths array contains values other than strings; ignoring manifest at %@
Multiple WatchKit app extensions found in app but only one is allowed (found %@ ; already found %@)
_CodeSignature/CodeResources
sourceAppIdentity
Failed to delete temp container %@: %@
-[MIKeychainAccessGroupTracker _removeGroupsWithError:error:]
com.apple.private.security.no-sandbox
v32@?0@\"NSString\"8@\"MIPersonaAttributes\"16^B24
PercentComplete
Returned %zu bytes of validation memory after testing
LSApplicationLaunchProhibited
+[MIMCMContainer _allContainersForIdentifiers:groupIdentifiers:contentClass:forPersona:transient:create:created:error:]
%@ was grandfathered but has no-sandbox entitlement
This platform does not support location type 
MILoadFilteredPlist
Bundle at path %@ has %lu %@ in its Info.plist, maximum of %lu allowed
Appex bundle at %@ with id %@ specifies a value (%@) for the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist that does not correspond to a known extension point.
fts_open failed for %@ : %s
Failed to find a valid architecture for %@ at %@ : %@
App
DriverKitBundleIDSuffixContainsPeriod
libMIS returned launch warning for %@
Invalid mach_header.magic in %@ : 0x%08x
iPhoneOS
Failed to fetch container URL from %@
HasParallelPlaceholder
IntentsAppexIntentsRestrictedFormat
hasSystemGroupContainers
-[MIExecutableBundle hasOnlyAllowedWatchKitAppInfoPlistKeysForWatchKitVersion:error:]
WatchKitAppIllegalInfoPlistKey
Failed to read file at %@: %s
-[MIFileManager setDataProtectionClassOfItemAtURL:toClass:ifPredicate:error:]
iTunesArtworkCaptureFailed
categories is not an array of strings: %@
iphoneos
MobileInstallation
com.apple.MusicUIService
_CheckRealpathHasBasePrefix
Failed to get app extension bundles for bundle %@ : %@
developerName
stagingContentType
Failed to create MIExecutableBundle instance for %@ : %@
tmp
CFBundleResourceSpecification
Serialized container encoded invalid class: %llu
assetToken
isEligibleForWatchAppInstall
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_USER_INITIATED
PersonaMigrationFromUMComplete
groupContainerURLs
SAD canary file exists. No system apps will be deletable
CodeSignerType
stagingRoot
Ignoring %@ %@ because it is not applicable to this device's capabilities: %@
MultipleWatchKitAppexBundles
Unable to determine application type for %@
signatureVersion
Failed to preserve existing stashed version of app %@ at %@
-[MIFileManager mountPointForURL:error:]
GeoJSONCaptureFailed
copyfile failed in source hierarchy while copying %s to %s: %s (%d)
LinkedParentBundleID
dext
Ignoring %@ at %@ because it doesn't work on this OS version
Failed to construct path to installd daemon container
write() returned %zd but we expected %lu when writing to %s
System/Developer
Couldn't fetch list of supported device families.
firstBytes=%@ 
Failed to write SYSTEM persona extension marker on plugin data container %@: %@
Failed to set staged update container attribute for identifier %@ 
Failed to write serialized MIStashedBundleMetadata to %@
Failed to create connection to %@
ratingRank
Expected to read %zu bytes but got %ld bytes when reading %@
IntentsAppexIntentsSupportedNotASubset
-[MILaunchServicesDatabaseGatherer _setForEntry:]
betaExternalVersionIdentifier
UIDeviceFamily
app
hasSystemContainer
MultipleWatchKitTwoApps
Ignoring key INIntentsSupported for %@ because not all elements are strings: %@
-[ICLWorkspace getAppReplacementState:forBundleContainerURL:error:]
UserManager returned an empty persona list
There is nothing to generate UUID
Appex bundle at %@ with id %@ does not define the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist.
Failed to retrieve realpath for base path %@ 
Couldn't set app identifier EA on \"%s\": %s
Failed to get data container for containerized app %@ for persona %@ : %@
Object returned from _CFBundleCreateFilteredInfoPlist was not a dictionary, was type %@
-[MIPluginDataContainer setParentBundleID:]
-[MIKeychainAccessGroupTracker _keychainAccessGroupsForBundle:error:]
bundleID
+[MIMCMContainer _containerForIdentifier:contentClass:forPersona:transient:create:error:]
Failed to determine if we're running in test mode : %@
Discovered app extension without data containers %@
-[MIFileManager setPermissionsForURL:toMode:error:]
_ClearExtendedAttributes_block_invoke
Could not create certificate from data for %@
app extension
-[MIMCMContainer recreateDefaultStructureWithError:]
Failed to clear apps associated with persona %@
IsDeletable
SignerIdentity
System
MICreateSHA256Digest
1.0
Failed to write iTunesMetadata to %@
-[MIExecutableBundle _makeContainersLive:ifRequired:error:]
Expected to find PERSONAL persona data container in %@
lstat() failed for %@: %s
CPUType
hasMIDBasedSINF
Failed to check for upgrade container for identifier %@ : %@
HasSystemContainer
com.apple.developer.swift-playgrounds-app
+[MIFileManager _sanitizeFilePathForVarOrTmpSymlink:error:]
MICopyExtensionCacheEntryWithPlatform
More than one Siri Intents app extension in the app %@ declares the value %@ in the IntentsSupported array in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist.
Failed to gather stashed app record info for %@ : %@
CreatePlaceholderOption
XPCServices
InstalledContentLibrary
Failed to construct path to installcoordinationd daemon container
Failed to read ExtensionKit based app extensions for bundle %@: %@
hasSettingsBundle
Any
com.apple.developer.embedded-web-browser-engine
Failed to remove move source after copy at %s : %@
Failed to read plist from %@
Delegate unexpectedly was nil
MIInstallationDomainUnknown
Appex bundle at %@ with id %@ does not specify an Apple extension point as the value of the EXExtensionPointIdentifier key in the EXAppExtensionAttributes dictionary in its Info.plist; found: %@
__DATA
IsWebNotificationBundle
-[MIStagingRootAbsolute resolveRootWithError:]_block_invoke
/System/Library/PrivateFrameworks/AdminLite.framework
StashedAtTimestamp
%@.supp
-[MIFileManager extendedAttributesFromURL:includeCompression:error:]_block_invoke
background
14.0
UIAppFonts
com.apple.developer.default-data-protection-if-available
InvalidSymlink
-[MIFileManager captureStoreDataFromDirectory:toDirectory:doCopy:failureIsFatal:includeiTunesMetadata:withError:]
Failed to get sandbox extension for installcoordinationd's daemon container
Failed to get installation identity for %@ : %@
Failed to create sentinel file at %@ for running in test mode: %@
-[MIExecutableBundle executableImageSlicesWithError:]
WatchKit %@ app has disallowed Info.plist key: %@
Skipping app with no bundle executable at %@ : %@
Discovered %@ app without bundle container %@
-[MIExecutableBundle checkExecutableExistsIfRequiredWithError:]
com.apple.
com.apple.installd.umAccessQueue
MobileInstallationDemotionCompleteErrorOccurred
-[MIPluginDataContainer associatedBuiltInBundleURL]
App with id %@ is not in the core services app map even though it's type core services
com.apple.susuiservice
com.apple.developer.associated-appclip-app-identifiers
symlink failed for %s -> %s: %s
com.apple.installd.appIdentifier
CoreOS
sMITestMode
Could not get install type because bundle metadata could not be read from %@
Failed to sanitize source file path %@
-[MIPluginDataContainer setAssociatedBuiltInBundleURL:]
bundleContainerURL parameter was not a valid URL
Failed to serialize app replacement state for [
Failed to decode plist from %@
-[MIMCMContainer _refreshContainerMetadataWithError:]
+[MIMCMContainer defaultDirectoriesForContainerType:error:]
System/Cryptexes/OS
Could not read SINF at %@ for identifier %@: %@
com.apple.developer.memory.transfer-send
-[MIFileManager logAccessPermissionsForURL:]
title
-[MIBundle hasAtLeastOneExtensionImplementingExtensionPointIn:error:]
Failed to mkdir %s
Updating app extension data containers with their parent bundle ID
installSessionID
default
CFBundleSignature
mkdir failed for %s: %s
+[MISystemAppState _systemAppStateFromURL:]
container_copy_sandbox_token returned NULL!
staticDiskUsage
MIGetBooleanEntitlement
App extension with identifier %@ already found at path %@; ignoring discovered appex at %@
DeviceBasedVPP
isB2BCustomApp
domain
-[MIKeychainAccessGroupTracker _keychainAccessGroupsForApp:error:]
Failed to create a CFBundle instance from bundle at %@
XROS
Updated bundle %@ added ref for keychain group %@
Caches
Found WatchKit 2.0 app at %@ but it does not have a WKWatchKitApp or WKApplication key set to true in its Info.plist
%s is not a %@ (mode 0%ho)
_CallBlockForBaseItem
There is nothing to be made live
Allowing possibly ad-hoc signed binary at path %@ because we're running in test mode
NSPrivacyTrackingDomains
com.apple.DocumentsApp
removefile of %@ failed: %s
Could not get the length for extended attribute list for %s: %s
IntentsSupported
This method is not valid for MIDriverKitBundle
readlink failed for %s: %s
removefile hit error for %s : %s
Reserved %zu bytes of validation memory for testing
com.apple.message-payload-provider
-[MIDataProtectionChangeOperation _runChangeOperationWasLocked:withError:]_block_invoke_2
teamIdentifier
-[MIFileManager clearPlaceholderStatusForBundle:withError:]
Failed to remove app launch prohibition at [
Failed to get the real path of /tmp
Could not extract signer identity for %@
-[MIBundle _validateWithError:]
<%@ : path = %@ identifier = %@ type = %@>
Embedded watch apps don't get reported to Launch Services: %@
-[MIExtensionKitBundle _validateDelegateClassWithError:]
Expected to find only one or more platform slices for %@ in executable at %@ but also found other platforms: %@
Failed to set EA named %s on \"%s\": %s
ACL={ %@ } 
DriverKit extension
-[MIGlobalConfiguration OSBuildVersionWithError:]
Could not get MID-based SINF status at %@: %ld
com.apple.Faces
InstallSessionID
ApplicationMoveFailed
Expected Info.plist file at %@ but found something that was not a file (found mode 0%o).
Failed to save bundle metadata for %@. Error: %@
ThinnedAppVariantID
Setting test flags 0x%llx (0x%llx -> 0x%llx)
MIExecutableBundle.m
-[MIFileManager volumeUUIDForURL:error:]
Failed to remove previous symlink at %@ : %@
B24@?0^{?=QqQ*Q*QIIIIIIISBC}8^B16
Failed to readlink %s
-[MIFileManager debugDescriptionForItemAtURL:]
Contents
The \"NSPrivacyTrackingDomains\" key in the app's Info.plist must have an array value. An entry was found of non-array type %@.
-[MIAppIdentity resolvePersonaWithError:]
SystemAppPlaceholder
Interface-notification
com.apple.WebKit.PushBundles
The app extension at \"%@\" specifies the entitlement \"%@\" = \"%@\" where the value does not match the parent app bundle's CFBundleIdentifier, \"%@\". This entitlement, if set, must have a value that matches the bundle identifier of the p
lstat returned an error when trying to determine type for %s
Failed to read sinf at %@ : %@
FamilyID
Failed to malloc %zd bytes for extended attribute list for %s: %s
+[MIStoreMetadata metadataFromPlistData:error:]
Failed to get filtered Info.plist with keys %@ from bundle %@
appManagementDomain
Appex bundle at %@ with id %@ defines either an NSExtensionMainStoryboard or NSExtensionPrincipalClass key, which is not allowed for the extension point %@
 on a volume with UUID [
Failed to destroy aborted temp container for app %@ : %@
lseek to %lld failed: %s
AppexBundleMissingExtensionPointIdentifierString
7.0
link failed for %s to %s: %s
Multiple file provider app extensions found in app but only one is allowed (found %@ ; already found %@)
Could not create MISProfileRef from profile data of length %lu
Failed to load sinf file %@ : %@
sourceURL
Appex bundle at %@ with id %@ does not define a NSExtensionPointIdentifier key with a string value in the NSExtension dictionary in its Info.plist
Unsigned Placeholder
-[MIFileManager aclTextFromURL:error:]
This app is not compatibile with this device. This app specifies a value for UISupportedDevices in its Info.plist as [%@], but none of the identifiers in this device's compatibility list are present in this app's supported devices. This dev
BuildVersion
isWebNotificationBundle
Live container is already present %@; continuing
-[MIBundle _filterExtensionBundles:forValidationFlags:]
-[MIBundle infoPlistHashWithError:]
Failed to set owner for %s : %s
Appex bundle at %@ with id %@ defines an EXPrincipalClass key in the EXAppExtensionAttributes dictionary in its Info.plist with a value that is not a string.
-[MIExecutableBundle updateMCMWithCodeSigningInfoAsAdvanceCopy:withError:]
Validating %@ as removable system app
-[MIKeychainAccessGroupTracker _onQueue_removeReferencesForBundle:error:]
Failed to enumerate matching profile for app identifier %@: %@
-[ICLWorkspace getAppLaunchProhibition:forBundleContainerURL:error:]
-[MIBundleContainer transferExistingStashesFromContainer:error:]
-[MIFileManager deviceForURLOrFirstAvailableParent:error:]_block_invoke
shortItemName
Missing location type
-[MIBundle _filterExtensionBundlesNotInCacheIfNeeded:]
com.apple.watchkit
-[MIExecutableBundle _hasNonContainerizingEntitlement:checkSeatbeltProfiles:]
Found subgenre dictionary that did not contain both required '%@' and '%@' keys: %@
InstalledContentLibrary.MILocationUserDefinedDirectory
SupportedDeviceFamilies
com.apple.MobileInstallation.BundleMaxLinkedSDKVersion
Failed to setclass(%d) on directory %@: %s
Attempt to clone %s to %s failed with EXDEV; falling back to copyfile
lstat for path \"/\" failed, which should never happen!
Failed to read iTunesMetadata.plist from %@
B36@?0i8r^{mach_header=IiiIIII}12Q20Q28
MinimumOSVersion
Could not get downloader DSID from SINF at %@: %ld
identifier
-[MIFileManager diskUsageForURL:]_block_invoke
Ignoring app extension at %@ due to validation issue(s): %@. See previous log messages for details.
shareURL
-[MIUserManagement isKnownPersonaUniqueString:error:]_block_invoke
com.apple.MobileContainerManager.SafeHarborInfo
Lacking other hints, because the root of the bundle %@ does not have only a Contents directory, assuming this is not a MacOS app
This bundle is a placeholder and so does not have an executable, so executable image slices are not available.
Failed to get keychain access groups for new bundle %@
open failed for %s : %s
user
isUpdatedSystemApp
Failed to scan content: %@
Failed to get data containers for identifier %@ : %@
com.apple.developer.on-demand-install-capable
-[MICodeSigningVerifier performValidationWithError:]
Recorded current system version as %@ (%@)
Failed to open %s
com.apple.mobileinstallation.stash
Unexpectedly received existing container %@ when request was to create a new container for %@
EXExtensionPointIdentifier
Built in framework is expectedly missing its bundle executable.
AppexBundleIDNotPrefixed
Root sinf URL points outside of bundle
Scanned %lu items in ExtensionKit extensions dir %@
MIIsApplicableToCurrentDeviceFamilyWithError
Found no entitlements for %@ at %@
Failed to gather launch services info for %@ : %@
-[MIExecutableBundle bundleSignatureVersionWithError:]
[system-defined]
_Bool TraverseDirectoryWithPostTraversal(const char *, TraverseDirectoryOptions, TraverseDirectoryAdditionalFetchProperties, NSError *__autoreleasing *, __strong TraverseDirectoryItemBlock, __strong TraverseDirectoryPostTraversalBlock)
-[MIExecutableBundle bestEffortRollbackSinfData:]
UILaunchImageName
nil url passed to -removeItemAtURL:error:
Failed to read SAFE_HARBOR_CONTAINER_ATTRIBUTE_KEY with %@
Could not get purchaser DSID from SINF at %@: %ld
Failed to determine if %@ exists: %s
_DiscoverPersonas
This app has the same bundle ID (\"%@\") as a known deletable system app, but was signed with no entitlements at all and thus is missing the required entitlement \"%@\" = true (boolean).
Could not determine architectures in the executable at \"%s\" because the file is malformed.
XPCService
WatchKit 2 app extension's NSExtension.NSExtensionAttributes.WKAppBundleIdentifier value is missing (should be WatchKit app's bundle ID).
Platform %@ (%u) does not have a simulator equivalent; returning PLATFORM_UNKNOWN
com.apple.Diagnostics.Canary
-[MIStashMetadata serializeToURL:error:]
%@ does not have any app extensions that implement any of the required extension points for its configuration. Based on its configuration, this app must have at least one app extension that implements one of these extension points: %@.
frameworkBundleURL parameter was not a valid URL
-[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:withError:]
Removing transient bundle container: %@
-[MIFilesystemScanner _scanAppsDirectory:withError:]_block_invoke
Skipping device thinning check because of a set default
AppexBundleIllegalExtensionViewControllerHostClass
Failed to open executable at %s
com.apple.fileprovider-nonui
setattrlist failed for file %s
Failed to extract signer identity from %@
Failed to delete container_object_t for %@
Failed to set data protection class %d on %@: %@
com.apple.PhotosViewService
_ParseAttributeBuf
Failed to get bundle URL for system app with id %@
Failed to create MIExtensionKitBundle instance for %@ : %@
v32@?0@\"NSString\"8@\"NSURL\"16^B24
-[ICLWorkspace bundleRecordsWithFrameworkURL:options:withError:]_block_invoke
Library/MobileInstallation
Media/ApplicationArchives
Failed to chmod %s : %s
Failed to open file %s : %s
opendir of %@ failed: %s
skipping mount point or trigger at %s/%s
LaunchWarningData
InstallQOSOverride pref set: installations will always occur at QOS_CLASS_USER_INTERACTIVE
Failed to retrieve system group container: %llu
Failed to discover associated personas for bundle in container %@ : %@
-[MIPluginDataContainer setSystemOrAnyPersonaExtension:]
Failed to get primary persona unique string
Entry %hu in %s did not include name information even though we requested it.
Failed to get Info.plist path
Trying to fetch watchkit version for non-watchkit app %@
genreId
interactive
StashMetadata.plist
Scanned %lu apps in %@
amfi_interface_query_bootarg_state returned error %s
Missing required internal content variant
-[MIExecutableBundle updateAndValidateSinf:withRollback:error:]
Expected to move %s to %s but got EXDEV; falling back to copyfile
Discovered persona %@ type %lu mount %@
This app has the %@ key set in its Info.plist, which identifies it as a shell app surrounding a Watch-only app; these are not installable.
NSExtensionPrincipalClassProhibited
read failed for %s, got %lld bytes
MI_Persona_BundleID_Relayering
sinf subpath %@ is absolute
MissingBundleIdentifier
i
UIPrerenderedIcon
copyfile of %@ to %@ failed: %s
/tmp/
SourceFileLine
Extra info about \"%@\": 
Did not validate all slice hashes on executable %@; unchecked hashes: %@
md5
WKCompanionAppBundleIdentifier
-[ICLWorkspace enumerateBuiltInSystemContentWithBlock:error:]_block_invoke_3
PathArgument
com.apple.developer.browser.app-installation
Failed to get plugin data containers for app extension %@ in bundle %@ for persona %@ : %@
SkipThinningCheck
Failed to remove profile for app identifier %@: %@
Expected to create/fetch only one container for %@ with persona %@, but got %ld
ProfileType
Failed to get ACL: %@
gameCenterEverEnabled
groupContainers
Failed to lstat %@ : %s (%d) (may require significant memory usage to validate this app)
Failed to delete partially created container %@ : %@
+[MIMCMContainer _enumeratorWithContainerClass:forPersona:isTransient:identifiers:groupIdentifiers:create:usingBlock:]
-[ICLAppRecord isEqual:]
UILaunchImageMinimumOSVersion
ICLSoftLinking.h
Restoring backed up system app state following a restore: %@
is-purchased-redownload
(%@-%@)
SystemExtensions
-[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:personas:addingToBundleSet:enumeratingEntry:withError:]
Appex bundle at \"%@\" with identifier \"%@\" contains a '.' in the portion after the parent app's prefix (prefix: \"%@\" ; dot in: \"%@\").'
stat of %s failed: %s
Ignoring copyfile error in source hierarchy while copying %s to %s: %s (%d)
-[MIGlobalConfiguration _bundleIDMapForBundlesInDirectory:withExtension:loadingAdditionalKeys:]_block_invoke
-[MIExecutableBundle hasExecutableSliceForPlatform:error:]
com.apple.accessory-transport-extension
<%@<%p> installDate=%@, originalInstallDate=%@ installBuildVersion=%@, installType=%lu, placeholderFailureReason=%lu, placeholderFailureUnderlyingError=%@, placeholderFailureUnderlyingErrorSource=%lu, watchKitAppExecutableHash=%@, autoInsta
CompatibilityState
Failed to verify code signature for this system app, %@. Because of that, we don't have entitlements or signing info so we'll assume that it requires a container.
itemId
NSExtensionPointVersion
CFBundleSupportedPlatforms
Posted downgrade notification with userInfo %@
system app placeholder
-[MIMCMContainer setInfoValue:forKey:error:]
ApplicationDSID
Successfully created the sentinel file for running in test mode: %@
NSUserActivityTypes
-[MIFileManager copyVolumeInfo:forURL:error:]
Could not get the product version from MobileGestalt.
FTS returned error for %s : %s
-[ICLBundlePersonaRecord isEqual:]
Removing orphaned transient bundle container %@
Unexpectedly was not passed personas for app bundle %@ in container %@
com.apple.installd.appclip
v40@?0r^{mach_header=IiiIIII}8Q16Q24^B32
Failed to create MIContainer instance for %@
NSExtensionPointName
beta-reports-active
-[MIBundleContainer cloneContentFromStashedBundleContainer:error:]_block_invoke
v20@?0I8^B12
redownload-params
Failed to get group container path for group 'systemgroup.com.apple.installcoordinationd'; container_system_group_path_for_identifier returned %llu
open() failed for %@: %s
Failed to renameatx_np() for source fd %d path \"%@\" to destination fd %d path \"%@\" with flags 0x%x, Error: %s
-[MIStoreMetadataDistributor initWithDictionary:]
-[MIExecutableBundle _dataContainerCreatingIfNeeded:forPersona:makeLive:checkIfNeeded:created:error:]
No WatchKit extension found
com.apple.installd.installType
-[MIStoreMetadata initWithDictionary:]
downloaderID
Failed to clear staged update container attribute for identifier %@ 
%@ is in the deny list
-[MIRelocatedBundleContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:]
MismatchedBundleIDSigningIdentifier
-[MIExecutableBundle isWatchOnlyApp]
system app
Locally signed apps are unrestricted because boot-args are set
Failed to get app replacement state from %@ : %@
Failed to copy the OS build version
Failed to get DriverKit support version: %s
Installation domain %@ does not map to a container class.
-[MIFileManager itemExistsAtURL:error:]
ParentIdentifiers
Failed to resolve persona %@
Appex bundle at %@ with id %@ does not define an NSExtension dictionary in its Info.plist
Code signing identifier (%@) does not match bundle identifier (%@) for %@
CFBundleLocalizations
app identity has nil bundle identifier
codeSigningInfoNotAuthoritative
-[MIExecutableBundle watchKitV2AppBundleWithError:]
Serialized container did not encode bundleURL for bundle in container %@
CFBundleNumericVersion
getmntinfo_r_np failed: %s
, 
Found multiple personas associated with %@; persona resolution is ambiguous. Found: %@
Error getting disk usage for %@ (%ld): %@
%d: %@ (%@:%ld %@)
appleID
-[ICLHelperServiceClient resolveStagingBaseWithSandboxExtension:forVolumeUUID:withinStagingSubsystem:error:]_block_invoke
Failed to make app extension %@ executable: %@
Failed to issue write barrier for %s : %s (%d)
Setting protection class of %s to %d
Failed to lchown %s : %s
gMfFfUYLxpniCKUmtjSz0XLrXGs=
Got nil linkDestination and oldLinkDestination; not doing anything
+[MIBundleMetadata metadataFromURL:error:]
User
AppexBundleMissingEXPrincipalClassString
xrsimulator
Extension cache does not define an NSExtension dictionary in its Info.plist: %@
.
Expected '%@' array element to be a dictionary.
PluginOwnerBundleID
SignatureVersion
WKWatchOnly
com.apple.mobile.installation
SerializedPlaceholderPath
UPPValidated
Couldn't open bundle \"%s\" for setting extended attributes: %s
-[MIFileManager _insecureCachedAppIdentifierIfMarkedWithEAFlag:bundleURL:allowPlaceholders:error:]
Unexpectedly received a nil rawContainer (MIMCMContainer)
WKApplication
Failed to get PluginKit bundles for app %@: %@
PersonalPersonaPlaceholderString
AppReplacementState.plist
getpwuid_r failed for uid %d : %s
-[MIKeychainAccessGroupTracker _onQueue_addReferencesForBundle:error:]
AppexBundleIllegalXPCServiceDict
stashOriginalInstallTimestamp
Extension cache does not have an entry for %@
UninstalledAppInfoArray
Failed to find container of class %llu with identity %@/%@
More than one Siri Intents UI app extension in the app %@ declares the value %@ in the IntentsSupported array in the ExtensionAttributes dictionary in the NSExtensionDictionary in its Info.plist.
IsAdHocSigned
com.apple.AppClips
installType
-[MIBundle validatePluginKitMetadataWithError:]
HasMIDBasedSINF
Session ID provided, %@, wasn't of expected length %zu
placeholderFailureUnderlyingError
Failed to read container error path
acl_copy_ext_native returned size %zd which was more than we had allocated (%zd)
 that expects paths on a volume with UUID [
Failed to get existing container when replacement found the live container was already present for %@
MIAppReplacementStatusCompleted
Failed to read app launch prohibition from [
com.apple.intents-ui-service
storeCohort
MILocationUserDefined
+[MIAppIdentity validateAppIdentity:withError:]
purchaseDate
ApplicationSINFCaptureFailed
Allowing patch installation without sinf present in options
void *ExtensionFoundationLibrary(void)
InstallDeviceClasses
Failed to discover bundles in directory %@
Failed to move clone replaced file from %@ to %@
nameTranscriptions
com.apple.managed_drm_id
bundleURL
/System/Library/PrivateFrameworks/Pasteboard.framework
protectedMetadata
MobileInstallationDemotionCompleteNotification
Failed to find any app with bundle ID %@
Failed to resolve staging root for unknown staging content type
TMPDIR
dataContainerURL
-[MIFileManager _stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:]
Unexpected staging mode: %d
UIRequiredDeviceCapabilities
-[MIContainer makeContainerLiveReplacingContainer:reason:waitForDeletion:withError:]
NonAllowedAppexTypeFoundInMessagesStubApp
-[MIAppIdentity _eligiblePersonaForBundle:error:]
AppexBundleUnreadableExecutable
com.apple.Home.HomeUIService
softwareVersionBundleId
Failed to allocate a continuation!
Load command %d exceeds bounds in %@
Could not stat %@ : %@
NSExtensionAttributes
-[MIExecutableBundle makeExecutableWithError:]
/System/Library/PrivateFrameworks/AirPlayDiagnostics.framework
Exiting before replacing transient bundle container: %@
GroupContainers
-[MIAppExtensionBundle validateHasNoDotInBundleIDSuffix:]
+[MILaunchServicesDatabaseGatherer fetchInfoForBundle:forPersonas:inContainer:withError:]_block_invoke
ServiceType
IntentsAppexIntentsRestrictedNotSubset
WatchKit version enum value %hhu is no longer supported
_checkIdentifierForConflict
-[MIBundleContainer _bundleExtensionForContainerClassWithError:]
StageCreationFailed
regular file
com.apple.WK
got error while processing entry %hu in %s : %s
isMissingRequiredSINF
B12@?0i8
com.apple.web-browser-engine.rendering.development
lstat of %s failed: %s
Expected value to be a valid array.
AppLaunchProhibition.plist
Made safe harbor container active for %@ at %@
com.apple.web-browser-engine.networking
Unknown location type [
fsync failed for %s : %s (%d)
Got unexpected bundle type for persona discovery: %@
Consumed sandbox token %lld for container at %@
MIInstallationDomainDefault
No WatchKit 2.0 placeholder found for app %@
com.apple.developer.accessory-transport-extension
Ignoring symlink at %s
InvalidSupportedDevices
Failed to get keychain access groups for old bundle %@
-[MIExecutableBundle _hasNoConflictWithSystemAppsForSigningInfo:error:]
BundleContainer can't be created for container type %llu
-[MIFileManager realPathForURL:ifChildOfURL:]
keyCount=%lu 
v20@?0I8I12I16
Failed to release sandbox token %lld for container %@
-[ICLHelperServiceClient stagingURLWithSandboxExtension:forSystemContentWithinSubsystem:error:]_block_invoke
deviceBasedVPP
B24@?0*8Q16
Array of supported device families returned from MobileGestalt was not an array of numbers; got: %@
macho_for_each_slice_in_fd failed for %s
Failed to get parent bundle ID for plugin data container %@ : %@
CoreServices
%@ contains a placeholder watch app, so an executable hash is not possible.
Verifying signature of %@ with options %@
Failed to create MIStoreMetadataSubGenre instance
_IsDictionaryWithKeyStringAndValueArrayOfString
Hashed more (%lld) than slice length %llu in %@
Discovered %@ app without data container %@
targetDirectoryURL
hasIdentifiedBundle
-[MIInstalledInfoGatherer _stashedAppRecordForStashedContainer:]
Unexpectedly found a second watch app, \"%@\", in this app's \"%@\" directory when we had already found \"%@\" in that directory. An iOS app may only have one embedded watch app.
-[MIBundleContainer initWithContainerURL:expectAppWithin:error:]
itemName
purchasedRedownload
internal app
Unexpectedly asked to validate thinning on a non-app bundle %@
xpc_user_sessions_get_foreground_uid() failed with error %d - %s
CFBundleVersion
B16@?0r*8
-[ICLPlaceholderRecord isEqual:]
Could not get install type because no bundle container relation is set on %@
This app was not built to support this device family; app is compatible with %@ but this device supports %@
AppexBundleIllegalEXPrincipalClassString
SystemAppInstallState.plist
System/Library/AppSignatures
com.apple.developer.wrapper-bundle
MIReserveMemoryForValidation
/System/Library/Frameworks/JavaScriptCore.framework
Failed to get sandbox extension for installd's daemon container
Failed to remove the source contents at %@ after a successful swap : %@
subgenres
isDeletable
SkipDeviceFamilyCheck
v24@?0@\"NSSet\"8@\"NSError\"16
-[MITestManager setIsRunningInTestModeForProcessWithPID:withError:]
com.apple.social.SLYahooAuth
Did not find any placeholder entitlements in %@
Journal
App with id %@ is not in the internal app map even though it's type internal
The appex bundle at %@ does not have a bundle executable at %@. App extensions must have an executable.
com.apple.developer.wifi-infrastructure
Failed to read iTunesMetadata from %@ : %@
distributorDomain
Failed to save content protection class value on data container %@ : %@
appletvsimulator
Appex bundle at \"%@\" with identifier \"%@\" does not have expected identifier prefix \"%@\"
-[MIFileManager createSymbolicLinkAtURL:withDestinationURL:error:]
File %s is multiply linked; cloning
MIGetSinfDataType
Unknown error: 0x%x
v32@?0@\"NSString\"8@\"NSString\"16^B24
removefile_state_set REMOVEFILE_STATE_ERROR_CONTEXT failed: %s
Failed to read %zu bytes : %s
No root sinf found to replicate at %@
_DiskImageApplicationsDirectories
com.apple.installcoordinationd
LaunchServicesOperations
Failed to copyfile %s to %s
Couldn't stat %@: %s
Failed to find LC_CODE_SIGNATURE load command in %@
Failed to get metadata from %@ : %@
EnvironmentVariables
-[MIDriverKitBundle validateBundleMetadataWithError:]
MISetSinfDataType
com.apple.installd.placeholder
Could not extract signer organizations for %@
Attempting to assume an identity of 0/0, which should be the default for the helper service
Failed to get Info.plist URL from %@; falling back to assumed path
-[MIDaemonConfiguration localSigningIsUnrestricted]_block_invoke
Client provided invalid persona for %@
PluginKit plugin with identifier %@ already found at path %@; ignoring discovered plugin at %@
24B
Error returned while calculating size under %@ : %@
fApr4oevAMrl65iFf3wAhUqJIOk=
Failed to get signing identifier from SecTask for pid %d
MultipleFileProviderAppexBundles
Skipping socket encountered at %s
localizedDistributorName dictionary does not have expected type
softwareVersionBundleID
+[MIBundle bundlesInParentBundle:subDirectory:matchingPredicate:error:]
IMPORTANT: Detected Internal release type but os_variant_allows_internal_security_policies returned false
App extension with identifier %@ already located; keeping that instead of new one found at %@
+[MIContainer containersForIdentifier:groupContainerIdentifier:ofContentClass:forPersona:fetchTransient:createIfNeeded:created:error:]
Failed to create bundle for %@ : %@
com.apple.private.security.no-container
kind
MIMCMContainer's superclass -init returned a nil self
NSExtensionContextClass
The system version is lower than the minimum OS version specified for bundle at %@. Have %@; need %@
System/Cryptexes/App
com.apple.developer.web-browser
mkdir of %@ failed: %s
pthread_setugid_np failed for uid %d gid %d; error %d (%s)
%@ is missing its bundle executable. Please check your build settings to make sure that a bundle executable is produced at the path \"%@\".
_WatchKitStub/WK
sinf subpath %@ contains illegal '..' segment
<%@<%p> dateStashed=%@ dateOriginallyInstalled=%@>
%@ is not expected to contain watch app executables
Found empty entitlements for %@ at %@
distributorAccountID
Could not locate platform for %@ string value \"%@\"
com.apple.AskPermissionUI
Appex bundle at %@ with id %@ does not have a legal value for the NSExtensionPointIdentifier key in the NSExtension dictionary in its Info.plist; found: %@
LSEligibilityUninstallPredicate
Could not extract dictionary from %@: %@
Could not append element \"%s\" of length %zd to path \"%s\" because it would make the path longer than MAXPATHLEN
LibMISErrorNumber
Failed to clear test mode %@ when %d exited
Updating MCM with signing info for %@ : %@; options %@
%s
+[MICodeSigningInfo signingIdentifierForAuditToken:error:]
MIInstallationDomainUserPrivate
-[MIBundleContainer cloneContentFromStashedBundleContainer:error:]
Rejecting %@ with base %@ (reals %@ ; %@) because components diverge at %@ != %@
rank
Expected '%@' element to have a string value for '%@'.
re6Zb+zwFKJNlkQTUeT+/w
driverkit
not 
-[MITestManager _onQueue_setIsRunningInTestModeForProcessWithPID:withError:]
Unable to compute relative executable path from base URL: \"%@\" executable URL: \"%@\"
Failed to get container URL from %@
directory
Rejecting %@ with base %@ because real component counts don't make sense (reals %@ ; %@)
PlugIns
Invalid
-[ICLWorkspace enumerateBuiltInSystemContentWithBlock:error:]
iad-conversion-date
iAdImpressionDate
Failed to rename %s to %s : %s
com.apple.private.webkit.pushbundle
+[MILaunchServicesDatabaseGatherer _createPluginDataContainersForAppexBundle:forPersona:setParent:didUseProvidedPersona:containedInAppBundle:]
-[MIUserManagement _onQueue_refreshPersonaInformationWithError:]
Failed to open %s : %s
In test mode, forcing code signing enforcement to be enabled
extendedAttributes=%@ 
Failed to malloc %zd bytes for extended attribute key %s: %s
Proxy returned error: %@
-[ICLAppExtensionRecord isEqual:]
watchKitAppExecutableHash
embedded watch app
Bundle URL missing in info for %@
app identity is nil
Failed to allocate memory for deleting containers
-[MITestManager _onQueue_clearIsRunningInTestModeForProcessWithPID:withError:]
com.apple.web-browser-engine.content
Could not get current build info; assuming this is an upgrade
SigningInfoSource
Deserialized SystemAppState dictionary from %@ did not contain only string keys and number values
Underlying errno set by container manager is %s
@\"MIBundleContainer\"24@?0@\"MIMCMContainer\"8^@16
<%@ platform:%@ sdkVersion:%u minOSVersion:%u>
-[MIContainer dealloc]
CodeInfoIdentifier
-[MIContainerToken initWithCoder:]
dirfd of %s failed: %s
secondaryGenreID
-[MIDataContainer makeSymlinkToBundleInContainerIfNeeded:]
personaUniqueString
ICLWorkspaceErrorDomain
Rejecting \"%s\" because its realpath \"%@\" points outside or to the base %@
iTunesMetadata.plist was not a dictionary; found class %@
MIPlaceholderArchitectures
*I
Unknown filesystem object type %u encountered at %s
The suspicious path %@ contains '..' paths, which are invalid
+[MICodeSigningVerifier _validateStubSignature:withSigningID:error:]
init()
isSwiftPlaygroundsApp
WatchOS
Extension point identifier was not set for app extension with bundle ID \"%@\".
The persona unique string %@ does not correspond to any known persona on this system.
INIntentsSupported
OSMinimumDriverKitVersion
Unknown WatchKit version enum value %hhu
ACL=<not found> 
id
Failed to create sinf directory at %@ : %@
com.apple.Preferences
Returning cached code signing info for %@
Failed to create URL for %s
purchaserID
-[MISignatureAgnosticHasher performHashWithError:]_block_invoke
This bundle does not have an executable, so executable image slices are not available.
Class getEXExtensionPointCatalogClass(void)_block_invoke
app identity has nil location
-[MICapabilitiesManager checkCapabilities:withOptions:error:]
Could't remove placeholder EA on \"%s\"
Could not determine architectures in the executable at \"%s\" because the file is not a mach-o format file.
InvalidiTunesMetadataPlist
supportsAppMigration
ValidatedByUPP
watchsimulator
Container
System App XPC Service
Ignoring copyfile error at %d while copying %s to %s: %s (%d)
INTERNAL-ONLY BEHAVIOR: allowing bundle at %@ despite its ad-hoc signature because boot-args allow it to be runnable.
This app has the same bundle ID (\"%@\") as a known deletable system app but is missing the required entitlement \"%@\" = true (boolean).
identity
Appex bundle at %@ with id %@ does not define a NSExtensionPointVersion key with a string value in the NSExtensionAttributes dictionary in the NSExtension dictionary in its Info.plist
-[MIRelocatedBundleContainer purgeContentWithError:]
com.apple.developer.web-browser-engine.webcontent
MIMachOFileMatchesMyArchitecture
Could not get access to staging directory
v32@?0@8@16^B24
lstat of %@ failed
WatchOnlyAppContainerNotInstallable
_installd
subgenre
v32@?0@\"NSString\"8@\"NSArray\"16^B24
sinf subpath %@ points outside of bundle
-[MIUserManagement systemPersonaUniqueStringWithError:]_block_invoke
Got value for %s extended attribute on %@ with unexpected length %lu
MIAppReplacementStatusInProgress
PrincipalClass
-[MIInstalledInfoGatherer _populateBundleRecord:error:]
systemgroup.com.apple.mobile.installationhelperlogs
invalid symlink at %s
Failed to create a continuation
UISupportedDevices
[f]getxattr failed to get length for xattr named %s path %s fd %d
com.apple.TestFlight
WKRunsIndependentlyOfCompanionApp
CFBundleGetInfoDictionary failed for bundle at %@
com.apple.MobileContainerManager.StagedUpdateContainer
-[MIDaemonConfiguration codeSigningEnforcementIsDisabled]_block_invoke
+[MICodeSigningVerifier _validateBundleExecutable:againstStubAt:trustedHashes:sectionName:signingIdentifier:error:]
/System/Library/PrivateFrameworks/AppleSauce.framework
System/Library/ExtensionKit/Extensions
-[MIExecutableBundle watchKitAppRunsIndependentlyOfCompanion]
CFBundlePackageType
com.apple.private.mobileinstall.xpc-services-enabled
-[MIDataContainer _oldCompatiblityLinkDestination]
Testing
-[MIInstalledInfoGatherer _sandboxEnvironmentForDataContainer:]
Unknown MIInstallationDomain: %lu
options parameter was not a dictionary
DeviceOSVersionTooLow
RequiredOSVersion
is-auto-download
com.apple.app-migration
com.apple.installd
Removing reference in %@ for %@
B16@?0^{container_object_s=}8
Failed to clear code signing cache: %llu
MIAppReplacementStatusRefused
WatchKitAppInvalidInfoPlistKey
 with a source app identity to [
Failed to locate system persona: UserManagement returned %lu personas but none of them had isSystemPersona = YES
Deserialized container object had identity %@/%@ but the token was for %@/%@
-[MIBundle thinningMatchesCurrentDeviceWithError:]
_ReadFile
InstalledContentLibrary.MIAppReplacementState
TraverseDirectoryWithPostTraversal
CLKComplicationPrincipalClass
com.apple.MobileContainerManager.ParentBundleID
opendir of %s failed: %s
supportPageURL
Failed to set symlink name attribute on container %@: %@
An error occurred when reclaiming disk after replacing a container of class %ld with identifier %@ : %@
container_operation_delete_array returned NULL but did not set an error
AppexBundleIllegalExtensionContextClass
-[MIExecutableBundle _installEmbeddedProvisioningProfileAtURL:withProgress:]
DSPersonID
Failed to get XPC services in app %@
System/Library
DriverKit extension bundle at \"%@\" with identifier \"%@\" does not have expected identifier prefix \"%@\"
-[ICLHelperServiceClient _remoteObjectProxyWithErrorHandler:]
MIAppReplacementStatusUnknown
InternalSupersededAppAdditions.plist
-[ICLInstallationDaemonClient _sharedConnectionWithError:]
-[MIBundleMetadata serializeToURL:error:]
MissingBundleExecutable
%lu
Failed to create stash base directory at %@
-[MIFileManager _moveItemAtURL:toURL:failIfSrcMissing:error:]
-[MIFileManager itemDoesNotExistAtURL:]
Temporary
Failed to get data container for bundle %@ for persona %@ : %@
IMPORTANT: Detected Internal release type but os_variant_has_internal_content returned false
Pref set to ignore code signing enforcement boot-args
isOnMountedDiskImage
Failed to write serialized app replacement state to [
InstalledContentLibrary.MILocationSystemDefinedBase
DiskUsageBytes
MIRemoveSinf
WatchKitAppExtensionAttributesInvalidAppBundleID
Failed to calculate hash on watchkit app executable for %@. Error: %@
softlink:o:path:/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
softlink:r:path:/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
Got memory size to return, %zu, which would result in %zu available, which is more than the maximum of %zu bytes; capping at max available
Failed to get installd daemon container: %@
%s: container_copy_sandbox_token returned NULL!
Scanning plugins in bundle at %@
Done scanning plugins in bundle at %@
Mark DriverKit extensions in bundle as executable at %@
[FAIL] Done scanning bundle at %@
Scanning framework at %@
Failed to get installcoordinationd daemon container: %@
getpwnam_r succeeded but no user was found with name %s
%s: Attempting to restore an identity without having first assumed an identity
pthread_setugid_np failed to restore root privs from %u/%u; error %d (%s); aborting because this thread is in a bad state.
GenerateDict
ScanBundle
%s: Platform %@ (%u) does not have a simulator equivalent; returning PLATFORM_UNKNOWN
%s: Attempting to assume an identity of 0/0, which should be the default for the helper service
Generating ICL bundle record for %@
[FAIL] Done scanning plugins in bundle at %@
Scanning bundle at %@
Expected at least %zu bytes of memory for validation but found %zu bytes
%s: Failed to release sandbox token %lld for container %@
%s: Expected non-NULL extensionHandle for %@
%s: Failed to release sandbox token %lld for %@ : %s
%@Done generating ICL bundle record for %@
%s: Expected to move %s to %s but got EXDEV; falling back to copyfile
%s: Attempt to clone %s to %s failed with EXDEV; falling back to copyfile
MarkDriverKitExtensionsExecutable
getpwnam_r failed for user %s : %s
Got validation memory usage of %zu bytes which is greater than our available memory of %zu bytes (while validating %@); hoping for the best
Done scanning bundle at %@
Done scanning framework at %@
[FAIL] Done scanning framework at %@
Expected headroom in installd (%zu) must be less than expected jetsam limit (%zu) in installd
[FAIL] Done marking DriverKit extensions in bundle as executable at %@
Got memory size to return %zu which is greater than our available memory of %zu bytes; capping at max available
%s: Unexpectedly got nil persona for %@
Unexpectedly called base class implementation of %s
ScanPlugins
Done marking DriverKit extensions in bundle as executable at %@
Failed to get home dir path size: %s
MIPersonaAssociation
MILocation
MIInstallationIdentity
MobileInstallationAdditions
MIFilesystemScanner
MIBundleMetadataProvider
ICLHelperServiceClient
NSCoding
MIStagingRootProtocol
MIDataProtectionChangeOperation
MICodeSigningVerifier
MIAppReplacementState
MILocationProtocol
MIStagingLocation
MIRelocatedBundleContainer
MIDaemonConfiguration
ICLSinfInfo
MobileInstallerProtocol
NSFastEnumeration
ICLBundleRecord
ICLWorkspace
MIStashedBundleContainer
MIFilesystemScannerDelegate
MIBundleMetadata
MICodeSigningInfo
ICLBundlePersonaRecord
MIGlobalConfiguration
MIBundleContainer
MIStoreMetadataDistributor
NSSecureCoding
ICLStashedAppRecord
MIPersonaContainerSet
MIFileManagerCopyfileContext
MIFileManager
MILocationSystemDefinedBase
MobileInstallationHelperServiceProtocol
ICLPlaceholderRecord
ICLSystemAppPlaceholderRecord
MIContainerToken
MILaunchServicesDatabaseGatherer
MIStagingRootAbsolute
ICLFrameworkRecord
MIEmbeddedWatchBundle
MICapabilitiesManager
ICLAppExtensionRecord
MIContainer
MIBundle
MIContainerQueryResult
MIMCMContainer
MIPluginKitBundle
MIGroupContainer
NSCopying
MIPluginDataContainer
MIKeychainAccessGroupTracker
MIExtensionKitBundle
ICLInstallationDaemonClient
MIDataContainer
MILocationUserDefinedDirectory
MILocationUserDefined
MIUserManagementDaemonContainerResolver
MIBundleContainerToken
MIAppIdentityPersonaResolver
MIInstalledInfoGatherer
MIPersonaAttributes
MIDriverKitBundle
ICLFeatureFlags
MIStoreMetadata
MIAppIdentity
MIUserManagement
MISignatureAgnosticHasher
MIStashMetadata
MIStagingRootVolumeUUID
ICLRegistrationOptions
InstalledContentLibrary
MILocationSystemDefinedCommon
NSObject
MISystemAppState
ICLUninstallRecord
ICLAppRecord
MITestManager
MIExecutableBundle
MIAppExtensionBundle
MIStoreMetadataContentDescriptor
MobileInstallerDelegateProtocol
MIMachOImageSlice
MIStoreMetadataSubGenre
MIPersonaAssociationLocalResolver
MIAppLaunchProhibition
T@\"NSString\",&,N,V_systemPersonaUniqueString
alternateThinningModelIdentifier
internalLibraryDirectory
setSystemAppStateList:
T@\"NSString\",R,C,N,V_signerOrganization
_filterExtensionBundlesNotInCacheIfNeeded:
componentsSeparatedByString:
setAppClipAppIdentifier:insecurelyCachedOnBundle:error:
setCodeSigningInfoNotAuthoritative:
isEqualWithLocationUserDefined:
packedNumberForCPUType:subtype:
T@\"NSURL\",C,N,V_parallelPlaceholderURL
_personaVolumeUUIDToDaemonContainerMap
_stagingSubsystem
setXpcConnection:
getIsBuiltForiOSPlatform:error:
T@\"NSNumber\",&,N,V_initialODRSize
parentBundle
getPidForTestingWithCompletion:
T@\"NSString\",C,N,V_genre
boolForKey:
isFactoryInstall
setItemID:
setSupportsPAC:
_compatibilityState
_lock
initWithPersonaString:personaType:associatedBundleIDs:dataBackedPersona:systemPersona:volumeDaemonContainer:volumeDaemonContainerSandboxExtension:
setGroupContainerURLs:
setInstallBuildVersion:
T@\"NSDate\",C,N,V_originalInstallDate
TB,N,V_isSwiftPlaygroundsApp
_loadSystemDetachedSignatureForBundleID:error:
_stageURLByCopying:toItemName:inStagingDir:stagingMode:settingUID:gid:dataProtectionClass:hasSymlink:error:
_xpcServiceBundles
allPersonaVolumeDaemonContainersMapWithError:
downloaderID
fetchDiskUsageForIdentifiers:withOptions:completion:
parentBundleURL
_platformHint
builtInFrameworkBundleIDs
nsExtensionPointIdentifier
pluginKitBundlesWithError:
setInfoPlistSubsetForTesting:
_contentDescriptors
TQ,N,V_profileValidationType
createSymbolicLinkAtURL:withDestinationURL:error:
dataWithBytes:length:
removeUnderlyingContainerWaitingForDeletion:error:
setApplicationDSID:
_validateBundleExecutable:againstStubAt:trustedHashes:sectionName:signingIdentifier:error:
purgeTransientBundleContainersWithError:
T@\"NSDictionary\",R,C,N,V_internalAppBundleIDToInfoMap
T@\"NSNumber\",&,N,V_itemID
setIsTransient:
T@\"NSNumber\",&,N,V_purchaserID
T@\"NSURL\",C,N,V_serializedPlaceholderURL
_extensionAttributes
setTestFlags:
stringWithFileSystemRepresentation:length:
_bundleMetadata
T@\"NSString\",C,N,V_signerIdentity
TB,N,V_gameCenterEverEnabled
_ixDataStorageDirectoryPath
acquireReferenceforInstalledAppWithIdentity:inDomain:matchingInstallSessionID:completion:
_validatePresenceOfSwiftEntrySectionInExecutable:shouldHaveSwiftEntry:withError:
daemonContainerForPersona:error:
defaultWorkspace
initWithDomain:code:userInfo:
_skipDeviceFamilyCheck
allowDeletableSystemApps
T@\"NSString\",C,N,V_variantID
TB,R,N,V_skipDeviceFamilyCheck
builtInApplicationBundleIDs
itemIsFIFOAtURL:error:
setIsInstallationHoldActive:
_associatedPersonaUniqueStrings
T@\"NSString\",R,N,V_personaUniqueString
isDataBackedPersona
removeObject:
setBundleShortVersion:
setObject:forKey:
builtInAppParallelPlaceholderBundle
contentProtectionClass
postNotificationName:object:userInfo:options:
T@\"NSURL\",R,N,V_rootPath
_iAdImpressionDate
maxLinkedSDKVersion
ratingRankEligibilityDomain
sinfDataTypeIsSet
isSystemPersonaAppWithBundleID:
_allContainersForIdentifier:persona:options:error:
_bundleName
allContainersForIdentifier:persona:options:error:
init
retain
setNameTranscriptions:
volumeUUIDForURL:error:
T@\"NSURL\",R,N,V_installdPath
currentUserLaunchServicesOperationLookAsideStorageBaseURL
isApplicableToCurrentDeviceCapabilitiesWithError:
```
