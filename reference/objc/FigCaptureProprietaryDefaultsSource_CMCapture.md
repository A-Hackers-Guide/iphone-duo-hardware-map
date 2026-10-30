# `FigCaptureProprietaryDefaultsSource`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 22 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _lock;
@"FigCaptureProprietaryDefaults" _proprietaryDefaults;
```

## Class methods

```
+[FigCaptureProprietaryDefaultsSource initialize];
```

## Instance methods

```
-[FigCaptureProprietaryDefaultsSource dealloc];
-[FigCaptureProprietaryDefaultsSource invalidate];
-[FigCaptureProprietaryDefaultsSource initWithDefaultsChangedHandler:];
-[FigCaptureProprietaryDefaultsSource _addToCameraOverrideHistory:historyOverridePreferenceKey:clientPID:];
-[FigCaptureProprietaryDefaultsSource _cleanupCameraHistoryDownplayOverrideListBecauseCameraWasRemovedFromOverrideHistory:clientPID:];
-[FigCaptureProprietaryDefaultsSource _handleRequestGesturesDefaultDisabledNotificationSignal:];
-[FigCaptureProprietaryDefaultsSource _handleRequestRingLightOnboardingTipSignal:];
-[FigCaptureProprietaryDefaultsSource _removeFromCameraOverrideHistory:historyOverridePreferenceKey:clientPID:];
-[FigCaptureProprietaryDefaultsSource _sendNotificationOfNewTransientValue:key:];
-[FigCaptureProprietaryDefaultsSource _updateCameraHistoriesUpdatedWithOverridingCameraForPreferenceKey:cameraInfo:clientPID:cameraCanBeInOverrideList:];
-[FigCaptureProprietaryDefaultsSource _updateCameraHistoryDownplayOverrideListForPreferenceKey:clientPID:];
-[FigCaptureProprietaryDefaultsSource copyCameraHistoryDownplayOverrideList];
-[FigCaptureProprietaryDefaultsSource copyDefaultForKey:valueOut:];
-[FigCaptureProprietaryDefaultsSource copyProprietaryDefaultsDomainForAuditToken:];
-[FigCaptureProprietaryDefaultsSource copyWildcardDefaultForKey:valueOut:];
-[FigCaptureProprietaryDefaultsSource migrateDefaultsFromAppBundleID:toAppBundleID:];
-[FigCaptureProprietaryDefaultsSource registerNotificationForProprietaryDefaultChanges:];
-[FigCaptureProprietaryDefaultsSource setDefaultForKey:value:];
-[FigCaptureProprietaryDefaultsSource setWildcardDefaultForKey:value:affectedKeysOut:];
-[FigCaptureProprietaryDefaultsSource unregisterNotificationForProprietaryDefaultChanges:];
-[FigCaptureProprietaryDefaultsSource updateCameraHistoryForClientPID:cameraHistoryKey:cameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:outNewCameraHistory:];
-[FigCaptureProprietaryDefaultsSource updateCameraOverrideHistoryForClientPID:cameraOverrideHistoryKey:overrideCameraInfo:setOverride:outOverrideHistoryChanged:outNewCameraOverrideHistory:];
```
