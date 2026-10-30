# `CMNetworkActivityObserver`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _valid;
B _registered;
i _cmActivityToken;
i _cmActivityPollingToken;
@"CMNetworkActivityMonitor" _activityMonitor;
```

## Properties

```
@property (T@"CMNetworkActivityMonitor",R,N) activityMonitor;
```

## Class methods

```
+[CMNetworkActivityObserver registeredObserverForActivityMonitor:];
```

## Instance methods

```
-[CMNetworkActivityObserver dealloc];
-[CMNetworkActivityObserver invalidate];
-[CMNetworkActivityObserver activityMonitor];
-[CMNetworkActivityObserver _pollWithInterval:networkActivityDidCompleteBlock:];
-[CMNetworkActivityObserver initForActivityMonitor:];
-[CMNetworkActivityObserver registerObservations];
-[CMNetworkActivityObserver unregisterObservations];
```
