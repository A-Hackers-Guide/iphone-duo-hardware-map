# `CMNatalimeterInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
B fStartedUpdates;
@? fHandler;
```

## Instance methods

```
-[CMNatalimeterInternal init];
-[CMNatalimeterInternal dealloc];
-[CMNatalimeterInternal _teardown];
-[CMNatalimeterInternal _handleQueryResponse:withHandler:];
-[CMNatalimeterInternal _promptsNeeded];
-[CMNatalimeterInternal _queryAbsoluteNatalimetryDataSinceDataRecord:withHandler:];
-[CMNatalimeterInternal _queryAbsoluteNatalimetryDataSinceRecord:withHandler:];
-[CMNatalimeterInternal _startAbsoluteNatalimetryDataUpdatesWithHandler:];
-[CMNatalimeterInternal _stopAbsoluteNatalimetryDataUpdates];
```
