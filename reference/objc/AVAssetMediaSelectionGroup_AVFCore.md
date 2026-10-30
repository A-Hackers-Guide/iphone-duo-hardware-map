# `AVAssetMediaSelectionGroup`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMediaSelectionGroup`
- 8 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"AVAsset" _asset;
@"NSDictionary" _dictionary;
@"NSArray" _groupMediaCharacteristics;
@"NSDictionary" _localizedMediaSelectionOptionDisplayNames;
@"AVCustomMediaSelectionScheme" _customMediaSelectionScheme;
@"NSArray" _options;
@"AVMediaSelectionOption" _defaultOption;
B _isStreamingGroup;
```

## Instance methods

```
-[AVAssetMediaSelectionGroup mediaSelectionOptionWithPropertyList:];
-[AVAssetMediaSelectionGroup asset];
-[AVAssetMediaSelectionGroup _isStreamingGroup];
-[AVAssetMediaSelectionGroup init];
-[AVAssetMediaSelectionGroup dealloc];
-[AVAssetMediaSelectionGroup defaultOption];
-[AVAssetMediaSelectionGroup dictionary];
-[AVAssetMediaSelectionGroup _optionWithID:identifier:source:displaysNonForcedSubtitles:audioCompositionPresetIndex:];
-[AVAssetMediaSelectionGroup _groupMediaCharacteristics];
-[AVAssetMediaSelectionGroup initWithAsset:dictionary:];
-[AVAssetMediaSelectionGroup hash];
-[AVAssetMediaSelectionGroup _optionWithID:displaysNonForcedSubtitles:audioCompositionPresetIndex:];
-[AVAssetMediaSelectionGroup _localizedMediaSelectionOptionDisplayNames];
-[AVAssetMediaSelectionGroup options];
-[AVAssetMediaSelectionGroup mediaSelectionOptionWithPropertyListMatchToMediaSelectionArray:];
-[AVAssetMediaSelectionGroup isEqual:];
-[AVAssetMediaSelectionGroup _mediaSelectionOptionWithPropertyList:matchToMediaSelectionArray:];
-[AVAssetMediaSelectionGroup customMediaSelectionScheme];
```
