# `/System/Library/Frameworks/CoreServices.framework/CoreServices`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 5,209,888 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 35 (Size: 5728)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (16)

- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0)`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libicucore.A.dylib (compatibility version 1.0.0, current version 78.1.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore (compatibility version 1.0.0, current version 1141.1.0)`
- `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration (compatibility version 1.0.0, current version 1453.40.1)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8, upward)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78, upward)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (261 classes, 48 protocols)

Classes: `CSStoreAttributedStringWriter`, `FSMimic`, `FSMimicPopulator`, `FSNode`, `ICLAppExtensionRecord`, `ICLBundleRecord`, `ICLPlaceholderRecord`, `LSATTrackingEnforcementManager`, `LSAltIconManager`, `LSAppClipMetadata`, `LSAppLink`, `LSApplicationExtensionRecord`, `LSApplicationIdentity`, `LSApplicationIdentityEnumerator`, `LSApplicationIdentityMigrationResult`, `LSApplicationIdentityMigrator`, `LSApplicationProxy`, `LSApplicationRecord`, `LSApplicationRestrictionsManager`, `LSApplicationWorkspace`, `LSApplicationWorkspaceObserver`, `LSApplicationWorkspaceRemoteObserver`, `LSAskManagerMCStateProvider`, `LSBuiltinApplicationRegistrant`, `LSBuiltinPluginRegistrant`, `LSBundleDataContainerMap`, `LSBundleGroupContainerMap`, `LSBundleIdentity`, `LSBundleInfoCachedValues`, `LSBundlePersonaAssociationResult`, `LSBundlePersonaRecordMap`, `LSBundleProxy`, `LSBundleRecord`, `LSBundleRecordBuilder`, `LSBundleRecordUpdater`, `LSBundleRegistrationStatePrecondition`, `LSBundleSetContainersOperation`, `LSBundleSetPersonaAssociationOperation`, `LSBundleURLRelationshipPrecondition`, `LSByURLBundleUnregistrant`, `LSByURLPluginUnregistrant`, `LSClaimBinding`, `LSClaimBindingBindable`, `LSClaimBindingConfiguration`, `LSClaimRecord`, `LSCleanReferencesToPersonaOperation`, `LSContainerCache`, `LSDBExecutionContext`, `LSDExtensionLaunchConfigurationStore`, `LSDPluginManager`, `LSDServerExtensionLaunchConfigurationRegistrar`, `LSDatabaseBlockingFetchClient`, `LSDatabaseBlockingFetchServer`, `LSDatabaseBuilder`, `LSDatabaseContext`, `LSDatabaseRebuildContext`, `LSDefaultApplicationQueryBackend`, `LSDefaultApplicationQueryDatabaseDefaultAppEvaluator`, `LSDefaultApplicationQueryEntry`, `LSDefaultApplicationQueryResult`, `LSDefaultApplicationQueryServerDatastore`, `LSDefaultApplicationQueryUnrestrictedBehavior`, `LSDocumentProxy`, `LSEligibilityCacheEligibilityResolver`, `LSEligibilityPredicate`, `LSEligibilityPredicateEvaluator`, `LSEnumerator`, `LSExtensionLaunchConfiguration`, `LSExtensionLaunchConfigurationAppRecordWrapper`, `LSExtensionLaunchConfigurationClientSystemRegistrar`, `LSExtensionLaunchConfigurationExtensionRecordWrapper`, `LSExtensionLaunchConfigurationResolutionLSDBProvoder`, `LSExtensionLaunchConfigurationResolver`, `LSExtensionPoint`, `LSExtensionPointRecord`, `LSFeatureFlagPredicate`, `LSFeatureFlagPredicateEvaluator`, `LSHRNSupport`, `LSIconAlertManager`, `LSIconChangeAlertToken`, `LSInstallInfo`, `LSInstallInfoOverrides`, `LSInstallProgressList`, `LSInstallProgressObserver`, `LSMIResultRegistrant`, `LSMIResultRegistrantServerDatabaseContextProviding`, `LSMIResultRegistrantTrueDatabaseContext`, `LSMIResultUnregistrant`, `LSMacApplicationIdentityBookmark`, `LSMarketplacesPreferences`, `LSObserver`, `LSOpenStagingDirectoryManager`, `LSOperationRequestContext`, `LSPlugInKitProxy`, `LSPlugInQuery`, `LSPlugInQueryAll`, `LSPlugInQueryAllUnits`, `LSPlugInQueryAllUnitsResult`, `LSPlugInQueryWithIdentifier`, `LSPlugInQueryWithQueryDictionary`, `LSPlugInQueryWithURL`, `LSPlugInQueryWithUnits`, `LSPrecondition`, `LSPreflightedCleanReferencesToPersonaOperation`, `LSProgressNotificationTimer`, `LSPropertyList`, `LSRatingRankEligibilityMonitor`, `LSRebuildStatisticsGatherer`, `LSRecord`, `LSRecordBuilder`, `LSRecordPromise`, `LSRegistrantServerStrategy`, `LSRegistrationInfo`, `LSResourceProxy`, `LSRestrictionsTargetResolver`, `LSServerOpenStagingIOPersonality`, `LSSettingsStore`, `LSSettingsStoreConfiguration`, `LSSliceInfo`, `LSSpotlightAction`, `LSStandalonePluginRecordUpdater`, `LSStashedAppMetadata`, `LSSystemBundleIdentity`, `LSSystemExtensionPointRefreshRegistrant`, `LSTransmissibleExtensionLaunchConfiguration`, `LSUseValuesMCStateProvider`, `LSVPNPluginProxy`, `LSWorkPipe`, `LSiTunesMetadata`, `NSArray`, `NSCoder`, `NSDictionary`, `NSFileManager`, `NSKeyedUnarchiver`, `NSNull`, `NSObject`, `NSProgress`, `NSString`, `NSURL`, `NSUUID`, `UTTypeRecord`, `_LSAggregatePropertyList`, `_LSAppLinkOpenState`, `_LSAppLinkPlugIn`, `_LSAppToUnregister`, `_LSApplicationExtensionRecordEnumerator`, `_LSApplicationIsInstalledQuery`, `_LSApplicationProxiesOfTypeQuery`, `_LSApplicationProxiesWithFlagsQuery`, `_LSApplicationProxyEnumerator`, `_LSApplicationProxyForIdentifierQuery`, `_LSApplicationRecordEnumerator`, `_LSApplicationRecordSpecificUnitsEnumerator`, `_LSApplicationRecordsWithinDirectoryEnumerator`, `_LSApplicationSensitiveDataProxy`, `_LSApplicationState`, `_LSAvailableApplicationsForURLQuery`, `_LSBindingForLog`, `_LSBoundIconInfo`, `_LSBundleIDValidationToken`, `_LSBundleIdentifierAndType`, `_LSBundleProvider`, `_LSBundleProxiesOfTypeQuery`, `_LSBundleQuery`, `_LSCanOpenURLManager`, `_LSChangeObserver`, `_LSClaimBindingDocumentProxyBindable`, `_LSClaimBindingTypeIdentifierBindable`, `_LSClaimBindingURLBindable`, `_LSClientSettingsStore`, `_LSCompatibilityNothingBindable`, `_LSCoreTypesRecordProxy`, `_LSCurrentBundleProxyQuery`, `_LSDAppProtectionAccessManager`, `_LSDAppProtectionClient`, `_LSDAppProtectionService`, `_LSDBEnumerator`, `_LSDClient`, `_LSDDeviceIdentifierClient`, `_LSDDeviceIdentifierService`, `_LSDIconClient`, `_LSDIconService`, `_LSDModificationPendingSaveToken`, `_LSDModifyClient`, `_LSDModifyService`, `_LSDOpenClient`, `_LSDOpenService`, `_LSDReadClient`, `_LSDReadService`, `_LSDRebuildClient`, `_LSDRebuildService`, `_LSDService`, `_LSDServiceDomain`, `_LSDataBackedPropertyList`, `_LSDatabase`, `_LSDefaultFeatureFlagResolver`, `_LSDefaults`, `_LSDeviceIdentifierCache`, `_LSDeviceIdentifierManager`, `_LSDictionaryBackedPropertyList`, `_LSDiskUsage`, `_LSDispatchWithTimeoutResult`, `_LSDisplayNameConstructor`, `_LSDocumentProxyBindingQuery`, `_LSEligibilityListenerNotificationToken`, `_LSEmptyContainerMap`, `_LSEmptyEnumerator`, `_LSEmptyGroupContainerMap`, `_LSEmptyPropertyList`, `_LSEnumeratedBundleInfo`, `_LSErrorEnumerator`, `_LSExtensionPointEnumerator`, `_LSExtensionPointRecordEnumerator`, `_LSInProcessSettingsStore`, `_LSInstallNotificationJournaller`, `_LSInstallProgressService`, `_LSJournalledNotification`, `_LSLazyGroupContainerMap`, `_LSLazyPropertyList`, `_LSLinkedChildApplicationRecordEnumerator`, `_LSLocalQueryResolver`, `_LSLocalizedStringRecord`, `_LSMultiContainerMap`, `_LSMultiGroupContainerMap`, `_LSOpenConfiguration`, `_LSOpenCopierContext`, `_LSOpenResourceOperationDelegateWrapper`, `_LSPersonaDatabase`, `_LSPersonaWithAttributes`, `_LSPlistHint`, `_LSPlugInPropertyList`, `_LSPlugInProxyEnumerator`, `_LSQuery`, `_LSQueryContext`, `_LSQueryResult`, `_LSQueryResultWithPropertyList`, `_LSRecordEnumerator`, `_LSRegistrationNotificationJournaller`, `_LSRemotePlaceholderEnumerator`, `_LSServerSettingsStore`, `_LSSettingStoreChangeObserver`, `_LSSharedWebCredentialsAppLink`, `_LSSharedWebCredentialsAppLinkPlugIn`, `_LSSingleContainerMap`, `_LSSingleGroupContainerMap`, `_LSSpringBoardCall`, `_LSStackBacktrace`, `_LSStartupJournalledDatabaseRebuiltNotification`, `_LSStartupJournalledInstallNotification`, `_LSStringLocalizer`, `_LSStringsFileContent`, `_LSSynthesizedExtensionPointRecord`, `_LSTypeEnumerator`, `_LSURLOverride`, `_LSUnregisteredTypeTelemetry`, `_LSValidationToken`, `_LSXPCQueryResolver`, `_UTDeclaredTypeRecord`, `_UTDynamicTypeRecord`, `_UTUndeclaredTypeRecord`, `__LSRECORD_NULL_PLACEHOLDER__`

Protocols: `FSNodePropertyProviding`, `LSAppRemovalServiceProtocol`, `LSApplicationWorkspaceObserverProtocol`, `LSDExtensionLaunchConfigurationStoring`, `LSDPluginProtocol`, `LSDPluginServiceProtocol`, `LSDatabaseBlockingFetchProtocol`, `LSDefaultApplicationQueryDatastore`, `LSDefaultApplicationQueryDefaultAppEvaluator`, `LSDetachable`, `LSDomainEligibilityResolver`, `LSExtensionLaunchConfigurationRegistrar`, `LSExtensionLaunchConfigurationResolutionApplicationExtensionRepresenting`, `LSExtensionLaunchConfigurationResolutionApplicationRepresenting`, `LSExtensionLaunchConfigurationResolutionBooleanEntitlementBearing`, `LSExtensionLaunchConfigurationResolutionDatabaseProviding`, `LSFeatureFlagResolver`, `LSIconResourceLocator`, `LSInstallProgressProtocol`, `LSInternalWorkspaceObserverProtocol`, `LSMCStateProvider`, `LSOpenResourceOperationDelegate`, `LSOpenStagingDirectoryManagerIOPersonality`, `LSPersonaInfoProviding`, `LSRatingRankEligibilityMonitorDelegate`, `LSRegistrantDatabaseContext`, `LSRegistrantDatabaseContextProviding`, `LSRegistrantStrategy`, `LSRestrictionsTargetResolving`, `NSCoding`, `NSCopying`, `NSDiscardableContent`, `NSMutableCopying`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `ODRLaunchServicesProtocol`, `_LSDAppProtectionProtocol`, `_LSDDeviceIdentifierProtocol`, `_LSDIconServiceProtocol`, `_LSDModifyProtocol`, `_LSDOpenProtocol`, `_LSDReadProtocol`, `_LSDRebuildServiceProtocol`, `_LSPendingSaveToken`, `_LSQueryResolving`, `_LSServerSettingsStoreXPCProtocol`, `_LSStartupJournalledNotification`

## Strings (11,720)

First 2,500 of 11,720.
```
UTType
v24@?0^{__CFArray=}8^{__CFError=}16
iTunesArtwork
v32@?0@\"LSPlugInKitProxy\"8@\"NSError\"16^B24
has-externalAccessory-protocols
TableName
CFArrayRef _LSCopyUserActivityDomainNamesForBundleID(CFStringRef)
LSHandlers
must be remote placeholder
LSAppLinksEnabledByDefault
has-supports-game-mode
-[_LSDReadClient getKernelPackageExtensionsWithCompletionHandler:]
+[_LSDService(SubclassesShouldOverride) connectionType]
static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueForNodeInPrefsArray(NSArray *__strong, FSNode *__strong)
No path available.
   latestEventId = %lld\n
