# `_UISegmentedControlAppearanceStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _backgroundImages;
@"NSMutableDictionary" _miniBackgroundImages;
@"NSMutableDictionary" _dividerImages;
@"NSMutableDictionary" _miniDividerImages;
@"NSMutableDictionary" _textAttributesForState;
@"NSMutableDictionary" _backgroundPositionAdjustmentsForBarMetrics;
@"NSMutableDictionary" _contentPositionOffsets;
@"NSMutableDictionary" _miniContentPositionOffsets;
B _legacyDontHighlight;
B _legacySuppressOptionsBackground;
B _isTiled;
Q _leftCapWidth;
Q _rightCapWidth;
```

## Instance methods

```
-[_UISegmentedControlAppearanceStorage init];
-[_UISegmentedControlAppearanceStorage setDetail:];
-[_UISegmentedControlAppearanceStorage legacySuppressOptionsBackground];
-[_UISegmentedControlAppearanceStorage anyDividerImage];
-[_UISegmentedControlAppearanceStorage backgroundImageForState:isMini:];
-[_UISegmentedControlAppearanceStorage anyDividerImageForMini:];
-[_UISegmentedControlAppearanceStorage backgroundImageForState:isMini:withFallback:];
-[_UISegmentedControlAppearanceStorage backgroundPositionAdjustmentForBarMetrics:];
-[_UISegmentedControlAppearanceStorage contentPositionOffsetForSegment:inMiniBar:];
-[_UISegmentedControlAppearanceStorage contentPositionOffsetForSegment:inMiniBar:noFallback:];
-[_UISegmentedControlAppearanceStorage dividerImageForLeftSegmentState:rightSegmentState:isMini:];
-[_UISegmentedControlAppearanceStorage dividerImageForLeftSegmentState:rightSegmentState:isMini:withFallback:];
-[_UISegmentedControlAppearanceStorage hasAPICustomizedImages];
-[_UISegmentedControlAppearanceStorage setBackgroundImage:forState:isMini:];
-[_UISegmentedControlAppearanceStorage setBackgroundPositionAdjustment:forBarMetrics:];
-[_UISegmentedControlAppearanceStorage setContentPositionOffset:forSegment:inMiniBar:];
-[_UISegmentedControlAppearanceStorage setDividerImage:forLeftSegmentState:rightSegmentState:isMini:];
-[_UISegmentedControlAppearanceStorage setIsTiled:leftCapWidth:rightCapWidth:];
-[_UISegmentedControlAppearanceStorage setTextAttributes:forState:];
-[_UISegmentedControlAppearanceStorage takeTextAttributesFrom:forState:];
-[_UISegmentedControlAppearanceStorage textAttributesForState:];
-[_UISegmentedControlAppearanceStorage wantsTrackingSuppressed];
```
