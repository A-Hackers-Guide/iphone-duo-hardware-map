# `_UIHingeState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _status;
q _magicPose;
d _hingeAngle;
q _nextStatus;
d _progress;
```

## Properties

```
@property (Tq,R,N,V_status) status;
@property (Tq,R,N,V_magicPose) magicPose;
@property (Td,R,N,V_hingeAngle) hingeAngle;
@property (Tq,R,N,V_nextStatus) nextStatus;
@property (Td,R,N,V_progress) progress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHingeState debugDescription];
-[_UIHingeState init];
-[_UIHingeState hingeAngle];
-[_UIHingeState status];
-[_UIHingeState progress];
-[_UIHingeState succinctDescription];
-[_UIHingeState hash];
-[_UIHingeState description];
-[_UIHingeState appendDescriptionToStream:];
-[_UIHingeState isEqual:];
-[_UIHingeState magicPose];
-[_UIHingeState nextStatus];
```
