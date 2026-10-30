# `_UIEditMenuContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIEditMenuDismissalGestureRecognizerDelegate`, `_UITouchFallbackViewDelegate`
- 7 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _lastHitTestPassedThrough;
B _didDismissFromGesture;
B _ignoresPassthroughInPresentationSource;
B _dismissesOnViewportResize;
@"_UITouchFallbackView" _touchFallbackView;
@"_UIEditMenuPresentation" _presentation;
@"_UIEditMenuDismissalGestureRecognizer" _dismissalGestureRecognizer;
```

## Properties

```
@property (T@"_UIEditMenuDismissalGestureRecognizer",R,N,V_dismissalGestureRecognizer) dismissalGestureRecognizer;
@property (T@"_UITouchFallbackView",R,N,V_touchFallbackView) touchFallbackView;
@property (T@"_UIEditMenuPresentation",R,W,N,V_presentation) presentation;
@property (TB,N,V_ignoresPassthroughInPresentationSource) ignoresPassthroughInPresentationSource;
@property (TB,N,V_dismissesOnViewportResize) dismissesOnViewportResize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIEditMenuContainerView didRecognizeDismissalGestureRecognizer:];
-[_UIEditMenuContainerView didMoveToWindow];
-[_UIEditMenuContainerView setDismissesOnViewportResize:];
-[_UIEditMenuContainerView presentation];
-[_UIEditMenuContainerView initWithPresentation:enablePassthrough:];
-[_UIEditMenuContainerView hitTest:withEvent:];
-[_UIEditMenuContainerView touchFallbackView];
-[_UIEditMenuContainerView setBounds:];
-[_UIEditMenuContainerView _installDismissalGesture];
-[_UIEditMenuContainerView willMoveToWindow:];
-[_UIEditMenuContainerView _dismissMenuPresentationForSizeChange];
-[_UIEditMenuContainerView setIgnoresPassthroughInPresentationSource:];
-[_UIEditMenuContainerView dismissalGestureRecognizer];
-[_UIEditMenuContainerView setFrame:];
-[_UIEditMenuContainerView ignoresPassthroughInPresentationSource];
-[_UIEditMenuContainerView dismissesOnViewportResize];
-[_UIEditMenuContainerView dismissalGestureRecognizer:shouldInteractAtLocation:withEvent:];
-[_UIEditMenuContainerView touchFallbackView:shouldHitTestAtLocation:withEvent:];
-[_UIEditMenuContainerView _sceneRegionsDidChange];
```
