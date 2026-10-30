# `MuxNotificationSink`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSProxy`
- Protocols: `CoreTelephonyClientDelegateProxyInterface`
- 1 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"<MuxNotificationSinkDelegate>" _delegate;
```

## Properties

```
@property (T@"<MuxNotificationSinkDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MuxNotificationSink notificationSink];
```

## Instance methods

```
-[MuxNotificationSink pingWithCompletion:];
-[MuxNotificationSink setDelegate:];
-[MuxNotificationSink delegate];
-[MuxNotificationSink clientDidTriggerFault:];
-[MuxNotificationSink methodSignatureForSelector:];
-[MuxNotificationSink forwardInvocation:];
```
