# `BLSHCancelWhenBacklightInactivatesAttributeEntry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSValidWhenBacklightInactiveAttributeEntry`
- Protocols: `BLSBacklightStateObserving`
- 3 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BLSBacklight" _backlight;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_active;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHCancelWhenBacklightInactivatesAttributeEntry backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHCancelWhenBacklightInactivatesAttributeEntry invalidate];
-[BLSHCancelWhenBacklightInactivatesAttributeEntry initForAttribute:fromAssertion:forService:attributeHandler:];
-[BLSHCancelWhenBacklightInactivatesAttributeEntry reactivateIfPossible];
```
