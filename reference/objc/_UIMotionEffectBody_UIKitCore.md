# `_UIMotionEffectBody`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMBodyIdentifiable`, `CMUUIDBodyIdentifiable`, `CMViewBodyIdentifiable`
- 4 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _motionBodyID;
d _interfaceAngle;
@"CMBodyToken" _bodyToken;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bodyTokenLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",R,&,N,V_motionBodyID) _motionBodyID;
@property (Td,R,N,V_interfaceAngle) _interfaceAngle;
```

## Instance methods

```
-[_UIMotionEffectBody _interfaceAngle];
-[_UIMotionEffectBody _motionBodyID];
-[_UIMotionEffectBody _startUpdatingBodyToken:];
-[_UIMotionEffectBody _stopUpdatingBodyToken:];
-[_UIMotionEffectBody updateMotionBodyID:interfaceAngle:];
```
