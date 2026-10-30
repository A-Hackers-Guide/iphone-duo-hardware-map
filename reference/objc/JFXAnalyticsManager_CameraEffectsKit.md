# `JFXAnalyticsManager`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXAnalytics`
- 0 instance variables, 4 properties, 8 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[JFXAnalyticsManager sharedInstance];
+[JFXAnalyticsManager allIncrementScalarEvents];
+[JFXAnalyticsManager bundleForAnalytics];
```

## Instance methods

```
-[JFXAnalyticsManager init];
-[JFXAnalyticsManager checkIfEventExistsWithName:];
-[JFXAnalyticsManager dictionaryWithEventName:value:];
-[JFXAnalyticsManager fullKeyFromEvent:];
-[JFXAnalyticsManager isIncrementScalar:];
-[JFXAnalyticsManager trackEventWithName:];
-[JFXAnalyticsManager trackKey:withCount:];
-[JFXAnalyticsManager trackKey:withPayload:];
```
