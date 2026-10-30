# `AVMetricPlayerItemVariantSwitchEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"AVAssetVariant" _fromVariant;
@"AVAssetVariant" _toVariant;
@"AVMetricMediaRendition" _videoRendition;
@"AVMetricMediaRendition" _audioRendition;
@"AVMetricMediaRendition" _subtitleRendition;
@"NSArray" _loadedTimeRanges;
B _didSucceed;
```

## Properties

```
@property (T@"AVAssetVariant",R) fromVariant;
@property (T@"AVAssetVariant",R) toVariant;
@property (T@"NSArray",R) loadedTimeRanges;
@property (T@"AVMetricMediaRendition",R) videoRendition;
@property (T@"AVMetricMediaRendition",R) audioRendition;
@property (T@"AVMetricMediaRendition",R) subtitleRendition;
@property (TB,R) didSucceed;
```

## Class methods

```
+[AVMetricPlayerItemVariantSwitchEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlayerItemVariantSwitchEvent debugDescription];
-[AVMetricPlayerItemVariantSwitchEvent dealloc];
-[AVMetricPlayerItemVariantSwitchEvent loadedTimeRanges];
-[AVMetricPlayerItemVariantSwitchEvent encodeWithCoder:];
-[AVMetricPlayerItemVariantSwitchEvent initWithCoder:];
-[AVMetricPlayerItemVariantSwitchEvent didSucceed];
-[AVMetricPlayerItemVariantSwitchEvent audioRendition];
-[AVMetricPlayerItemVariantSwitchEvent fromVariant];
-[AVMetricPlayerItemVariantSwitchEvent initWithDate:mediaTime:sessionID:figMetricEvent:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:didSucceed:];
-[AVMetricPlayerItemVariantSwitchEvent subtitleRendition];
-[AVMetricPlayerItemVariantSwitchEvent toVariant];
-[AVMetricPlayerItemVariantSwitchEvent videoRendition];
```
