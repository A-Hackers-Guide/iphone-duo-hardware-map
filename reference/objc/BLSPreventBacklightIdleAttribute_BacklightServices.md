# `BLSPreventBacklightIdleAttribute`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSAttribute`
- Protocols: `BSXPCCoding`
- 2 instance variables, 6 properties, 12 instance methods, 4 class methods

## Instance variables

```
B _restartTimerOnInvalidation;
B _clearUserInteraction;
```

## Properties

```
@property (TB,R,N,V_restartTimerOnInvalidation) restartTimerOnInvalidation;
@property (TB,R,N,V_clearUserInteraction) clearUserInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSPreventBacklightIdleAttribute supportsSecureCoding];
+[BLSPreventBacklightIdleAttribute preventIdle];
+[BLSPreventBacklightIdleAttribute preventIdleAndRestartTimerOnInvalidation];
+[BLSPreventBacklightIdleAttribute preventIdleClearUserInteractionAndRestartTimerOnInvalidation];
```

## Instance methods

```
-[BLSPreventBacklightIdleAttribute initWithXPCDictionary:];
-[BLSPreventBacklightIdleAttribute encodeWithXPCDictionary:];
-[BLSPreventBacklightIdleAttribute encodeWithCoder:];
-[BLSPreventBacklightIdleAttribute hash];
-[BLSPreventBacklightIdleAttribute description];
-[BLSPreventBacklightIdleAttribute initWithCoder:];
-[BLSPreventBacklightIdleAttribute copyWithZone:];
-[BLSPreventBacklightIdleAttribute isEqual:];
-[BLSPreventBacklightIdleAttribute checkEntitlementSourceForRequiredEntitlements:error:];
-[BLSPreventBacklightIdleAttribute clearUserInteraction];
-[BLSPreventBacklightIdleAttribute restartTimerOnInvalidation];
-[BLSPreventBacklightIdleAttribute initWithRestartTimerOnInvalidation:clearUserInteraction:];
```
