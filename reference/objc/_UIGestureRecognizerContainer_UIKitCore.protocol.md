# `_UIGestureRecognizerContainer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) gestureRecognizers;
@property (T@"<_UIGestureRecognizerContainer>",R,N) _parentGestureRecognizerContainer;
@property (T@"NSArray",R,N) _childGestureRecognizerContainers;
@property (T@"<_UIGestureRecognizerContainer>",R,N) _actingParentGestureRecognizerContainer;
@property (T@"UIWindow",R,N) _eventReceivingWindow;
@property (T@"UIView",R,N) _proxyView;
```

## Instance methods

```
-[_UIGestureRecognizerContainer gestureRecognizers];
-[_UIGestureRecognizerContainer addGestureRecognizer:];
-[_UIGestureRecognizerContainer _compareGestureRecognizerContainer:];
-[_UIGestureRecognizerContainer _proxyView];
-[_UIGestureRecognizerContainer _parentGestureRecognizerContainer];
-[_UIGestureRecognizerContainer removeGestureRecognizer:];
-[_UIGestureRecognizerContainer _eventReceivingWindow];
-[_UIGestureRecognizerContainer _actingParentGestureRecognizerContainer];
-[_UIGestureRecognizerContainer _childGestureRecognizerContainers];
```
