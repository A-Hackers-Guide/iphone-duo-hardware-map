# `FBSApplicationInfo`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSBundleInfo`
- Protocols: `BSDescriptionProviding`
- 48 instance variables, 54 properties, 76 instance methods, 3 class methods

## Instance variables

```
I _signatureVersion;
@"NSSet" _backgroundModes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _initialized;
B _hasViewServicesEntitlement;
B _provisioningProfileValidated;
B _uppProvisioningProfileValidated;
B _freeDeveloperProvisioningProfileValidated;
B _supportsMultiwindow;
B _restricted;
B _blocked;
B _beta;
B _requiresPersistentWiFi;
B _builtWithTSAN;
B _installing;
B _uninstalling;
B _pendingUninstall;
B _tentativeUninstall;
f _minimumBrightnessLevel;
@"LSApplicationIdentity" _applicationIdentity;
@"RBSProcessIdentity" _processIdentity;
@"NSURL" _executableURL;
@"NSURL" _bundleContainerURL;
@"NSURL" _dataContainerURL;
@"NSURL" _sandboxURL;
d _lastModifiedDate;
@"NSString" _preferenceDomain;
@"NSString" _teamIdentifier;
@"NSString" _signerIdentity;
@"NSDictionary" _environmentVariables;
@"NSString" _sdkVersion;
@"NSArray" _customMachServices;
Q _type;
@"NSArray" _requiredCapabilities;
@"NSArray" _deviceFamilies;
@"NSArray" _tags;
@"NSString" _shortVersionString;
q _interfaceOrientation;
Q _supportedInterfaceOrientations;
@"NSArray" _externalAccessoryProtocols;
q _screenTimePolicy;
q _ratingRank;
@"NSNumber" _itemID;
@"NSNumber" _purchaserDSID;
@"NSNumber" _downloaderDSID;
@"NSURL" _advertisingAttributionReportEndpoint;
@"NSString" _appIDEntitlement;
@"NSDictionary" _entitlements;
```

## Properties

```
@property (TI,R,D,N) signatureVersion;
@property (TB,R,N) isSignatureVersionSupported;
@property (TB,R,N) isSignatureVersionSupportEndingSoon;
@property (T@"_FBSCDHashCacheInfo",&) cachedCDHashInfo;
@property (TB,R,N,GwasBuiltWithTSAN,V_builtWithTSAN) builtWithTSAN;
@property (T@"NSURL",R,C,N,V_advertisingAttributionReportEndpoint) advertisingAttributionReportEndpoint;
@property (T@"NSString",R,C,N,G_appIDEntitlement,V_appIDEntitlement) appIDEntitlement;
@property (TB,N,G_isInstalling,S_setInstalling:,V_installing) installing;
@property (TB,N,G_isUninstalling,S_setUninstalling:,V_uninstalling) uninstalling;
@property (TB,N,G_isPendingUninstall,S_setPendingUninstall:,V_pendingUninstall) pendingUninstall;
@property (TB,N,G_isTentativeUninstall,S_setTentativeUninstall:,V_tentativeUninstall) tentativeUninstall;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (TQ,N,V_supportedInterfaceOrientations) supportedInterfaceOrientations;
@property (TB,R,N,GisBlocked,V_blocked) blocked;
@property (T@"LSApplicationIdentity",R,C,N,V_applicationIdentity) applicationIdentity;
@property (T@"RBSProcessIdentity",R,C,N,V_processIdentity) processIdentity;
@property (T@"NSURL",R,N,V_executableURL) executableURL;
@property (T@"NSURL",R,N,V_bundleContainerURL) bundleContainerURL;
@property (T@"NSURL",R,N,V_dataContainerURL) dataContainerURL;
@property (T@"NSURL",R,N,V_sandboxURL) sandboxURL;
@property (Td,R,N,V_lastModifiedDate) lastModifiedDate;
@property (T@"NSString",R,C,N,V_preferenceDomain) preferenceDomain;
@property (T@"NSString",R,N,V_teamIdentifier) teamIdentifier;
@property (T@"NSString",R,C,N,V_signerIdentity) signerIdentity;
@property (T@"NSDictionary",R,N,V_environmentVariables) environmentVariables;
@property (T@"NSDictionary",R,N,V_entitlements) entitlements;
@property (TB,R,N,V_hasViewServicesEntitlement) hasViewServicesEntitlement;
@property (T@"NSArray",R,N,V_tags) tags;
@property (T@"NSArray",R,N,V_customMachServices) customMachServices;
@property (TB,R,N,V_supportsMultiwindow) supportsMultiwindow;
@property (TB,R,N,GisProvisioningProfileValidated,V_provisioningProfileValidated) provisioningProfileValidated;
@property (TB,R,N,GisUPPProvisioningProfileValidated,V_uppProvisioningProfileValidated) UPPProvisioningProfileValidated;
@property (TB,R,N,GisFreeDeveloperProvisioningProfileValidated,V_freeDeveloperProvisioningProfileValidated) freeDeveloperProvisioningProfileValidated;
@property (TQ,R,N,V_type) type;
@property (TB,R,N,GisRestricted,V_restricted) restricted;
@property (T@"NSArray",R,N,V_requiredCapabilities) requiredCapabilities;
@property (T@"NSArray",R,N,V_deviceFamilies) deviceFamilies;
@property (T@"NSString",R,C,N,V_sdkVersion) sdkVersion;
@property (TB,R,N,GisBeta,V_beta) beta;
@property (T@"NSString",R,C,N,V_shortVersionString) shortVersionString;
@property (TB,R,N,GisExitsOnSuspend) exitsOnSuspend;
@property (TB,R,N,V_requiresPersistentWiFi) requiresPersistentWiFi;
@property (Tf,R,N,V_minimumBrightnessLevel) minimumBrightnessLevel;
@property (T@"NSArray",R,N,V_externalAccessoryProtocols) externalAccessoryProtocols;
@property (Tq,R,N,V_screenTimePolicy) screenTimePolicy;
@property (TB,R,N,GisBlockedForScreenTimeExpiration) blockedForScreenTimeExpiration;
@property (Tq,R,N,V_ratingRank) ratingRank;
@property (T@"NSNumber",R,N,V_itemID) itemID;
@property (T@"NSNumber",R,N,V_purchaserDSID) purchaserDSID;
@property (T@"NSNumber",R,N,V_downloaderDSID) downloaderDSID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSApplicationInfo _applicationTypeForProxy:];
+[FBSApplicationInfo _applicationTypeForRecord:];
+[FBSApplicationInfo _configureEnvironment:withInfo:isPreApex:];
```

