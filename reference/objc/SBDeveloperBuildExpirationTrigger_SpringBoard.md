# `SBDeveloperBuildExpirationTrigger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppInteractionEventSourceObserving`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBAlertItemsController" _alertItemsController;
@"<SBAppInteractionEventSourceProviding>" _eventSource;
@"NSDate" _expirationDate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeveloperBuildExpirationTrigger dealloc];
-[SBDeveloperBuildExpirationTrigger _coverSheetDidDismiss:];
-[SBDeveloperBuildExpirationTrigger _initWithAlertItemsController:eventSource:expirationDate:];
-[SBDeveloperBuildExpirationTrigger eventSource:didFinishTransitionToMode:withLayoutState:activatingElement:triggeredBy:];
-[SBDeveloperBuildExpirationTrigger initWithAlertItemsController:eventSource:];
-[SBDeveloperBuildExpirationTrigger showDeveloperBuildExpirationAlertIfNecessaryFromLockscreen:toLauncher:];
```
