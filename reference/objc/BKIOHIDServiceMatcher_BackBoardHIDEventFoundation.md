# `BKIOHIDServiceMatcher`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 14 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BKSHIDEventSenderDescriptor" _senderDescriptor;
B _observeSynchronously;
B _startedMatching;
B _dataProviderSupportsHoisting;
B _dataProviderSupportsSessionHoisting;
I _sessionID;
AB _invalidated;
q _matcherID;
@"NSDictionary" _matchingDictionary;
# _serviceClass;
@"<BKIOHIDServiceMatchObserver>" _observer;
@"NSObject<OS_dispatch_queue>" _observerQueue;
@"<BKIOHIDServiceMatcherDataProviding>" _dataProvider;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKIOHIDServiceMatcher setSessionID:];
-[BKIOHIDServiceMatcher dealloc];
-[BKIOHIDServiceMatcher invalidate];
-[BKIOHIDServiceMatcher _expectDeallocation];
-[BKIOHIDServiceMatcher _servicesForIOHIDServiceRefs:];
-[BKIOHIDServiceMatcher existingServices];
-[BKIOHIDServiceMatcher initWithMatchingDictionary:dataProvider:];
-[BKIOHIDServiceMatcher initWithMatchingDictionary:serviceClass:dataProvider:];
-[BKIOHIDServiceMatcher initWithSenderDescriptor:dataProvider:];
-[BKIOHIDServiceMatcher initWithUsagePage:usage:builtIn:dataProvider:];
-[BKIOHIDServiceMatcher startObserving:queue:];
-[BKIOHIDServiceMatcher startObservingSynchronously:];
```
