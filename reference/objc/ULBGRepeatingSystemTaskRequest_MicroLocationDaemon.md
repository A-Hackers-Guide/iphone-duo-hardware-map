# `ULBGRepeatingSystemTaskRequest`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULBGSystemTaskRequest`
- 2 instance variables, 2 properties, 6 instance methods, 7 class methods

## Instance variables

```
d _interval;
d _minDurationBetweenInstances;
```

## Properties

```
@property (Td,N,V_interval) interval;
@property (Td,N,V_minDurationBetweenInstances) minDurationBetweenInstances;
```

## Class methods

```
+[ULBGRepeatingSystemTaskRequest analyticsULBGRepeatingSystemTaskRequest];
+[ULBGRepeatingSystemTaskRequest exportBackupULBGRepeatingSystemTaskRequest];
+[ULBGRepeatingSystemTaskRequest learningULBGRepeatingSystemTaskRequest];
+[ULBGRepeatingSystemTaskRequest maintenanceULBGRepeatingSystemTaskRequest];
+[ULBGRepeatingSystemTaskRequest mapReconstructionULBGRepeatingSystemTaskRequest];
+[ULBGRepeatingSystemTaskRequest routineStateAnalyzerULBGRepeatingSystemTaskRequest];
+[ULBGRepeatingSystemTaskRequest wifiAnalyzerULBGRepeatingSystemTaskRequest];
```

## Instance methods

```
-[ULBGRepeatingSystemTaskRequest minDurationBetweenInstances];
-[ULBGRepeatingSystemTaskRequest initWithIdentifier:interval:minDurationBetweenInstances:];
-[ULBGRepeatingSystemTaskRequest setInterval:];
-[ULBGRepeatingSystemTaskRequest interval];
-[ULBGRepeatingSystemTaskRequest setMinDurationBetweenInstances:];
-[ULBGRepeatingSystemTaskRequest createRequestFromSelf];
```
