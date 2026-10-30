# `UIKeyboardTouchInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 16 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _touchHistory;
Q _processedTouchCount;
@"UIKBTree" _key;
@"UIKBTree" _keyplane;
@"UIKBTree" _slidOffKey;
{CGPoint="x"d"y"d} _initialPoint;
{CGPoint="x"d"y"d} _initialDragPoint;
B _dragged;
i _stage;
i _fingerID;
B _maySuppressUpAction;
i _initialKeyState;
q _continuousPathState;
B _delayed;
B _didPlayKeyFeedback;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_touchHistory) touchHistory;
@property (T@"UIKBTouchState",R,N) touch;
@property (TQ,N,V_processedTouchCount) processedTouchCount;
@property (T@"UIKBTree",&,N,V_key) key;
@property (T@"UIKBTree",&,N,V_keyplane) keyplane;
@property (T@"UIKBTree",&,N,V_slidOffKey) slidOffKey;
@property (T{CGPoint=dd},N,V_initialPoint) initialPoint;
@property (T{CGPoint=dd},N,V_initialDragPoint) initialDragPoint;
@property (TB,N,V_dragged) dragged;
@property (Ti,N,V_stage) stage;
@property (Ti,N,V_fingerID) fingerID;
@property (TB,N,V_maySuppressUpAction) maySuppressUpAction;
@property (Ti,N,V_initialKeyState) initialKeyState;
@property (Tq,N,V_continuousPathState) continuousPathState;
@property (TB,N,V_delayed) delayed;
@property (TB,N,V_didPlayKeyFeedback) didPlayKeyFeedback;
```

## Instance methods

```
-[UIKeyboardTouchInfo initialPoint];
-[UIKeyboardTouchInfo setKeyplane:];
-[UIKeyboardTouchInfo keyplane];
-[UIKeyboardTouchInfo touchHistory];
-[UIKeyboardTouchInfo touch];
-[UIKeyboardTouchInfo delayed];
-[UIKeyboardTouchInfo setMaySuppressUpAction:];
-[UIKeyboardTouchInfo setProcessedTouchCount:];
-[UIKeyboardTouchInfo setInitialDragPoint:];
-[UIKeyboardTouchInfo maySuppressUpAction];
-[UIKeyboardTouchInfo initialDragPoint];
-[UIKeyboardTouchInfo fingerID];
-[UIKeyboardTouchInfo init];
-[UIKeyboardTouchInfo stage];
-[UIKeyboardTouchInfo setSlidOffKey:];
-[UIKeyboardTouchInfo setKey:];
-[UIKeyboardTouchInfo setDidPlayKeyFeedback:];
-[UIKeyboardTouchInfo setInitialPoint:];
-[UIKeyboardTouchInfo slidOffKey];
-[UIKeyboardTouchInfo setDelayed:];
-[UIKeyboardTouchInfo continuousPathState];
-[UIKeyboardTouchInfo dragged];
-[UIKeyboardTouchInfo processedTouchCount];
-[UIKeyboardTouchInfo setContinuousPathState:];
-[UIKeyboardTouchInfo setInitialKeyState:];
-[UIKeyboardTouchInfo setStage:];
-[UIKeyboardTouchInfo addTouch:];
-[UIKeyboardTouchInfo didPlayKeyFeedback];
-[UIKeyboardTouchInfo setFingerID:];
-[UIKeyboardTouchInfo initialKeyState];
-[UIKeyboardTouchInfo setDragged:];
-[UIKeyboardTouchInfo key];
```