com.apple.LaunchServices.DefaultAppCategory.Marketplace
legacy claim
ioDictionary != nil
simulator (%llu)
com.apple.default-app.carrier-messaging
myDocuments.cannedSearch
-nil-
FreeProfileValidated
Restore Now
/System/Library/PrivateFrameworks/TCC.framework/TCC
Unable to access the specified record in the LS database for an unknown reason. Please file a bug report.
disable_url_overrides
-[LSApplicationWorkspace installContainerizedApplicationArtifactAtURL:withOptions:returningRecordPromise:error:progressBlock:]
NSError * _Nullable _LSServer_LSMigratePreferencesForDefaultApps(LSContext * _Nonnull)
public.named-pipe
com.apple.
HasCriticalAlerts
application-identifier
nil proxy provided to %s
const LocalizedString *LaunchServices::getKindStringFromState(State &, BOOL *, ExtendedBinding *)
SBRepresentedBundleIdentifier
-[_LSDModifyClient setAppReplacementSourceBundleIdentifier:forApplicationWithBundleIdentifier:operationUUID:reply:]_block_invoke
bluetooth product ID (?)
/private/var/mobile/Library/Preferences/com.apple.MobileCoreServices/com.apple.launchservices.secure.plist
mailto
no
_corrupt
-[_LSServerSettingsStore resetUserElectionsWithReply:]
.framework/
-[LSAppLink setEnabled:error:]
%@:...
isOnRootVolume
-[_LSQueryContext(Internal) _resolveQueries:XPCConnection:error:]
app in container
Failed to extract extension from name
exec-for-bundle
referenceDate
SDK too old to support SMB/USB documents (iOS 13.0 required.)
public.mp3
v32@?0@\"NSArray\"8@\"NSArray\"16@\"NSError\"24
<%@ %p> { url = %@, app = %@ }
/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
__PayloadOptions
INSchemaURLsForIntentNamesWithBundle
com.apple.lsd.system.diagnostics
/AppleInternal/Library
Updating PlaceholderMetadata for %@ with failure %@ <LSInstallType %@, underlyingError (%@), source %@>
-[LSDExtensionLaunchConfigurationStore _currentBootUUID]
couldn't find bundle to check persona association
\"%@\" = ?
_LSOpenOperationPerformContinueAfterAsyncGather
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSSpringBoardCall.mm
public.3d-content
com.apple.launchservices.databaserebuilt
registering app bundle
com.apple.DataMigrator
-[LSServerOpenStagingIOPersonality stagingDirectoryInfoForPersonaUniqueString:error:]
%@-->%@
_LSSchemaConfigureBindingMap
getFailableNumericFromBaseProperties
com.apple.developer.embedded-web-browser-engine
Attempting to set an observer's queue while it is already observing.
public.utf16-external-plain-text
public.font
v24@?0@\"<_LSPendingSaveToken>\"8@\"NSError\"16
binding result filter
-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]
has-multiple-containers
<LSBundleURLRelationshipPrecondition: %@ relationship to %@>
public.app-category.casino-games
com.apple.metadata-importer
v16@?0r^v8
NoneType
NSBuiltWithThreadSanitizer
+[LSRatingRankEligibilityMonitor sharedServerInstance]
label != NULL
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Base/LSDispatchUtils.mm
UTTypeRecord.mm
app-protection-locked
com.apple.lsd.dissemination
/private/preboot/Cryptexes/App/System/Library/CoreServices
LS SpringBoard sync call deadlock prevention queue
fmfmail.icloud.com
com.apple.launchservices.applicationsDidChangePersonas
app ID
NSSupportsPurgeableLocalStorage
com.sun.java-archive
shared
com.apple.private.ids.messaging
SBStarkCapable
<LSPrecondition: empty>
+[_LSURLOverride(Functions) iCloudSchoolworkURL:]
%@ %@ %@ <%@>
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator+LSData.m
No path in container
v32@?0@8Q16^B24
FSEventStreamFlushAsync
v12@?0B8
v12@?0I8
Can't ask to evaluate domain %llu
com.apple.private.handoff.pong
LSHandlerRoleShell
dev %d (%s) : purging events up to event id %lld
/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
com.apple.default-app.side-button
infoPlist
com.apple.MobileCoreServices
_LSDServiceGetXPCProxyForServiceClass
encDsId
registered app extension
+[NSKeyedUnarchiver(LaunchServicesAdditions) ls_unarchivedObjectOfClass:fromData:error:]
CSIdentityQuery
com.apple.AuthenticationServices.canHandleASWebAuthenticationSessionRequest
stashed app info
-[_LSDAppProtectionClient setLockedApplications:completion:]
volumeURL.fileURL
PackageType
Either bundleID or resourceURL must be specified to present an app restoration prompt.
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSMobileDataTransitSupport.mm
%02x
/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
Removed
type
CFBundleSignature
com.apple.telephonyutilities.callservicesd
CFBundleTypeMIMETypes
runLoop != NULL
FSEventStream was released (causing it to be deallocated) without calling FSEventStreamInvalidate()
_LSServer_PerformExternalRebuildRegistration
eligibility-checked-browser-engine-embedder
_EXAppExtensionPointEnumerator
refreshAfter
public.camera-raw-image
INSTALL
-[LSApplicationRecord(Diagnostic) getApplicationExtensionDiagnosticDescriptionWithError:]_block_invoke_2
sourceIdentity and destinationIdentity must have different bundle identifiers
unknown entitlement
Mount point was root/nil
canonical != nil
migrateDefaultAppsToNewWorld_block_invoke
+[FSNode(BookmarkData) pathForBookmarkData:error:]
iconFiles
BindingClassName
unitID
originalIdentifier
kMISMinSupportedSignatureVersion
LSAlwaysEligible
LSGetCSUIAUpcallManager_block_invoke
com.apple.launchservices.securepreferences.plist
/Network/Library
Failed to register %@
LSApplicationWorkspaceErrorDomain
subgenres
com.apple.os-eligibility-domain.change
com.apple.appstored.xpc.updates
num_paths == event_timesCnt
   pathsToWatch = %p\n
