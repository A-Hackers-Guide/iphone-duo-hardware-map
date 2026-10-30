# `NCUserAlertActionRunner`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NCNotificationActionRunner`
- 2 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _shouldForwardAction;
@"SBAlertItem" _alertItem;
```

## Properties

```
@property (T@"SBAlertItem",R,W,N,V_alertItem) alertItem;
@property (TB,N,V_shouldForwardAction) shouldForwardAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NCUserAlertActionRunner alertItem];
-[NCUserAlertActionRunner executeAction:fromOrigin:endpoint:withParameters:completion:];
-[NCUserAlertActionRunner setShouldForwardAction:];
-[NCUserAlertActionRunner shouldForwardAction];
-[NCUserAlertActionRunner initWithSBAlertItem:];
```
