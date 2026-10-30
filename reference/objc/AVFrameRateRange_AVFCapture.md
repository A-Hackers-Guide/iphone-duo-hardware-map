# `AVFrameRateRange`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"AVFrameRateRangeInternal" _internal;
```

## Properties

```
@property (Td,R) minFrameRate;
@property (Td,R) maxFrameRate;
@property (T{?=qiIq},R) maxFrameDuration;
@property (T{?=qiIq},R) minFrameDuration;
```

## Class methods

```
+[AVFrameRateRange initialize];
+[AVFrameRateRange frameRateRangeWithMinRate:maxFrameRate:];
```

## Instance methods

```
-[AVFrameRateRange minFrameRate];
-[AVFrameRateRange maxFrameRate];
-[AVFrameRateRange minFrameDuration];
-[AVFrameRateRange dealloc];
-[AVFrameRateRange description];
-[AVFrameRateRange isEqual:];
-[AVFrameRateRange maxFrameDuration];
-[AVFrameRateRange includesFrameDuration:];
-[AVFrameRateRange includesFrameRate:];
-[AVFrameRateRange initWithMinFrameRate:maxFrameRate:];
```
