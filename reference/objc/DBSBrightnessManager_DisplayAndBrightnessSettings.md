# `DBSBrightnessManager`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 21 instance methods, 3 class methods

## Instance variables

```
B _isUpdatingWhiteBalance;
@"CBClient" _brightnessClient;
@"PSListController" _delegate;
@"NSMutableArray" _specifiers;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_specifiers) specifiers;
@property (TB,N,V_isUpdatingWhiteBalance) isUpdatingWhiteBalance;
@property (T@"CBClient",&,N,V_brightnessClient) brightnessClient;
@property (T@"PSListController",W,N,V_delegate) delegate;
```

## Class methods

```
+[DBSBrightnessManager defaultManager];
+[DBSBrightnessManager removeSpecifiersFrom:];
+[DBSBrightnessManager specifiersPresentIn:];
```

## Instance methods

```
-[DBSBrightnessManager init];
-[DBSBrightnessManager dealloc];
-[DBSBrightnessManager setDelegate:];
-[DBSBrightnessManager delegate];
-[DBSBrightnessManager specifiers];
-[DBSBrightnessManager setSpecifiers:];
-[DBSBrightnessManager brightnessClient];
-[DBSBrightnessManager brightnessChangedExternally];
-[DBSBrightnessManager setBrightnessClient:];
-[DBSBrightnessManager backlightValue:];
-[DBSBrightnessManager mainDisplayBrightnessSpecifiers];
-[DBSBrightnessManager _autoWhiteBalanceEnabledDidChange:];
-[DBSBrightnessManager _cleanupTransactionRef];
-[DBSBrightnessManager _generateMainBrightnessSpecifier];
-[DBSBrightnessManager getAutoWhiteBalanceEnabled:];
-[DBSBrightnessManager handleBrightnessChangedExternallyNotification:];
-[DBSBrightnessManager isUpdatingWhiteBalance];
-[DBSBrightnessManager setAutoWhiteBalanceEnabled:forSpecifier:];
-[DBSBrightnessManager setBacklightValue:specifier:];
-[DBSBrightnessManager setIsUpdatingWhiteBalance:];
-[DBSBrightnessManager showAlertToDisableAccessibilityFilters:cancel:];
```
