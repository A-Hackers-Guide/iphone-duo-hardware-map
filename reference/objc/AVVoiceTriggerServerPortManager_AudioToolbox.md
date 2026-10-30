# `AVVoiceTriggerServerPortManager`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _listeningEnabled;
B _lastStateSent;
f _hysteresisDurationSeconds;
Q _portType;
@? _notificationBlock;
q _generation;
```

## Properties

```
@property (TQ,N,V_portType) portType;
@property (Tf,N,V_hysteresisDurationSeconds) hysteresisDurationSeconds;
@property (T@?,C,N,V_notificationBlock) notificationBlock;
@property (TB,N,V_listeningEnabled) listeningEnabled;
@property (TB,N,V_lastStateSent) lastStateSent;
@property (Tq,N,V_generation) generation;
```

## Instance methods

```
-[AVVoiceTriggerServerPortManager portType];
-[AVVoiceTriggerServerPortManager setGeneration:];
-[AVVoiceTriggerServerPortManager setNotificationBlock:];
-[AVVoiceTriggerServerPortManager setPortType:];
-[AVVoiceTriggerServerPortManager generation];
-[AVVoiceTriggerServerPortManager notificationBlock];
-[AVVoiceTriggerServerPortManager callNotificationBlock:];
-[AVVoiceTriggerServerPortManager hysteresisDurationSeconds];
-[AVVoiceTriggerServerPortManager initWithPortType:hysteresisDurationSeconds:notificationBlock:];
-[AVVoiceTriggerServerPortManager lastStateSent];
-[AVVoiceTriggerServerPortManager listeningEnabled];
-[AVVoiceTriggerServerPortManager notifyStateChanged:onQueue:];
-[AVVoiceTriggerServerPortManager setHysteresisDurationSeconds:];
-[AVVoiceTriggerServerPortManager setLastStateSent:];
-[AVVoiceTriggerServerPortManager setListeningEnabled:];
```
