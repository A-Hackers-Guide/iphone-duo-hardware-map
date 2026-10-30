# `PLMDNSAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 7 instance variables, 7 properties, 19 instance methods, 7 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _startBrowse;
@"PLXPCListenerOperatorComposition" _stopBrowse;
@"PLXPCListenerOperatorComposition" _startAdvertise;
@"PLXPCListenerOperatorComposition" _stopAdvertise;
@"PLXPCListenerOperatorComposition" _startResolve;
@"PLXPCListenerOperatorComposition" _stopResolve;
@"PLXPCListenerOperatorComposition" _clientSummary;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_startBrowse) startBrowse;
@property (T@"PLXPCListenerOperatorComposition",&,V_stopBrowse) stopBrowse;
@property (T@"PLXPCListenerOperatorComposition",&,V_startAdvertise) startAdvertise;
@property (T@"PLXPCListenerOperatorComposition",&,V_stopAdvertise) stopAdvertise;
@property (T@"PLXPCListenerOperatorComposition",&,V_startResolve) startResolve;
@property (T@"PLXPCListenerOperatorComposition",&,V_stopResolve) stopResolve;
@property (T@"PLXPCListenerOperatorComposition",&,V_clientSummary) clientSummary;
```

## Class methods

```
+[PLMDNSAgent entryEventPointDefinitions];
+[PLMDNSAgent entryEventForwardDefinitions];
+[PLMDNSAgent entryEventBackwardDefinitions];
+[PLMDNSAgent entryEventNoneDefinitions];
+[PLMDNSAgent load];
+[PLMDNSAgent entryEventBackwardDefinitionClientSummary];
+[PLMDNSAgent entryEventPointDefinitionsReceivedMDNSEvent];
```

## Instance methods

```
-[PLMDNSAgent stopAdvertise];
-[PLMDNSAgent setStartBrowse:];
-[PLMDNSAgent setStopResolve:];
-[PLMDNSAgent setStopBrowse:];
-[PLMDNSAgent startResolve];
-[PLMDNSAgent init];
-[PLMDNSAgent logEventPointMDNS:forEvent:];
-[PLMDNSAgent initOperatorDependancies];
-[PLMDNSAgent setStartResolve:];
-[PLMDNSAgent setClientSummary:];
-[PLMDNSAgent stopResolve];
-[PLMDNSAgent clientSummary];
-[PLMDNSAgent logEventBackwardClientSummary:];
-[PLMDNSAgent setStartAdvertise:];
-[PLMDNSAgent stopBrowse];
-[PLMDNSAgent startBrowse];
-[PLMDNSAgent log];
-[PLMDNSAgent setStopAdvertise:];
-[PLMDNSAgent startAdvertise];
```
