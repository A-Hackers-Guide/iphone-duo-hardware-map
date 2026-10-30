# `AVDataAsset`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAsset`
- 4 instance variables, 0 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _initializationOptions;
@"AVAssetInspectorLoader" _loader;
@"AVDispatchOnce" _allocateTracksOnceOnly;
@"NSArray" _tracks;
```

## Class methods

```
+[AVDataAsset _dataLengthLimit];
+[AVDataAsset _getFigAssetCreationOptionsFromDataAssetInitializationOptions:figAssetCreationFlags:];
```

## Instance methods

```
-[AVDataAsset dealloc];
-[AVDataAsset _classForTrackInspectors];
-[AVDataAsset tracks];
-[AVDataAsset _copyFormatReader];
-[AVDataAsset initWithData:contentType:];
-[AVDataAsset _assetInspector];
-[AVDataAsset _assetInspectorLoader];
-[AVDataAsset _requiresInProcessOperation];
-[AVDataAsset initWithData:contentType:options:];
-[AVDataAsset referenceRestrictions];
```
