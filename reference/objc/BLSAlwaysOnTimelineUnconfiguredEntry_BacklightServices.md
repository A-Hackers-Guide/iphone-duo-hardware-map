# `BLSAlwaysOnTimelineUnconfiguredEntry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSAlwaysOnTimelineEntry`
- 0 instance variables, 5 properties, 1 instance methods, 4 class methods

## Properties

```
@property (Tq,D,N) requestedFidelity;
@property (T@"<NSObject><NSCopying>",&,D,N) timelineIdentifier;
@property (TB,D,N,GisAnimated) animated;
@property (Td,D,N) duration;
@property (T@"<NSObject>",&,D,N) userObject;
```

## Class methods

```
+[BLSAlwaysOnTimelineUnconfiguredEntry entryForPresentationTime:withRequestedFidelity:];
+[BLSAlwaysOnTimelineUnconfiguredEntry entryForPresentationTime:withRequestedFidelity:animated:userObject:];
+[BLSAlwaysOnTimelineUnconfiguredEntry entryForPresentationTime:];
+[BLSAlwaysOnTimelineUnconfiguredEntry entryForPresentationTime:animated:userObject:];
```

## Instance methods

```
-[BLSAlwaysOnTimelineUnconfiguredEntry initWithPresentationTime:requestedFidelity:animated:duration:timelineIdentifier:userObject:];
```
