# `BCUIBatteryAvocadoViewController`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BCBatteryDeviceObserving`
- 6 instance variables, 8 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"BCBatteryDeviceController" _batteryDeviceController;
@"NSObject<OS_dispatch_queue>" _queue;
q _widgetFamily;
d _scaleFactor;
@"NSString" _debugIdentifier;
@"BCUIAvocadoViewController" _avocadoViewController;
```

## Properties

```
@property (T@"BCUIAvocadoViewController",&,N,G_avocadoViewController,S_setAvocadoViewController:,V_avocadoViewController) avocadoViewController;
@property (Tq,N,V_widgetFamily) widgetFamily;
@property (Td,N,V_scaleFactor) scaleFactor;
@property (T@"NSString",C,N,V_debugIdentifier) debugIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BCUIBatteryAvocadoViewController initialize];
+[BCUIBatteryAvocadoViewController imageForIconInfo:];
```

## Instance methods

```
-[BCUIBatteryAvocadoViewController setDebugIdentifier:];
-[BCUIBatteryAvocadoViewController debugIdentifier];
-[BCUIBatteryAvocadoViewController viewWillDisappear:];
-[BCUIBatteryAvocadoViewController setScaleFactor:];
-[BCUIBatteryAvocadoViewController viewDidLoad];
-[BCUIBatteryAvocadoViewController viewWillAppear:];
-[BCUIBatteryAvocadoViewController _canShowWhileLocked];
-[BCUIBatteryAvocadoViewController viewDidAppear:];
-[BCUIBatteryAvocadoViewController scaleFactor];
-[BCUIBatteryAvocadoViewController viewWillLayoutSubviews];
-[BCUIBatteryAvocadoViewController connectedDevicesDidChange:];
-[BCUIBatteryAvocadoViewController viewDidDisappear:];
-[BCUIBatteryAvocadoViewController setWidgetFamily:];
-[BCUIBatteryAvocadoViewController widgetFamily];
-[BCUIBatteryAvocadoViewController _avocadoViewController];
-[BCUIBatteryAvocadoViewController _configureAvocadoViewControllerIfNecessary];
-[BCUIBatteryAvocadoViewController _setAvocadoViewController:];
-[BCUIBatteryAvocadoViewController _synthesizedDebugIdentifier];
-[BCUIBatteryAvocadoViewController setWidgetFamliy:];
```
