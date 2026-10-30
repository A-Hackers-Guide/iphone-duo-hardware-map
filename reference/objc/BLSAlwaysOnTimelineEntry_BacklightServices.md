# `BLSAlwaysOnTimelineEntry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 6 instance variables, 6 properties, 19 instance methods, 2 class methods

## Instance variables

```
B _animated;
@"NSDate" _presentationTime;
q _requestedFidelity;
d _duration;
@"<NSObject><NSCopying>" _timelineIdentifier;
@"<NSObject>" _userObject;
```

## Properties

```
@property (Tq,N,V_requestedFidelity) requestedFidelity;
@property (TB,N,GisAnimated,V_animated) animated;
@property (Td,N,V_duration) duration;
@property (T@"<NSObject>",&,N,V_userObject) userObject;
@property (T@"<NSObject><NSCopying>",&,N,V_timelineIdentifier) timelineIdentifier;
@property (T@"NSDate",R,N,V_presentationTime) presentationTime;
```

## Class methods

```
+[BLSAlwaysOnTimelineEntry loggingStringForPresentationTime:];
+[BLSAlwaysOnTimelineEntry shortLoggingStringForPresentationTime:];
```

## Instance methods

```
-[BLSAlwaysOnTimelineEntry mutableCopyWithZone:];
-[BLSAlwaysOnTimelineEntry debugDescription];
-[BLSAlwaysOnTimelineEntry compare:];
-[BLSAlwaysOnTimelineEntry isAnimated];
-[BLSAlwaysOnTimelineEntry setAnimated:];
-[BLSAlwaysOnTimelineEntry duration];
-[BLSAlwaysOnTimelineEntry hash];
-[BLSAlwaysOnTimelineEntry description];
-[BLSAlwaysOnTimelineEntry setDuration:];
-[BLSAlwaysOnTimelineEntry copyWithZone:];
-[BLSAlwaysOnTimelineEntry isEqual:];
-[BLSAlwaysOnTimelineEntry presentationTime];
-[BLSAlwaysOnTimelineEntry requestedFidelity];
-[BLSAlwaysOnTimelineEntry userObject];
-[BLSAlwaysOnTimelineEntry setUserObject:];
-[BLSAlwaysOnTimelineEntry initWithPresentationTime:requestedFidelity:animated:duration:timelineIdentifier:userObject:];
-[BLSAlwaysOnTimelineEntry setRequestedFidelity:];
-[BLSAlwaysOnTimelineEntry setTimelineIdentifier:];
-[BLSAlwaysOnTimelineEntry timelineIdentifier];
```
