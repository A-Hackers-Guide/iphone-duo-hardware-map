# `BKSHIDEventDeferringReachabilityStatus`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`
- 2 instance variables, 8 properties, 12 instance methods, 2 class methods

## Instance variables

```
q _reachability;
q _deferringGraphGeneration;
```

## Properties

```
@property (Tq,R,N) reachability;
@property (TB,R,N) isReachable;
@property (TB,R,N) isReachableRespectingConstraints;
@property (Tq,R,N) deferringGraphGeneration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDeferringReachabilityStatus supportsSecureCoding];
+[BKSHIDEventDeferringReachabilityStatus new];
```

## Instance methods

```
-[BKSHIDEventDeferringReachabilityStatus isReachableRespectingConstraints];
-[BKSHIDEventDeferringReachabilityStatus initWithReachability:deferringGraphGeneration:];
-[BKSHIDEventDeferringReachabilityStatus reachability];
-[BKSHIDEventDeferringReachabilityStatus init];
-[BKSHIDEventDeferringReachabilityStatus isReachable];
-[BKSHIDEventDeferringReachabilityStatus encodeWithCoder:];
-[BKSHIDEventDeferringReachabilityStatus hash];
-[BKSHIDEventDeferringReachabilityStatus description];
-[BKSHIDEventDeferringReachabilityStatus initWithCoder:];
-[BKSHIDEventDeferringReachabilityStatus appendDescriptionToStream:];
-[BKSHIDEventDeferringReachabilityStatus deferringGraphGeneration];
-[BKSHIDEventDeferringReachabilityStatus isEqual:];
```
