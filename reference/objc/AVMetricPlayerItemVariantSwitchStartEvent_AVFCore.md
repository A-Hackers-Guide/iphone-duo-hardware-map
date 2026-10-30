# `AVMetricPlayerItemVariantSwitchStartEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"AVAssetVariant" _fromVariant;
@"AVAssetVariant" _toVariant;
@"AVMetricMediaRendition" _videoRendition;
@"AVMetricMediaRendition" _audioRendition;
@"AVMetricMediaRendition" _subtitleRendition;
@"NSArray" _loadedTimeRanges;
```

## Properties

```
@property (T@"AVAssetVariant",R) fromVariant;
@property (T@"AVAssetVariant",R) toVariant;
@property (T@"NSArray",R) loadedTimeRanges;
@property (T@"AVMetricMediaRendition",R) videoRendition;
@property (T@"AVMetricMediaRendition",R) audioRendition;
@property (T@"AVMetricMediaRendition",R) subtitleRendition;
```

## Class methods

```
+[AVMetricPlayerItemVariantSwitchStartEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlayerItemVariantSwitchStartEvent debugDescription];
-[AVMetricPlayerItemVariantSwitchStartEvent dealloc];
-[AVMetricPlayerItemVariantSwitchStartEvent loadedTimeRanges];
-[AVMetricPlayerItemVariantSwitchStartEvent encodeWithCoder:];
-[AVMetricPlayerItemVariantSwitchStartEvent initWithCoder:];
-[AVMetricPlayerItemVariantSwitchStartEvent audioRendition];
-[AVMetricPlayerItemVariantSwitchStartEvent fromVariant];
-[AVMetricPlayerItemVariantSwitchStartEvent initWithDate:mediaTime:sessionID:figMetricEvent:fromVariant:toVariant:videoRendition:audioRendition:subtitleRendition:loadedTimeRanges:];
-[AVMetricPlayerItemVariantSwitchStartEvent subtitleRendition];
-[AVMetricPlayerItemVariantSwitchStartEvent toVariant];
-[AVMetricPlayerItemVariantSwitchStartEvent videoRendition];
```
