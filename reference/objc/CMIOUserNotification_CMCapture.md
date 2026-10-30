# `CMIOUserNotification`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMCaptureUserNotification`
- 6 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_group>" _responseGroup;
Q _response;
@"NSObject<OS_xpc_object>" _userNotificationServiceConnection;
B _responseIsValid;
B _connectionIsValid;
```

## Instance methods

```
-[CMIOUserNotification _handleXPCEvent:];
-[CMIOUserNotification dealloc];
-[CMIOUserNotification cancel];
-[CMIOUserNotification _closeConnection];
-[CMIOUserNotification _createOrUpdate:withTimeout:flags:dictionary:];
-[CMIOUserNotification asyncResponse:block:];
-[CMIOUserNotification initNotificationWithTimeout:flags:dictionary:error:];
-[CMIOUserNotification receiveResponseWithTimeout:error:];
-[CMIOUserNotification updateWithTimeout:flags:dictionary:];
```
