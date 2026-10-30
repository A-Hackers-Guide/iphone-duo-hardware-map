# `MLBackgroundTask`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 1 properties, 9 instance methods, 5 class methods

## Instance variables

```
@"NSString" _taskIdentifier;
```

## Properties

```
@property (T@"NSString",C,N,V_taskIdentifier) taskIdentifier;
```

## Class methods

```
+[MLBackgroundTask supportsSecureCoding];
+[MLBackgroundTask scheduleTask:];
+[MLBackgroundTask cancelAllTasks];
+[MLBackgroundTask cancelTaskWithIdentifier:];
+[MLBackgroundTask taskIsScheduledWithIdentifier:];
```

## Instance methods

```
-[MLBackgroundTask taskIdentifier];
-[MLBackgroundTask init];
-[MLBackgroundTask encodeWithCoder:];
-[MLBackgroundTask hash];
-[MLBackgroundTask initWithCoder:];
-[MLBackgroundTask copyWithZone:];
-[MLBackgroundTask isEqual:];
-[MLBackgroundTask setTaskIdentifier:];
-[MLBackgroundTask activityForScheduling];
```