+[FSNode(BookmarkData) nameForBookmarkData:error:]
LSExtensionRestrictedSystemModes
lproj
Boot nonce must be initialized
LSLazyPropertyList.mm
com.apple.security.exception.files.home-relative-path.read-only
CompatibilityState
persistent identifier of length %zu is too short to extract database UUID!
com.apple.springboard.setWantsLockButtonEvents
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSPluginBundle.mm
NSExtensionSandboxProfile
baseData
LSServerInterface.mm
_SWCErrorDomain
com.apple.LaunchServices.systemAppRemoval.%@
WiFiAware
Plugin unit %llx does not have multiple containers
UMUserPersona
Failed to create empty CFArray.
LSUnregisteredTypeReportingInterval
public.assembly-source
v8@?0
UISOpenApplicationOptionPasteSharingToken
com.apple.lsdidentifiers.plist
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Base/LSPrefsSupport.mm
public.shell-script
imported
App not a candidate for this category, so will never be the default
extension point ID
com.apple.launchservices.preferredLocalizations
LSServerDBExecutionContext.mm
remote
BundleIDBinding
QuickLook
Invalid AppleID account identifier prefix
Fallback for nil error in enumerator error handler
(no bundle)
(restricted %d)
__ActivateSuspended
is-playgrounds-app
failed to import user elcection '%ld' for extension record: %@
aps-connection-initiate
Spotlight
public.x509-certificate
]
INIntentsSupported
v28@?0B8@\"<_LSPendingSaveToken>\"12@\"NSError\"20
BA
bindingMap
com.apple.lsd.system.openurl
Upgrade
LSDefaultAppCategoryContactlessPayment
com.apple.familycircle.agent
claim has correct handler rank
gameCenterEnabled
dispose_f2d_private_port
NSPrivacyTrackingDomains
Failed to create container query
UTExportedTypeDeclarations
For plist key %@, value has class %s (should be CFString).
_LSURLSchemeType _LSGetSchemeType(LSContext *, NSString *__strong)
icons
MCFeatureNewsAllowed
_LSCreateStandardRemovedAppPrompt
enumeration
LSDefaultAppCategoryDialing
signerOrg
pluginHasOverride
allocate_d2f_port
BOOL _LSDatabaseSetSeededSystemBuildVersion(_LSDatabase *__unsafe_unretained, NSString *__strong, NSError *__autoreleasing *)
-[_LSSpringBoardCall(Private) callSpringBoardWithCompletionHandler:]
EligibilityPredicate {
web-browser
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSCore.mm
-[_LSDiskUsage(Internal) _fetchWithXPCConnection:error:]
public.png
FSEventStreamGetDeviceBeingWatched
Item ID 0 never exists.
sdkPlist
_NSURLIsHiddenBySystemChangedNotificationsKey
LaunchAgents
i386
LSSessionKey _LSServer_SelfSessionKey()
HFSTypesSet
Predicate key not a feature flag
binding
DTPlatformVersion
NSPrincipalClass
isRestricted
+[_LSDeviceIdentifierManager sharedInstance]
com.apple.security.exception.shared-preference.read-only
No strong binding found
db != nil
com.apple.lsd.appcontrols
Could not copy destination URL
dateStashed
LSVendors
v32@?0@\"NSString\"8@\"_LSDisplayNameConstructor\"16^B24
multiple-descriptions
streamRef->cfRunLoopSourceRef != NULL
com.apple.lsd.iconNames
requires-iphone-os
void _LSEnumerateClaimedSchemes(LSContext * _Nonnull, const LSClaimData * _Nonnull, void (^__strong _Nonnull)(NSString *__strong))
LSDModifyService.mm
_LSRecord_resolve_
badge
com.apple.private.xpc.launchd.per-user-lookup
public.objective-c-source
com.netscape.javascript-source
invalid-redeclaration
SBAppTags
kTCCServiceMediaLibrary
has-custom-notification
com.apple.LaunchServices.DefaultAppCategory.CarrierMessaging
execSDK ver
public.executable
INVALID
Not examining strong bindings on public.folder item
CP
Entitlements
-[_LSCanOpenURLManager canOpenURL:publicSchemes:privateSchemes:XPCConnection:error:]
+[_LSDService(SubclassesShouldOverride) XPCInterface]
com.apple.private.corespotlight.internal
/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache/Library/Caches/com.apple.IconsCache/
uuid
strings
SF
connection != nil
com.apple.managedconfiguration.profiled.configurationprofiles
LSApplicationProxiesList
CFBundleDisplayName
-[LSRecord beginContentAccess] counter saturated.
appRecord != nil
Disk usage population queue
Failed to get LSDService subclass list for process %lu
_LSDAppProtectionService
eligibleForDomainFailingClosed
arm64.x1
File system object has an unknown POSIX type.
inKey != nil
/AppleInternal
fullAppInstalled
Failed to create mutable copy of dictionary, cannot safely proceed, aborting
subtype
public.zip-archive
won't
v24@?0@\"LSDBExecutionContext\"8@\"NSError\"16
LSBlockUntilComplete
Seeding is in progress.
start_wqthread
armv7em
com.apple.private.tcc.allow.overridable
** invalid plugin! %@**
Open
IsMarketplace
built-with-tsan
inBuildVersion != nil
LSInstallProgressList: %@, %@
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSServerDBExecutionContext.mm
shows-sec-prompts
_LSUsesSystemPersona
static const LocalizedString *LaunchServices::LocalizedString::Get(_LSDatabase *__strong _Nonnull, _LSLocalizedStringID)
static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Source
messages
com.apple.nspboard-type
Dest: %@
-[_LSBundleProxiesOfTypeQuery _enumerateWithXPCConnection:block:]
bundleData != NULL
Library/Application Support/Containers/%@/Documents/Inbox/
-[LSRecordPromise fulfillReturningError:]
isForcedUpdate
sandbox_extension
-[_LSDReadClient getBoundIconInfoForDocumentProxy:completionHandler:]
com.apple.itunesstored.private
-[LSRecordPromise initWithCoder:]
localizedName
getDictionaryFromAttributeOfNode
UserActivityIsForPairedDevice
com.apple.mobile.MobileDataTrasit
version-too-low
delegate
apple-internal
com.apple.device-model-code
com.apple.LaunchServices.UnregisteredTypeRequests
Must call FSEventStreamScheduleWithRunLoop() before calling FSEventStreamStart()
isPlaceholder
v16@?0@\"NSArray\"8
CoreServices
yield != nil
queries != nil
dbUUID
com.apple.springboard
Creating binding evaluator for application identifier %@
exe
LSPlugInQuery.m
schoolwork
-[_LSSharedWebCredentialsAppLink removeSettingsReturningError:]
_LSDOpenService
com.apple.private.coreservices.can-force-database-save-for-testing
@\"NSSet\"16@?0^{LSContext=@}8
storeFront
uses-system-persona
supports-CarPlay-instrument-cluster-scene
_LSDatabaseCreateByRemappingDatabase
No installed application with bundle identifier %@
defaultForCategory
URL
#
_LSGetBSActionForUserActivity
?CODEREQUIREMENT
serialized placeholder
com.apple.Siri
Script Libraries
-[LSByURLPluginUnregistrant runWithCompletion:]_block_invoke
fmf1
com.apple.FSEvents
kern.bootsessionuuid
Status
LaunchServices::TypeEvaluator::TypeEvaluator(const __strong id<FSNodePropertyProviding> _Nonnull)
%d
(blocked)
CertificateAssumedOK
-[LSApplicationWorkspace commonClientOpenURL:options:configuration:synchronous:completionHandler:]
FBSDisplayLayoutMonitor
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSEligibilityPredicateEvaluator.mm
/System/Library/Frameworks/CoreServices.framework
_ISPrimaryIconDataForApplicationProxy
iCloud Drive fault file looks like it has UTI %@.
icns
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationState.mm
BB
.mapdb
com.apple.coreservices
Driver Extensions
v24@?0q8@\"NSError\"16
plists
LSIsAppleDefaultForType
v28@?0I8r^{UTTypeDisplayNameFlavor=^?^{__CFString}*}12*20
Counterparts
value for key='%@' not requested to be cached
IsUpdatedSystemApp
no execution context in server?
com.apple.LaunchServices.DefaultAppCategory.MailClient
genreIdentifier
LSDefaultAppCategoryWebBrowser
Parent app is in an unsupported location
Bad input initializing with identity string: %@
ratingRank
void _LSCommonOpenApplicationWithBundleIdentifier(LSApplicationWorkspace *__strong, NSString *__strong, _LSOpenConfiguration *__strong, BOOL, void (^__strong)(BOOL, NSError *__strong))
com.apple.private.canIgnoreAppLinkOpenStrategy
Creating binding evaluator for FSNode %@
Alias
inDB != NULL
public.bzip2-archive
inBlock != nil
b
targetApplicationProxy
BRCopyDisplayNameForContainerAtURL
CoreTypes
HandlerPref
/var/db/PlugInKit-Annotations
bindable
FSEventsGetCurrentEventId
Could not create MDT session
has-watch-glance
SBRequiredCapabilities
ChangeLog
v24@?0@\"LSPlugInKitProxy\"8@\"NSError\"16
com.apple.default-app.mail-client
I
Could not decode the set of resolved property values for this record.
_timestamp
_LSBundleIsInGenerationalStorage
unexpected NULL bundle data
Store Object
ActivityTypeBinding
updateAvailabilities != nil
relaxed-default-apps-claim
-[_LSDModifyClient synchronizeWithMobileInstallation]
com.apple.private.librarian.container-proxy
content type
UserActivityIsNotification
invalid input parameters
requires-iphone-simulator
NSComparisonResult _LSBundleCompareForActivityContinuationSuitability(__strong LSDatabaseRef, const LSBundleData *, const LSBundleData *)
v32@?0@\"_LSPersonaWithAttributes\"8Q16^B24
-[_LSDModifyClient unregisterApplicationAtURL:operationUUID:reply:]
-[_LSDReadClient getBundleRecordForCurrentProcessWithCompletionHandler:]
com.apple.private.persona.write
-[NSCoder(LaunchServicesAdditions) ls_decodeArrayWithValuesOfClass:forKey:]
v16@?0@\"NSObject<OS_xpc_object>\"8
GCSupportsGameMode
-[_LSDIconClient setAlternateIconNameForCurrentApplication:completionHandler:]_block_invoke
void _LSOpenOperationPerformContinueAfterAsyncGather(NSURL *__strong, NSFileHandle *__strong, NSString *__strong, BOOL, NSString *__strong, NSDictionary<NSString *,id> *__strong, NSDictionary<NSString *,id> *__strong, __strong id<LSOpenReso
-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke
/System/Library/CoreServices/com.apple.cloudkit.launchservices.hostnames.plist
it
The requested account does not exist
-[LSApplicationWorkspace ls_testWithCleanDatabaseWithError:]
has-quarantine-path-exclusion
LS_NO_SERVER
com.apple.private.healthkit.authorization_bypass
BOOL _LSAliasDataMatchesPath_NoIO(NSData *__strong, NSString *__strong, LSPathMatchType)
public.rtf
v24@?0^{__CFDictionary=}8^{__CFError=}16
can't re-emplace a DelayedInitable
requires-secure-launch
openState
TCC Policy
com.apple.default-app.dialer
-[LSServerOpenStagingIOPersonality stagingDirectoryKeyForNode:error:]
kLSHiddenAppsEligibilityChangedNotification
writing preliminary journal but more than 0 journalled notifications?
iTunesMetadata.plist
*** Container V%08lu has invalid alias reference A%08lu
com.apple.private.assets.accessible-asset-types
childPath
NSExtensionPointName
com.apple.springboard.launchapplications
com.apple.LSStrongBindingDictionaryKey
-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installInfo:completionHandler:]
calling %s but already had a per thread context!
-[LSBundleRecordUpdater parsePersonas:error:]
EXEnumerator
LSCheckDatabaseAvailableWithServer_block_invoke
UpdateSinfForLaunchServices/UpdateiTunesMetadataForLaunchServices/UpdatePlaceholderMetadata
_kLSURLApplicationBinaryCompatibilityLocalizedWarningKey
<CSIdentityQuery %p [%p]>
NSExtension
wildcard
com.apple.ondemandd.launchservices
\" = ?
com.apple.private.accounts.allaccounts
UIApplicationSupportsMultipleScenes
-[LSApplicationWorkspace scanForAppsWithIdentifiersInSet:]_block_invoke
supports-aod
disk image
.openurl
LSRecord+Enumeration.mm
DELETE FROM unregisteredTypeRequests;
_LSGetMainBundleURL_block_invoke
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSDatabase.mm
v24@?0@\"NSNumber\"8@\"NSError\"16
com.apple.LaunchServices.URLTypesChanged
com.apple.audioUnit.temp
BundleNameBinding
com.apple.pkd
_LSStageOrConfirmInPlaceOpenabilityOfFileResource
externally-playable-content
com.apple.LaunchServices
default only
prepareIsHiddenBySystemValue
FileProviderString
runEvaluator
managed-app-distributor
NSIdentityUsageDescription
-[_LSDModifyClient removeReferencesToPersonaWithUniqueString:operationUUID:reply:]
purchasedRedownload
streamRef->refCount == 0
v32@?0@\"_LSQueryResult\"8@\"NSError\"16^B24
~/Library
void _LSTryUniversalLink(NSURL *__strong, NSString *__strong, NSDictionary<NSString *,id> *__strong, NSXPCConnection *__strong, void (^__strong)(BOOL))_block_invoke
-[LSClaimBindingConfiguration initWithCoder:]
_UTHardwareColorMakeWithRGBComponents
INDEX.BDM
@\"NSObject<OS_xpc_object>\"16@?0r*8
com.apple.passes.add-silently
Plugin invalid plugin platform %d on platform %d
%@ pluginID=%@ UUID=%@ version=%@
CREATE TABLE IF NOT EXISTS unregisteredTypeRequests (bundleID TEXT NOT NULL, typeID TEXT NOT NULL, firstAccessDate REAL NOT NULL, PRIMARY KEY (bundleID, typeID));
Alternate
_LSEnumeratorFireErrorHandler
expectedFinalInstallPhase
com.apple.LaunchServices.DefaultAppCategory.Dialer
v12@?0i8
PasswordInvalid
Hidden
disk-image
TemporaryDowngrade
com.apple.QuartzCore.secure-mode
minimumNumericHandlerRank
query != nil
reality
com.apple.mobileprovision
com.apple.lsd
Default
system_session_lsd
com.apple.lsd.system.open
T
com.apple.Numbers
com.apple.idms.appleid.
Must call FSEventStreamScheduleWithRunLoop() before calling FSEventStreamUnscheduleFromRunLoop()
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationIsInstalledQuery.mm
LSBundleProxy.m
ba_is_process_extension
GeoJSON
/Applications/
FBSOpenApplicationOptions
node != nil
@\"NSString\"16@?0@\"_LSPersonaWithAttributes\"8
Updated Placeholder install type with error %@
Cancel
CF
LSBundleInfoCachedValues.m
container iteration failed but no error from containermanager
com.apple.default-app.navigation
_SWCServiceSpecifier
reference URL
MAPS_REMOVED_VAGUE_RESTORE_MESSAGE
v24@?0@\"NSString\"8r^{?=IIIsSIII[8I]III}16
Could not get query resolver
com.apple.lsd.restrictionsmanager.signerIdentitySyncQueue
Adding user preferences
Invalid length
com.apple.private.coreservices.canforcedatabasegc
onlyCryptexContent
privacy
Invoked -stopObserving on this observer without first invoking -startObserving.
no path in data container URL
has-custom-bindings
LSContainerErrorNumber
bundleID != nil
addClaimRecordIfMissing
all roles
!
+[LSDExtensionLaunchConfigurationStore sharedServerInstance]
symbolImageName
has-display-name
BOOL _LSContextInitWithPath(LSContext *, const char *, NSError *__autoreleasing *)
unremappable
Found unit %llx for job label %@ but found no bundle data for it
+[LSBundleRecord bundleRecordWithBundleIdentifier:allowPlaceholder:error:]
_LSBundlePlugins
CertificatePending
 (placeholder only if parallel)
v24@?0r^S8Q16
-[_LSDOpenClient getiCloudHostNamesWithCompletionHandler:]
claimed UTIs
spotlight-actions
_LSDModifyService
com.apple.springboard.activateassistant
maximumNumericHandlerRank
Contacts
SCHEME_APPROVAL_DO_NOT_OPEN_BUTTON
com.apple.pkpass
identityBookmark
+[LSApplicationRecord setUpdateAvailabilityForApplicationsWithBundleIdentifiers:completionHandler:]_block_invoke
bundleID
-[LSApplicationWorkspace(DefaultApps) setDefaultHandlerForTypeRecord:toApplicationRecord:completionHandler:]_block_invoke
_LSBundleLibraryPath
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimRecord.mm
B16@?0^{container_object_s=}8
FBSOpenApplicationService
com.apple.private.coreservices.appmigration.write
com.apple.authkit.client.private
map
rating rank exception bundleIDs
v32@?0@\"NSString\"8Q16^B24
CK
UI
personaType
i
extension
extensionPointIdentifier != nil
FBSOpenApplicationOptionKeyDocumentOpen4LS
/System/Volumes/Data/
v32@?0I8r^v12I20*24
com.apple.launchservices.clearadvertisingid
IsWebNotificationBundle
process may not modify the requirements for default applications
VPNPlugin
AudioComponents
+[_LSDAppProtectionClient hiddenApplicationsForLSDUseOnly]
com.apple.launchservices.prefs-%p
/System/Library/Frameworks/Intents.framework/Intents
public.email-message
LSTargetBSServiceConnectionEndpointKey
_LSFile
public.app-category.medical
UTImportedTypeDeclarations
void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServic
@16@?0@\"_LSPersonaWithAttributes\"8
@\"NSNumber\"8@?0
LS:IncludeRestricted
SFAppleIDClientCopyMyAppleID
The caller does not have permission to complete the operation.
getFileHandleForOpeningResourceIfNecessary
(parallel)
is-Placeholder
Shell
ApplicationSINF
uuidOrNil != nil || activityDataOrNil != nil
will
install build version
WatchKitVersion
CFBundleDocumentTypes
-[LSPlugInQueryWithIdentifier _enumerateWithXPCConnection:block:]
public.tiff
-[LSApplicationWorkspaceRemoteObserver applicationsDidUpdateMetadata:]_block_invoke
LSUserActivityInvalidateAfterFetch
exported
APP_REMOVAL_PROMPT_DETAIL_APP_STORE_DELETED
com.apple.txn.text-multimedia-data
-[_LSDReadClient getBundleProxyForCurrentProcessWithCompletionHandler:]
Don't add weak binding (ineligible)
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Record/LSClaimBindingConfiguration.mm
public.app-category.productivity
userActivity != nil
/usr/lib/libBASupport.dylib
public.app-category.trivia-games
_LSFindBundleWithInfo_NoIOFiltered
_LSNodeIsOnCryptex
rel-icon-path
_LSInstallProgressService.m
Q
invalid URL or scheme
LSDisplayNameConstructor.mm
execContentModDate
public.app-category.reference
com.compuserve.gif
appleid.apple.com
Invalid parameter not satisfying: %@
 (placeholder)
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSBindingEvaluator.mm
SB
missing-required-SINF
v64@?0@\"NSString\"8{_NSRange=QQ}16@\"NSAttributedString\"32{_NSRange=QQ}40^B56
NSURL *_LSDefaultsUserContainerURL(void)
-[_LSDModifyClient resetServerStoreWithCompletionHandler:]_block_invoke
fileID
/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
NSUserActivityTypeBrowsingWeb
-[_LSDModifyClient updateRecordForApp:withSINF:iTunesMetadata:placeholderMetadata:sendNotification:operationUUID:returnSaveToken:completionHandler:]_block_invoke_2
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSDocumentProxy.mm
-[_LSDReadClient getDiskUsage:completionHandler:]
LS plugin notifications/icon cache queue
Category %llu is out of range
}
could not decode identity (missing bundleID?)
com.apple.LaunchServices.pluginsregistered
Document
_LSSliceInfosKey
-[_LSDReadClient mapBundleIdentifiers:orMachOUUIDs:completionHandler:]
Parent Bundle ID
Active
InfoPlist
_LSLocalizedStringsDictionary
Missing resource file handle
arm64_32
+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]
inDB
||
_operationType
bad_variant_access was thrown in -fno-exceptions mode
represented bundle
setStrongBindingValue
public.app-category.entertainment
public.utf8-plain-text
<null>
_LSServer_RefreshContentInFrameworkAtURL_block_invoke
cacheGUID
com.apple.private.coreservices.canmapbundleidtouuid
com.apple.resolvable
public.app-category.strategy-games
@
no AlternateName found for app
-[LSExtensionLaunchConfigurationClientSystemRegistrar fetchRegisteredConfigurationWithUUID:additionalConfigurationClass:error:]_block_invoke_2
_LSSchemeApprovalPromptWithCompletionHandler_block_invoke_2
CarrierBundle
%ld.exhausted
sem != NULL
%@#%@:%@
plugin is in an app
@\"LSBundleDataContainerMap\"8@?0
HOME
com.apple.mac
CSAppleIDAccountConfigurationAddedOrRemovedNotification
Customer
-[LSDocumentProxy initWithCoder:]
LSDefaultAppCategoryMessaging
<%@ %p> { table: %llx, unit: %llx, attached: %@ }
com.apple.mount-point
gnumakefile
UIVPNPlugin
com.apple.launchservices.applicationsDidUpdateMetadata
SIMULATOR_RUNTIME_BUILD_VERSION
-[FSMimicPopulator populateSimpleSelector:error:]
com.apple.private.launchservices.canspecifymanageddocumentsource
IsContainerized
-[LSRatingRankEligibilityMonitor _queue_domainNotificationFired:]_block_invoke
ExtensionBinding
-[_LSDReadClient getWhetherTypeIdentifier:conformsToTypeIdentifier:completionHandler:]
options
NSAppClipRequestEphemeralUserNotification
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSQuery/LSQueryContext.mm
LSURLPropertyProvider.mm
com.apple.launchservices.LSApplicationWorkspacePluginsChangedCallback
Skipping alternate UTI claims (no path extension)
_LSDirectoryClass
com.apple.LaunchServices.prefsFile
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.mm
continuous
NSAppClipRequestLocationConfirmation
MobileInstallationUpdatePlaceholderMetadata
Context
com.apple.lsd.mapdb
_LSServer_GetServerStoreForConnectionWithCompletionHandler
com.apple.AppleIDAuth
The identity authority cannot be accessed at this time.
not eligible
alias
LSDReadService.mm
arcade-app
com.apple.accounts.appleidauthentication.defaultaccess
com.apple.applescript.script
OSStatus _LSServer_RegisterItemInfo(const LSRegistrationInfo *__strong, NSData *__strong, CFDictionaryRef, LSInstallInfo *__strong, CSStoreUnitID *, CSStoreUnitID *, Boolean *, CFStringRef *)
com.apple.launchservices
handler rank
declared-by-extension
com.apple.usermanagerd.persona.fetch
internal
v16@?0@\"UTTypeRecord\"8
App validation failed (no bundle path), ignoring didInstall notification for %@
not placeholder
NSUIElement
private-scheme
all roles (bundle ver)
_LSSchemaConfigureForStore
BOOL _LSDatabaseContextStartAccessingWithDomain(_LSDServiceDomain *const __strong _Nonnull, LSDatabaseContextAccessOptions, NSError *__autoreleasing * _Nullable)
getMonitor_block_invoke_2
bogus app category %lu
NSString *LaunchServices::LocalizedString::localizeUnsafely(_LSDatabase *__strong _Nonnull, NSArray<NSString *> *__strong _Nullable) const
com.apple.private.healthkit.medicaliddata
appextensionpoints
-[LSApplicationWorkspace(DefaultApps) setPreferenceForNoHandlerForCategory:completionHandler:]_block_invoke
...done.
+[_LSDiskUsage(Internal) _serverQueue]
SDKData
classic-app
-[_LSDModifyClient removeAllHandlerPrefsForBundleID:completionHandler:]
UIActivityContinuationAction
com.apple.launchservices.extension-launch-configuration.registrar
linked parent bundleID
%@Paths:\n\tdatabaseStoreFileURL: %@\n\tqueriedSchemesMapFileURL: %@\n\tidentifiersFileURL: %@\n\tpreferencesFileURL: %@\n\tsecurePreferencesFileURL: %@\nEnvironment:\n\tisServer: %@\n\thasServer: %@\n\tinEducationMode: %@\n\thasPersistentP
LSExecutableCFMFormat
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryWithIdentifier.m
IN
NSSupportsLiveActivitiesFrequentUpdates
context != NULL
_SWCServiceTypeActivityContinuation
Developer
Bundle in binding map 
entitlements
LSExecutableSDKVersion
public.bluetooth-vendor-product-id
-[_LSDReadClient getSystemContentStoreWithCompletionHandler:]
CFMutableDictionaryRef copyDeepMutableDictionary(CFDictionaryRef)
com.apple.private.suggestions.events
protocol
sourceApp
 not
