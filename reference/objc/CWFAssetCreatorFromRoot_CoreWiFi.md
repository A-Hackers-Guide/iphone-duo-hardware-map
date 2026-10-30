# `CWFAssetCreatorFromRoot`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _availableForUse;
@"NSDictionary" _infoPlist;
@"NSDate" _creationDate;
@"NSDictionary" _rootCatalogInfo;
@"NSURL" _localContentURL;
@"NSString" _AssetSpecifier;
@"NSString" _AssetVersion;
@"NSDateFormatter" _formatter;
```

## Properties

```
@property (T@"NSDateFormatter",&,N,V_formatter) formatter;
@property (T@"NSDictionary",&,N,V_infoPlist) infoPlist;
@property (T@"NSDate",&,N,V_creationDate) creationDate;
@property (T@"NSDictionary",&,N,V_rootCatalogInfo) rootCatalogInfo;
@property (T@"NSURL",&,N,V_localContentURL) localContentURL;
@property (TB,N,V_availableForUse) availableForUse;
@property (T@"NSString",&,N,V_AssetSpecifier) AssetSpecifier;
@property (T@"NSString",&,N,V_AssetVersion) AssetVersion;
```

## Instance methods

```
-[CWFAssetCreatorFromRoot localContentURL];
-[CWFAssetCreatorFromRoot formatter];
-[CWFAssetCreatorFromRoot setAssetSpecifier:];
-[CWFAssetCreatorFromRoot setFormatter:];
-[CWFAssetCreatorFromRoot newerVersionAttributes];
-[CWFAssetCreatorFromRoot setAssetVersion:];
-[CWFAssetCreatorFromRoot creationDate];
-[CWFAssetCreatorFromRoot setCreationDate:];
-[CWFAssetCreatorFromRoot setLocalContentURL:];
-[CWFAssetCreatorFromRoot availableForUseAttributes];
-[CWFAssetCreatorFromRoot initWithPaths:];
-[CWFAssetCreatorFromRoot infoPlist];
-[CWFAssetCreatorFromRoot AssetSpecifier];
-[CWFAssetCreatorFromRoot AssetVersion];
-[CWFAssetCreatorFromRoot setInfoPlist:];
-[CWFAssetCreatorFromRoot availableForUse];
-[CWFAssetCreatorFromRoot loadTopLevelInfoPlistFromPaths:];
-[CWFAssetCreatorFromRoot rootCatalogInfo];
-[CWFAssetCreatorFromRoot setAvailableForUse:];
-[CWFAssetCreatorFromRoot setRootCatalogInfo:];
```
