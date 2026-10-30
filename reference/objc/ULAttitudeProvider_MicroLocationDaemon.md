# `ULAttitudeProvider`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP19MicroLocationDaemon19ULAttitudeProviding_`
- 7 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<ULAttitudeSource>" _attitudeSource;
@"NSObject<OS_dispatch_queue>" _queue;
^{ULAttitudeProviderDelegate=^^?} _delegate;
@"NSDate" _previousStatusUpdateDate;
d _updateInterval;
@"NSMutableArray" _attitudeBuffer;
Q _maxBufferSize;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{ULAttitudeProviderDelegate=^^?},N,V_delegate) delegate;
@property (T@"NSDate",&,N,V_previousStatusUpdateDate) previousStatusUpdateDate;
@property (Td,N,V_updateInterval) updateInterval;
@property (T@"NSMutableArray",&,N,V_attitudeBuffer) attitudeBuffer;
@property (TQ,N,V_maxBufferSize) maxBufferSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ULAttitudeProvider setMaxBufferSize:];
-[ULAttitudeProvider setPreviousStatusUpdateDate:];
-[ULAttitudeProvider queue];
-[ULAttitudeProvider stopUpdates];
-[ULAttitudeProvider setDelegate:];
-[ULAttitudeProvider setUpdateInterval:];
-[ULAttitudeProvider delegate];
-[ULAttitudeProvider previousStatusUpdateDate];
-[ULAttitudeProvider maxBufferSize];
-[ULAttitudeProvider setQueue:];
-[ULAttitudeProvider updateInterval];
-[ULAttitudeProvider startUpdates];
-[ULAttitudeProvider attitudeAtTime:];
-[ULAttitudeProvider attitudeAtGTBTimestamp:];
-[ULAttitudeProvider attitudeBuffer];
-[ULAttitudeProvider didReceiveAttitudeUpdate:withError:];
-[ULAttitudeProvider initWithQueue:delegate:bridgeType:];
-[ULAttitudeProvider setAttitudeBuffer:];
```
