# `UIDragInteractionContextImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionContext`, `UIDragAnimating`
- 13 instance variables, 17 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _shouldAnimateLift;
B _preparedForLift;
B _hasBegunDrag;
@"NSMutableArray" _animationBlocks;
@"NSMutableArray" _completionBlocks;
q _state;
@"NSArray" _items;
@? _animations;
@? _completion;
@? __sessionDidBegin;
q _invocationType;
@"UITouch" _initiationTouch;
{CAPoint3D="x"d"y"d"z"d} _initialLocation;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@"NSArray",&,N,V_items) items;
@property (TB,N,V_shouldAnimateLift) shouldAnimateLift;
@property (T@?,C,N,V_animations) animations;
@property (T@?,C,N,V_completion) completion;
@property (T@?,C,N,V__sessionDidBegin) _sessionDidBegin;
@property (T{CAPoint3D=ddd},N,V_initialLocation) initialLocation;
@property (TB,N,GisPreparedForLift,V_preparedForLift) preparedForLift;
@property (Tq,N,V_invocationType) invocationType;
@property (T@"UITouch",&,N,V_initiationTouch) initiationTouch;
@property (TB,N,V_hasBegunDrag) hasBegunDrag;
@property (T@"NSMutableArray",R,N,V_animationBlocks) animationBlocks;
@property (T@"NSMutableArray",R,N,V_completionBlocks) completionBlocks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDragInteractionContextImpl addAnimations:];
-[UIDragInteractionContextImpl setCompletion:];
-[UIDragInteractionContextImpl addCompletion:];
-[UIDragInteractionContextImpl shouldAnimateLift];
-[UIDragInteractionContextImpl setShouldAnimateLift:];
-[UIDragInteractionContextImpl setInitialLocation:];
-[UIDragInteractionContextImpl animations];
-[UIDragInteractionContextImpl completionBlocks];
-[UIDragInteractionContextImpl completion];
-[UIDragInteractionContextImpl setState:];
-[UIDragInteractionContextImpl setPreparedForLift:];
-[UIDragInteractionContextImpl initialLocation];
-[UIDragInteractionContextImpl setItems:];
-[UIDragInteractionContextImpl invocationType];
-[UIDragInteractionContextImpl setAnimations:];
-[UIDragInteractionContextImpl items];
-[UIDragInteractionContextImpl isPreparedForLift];
-[UIDragInteractionContextImpl animationBlocks];
-[UIDragInteractionContextImpl setInitiationTouch:];
-[UIDragInteractionContextImpl _sessionDidBegin];
-[UIDragInteractionContextImpl initiationTouch];
-[UIDragInteractionContextImpl setHasBegunDrag:];
-[UIDragInteractionContextImpl set_sessionDidBegin:];
-[UIDragInteractionContextImpl setInvocationType:];
-[UIDragInteractionContextImpl hasBegunDrag];
-[UIDragInteractionContextImpl state];
```
