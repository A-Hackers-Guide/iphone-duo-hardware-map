# `CAMAnalyticsEvent`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 6 instance methods, 5 class methods

## Instance variables

```
@"NSString" _uuid;
@"NSMutableDictionary" __eventMap;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__eventMap) _eventMap;
@property (T@"NSString",R,N,V_uuid) uuid;
@property (T@"NSString",R,N) eventName;
```

## Class methods

```
+[CAMAnalyticsEvent durationRangeStringForDuration:];
+[CAMAnalyticsEvent bucketedGigabytesStringForBytes:];
+[CAMAnalyticsEvent bucketedGigabytesStringForBytes:allowZero:minPositiveValue:maxValue:];
+[CAMAnalyticsEvent bucketedPowerOf2ForValue:allowZero:minPositiveValue:maxValue:];
+[CAMAnalyticsEvent gigabytesForBytes:];
```

## Instance methods

```
-[CAMAnalyticsEvent publish];
-[CAMAnalyticsEvent initWithEvent:];
-[CAMAnalyticsEvent uuid];
-[CAMAnalyticsEvent init];
-[CAMAnalyticsEvent eventName];
-[CAMAnalyticsEvent _eventMap];
```
