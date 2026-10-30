# `VTAssetManager`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"VTPolicy" _enablePolicy;
```

## Class methods

```
+[VTAssetManager sharedInstance];
```

## Instance methods

```
-[VTAssetManager init];
-[VTAssetManager _updateFromRemoteToLocalAssets:];
-[VTAssetManager _addKeyValuePairForQuery:];
-[VTAssetManager _assetQueryForLanguage:supportPremium:];
-[VTAssetManager _defaultDownloadOptions];
-[VTAssetManager _downloadAsset:withComplete:];
-[VTAssetManager _fetchRemoteAssetForLanguage:supportPremium:];
-[VTAssetManager _fetchRemoteMetaData];
-[VTAssetManager _filteredAssetsForAssets:language:supportPremium:];
-[VTAssetManager _findLatestInstalledAsset:];
-[VTAssetManager _installedAssetForLanguage:supportPremium:];
-[VTAssetManager _installedAssetWithoutMetaDataForLanguage:supportPremium:];
-[VTAssetManager _isReadyToUse];
-[VTAssetManager _runAssetQuery:completion:];
-[VTAssetManager _startDownloadingVoiceTriggerAsset:progress:completion:];
-[VTAssetManager assetForLanguage:];
-[VTAssetManager installedAssetForLanguage:];
```
