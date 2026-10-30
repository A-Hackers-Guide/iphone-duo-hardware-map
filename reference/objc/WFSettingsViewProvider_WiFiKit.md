# `WFSettingsViewProvider`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFNetworkViewProvider`
- 2 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _credentialsViewControllerMap;
@"WFSettingsController" _settingsController;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_credentialsViewControllerMap) credentialsViewControllerMap;
@property (T@"WFSettingsController",&,N,V_settingsController) settingsController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFSettingsViewProvider init];
-[WFSettingsViewProvider credentialsViewControllerWithContext:];
-[WFSettingsViewProvider networkErrorViewControllerWithContext:];
-[WFSettingsViewProvider certificateViewControllerWithContext:];
-[WFSettingsViewProvider networkDetailsViewControllerWithContext:];
-[WFSettingsViewProvider setSettingsController:];
-[WFSettingsViewProvider settingsController];
-[WFSettingsViewProvider didDismissNetworkViewController:forContext:];
-[WFSettingsViewProvider credentialsViewControllerMap];
-[WFSettingsViewProvider otherNetworkViewControllerWithContext:appearanceProxy:];
-[WFSettingsViewProvider setCredentialsViewControllerMap:];
```
