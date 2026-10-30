# `SBBannerPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- 5 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _wantsCancelsTouchesInView;
B _clientWantsCancelsTouchesInView;
@"<SBBannerPanGestureSystemDragCancellingDelegate>" _systemDragCancellingDelegate;
@"SBWindowScene" _windowScene;
@"NSMutableSet" _identifiersForTouchesDisablingTouchCancellation;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V_identifiersForTouchesDisablingTouchCancellation) identifiersForTouchesDisablingTouchCancellation;
@property (TB,N,V_clientWantsCancelsTouchesInView) clientWantsCancelsTouchesInView;
@property (T@"<SBBannerPanGestureSystemDragCancellingDelegate>",W,N,V_systemDragCancellingDelegate) systemDragCancellingDelegate;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
```

## Instance methods

```
-[SBBannerPanGestureRecognizer setCancelsTouchesInView:];
-[SBBannerPanGestureRecognizer touchesEnded:withEvent:];
-[SBBannerPanGestureRecognizer _shouldReceiveTouch:withEvent:];
-[SBBannerPanGestureRecognizer identifiersForTouchesDisablingTouchCancellation];
-[SBBannerPanGestureRecognizer setWindowScene:];
-[SBBannerPanGestureRecognizer setState:];
-[SBBannerPanGestureRecognizer touchesCancelled:withEvent:];
-[SBBannerPanGestureRecognizer setSystemDragCancellingDelegate:];
-[SBBannerPanGestureRecognizer _removeTouchDisablingTouchCancellation:];
-[SBBannerPanGestureRecognizer touchesBegan:withEvent:];
-[SBBannerPanGestureRecognizer initWithTarget:action:];
-[SBBannerPanGestureRecognizer _removeTouchesDisablingTouchCancellation:];
-[SBBannerPanGestureRecognizer setEnabled:];
-[SBBannerPanGestureRecognizer _actuallySetCancelsTouchesInView:];
-[SBBannerPanGestureRecognizer setClientWantsCancelsTouchesInView:];
-[SBBannerPanGestureRecognizer windowScene];
-[SBBannerPanGestureRecognizer clientWantsCancelsTouchesInView];
-[SBBannerPanGestureRecognizer systemDragCancellingDelegate];
-[SBBannerPanGestureRecognizer _addTouchDisablingTouchCancellation:];
-[SBBannerPanGestureRecognizer _updateCancelsTouchesInView];
```
