# `CAMKeyValueCoalescer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
d __interval;
@? __handler;
@"NSObject<OS_dispatch_source>" _coalescingTimer;
@"NSMutableDictionary" __values;
@"NSMutableDictionary" __previousValues;
@"NSObject<OS_dispatch_queue>" __coalescingQueue;
```

## Properties

```
@property (Td,R,N,V__interval) _interval;
@property (T@?,R,C,N,V__handler) _handler;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_coalescingTimer) coalescingTimer;
@property (T@"NSMutableDictionary",R,N,V__values) _values;
@property (T@"NSMutableDictionary",R,N,V__previousValues) _previousValues;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__coalescingQueue) _coalescingQueue;
```

## Instance methods

```
-[CAMKeyValueCoalescer flush];
-[CAMKeyValueCoalescer setCoalescingTimer:];
-[CAMKeyValueCoalescer _values];
-[CAMKeyValueCoalescer coalescingTimer];
-[CAMKeyValueCoalescer _handler];
-[CAMKeyValueCoalescer _previousValues];
-[CAMKeyValueCoalescer _coalescingQueue];
-[CAMKeyValueCoalescer _interval];
-[CAMKeyValueCoalescer _pushCoalescedValues];
-[CAMKeyValueCoalescer coalesceValue:forKeyPath:];
-[CAMKeyValueCoalescer initWithInterval:handler:];
```