UTTypeIsWildcard
*.pass.com.apple.itunes.storecredit
-[FSNode(BookmarkData) initByResolvingBookmarkData:options:relativeToNode:bookmarkDataIsStale:error:]
ctx != NULL
MPSupportsExternallyPlayableContent
CacheSequenceNum
userInfo.expectedFinalInstallPhase
__UserActivity4LS
CanonicalString
-[_LSDAppProtectionClient getHiddenApplicationsWithCompletion:]
Called +startAccessingReturningError: a ludicrous number of times without calling +stopAccessing. This is likely a bug in the Launch Services client.
i8@?0
valuesByBundleID
com.apple.LaunchServices.applicationRegistered
_primaryBundleID
   numPathsToExclude = %lu\n
Base type of UTI %@ was com.apple.package; looking for alternate UTI claims
0x%llx
creator
rb
public.app-category.developer-tools
public.app-category.role-playing-games
-[LSApplicationWorkspace sendApplicationStateChangedNotificationsFor:stateProvider:completion:]
_LSContainerFindOrRegisterWithNode
-[_LSDOpenClient failedToOpenApplication:withURL:completionHandler:]
-[_LSDClient initWithXPCConnection:]
?UT-IS:
groupContainers
com.omnigroup.foreign-types.
_LSSchemeApprovalPromptWithCompletionHandler
com.apple.ostype
GCSupportedGameControllers
-[FSNode childNodeWithRelativePath:flags:error:]
bundle flags
-[_LSDModifyClient setHandler:version:roles:forContentType:completionHandler:]
sms
untrusted
B28@?0I8^I12r^^{LSBundleData}20
v24@?0@\"LSBundleProxy\"8^B16
com.apple.launchservices.rebuildWorkPipe
LoginItems
public.swift-source
Invalid AppleID account identifier lenth %d
ratingRankEligibilityDomain
ApplicationDSID
-[LSIconChangeAlertToken presentWithCompletion:]
Had claimless binding %@, but found a claim-based binding %@ to substitute
Configuration had additional configuration but no class was provided
*
LSBundleDataContainer.mm
DT
public.app-category.travel
-[LSApplicationRestrictionsManager _lazyLoadRestrictionsIdentifierSet:identifiersAreNullable:context:reason:getter:]_block_invoke
-[LSBundleSetContainersOperation executeWithContext:]
Invalid default app category
registration
placeholderFetchBehavior
The posix name is aleady assigned to another identity.
Application must be non-nil and installed.
is-ad-hoc-signed
yes
zip
com.apple.private.webinspector.allow-remote-inspection
UIViewControllerBasedStatusBarAppearance
public.source-code
LSObserver.mm
AllEmails
com.apple.launchservices.applicationsWillInstall
_LSWriteApplicationPlaceholderToURL_block_invoke
void _LSEnumerateClaimedTypes(LSContext * _Nonnull, const LSClaimData * _Nonnull, void (^__strong _Nonnull)(NSString *__strong))
/Developer/Applications/
com.apple.iwork.keynote-live
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Type/UTTypeEvaluator.mm
Failed to create localized name dictionary.
UIFileSharingEnabled
supports-collaboration
<%@: %p type %d resolvedDomainUID %d>
INSERT OR IGNORE INTO unregisteredTypeRequests (bundleID, typeID, firstAccessDate) SELECT ?1, ?2, ?3 WHERE (SELECT COUNT(*) FROM unregisteredTypeRequests WHERE bundleID = ?1) < ?4;
FSEventStreamRef @ %p:\n
B16@?0@\"ICLBundleRecord\"8
outRequiresBiDi != NULL
-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]_block_invoke
Requires GC
UTTypeGlyphName
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfigurationResolver.m
.rebuild
com.apple.private.launchservices.canChangeEntitlementRequirementsForDefaultApplications
com.apple.wifi.manager-access
com.apple.private.healthkit.authorization_manager
open_dprotected_np failed
p2-url-resolution
com.apple.lsd.seeding
Couldn't get C string from entitlement name '%@'
LS:ExtensionPlatforms
v24@?0@\"NSString\"8@\"NSError\"16
input application record was not a mail client
_LSBundleCopyOrCheckNode_block_invoke
~/Applications
never
-[LSBundleRecord(Containers) getGroupContainersForPersonaWithUniqueString:createIfNecessary:error:]
MinimumOSVersion
public.composite-content
mailclient
com.apple.lsd.system.modifydb
LSDOpenService.mm
void _LSDServiceStartAllServices()_block_invoke
com.apple.default-app.messaging
is-placeholder-plugin
updateAvailabilities
_LSBundleCopyOrCheckNode
string != nil
prepareCanSetStrongBindingValue
critical-alerts
@\"LSApplicationProxy\"16@?0@\"NSString\"8
-[_LSDModifyClient updateContainerUnit:completionHandler:]_block_invoke
LSEligibilityDeletionDomain
universal links
The file system path for this process could not be determined. It may not be running, or it may have been deleted or moved while running.
v40@?0@\"NSString\"8@\"NSDictionary\"16@\"NSSet\"24^B32
-[LSSystemExtensionPointRefreshRegistrant runWithCompletion:]_block_invoke
LSExecutable#!Format
<LSDatabase %p> { system session, path = '%@' }
_LSCanModifyDefaultHandler
genre
-[_LSDReadClient fetchRegisteredConfigurationWithUUID:completion:]
/Library
finderInfo
void LaunchServices::DelayedInitable<LaunchServices::Predicate>::emplace(Args &&...) [T = LaunchServices::Predicate, Args = <LaunchServices::Predicate>]
@?<v@?>16@?0@\"NSProgress\"8
newDefaultApps2024
Invalid input URL
None
uti-wildcard
LSDefaultAppCategoryCarrierMessaging
/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
open(2) failed when opening resource to open
-[FSMimic canonicalPathWithError:]
com.apple.bundle
Apple Account
num_paths == path_offsetsCnt
UTTypeEnumerateFlavoredDisplayNames
block != nil
Destroying binding evaluator %p
v16@?0^{LSContext=@}8
label
void _XCFRelease(CFAllocatorRef, const void *)
key != nil
-[_LSAvailableApplicationsForURLQuery _enumerateWithXPCConnection:block:]
com.apple.icloud.fmfd.access
-[LSAppLink(BrowserSettings) setBrowserSettings:error:]
bundleInfoDictionary
plist
-[FSNode getFSID:error:]
discover-from-hidden-apps
com.apple.security.exception.mach-lookup.global-name
LSAlias.mm
_LSGetPlaceholderRecordForRemovedAppPrompt
app-protection-hidden
Editor
FSUtils.mm
handles-file-url
mail-client
_LSCreateStoreWithFileContents
observer
v20@?0^{__CFDictionary=}8i16
PluginBundleIDBinding
com.apple.launchservices.clearvendorid
<%@@%p: referenceDate %@ didRefresh %d refreshAfter %@ defaultForCategory %d>
validation
public.text
public.jpeg-2000
ratingLabel
SkipWatchAppInstall
IsOnDemandInstallCapable
NSExtensionPointIdentifier
com.apple.mobilemail
Bad binding string
FamilyID
Returned XPC object %@ was not an array, cannot continue
invalid LSRegistrationInfo
LS SpringBoard call queue
family
/AppleInternal/
settings-navigation://com.apple.Settings.AppInstallation/#ADRestoreAppStore
Node %@ was an iCloud Drive fault file. Substituting binding evaluator.
q
LSRegistration.mm
AppleIDValidationRecordOptionDoNotCheckValidAsOfDate
Must call FSEventStreamStart() before calling FSEventStreamFlushAsync()
_LSServer_PerformOpenOperation_block_invoke
LSRequiresIPhoneOS
-[LSRatingRankEligibilityMonitor ensureMonitoringDomain:]
LSAbortIfMayNotMapDatabase
Parent app has a parallel placeholder
-[LSIconAlertManager iconChangeAlertTokenForIdentity:error:]
minVersion != nil
/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
CFBundleURLAlwaysAvailable
com.apple.binary-property-list
_LSDatabaseRemap_block_invoke
v28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1
_LSCreateVagueRemovedAppPrompt
com.apple.LaunchServices.syncInterrupted
static _LSCanonicalStringID LaunchServices::CanonicalString::Add(_LSDatabase *__strong _Nonnull, NSString *__strong _Nonnull, NSDictionary<NSString *,NSString *> *__strong _Nonnull)
\" = \"
-[LSAltIconManager _setAlternateIconName:forIdentifier:withIconsDictionary:error:]
https
plist flags
inContainerUnit != kCSStoreNullID
Sync
UTTypeConformsTo
should have an error on failure path!
<=
BOOL _FSNodeGetSimpleBoolValue(FSNode *const __strong, const __strong NSURLResourceKey, CFURLResourcePropertyFlags, CFURLVolumePropertyFlags)
v32@?0^{LSContext=@}8I16I20r^v24
MCRestrictionManager
INSERT OR REPLACE INTO Election (identifier, userElection) VALUES (?, ?)
Already invoked -startObserving on this observer.
fmip1
public.presentation
%llu bindings found
LSVendorIdentifier
UIApplicationShortcutItemsVersion
certCN
LSLastSeenImportantAppRestrictionStateKey
-[LSDExtensionLaunchConfigurationStore _writeBootInfo:nonce:]
.diagnostics
canonicalPath
com.apple.private.launchservices.canspecifysourceapplication
APSystemPlugInEffectiveContainer
status
DiagnosticsSupport
extension point flags
public.app-category.video
public.json
NSExtensionSDK
Skipping parent UTI claim for %@ due to options (wildcard UTIs not requested)
distributorInfo
betaVersionIdentifier
MIME type
_LSMimicKey
 - restricted
