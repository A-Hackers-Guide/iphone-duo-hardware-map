# `CMMotionActivityManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 12 instance methods, 4 class methods

## Instance variables

```
^v fLocationConnection;
@"NSObject<OS_dispatch_queue>" fIncomingQueue;
@"NSObject<OS_dispatch_queue>" fOutgoingQueue;
@? fHandler;
@"NSOperationQueue" fHandlerQueue;
```

## Class methods

```
+[CMMotionActivityManager authorizationStatus];
+[CMMotionActivityManager isActivityAvailable];
+[CMMotionActivityManager isActivityLiteAvailable];
+[CMMotionActivityManager paginateDatesIntoDatesFrom:datesTo:start:end:intervalLength:];
```

## Instance methods

```
-[CMMotionActivityManager stopActivityUpdates];
-[CMMotionActivityManager init];
-[CMMotionActivityManager dealloc];
-[CMMotionActivityManager stopActivityLiteUpdates];
-[CMMotionActivityManager startActivityLiteUpdatesToQueue:withHandler:];
-[CMMotionActivityManager stopPeriodicActivityUpdates];
-[CMMotionActivityManager startPeriodicActivityUpdatesToQueue:withHandler:];
-[CMMotionActivityManager startActivityUpdatesToQueue:withHandler:];
-[CMMotionActivityManager _handleQueryResponse:onQueue:withHandler:];
-[CMMotionActivityManager queryActivityWithAttribute:fromDate:toDate:toQueue:withHandler:];
-[CMMotionActivityManager queryActivityStartingFromDate:toDate:toQueue:withHandler:];
-[CMMotionActivityManager filterActivities:withAttribute:];
```
