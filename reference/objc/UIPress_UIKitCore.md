# `UIPress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIResponderForwardableEventComponent`
- 18 instance variables, 23 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _gestureRecognizers;
@"NSMutableArray" _forwardingRecord;
B _abandonForwardingRecord;
B _isDelayed;
B _sentPressesEnded;
B _longClick;
I _contextID;
d _timestamp;
q _phase;
q _type;
@"UIWindow" _window;
@"UIResponder" _responder;
d _force;
@"UIKey" _key;
q _modifierFlags;
Q _source;
Q _gameControllerComponent;
Q _clickCount;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (Tq,N,V_phase) phase;
@property (Tq,N,V_type) type;
@property (T@"UIWindow",&,N,V_window) window;
@property (T@"UIResponder",&,N,V_responder) responder;
@property (T@"NSArray",C,N) gestureRecognizers;
@property (T@"UIKey",&,N,V_key) key;
@property (Tq,N,V_modifierFlags) modifierFlags;
@property (Td,N,V_force) force;
@property (TQ,N,G_source,S_setSource:,V_source) source;
@property (TQ,N,G_gameControllerComponent,S_setGameControllerComponent:,V_gameControllerComponent) gameControllerComponent;
@property (TI,R,N,V_contextID) contextID;
@property (TB,N,V_isDelayed) isDelayed;
@property (TB,N,V_sentPressesEnded) sentPressesEnded;
@property (TQ,N,V_clickCount) clickCount;
@property (TB,N,GisLongClick,V_longClick) longClick;
@property (T@"UIResponder<_UIGestureRecognizerContainer>",&,N,S_setResponder:) _responder;
@property (TQ,R,N) _eventComponentType;
@property (T@"_UIEventComponentPhaseValue",&,N,S_setEventComponentPhase:) _eventComponentPhase;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPress setTimestamp:];
-[UIPress gestureRecognizers];
-[UIPress clickCount];
-[UIPress sentPressesEnded];
-[UIPress _isDirectionalPress];
-[UIPress _isAbandoningForwardingRecord];
-[UIPress phase];
-[UIPress isDelayed];
-[UIPress isLongClick];
-[UIPress _isSynthetic];
-[UIPress _removeGestureRecognizer:];
-[UIPress timestamp];
-[UIPress _responder];
-[UIPress modifierFlags];
-[UIPress _loadStateFromPressInfo:];
-[UIPress _abandonForwardingRecord];
-[UIPress responder];
-[UIPress window];
-[UIPress _mutableForwardingRecord];
-[UIPress _setResponder:];
-[UIPress setKey:];
-[UIPress _source];
-[UIPress setModifierFlags:];
-[UIPress _forwardingRecord];
-[UIPress _isAnalogStickPress];
-[UIPress _gameControllerComponent];
-[UIPress setResponder:];
-[UIPress setGestureRecognizers:];
-[UIPress setClickCount:];
-[UIPress setType:];
-[UIPress type];
-[UIPress _eventComponentPhaseForValue:];
-[UIPress description];
-[UIPress _loadStateFromPress:];
-[UIPress _eventComponentPhase];
-[UIPress setPhase:];
-[UIPress _eventComponentType];
-[UIPress setSentPressesEnded:];
-[UIPress force];
-[UIPress contextID];
-[UIPress _setGameControllerComponent:];
-[UIPress setLongClick:];
-[UIPress _phaseDescription];
-[UIPress _setEventComponentPhase:];
-[UIPress setForce:];
-[UIPress setWindow:];
-[UIPress _responderSelectorForPhase:];
-[UIPress _setSource:];
-[UIPress _wantsForwardingFromResponder:toNextResponder:withEvent:];
-[UIPress key];
-[UIPress setIsDelayed:];
```
