# `PLPersistentConnectionAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 2 instance variables, 2 properties, 9 instance methods, 9 class methods

## Instance variables

```
@"PLCFNotificationOperatorComposition" _intervalChangedNotification;
@"PLCFNotificationOperatorComposition" _preferencesChangedNotification;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",R,V_intervalChangedNotification) intervalChangedNotification;
@property (T@"PLCFNotificationOperatorComposition",R,V_preferencesChangedNotification) preferencesChangedNotification;
```

## Class methods

```
+[PLPersistentConnectionAgent entryEventIntervalDefinitions];
+[PLPersistentConnectionAgent entryEventPointDefinitions];
+[PLPersistentConnectionAgent entryEventForwardDefinitions];
+[PLPersistentConnectionAgent entryEventBackwardDefinitions];
+[PLPersistentConnectionAgent entryEventNoneDefinitions];
+[PLPersistentConnectionAgent load];
+[PLPersistentConnectionAgent defaults];
+[PLPersistentConnectionAgent accountingGroupDefinitions];
+[PLPersistentConnectionAgent railDefinitions];
```

## Instance methods

```
-[PLPersistentConnectionAgent pollingInterval];
-[PLPersistentConnectionAgent init];
-[PLPersistentConnectionAgent initOperatorDependancies];
-[PLPersistentConnectionAgent log];
-[PLPersistentConnectionAgent intervalChangedNotification];
-[PLPersistentConnectionAgent logEventForwardConfig];
-[PLPersistentConnectionAgent logEventPointCache];
-[PLPersistentConnectionAgent preferencesChangedNotification];
-[PLPersistentConnectionAgent pushEnabled];
```
