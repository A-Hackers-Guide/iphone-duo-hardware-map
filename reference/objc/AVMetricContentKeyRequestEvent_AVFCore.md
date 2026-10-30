# `AVMetricContentKeyRequestEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"AVContentKeySpecifier" _contentKeySpecifier;
@"NSString" _mediaType;
B _isClientInitiated;
@"AVMetricMediaResourceRequestEvent" _mediaResourceRequestEvent;
```

## Properties

```
@property (T@"AVContentKeySpecifier",R) contentKeySpecifier;
@property (T@"NSString",R) mediaType;
@property (TB,R) isClientInitiated;
@property (T@"AVMetricMediaResourceRequestEvent",R) mediaResourceRequestEvent;
```

## Class methods

```
+[AVMetricContentKeyRequestEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricContentKeyRequestEvent debugDescription];
-[AVMetricContentKeyRequestEvent dealloc];
-[AVMetricContentKeyRequestEvent encodeWithCoder:];
-[AVMetricContentKeyRequestEvent initWithCoder:];
-[AVMetricContentKeyRequestEvent mediaType];
-[AVMetricContentKeyRequestEvent contentKeySpecifier];
-[AVMetricContentKeyRequestEvent initWithDate:mediaTime:sessionID:figMetricEvent:contentKeySpecifier:mediaType:isClientInitiated:mediaResourceRequestEvent:];
-[AVMetricContentKeyRequestEvent isClientInitiated];
-[AVMetricContentKeyRequestEvent mediaResourceRequestEvent];
```
