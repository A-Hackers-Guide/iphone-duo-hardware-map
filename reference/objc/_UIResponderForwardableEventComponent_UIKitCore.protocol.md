# `_UIResponderForwardableEventComponent` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UIEventComponent`
- 0 instance variables, 3 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"UIResponder<_UIGestureRecognizerContainer>",&,N,S_setResponder:) _responder;
@property (T@"UIWindow",R,N) window;
@property (T@"NSArray",R,N) gestureRecognizers;
```

## Instance methods

```
-[_UIResponderForwardableEventComponent gestureRecognizers];
-[_UIResponderForwardableEventComponent _isAbandoningForwardingRecord];
-[_UIResponderForwardableEventComponent _responder];
-[_UIResponderForwardableEventComponent _abandonForwardingRecord];
-[_UIResponderForwardableEventComponent window];
-[_UIResponderForwardableEventComponent _mutableForwardingRecord];
-[_UIResponderForwardableEventComponent _setResponder:];
-[_UIResponderForwardableEventComponent _forwardingRecord];
-[_UIResponderForwardableEventComponent _responderSelectorForPhase:];
-[_UIResponderForwardableEventComponent _wantsForwardingFromResponder:toNextResponder:withEvent:];
```
