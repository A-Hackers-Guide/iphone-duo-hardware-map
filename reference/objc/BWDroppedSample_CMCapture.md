# `BWDroppedSample`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSString" _reason;
{?="value"q"timescale"i"flags"I"epoch"q} _pts;
@"NSArray" _backPressureSemaphoresToIgnore;
B _didReportPreviewFrameDrop;
```

## Properties

```
@property (T@"NSString",R) reason;
@property (T{?=qiIq},R) pts;
@property (T@"NSArray",R) backPressureSemaphoresToIgnore;
@property (TB,R) originatedFromISP;
```

## Class methods

```
+[BWDroppedSample newDroppedSampleWithReason:pts:];
+[BWDroppedSample newDroppedSampleFromDroppedSample:backPressureSemaphoresToIgnore:];
+[BWDroppedSample newDroppedSampleWithReason:pts:backPressureSemaphoresToIgnore:];
```

## Instance methods

```
-[BWDroppedSample pts];
-[BWDroppedSample dealloc];
-[BWDroppedSample description];
-[BWDroppedSample reason];
-[BWDroppedSample backPressureSemaphoresToIgnore];
-[BWDroppedSample originatedFromISP];
-[BWDroppedSample reportPreviewFrameDropIfNeeded];
```
