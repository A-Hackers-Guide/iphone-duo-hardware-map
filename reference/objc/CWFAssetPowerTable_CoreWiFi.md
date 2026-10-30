# `CWFAssetPowerTable`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 13 instance methods, 17 class methods

## Instance variables

```
Q numberOfCallsToCopyAsset;
Q numberOfTimesAssetExisted;
Q numberOfSuccessfullAssetCopy;
B _allowTestingOnUnSupportedChipset;
@"NSString" _powerTableAPIMajorVersion;
@"CWFAssetPowerTableElector" __elector;
```

## Properties

```
@property (TB,N,V_allowTestingOnUnSupportedChipset) allowTestingOnUnSupportedChipset;
@property (T@"CWFAssetPowerTableElector",&,N,V__elector) _elector;
@property (T@"NSString",C,N,V_powerTableAPIMajorVersion) powerTableAPIMajorVersion;
```

## Class methods

```
+[CWFAssetPowerTable isSupportedDeviceClass];
+[CWFAssetPowerTable currentLatestAssetVersion];
+[CWFAssetPowerTable currentLatestPowerTableAssemblyDate];
+[CWFAssetPowerTable currentLatestPowerTableAssemblyDateFromPT:];
+[CWFAssetPowerTable currentLatestPowerTableVersion];
+[CWFAssetPowerTable currentLatestPowerTableVersionFromPT:];
+[CWFAssetPowerTable currentLatestPowerTableVersionInfoDict];
+[CWFAssetPowerTable getDeviceSKU];
+[CWFAssetPowerTable getPowerTableAssemblyDateFromDict:];
+[CWFAssetPowerTable getPowerTableVersionFromDict:];
+[CWFAssetPowerTable getPowerTableVersionInfoDict:];
+[CWFAssetPowerTable isChipsetDownloadOnly];
+[CWFAssetPowerTable isChipsetFullySupported];
+[CWFAssetPowerTable isSupportedOTAPTDownloadOnly];
+[CWFAssetPowerTable isSupportedOTAPTUpdate];
+[CWFAssetPowerTable sharedObj];
+[CWFAssetPowerTable shouldAllowTestingOnUnSupportedChipset];
```

## Instance methods

```
-[CWFAssetPowerTable init];
-[CWFAssetPowerTable description];
-[CWFAssetPowerTable _elector];
-[CWFAssetPowerTable allowTestingOnUnSupportedChipset];
-[CWFAssetPowerTable assetSpecifierToTrack];
-[CWFAssetPowerTable createTopLevelDir];
-[CWFAssetPowerTable garbageCollectWithNewAsset:prevAsset:];
-[CWFAssetPowerTable powerTableAPIMajorVersion];
-[CWFAssetPowerTable processLocalAsset:];
-[CWFAssetPowerTable setAllowTestingOnUnSupportedChipset:];
-[CWFAssetPowerTable setPowerTableAPIMajorVersion:];
-[CWFAssetPowerTable set_elector:];
-[CWFAssetPowerTable transferAssetFromSrc:toDst:withAsseID:withVersion:assetBuild:firstSupportedOS:lastSupportedOS:firstSupportedBuild:lastSupportedBuild:ptVersionInfo:lastTimeCatalogChecked:catalogPostedDate:];
```
