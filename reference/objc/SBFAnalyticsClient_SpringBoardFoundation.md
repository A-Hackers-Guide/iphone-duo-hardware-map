# `SBFAnalyticsClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"SBFAnalyticsBackend" _backend;
@"NSString" _significantTimeChangedNotificationName;
```

## Properties

```
@property (T@"NSString",C,N,V_significantTimeChangedNotificationName) significantTimeChangedNotificationName;
```

## Class methods

```
+[SBFAnalyticsClient sharedInstance];
```

## Instance methods

```
-[SBFAnalyticsClient _noteSignificantTimeChanged:];
-[SBFAnalyticsClient emitEvent:];
-[SBFAnalyticsClient emitEvent:withPayload:];
-[SBFAnalyticsClient initWithBackend:];
-[SBFAnalyticsClient registerForQueryName:handler:];
-[SBFAnalyticsClient setSignificantTimeChangedNotificationName:];
-[SBFAnalyticsClient significantTimeChangedNotificationName];
```
