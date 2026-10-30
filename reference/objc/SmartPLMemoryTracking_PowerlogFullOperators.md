# `SmartPLMemoryTracking`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"PLSmartPLService" _operator;
@"PLEntryNotificationOperatorComposition" _memoryTrackingNotification;
```

## Properties

```
@property (T@"PLSmartPLService",W,V_operator) operator;
@property (T@"PLEntryNotificationOperatorComposition",&,V_memoryTrackingNotification) memoryTrackingNotification;
```

## Class methods

```
+[SmartPLMemoryTracking defaults];
```

## Instance methods

```
-[SmartPLMemoryTracking operator];
-[SmartPLMemoryTracking setOperator:];
-[SmartPLMemoryTracking handleMemoryTracking:];
-[SmartPLMemoryTracking memoryTrackingNotification];
-[SmartPLMemoryTracking setMemoryTrackingNotification:];
-[SmartPLMemoryTracking startWithOperator:];
```
