# `SBRemoveWidgetAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertItem`
- 4 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<SBLeafIconDataSource>" _widget;
@"SBWidgetIcon" _icon;
@"NSString" _iconLocation;
@"SBHIconManager" _iconManager;
```

## Properties

```
@property (T@"<SBLeafIconDataSource>",&,N,V_widget) widget;
@property (T@"SBWidgetIcon",&,N,V_icon) icon;
@property (T@"NSString",&,N,V_iconLocation) iconLocation;
@property (T@"SBHIconManager",W,N,V_iconManager) iconManager;
```

## Instance methods

```
-[SBRemoveWidgetAlertItem iconManager];
-[SBRemoveWidgetAlertItem setWidget:];
-[SBRemoveWidgetAlertItem widget];
-[SBRemoveWidgetAlertItem setIcon:];
-[SBRemoveWidgetAlertItem dismissOnLock];
-[SBRemoveWidgetAlertItem setIconLocation:];
-[SBRemoveWidgetAlertItem configure:requirePasscodeForActions:];
-[SBRemoveWidgetAlertItem forcesModalAlertAppearance];
-[SBRemoveWidgetAlertItem shouldShowInLockScreen];
-[SBRemoveWidgetAlertItem iconLocation];
-[SBRemoveWidgetAlertItem icon];
-[SBRemoveWidgetAlertItem setIconManager:];
-[SBRemoveWidgetAlertItem didActivate];
-[SBRemoveWidgetAlertItem initWithWidget:inIcon:location:iconManager:];
-[SBRemoveWidgetAlertItem initWithWidgetIcon:location:iconManager:];
```
