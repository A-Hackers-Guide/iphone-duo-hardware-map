# `UIStatusBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBar_Base`
- Protocols: `UIStatusBarServerClient`
- 24 instance variables, 1 properties, 100 instance methods, 17 class methods

## Instance variables

```
B _showsForeground;
B _observingDefaults;
@"UIStatusBarBackgroundView" _backgroundView;
@"UIStatusBarForegroundView" _foregroundView;
@"UILabel" _doubleHeightLabel;
@"UIView" _doubleHeightLabelContainer;
@"NSString" _currentDoubleHeightText;
{?="itemIsEnabled"[46B]"timeString"[64c]"shortTimeString"[64c]"dateString"[256c]"gsmSignalStrengthRaw"i"secondaryGsmSignalStrengthRaw"i"gsmSignalStrengthBars"i"secondaryGsmSignalStrengthBars"i"serviceString"[100c]"secondaryServiceString"[100c]"serviceCrossfadeString"[100c]"secondaryServiceCrossfadeString"[100c]"serviceImages"[2[100c]]"operatorDirectory"[1024c]"serviceContentType"I"secondaryServiceContentType"I"cellLowDataModeActive"b1"secondaryCellLowDataModeActive"b1"wifiSignalStrengthRaw"i"wifiSignalStrengthBars"i"wifiLowDataModeActive"b1"dataNetworkType"I"secondaryDataNetworkType"I"batteryCapacity"i"batteryState"I"batteryDetailString"[150c]"bluetoothBatteryCapacity"i"thermalColor"i"thermalSunlightMode"b1"slowActivity"b1"syncActivity"b1"activityDisplayId"[256c]"bluetoothConnected"b1"displayRawGSMSignal"b1"displayRawWifiSignal"b1"locationIconType"b2"voiceControlIconType"b2"quietModeInactive"b1"tetheringConnectionCount"I"batterySaverModeActive"b1"deviceIsRTL"b1"lock"b1"breadcrumbTitle"[256c]"breadcrumbSecondaryTitle"[256c]"personName"[100c]"electronicTollCollectionAvailable"b1"radarAvailable"b1"announceNotificationsAvailable"b1"wifiLinkWarning"b1"wifiSearching"b1"backgroundActivityDisplayStartDate"d"shouldShowEmergencyOnlyStatus"b1"emergencyOnly"b1"secondaryCellularConfigured"b1"primaryServiceBadgeString"[100c]"secondaryServiceBadgeString"[100c]"quietModeImage"[256c]"quietModeName"[256c]"serviceSuffixString"[100c]"secondaryServiceSuffixString"[100c]"numberSharingState"b2"secondaryNumberSharingState"b2"localNetworkType"I"localNetworkName"[100c]} _currentRawData;
@"NSMutableArray" _interruptedAnimationCompositeViews;
@"UIStatusBarBackgroundView" _newStyleBackgroundView;
@"UIStatusBarForegroundView" _newStyleForegroundView;
@"UIStatusBar" _slidingStatusBar;
@"UIStatusBarStyleAttributes" _styleAttributes;
B _waitingOnCallbackAfterChangingStyleOverridesLocally;
B _showOnlyCenterItems;
B _foregroundViewShouldIgnoreStatusBarDataDuringAnimation;
@"UIColor" _tintColor;
@"UIColor" _lastUsedBackgroundColor;
@"UIStatusBarStyleAnimationParameters" _nextTintTransition;
@"NSNumber" _overrideHeight;
@"NSMutableSet" _disableRasterizationReasons;
@"NSMutableDictionary" _actions;
B _disablesRasterization;
B _timeHidden;
```

## Properties

```
@property (TB,N,GisTimeHidden,V_timeHidden) timeHidden;
```

## Class methods

```
+[UIStatusBar _heightForStyle:orientation:forStatusBarFrame:inWindow:isAzulBLinked:];
+[UIStatusBar lowBatteryLevel];
+[UIStatusBar _deviceUserInterfaceLayoutDirection];
+[UIStatusBar _isLightContentStyle:];
+[UIStatusBar _newStyleAttributesForRequest:];
+[UIStatusBar _regularPadBaselineOffset];
+[UIStatusBar _regularPadEdgeInsets];
+[UIStatusBar _roundedPadBaselineOffset];
+[UIStatusBar _roundedPadEdgeInsets];
+[UIStatusBar _setDeviceUserInterfaceLayoutDirection:];
+[UIStatusBar _shouldForwardToImplementationClassForStyle:];
+[UIStatusBar _styleAttributesForRequest:];
+[UIStatusBar _styleAttributesForStatusBarStyle:];
+[UIStatusBar _viewControllerAdjustmentForOrientation:inWindow:];
+[UIStatusBar defaultStyleForRequestedStyle:styleOverrides:];
+[UIStatusBar enumerateStatusBarStyleOverridesWithBlock:];
+[UIStatusBar getData:forRequestedData:withOverrides:];
```

## Instance methods

