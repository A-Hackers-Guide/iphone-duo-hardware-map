# `PLCoreDuetAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 6 instance variables, 6 properties, 21 instance methods, 9 class methods

## Instance variables

```
@"PLNSNotificationOperatorComposition" _dailyTaskNotification;
@"PLXPCListenerOperatorComposition" _inactivityPredictionListener;
@"PLXPCListenerOperatorComposition" _inactivityFeaturesListener;
@"PLXPCListenerOperatorComposition" _inactivityPredictionQueryListener;
@"PLXPCListenerOperatorComposition" _inactivityPredictionTimelineListener;
@"PLXPCListenerOperatorComposition" _inactivityPredictionInterruptionListener;
```

## Properties

```
@property (T@"PLNSNotificationOperatorComposition",&,V_dailyTaskNotification) dailyTaskNotification;
@property (T@"PLXPCListenerOperatorComposition",&,V_inactivityPredictionListener) inactivityPredictionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_inactivityFeaturesListener) inactivityFeaturesListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_inactivityPredictionQueryListener) inactivityPredictionQueryListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_inactivityPredictionTimelineListener) inactivityPredictionTimelineListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_inactivityPredictionInterruptionListener) inactivityPredictionInterruptionListener;
```

## Class methods

```
+[PLCoreDuetAgent entryEventIntervalDefinitions];
+[PLCoreDuetAgent entryEventForwardDefinitions];
+[PLCoreDuetAgent load];
+[PLCoreDuetAgent entryEventIntervalDefinitionInactivityPrediction];
+[PLCoreDuetAgent entryEventForwardDefinitionInactivityPredictionInterruption];
+[PLCoreDuetAgent entryEventIntervalDefinitionInBedDetection];
+[PLCoreDuetAgent entryEventForwardDefinitionInactivityFeatures];
+[PLCoreDuetAgent entryEventForwardDefinitionInactivityPredictionQuery];
+[PLCoreDuetAgent entryEventForwardDefinitionInactivityPredictionTimeline];
```

## Instance methods

```
-[PLCoreDuetAgent init];
-[PLCoreDuetAgent initOperatorDependancies];
-[PLCoreDuetAgent initTaskOperatorDependancies];
-[PLCoreDuetAgent setDailyTaskNotification:];
-[PLCoreDuetAgent log];
-[PLCoreDuetAgent dailyTaskNotification];
-[PLCoreDuetAgent inactivityFeaturesListener];
-[PLCoreDuetAgent inactivityPredictionInterruptionListener];
-[PLCoreDuetAgent inactivityPredictionListener];
-[PLCoreDuetAgent inactivityPredictionQueryListener];
-[PLCoreDuetAgent inactivityPredictionTimelineListener];
-[PLCoreDuetAgent logEventForwardInactivityFeatures:];
-[PLCoreDuetAgent logEventForwardInactivityPredictionInterruption:];
-[PLCoreDuetAgent logEventForwardInactivityPredictionQuery:];
-[PLCoreDuetAgent logEventForwardInactivityPredictionTimeline:];
-[PLCoreDuetAgent logEventIntervalInactivityPrediction:];
-[PLCoreDuetAgent setInactivityFeaturesListener:];
-[PLCoreDuetAgent setInactivityPredictionInterruptionListener:];
-[PLCoreDuetAgent setInactivityPredictionListener:];
-[PLCoreDuetAgent setInactivityPredictionQueryListener:];
-[PLCoreDuetAgent setInactivityPredictionTimelineListener:];
```
