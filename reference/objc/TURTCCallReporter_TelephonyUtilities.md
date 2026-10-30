# `TURTCCallReporter`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _callUUIDToConversation;
@"TUCallCenter" _callCenter;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSMutableDictionary",R,N,V_callUUIDToConversation) callUUIDToConversation;
@property (T@"TUCallCenter",R,N,V_callCenter) callCenter;
```

## Instance methods

```
-[TURTCCallReporter queue];
-[TURTCCallReporter callCenter];
-[TURTCCallReporter callStatusChangedNotification:];
-[TURTCCallReporter callUUIDToConversation];
-[TURTCCallReporter clientName:];
-[TURTCCallReporter initWithCallCenter:];
-[TURTCCallReporter report:withConversation:];
-[TURTCCallReporter reportingSessionForCall:withConversation:];
-[TURTCCallReporter rtcCallInfoDictionary:withConversation:];
-[TURTCCallReporter serviceName:withConversation:];
```
