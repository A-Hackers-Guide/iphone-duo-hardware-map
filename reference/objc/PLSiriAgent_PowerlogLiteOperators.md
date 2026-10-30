# `PLSiriAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 6 instance variables, 6 properties, 25 instance methods, 13 class methods

## Instance variables

```
@"PLXPCListenerOperatorComposition" _asrEventListener;
@"PLXPCListenerOperatorComposition" _dictationConnectionListener;
@"PLXPCListenerOperatorComposition" _selfTriggerSuppressionDetectedListener;
@"PLXPCListenerOperatorComposition" _selfTriggerSuppressionProcessingListener;
@"PLXPCListenerOperatorComposition" _siriWakesListener;
@"PLXPCListenerOperatorComposition" _siriConfigListener;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_asrEventListener) asrEventListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_dictationConnectionListener) dictationConnectionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_selfTriggerSuppressionDetectedListener) selfTriggerSuppressionDetectedListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_selfTriggerSuppressionProcessingListener) selfTriggerSuppressionProcessingListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_siriWakesListener) siriWakesListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_siriConfigListener) siriConfigListener;
```

## Class methods

```
+[PLSiriAgent entryEventIntervalDefinitions];
+[PLSiriAgent entryEventPointDefinitions];
+[PLSiriAgent entryEventForwardDefinitions];
+[PLSiriAgent entryEventBackwardDefinitions];
+[PLSiriAgent entryEventNoneDefinitions];
+[PLSiriAgent load];
+[PLSiriAgent entryEventIntervalSelfTriggerSuppression];
+[PLSiriAgent entryEventPointDefinitionSiriWakes];
+[PLSiriAgent entryEventForwardDefinitionDictationConnection];
+[PLSiriAgent entryEventPointSelfTriggerSuppressionDetected];
+[PLSiriAgent entryEventForwardASREvent];
+[PLSiriAgent entryEventForwardDefinitionSiriConfig];
+[PLSiriAgent entryAggregateDefinitions];
```

## Instance methods

```
-[PLSiriAgent siriConfigListener];
-[PLSiriAgent convertMode:];
-[PLSiriAgent siriWakesListener];
-[PLSiriAgent setSelfTriggerSuppressionDetectedListener:];
-[PLSiriAgent selfTriggerSuppressionDetectedListener];
-[PLSiriAgent convertASREvent:];
-[PLSiriAgent init];
-[PLSiriAgent logEventForwardSiriConfig:];
-[PLSiriAgent logEventPointSelfTriggerSuppressionDetected:];
-[PLSiriAgent convertRecognition:];
-[PLSiriAgent setSiriWakesListener:];
-[PLSiriAgent dictationConnectionListener];
-[PLSiriAgent initOperatorDependancies];
-[PLSiriAgent logEventPointSiriWakes:];
-[PLSiriAgent setAsrEventListener:];
-[PLSiriAgent setSiriConfigListener:];
-[PLSiriAgent selfTriggerSuppressionProcessingListener];
-[PLSiriAgent logEventForwardASREvent:];
-[PLSiriAgent logEventForwardDictationConnection:];
-[PLSiriAgent convertSiriEvent:];
-[PLSiriAgent log];
-[PLSiriAgent asrEventListener];
-[PLSiriAgent setDictationConnectionListener:];
-[PLSiriAgent setSelfTriggerSuppressionProcessingListener:];
-[PLSiriAgent logEventIntervalSelfTriggerSuppression:];
```
