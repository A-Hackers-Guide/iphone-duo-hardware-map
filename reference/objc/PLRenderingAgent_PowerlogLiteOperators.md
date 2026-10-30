# `PLRenderingAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- Protocols: `FBSDisplayLayoutObserver`
- 6 instance variables, 10 properties, 26 instance methods, 8 class methods

## Instance variables

```
I _lastFrameCount;
@"FBSDisplayLayoutMonitor" _mainDisplayMonitor;
@"PLEntryNotificationOperatorComposition" _pluggedInStateNotification;
@"NSNumber" _deviceIsPlugged;
@"PLXPCListenerOperatorComposition" _frameStatsListener;
@"PLCFNotificationOperatorComposition" _scrollPocketListener;
```

## Properties

```
@property (T@"FBSDisplayLayoutMonitor",&,V_mainDisplayMonitor) mainDisplayMonitor;
@property (T@"PLEntryNotificationOperatorComposition",&,V_pluggedInStateNotification) pluggedInStateNotification;
@property (TI,V_lastFrameCount) lastFrameCount;
@property (T@"NSNumber",&,V_deviceIsPlugged) deviceIsPlugged;
@property (T@"PLXPCListenerOperatorComposition",&,V_frameStatsListener) frameStatsListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_scrollPocketListener) scrollPocketListener;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLRenderingAgent entryEventPointDefinitions];
+[PLRenderingAgent entryEventForwardDefinitions];
+[PLRenderingAgent entryEventBackwardDefinitions];
+[PLRenderingAgent entryEventNoneDefinitions];
+[PLRenderingAgent load];
+[PLRenderingAgent entryAggregateDefinitions];
+[PLRenderingAgent entryEventBackwardDefinitionFrameCount];
+[PLRenderingAgent entryEventBackwardDefinitionFrameStats];
```

## Instance methods

```
-[PLRenderingAgent setLastFrameCount:];
-[PLRenderingAgent setMainDisplayMonitor:];
-[PLRenderingAgent frameStatsListener];
-[PLRenderingAgent lastFrameCount];
-[PLRenderingAgent enableCAScreenTelemetry];
-[PLRenderingAgent logEventForwardScrollPocket];
-[PLRenderingAgent init];
-[PLRenderingAgent shouldLogFrameStats];
-[PLRenderingAgent setFrameStatsListener:];
-[PLRenderingAgent dealloc];
-[PLRenderingAgent initOperatorDependancies];
-[PLRenderingAgent mainDisplayMonitor];
-[PLRenderingAgent setDeviceIsPlugged:];
-[PLRenderingAgent logEventBackwardFrameStats:];
-[PLRenderingAgent logEventForwardFrameCount:];
-[PLRenderingAgent pluggedInStateNotification];
-[PLRenderingAgent disableCAScreenTelemetry];
-[PLRenderingAgent handleConnectedChange:];
-[PLRenderingAgent setPluggedInStateNotification:];
-[PLRenderingAgent layoutMonitor:didUpdateDisplayLayout:withContext:];
-[PLRenderingAgent initTaskOperatorDependancies];
-[PLRenderingAgent setScrollPocketListener:];
-[PLRenderingAgent log];
-[PLRenderingAgent deviceIsPlugged];
-[PLRenderingAgent scrollPocketListener];
-[PLRenderingAgent logFrameCount:forConnectedState:];
```
