# `BKUIAlertView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 8 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"UIAlertController" _alertController;
d _alertHudTextStartTime;
@ _parent;
: _cancelButtonSelector;
: _otherButtonSelector;
@"UIView" _alertHudView;
@"UILabel" _alertHudText;
d _alertHudTimeout;
d _alertHudMinDisplayTime;
@"NSObject<OS_os_log>" _log;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (T@,W,N,V_parent) parent;
@property (T:,N,V_cancelButtonSelector) cancelButtonSelector;
@property (T:,N,V_otherButtonSelector) otherButtonSelector;
@property (T@"UIView",W,N,V_alertHudView) alertHudView;
@property (T@"UILabel",W,N,V_alertHudText) alertHudText;
@property (Td,N,V_alertHudTimeout) alertHudTimeout;
@property (Td,N,V_alertHudMinDisplayTime) alertHudMinDisplayTime;
```

## Instance methods

```
-[BKUIAlertView setLog:];
-[BKUIAlertView setParent:];
-[BKUIAlertView init];
-[BKUIAlertView _init];
-[BKUIAlertView parent];
-[BKUIAlertView log];
-[BKUIAlertView hideAnimated:];
-[BKUIAlertView alertHudTimeout];
-[BKUIAlertView _hideAlertHudView];
-[BKUIAlertView _setFadeAnimation:];
-[BKUIAlertView alertHudMinDisplayTime];
-[BKUIAlertView alertHudText];
-[BKUIAlertView alertHudView];
-[BKUIAlertView cancelButtonSelector];
-[BKUIAlertView isAlertHidden];
-[BKUIAlertView otherButtonSelector];
-[BKUIAlertView setAlertHudMinDisplayTime:];
-[BKUIAlertView setAlertHudText:];
-[BKUIAlertView setAlertHudTimeout:];
-[BKUIAlertView setAlertHudView:];
-[BKUIAlertView setCancelButtonSelector:];
-[BKUIAlertView setOtherButtonSelector:];
-[BKUIAlertView show:message:cancelButtonTitle:viewController:];
-[BKUIAlertView show:title:message:cancelButtonTitle:cancelButtonSelector:otherButtonTitle:otherButtonSelector:viewController:];
-[BKUIAlertView show:title:message:cancelButtonTitle:cancelButtonSelector:viewController:];
-[BKUIAlertView showAlert:message:cancelButtonTitle:otherButtonTitle:viewController:];
```