_LSServer_UpdateDatabaseWithInfo
LSEntitlements.mm
(LSInstallType)%llu
-[_LSServerSettingsStore setUserElection:forExtensionKey:reply:]
AnalyticsSendEvent
Sending uninstalledNotifications for %@
-[LSDExtensionLaunchConfigurationStore registerConfiguration:error:]
_LSBundleCreateNode
itemId
Claim
-[LSApplicationRecord(AlternateIcons) setAlternateIconNameSilently:completionHandler:]_block_invoke
InstallSessionID
v24@?0#8^B16
Parent app is a placeholder
bundle data for bundle %llx was nil; binding %zu of %zu; please file a bug and relate to rdar://126722263
0000000000
LSRequiresClassic
Bundle
com.apple.lsapplicationproxy.deviceidentifierforvendor
DTSDKBuild
com.apple.private.communicationsfilter
userID
/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
record
LSLaunchDAllowMultipleInstances
SetStrongBindingForNode
inPath != nil
includeLinksForCallingApplication
com.apple.launchservices.canopenurl
com.apple.private.extensionkit.builtinanypersona
BuildMachineOSBuild
com.apple.private.imcore.imremoteurlconnection
streamRef->f2d_private_port != MACH_PORT_NULL
Could not request port notification
v16@?0@?<v@?@@\"NSError\">8
Platform
public.avchd-collection
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/_LSInstallProgressService.m
FSEventStreamScheduleWithRunLoop
-[_LSDOpenClient performOpenOperationWithURL:fileHandle:bundleIdentifier:documentIdentifier:isContentManaged:sourceAuditToken:userInfo:options:delegate:completionHandler:]
static bool LaunchServices::PrefsStorage::_SetValueForNodeInPrefsArray(NSMutableArray *__strong, FSNode *__strong, __strong id, NSError *__autoreleasing *)
com.apple.protected-mpeg-4-video
kextName
bundleIdentifier != nil
v32@?0@\"NSString\"8@\"NSURL\"16^B24
-[LSSettingsStore setUserElection:forExtensionKey:error:]
SFAppleIDClientCopyIdentity
com.apple.security.application-groups
:nooverride
public.utf8-tab-separated-values-text
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/_LSPersonaDatabase.mm
Cancelled
LS_SIMULATE_LIMITED_MAPPING_FOR_XCTESTS
com.apple.LaunchServices.TypeDeclarationsChanged
com.apple.lsapplicationworkspace.restrictions
trash
@\"NSString\"24@?0@\"_CSVisualizer\"8I16I20
exactBundleVersion
server_gone_StreamRef_callback
/var/mobile/Applications/
com.apple.private.launchservices.canEncodeSensitiveData
ibooks
The specified application is restricted, so the system cannot prompt to reinstall it.
CFBundleURLIsPrivate
com.apple.private.coreservices.canmaplsdatabase
CAProcessCanAccessGPU
This platform does not support discovery of companion application identifiers.
SystemDataOnly-
public.movie
-[_LSDReadClient getExtensionPointRecordForCurrentProcessWithCompletionHandler:]
failed to set user election to '%d' for extension record: %@
seatbelt-profiles
-[NSCoder(LaunchServicesAdditions) ls_decodeSetWithValuesOfClass:forKey:]
com.apple.lsd.observers
CoreSpotlightActionSymbolImage
MKDirectionsApplicationSupportedModes
inBundleData
public.app-category.healthcare-fitness
cancellable
appLink != nil || openState != nil
LS app removal prompt queue
Skipping wildcard document claims because we are not binding to a UTI
secondaryGenreID
public.video
com.microsoft.waveform-audio
<FSNode %p> { isDir = %c, path = <private> }
-[LSDBExecutionContext _perThreadContextsLock_createPerThreadContextForThisThread]
v24@?0^{__CFString=}8^{__CFError=}16
com.apple.locationd.usage_oracle
v24@?0@\"<EXExtensionPoint>\"8^B16
/Device/
INIntentsRestrictedWhileLocked
default-apps-claim
Seeded Cryptex Version
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/SettingsStore/LSSettingsStore.mm
com.apple.LaunchServices.DatabaseSeedingComplete
public.spreadsheet
line
ioAddress != NULL
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Record/Enumerator/LSEnumerator.mm
_DebugMode
Failed to get back value \"%@\" we just inserted into an NSMutableSet.
AppleIDAuthenticationErrorDomain
com.apple.NetworkBrowser
+[LSAppLink(Internal) _openAppLink:state:completionHandler:]
The posix name value is not valid.
why don't we have a container in the map?
bundle version
-[LSBundleRecordBuilder buildBundleData:error:]
v36@?0I8r^{?=IIIIiII[8I]IIIIIIIII}12q20*28
com.apple.notificationcenter.widgetcontrollerhascontent
_kLSURLApplicationShouldBeHiddenBySystemPreferenceKey
Boolean LaunchServices::prepareLocalizedNameDictionaryValue(Context &, __unsafe_unretained id<FSNodePropertyProviding>, _CFURLFileCacheRef, CFStringRef, State *, NSError *__autoreleasing *)
binding count unexpectedly changed from %zu to %zu; please file a bug and relate to rdar://126722263
PurchaserID
CPSupportsInstrumentClusterNavigationScene
com.apple.pict
props != nil
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSAppPlaceholders.mm
restricted by Managed Configuration
Unknown error
index.bdmv
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSBundleBase.h
No concrete persona found for system persona app.
com.apple.springboard.shortcutitems.customimage
com.apple.quicktime-movie
Skipping rebuild
Unix Executable File
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSBundle.mm
LSBundleBase.h
appProtectionEffectiveContainer
com.apple.lsd.server.asyncwork
email
SFAppleIDClientCopyPersonInfo
-[LSEligibilityPredicate initWithDictionary:error:]
unknown notification type %d
openConfiguration
 `
LSSettingsStore.mm
v24@?0r*8^B16
openState.XPCConnection
systemSession
public.c-plus-plus-header
Bundle node not found on disk: %@
-[_LSDReadClient getPersonalPersonaUniqueString:]
com.apple.Pages
URL scheme
copyPreferencesACL
on-cryptex
LSBundleRecord.mm
link-enabled
CanInheritApplicationStateFromOtherProcesses
UILaunchStoryboardName
CFBundleSupportedPlatforms
A type must be specified.
void _LSServer_OpenUserActivity(NSUUID *__strong, NSData *__strong, NSString *__strong, BOOL, NSString *__strong, LSAppLink *__strong, _LSAppLinkOpenState *__strong, NSDictionary<NSString *,id> *__strong, NSXPCConnection *__strong, __strong
com.apple.quicklook-generator
LastName
resultStruct != nil
Couldn't find personal persona unique string?
arm64e
-[LSDatabaseBlockingFetchClient getServerStoreBlockingWithCompletionHandler:]
public.item
bookmark
appstore-ui://restoreAppStore
-[LSDExtensionLaunchConfigurationStore _initializeStorage]
Intents
com.apple.TextInput.rdt.me
LSContinuityErrorDomain
/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
usingNetwork
LSDatabaseContext cannot take a user ID while the database is already being accessed.
containers
identifier version %d is unknown
FSEventStreamGetLatestEventId
Contents/PkgInfo
LSUpdatePlaceholderIcon
<%@ %p> { %@ }
com.apple.private.handoff.ping
uid
v16@?0^v8
Cannot register parallel placeholders or standalone placeholders with this interface.
prepareDistinctLocalizedNameValue
FSEventStreamCopyPathsBeingWatched
container
com.apple.Keynote
/System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
couldn't load upcall bundle principal class
-[LSApplicationRecord setUpdateAvailability:completionHandler:]
LSRegisterURL
has-override
hw.optional.avx2_0
LSSessionKey(system: %d uid: %d)
-[_LSValidationToken initWithPayload:]
org.gnu.gnu-zip-archive
AppleIDEncodedDSIDCertificateType
bumping sequence number
-[_LSSpringBoardCall(Private) promptAndCallSpringBoardWithCompletionHandler:]
public.perl-script
com.apple.launchservices.applicationInstallsDidUpdateIcon
The persistent identifier passed to -[LSBundleRecord initWithPersistentIdentifier:] was for a different type of record.
{ bundleID: %@, URL: %@ }
validateBundlePersonaRemoval
-[LSiTunesMetadata storeCohortWithError:]
telemetry
%@ %@ %@ <%@:%@>
managementDeclarationID
UINewsstandApp
_LSServerRegisterItemInfo begin
/private/preboot/Cryptexes/OS/SystemVersion.plist
LSMarkLocalizationsStoredInDatabase
/System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
void _LSAssertRunningInServer(const char *)
synchronous (server)
URLSchemeBinding
-[LSMIResultRegistrantTrueDatabaseContext unregisterPluginBundleByUnit:error:]
com.microsoft.ico
placeholderMetadata
BOOL _LSGetItemInfoFlagsForNode(LSContext *, FSNode *__strong, LSItemInfoFlags *, NSError *__autoreleasing *)
-[_LSDModifyClient rebuildApplicationDatabasesForSystem:internal:user:completionHandler:]
BOOL _LSCheckIfXPCConnectionCanReadDocument(NSXPCConnection *__strong, LSApplicationProxy *__strong, NSURL *__strong, NSError *__autoreleasing *)
-[LSRecordPromise initWithRecord:error:]
com.apple.launchservices.clientprogress
void _LSServer_BeginProvidingVisualizationArchives()
com.apple.developer.media-device-extension
stageResourceByCloningHandle
teamID
loadIfNeeded
trusted
MobileInstallationCopyFrameworkInfoForLaunchServices
Unable to find this claim record in the Launch Services database.
Binding
Database is seeded.
LSDefaultAppCategorySideButton
editor
resolvedProperties
-iphoneos
streamRef != NULL
/private/var/mobile
Failed to remove
is-update-available
HFSTypesUnavailable
_LSDatabase *_LSDatabaseCreateSnapshotAgainstAccessContext(_LSDatabase *__strong, CSStoreAccessContextRef, NSError *__autoreleasing *)
com.apple.private.coreservices.can-set-system-build-version
Built bundle record for app
_notification
AppRemoval
com.apple.lsapplicationworkspace.rebuildappdatabases
+[LSApplicationRecord(Enumeration) enumeratorForViableDefaultAppsForCategory:options:]
Extended attribute name too long or invalid.
LSClaimedTypes.mm
mdimporter
com.apple.private.alloy.passbook.provisioning
public.vcard
prerendered
invisible
? (%llu)
LS_PREFERRED_LOCALIZATIONS
hw.cputype
bundleIdentifier was nil when creating application identity
<LSDatabase %p> { path = '%@' }
EssentialAssets
Has override
v32@?0@\"_LSQueryResult\"8Q16^B24
=>
inDB != nil
rejected placeholder
streamRef->appRunLoop != NULL || streamRef->event_source != NULL
/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
-[LSApplicationWorkspace(Migration) migrateApplicationPreferencesFromIdentity:toIdentity:error:]
contains-settings-bundle
void _LSDatabaseContextAccessContextUsingBlock(LSContext * _Nonnull, void (^const __strong _Nonnull)())
-[LSSettingsStore resetUserElectionsWithError:]
Automator
-[_LSApplicationIsInstalledQuery _enumerateWithXPCConnection:block:]
2ry category
Query not allowed
void _LSAssertNotRunningInServer(const char *)
v32@?0@\"NSString\"8@\"_LSPersonaWithAttributes\"16^B24
YES
-[_LSApplicationRecordsWithinDirectoryEnumerator _preflightPathOfBundleWithContext:bundleUnit:bundleData:]
isRemoved
0A `
-[_LSDReadClient mapPlugInBundleIdentifiersToContainingBundleIdentifiers:completionHandler:]
ContextMenuShowsOpenWithApp
_LSCopyDataContainerURLFromContainermanagerForPersona
com.apple.developer.side-button-access.allow
defaultIcon
prepareLocalizedNameDictionaryValue
_LSIsExecutableForParentBundle
makeStagingDirectoryURLInContainer_block_invoke
placeholder for missing error; file a bug
   numPathsToWatch = %lu\n
-[FSNode initWithURL:flags:error:]
%@ (v %@)
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm
LSUtils.mm
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Server/LSDOpenService.mm
MKBDeviceUnlockedSinceBoot
FSEventStream was released (causing it to be deallocated) without calling FSEventStreamStop()
codedAdditionalConfiguration
+[LSApplicationExtensionRecord applicationExtensionRecordsForUUIDs:outContainingBundleRecords:error:]
-[_LSApplicationRecordEnumerator(Private) _applicationRecordWithContext:bundleIdentifierOrUnit:]
kLSBundleClassAutomatorAction
supports-asset-catalog
+[LSBundleProxy bundleProxyForURL:error:]
com.apple.private.coreservices.appmarketplace.read
com.apple.launchservices.applicationsDidInstall
min version platform
has-min-sys-version-by-arch
com.apple.traditional-mac-plain-text
com.apple.icns
v20@?0C8^{__CFError=}12
interpretEligibilityAnswerForBrowserDomain
_LSRequiresGarbageCollection
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordUpdater.mm
-[_LSDModifyClient updateRecordForApp:withSINF:iTunesMetadata:placeholderMetadata:sendNotification:operationUUID:returnSaveToken:completionHandler:]_block_invoke
-[_LSDReadClient getTypeRecordsWithIdentifiers:completionHandler:]
no known persona with unique string %@
supports-live-activities-frequent-updates
Annotations
Denylisted type: %@
foundBundle
has-vpn-plugins
com.apple.launchservices.defaults
-[FSMimic sideFaultResourceValuesWithError:]
   runLoop = %p\n
-[FSNode sideFaultResourceValuesWithError:]
ioContext != NULL
_LSPluginFindWithPlatformInfo
extension point name
@ 5#1%4
setting nil database
com.apple.localizable-name-bundle
ever-game-center
MissingSINF
Disk usage property queue
com.cisco.jabber.filetransfer.
-[_LSCanOpenURLManager(PrivateSchemeChecking) writeSchemesMap]
PlaceholderEntitlements.plist
Domain
Failed to allocate empty NSData.
v24@?0^{?=[64S]^{__CFString}^S*{?=qq}qq}8Q16
-[_LSDReadClient getAllUserActivityTypesAndDomainNamesWithCompletionHandler:]
Signature mismatch: %s signature = '%@', plist CFBundleSignature = '%@'
com.apple.user-library
CAP
<%@ %p> { identifier: %@ }
service
Didn't find domain %llu in domain cache after refreshing successfully
v28@?0C8^{__CFDictionary=}12^{__CFError=}20
LSShouldORIdentifiers
<private>%@ (B:0x%llx, C:0x%llx)
IdentityUsage
(none available)
-[_LSDModifyClient setPreferredAppMarketplaces:completion:]
com.apple.LaunchServices.DefaultAppCategory.InactiveCategory
v16@?0q8
store
com.apple.private.network.socket-delegate
UserActivityTypeTeamIDOveride
FSEventStreamSetDispatchQueue
ADClientAddValueForScalarKey
_LSCopyOrMoveFileResource_block_invoke
Placeholder
LSAppPlaceholders.mm
%@ (0x%llx)
kLSBundleClassSystemLibrary
Could not create CFMachPort
v24@?0@\"NSUUID\"8@\"NSNumber\"16
end inspect %@
com.apple.security.system-groups
com.apple.background-asset-downloader-extension
+[_LSDiskUsage(Private) ODRUsageForBundleIdentifier:error:]
-[LSApplicationWorkspace registerBuiltinApplicationWithInstallationRecord:extensionInstallationRecords:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]
com.apple.lsd.appprotection
LSUIElement
public.filename-extension
BDMV
-[FSNode(FinderInfo) setFinderInfo:error:]
v24@?0@\"LSApplicationRecord\"8^B16
static
create_block_invoke
com.apple.private.accounts.customaccesssinfo
CFBundleTypeIconSystemGenerated
/Library/Developer/
-[_LSDModifyClient setSystemBuildVersion:completionHandler:]
unable to locate user container: error %s
need that database
glyphName
CSIdentityErrorDomain
DefaultAppCategorization
containerURL
Bundle unit %llx not found
-[_LSDModifyClient uninstallApplication:withOptions:uninstallType:reply:]
_LSPluginFindWithPlatformInfo_block_invoke_2
v16@?0@\"NSURL\"8
extensions
DTPlatformBuild
un-
AVCHD
NSAccentColorName
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Visualization/LSDatabaseVisualization.mm
ioCoalescingFlag != NULL
public.mpeg-2-video
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSStrongBinding.mm
public.playlist
   flags = 0x%08x\n
   runLoopMode = %p\n
