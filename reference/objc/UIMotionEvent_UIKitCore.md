# `UIMotionEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- Protocols: `BLSBacklightStateObserving`
- 15 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"BKSAccelerometer" _motionAccelerometer;
q _subtype;
i _shakeState;
q _stateMachineState;
d _shakeStartTime;
d _lastMovementTime;
d _highLevelTime;
d _lowEndTimeout;
@"NSTimer" _idleTimer;
B _sentMotionBegan;
[10f] _lowPassState;
Q _lowPassStateIndex;
Q _highPassStateIndex;
[2f] _highPassState;
@"BLSBacklight" _observedBacklight;
```

## Properties

```
@property (Ti,N,V_shakeState) shakeState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIMotionEvent _allWindows];
-[UIMotionEvent backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[UIMotionEvent subtype];
-[UIMotionEvent _updateAccelerometerEnabled];
-[UIMotionEvent _enablePeakDetectionForScreenBlanked:];
-[UIMotionEvent _accelerometerDidDetectMovementWithTimestamp:];
-[UIMotionEvent _detectWhenNotActive];
-[UIMotionEvent _sendEventToResponder:];
-[UIMotionEvent _highPass:];
-[UIMotionEvent dealloc];
-[UIMotionEvent setShakeState:];
-[UIMotionEvent _isDetectingMotionEvents];
-[UIMotionEvent _willResume];
-[UIMotionEvent _shakeState];
-[UIMotionEvent _willSuspend];
-[UIMotionEvent _init];
-[UIMotionEvent _determineShakeLevelX:y:z:currentState:];
-[UIMotionEvent _setSubtype:];
-[UIMotionEvent type];
-[UIMotionEvent shakeState];
-[UIMotionEvent description];
-[UIMotionEvent _feedStateMachine:currentState:timestamp:];
-[UIMotionEvent _idleTimerFired];
-[UIMotionEvent _resetLowPassState];
-[UIMotionEvent accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:];
-[UIMotionEvent _lowPass:];
```
