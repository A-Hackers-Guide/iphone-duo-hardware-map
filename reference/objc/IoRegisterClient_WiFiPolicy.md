# `IoRegisterClient`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _internalQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
```

## Class methods

```
+[IoRegisterClient sharedInstance];
```

## Instance methods

```
-[IoRegisterClient init];
-[IoRegisterClient description];
-[IoRegisterClient setInternalQueue:];
-[IoRegisterClient internalQueue];
-[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:];
-[IoRegisterClient _isMatch:onClassNames:];
-[IoRegisterClient _isMatch:onKeys:planeName:results:];
-[IoRegisterClient _searchEntry:hasMatchedDepth:currentDepth:maxDepth:classNames:keys:planeName:results:];
-[IoRegisterClient fetchEntriesForClasses:depth:keys:plane:error:];
```
