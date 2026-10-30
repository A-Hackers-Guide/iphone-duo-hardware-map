# `_UIRemoteKeyboardsEventObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIEventObserver`
- 4 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _touchTracker;
B _keyboardIsVisible;
B _hasTextInputResponder;
@"<_UIRemoteKeyboardsEventObserverDelegate>" _delegate;
```

## Properties

```
@property (TB,N,V_hasTextInputResponder) hasTextInputResponder;
@property (T@"<_UIRemoteKeyboardsEventObserverDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_keyboardIsVisible) keyboardIsVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIRemoteKeyboardsEventObserver _preferredEventSourceForTouch:tracking:shouldUpdateOut:];
-[_UIRemoteKeyboardsEventObserver peekApplicationEvent:];
-[_UIRemoteKeyboardsEventObserver _gestureRecognizer:didTransitionToState:];
-[_UIRemoteKeyboardsEventObserver _updateTrackingForTouch:];
-[_UIRemoteKeyboardsEventObserver init];
-[_UIRemoteKeyboardsEventObserver dealloc];
-[_UIRemoteKeyboardsEventObserver setKeyboardIsVisible:];
-[_UIRemoteKeyboardsEventObserver _cancelTrackingForTouch:];
-[_UIRemoteKeyboardsEventObserver _endTrackingForTouch:];
-[_UIRemoteKeyboardsEventObserver setDelegate:];
-[_UIRemoteKeyboardsEventObserver _isTrackingPencilTouch];
-[_UIRemoteKeyboardsEventObserver _trackTouch:];
-[_UIRemoteKeyboardsEventObserver _hasTextAlternativesForTouch:];
-[_UIRemoteKeyboardsEventObserver delegate];
-[_UIRemoteKeyboardsEventObserver _invalidateTrackingForTouch:];
-[_UIRemoteKeyboardsEventObserver _markTrackingForTouch:withGesture:];
-[_UIRemoteKeyboardsEventObserver _shouldTrackTouch:];
-[_UIRemoteKeyboardsEventObserver setHasTextInputResponder:];
-[_UIRemoteKeyboardsEventObserver keyboardIsVisible];
-[_UIRemoteKeyboardsEventObserver textInputResponderDidChange:];
-[_UIRemoteKeyboardsEventObserver _startTrackingForTouch:];
-[_UIRemoteKeyboardsEventObserver hasTextInputResponder];
```
