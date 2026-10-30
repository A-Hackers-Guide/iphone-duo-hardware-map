# `SBCardItemsController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCardItemsControllerRemoteInterface`, `NSXPCListenerDelegate`
- 6 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _cardItems;
@"NSMutableArray" _connections;
@"NSXPCListener" _listener;
@"MCProfileConnection" _profileConnection;
B _cardWhileLockedAllowed;
@"SBWalletNotificationSource" _walletNotificationSource;
```

## Properties

```
@property (T@"SBWalletNotificationSource",&,N,V_walletNotificationSource) walletNotificationSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCardItemsController listener:shouldAcceptNewConnection:];
-[SBCardItemsController init];
-[SBCardItemsController dealloc];
-[SBCardItemsController walletNotificationSource];
-[SBCardItemsController getCardItemsForControllerWithIdentifier:withHandler:];
-[SBCardItemsController setCardItems:forControllerWithIdentifier:];
-[SBCardItemsController _activateCardItem:animated:];
-[SBCardItemsController _deactivateCardItem:];
-[SBCardItemsController _updateCardItem:];
-[SBCardItemsController _updateRestrictions];
-[SBCardItemsController _updateThumbnailForCardItem:withSnapshotter:completion:];
-[SBCardItemsController setWalletNotificationSource:];
```
