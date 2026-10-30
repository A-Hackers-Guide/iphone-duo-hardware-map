# `SBHardwareButtonZStackClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHardwareButtonServiceObserver`, `SBFZStackParticipantDelegate`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBFZStackResolver" _zStackResolver;
@"SBHardwareButtonService" _hardwareButtonService;
@"SBFZStackParticipant" _zStackParticipant;
@"<BSInvalidatable>" _hardwareButtonObserverAssertion;
```

## Properties

```
@property (T@"SBFZStackResolver",R,W,N,V_zStackResolver) zStackResolver;
@property (T@"SBHardwareButtonService",R,W,N,V_hardwareButtonService) hardwareButtonService;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (T@"<BSInvalidatable>",&,N,V_hardwareButtonObserverAssertion) hardwareButtonObserverAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHardwareButtonZStackClient zStackParticipant];
-[SBHardwareButtonZStackClient setZStackParticipant:];
-[SBHardwareButtonZStackClient zStackParticipant:updatePreferences:];
-[SBHardwareButtonZStackClient dealloc];
-[SBHardwareButtonZStackClient zStackParticipantDidChange:];
-[SBHardwareButtonZStackClient zStackResolver];
-[SBHardwareButtonZStackClient hardwareButtonObserverAssertion];
-[SBHardwareButtonZStackClient _updateZStackParticipant];
-[SBHardwareButtonZStackClient buttonService:buttonKind:eventsConsumedDidChange:];
-[SBHardwareButtonZStackClient hardwareButtonService];
-[SBHardwareButtonZStackClient initWithZStackResolver:hardwareButtonService:];
-[SBHardwareButtonZStackClient setHardwareButtonObserverAssertion:];
```
