# `SBSOSLockGestureObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPressSequenceRecognizerDelegate`
- 10 instance variables, 10 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SBPressSequenceRecognizer" _recognizer;
@"SBPressSequenceValidator" _validator;
@"SBPressSequenceSettings" _settings;
B _lastKnownActiveState;
@"BSAction" _triggerAction;
B _gestureLoggingEnabled;
B _sosEnabled;
@"SBPressSequenceObserver" _sosLockPressSequenceObserver;
@"<SBSOSLockGestureObserverDelegate>" _delegate;
q _configuration;
```

## Properties

```
@property (T@"SBPressSequenceObserver",&,N,V_sosLockPressSequenceObserver) sosLockPressSequenceObserver;
@property (T@"<SBSOSLockGestureObserverDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,V_configuration) configuration;
@property (Tq,R,N) triggerMechanism;
@property (TB,N,GisGestureLoggingEnabled,V_gestureLoggingEnabled) gestureLoggingEnabled;
@property (TB,N,GisSOSEnabled,SsetSOSEnabled:,V_sosEnabled) sosEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSOSLockGestureObserver _configure];
-[SBSOSLockGestureObserver init];
-[SBSOSLockGestureObserver initWithConfiguration:];
-[SBSOSLockGestureObserver setDelegate:];
-[SBSOSLockGestureObserver configuration];
-[SBSOSLockGestureObserver delegate];
-[SBSOSLockGestureObserver _validator];
-[SBSOSLockGestureObserver _setRecognizer:];
-[SBSOSLockGestureObserver pressSequenceRecognizerDidFail:];
-[SBSOSLockGestureObserver registerPressDownWithTimestamp:];
-[SBSOSLockGestureObserver _configureSettings];
-[SBSOSLockGestureObserver _intervalThatSucceeds];
-[SBSOSLockGestureObserver _noteTriggerActionReceivedResponse];
-[SBSOSLockGestureObserver _noteTriggerDidBecomeActive];
-[SBSOSLockGestureObserver _noteTriggerDidBecomeInactive];
-[SBSOSLockGestureObserver _numberOfPressesThatActivate];
-[SBSOSLockGestureObserver _numberOfPressesThatTrigger];
-[SBSOSLockGestureObserver _watchdogInterval];
-[SBSOSLockGestureObserver isGestureLoggingEnabled];
-[SBSOSLockGestureObserver isSOSEnabled];
-[SBSOSLockGestureObserver noteDidBeginSOSWithUUID:];
-[SBSOSLockGestureObserver pressSequenceRecognizer:didBeginPressDownAtIndex:];
-[SBSOSLockGestureObserver pressSequenceRecognizerDidCompleteSequence:];
-[SBSOSLockGestureObserver registerPressUpWithTimestamp:];
-[SBSOSLockGestureObserver resetWithNewConfiguration:];
-[SBSOSLockGestureObserver setGestureLoggingEnabled:];
-[SBSOSLockGestureObserver setSOSEnabled:];
-[SBSOSLockGestureObserver setSosLockPressSequenceObserver:];
-[SBSOSLockGestureObserver sosLockPressSequenceObserver];
-[SBSOSLockGestureObserver triggerMechanism];
```
