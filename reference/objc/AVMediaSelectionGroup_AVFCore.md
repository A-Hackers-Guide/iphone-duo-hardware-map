# `AVMediaSelectionGroup`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 4 properties, 25 instance methods, 7 class methods

## Instance variables

```
@"AVMediaSelectionGroupInternal" _mediaSelectionGroup;
```

## Properties

```
@property (T@"NSArray",R,N) mediaSelectionOptionsWithEnhancedIntelligibilityOfSpeech;
@property (T@"NSArray",R,N) options;
@property (T@"AVMediaSelectionOption",R,N) defaultOption;
@property (TB,R,N) allowsEmptySelection;
```

## Class methods

```
+[AVMediaSelectionGroup mediaSelectionGroupWithAsset:dictionary:];
+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:];
+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withAnyMediaCharacteristicFromArray:];
+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withLocale:];
+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withMediaCharacteristics:];
+[AVMediaSelectionGroup mediaSelectionOptionsFromArray:withoutMediaCharacteristics:];
+[AVMediaSelectionGroup playableMediaSelectionOptionsFromArray:];
```

## Instance methods

```
-[AVMediaSelectionGroup _groupID];
-[AVMediaSelectionGroup mediaSelectionOptionWithPropertyList:];
-[AVMediaSelectionGroup asset];
-[AVMediaSelectionGroup _isStreamingGroup];
-[AVMediaSelectionGroup init];
-[AVMediaSelectionGroup dealloc];
-[AVMediaSelectionGroup defaultOption];
-[AVMediaSelectionGroup dictionary];
-[AVMediaSelectionGroup _weakReference];
-[AVMediaSelectionGroup _groupMediaCharacteristics];
-[AVMediaSelectionGroup description];
-[AVMediaSelectionGroup _optionWithID:displaysNonForcedSubtitles:audioCompositionPresetIndex:];
-[AVMediaSelectionGroup _localizedMediaSelectionOptionDisplayNames];
-[AVMediaSelectionGroup options];
-[AVMediaSelectionGroup mediaSelectionOptionWithPropertyListMatchToMediaSelectionArray:];
-[AVMediaSelectionGroup _groupMediaType];
-[AVMediaSelectionGroup copyWithZone:];
-[AVMediaSelectionGroup customMediaSelectionScheme];
-[AVMediaSelectionGroup currentBundleIdentifier];
-[AVMediaSelectionGroup _matchesGroupID:mediaType:];
-[AVMediaSelectionGroup _primaryMediaCharacteristic];
-[AVMediaSelectionGroup allowsEmptySelection];
-[AVMediaSelectionGroup mediaSelectionOptionComplementaryToOption:forMediaCharacteristic:];
-[AVMediaSelectionGroup mediaSelectionOptionsWithEnhancedIntelligibilityOfSpeech];
-[AVMediaSelectionGroup setCurrentBundleIdentifier:];
```
