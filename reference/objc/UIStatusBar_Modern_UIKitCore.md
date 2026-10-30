# `UIStatusBar_Modern`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBar_Base`
- 1 instance variables, 1 properties, 41 instance methods, 7 class methods

## Instance variables

```
@"_UIStatusBar" _statusBar;
```

## Properties

```
@property (T@"_UIStatusBar",&,N,V_statusBar) statusBar;
```

## Class methods

```
+[UIStatusBar_Modern _implementationClass];
+[UIStatusBar_Modern setSensorActivityIndicator:];
+[UIStatusBar_Modern registerSensorActivityIndicator:forScreen:];
+[UIStatusBar_Modern sensorActivityIndicator];
+[UIStatusBar_Modern _defaultStyleForRequestedStyle:styleOverrides:activeStyleOverride:];
+[UIStatusBar_Modern sensorActivityIndicatorForScreen:];
+[UIStatusBar_Modern _heightForStyle:orientation:forStatusBarFrame:inWindow:isAzulBLinked:];
```

## Instance methods

```
-[UIStatusBar_Modern alphaForPartWithIdentifier:];
-[UIStatusBar_Modern forceUpdate:];
-[UIStatusBar_Modern frameForPartWithIdentifier:];
-[UIStatusBar_Modern setOffset:forPartWithIdentifier:];
-[UIStatusBar_Modern setOrientation:];
-[UIStatusBar_Modern setEnabledPartIdentifiers:];
-[UIStatusBar_Modern jiggleLockIcon];
-[UIStatusBar_Modern currentStyle];
-[UIStatusBar_Modern disabledPartIdentifiers];
-[UIStatusBar_Modern statusBar];
-[UIStatusBar_Modern setForegroundColor:animationParameters:];
-[UIStatusBar_Modern intrinsicContentSize];
-[UIStatusBar_Modern setStatusBar:];
-[UIStatusBar_Modern _requestStyle:partStyles:legibilityStyle:foregroundColor:animationParameters:forced:];
-[UIStatusBar_Modern actionForPartWithIdentifier:];
-[UIStatusBar_Modern setAction:forPartWithIdentifier:];
-[UIStatusBar_Modern layoutSubviews];
-[UIStatusBar_Modern _updateWithData:force:];
-[UIStatusBar_Modern _requestStyle:partStyles:animationParameters:forced:];
-[UIStatusBar_Modern forceUpdateData:];
-[UIStatusBar_Modern setAlpha:forPartWithIdentifier:];
-[UIStatusBar_Modern setMode:];
-[UIStatusBar_Modern setForegroundAlpha:animationParameters:];
-[UIStatusBar_Modern offsetForPartWithIdentifier:];
-[UIStatusBar_Modern setAvoidanceFrame:animationSettings:options:];
-[UIStatusBar_Modern _dataFromLegacyData:];
-[UIStatusBar_Modern _updateSemanticContentAttributeFromLegacyData:];
-[UIStatusBar_Modern statusBarServer:didReceiveDoubleHeightStatusString:forStyle:];
-[UIStatusBar_Modern setDisabledPartIdentifiers:];
-[UIStatusBar_Modern statusBarServer:didReceiveStatusBarData:withActions:];
-[UIStatusBar_Modern clockFont];
-[UIStatusBar_Modern _implicitStyleOverrideForStyle:];
-[UIStatusBar_Modern _effectiveStyleFromStyle:];
-[UIStatusBar_Modern statusBarServer:didReceiveStyleOverrides:];
-[UIStatusBar_Modern setStyleRequest:animationParameters:];
-[UIStatusBar_Modern setLegibilityStyle:animationParameters:];
-[UIStatusBar_Modern statusBarStateProvider:didPostStatusBarData:withActions:];
-[UIStatusBar_Modern enabledPartIdentifiers];
-[UIStatusBar_Modern _initWithFrame:showForegroundView:wantsServer:inProcessStateProvider:];
-[UIStatusBar_Modern defaultDoubleHeight];
-[UIStatusBar_Modern _effectiveDataFromData:activeOverride:canUpdateBackgroundActivity:];
```
