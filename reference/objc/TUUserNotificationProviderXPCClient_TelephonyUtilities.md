# `TUUserNotificationProviderXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUUserNotificationsProviderXPCServer`, `TUUserNotificationProviderDataSource`
- 2 instance variables, 6 properties, 8 instance methods, 5 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _xpcConnection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUUserNotificationProviderXPCClient setAsynchronousServer:];
+[TUUserNotificationProviderXPCClient asynchronousServer];
+[TUUserNotificationProviderXPCClient setSynchronousServer:];
+[TUUserNotificationProviderXPCClient synchronousServer];
+[TUUserNotificationProviderXPCClient userNotificationProviderServerXPCInterface];
```

## Instance methods

```
-[TUUserNotificationProviderXPCClient synchronousServerWithErrorHandler:];
-[TUUserNotificationProviderXPCClient init];
-[TUUserNotificationProviderXPCClient setXpcConnection:];
-[TUUserNotificationProviderXPCClient dealloc];
-[TUUserNotificationProviderXPCClient queue];
-[TUUserNotificationProviderXPCClient xpcConnection];
-[TUUserNotificationProviderXPCClient serverWithErrorHandler:];
-[TUUserNotificationProviderXPCClient momentCapturedForStreamToken:requesterID:reply:];
```
