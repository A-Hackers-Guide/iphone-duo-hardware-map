# `BCUIAvocadoViewController`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 5 instance variables, 6 properties, 19 instance methods, 2 class methods

## Instance variables

```
B _batteryDeviceViewsValid;
@"NSMutableArray" _batteryDeviceViews;
@"NSArray" _batteryDevices;
d _scaleFactor;
@"NSString" _debugIdentifier;
```

## Properties

```
@property (T@"NSMutableArray",R,C,N,G_batteryDeviceViews) batteryDeviceViews;
@property (TQ,R,N,G_maximumNumberOfBatteryDeviceViews) maximumNumberOfBatteryDeviceViews;
@property (TB,R,N,G_includeEmptyDevices) includeEmptyDevices;
@property (T@"NSArray",C,N,V_batteryDevices) batteryDevices;
@property (Td,N,V_scaleFactor) scaleFactor;
@property (T@"NSString",C,N,V_debugIdentifier) debugIdentifier;
```

## Class methods

```
+[BCUIAvocadoViewController initialize];
+[BCUIAvocadoViewController avocadoViewControllerForWidgetFamily:];
```

## Instance methods

```
-[BCUIAvocadoViewController setDebugIdentifier:];
-[BCUIAvocadoViewController debugIdentifier];
-[BCUIAvocadoViewController setScaleFactor:];
-[BCUIAvocadoViewController viewDidLoad];
-[BCUIAvocadoViewController _canShowWhileLocked];
-[BCUIAvocadoViewController scaleFactor];
-[BCUIAvocadoViewController _contentSizeCategoryDidChange:];
-[BCUIAvocadoViewController viewWillLayoutSubviews];
-[BCUIAvocadoViewController _batteryDeviceViews];
-[BCUIAvocadoViewController _columnWidthForBounds:andMaxNumViews:];
-[BCUIAvocadoViewController _configureBatteryDeviceView:withBatteryDevice:transitionCoordinator:];
-[BCUIAvocadoViewController _includeEmptyDevices];
-[BCUIAvocadoViewController _maximumNumberOfBatteryDeviceViews];
-[BCUIAvocadoViewController _newBatteryDeviceView];
-[BCUIAvocadoViewController _synthesizedDebugIdentifier];
-[BCUIAvocadoViewController _validateBatteryDeviceViewsIfNecessary];
-[BCUIAvocadoViewController batteryDevices];
-[BCUIAvocadoViewController invalidateBatteryDeviceState];
-[BCUIAvocadoViewController setBatteryDevices:];
```
