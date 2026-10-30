# `AOPHapticsController`

- Image: [`/System/Library/PrivateFrameworks/AOPHaptics.framework/AOPHaptics`](../userland/System__Library__PrivateFrameworks__AOPHaptics.framework__AOPHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 2 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
^{IONotificationPort=} _notificationPort;
I _arrivalNotification;
@? _cancelHandler;
@? _readyHandler;
{atomic_flag="_Value"AB} _activated;
{atomic_flag="_Value"AB} _cancelled;
I _service;
I _connect;
```

## Properties

```
@property (TI,N,V_service) service;
@property (TI,N,V_connect) connect;
```

## Class methods

```
+[AOPHapticsController AHtoHMOutputType:];
```

## Instance methods

```
-[AOPHapticsController connect];
-[AOPHapticsController setService:];
-[AOPHapticsController init];
-[AOPHapticsController dealloc];
-[AOPHapticsController setDispatchQueue:];
-[AOPHapticsController setConnect:];
-[AOPHapticsController setCancelHandler:];
-[AOPHapticsController service];
-[AOPHapticsController activate];
-[AOPHapticsController cancel];
-[AOPHapticsController setReadyHandler:];
-[AOPHapticsController _findService];
-[AOPHapticsController playSlotIndices:error:];
-[AOPHapticsController setMappings:error:];
-[AOPHapticsController signalReady];
```
