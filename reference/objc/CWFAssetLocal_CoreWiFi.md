# `CWFAssetLocal`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 18 instance methods, 9 class methods

## Instance variables

```
@"NSString" _assetType;
@"NSString" _assetSpecifier;
@"NSString" _assetVersion;
@"NSString" _firstSupportedOS;
@"NSString" _lastSupportedOS;
@"NSString" _firstSupportedBuild;
@"NSString" _lastSupportedBuild;
@"NSURL" _localURL;
@"NSString" _assetID;
@"NSString" _assetBuild;
@"NSDate" _lastTimeCatalogChecked;
@"NSDate" _catalogPostedDate;
```

## Properties

```
@property (T@"NSString",R,N,V_assetType) assetType;
@property (T@"NSString",R,N,V_assetSpecifier) assetSpecifier;
@property (T@"NSString",R,N,V_assetVersion) assetVersion;
@property (T@"NSString",R,N,V_firstSupportedOS) firstSupportedOS;
@property (T@"NSString",R,N,V_lastSupportedOS) lastSupportedOS;
@property (T@"NSString",R,N,V_firstSupportedBuild) firstSupportedBuild;
@property (T@"NSString",R,N,V_lastSupportedBuild) lastSupportedBuild;
@property (T@"NSURL",R,N,V_localURL) localURL;
@property (T@"NSString",R,N,V_assetID) assetID;
@property (T@"NSString",R,N,V_assetBuild) assetBuild;
@property (T@"NSDate",R,N,V_lastTimeCatalogChecked) lastTimeCatalogChecked;
@property (T@"NSDate",R,N,V_catalogPostedDate) catalogPostedDate;
```

## Class methods

```
+[CWFAssetLocal assetIDFromLocalURL:];
+[CWFAssetLocal compareAssetVersion:withVersion:];
+[CWFAssetLocal compareOSRestoreVersion:withVersion:];
+[CWFAssetLocal compareOSVersion:withVersion:];
+[CWFAssetLocal compareSUCoreRestoreVersion:withVersion:];
+[CWFAssetLocal isValidAssetVersion:];
+[CWFAssetLocal isValidOSVersion:];
+[CWFAssetLocal isValidRestoreOSVersion:];
+[CWFAssetLocal restoreOSVersionFromOSVersion:];
```

## Instance methods

```
-[CWFAssetLocal assetType];
-[CWFAssetLocal assetVersion];
-[CWFAssetLocal assetSpecifier];
-[CWFAssetLocal localURL];
-[CWFAssetLocal catalogPostedDate];
-[CWFAssetLocal assetBuild];
-[CWFAssetLocal assetID];
-[CWFAssetLocal lastSupportedOS];
-[CWFAssetLocal sanityCheckAssetBuildAttribute:];
-[CWFAssetLocal firstSupportedBuild];
-[CWFAssetLocal firstSupportedOS];
-[CWFAssetLocal getCoreWiFiCatalogDataFromMobileAssetFile:];
-[CWFAssetLocal initWithAssetType:assetSpecifier:assetVersion:attributes:rootCatalogInfo:localURL:];
-[CWFAssetLocal lastSupportedBuild];
-[CWFAssetLocal lastTimeCatalogChecked];
-[CWFAssetLocal sanityCheckOSRestoreVersion:];
-[CWFAssetLocal sanityCheckOSVersion:];
-[CWFAssetLocal sanityCheckSKUVersion:];
```