CFBundleIconName
MCFeatureIdentifierForAdvertisingAllowed
appLink != nil
http
-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:bundlePersonaRecordMap:operationUUID:reply:]
v16@?0@\"LSExtensionPointRecord\"8
com.apple.purplebuddy
May not unregister bundle
@\"_LSLazyPropertyList\"8@?0
public.utf16-plain-text
-[LSDExtensionLaunchConfigurationStore fetchConfigurationWithUUID:error:]
LSRequiresPostProcessing
_LSDispatchWithTimeoutCompletionHandler _LSGetDispatchWithTimeoutCompletionHandler(_LSDispatchWithTimeoutResult *__strong, __strong id<NSLocking>, __strong dispatch_semaphore_t)
pausable
_LSAppStateFlags
+[_LSSharedWebCredentialsAppLink setSettingsSwitchState:forApplicationIdentifier:error:]
game-center
binding != NULL
_LSDatabaseCreateFromPersistentStoreIgnoringRecoveryFile
localized
_LSBindingListDestroy: binding list not found
systemgroup.com.apple.lsd
LSHandlerRoleEditor
/family/messages
specified plugin units were not available
TVUserActivityTypeBrowsingChannelGuide
com.apple.security.exception.files.absolute-path.read-only
NSUserElection
!isnan( timeout ) && !isinf( timeout ) && timeout > 0.0
com.apple.lsd.unregisterPluginAtURL:operationUUID:reply
com.apple.seld.tsmmanager
BGPermittedIDs
Caller is not allowed to map pluginIDs/bundleIDs, required entitlement missing
com.apple.private.security.container-required
ACTIVE
<FSNode %p> { isDir = %c, path = '%s' }
-[_LSDIconClient setAlternateIconName:forIdentifier:iconsDictionary:reply:]
v24@?0@\"_LSDiskUsage\"8@\"NSError\"16
-[FSMimic nameWithError:]
/Library/Preferences/com.apple.mobilephone.speeddial.plist
LSBundlePersonaRecordMap.m
LSHandlerRoleNone
public.character-special
are
forbidden-ls-internal-symbol-invoked-directly
pluginIDs != nil
not a builtin plugin
%llu
validatePrecondition
v24@?0@\"ICLBundleRecord\"8@\"NSError\"16
prefers-native-cfm
_LSDispatchWithTimeout
-[_LSDReadClient getBundleRecordForCoreTypesWithCompletionHandler:]
AutomaticDowngrade
can't remove last persona from data container mapping
profile validated
vocabulary
persistent identifier of length %zu is too short to extract sequence number!
RUNNING_IN_SYNC_BUBBLE
NSXPCConnection *_LSDServiceGetXPCConnection(__unsafe_unretained Class _Nonnull, _LSDServiceDomain *const __strong _Nonnull)
q24@?0@\"_LSInstallNotificationJournaller\"8@\"_LSInstallNotificationJournaller\"16
_ISInvalidateCacheEntriesForBundleIdentifier
kLSBundleClassNull
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/LSContainer.mm
exactly one of result %@ or error %@ must be nonnil
Could not create CF instance
_LSCopyGroupContainerURLSFromContainermanagerForPersona
Seeded Model Code
LS_SUFFIX_FOR_REMOTE_XCTESTS
quarantined
LS_NO_PERSISTENT_PREFS
_LSSupportsRemoval
 (bundle ver)
record != nil
v28@?0B8@\"<LSRegistrantDatabaseContext>\"12@\"NSError\"20
com.apple.coremedia.allow-mpeg4streaming
distinctUnregisteredTypeCount
path-patterns
-[LSApplicationWorkspace(DefaultApps) setDefaultApplicationForCategory:toApplicationRecord:completionHandler:]_block_invoke
native
beta-reports-active
com.apple.fsevents
UMUserPersonaAttributes
SUCCESS
LS default app setter queue
/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
id
com.apple.LaunchServices.database
EXExtensionPointIsPublic
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSAppLink.mm
FBSOpenApplicationOptionKeyIsSensitiveURL
v24@?0{LSSliceData=ii}8*16
library
allowed partner financing bundleIDs
sequenceNum
no-executable
OriginalInstallDate
com.apple.private.coreservices.can-send-install-notifications
com.apple.private.subscriptionservice.internal
_LSAliasAdd
-[LSApplicationRecord initWithJobLabel:error:]
com.apple.developer.translation-ui-provider.network-access
{?=[8I]}
operator()
LSApplicationCategoryType
com.apple.lsd.rebuild
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
ptr != NULL
<%@ %p %s>
-[LSApplicationRestrictionsManager _LSResolveIdentifiers:]_block_invoke
.open
com.apple.springboard.statusbarstyleoverrides
/private/var/mobile/Library/Preferences/com.apple.MobileCoreServices/com.apple.LaunchServices.plist
CLASSIC_SUFFIX
one-tap-openable
v32@?0@\"LSRecordPromise\"8@\"<_LSPendingSaveToken>\"16@\"NSError\"24
CFUserNotificationCreate() failed.
-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke
CREATE TABLE IF NOT EXISTS Election( identifier TEXT PRIMARY KEY NOT NULL, timestamp INT DEFAULT CURRENT_TIMESTAMP NOT NULL, userElection INT);CREATE TRIGGER insert_Timestamp_Trigger AFTER INSERT ON Election BEGIN UPDATE Election SET timest
FSEventStreamCreateRelativeToDevice
com.apple.LaunchServices.DocumentTypesChanged
com.apple.lsd.waiting_queue
setup.icloud.com
com.apple.launchservices.applicationsDidFailToUninstall
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSPlugInQueryAll.m
UTIBinding
LSD_SERVICE_BASE
LSDefaultAppCategoryNavigation
com.apple.radios.plist
invalid plugin URL
v32@?0I8I12r^{?=IIIIiII[8I]IIIIIIIII}16*24
insecureProcessID
work != nil
invalid bundleInit for unregistering
DataProtectionClass
nil URL provided to %s
LSHandlerRank
docID
.modifydb
LSDefaultAppCategoryPhoneCalls
-[LSMIResultRegistrantServerDatabaseContextProviding init]
public.ruby-script
   allocator = %p\n
   latency = %llu (microseconds)\n
