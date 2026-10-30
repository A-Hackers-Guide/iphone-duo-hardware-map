# `_UIFeedbackGeneratorGestureRecognizerCompletedTouch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFeedbackGeneratorGestureRecognizerTouch`
- 6 instance variables, 10 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _pointerTouch;
q _type;
Q _senderID;
Q _pointerSenderID;
@"UIWindow" _window;
{CGPoint="x"d"y"d} _locationInWindow;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (TQ,R,N,G_senderID,V_senderID) senderID;
@property (TB,R,N,G_isPointerTouch,V_pointerTouch) pointerTouch;
@property (TQ,R,N,G_pointerSenderID,V_pointerSenderID) pointerSenderID;
@property (T{CGPoint=dd},N,V_locationInWindow) locationInWindow;
@property (T@"UIWindow",R,W,N,V_window) window;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFeedbackGeneratorGestureRecognizerCompletedTouch completedTouchFromTouch:];
```

## Instance methods

```
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch setLocationInWindow:];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch window];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch locationInView:];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch type];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch locationInWindow];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch _isPointerTouch];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch _pointerSenderID];
-[_UIFeedbackGeneratorGestureRecognizerCompletedTouch _senderID];
```
