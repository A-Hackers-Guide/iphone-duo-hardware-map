# `PLCoreDuetEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
C _updateType;
@"NSString" _bundleID;
@"NSString" _processName;
@"NSDictionary" _childBundleIDToWeight;
@"NSArray" _eventIntervals;
```

## Properties

```
@property (T@"NSString",&,V_bundleID) bundleID;
@property (TC,V_updateType) updateType;
@property (T@"NSString",&,V_processName) processName;
@property (T@"NSDictionary",&,V_childBundleIDToWeight) childBundleIDToWeight;
@property (T@"NSArray",&,V_eventIntervals) eventIntervals;
```

## Instance methods

```
-[PLCoreDuetEvent setProcessName:];
-[PLCoreDuetEvent setUpdateType:];
-[PLCoreDuetEvent setBundleID:];
-[PLCoreDuetEvent updateType];
-[PLCoreDuetEvent processName];
-[PLCoreDuetEvent description];
-[PLCoreDuetEvent bundleID];
-[PLCoreDuetEvent childBundleIDToWeight];
-[PLCoreDuetEvent eventIntervals];
-[PLCoreDuetEvent setChildBundleIDToWeight:];
-[PLCoreDuetEvent setEventIntervals:];
```
