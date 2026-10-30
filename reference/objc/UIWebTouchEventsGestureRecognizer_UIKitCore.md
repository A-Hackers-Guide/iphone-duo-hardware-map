# `UIWebTouchEventsGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 12 instance variables, 12 properties, 28 instance methods, 3 class methods

## Instance variables

```
@ _touchTarget;
: _touchAction;
@"<UIWebTouchEventsGestureRecognizerDelegate>" _webTouchDelegate;
B _passedHitTest;
B _defaultPrevented;
B _dispatchingTouchEvents;
B _isPotentialTap;
B _wasExplicitlyCancelled;
d _originalGestureDistance;
d _originalGestureAngle;
{_UIWebTouchEvent="type"i"timestamp"d"locationInScreenCoordinates"{CGPoint="x"d"y"d}"locationInDocumentCoordinates"{CGPoint="x"d"y"d}"scale"d"rotation"d"inJavaScriptGesture"B"touchPoints"^{_UIWebTouchPoint}"touchPointCount"I"isPotentialTap"B} _lastTouchEvent;
@"NSMapTable" _activeTouchesByIdentifier;
```

## Properties

```
@property (TB,N,GisDefaultPrevented,V_defaultPrevented) defaultPrevented;
@property (Tr^{_UIWebTouchEvent=id{CGPoint=dd}{CGPoint=dd}ddB^{_UIWebTouchPoint}IB},R,N) lastTouchEvent;
@property (TB,R,N,GisDispatchingTouchEvents,V_dispatchingTouchEvents) dispatchingTouchEvents;
@property (T@"NSMapTable",R,N,V_activeTouchesByIdentifier) activeTouchesByIdentifier;
@property (Ti,R,N) type;
@property (T{CGPoint=dd},R,N) locationInWindow;
@property (T@"NSMutableArray",R,N) touchLocations;
@property (T@"NSMutableArray",R,N) touchIdentifiers;
@property (T@"NSMutableArray",R,N) touchPhases;
@property (TB,R,N) inJavaScriptGesture;
@property (Td,R,N) scale;
@property (Td,R,N) rotation;
```

## Class methods

```
+[UIWebTouchEventsGestureRecognizer initialize];
+[UIWebTouchEventsGestureRecognizer _supportsDefaultTouchTypes];
+[UIWebTouchEventsGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UIWebTouchEventsGestureRecognizer touchesEnded:withEvent:];
-[UIWebTouchEventsGestureRecognizer canBePreventedByGestureRecognizer:];
-[UIWebTouchEventsGestureRecognizer _resetGestureRecognizer];
-[UIWebTouchEventsGestureRecognizer touchesCancelled:withEvent:];
-[UIWebTouchEventsGestureRecognizer rotation];
-[UIWebTouchEventsGestureRecognizer lastTouchEvent];
-[UIWebTouchEventsGestureRecognizer _updateTapStateWithTouches:];
-[UIWebTouchEventsGestureRecognizer performAction];
-[UIWebTouchEventsGestureRecognizer dealloc];
-[UIWebTouchEventsGestureRecognizer isDispatchingTouchEvents];
-[UIWebTouchEventsGestureRecognizer reset];
-[UIWebTouchEventsGestureRecognizer touchesBegan:withEvent:];
-[UIWebTouchEventsGestureRecognizer touchesMoved:withEvent:];
-[UIWebTouchEventsGestureRecognizer isDefaultPrevented];
-[UIWebTouchEventsGestureRecognizer scale];
-[UIWebTouchEventsGestureRecognizer type];
-[UIWebTouchEventsGestureRecognizer _processTouches:withEvent:type:];
-[UIWebTouchEventsGestureRecognizer setDefaultPrevented:];
-[UIWebTouchEventsGestureRecognizer cancel];
-[UIWebTouchEventsGestureRecognizer activeTouchesByIdentifier];
-[UIWebTouchEventsGestureRecognizer _updateTapStateWithTouches:type:];
-[UIWebTouchEventsGestureRecognizer locationInWindow];
-[UIWebTouchEventsGestureRecognizer _recordTouches:type:];
-[UIWebTouchEventsGestureRecognizer inJavaScriptGesture];
-[UIWebTouchEventsGestureRecognizer initWithTarget:action:touchDelegate:];
-[UIWebTouchEventsGestureRecognizer touchIdentifiers];
-[UIWebTouchEventsGestureRecognizer touchLocations];
-[UIWebTouchEventsGestureRecognizer touchPhases];
```
