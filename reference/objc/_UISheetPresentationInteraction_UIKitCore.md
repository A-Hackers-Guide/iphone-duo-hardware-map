# `_UISheetPresentationInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 3 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIPanGestureRecognizer" __panGestureRecognizer;
@"<_UISheetPresentationInteractionDelegate>" __delegate;
@"UIView" _view;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"UIPanGestureRecognizer",&,N,S_setPanGestureRecognizer:,V__panGestureRecognizer) _panGestureRecognizer;
@property (T@"<_UISheetPresentationInteractionDelegate>",W,N,S_setDelegate:,V__delegate) _delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISheetPresentationInteraction _setDelegate:];
-[_UISheetPresentationInteraction _handlePan:];
-[_UISheetPresentationInteraction _panGestureRecognizer];
-[_UISheetPresentationInteraction setView:];
-[_UISheetPresentationInteraction _delegate];
-[_UISheetPresentationInteraction view];
-[_UISheetPresentationInteraction willMoveToView:];
-[_UISheetPresentationInteraction didMoveToView:];
-[_UISheetPresentationInteraction _setPanGestureRecognizer:];
```
