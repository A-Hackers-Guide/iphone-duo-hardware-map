# `UITextTouchObservingInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"UILongPressGestureRecognizer" _longPressGesture;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"UILongPressGestureRecognizer",&,N,V_longPressGesture) longPressGesture;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextTouchObservingInteraction _removeGestureRecognizers];
-[UITextTouchObservingInteraction setView:];
-[UITextTouchObservingInteraction _addGestureRecognizers];
-[UITextTouchObservingInteraction view];
-[UITextTouchObservingInteraction willMoveToView:];
-[UITextTouchObservingInteraction _createGestureRecognizersIfNecessary];
-[UITextTouchObservingInteraction didMoveToView:];
-[UITextTouchObservingInteraction longPressGesture];
-[UITextTouchObservingInteraction longPressObserved:];
-[UITextTouchObservingInteraction setLongPressGesture:];
```
