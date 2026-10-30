# `AVMetricEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _date;
{?="value"q"timescale"i"flags"I"epoch"q} _mediaTime;
@"NSString" _sessionID;
^{OpaqueFigMetricEvent=} _figMetricEvent;
@"NSObject<OS_xpc_object>" _serializedEvent;
```

## Properties

```
@property (T@"NSDate",R) date;
@property (T{?=qiIq},R) mediaTime;
@property (T@"NSString",R) sessionID;
```

## Class methods

```
+[AVMetricEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricEvent sessionID];
-[AVMetricEvent debugDescription];
-[AVMetricEvent dealloc];
-[AVMetricEvent date];
-[AVMetricEvent encodeWithCoder:];
-[AVMetricEvent initWithCoder:];
-[AVMetricEvent serializedEvent];
-[AVMetricEvent debugDescriptionForAttr];
-[AVMetricEvent initWithDate:mediaTime:sessionID:figMetricEvent:];
-[AVMetricEvent mediaTime];
```