## Instance methods

```
-[FBSApplicationInfo isRestricted];
-[FBSApplicationInfo _synchronize:];
-[FBSApplicationInfo signerIdentity];
-[FBSApplicationInfo dataContainerURL];
-[FBSApplicationInfo isBlockedForScreenTimeExpiration];
-[FBSApplicationInfo processIdentity];
-[FBSApplicationInfo interfaceOrientation];
-[FBSApplicationInfo signatureVersion];
-[FBSApplicationInfo tags];
-[FBSApplicationInfo purchaserDSID];
-[FBSApplicationInfo _loadFromProxy:];
-[FBSApplicationInfo lastModifiedDate];
-[FBSApplicationInfo succinctDescriptionBuilder];
-[FBSApplicationInfo setInterfaceOrientation:];
-[FBSApplicationInfo screenTimePolicy];
-[FBSApplicationInfo supportedInterfaceOrientations];
-[FBSApplicationInfo requiredCapabilities];
-[FBSApplicationInfo teamIdentifier];
-[FBSApplicationInfo bundleContainerURL];
-[FBSApplicationInfo environmentVariables];
-[FBSApplicationInfo downloaderDSID];
-[FBSApplicationInfo ratingRank];
-[FBSApplicationInfo type];
-[FBSApplicationInfo executableURL];
-[FBSApplicationInfo entitlements];
-[FBSApplicationInfo preferenceDomain];
-[FBSApplicationInfo isExitsOnSuspend];
-[FBSApplicationInfo isBlocked];
-[FBSApplicationInfo deviceFamilies];
-[FBSApplicationInfo shortVersionString];
-[FBSApplicationInfo sdkVersion];
-[FBSApplicationInfo initWithApplicationProxy:];
-[FBSApplicationInfo supportsMultiwindow];
-[FBSApplicationInfo itemID];
-[FBSApplicationInfo descriptionBuilderWithMultilinePrefix:];
-[FBSApplicationInfo fallbackFolderName];
-[FBSApplicationInfo folderNames];
-[FBSApplicationInfo setSupportedInterfaceOrientations:];
-[FBSApplicationInfo supportsDeviceFamily:];
-[FBSApplicationInfo externalAccessoryProtocols];
-[FBSApplicationInfo isBeta];
-[FBSApplicationInfo initWithApplicationRecord:];
-[FBSApplicationInfo sandboxURL];
-[FBSApplicationInfo _isUninstalling];
-[FBSApplicationInfo _setInstalling:];
-[FBSApplicationInfo _appIDEntitlement];
-[FBSApplicationInfo _initWithApplicationProxy:record:appIdentity:processIdentity:overrideURL:];
-[FBSApplicationInfo _initWithBundleIdentifier:url:];
-[FBSApplicationInfo _initWithBundleProxy:overrideURL:];
-[FBSApplicationInfo _isInstalling];
-[FBSApplicationInfo _isPendingUninstall];
-[FBSApplicationInfo _isTentativeUninstall];
-[FBSApplicationInfo _loadFromRecord:];
-[FBSApplicationInfo _overrideTags:];
-[FBSApplicationInfo _setPendingUninstall:];
-[FBSApplicationInfo _setTentativeUninstall:];
-[FBSApplicationInfo _setUninstalling:];
-[FBSApplicationInfo advertisingAttributionReportEndpoint];
-[FBSApplicationInfo applicationIdentity];
-[FBSApplicationInfo builtOnOrAfterSDKVersion:];
-[FBSApplicationInfo cachedCDHashInfo];
-[FBSApplicationInfo customMachServices];
-[FBSApplicationInfo hasViewServicesEntitlement];
-[FBSApplicationInfo isFreeDeveloperProvisioningProfileValidated];
-[FBSApplicationInfo isProvisioningProfileValidated];
-[FBSApplicationInfo isSignatureVersionSupportEndingSoon];
-[FBSApplicationInfo isSignatureVersionSupported];
-[FBSApplicationInfo isUPPProvisioningProfileValidated];
-[FBSApplicationInfo minimumBrightnessLevel];
-[FBSApplicationInfo requiresPersistentWiFi];
-[FBSApplicationInfo setCachedCDHashInfo:];
-[FBSApplicationInfo supportsAllInterfaceOrientations];
-[FBSApplicationInfo supportsBackgroundMode:];
-[FBSApplicationInfo supportsInterfaceOrientation:];
-[FBSApplicationInfo unauthoritativeTrustState];
-[FBSApplicationInfo wasBuiltWithTSAN];
```
