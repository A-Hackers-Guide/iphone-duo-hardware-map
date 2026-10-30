# `AVMetricErrorEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _didRecover;
@"NSError" _error;
```

## Properties

```
@property (TB,R) didRecover;
@property (T@"NSError",R) error;
```

## Class methods

```
+[AVMetricErrorEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricErrorEvent debugDescription];
-[AVMetricErrorEvent dealloc];
-[AVMetricErrorEvent error];
-[AVMetricErrorEvent encodeWithCoder:];
-[AVMetricErrorEvent initWithCoder:];
-[AVMetricErrorEvent didRecover];
-[AVMetricErrorEvent initWithDate:mediaTime:sessionID:figMetricEvent:didRecover:error:];
```
