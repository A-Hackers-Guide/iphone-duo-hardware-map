# `PLSecureServiceAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 12 instance variables, 12 properties, 29 instance methods, 6 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _daemonLaunchListener;
@"PLXPCListenerOperatorComposition" _connectionListener;
@"PLXPCListenerOperatorComposition" _disconnectionListener;
@"PLXPCListenerOperatorComposition" _deviceIntentListener;
@"PLXPCListenerOperatorComposition" _periodicReportListener;
@"PLTimer" _entriesPerHourTimer;
q _numBTConn;
q _periodicReportCount;
q _prevActiveKeys;
q _numEntries;
q _previousEvent;
@"NSString" _previousHash;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_daemonLaunchListener) daemonLaunchListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_connectionListener) connectionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_disconnectionListener) disconnectionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_deviceIntentListener) deviceIntentListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_periodicReportListener) periodicReportListener;
@property (T@"PLTimer",&,V_entriesPerHourTimer) entriesPerHourTimer;
@property (Tq,V_numBTConn) numBTConn;
@property (Tq,V_periodicReportCount) periodicReportCount;
@property (Tq,V_prevActiveKeys) prevActiveKeys;
@property (Tq,V_numEntries) numEntries;
@property (Tq,V_previousEvent) previousEvent;
@property (T@"NSString",&,V_previousHash) previousHash;
```

## Class methods

```
+[PLSecureServiceAgent entryEventPointDefinitions];
+[PLSecureServiceAgent load];
+[PLSecureServiceAgent defaults];
+[PLSecureServiceAgent entryEventPointDefinitionConnectionState];
+[PLSecureServiceAgent entryEventPointDefinitionSummary];
+[PLSecureServiceAgent isSecureServiceSupported];
```

## Instance methods

```
-[PLSecureServiceAgent connectionListener];
-[PLSecureServiceAgent init];
-[PLSecureServiceAgent initOperatorDependancies];
-[PLSecureServiceAgent setConnectionListener:];
-[PLSecureServiceAgent log];
-[PLSecureServiceAgent previousEvent];
-[PLSecureServiceAgent setPreviousEvent:];
-[PLSecureServiceAgent numEntries];
-[PLSecureServiceAgent setNumEntries:];
-[PLSecureServiceAgent daemonLaunchListener];
-[PLSecureServiceAgent deviceIntentListener];
-[PLSecureServiceAgent disconnectionListener];
-[PLSecureServiceAgent entriesPerHourTimer];
-[PLSecureServiceAgent logEventPointConnectionState:withEvent:];
-[PLSecureServiceAgent logEventPointPeriodicReport:];
-[PLSecureServiceAgent numBTConn];
-[PLSecureServiceAgent periodicReportCount];
-[PLSecureServiceAgent periodicReportListener];
-[PLSecureServiceAgent prevActiveKeys];
-[PLSecureServiceAgent previousHash];
-[PLSecureServiceAgent setDaemonLaunchListener:];
-[PLSecureServiceAgent setDeviceIntentListener:];
-[PLSecureServiceAgent setDisconnectionListener:];
-[PLSecureServiceAgent setEntriesPerHourTimer:];
-[PLSecureServiceAgent setNumBTConn:];
-[PLSecureServiceAgent setPeriodicReportCount:];
-[PLSecureServiceAgent setPeriodicReportListener:];
-[PLSecureServiceAgent setPrevActiveKeys:];
-[PLSecureServiceAgent setPreviousHash:];
```
