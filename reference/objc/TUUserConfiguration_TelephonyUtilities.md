# `TUUserConfiguration`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUConfiguration`
- 1 instance variables, 1 properties, 44 instance methods, 16 class methods

## Instance variables

```
@"CoreTelephonyClient" _coreTelephonyClient;
```

## Properties

```
@property (T@"CoreTelephonyClient",R,N,V_coreTelephonyClient) coreTelephonyClient;
```

## Class methods

```
+[TUUserConfiguration userDefaults];
+[TUUserConfiguration isFilterAsNewCallersEnabledForFaceTime];
+[TUUserConfiguration faceTimeNewCallersFilterMode];
+[TUUserConfiguration setFaceTimeHideNotifications:];
+[TUUserConfiguration setFaceTimeNewCallersFilterMode:];
+[TUUserConfiguration registeredDefaults];
+[TUUserConfiguration faceTimeHideNotifications];
+[TUUserConfiguration isFilterAsNewCallersEnabledForPhone];
+[TUUserConfiguration isSilenceUnknownCallersEnabledForFaceTime];
+[TUUserConfiguration featureFlags];
+[TUUserConfiguration getBooleanFromUserDefaults:default:dataSource:];
+[TUUserConfiguration isLegacyFilterAsNewCallersEnabledForFaceTime];
+[TUUserConfiguration migrateLegacyCallFiltering];
+[TUUserConfiguration numberForKey:dataSource:];
+[TUUserConfiguration refreshFaceTimeHideNotifications];
+[TUUserConfiguration shouldHideFaceTimeNotificationsByDefault];
```

## Instance methods

```
-[TUUserConfiguration setReceptionistEnabled:];
-[TUUserConfiguration setBusinessConnectCallingEnabled:];
-[TUUserConfiguration initForTestingWithDataSource:];
-[TUUserConfiguration isCallScreeningEnabled];
-[TUUserConfiguration observeValueForKeyPath:ofObject:change:context:];
-[TUUserConfiguration coreTelephonyClient];
-[TUUserConfiguration isSilenceJunkCallingEnabled];
-[TUUserConfiguration isCallRecordingEnabled];
-[TUUserConfiguration synchronize];
-[TUUserConfiguration setFilterAsNewCallersEnabledForFaceTime:];
-[TUUserConfiguration setSpamFilterEnabledForFaceTime:];
-[TUUserConfiguration init];
-[TUUserConfiguration setFilterAsNewCallersEnabledForPhone:];
-[TUUserConfiguration isSpamFilterEnabledForFaceTime];
-[TUUserConfiguration isSmartVoicemailActionsEnabled];
-[TUUserConfiguration isBusinessConnectCallingEnabled];
-[TUUserConfiguration dealloc];
-[TUUserConfiguration setCallRecordingEnabled:];
-[TUUserConfiguration isFilterAsNewCallersEnabledForFaceTime];
-[TUUserConfiguration getBooleanFromUserDefaults:default:];
-[TUUserConfiguration setHoldAssistDetectionEnabled:];
-[TUUserConfiguration faceTimeNewCallersFilterMode];
-[TUUserConfiguration setFaceTimeHideNotifications:];
-[TUUserConfiguration isEligibleForReceptionistOnboardingNotification];
-[TUUserConfiguration setFaceTimeNewCallersFilterMode:];
-[TUUserConfiguration setUplevelFTAEnabled:];
-[TUUserConfiguration setSilenceJunkCallingEnabled:];
-[TUUserConfiguration setSilenceUnknownCallersEnabledForFaceTime:];
-[TUUserConfiguration setSilenceUnknownCallersEnabledForPhone:];
-[TUUserConfiguration setCallScreeningEnabled:];
-[TUUserConfiguration faceTimeHideNotifications];
-[TUUserConfiguration isBrandedCallingEnabled:];
-[TUUserConfiguration setEligibleForReceptionistOnboardingNotification:];
-[TUUserConfiguration isCallHapticsEnabled];
-[TUUserConfiguration isUplevelFTAEnabled];
-[TUUserConfiguration isHoldAssistDetectionEnabled];
-[TUUserConfiguration setCallHapticsEnabled:];
-[TUUserConfiguration isFilterAsNewCallersEnabledForPhone];
-[TUUserConfiguration isSilenceUnknownCallersEnabledForPhone];
-[TUUserConfiguration isSilenceUnknownCallersEnabledForFaceTime];
-[TUUserConfiguration setValueInUserDefaults:forKey:];
-[TUUserConfiguration setSmartVoicemailActionsEnabled:];
-[TUUserConfiguration isReceptionistEnabled];
-[TUUserConfiguration setBrandedCallingEnabled:subscription:];
```
