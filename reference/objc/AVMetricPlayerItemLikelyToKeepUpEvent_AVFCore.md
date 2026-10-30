# `AVMetricPlayerItemLikelyToKeepUpEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"AVAssetVariant" _variant;
d _timeTaken;
@"NSArray" _loadedTimeRanges;
```

## Properties

```
@property (T@"AVAssetVariant",R) variant;
@property (Td,R) timeTaken;
@property (T@"NSArray",R) loadedTimeRanges;
```

## Class methods

```
+[AVMetricPlayerItemLikelyToKeepUpEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlayerItemLikelyToKeepUpEvent debugDescription];
-[AVMetricPlayerItemLikelyToKeepUpEvent dealloc];
-[AVMetricPlayerItemLikelyToKeepUpEvent loadedTimeRanges];
-[AVMetricPlayerItemLikelyToKeepUpEvent encodeWithCoder:];
-[AVMetricPlayerItemLikelyToKeepUpEvent initWithCoder:];
-[AVMetricPlayerItemLikelyToKeepUpEvent variant];
-[AVMetricPlayerItemLikelyToKeepUpEvent debugDescriptionForAttr];
-[AVMetricPlayerItemLikelyToKeepUpEvent initWithDate:mediaTime:sessionID:figMetricEvent:variant:timeTaken:loadedTimeRanges:];
-[AVMetricPlayerItemLikelyToKeepUpEvent timeTaken];
```
