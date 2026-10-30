# `UILargeContentViewerInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIAccessibilityHUDGestureDelegateInternal`, `UIInteraction`
- 2 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"UIView" _view;
@"<UILargeContentViewerInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"<UILargeContentViewerInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIGestureRecognizer",R,N) gestureRecognizerForExclusionRelationship;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N) view;
```

## Class methods

```
+[UILargeContentViewerInteraction initialize];
+[UILargeContentViewerInteraction isEnabled];
```

## Instance methods

```
-[UILargeContentViewerInteraction _accessibilityHUDGestureManager:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UILargeContentViewerInteraction initWithDelegate:];
-[UILargeContentViewerInteraction _accessibilityHUDGestureManager:HUDItemForPoint:];
-[UILargeContentViewerInteraction _accessibilityHUDGestureManager:gestureLiftedAtPoint:];
-[UILargeContentViewerInteraction gestureRecognizerForExclusionRelationship];
-[UILargeContentViewerInteraction init];
-[UILargeContentViewerInteraction view];
-[UILargeContentViewerInteraction _itemAtPoint:];
-[UILargeContentViewerInteraction _viewControllerForAccessibilityHUDGestureManager:];
-[UILargeContentViewerInteraction willMoveToView:];
-[UILargeContentViewerInteraction delegate];
-[UILargeContentViewerInteraction didMoveToView:];
```