```
-[UIStatusBar forceUpdate:];
-[UIStatusBar frameForPartWithIdentifier:];
-[UIStatusBar setOrientation:];
-[UIStatusBar setEnabledPartIdentifiers:];
-[UIStatusBar jiggleLockIcon];
-[UIStatusBar currentStyle];
-[UIStatusBar disabledPartIdentifiers];
-[UIStatusBar touchesEnded:withEvent:];
-[UIStatusBar setForegroundColor:animationParameters:];
-[UIStatusBar setRegistered:];
-[UIStatusBar observeValueForKeyPath:ofObject:change:context:];
-[UIStatusBar _shouldReverseLayoutDirection];
-[UIStatusBar defaultHeight];
-[UIStatusBar _didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UIStatusBar actionForPartWithIdentifier:];
-[UIStatusBar setAction:forPartWithIdentifier:];
-[UIStatusBar dealloc];
-[UIStatusBar statusBarServer:didReceiveGlowAnimationState:forStyle:];
-[UIStatusBar layoutSubviews];
-[UIStatusBar _requestStyle:partStyles:animationParameters:forced:];
-[UIStatusBar forceUpdateData:];
-[UIStatusBar _backgroundView];
-[UIStatusBar setForegroundAlpha:animationParameters:];
-[UIStatusBar _setStyle:];
-[UIStatusBar setTintColor:];
-[UIStatusBar isTranslucent];
-[UIStatusBar statusBarServer:didReceiveDoubleHeightStatusString:forStyle:];
-[UIStatusBar setDisabledPartIdentifiers:];
-[UIStatusBar statusBarServer:didReceiveStatusBarData:withActions:];
-[UIStatusBar pointInside:withEvent:];
-[UIStatusBar statusBarWindow];
-[UIStatusBar statusBarServer:didReceiveStyleOverrides:];
-[UIStatusBar setStyleRequest:animationParameters:];
-[UIStatusBar setLegibilityStyle:animationParameters:];
-[UIStatusBar statusBarStateProvider:didPostStatusBarData:withActions:];
-[UIStatusBar enabledPartIdentifiers];
-[UIStatusBar _initWithFrame:showForegroundView:wantsServer:inProcessStateProvider:];
-[UIStatusBar defaultDoubleHeight];
-[UIStatusBar _slideTransform];
-[UIStatusBar setEnabledCenterItems:duration:];
-[UIStatusBar setSuppressesHiddenSideEffects:];
-[UIStatusBar setPersistentAnimationsEnabled:];
-[UIStatusBar _adjustDoubleHeightTextVisibility];
-[UIStatusBar _backgroundFrameForAttributes:];
-[UIStatusBar _beginDisablingRasterizationForReason:];
-[UIStatusBar _clearOverrideHeight];
-[UIStatusBar _crossfadeToNewBackgroundView];
-[UIStatusBar _crossfadeToNewForegroundViewWithAlpha:];
-[UIStatusBar _currentComposedData];
-[UIStatusBar _currentComposedDataForStyle:];
-[UIStatusBar _currentStyleAttributes];
-[UIStatusBar _dateTimePreferencesUpdated];
-[UIStatusBar _doubleHeightStatusStringForStyle:];
-[UIStatusBar _endDisablingRasterizationForReason:];
-[UIStatusBar _finishedSettingStyleWithOldHeight:newHeight:animation:];
-[UIStatusBar _isTransparent];
-[UIStatusBar _itemViewPerformButtonAction:];
-[UIStatusBar _itemViewShouldBeginDisablingRasterization:];
-[UIStatusBar _itemViewShouldEndDisablingRasterization:];
-[UIStatusBar _noteStyleOverridesChangedLocally];
-[UIStatusBar _performBlockWhileIgnoringForegroundViewChanges:];
-[UIStatusBar _prepareInterruptedAnimationCompositeViewIncludingForeground:];
-[UIStatusBar _prepareToSetStyle:animation:forced:];
-[UIStatusBar _rectIntersectsTimeItem:];
-[UIStatusBar _setDisablesRasterization:];
-[UIStatusBar _setDoubleHeightStatusString:];
-[UIStatusBar _setFrameForStyle:];
-[UIStatusBar _setOverrideHeight:];
-[UIStatusBar _setStyle:animation:];
-[UIStatusBar _setVisualAltitude:];
-[UIStatusBar _setVisualAltitudeBias:];
-[UIStatusBar _shouldSeekHigherPriorityTouchTarget];
-[UIStatusBar _shouldUseInProcessProviderDoubleHeightStatusString];
-[UIStatusBar _statusBarDidAnimateRotation];
-[UIStatusBar _statusBarWillAnimateRotation];
-[UIStatusBar _styleAttributesForRequest:];
-[UIStatusBar _swapToNewBackgroundView];
-[UIStatusBar _swapToNewForegroundView];
-[UIStatusBar _touchShouldProduceReturnEvent];
-[UIStatusBar _updateBackgroundFrame];
-[UIStatusBar _updatePersistentAnimationsEnabledForForegroundView:];
-[UIStatusBar _updateShouldRasterize];
-[UIStatusBar _updateUIWithStyleAttributes:animationParameters:];
-[UIStatusBar _updateUIWithStyleAttributes:animationParameters:forced:];
-[UIStatusBar animateUnlock];
-[UIStatusBar currentStyleRequestForStyle:];
-[UIStatusBar disablesRasterization];
-[UIStatusBar forceUpdateDoubleHeightStatus];
-[UIStatusBar forceUpdateToData:animated:];
-[UIStatusBar forgetEitherSideHistory];
-[UIStatusBar frameForOrientation:];
-[UIStatusBar heightForOrientation:];
-[UIStatusBar isDoubleHeight];
-[UIStatusBar isTimeHidden];
-[UIStatusBar requestStyle:animation:startTime:duration:curve:];
-[UIStatusBar setShowsOnlyCenterItems:];
-[UIStatusBar setTimeHidden:];
-[UIStatusBar setTintColor:withDuration:];
-[UIStatusBar statusBarStateProvider:didChangeDoubleHeightStatusStringForStyle:];
-[UIStatusBar styleRequest];
```
