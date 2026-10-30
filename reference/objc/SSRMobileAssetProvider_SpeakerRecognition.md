# `SSRMobileAssetProvider`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SSRAssetProviding`
- 0 instance variables, 4 properties, 20 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SSRMobileAssetProvider _findLatestInstalledAsset:];
-[SSRMobileAssetProvider installedSpeakerRecognitionAssetForLanguage:];
-[SSRMobileAssetProvider _getVoiceTriggerAssetTypeString];
-[SSRMobileAssetProvider _buildAssetQueryForAssetType:];
-[SSRMobileAssetProvider _filteredAssets:forLanguage:];
-[SSRMobileAssetProvider _getEndpointAssetCurrentCompatibilityVersion];
-[SSRMobileAssetProvider _getEndpointAssetTypeString];
-[SSRMobileAssetProvider _getSSRAssetCurrentCompatibilityVersion];
-[SSRMobileAssetProvider _getSSRAssetTypeString];
-[SSRMobileAssetProvider _getVTRepromptListAssetTypeString];
-[SSRMobileAssetProvider _getVTRepromptListCurrentCompatibilityVersion];
-[SSRMobileAssetProvider _getVoiceTriggerAssetCurrentCompatibilityVersion];
-[SSRMobileAssetProvider _installedMobileAssetOfType:forLanguage:];
-[SSRMobileAssetProvider _installedMobileAssetOfType:forLanguage:ofType:];
-[SSRMobileAssetProvider _queryMAAssetsForAssetType:Language:];
-[SSRMobileAssetProvider _shouldUseHPMarshSSRAsset];
-[SSRMobileAssetProvider allInstalledAssetsOfType:forLanguage:];
-[SSRMobileAssetProvider allInstalledSpeakerRecognitionAssetForLanguage:];
-[SSRMobileAssetProvider getAssetProviderType];
-[SSRMobileAssetProvider installedAssetOfType:forLanguageCode:];
```
