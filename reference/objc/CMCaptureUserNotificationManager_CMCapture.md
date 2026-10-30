# `CMCaptureUserNotificationManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _flags;
@"NSDictionary" _notificationDictionary;
@"NSNumber" _response;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_group>" _responseGroup;
@"CMCaptureUserNotification" _notification;
Q _notificationCount;
```

## Properties

```
@property (TQ,R,N) flags;
@property (T@"NSDictionary",R,N) notificationDictionary;
@property (T@"NSNumber",&,N) response;
@property (TB,R,N) hasResponse;
@property (TB,R,N) responseWasDefault;
@property (TB,R,N) responseWasAlternate;
@property (TB,R,N) responseWasOther;
@property (TB,R,N) responseWasCancelled;
```

## Instance methods

```
-[CMCaptureUserNotificationManager hasResponse];
-[CMCaptureUserNotificationManager setResponse:];
-[CMCaptureUserNotificationManager flags];
-[CMCaptureUserNotificationManager init];
-[CMCaptureUserNotificationManager dealloc];
-[CMCaptureUserNotificationManager response];
-[CMCaptureUserNotificationManager showNotification];
-[CMCaptureUserNotificationManager waitForResponse];
-[CMCaptureUserNotificationManager _beginNotification:];
-[CMCaptureUserNotificationManager _endNotification];
-[CMCaptureUserNotificationManager asyncResponse:block:];
-[CMCaptureUserNotificationManager cancelNotification];
-[CMCaptureUserNotificationManager notificationDictionary];
-[CMCaptureUserNotificationManager responseWasAlternate];
-[CMCaptureUserNotificationManager responseWasCancelled];
-[CMCaptureUserNotificationManager responseWasDefault];
-[CMCaptureUserNotificationManager responseWasOther];
-[CMCaptureUserNotificationManager setNotificationFlags:andDictionary:];
-[CMCaptureUserNotificationManager waitForResponseUntilTimeout:];
```
