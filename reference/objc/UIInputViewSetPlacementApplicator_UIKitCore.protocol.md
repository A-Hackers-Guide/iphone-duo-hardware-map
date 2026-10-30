# `UIInputViewSetPlacementApplicator` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 17 instance methods, 1 class methods

## Properties

```
@property (T{CGPoint=dd},R) origin;
@property (T@"NSArray",R) constraints;
@property (T@"UIView",R) draggableView;
@property (T@"UIView",R) twoFingerDraggableView;
@property (T@"UIView",R) backdropContainer;
@property (T{UIEdgeInsets=dddd},R) contentInsets;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R) popoverFrame;
@property (T{UIEdgeInsets=dddd},R) inputAssistantPadding;
@property (T{UIEdgeInsets=dddd},R) inputAccessoryPadding;
```

## Class methods

```
+[UIInputViewSetPlacementApplicator applicatorForOwner:withPlacement:];
```

## Instance methods

```
-[UIInputViewSetPlacementApplicator draggableView];
-[UIInputViewSetPlacementApplicator applyChanges:];
-[UIInputViewSetPlacementApplicator updateForInteractiveTransitionStart:];
-[UIInputViewSetPlacementApplicator constraints];
-[UIInputViewSetPlacementApplicator origin];
-[UIInputViewSetPlacementApplicator popoverFrame];
-[UIInputViewSetPlacementApplicator allConstraintsActive];
-[UIInputViewSetPlacementApplicator preBeginGesture:shouldBegin:];
-[UIInputViewSetPlacementApplicator twoFingerDraggableView];
-[UIInputViewSetPlacementApplicator inputAssistantPadding];
-[UIInputViewSetPlacementApplicator invalidate];
-[UIInputViewSetPlacementApplicator prepare];
-[UIInputViewSetPlacementApplicator isGesture:inDraggableView:];
-[UIInputViewSetPlacementApplicator contentInsets];
-[UIInputViewSetPlacementApplicator backdropContainer];
-[UIInputViewSetPlacementApplicator updateForOffset:];
-[UIInputViewSetPlacementApplicator inputAccessoryPadding];
```
