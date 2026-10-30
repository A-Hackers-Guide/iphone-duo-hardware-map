# `AVComposition`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAsset`
- Protocols: `NSSecureCoding`, `NSMutableCopying`
- 1 instance variables, 3 properties, 29 instance methods, 3 class methods

## Instance variables

```
@"AVCompositionInternal" _priv;
```

## Properties

```
@property (T@"NSArray",R,N) tracks;
@property (T{CGSize=dd},R,N) naturalSize;
@property (T@"NSDictionary",R,C,N) URLAssetInitializationOptions;
```

## Class methods

```
+[AVComposition supportsSecureCoding];
+[AVComposition initialize];
+[AVComposition expectsPropertyRevisedNotifications];
```

## Instance methods

```
-[AVComposition tracksWithMediaCharacteristic:];
-[AVComposition tracksWithMediaType:];
-[AVComposition mutableCopyWithZone:];
-[AVComposition _mediaSelectionGroupDictionaries];
-[AVComposition init];
-[AVComposition naturalSize];
-[AVComposition _initWithComposition:];
-[AVComposition dealloc];
-[AVComposition _classForTrackInspectors];
-[AVComposition isDefunct];
-[AVComposition trackWithTrackID:];
-[AVComposition encodeWithCoder:];
-[AVComposition _authoredMediaSelectionGroupDictionaries];
-[AVComposition _figAsset];
-[AVComposition description];
-[AVComposition initWithCoder:];
-[AVComposition tracks];
-[AVComposition _copyFormatReader];
-[AVComposition _newTrackForIndex:];
-[AVComposition _assetInspector];
-[AVComposition URLAssetInitializationOptions];
-[AVComposition _assetInspectorLoader];
-[AVComposition _clientProvidesNaturalSize];
-[AVComposition _createEmptyMutableCompositionIfNeeded];
-[AVComposition _loadAssetInspectorAndLoaderOnce];
-[AVComposition _mutableComposition];
-[AVComposition _mutableTracks];
-[AVComposition _setNaturalSize:];
-[AVComposition _setURLAssetInitializationOptions:error:];
```
