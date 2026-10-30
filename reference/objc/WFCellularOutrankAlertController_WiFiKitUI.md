# `WFCellularOutrankAlertController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFPromptAlertController`
- 2 instance variables, 2 properties, 4 instance methods, 5 class methods

## Instance variables

```
@"NSString" _cancelButtonTitle;
@"NSString" _defaultButtonTitle;
```

## Properties

```
@property (T@"NSString",C,N,V_cancelButtonTitle) cancelButtonTitle;
@property (T@"NSString",C,N,V_defaultButtonTitle) defaultButtonTitle;
```

## Class methods

```
+[WFCellularOutrankAlertController cancelButtonTitleForPrivateCellular:];
+[WFCellularOutrankAlertController cellularOutrankAlertControllerWithNetworkName:chinaDevice:privateCellular:completionHandler:];
+[WFCellularOutrankAlertController defaultButtonTitleForChinaDevice:];
+[WFCellularOutrankAlertController messageForChinaDevice:privateCellular:];
+[WFCellularOutrankAlertController titleForNetworkName:chinaDevice:privateCellular:];
```

## Instance methods

```
-[WFCellularOutrankAlertController setDefaultButtonTitle:];
-[WFCellularOutrankAlertController defaultButtonTitle];
-[WFCellularOutrankAlertController cancelButtonTitle];
-[WFCellularOutrankAlertController setCancelButtonTitle:];
```
