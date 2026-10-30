# `AVAssetTrackSegment`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
{?="source"{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}}"target"{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}}} _timeMapping;
```

## Properties

```
@property (T{?={?={?=qiIq}{?=qiIq}}{?={?=qiIq}{?=qiIq}}},R,N,V_timeMapping) timeMapping;
@property (TB,R,N,GisEmpty) empty;
```

## Class methods

```
+[AVAssetTrackSegment supportsSecureCoding];
```

## Instance methods

```
-[AVAssetTrackSegment init];
-[AVAssetTrackSegment isEmpty];
-[AVAssetTrackSegment encodeWithCoder:];
-[AVAssetTrackSegment hash];
-[AVAssetTrackSegment description];
-[AVAssetTrackSegment initWithCoder:];
-[AVAssetTrackSegment isEqual:];
-[AVAssetTrackSegment _initWithTimeMapping:];
-[AVAssetTrackSegment timeMapping];
```
