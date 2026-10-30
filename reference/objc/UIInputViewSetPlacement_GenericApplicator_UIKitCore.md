# `UIInputViewSetPlacement_GenericApplicator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInputViewSetPlacementApplicator`
- 5 instance variables, 13 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSLayoutConstraint" _horizontalConstraint;
@"NSLayoutConstraint" _verticalConstraint;
@"NSLayoutConstraint" _widthConstraint;
@"<UIInputViewSetPlacementOwner>" _owner;
B _isInteractiveStateTransition;
```

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInputViewSetPlacement_GenericApplicator applicatorForOwner:withPlacement:];
```

## Instance methods

```
-[UIInputViewSetPlacement_GenericApplicator draggableView];
-[UIInputViewSetPlacement_GenericApplicator applyChanges:];
-[UIInputViewSetPlacement_GenericApplicator updateForInteractiveTransitionStart:];
-[UIInputViewSetPlacement_GenericApplicator constraints];
-[UIInputViewSetPlacement_GenericApplicator checkVerticalConstraint];
-[UIInputViewSetPlacement_GenericApplicator origin];
-[UIInputViewSetPlacement_GenericApplicator popoverFrame];
-[UIInputViewSetPlacement_GenericApplicator allConstraintsActive];
-[UIInputViewSetPlacement_GenericApplicator preBeginGesture:shouldBegin:];
-[UIInputViewSetPlacement_GenericApplicator twoFingerDraggableView];
-[UIInputViewSetPlacement_GenericApplicator resetConstantsIfNeeded];
-[UIInputViewSetPlacement_GenericApplicator inputAssistantPadding];
-[UIInputViewSetPlacement_GenericApplicator initForOwner:withPlacement:];
-[UIInputViewSetPlacement_GenericApplicator targetRect];
-[UIInputViewSetPlacement_GenericApplicator invalidate];
-[UIInputViewSetPlacement_GenericApplicator prepare];
-[UIInputViewSetPlacement_GenericApplicator isGesture:inDraggableView:];
-[UIInputViewSetPlacement_GenericApplicator contentInsets];
-[UIInputViewSetPlacement_GenericApplicator description];
-[UIInputViewSetPlacement_GenericApplicator backdropContainer];
-[UIInputViewSetPlacement_GenericApplicator updateForOffset:];
-[UIInputViewSetPlacement_GenericApplicator inputAccessoryPadding];
-[UIInputViewSetPlacement_GenericApplicator isEqual:];
```
