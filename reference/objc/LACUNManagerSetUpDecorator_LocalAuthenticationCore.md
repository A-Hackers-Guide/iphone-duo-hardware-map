# `LACUNManagerSetUpDecorator`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDarwinNotificationCenterObserver`, `LACUNManager`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _builderLock;
@"<LACUNManagerDelegate>" _delegate;
@? _responderBuilder;
@"<LACUNManager>" _responder;
@"<LACSetUpStateProvider>" _setupStateProvider;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACUNManagerDelegate>",W,N) delegate;
```

## Instance methods

```
-[LACUNManagerSetUpDecorator dealloc];
-[LACUNManagerSetUpDecorator responder];
-[LACUNManagerSetUpDecorator setDelegate:];
-[LACUNManagerSetUpDecorator delegate];
-[LACUNManagerSetUpDecorator _setupResponder];
-[LACUNManagerSetUpDecorator _registerNotificationObservers];
-[LACUNManagerSetUpDecorator cancelAllNotificationsWithCompletion:];
-[LACUNManagerSetUpDecorator cancelNotificationsWithIdentifiers:scheduledOnly:completion:];
-[LACUNManagerSetUpDecorator initWithManagerBuilder:];
-[LACUNManagerSetUpDecorator initWithManagerBuilder:setupStateProvider:];
-[LACUNManagerSetUpDecorator notificationCenter:didReceiveNotification:];
-[LACUNManagerSetUpDecorator postNotification:completion:];
```
