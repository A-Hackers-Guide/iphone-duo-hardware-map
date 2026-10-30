# `SBSOSClawGestureObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SOSManagerClientObserver`, `SBVolumePressBandit`
- 10 instance variables, 15 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SOSManager" _sosManager;
@"SBMainWorkspace" _workspace;
@"NSMutableDictionary" _activePressTypeToDownTimestamp;
B _sosEnabled;
B _wasSOSTiggeredByClaw;
B _gestureLoggingEnabled;
@"NSMutableSet" _activePressTypes;
@"<SBSOSClawGestureObserverDelegate>" _delegate;
@"SBSOSDefaults" _sosDefaults;
@"BSAbsoluteMachTimer" _sosTriggerTimer;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_activePressTypes) activePressTypes;
@property (TB,R,N,G_isSOSActivated) sosActivated;
@property (T@"SBSOSDefaults",&,N,S_setSOSDefaults:,V_sosDefaults) sosDefaults;
@property (T@"BSAbsoluteMachTimer",&,N,V_sosTriggerTimer) sosTriggerTimer;
@property (TB,N,G_wasSOSTriggeredByClaw,S_setWasSOSTriggeredByClaw:,V_wasSOSTiggeredByClaw) wasSOSTiggeredByClaw;
@property (TB,R,N,G_isClawGestureActive) clawGestureActive;
@property (TB,R,N,G_isAutomaticCallCountdownEnabled) autoCallCountdownEnabled;
@property (TB,N,GisGestureLoggingEnabled,V_gestureLoggingEnabled) gestureLoggingEnabled;
@property (TB,N,GisSOSEnabled,SsetSOSEnabled:,V_sosEnabled) sosEnabled;
@property (T@"<SBSOSClawGestureObserverDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisClawActivated) clawActivated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSOSClawGestureObserver init];
-[SBSOSClawGestureObserver dealloc];
-[SBSOSClawGestureObserver setDelegate:];
-[SBSOSClawGestureObserver sosDefaults];
-[SBSOSClawGestureObserver delegate];
-[SBSOSClawGestureObserver _isSOSActivated];
-[SBSOSClawGestureObserver sosTriggerTimer];
-[SBSOSClawGestureObserver isClawActivated];
-[SBSOSClawGestureObserver _cancelSOSActivity];
-[SBSOSClawGestureObserver _currentSOSButtonPressState];
-[SBSOSClawGestureObserver _initWithSOSManager:workspace:];
-[SBSOSClawGestureObserver _isAutomaticCallCountdownEnabled];
-[SBSOSClawGestureObserver _isClawGestureActive];
-[SBSOSClawGestureObserver _presentSOSInterface];
-[SBSOSClawGestureObserver _setSOSDefaults:];
-[SBSOSClawGestureObserver _setWasSOSTriggeredByClaw:];
-[SBSOSClawGestureObserver _updateActivePressesForPressType:down:timestamp:];
-[SBSOSClawGestureObserver _wasSOSTriggeredByClaw];
-[SBSOSClawGestureObserver activePressTypes];
-[SBSOSClawGestureObserver didUpdateCurrentSOSInitiationState:];
-[SBSOSClawGestureObserver handleVolumeDecrease];
-[SBSOSClawGestureObserver handleVolumeIncrease];
-[SBSOSClawGestureObserver isGestureLoggingEnabled];
-[SBSOSClawGestureObserver isSOSEnabled];
-[SBSOSClawGestureObserver noteButtonPress:isDown:];
-[SBSOSClawGestureObserver noteGestureReset];
-[SBSOSClawGestureObserver setActivePressTypes:];
-[SBSOSClawGestureObserver setGestureLoggingEnabled:];
-[SBSOSClawGestureObserver setSOSEnabled:];
-[SBSOSClawGestureObserver setSosTriggerTimer:];
```
