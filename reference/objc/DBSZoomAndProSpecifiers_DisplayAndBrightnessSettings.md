# `DBSZoomAndProSpecifiers`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _specifiers;
@"PSSpecifier" _advancedSpecifier;
@"<DBSZoomAndProSpecifiersDelegate>" _delegate;
```

## Properties

```
@property (T@"<DBSZoomAndProSpecifiersDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,N) specifiers;
@property (T@"PSSpecifier",R,N,V_advancedSpecifier) advancedSpecifier;
```

## Class methods

```
+[DBSZoomAndProSpecifiers removeSpecifiersFrom:];
+[DBSZoomAndProSpecifiers specifiersPresentIn:];
```

## Instance methods

```
-[DBSZoomAndProSpecifiers setDelegate:];
-[DBSZoomAndProSpecifiers delegate];
-[DBSZoomAndProSpecifiers specifiers];
-[DBSZoomAndProSpecifiers _dimWindowBeforeRestart];
-[DBSZoomAndProSpecifiers _displayEdgeCompensationConfirmationDictForEnable:];
-[DBSZoomAndProSpecifiers _displayEdgeCompensationGroupSpecifier];
-[DBSZoomAndProSpecifiers _displayEdgeCompensationSpecifier];
-[DBSZoomAndProSpecifiers _restartRenderServerForDisplayEdgeCompensation];
-[DBSZoomAndProSpecifiers _userDidCancelDisplayEdgeCompensationWithSpecifier:];
-[DBSZoomAndProSpecifiers _userDidConfirmDisplayEdgeCompensationWithSpecifier:];
-[DBSZoomAndProSpecifiers _writeDisplayEdgeCompensationEnabled:];
-[DBSZoomAndProSpecifiers advancedDetailString:];
-[DBSZoomAndProSpecifiers advancedSpecifier];
-[DBSZoomAndProSpecifiers displayEdgeCompensationAvailable];
-[DBSZoomAndProSpecifiers displayZoomFooterText];
-[DBSZoomAndProSpecifiers isDisplayEdgeCompensationEnabled:];
-[DBSZoomAndProSpecifiers localizedMagnifyModeName];
-[DBSZoomAndProSpecifiers presentModalMagnifyController];
-[DBSZoomAndProSpecifiers setDisplayEdgeCompensationEnabled:specifier:];
```
