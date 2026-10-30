# `BKSHIDTouchRoutingPolicy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 10 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"BSMutableSettings" _settings;
```

## Properties

```
@property (T@"BSMutableSettings",&,N,V_settings) settings;
@property (T@"NSArray",C,N) targetsToAlwaysSendTouches;
@property (T@"NSArray",C,N) restrictHitTestToTheseTargets;
@property (T@"NSArray",C,N) targetsToExcludeFromHitTesting;
@property (T@"NSArray",C,N) contextIDsToAlwaysSendTouches;
@property (T@"NSArray",C,N) restrictHitTestToTheseContextIDs;
@property (T@"NSArray",C,N) contextIDsToExcludeFromHitTesting;
@property (TB,N,GshouldAvoidHitTesting) avoidHitTesting;
@property (TB,N) restrictedHitTestsAllowEmbeddedTargets;
@property (TB,N,GshouldAvoidCancelingContinuingClients) avoidCancelingContinuingClients;
```

## Class methods

```
+[BKSHIDTouchRoutingPolicy supportsSecureCoding];
+[BKSHIDTouchRoutingPolicy inspectChangesWithOldPolicy:newPolicy:usingBlock:];
```

## Instance methods

```
-[BKSHIDTouchRoutingPolicy setSettings:];
-[BKSHIDTouchRoutingPolicy init];
-[BKSHIDTouchRoutingPolicy settings];
-[BKSHIDTouchRoutingPolicy encodeWithCoder:];
-[BKSHIDTouchRoutingPolicy hash];
-[BKSHIDTouchRoutingPolicy initWithCoder:];
-[BKSHIDTouchRoutingPolicy copyWithZone:];
-[BKSHIDTouchRoutingPolicy isEqual:];
-[BKSHIDTouchRoutingPolicy contextIDsToExcludeFromHitTesting];
-[BKSHIDTouchRoutingPolicy setContextIDsToExcludeFromHitTesting:];
-[BKSHIDTouchRoutingPolicy _initWithSettings:];
-[BKSHIDTouchRoutingPolicy contextIDsToAlwaysSendTouches];
-[BKSHIDTouchRoutingPolicy restrictHitTestToTheseContextIDs];
-[BKSHIDTouchRoutingPolicy restrictHitTestToTheseTargets];
-[BKSHIDTouchRoutingPolicy restrictedHitTestsAllowEmbeddedTargets];
-[BKSHIDTouchRoutingPolicy setAvoidCancelingContinuingClients:];
-[BKSHIDTouchRoutingPolicy setAvoidHitTesting:];
-[BKSHIDTouchRoutingPolicy setContextIDsToAlwaysSendTouches:];
-[BKSHIDTouchRoutingPolicy setRestrictHitTestToTheseContextIDs:];
-[BKSHIDTouchRoutingPolicy setRestrictHitTestToTheseTargets:];
-[BKSHIDTouchRoutingPolicy setRestrictedHitTestsAllowEmbeddedTargets:];
-[BKSHIDTouchRoutingPolicy setTargetsToAlwaysSendTouches:];
-[BKSHIDTouchRoutingPolicy setTargetsToExcludeFromHitTesting:];
-[BKSHIDTouchRoutingPolicy shouldAvoidCancelingContinuingClients];
-[BKSHIDTouchRoutingPolicy shouldAvoidHitTesting];
-[BKSHIDTouchRoutingPolicy targetsToAlwaysSendTouches];
-[BKSHIDTouchRoutingPolicy targetsToExcludeFromHitTesting];
```
