# `SBWalletNotificationSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NCNotificationSource`
- 1 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NCNotificationDispatcher" _dispatcher;
```

## Properties

```
@property (T@"NCNotificationDispatcher",&,N,V_dispatcher) dispatcher;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWalletNotificationSource dispatcher];
-[SBWalletNotificationSource setDispatcher:];
-[SBWalletNotificationSource initWithDispatcher:];
-[SBWalletNotificationSource modifyNotificationRequestForCardItem:];
-[SBWalletNotificationSource postNotificationRequestForCardItem:];
-[SBWalletNotificationSource withdrawNotificationRequestForCardItem:];
```
