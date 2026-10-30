# `VTTriggerEventMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTTriggerEventMonitorDelegate`
- 6 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _notifyToken;
i _notifyTokenLegacyTrigger;
i _notifyTokenLegacyEarlyDetect;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _connection;
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTTriggerEventMonitor sharedMonitor];
```

## Instance methods

```
-[VTTriggerEventMonitor removeObserver:];
-[VTTriggerEventMonitor init];
-[VTTriggerEventMonitor _invalidateConnection];
-[VTTriggerEventMonitor dealloc];
-[VTTriggerEventMonitor addObserver:];
-[VTTriggerEventMonitor _voiceTriggered];
-[VTTriggerEventMonitor _attemptConnection];
-[VTTriggerEventMonitor _attemptConnectionInQueue];
-[VTTriggerEventMonitor _earlyDetected];
-[VTTriggerEventMonitor _enableTriggerEventXPCNotification:];
-[VTTriggerEventMonitor earlyDetected];
-[VTTriggerEventMonitor voiceTriggered];
```
