# `AVSampleBufferRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"AVSampleBufferRequestInternal" _request;
```

## Properties

```
@property (T@"AVSampleCursor",R,&,N) startCursor;
@property (Tq,N) direction;
@property (T@"AVSampleCursor",&,N) limitCursor;
@property (Tq,N) preferredMinSampleCount;
@property (Tq,N) maxSampleCount;
@property (Tq,N) mode;
@property (T{?=qiIq},N) overrideTime;
```

## Class methods

```
+[AVSampleBufferRequest sampleBufferRequestWithStartCursor:];
```

## Instance methods

```
-[AVSampleBufferRequest init];
-[AVSampleBufferRequest dealloc];
-[AVSampleBufferRequest setDirection:];
-[AVSampleBufferRequest setMode:];
-[AVSampleBufferRequest direction];
-[AVSampleBufferRequest mode];
-[AVSampleBufferRequest setLimitCursor:];
-[AVSampleBufferRequest _figSampleGeneratorReadFlags];
-[AVSampleBufferRequest _figSampleGeneratorReadPolicy];
-[AVSampleBufferRequest initWithStartCursor:];
-[AVSampleBufferRequest limitCursor];
-[AVSampleBufferRequest maxSampleCount];
-[AVSampleBufferRequest overrideTime];
-[AVSampleBufferRequest preferredMinSampleCount];
-[AVSampleBufferRequest setMaxSampleCount:];
-[AVSampleBufferRequest setOverrideTime:];
-[AVSampleBufferRequest setPreferredMinSampleCount:];
-[AVSampleBufferRequest startCursor];
```
