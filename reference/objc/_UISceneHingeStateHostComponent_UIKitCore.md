# `_UISceneHingeStateHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UISceneRelationshipManagementHostComponentObserver`, `_UISceneHingeStateClientObserver`, `FBSceneComponent`, `_UISceneHingeStateHost`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
{?="hasUpdatedSceneHingeState"b1"hasUpdatedDeprecatedHingeState"b1"hasRegisteredForParentChanges"b1} _flags;
@"<BSInvalidatable>" _stateCaptureToken;
@"_UISceneHingeState" _heldSceneHingeState;
d _heldHingeAngle;
d _heldNextHingeStatusProgress;
q _heldHingeStatus;
q _heldMagicPose;
q _heldNextHingeStatus;
@"_UISceneHingeStateClientComponent" _observedParentClientComponent;
@"<BSInvalidatable>" _parentObservationToken;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UISceneHingeState",C,N) sceneHingeState;
@property (Tq,N) magicPose;
@property (Tq,N) status;
@property (Tq,N) nextStatus;
@property (Td,N) progress;
@property (Td,N) hingeAngle;
```

## Instance methods

```
-[_UISceneHingeStateHostComponent debugDescription];
-[_UISceneHingeStateHostComponent setProgress:];
-[_UISceneHingeStateHostComponent hingeAngle];
-[_UISceneHingeStateHostComponent setScene:];
-[_UISceneHingeStateHostComponent setHingeAngle:];
-[_UISceneHingeStateHostComponent status];
-[_UISceneHingeStateHostComponent progress];
-[_UISceneHingeStateHostComponent succinctDescription];
-[_UISceneHingeStateHostComponent invalidate];
-[_UISceneHingeStateHostComponent _scene:isMovingToParent:];
-[_UISceneHingeStateHostComponent description];
-[_UISceneHingeStateHostComponent appendDescriptionToStream:];
-[_UISceneHingeStateHostComponent setStatus:];
-[_UISceneHingeStateHostComponent scene:didUpdateClientSettings:];
-[_UISceneHingeStateHostComponent sceneHingeState];
-[_UISceneHingeStateHostComponent magicPose];
-[_UISceneHingeStateHostComponent nextStatus];
-[_UISceneHingeStateHostComponent sceneHingeStateClientComponent:didUpdateFromHingeState:toHingeState:];
-[_UISceneHingeStateHostComponent setMagicPose:];
-[_UISceneHingeStateHostComponent setNextStatus:];
-[_UISceneHingeStateHostComponent setSceneHingeState:];
```
