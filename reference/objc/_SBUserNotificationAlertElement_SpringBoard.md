# `_SBUserNotificationAlertElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertProvidedContentElement`
- Protocols: `SBSystemApertureContextProviding`
- 3 instance variables, 13 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<SAAlertHosting>" _alertHost;
B _preventsAutomaticDismissal;
@"UIColor" _keyColor;
```

## Properties

```
@property (T@"UIColor",&,N,V_keyColor) keyColor;
@property (TB,N,V_preventsAutomaticDismissal) preventsAutomaticDismissal;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBUserNotificationAlertElement keyColor];
-[_SBUserNotificationAlertElement setKeyColor:];
-[_SBUserNotificationAlertElement preventsAutomaticDismissal];
-[_SBUserNotificationAlertElement setAlertHost:];
-[_SBUserNotificationAlertElement setPreventsAutomaticDismissal:];
-[_SBUserNotificationAlertElement alertHost];
```
