# `_UIClientToHostRelationshipGestureInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 4 instance variables, 8 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _gestureRecognizers;
@"UIView" _view;
@"NSString" _hostIdentifier;
@"<_UIAssertion>" _pointerUpdatePauseAssertion;
```

## Properties

```
@property (T@"<_UIAssertion>",&,N,V_pointerUpdatePauseAssertion) pointerUpdatePauseAssertion;
@property (T@"NSString",R,C,N,V_hostIdentifier) hostIdentifier;
@property (T@"NSArray",R,N,V_gestureRecognizers) gestureRecognizers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[_UIClientToHostRelationshipGestureInteraction _hostGestureRecognizersForFailureRelationshipsWithIdentifier:];
+[_UIClientToHostRelationshipGestureInteraction dispatchGestureRecognizerStateChange:toHostGestureWithIdentifier:];
+[_UIClientToHostRelationshipGestureInteraction hostGestureRecognizerForFailureRelationshipsWithIdentifier:];
```

## Instance methods

```
-[_UIClientToHostRelationshipGestureInteraction hostIdentifier];
-[_UIClientToHostRelationshipGestureInteraction gestureRecognizers];
-[_UIClientToHostRelationshipGestureInteraction addGestureRecognizer:];
-[_UIClientToHostRelationshipGestureInteraction _invalidatePointerPauseAssertion];
-[_UIClientToHostRelationshipGestureInteraction view];
-[_UIClientToHostRelationshipGestureInteraction setPointerUpdatePauseAssertion:];
-[_UIClientToHostRelationshipGestureInteraction gestureRecognizerShouldBegin:];
-[_UIClientToHostRelationshipGestureInteraction initWithHostIdentifier:];
-[_UIClientToHostRelationshipGestureInteraction removeGestureRecognizer:];
-[_UIClientToHostRelationshipGestureInteraction willMoveToView:];
-[_UIClientToHostRelationshipGestureInteraction pointerUpdatePauseAssertion];
-[_UIClientToHostRelationshipGestureInteraction _wrappedRecognizerDidRecognize:];
-[_UIClientToHostRelationshipGestureInteraction didMoveToView:];
```
