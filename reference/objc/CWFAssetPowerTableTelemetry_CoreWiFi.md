# `CWFAssetPowerTableTelemetry`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDateFormatter" _dateFormatter;
@"NSDate" _initializationDate;
@"NSString" _assetSpecifier;
B _isSupportedChipset;
@"NSString" _deviceSKU;
@"NSString" _notificationString;
@"NSString" _assetType;
@"NSString" _assetVersion;
B _assetAvailable;
@"NSString" _assetBuild;
@"NSDate" _assetCatalogLastTimeChecked;
@"NSDate" _assetCatalogPostedDate;
B _assetVersionSanity;
B _osVersionSanity;
B _osRestoreVersionSanity;
B _skuSanity;
B _assetBuildSanity;
B _transferSuccess;
B _transferAssetAlreadyHere;
B _transferPreviousAssetCleaned;
@"NSDate" _transferAvailableDate;
@"NSString" _assetVersionInfoVersion;
@"NSDate" _assetVersionInfoDate;
@"NSString" _assetVersionInfoDateString;
@"NSError" _lastError;
```

## Class methods

```
+[CWFAssetPowerTableTelemetry sharedObj];
```

## Instance methods

```
-[CWFAssetPowerTableTelemetry setAssetSpecifier:];
-[CWFAssetPowerTableTelemetry init];
-[CWFAssetPowerTableTelemetry setSKU:];
-[CWFAssetPowerTableTelemetry getNSDateFromString:];
-[CWFAssetPowerTableTelemetry sendTelemetryAndClear];
-[CWFAssetPowerTableTelemetry setAssetContentSyncResult:availableForUseAttributes:newerVersionAttributes:assetType:assetSpecifier:assetVersion:error:];
-[CWFAssetPowerTableTelemetry setAssetHandoffInfo:assetAlreadyHere:previousAssetCleanedUp:previousLatestPlist:latestPlistDict:newPlist:error:];
-[CWFAssetPowerTableTelemetry setAssetLocalInfo:assetSpecifier:assetVersion:assetBuild:lastTimeCatalogChecked:catalogPostedDate:assetVersionSanity:osVersionSanity:osRestoreVersionSanity:skuSanity:sanityCheckAssetBuildAttribute:attributes:localURL:];
-[CWFAssetPowerTableTelemetry setAssetVersionDownloadNotifcation:reason:];
-[CWFAssetPowerTableTelemetry setIsSupportedChipset:];
```
