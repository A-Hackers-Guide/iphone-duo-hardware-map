# `_UIWindowSceneDragInteractionImpl_iOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowSceneDragInteractionImpl`
- 6 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"_UIClientToHostRelationshipGestureInteraction" _clientRelationshipInteraction;
@"_UIDoubleTapInteraction" _doubleTapInteraction;
@"UIPanGestureRecognizer" _directTouchPanGestureRecognizer;
@"UIPanGestureRecognizer" _pointerTouchPanGestureRecognizer;
@"_UIRelationshipGestureRecognizer" _failureRelationshipGestureRecognizer;
```

## Properties

```
@property (T@"_UIClientToHostRelationshipGestureInteraction",&,N,V_clientRelationshipInteraction) clientRelationshipInteraction;
@property (T@"_UIDoubleTapInteraction",&,N,V_doubleTapInteraction) doubleTapInteraction;
@property (T@"UIPanGestureRecognizer",&,N,V_directTouchPanGestureRecognizer) directTouchPanGestureRecognizer;
@property (T@"UIPanGestureRecognizer",&,N,V_pointerTouchPanGestureRecognizer) pointerTouchPanGestureRecognizer;
@property (T@"_UIRelationshipGestureRecognizer",&,N,V_failureRelationshipGestureRecognizer) failureRelationshipGestureRecognizer;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIWindowSceneDragInteractionImpl_iOS _makeDraggingPanGestureRecognizer];
-[_UIWindowSceneDragInteractionImpl_iOS init];
-[_UIWindowSceneDragInteractionImpl_iOS updateForEnhancedWindowingEnablementChange:];
-[_UIWindowSceneDragInteractionImpl_iOS _didRecognizePanGesture:];
-[_UIWindowSceneDragInteractionImpl_iOS failureRelationshipGestureRecognizer];
-[_UIWindowSceneDragInteractionImpl_iOS doubleTapInteraction];
-[_UIWindowSceneDragInteractionImpl_iOS gestureForFailureRelationships];
-[_UIWindowSceneDragInteractionImpl_iOS pointerTouchPanGestureRecognizer];
-[_UIWindowSceneDragInteractionImpl_iOS setFailureRelationshipGestureRecognizer:];
-[_UIWindowSceneDragInteractionImpl_iOS view];
-[_UIWindowSceneDragInteractionImpl_iOS willMoveToView:];
-[_UIWindowSceneDragInteractionImpl_iOS setClientRelationshipInteraction:];
-[_UIWindowSceneDragInteractionImpl_iOS updateForEnhancedWindowingEnabled:];
-[_UIWindowSceneDragInteractionImpl_iOS directTouchPanGestureRecognizer];
-[_UIWindowSceneDragInteractionImpl_iOS setDirectTouchPanGestureRecognizer:];
-[_UIWindowSceneDragInteractionImpl_iOS setDoubleTapInteraction:];
-[_UIWindowSceneDragInteractionImpl_iOS setPointerTouchPanGestureRecognizer:];
-[_UIWindowSceneDragInteractionImpl_iOS clientRelationshipInteraction];
-[_UIWindowSceneDragInteractionImpl_iOS didMoveToView:];
```