has-cohort-metadata
IsEligibleForWatchAppInstall
v32@?0@\"UTTypeRecord\"8q16^B24
select userElection from ( select identifier, userElection , 0 as legacy from Election UNION SELECT identifier, userElection, 1 as legacy from LegacyElection) where identifier = ? ORDER BY identifier, legacy limit 1
com.apple.hsa-authentication-server
com.apple.TestFlight
openState != nil
isDirectory
deallocating resumed but uninvalidated monitor
MI_Persona_BundleID_Relayering
com.apple.lsd.registrationIO
public.contact
com.apple.applescript.text
fileNames
DB Object
FBSOpenApplicationOptionKeyAppLink4LS
/Library/Printers/
localizedDescription%s
UniqueInstallID
ensure monitoring for invalidated monitor
self != [_LSDService class]
containingBundle
BOOL _LSServer_LSHandlerPrefMigrateBundleID(LSContext *, NSString *__strong, NSString *__strong, LSVersionNumber, NSError *__autoreleasing *)
typeRecord
AppleIDValidatedItemsRecordDataCertificateType
Client
const void *_XCFRetain(CFAllocatorRef, const void *)
-[FSNode(ExtendedAttributes) setExtendedAttribute:name:options:error:]
ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn
WrongHeaderLength
com.apple.private.coreservices.definesExtensionPoint
com.apple.coremedia.allow-protected-content-playback
Hit the client-side query resolution codepath from within lsd! This is a serious bug! Please file a radar against Launch Services.
/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
provided a snapshot queue but it was not equal to the queue in the db to snapshot
com.apple.private.coreservices.can-access-unregistered-type-info
com.apple.developer.associated-domains
com.apple.authkit.client.internal
Could not look up MDT service
com.apple.launchservices.app-placeholders
initialODRSize
-[_LSDOpenClient openApplicationWithIdentifier:options:useClientProcessHandle:completionHandler:]
-[LSApplicationIdentity findApplicationRecordFetchingPlaceholder:error:]
PersonalType
com.apple.apple-internal-library
FSNode
{\"v\":%d,
CleanTimeout
public.disk-image
AppleID
restricted bundleIDs
com.apple.frontboard.launchapplications
com.apple.systempreference.prefpane
com.apple.alias-record
v16@?0^{__CFDictionary=}8
com.apple.FaceTime
targetApp != nil
com.apple.private.security.no-sandbox
kLSBundleClassMDImporter
backtrace
versionIdentifier
   f2d_private_port = 0x%x\n
-[LSApplicationIdentity initWithBundleIdentifier:allowPlaceholder:personaUniqueString:error:]
kLSBundleClassDriverOrSystemExtension
Unicode
group ctrs
<
can't provide with mimic
public.app-category.board-games
LSEligibilityUninstallPredicate
LocalizedString
<%@ %p> %@
scheme-mapping
tags
Path:%@
UIMainStoryboardFile
pages
Beta:%@
Widgets
/System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials
UTKEXTIdentifier
-[LSApplicationWorkspace(DefaultApps) setDefaultMailClientToApplicationRecord:completionHandler:]_block_invoke
BundleID:%@
com.apple.locationd.authorizeapplications
v32@?0@8@16^B24
-[_LSDModifyClient unregisterBundleUnit:options:completionHandler:]
process may not map database
@`
LSInstallType
armv6
com.apple.springboard.appbackgroundstyle
%@.%f.%d
Code
com-apple-audiounit
raw extension point ID
file
has-parallel-placeholder
getAffectedBundleInfoForIdentifiers
-[_LSDModifyClient registerContainerURL:completionHandler:]_block_invoke
removePersona
com.apple.nanosystemsettings
!streamRef->isStarted
CFBundleAlternateIcons
parentApplicationIdentifiers
SCHEME_APPROVAL_PROMPT_TITLE_NO_SOURCE
Precondition not met: %@
BOOL _LSPathMatchesPath_NoIO(NSString *__strong, NSString *__strong, LSPathMatchType)
MobileDataTransitErrorLine
void _LSDatabaseClean(LSDatabaseHandle)
outSafeBaseName != NULL
code signature version
NSXPCInterface *_LSOpenResourceOperationDelegateGetXPCInterface()_block_invoke
prepareApplicationDeviceManagementPolicyValue
com.apple.launchservices.private._LSDMFPolicyDidChangeNotification
com.apple.developer.ubiquity-kvstore-identifier
No container set for plugin
_LSSchemeApprovalFindWithCompletionHandler
NSData *_LSValidationTokenComputeHMAC(NSData *__strong, NSData *__strong)
COPYING
+[UTTypeRecord _typeRecordWithContext:forPromiseAtNode:error:]
missing
launch-prohibited
plistFlags
CFBundleAllowMixedLocalizations
_LSDReadService
com.apple.lsd.rebuildAnalyticsSubmit
NoEncodedDSID
min version
outFlags != NULL
Application
LSHandlerRoleViewer
bundleVersion
referrerURL
needs-reg
v32@?0@\"NSString\"8@\"NSString\"16*24
kTCCServiceReminders
com.apple.LSPkgInfoKey
ExtensionKit
bundleUnit
critical
Apple Application Integration Certification Authority
UserInfo
stash_system_content_database_to_diagnostics
Unknown directory class
progress
FBSOpenApplicationErrorCodeToString
SELECT bundleID, COUNT(*) FROM unregisteredTypeRequests GROUP BY bundleID;
v32@?0@\"NSString\"8@\"NSArray\"16^B24
.xpc
_LSDisplayRemovedAppPrompt
xctest
DeviceClassNumber
CFBundleIconFiles
Nonce
<LSPersistentIdentifier %p> { v = %u, t = 0x%llx, u = 0x%llx, db = %s
com.apple.application-bundle
APP_REMOVAL_PROMPT_DETAIL_APP_STORE_DELETED_SELF
gameCenterEverEnabled
LSLaunchDLabel
.dissemination
LS MDT helper thread/run loop
_LSIconPath
-[LSFeatureFlagPredicate initWithDictionary:error:]
public.volume
OFF
LSOneTapOpenBehaviorKey
_LSUnregisterPluginsAtURL
Show in App Store
com.apple.lsd.xpc
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Server/LSDModifyService.mm
Failed to create XPC listener for class %@
NSExtensionAttributes
missing persona unique string
asynchronous (client)
LSContainer.mm
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/Util/LSDefaults.m
{\"v\":2,\"b\":%@,\"it\":%lu}
com.apple.private.coreservices.lsaw
public
com.apple.security.exception.iokit-user-client-class
is-override
Attempted to get a kind string when performing bundle lookup.
prefers-classic-cfm
+[_LSDiskUsage(Private) usageFromMobileInstallationForBundleIdentifier:error:]_block_invoke
_LSRegisterTypeDeclarationsForPlugin
EXDiscoverFromHiddenApps
UTTypeBreadBoardTestMode2Description
personas
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Server/LSDReadService.mm
NSString *LSDefaultAppCategoryCopyName(LSDefaultAppCategory)
arm64e.x1
dispose_d2f_port
com.apple.developer.replace-plugin
org.reactjs.native.Popspedia
inoBundle
NewsstandArtwork
_LSIsLinkEnabled
release
NSAppClip
LSWorkspaceObserverPing
-[LSDExtensionLaunchConfigurationStore _readBootInfo]
root
-[_LSDModifyClient forceSaveForTestingWithCompletion:]
making string localizer
-[LSApplicationWorkspace(URLQueries) isApplicationAvailableToOpenURLCommon:includePrivateURLSchemes:error:]
Failed to allocate CFMutableSet for category types.
Type
_LSDatabaseSave
/System/Cryptexes/App/System/Library/CoreServices
v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24
com.sun.java-class
inDestURL != nil
Got extension \".%@\" from caller-supplied filename. This is less accurate than passing a file URL.
ppc64
Failed to get URL for lsd-schemes file
This app has exceeded the number of allowed scheme queries
LSRatingRankEligibilityMonitor.mm
NOTIFICATION
NSDictionary<NSString *,NSString *> *LaunchServices::LocalizedString::getAllUnsafeLocalizations(_LSDatabase *__strong _Nonnull, NSString *__strong _Nullable, BOOL * _Nullable, BOOL * _Nullable) const
The claim record was bound to an unknown bundle record.
dataContainer
bundleidentifier
com.apple.springboard.allowIconVisibilityChanges
KEXT-icon
has-audiocomponents
void _LSEnumerateAllClaimedTypesOrSchemesForBundleID(LSContext * _Nonnull, const LSBundleData * _Nonnull, LSRolesMask, BOOL, void (^__strong _Nonnull)(NSString *__strong, const LSClaimData *))
FBSOpenApplicationOptionKeyBrowserAppLinkState4LS
-[LSApplicationRecord(Identities) identities]
This app is not allowed to query for scheme %@
bindings
%@.plist
_dispatch_
LSMoveDocumentOnOpen
if asyncing _LSContainerAddWithNode it cannot use a caller's context
CFBundleIconFile
ProfileValidated
has-eligibility-deletion-domain
v24@?0^v8Q16
BOOL _LSDisplayMachineReadableData(LSContext * _Nonnull, FILE * _Nonnull, NSSet<NSString *> *__strong _Nullable, NSPredicate *__strong _Nullable, _LSDisplayDataOptions, NSError *__autoreleasing * _Nullable)
-[_LSDReadClient getTypeRecordWithIdentifier:allowUndeclared:completionHandler:]
com.apple.lsd.LSDatabaseBlockingFetchServer
Unregister bundles - End
-[FSNode initWithConfigurationString:flags:error:]
+[LSAppLink(Private) URLComponentsAreValidForAppLinks:error:]
Truncating a list of bindings to max %lu known-good ones.
is-Newsstand-App
has-uibackgroundmodes
com.apple.LaunchServices.DefaultAppCategory.Calling
+[LSOpenStagingDirectoryManager sharedServerInstance]
B24@?0@\"_LSQueryResult\"8@\"NSError\"16
bad_function_call was thrown in -fno-exceptions mode
v32@?0@\"NSString\"8@\"NSDictionary\"16^B24
-[_LSCanOpenURLManager(PrivateSchemeChecking) isBundleID:bundleData:context:allowedToCheckScheme:error:]
inPluginData
notejournal
-[FSNode initWithDirectory:inDomain:lastPathComponent:createIntermediateDirectories:flags:error:]
LSIncludeAppLinksForCallingApplicationKey
-[LSApplicationWorkspace(DefaultApps) setDefaultURLHandlerForScheme:to:completion:]_block_invoke_2
caller-supplied filter
inBlock != NULL
0123456789abcdef
UIStatusBarStyle
LS_FORCE_URL_PROPERTY_PREP_OOP
Attempted to use uninitialized FSNode %p.
Extensions
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Base/LSDMFSupport.mm
UpdatePlaceholderMetadata
LSMinimumSystemVersion
public.bookmark
public.
<LSBundleRegistrationStatePrecondition: %@ placeholder: %@ fullApp: %@>
IsDefault
To do this, you need to install a relevant handler app.
reg date
resolves-icloud-conflicts
com.apple.assistant.dictation.prerecorded
Wildcard document claim
v24@?0@8@\"NSError\"16
_LSCheckIfApplicationCanOpenUSBOrSMBDocument
v16@?0@8
referenceAccessoryPath
@\"_CSVisualizer\"24@?0^v8@16
com.apple.news
com.apple.springboard.wallpaperAnimationSuspension
Registered bundle status = %@
 (skipped)
QLGenerator
-[_LSDefaults HMACSecret]
ContainerErrorDescription
record-pi
LSApplicationIdentity.mm
Skipping weak binding due to options
kLSBundleClassCannedSearch
BindingList
-[_LSDReadClient getRelatedTypesOfTypeWithIdentifier:maximumDegreeOfSeparation:completionHandler:]
-[_LSDServiceDomain resolvedDomainUID]
com.apple.CommCenter.fine-grained
_LSGetDataForUserActivity
LSMultipleInstancesProhibited
PluginUUIDBinding
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSBundleRecordBuilder.mm
# (%i)
public.calendar-event
Path extension allegedly starts at the beginning of the display name, which is invalid.
com.apple.private.hid.client.service-protected
must have completion
getLocalizedKindStringDictionary
restricted due to rating
inSearchBlock != nil
DownloaderDSID
com.apple.private.coreservices.cansetalternateicons
InstallingPlaceholder
static std::optional<CanonicalString> LaunchServices::CanonicalString::Create(_LSDatabase *__strong _Nonnull, NSString *__strong _Nonnull, NSDictionary<NSString *,NSString *> *__strong _Nonnull)
/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDMAppManagement.plist
DeviceBasedVPP
db-spi
isSystemManaged
revision
-[_LSCanOpenURLManager(PrivateSchemeChecking) legacy_isBundleID:bundleData:context:allowedToCheckScheme:error:]
cannedsearch
__NO_PERSONA__
SBAppUsesLocalNotifications
~%@
-[_LSDModifyClient setUpdateAvailabilities:completionHandler:]
_LSPluginCheckExtensionPoint
<%@: %@ (type %d)>
isSystemSession
kLSBundleClassRemotePlaceholder
recordMap
public.app-category.family-games
Server not supported error
allowlisted bundleIDs
Adding and sorting bundles
has-MID-based-SINF
com.apple.Contacts.database-allow
_
isBlocked
App validation failed (no executable path), ignoring didInstall notification for %@
com.apple.siri
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSFeatureFlagPredicateEvaluator.mm
appinstallation
<%@ %p> { %lu localizations loaded: %@ }
-[_LSApplicationState initWithCoder:]
com.apple.private.extensionkit.crossPersonaLaunch
CCStatusErrorDomain
datasep
InstalledContentLibrary
streamRef->cfRunLoopSourceRef != NULL || streamRef->event_source != NULL
targetApplicationRecord
com.apple.private.suggestions.contacts
Authentication disabled
applicationIdentifier
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Server/LSDIconService.m
v44@?0@8@\"FSNode\"16@\"NSXPCListenerEndpoint\"24B32@\"NSError\"36
-[LSClaimBindingConfiguration initWithDocumentProxy:]
Binding application %@ to itself
application
+[LSBundleRecord _bundleRecordForApplicationIdentifier:context:pluginFindOptions:error:]
LSMaximumSystemVersion
SignerOrganization
_LSDisplayData
LS open operation queue
v32@?0@\"NSString\"8@\"NSString\"16^B24
activityTypes
-[_LSDModifyClient setPreferenceValueForCallingApplication:forKey:completionHandler:]
Publishing-Any; Any-Latin; NFKD; [:^ASCII:] Remove
disabled
EXRequiresLegacyInfrastructure
setForNode
com.apple.videoconference.allow-conferencing
NSExtensionContainingApp
MCEffectiveSettingsChangedNotification
App Clip Parents
%@ (%s)
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Base/LSDisplayNameConstructor.mm
com.apple.private.mobileinstall.allowedSPI
UTTypeCore.mm
   callback = %p\n
kLSBundleClassXPCService
InvalidType(%lu)
LSSupportsGameMode
System
Could not copy unique ID
_LSServer_OpenUserActivity_block_invoke
platform-application
 5#1%4#0\"2
public.url-scheme
-[_LSDReadClient getTypeRecordForPromiseAtURL:completionHandler:]
com.apple.news.widget
>
value
-[_LSPersonaDatabase personaWithAttributesForPersonaUniqueString:error:]
v24@?0@\"NSArray\"8@\"NSError\"16
Desktop
UIApplicationSupportsAlwaysOnDisplay
IsSwiftPlaygroundsApp
LSContainerHelpers.m
resourcesDirectoryURL
storeCohort
@\"NSData\"8@?0
category %lu
[pid:%d/%d uid:%d/%d gid:%d/%d %d/%d]
getTypeUnit
scheme != nil
LSDatabase.mm
com.apple.lsd.advertisingidentifiers
UAUserActivityManagerActivityContinuationIsEnabledChangedNotification
CFBundleInfoPlistURL
com.apple.private.extensionkit.builtinsystempersona
com.apple.accounts.facebook.defaultaccess
importer
extensionPointRecord != nil
LSDefaultLocalizedValue
asynchronous (server)
CFBundleShortVersionString
com.apple.intents.extension.discovery
-[LSPlugInQueryWithURL _enumerateWithXPCConnection:block:]_block_invoke
com.sun.java-source
CFBundleRawInfoPlistURL
No known standalone plugin for %@
query
public.jpeg
-[LSApplicationWorkspace ls_injectUTTypeWithDeclaration:inDatabase:error:]
GC
dynamic
apfs
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Base/FSMimic.mm
-[_LSDReadClient getCurrentApplicationDefaultInfoForCategory:completion:]
localizedShortNames
keychain-access-groups
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_
Skipping parent UTI claims due to options
staticSize
_LSDatabaseCreateSnapshotAgainstAccessContext_block_invoke
failed to reset user election
LSDefaultAppsCore.mm
com.apple.coreaudio.allow-amr-decode
_LSHandlerPrefRemoveAllWithBundleID_block_invoke
<CSIdentityAuthority %p [%p]>{localizedName = \"%@\"}
-[LSApplicationWorkspace uninstallContainerizedApplicationWithIdentifier:options:error:progressBlock:]
appletv
v28@?0^{__CFArray=}8C16^{__CFError=}20
kSFAppleIDClientPersonInfoAccountIdentifierCFKey
node
itemName
bogus input persona for input appex
com.apple.lsd.system.plugin
ignoreAppLinkEnabledProperty
public.audio
SupportsAudiobooks
inBindingList != kCSStoreNullID
com.apple.private.healthkit
rank
cannot directly instantiate LSPlugInQuery
public.app-category
Macintosh
FSEventStreamUnscheduleFromRunLoop
IsParallelPlaceholder
Updated PlaceholderMetadata for app with error %@
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSExtensionLaunchConfiguration.m
-[_LSDModifyClient performPostInstallationRegistration:operationUUID:reply:]
registrationDate
com.apple.lsd.appremoval
-[LSApplicationWorkspace updateiTunesMetadataWithData:forApplication:options:error:]
-[_LSDocumentProxyBindingQuery _enumerateWithXPCConnection:block:]
clickAttribution
_NSURLStrongBindingKey
?0=
UpdateSinfForLaunchServices
-[FSNode getFileSystemRepresentation:error:]
bundleIdentifier
INIntentsRestrictedWhileProtectedDataUnavailable
UUID must not be nil
HasCustomNotificationKey
SIMULATOR_ROOT
appContainer
UIApplicationSystemWindowsSecureKey
UIBackgroundStyle
UTTypeTagSpecification
v16@?0@\"NSError\"8
jobLabel != nil
com.apple.launchservices.applicationsDidUninstall
LS database changed notification queue
com.apple.package
com.apple.launchservices.applicationsWillUninstall
Volume
Database seeding is incomplete.
v32@?0@\"NSDictionary\"8@\"NSSet\"16@\"NSError\"24
_LSSessionSave
NSURL *pluginKitUserElectionStoreURL()_block_invoke
-[LSInstallProgressObserver setProgressProportionsByPhase:forInstallOfApplicationWithIdentifier:completion:]
NSRegulatoryPrivacyDisclosure
-[LSApplicationWorkspace sendNotificationOfType:forApplicationWithBundleIdentifier:requestContext:error:]
-[LSApplicationWorkspace(DefaultApps) defaultApplicationForCategory:error:]
/System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
platform default
Documents
inContext != NULL
UnknownType
The specified application is currently installed or installing.
com.apple.iTunesStore.downloadInfo
com.apple.lsd.open
com.apple.LaunchServices.DefaultAppCategory.Navigation
\x91
com.apple.private.hsa-authentication-processing
com.apple.lsd.sigact
Must call FSEventStreamStop() before calling FSEventStreamInvalidate()
installation-hold
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSBundleQuery.mm
-[_LSDModifyClient registerContainerURL:completionHandler:]
bundleClass
displayName
_LSUnregisterAppWithBundleID
-[LSApplicationWorkspace registerBuiltinStandaloneExtension:personaUniqueStrings:operationUUID:requestContext:saveObserver:registrationError:]
DTAppStoreToolsBuild
useractivity-team-identifier
Mac Catalyst
void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = void (^)(unsigned int, const LaunchServices::UTTypeDisplayNameFlavor &, unsigned char *)]
-[FSNode bundleIdentifierWithContext:error:]
CFBundleIcons
com.apple.LaunchServices.DefaultApps
Attempting to set an observer's delegate while it is already observing.
Finished registering %@, bundle unit %llx
ISGraphicIconConfiguration
-[LSApplicationWorkspace _openUserActivity:orUserActivityUUID:activityTypeForUUID:withApplicationProxy:options:completionHandler:]
com.apple.LaunchServices.browserSettings
has-prerendered-icon
inBundleData != NULL
kTCCServiceAddressBook
public.delimited-values-text
/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
Finished rebuilding LaunchServices database
v32@?0@8@\"FSNode\"16@\"NSError\"24
DTPlatformName
<%@ %p> %@ %@ %i %i
com.apple.developer.ubiquity-container-identifiers
prepareStrongBindingValue
B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1
icon flags
AutomaticDownload
public.midi-audio
com.apple.system-library
LSAppLink.mm
applicationDSID
DocumentManager
numbers
LSDefaultApplicationQueryBackend.mm
LSApplicationSecondaryCategoryType
context != NULL && context->db != NULL
all personas and platforms
allowURLOverrides
UIApplicationShortcutWidget
LSPrefs.mm
com.lsinstallprogress.appcontrols.resume
registering changed bundle
eligibility-checked-browser
bundlePersonas
Database not availabile yet
ioExtension != NULL
UPP validated
/Network/Applications/
browserState
server local database differed from context after registration?
CertificateOK
CN=Apple Root CA,OU=Apple Certification Authority,O=Apple Inc.,C=US
name
UISupportedExternalAccessoryProtocols
com.apple.developer.web-browser-engine.host
watchsimulator
com.apple.mobile.deleted.AllowFreeSpace
-[_LSClaimBindingTypeIdentifierBindable typeRecordWithError:]
forbidden-ls-deprecated-symbol
v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24
LSUnregisteredTypeTelemetryMaxAge
-[LSBundleRecord(Redaction) unredactWithError:]
MachOUUIDs
UTTypeDescription
public.make-source
-[LSApplicationRecord categoryTypesWithError:]
can't end rebuild context: current context is different!?
-[_LSDOpenClient openAppLink:state:completionHandler:]_block_invoke
authority
Adding and sorting parent UTI claims
file-sharing-enabled
+[LSBundleRecord _bundleRecordForAuditToken:checkNSBundleMainBundle:error:]
LSIsAppleDefaultForScheme
v24@?0@\"LSApplicationExtensionRecord\"8@\"NSError\"16
LSSetHandlerOnDocumentOpenKey
type != LSBundleTypePlugInKitPlugin
com.apple.private.canIgnoreAppLinkEnabledProperty
com.apple.launchservices._LSSettingsInProcessStore.notification
com.apple.private.lockdown.finegrained-get
com.apple.xpc-service
v16@?0@\"NSString\"8
public.mpeg-4
_createAndAddRunLoopSource
previously found to be not-OK
in-generational-storage
itemFlags
v16@?0@\"NSDictionary\"8
_LSBundleExtensionPoints
v28@?0B8@\"NSError\"12@\"NSString\"20
May not update container registation
v16@?0@\"LSMarketplacesPreferences\"8
base flags
APProtectedShieldOptOut
v16@?0@\"NSSet\"8
public.php-script
-[LSApplicationWorkspace(DefaultApps) setDefaultURLHandlerForScheme:to:completion:]_block_invoke
CFMutableDictionaryRef _LSCopyBundleInfoDictionary(CFBundleRef)
no publishing key
Preferences %@ loaded.
installState
placeholderInstalled
CFBundleIcons dictionary is missing or incorrect type
Internal
Bad context provided
LSApplicationProxy.m
_LSIsDocumentOpenRequestValid
CFBundleURLTypes
com.apple.media.ringtones.read-only
<LSProgressNotificationTimer: %@>
SFAppleIDClientCopyCertificateInfo
Could not get bootstrap port
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Workspace/LSApplicationWorkspace.m
buildVersion != nil
v16@?0@\"LSDatabaseRebuildContext\"8
-[_LSDIconClient getAlternateIconNameForIdentifier:reply:]
com.apple.default-app.web-browser
SDKVersion
com.apple.LaunchServices.applicationUnregistered
MDTCopier
LSExplicitlyRestrictable
wdgt
_LSContextInitReturningError() failed with error %@
Need to prepare after first iteration. This should not be possible.
/private/preboot
-[FSNode(ExtendedAttributes) extendedAttributeWithName:options:error:]
appex
NOT FOUND!
+[_LSDiskUsage(Private) mobileInstallationQueue]
CFBundleName
/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
StaticDiskUsage
digest mismatch fetching extension launch configuration
kSFAppleIDClientAccountInfoAppleIDCFKey
bundleUnit == kCSStoreNullID || context != NULL
+[_LSSharedWebCredentialsAppLink afterAppLinksBecomeAvailableForURL:limit:performBlock:]_block_invoke
_UI
com.apple.developer.mail-client
com.apple.telephonyutilities.callservicesdaemon.callprovidermanager
.%@
Unit exhaustion in table %@
/dev/console
com.apple.quicktime-image
_LSBundleApplyCheckUpdate
+[_LSDService(SubclassesShouldOverride) clientClass]
com.apple.launchservices.receivereferrerrurl
DTSDKName
%s: %@ FILTERED
reqCaps
-[LSBundleRecord(Containers) dataContainerURLForPersonaWithUniqueString:error:]
_LSSchemeApprovalUsePreferenceOrPromptWithCompletionHandler
-[_LSDAppProtectionClient setHiddenApplications:completion:]
data
-[LSBuiltinApplicationRegistrant runWithCompletion:]_block_invoke_2
com.apple.lsd.registerBuiltinAppex:operationUUID:reply
pluginfault
SystemDataOnly-%s-
CoreSpotlightActionTitle
-[LSApplicationWorkspace unregisterBuiltinApplicationAtURL:operationUUID:requestContext:saveObserver:error:]
Assets.car
kNotificationActivationStateChanged
BreadBoard
process_dir_events
1
app-clip
LSPluginBundle.mm
public.comma-separated-values-text
has-feature-flag-predicate
mobile
com.apple.idms.appleid.prd
com.apple.launchservices.applicationInstallsDidStart
virtual std::optional<os_eligibility_answer_t> LaunchServices::ServerDomainEvaluator::eligibilityForDomain(os_eligibility_domain_t, NSError *__autoreleasing *)
Hit the client-side remote-expensive query resolution codepath from within lsd! This is a serious bug! Please file a radar against Launch Services.
com.apple.mobileconfig
/var/mobile/Library/Caches/com.apple.itunesstored/url-resolution.plist
INDEX.BDMV
.appex
contentManaged
-[_LSDReadClient resolveQueries:legacySPI:completionHandler:]
LSOpenCallbackWaitMode
com.apple.coretelephony.Identity.get
host-patterns
AppleIDValidationRecordOptionDoNotEvaluateTrustRef
ProgressProporitions.plist
_LSFunction
<%@ %p> \"%@\"
id _LSLazyLoadObjectForKey(NSMutableDictionary *__strong _Nonnull, __strong id _Nonnull, __strong dispatch_queue_t _Nonnull, NS_NOESCAPE _LSLazyLoadGenerator __strong)
void _LSAskForScreenUnlock(__strong dispatch_queue_t _Nullable, void (^__strong _Nonnull)(BOOL, NSError *__strong))
DisableAirDrop
installed
com.apple.launchservices.clientcallbacks
%@:
apple-default
Boolean _LSDispatchCoalescedAfterDelay(volatile int32_t * _Nonnull, __strong dispatch_queue_t _Nonnull, NSTimeInterval, __strong dispatch_block_t _Nonnull)
-[FSMimic getFileSystemRepresentation:error:]
:error:
v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b
LSBackgroundOnly
_LSGetDispatchWithTimeoutCompletionHandler_block_invoke
v16@?0^{BindingResult=^^?}8
3rd party
com.apple.coreservices.DatabaseRebuildStatistics
wrong number of appex records
Must call %s from within the Launch Services daemon.
CFBundlePrimaryIcon
Updating PlaceholderMetadata for %@ with LSInstallType %@
supports-audiobooks
com.apple.lsd.installation
pv-
Folder
-[_LSDReadClient getKnowledgeUUIDAndSequenceNumberWithCompletionHandler:]
-[LSServerOpenStagingIOPersonality stagingDirectoryKeyForFileHandle:error:]
lazyPlist
filterBlock != nil
DELETE FROM unregisteredTypeRequests WHERE firstAccessDate < ?;
keys != nil
_LSGetItemInfoFlagsForNode
-[_LSDModifyClient unregisterBundleUnit:options:completionHandler:]_block_invoke_2
NSLocationWhenInUseUsageDescription
personaMap
Called +stopAccessing when not accessing the database. This is a bug in the Launch Services client.
com.apple.homekit.private-spi-access
News app extension is restricted
v20@?0^{__SecIdentity=}8i16
NSBackgroundActivityUsageDescription
SBIconVisibilityDefaultVisible
LNIsLinkEnabled
Unknown
MCFeatureSystemAppRemovalAllowed
contentDescriptors
LSCanOpenURLManager.mm
<%@: %p %@>
v24@?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}QBB}8^B16
-[_LSDOpenClient updateRestrictionKnowledgeWithCompletionHandler:]
<>
prepareHFSTypeCodeValue
effectiveBundleIdentifier
-[_LSRemotePlaceholderEnumerator _applicationRecordWithContext:bundleIdentifierOrUnit:]
have error even though we succeeded!? %@
 (MIME %@)
void _LSContainerAddWithNode(LSContext *, FSNode *__strong, Boolean, void (^__strong)(LSContainerID, NSError *__strong))
app
com.apple.LaunchServices.DefaultAppCategory.SideButton
cryptexContentScanTime
ENTITLEMENT:
ersatz
p
%@://
_LSCopyLocalDatabase
_LSSchemaConfigureTable
PhoneAppCoupledRelay
LSMobileDataTransitSupport.mm
UIStatusBarHidden
/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
MCFeatureRemovedSystemAppBundleIDs
Skipping alternate UTI claims (no UTI!)
-[_LSDModifyClient removeHandlerForURLScheme:completionHandler:]
DeviceManagementClient
is-legacy-plugin
Owner
SpecialAppEligibilityState.plist
depth > 0
-[LSApplicationWorkspace updateiTunesMetadataWithData:forApplicationAtURL:error:]
_LSBundleFindWithInfoAndNo_IOFilter
+[LSFeatureFlagPredicate(LSBundleDataPredicate) featureFlagPredicateForBundle:bundleData:database:error:]
-[LSApplicationWorkspace _getBundleIdentifierForBundleAtURL:invokeUpdateBlockAndReregister:error:]
Device Family
identifier
public.app-category.simulation-games
Predicate key Conditions was not a dictionary
com.apple.LaunchServices.DeviceIdentifierEntropy
public.block-special
-[LSApplicationIdentity initWithIdentityString:parsedIdentityStringDictionary:error:]
getLocalizedKindStringWithEvaluator
v32@?0@\"<LSDetachable>\"8Q16^B24
bundleClassMask
com.apple.launchservices.hiddenPreferenceNotification
-[_LSInstallProgressService createInstallProgressForApplication:withPhase:andPublishingString:reply:]
BDMV/INDEX.BDMV
-[_LSAppLinkPlugIn appLinksWithContext:error:]
sequenceNumber
UMUserManager
com.apple.developer.game-center
all values equal
v20@?0I8@\"NSError\"12
-[_LSDOpenClient canOpenURL:publicSchemes:privateSchemes:completionHandler:]
v20@?0I8I12I16
propertyList
CertificateRevoked
Media
prioritizable
-[LSApplicationWorkspace sendApplicationStateChangedNotificationsFor:stateProvider:completion:]_block_invoke_2
com.apple.MobileSMS
AudioUnitURLOpen
-[_LSDModifyClient setContainersForApplicationsWithBundleIdentifiers:unbundledExtensionsWithBundleIdentifiers:fromBundlePersonaRecordMap:operationUUID:reply:]
com.apple.private.game-center.bypass-authentication
provided record was not attached
_bundleIDs
_FSEventStreamCreate
-[_LSApplicationProxyForIdentifierQuery _enumerateWithXPCConnection:block:]
LSDServerExtensionLaunchConfigurationRegistrar.m
file-read-data
version
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Record/LSApplicationRecord.mm
no container but no error from containermanager
Seeded System Version
com.apple.lsd.system.dissemination
Other (%llu)
appletvsimulator
user prefers no handler for : %@ %@
IntentionalDowngrade
flagsData
com.apple.launchservices.schemeapproval
FSEventStreamFlushSync
LSUserInitiatedUninstall
@\"NSSet\"8@?0
kLSBundleClassSystemPlaceholder
LSAdvertiserIdentifier
com.apple.icloud.findmydeviced.access
B16@?0^v8
*** Claim C%08lu has invalid bundle reference B%08lu
LS(Proxied)BundleRecord
accountInfo
v16@?0@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">8
NSUserActivityTypes
\"
model (?)
com.apple.BackToMyMac
Found
invalid containerURL
Migration
/Library/Caches/com.apple.xbs/2471A98B-113A-43B7-ADD2-2BB2E2EC37F9/TemporaryDirectory.OZDxI5/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Record/LSiTunesMetadata.mm
B24@?0^{LSContext=@}8r^{LSBinding=I^{LSBundleData}I^{?}@@Q}16
/var/mobile/
com.apple.developer.messaging-app
public.avi
-[LSAltIconManager setAlternateIconName:forIdentifier:iconsDictionary:reply:]
rec mod date
v24@?0@\"LSBundleProxy\"8@\"NSError\"16
-[_LSDModifyClient setHandler:version:forURLScheme:completionHandler:]
num_paths == event_flagsCnt
invalid container Unit
v28@?0@\"NSString\"8I16*20
bundleFlags
.icons
node != NULL
com.apple.telephonyutilities.callservicesdaemon.callstatecontroller
SchemeApproval
LaunchServices: registering extension point %@
MAIL_REMOVED_VAGUE_TITLE
appexRecord
x-keynote-live
public.app-category.dice-games
_LSBacktrace
SBLaunchSuspendedAlways
OSStatus _LSUpdateContainerStateAsync(__strong LSDatabaseRef, LSContainerID, LSContainerData *)
-[_LSValidationToken initWithCoder:]
--
kLSBundleClassCoreTypes
```
