# `SBUserAlertNotificationSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlertItemsControllerObserver`, `NCNotificationSource`, `SBAlertItemPresenter`
- 2 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NCNotificationDispatcher" _dispatcher;
Q _mode;
```

## Properties

```
@property (T@"NCNotificationDispatcher",&,N,V_dispatcher) dispatcher;
@property (TQ,N,V_mode) mode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUserAlertNotificationSource dispatcher];
-[SBUserAlertNotificationSource alertItemsController:willActivateAlertItem:];
-[SBUserAlertNotificationSource alertItemsController:didActivateAlertItem:];
-[SBUserAlertNotificationSource setDispatcher:];
-[SBUserAlertNotificationSource dealloc];
-[SBUserAlertNotificationSource initWithDispatcher:];
-[SBUserAlertNotificationSource setMode:];
-[SBUserAlertNotificationSource alertItemsController:didDeactivateAlertItem:forReason:];
-[SBUserAlertNotificationSource mode];
-[SBUserAlertNotificationSource _notificationRequestForAlertItem:];
-[SBUserAlertNotificationSource canPresentMultipleAlertItemsSimultaneously];
-[SBUserAlertNotificationSource dismissAlertItem:animated:completion:];
-[SBUserAlertNotificationSource initWithDispatcher:mode:];
-[SBUserAlertNotificationSource presentAlertItem:animated:completion:];
-[SBUserAlertNotificationSource presentsAlertItemsModally];
```
