# `SFAnalyticsActivityTracker`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _name;
# _clientClass;
Q _start;
B _canceled;
@"NSNumber" _measurement;
```

## Properties

```
@property (T@"NSNumber",&,V_measurement) measurement;
```

## Instance methods

```
-[SFAnalyticsActivityTracker performAction:];
-[SFAnalyticsActivityTracker stop];
-[SFAnalyticsActivityTracker dealloc];
-[SFAnalyticsActivityTracker start];
-[SFAnalyticsActivityTracker cancel];
-[SFAnalyticsActivityTracker measurement];
-[SFAnalyticsActivityTracker setMeasurement:];
-[SFAnalyticsActivityTracker initWithName:clientClass:];
-[SFAnalyticsActivityTracker stopWithEvent:result:];
```
