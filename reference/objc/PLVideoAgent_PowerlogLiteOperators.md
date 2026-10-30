# `PLVideoAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 6 instance variables, 6 properties, 22 instance methods, 10 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _notification;
@"PLXPCListenerOperatorComposition" _cMVideoQueueListener;
@"PLXPCListenerOperatorComposition" _vTSessionListener;
@"PLXPCListenerOperatorComposition" _vTTileListener;
@"PLXPCListenerOperatorComposition" _cMVideoPlaybackListener;
@"PLXPCListenerOperatorComposition" _groupSessionListener;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_notification) notification;
@property (T@"PLXPCListenerOperatorComposition",&,V_cMVideoQueueListener) cMVideoQueueListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_vTSessionListener) vTSessionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_vTTileListener) vTTileListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_cMVideoPlaybackListener) cMVideoPlaybackListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_groupSessionListener) groupSessionListener;
```

## Class methods

```
+[PLVideoAgent entryEventIntervalDefinitions];
+[PLVideoAgent entryEventPointDefinitions];
+[PLVideoAgent entryEventForwardDefinitions];
+[PLVideoAgent entryEventBackwardDefinitions];
+[PLVideoAgent entryEventNoneDefinitions];
+[PLVideoAgent load];
+[PLVideoAgent defaults];
+[PLVideoAgent entryAggregateDefinitions];
+[PLVideoAgent entryEventIntervalDefinitionGroupSession];
+[PLVideoAgent stateEnumForStateString:];
```

## Instance methods

```
-[PLVideoAgent notification];
-[PLVideoAgent logEventBackwardVTSessionWithEntry:];
-[PLVideoAgent logEventBackwardCMVideoPlaybackWithEntry:];
-[PLVideoAgent logEventBackwardCMVideoQueueWithEntry:];
-[PLVideoAgent logEventForwardVideoWithEntry:];
-[PLVideoAgent setCMVideoQueueListener:];
-[PLVideoAgent init];
-[PLVideoAgent setNotification:];
-[PLVideoAgent setVTSessionListener:];
-[PLVideoAgent groupSessionListener];
-[PLVideoAgent initOperatorDependancies];
-[PLVideoAgent setCMVideoPlaybackListener:];
-[PLVideoAgent vTTileListener];
-[PLVideoAgent setVTTileListener:];
-[PLVideoAgent logEventBackwardVTTileWithEntry:];
-[PLVideoAgent setGroupSessionListener:];
-[PLVideoAgent cMVideoQueueListener];
-[PLVideoAgent log];
-[PLVideoAgent convertPlaybackTypetoInt:];
-[PLVideoAgent logEventIntervalGroupSession:];
-[PLVideoAgent cMVideoPlaybackListener];
-[PLVideoAgent vTSessionListener];
```
