# `FigCoreTelephonyServiceConnection`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientDataDelegate`
- 8 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _doomTimer;
^{__CTServerConnection=} _ctServerConnection;
@"CoreTelephonyClient" _ctClient;
@"CTDataStatusBasic" _ctDataStatus;
{OpaqueFigCoreTelephonyStatus="hasHighSpeedHighPower"C} _currentStatus;
{FigCoreTelephonyMonitorListHead="stqh_first"^{FigCoreTelephonyMonitorCallbackEntry}"stqh_last"^^{FigCoreTelephonyMonitorCallbackEntry}} _callbackEntries;
^{__CFAllocator=} _allocator;
```

## Properties

```
@property (T{OpaqueFigCoreTelephonyStatus=C},R,N) currentStatus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCoreTelephonyServiceConnection sharedInstance];
```

## Instance methods

```
-[FigCoreTelephonyServiceConnection currentStatus];
-[FigCoreTelephonyServiceConnection init];
-[FigCoreTelephonyServiceConnection deregisterListener:];
-[FigCoreTelephonyServiceConnection processDataStatusBasic:];
-[FigCoreTelephonyServiceConnection dealloc];
-[FigCoreTelephonyServiceConnection registerListener:callback:queue:];
-[FigCoreTelephonyServiceConnection internetDataStatusBasic:];
-[FigCoreTelephonyServiceConnection _teardownConnection];
-[FigCoreTelephonyServiceConnection _setupConnection];
-[FigCoreTelephonyServiceConnection _handleCTNotification:notificationInfo:];
```
