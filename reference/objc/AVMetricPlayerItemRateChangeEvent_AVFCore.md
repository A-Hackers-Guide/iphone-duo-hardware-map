# `AVMetricPlayerItemRateChangeEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
d _rate;
d _previousRate;
@"AVAssetVariant" _variant;
```

## Properties

```
@property (Td,R) rate;
@property (Td,R) previousRate;
@property (T@"AVAssetVariant",R) variant;
```

## Class methods

```
+[AVMetricPlayerItemRateChangeEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlayerItemRateChangeEvent rate];
-[AVMetricPlayerItemRateChangeEvent debugDescription];
-[AVMetricPlayerItemRateChangeEvent dealloc];
-[AVMetricPlayerItemRateChangeEvent encodeWithCoder:];
-[AVMetricPlayerItemRateChangeEvent initWithCoder:];
-[AVMetricPlayerItemRateChangeEvent variant];
-[AVMetricPlayerItemRateChangeEvent debugDescriptionForAttr];
-[AVMetricPlayerItemRateChangeEvent initWithDate:mediaTime:sessionID:figMetricEvent:variant:rate:previousRate:];
-[AVMetricPlayerItemRateChangeEvent previousRate];
```
