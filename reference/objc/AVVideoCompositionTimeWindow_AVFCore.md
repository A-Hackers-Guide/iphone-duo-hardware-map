# `AVVideoCompositionTimeWindow`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _durationBefore;
{?="value"q"timescale"i"flags"I"epoch"q} _durationAfter;
{?="value"q"timescale"i"flags"I"epoch"q} _durationBeforeWhenSeeking;
{?="value"q"timescale"i"flags"I"epoch"q} _durationAfterWhenSeeking;
```

## Properties

```
@property (T{?=qiIq},R,N,V_durationBefore) durationBefore;
@property (T{?=qiIq},R,N,V_durationAfter) durationAfter;
@property (T{?=qiIq},R,N,V_durationBeforeWhenSeeking) durationBeforeWhenSeeking;
@property (T{?=qiIq},R,N,V_durationAfterWhenSeeking) durationAfterWhenSeeking;
```

## Instance methods

```
-[AVVideoCompositionTimeWindow hash];
-[AVVideoCompositionTimeWindow description];
-[AVVideoCompositionTimeWindow copyWithZone:];
-[AVVideoCompositionTimeWindow isEqual:];
-[AVVideoCompositionTimeWindow durationAfter];
-[AVVideoCompositionTimeWindow durationAfterWhenSeeking];
-[AVVideoCompositionTimeWindow durationBefore];
-[AVVideoCompositionTimeWindow durationBeforeWhenSeeking];
-[AVVideoCompositionTimeWindow initWithDurationBefore:durationAfter:];
-[AVVideoCompositionTimeWindow initWithDurationBefore:durationAfter:durationBeforeWhenSeeking:durationAfterWhenSeeking:];
```
