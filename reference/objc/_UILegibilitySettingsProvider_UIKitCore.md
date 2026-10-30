# `_UILegibilitySettingsProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 31 instance methods, 2 class methods

## Instance variables

```
B _hasContrast;
B _accumulatorIsPrimed;
d _mostRecentSaturation;
d _accumulatedSaturation;
d _mostRecentBrightness;
d _accumulatedBrightness;
@"UIColor" _contentColor;
d _mostRecentContrast;
d _accumulatedContrast;
d _mostRecentLuminance;
d _accumulatedLuminance;
d _nextChangeBarrier;
q _currentStyle;
```

## Properties

```
@property (T@"UIColor",&,N,V_contentColor) contentColor;
@property (Td,N,V_mostRecentBrightness) mostRecentBrightness;
@property (Td,N,V_accumulatedBrightness) accumulatedBrightness;
@property (Td,N,V_mostRecentContrast) mostRecentContrast;
@property (Td,N,V_accumulatedContrast) accumulatedContrast;
@property (Td,N,V_mostRecentLuminance) mostRecentLuminance;
@property (Td,N,V_accumulatedLuminance) accumulatedLuminance;
@property (Td,N,V_mostRecentSaturation) mostRecentSaturation;
@property (Td,N,V_accumulatedSaturation) accumulatedSaturation;
@property (TB,N,V_hasContrast) hasContrast;
@property (TB,N,V_accumulatorIsPrimed) accumulatorIsPrimed;
@property (Td,N,V_nextChangeBarrier) nextChangeBarrier;
@property (Tq,N,V_currentStyle) currentStyle;
```

## Class methods

```
+[_UILegibilitySettingsProvider styleForContentColor:];
+[_UILegibilitySettingsProvider styleForContentColor:contrast:];
```

## Instance methods

```
-[_UILegibilitySettingsProvider currentStyle];
-[_UILegibilitySettingsProvider setAccumulatorIsPrimed:];
-[_UILegibilitySettingsProvider setContentColor:];
-[_UILegibilitySettingsProvider mostRecentContrast];
-[_UILegibilitySettingsProvider settings];
-[_UILegibilitySettingsProvider setAccumulatedLuminance:];
-[_UILegibilitySettingsProvider mostRecentSaturation];
-[_UILegibilitySettingsProvider dealloc];
-[_UILegibilitySettingsProvider hasContrast];
-[_UILegibilitySettingsProvider mostRecentBrightness];
-[_UILegibilitySettingsProvider setMostRecentLuminance:];
-[_UILegibilitySettingsProvider setAccumulatedSaturation:];
-[_UILegibilitySettingsProvider contentColor];
-[_UILegibilitySettingsProvider setCurrentStyle:];
-[_UILegibilitySettingsProvider accumulatedContrast];
-[_UILegibilitySettingsProvider nextChangeBarrier];
-[_UILegibilitySettingsProvider mostRecentLuminance];
-[_UILegibilitySettingsProvider accumulateChangesToContentColor:contrast:];
-[_UILegibilitySettingsProvider setHasContrast:];
-[_UILegibilitySettingsProvider setMostRecentContrast:];
-[_UILegibilitySettingsProvider accumulatedSaturation];
-[_UILegibilitySettingsProvider setAccumulatedContrast:];
-[_UILegibilitySettingsProvider accumulatedLuminance];
-[_UILegibilitySettingsProvider setNextChangeBarrier:];
-[_UILegibilitySettingsProvider setMostRecentSaturation:];
-[_UILegibilitySettingsProvider setMostRecentBrightness:];
-[_UILegibilitySettingsProvider accumulateChangesToContentColor:];
-[_UILegibilitySettingsProvider accumulatedBrightness];
-[_UILegibilitySettingsProvider clearContentColorAccumulator];
-[_UILegibilitySettingsProvider setAccumulatedBrightness:];
-[_UILegibilitySettingsProvider accumulatorIsPrimed];
```
