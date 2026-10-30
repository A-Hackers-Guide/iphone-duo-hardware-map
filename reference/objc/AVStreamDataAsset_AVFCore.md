# `AVStreamDataAsset`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAsset`
- 6 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"AVStreamDataParser" _weakReferenceToParser;
@"AVStreamDataAssetInspector" _inspector;
@"AVAssetSynchronousInspectorLoader" _inspectorLoader;
@"AVDispatchOnce" _tracksOnce;
@"NSArray" _tracks;
@"NSDictionary" _trackDictsByTrackID;
```

## Instance methods

```
-[AVStreamDataAsset dealloc];
-[AVStreamDataAsset _classForTrackInspectors];
-[AVStreamDataAsset tracks];
-[AVStreamDataAsset _copyFormatReader];
-[AVStreamDataAsset parser];
-[AVStreamDataAsset _assetInspector];
-[AVStreamDataAsset _assetInspectorLoader];
-[AVStreamDataAsset copyAssetRemovingTrackID:];
-[AVStreamDataAsset copyAssetWithAdditionalTrackID:mediaType:languageCode:transportStreamPID:];
-[AVStreamDataAsset copyAssetWithReplacementFormatDescription:forTrackID:];
-[AVStreamDataAsset formatDescriptionsForTrackID:];
-[AVStreamDataAsset initWithParser:tracks:];
-[AVStreamDataAsset languageCodeForTrackID:];
-[AVStreamDataAsset mediaTypeForTrackID:];
-[AVStreamDataAsset transportStreamPIDForTrackID:];
```
