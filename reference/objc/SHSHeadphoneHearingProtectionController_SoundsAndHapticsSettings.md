# `SHSHeadphoneHearingProtectionController`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 10 instance variables, 10 properties, 53 instance methods, 0 class methods

## Instance variables

```
B _DeviceiPad;
B _DeviceiPod;
B _DeviceInRetailKioskMode;
B _shouldShowHeadphoneNotificationsSection;
i _weeklyNotificationCount;
@"ADASManager" _audioSettingsManager;
@"HKHealthStore" _healthStore;
@"NSArray" _weeklyNotificationData;
@"NSNumberFormatter" _numberFormatter;
@"NSNumber" _levelLimitThreshold;
```

## Properties

```
@property (T@"ADASManager",&,N,V_audioSettingsManager) audioSettingsManager;
@property (TB,N,GisDeviceiPad,V_DeviceiPad) DeviceiPad;
@property (TB,N,GisDeviceiPod,V_DeviceiPod) DeviceiPod;
@property (TB,N,GisDeviceInRetailKioskMode,V_DeviceInRetailKioskMode) DeviceInRetailKioskMode;
@property (TB,R,N,V_shouldShowHeadphoneNotificationsSection) shouldShowHeadphoneNotificationsSection;
@property (T@"HKHealthStore",&,N,V_healthStore) healthStore;
@property (T@"NSArray",&,N,V_weeklyNotificationData) weeklyNotificationData;
@property (Ti,N,V_weeklyNotificationCount) weeklyNotificationCount;
@property (T@"NSNumberFormatter",&,N,V_numberFormatter) numberFormatter;
@property (T@"NSNumber",&,N,V_levelLimitThreshold) levelLimitThreshold;
```

## Instance methods

```
-[SHSHeadphoneHearingProtectionController numberFormatter];
-[SHSHeadphoneHearingProtectionController startDate];
-[SHSHeadphoneHearingProtectionController healthStore];
-[SHSHeadphoneHearingProtectionController setHealthStore:];
-[SHSHeadphoneHearingProtectionController dismiss];
-[SHSHeadphoneHearingProtectionController init];
-[SHSHeadphoneHearingProtectionController dealloc];
-[SHSHeadphoneHearingProtectionController endDate];
-[SHSHeadphoneHearingProtectionController viewWillAppear:];
-[SHSHeadphoneHearingProtectionController viewDidAppear:];
-[SHSHeadphoneHearingProtectionController loadView];
-[SHSHeadphoneHearingProtectionController setNumberFormatter:];
-[SHSHeadphoneHearingProtectionController specifiers];
-[SHSHeadphoneHearingProtectionController isDeviceiPad];
-[SHSHeadphoneHearingProtectionController openAboutHeadphoneNotifications];
-[SHSHeadphoneHearingProtectionController audioSettingsManager];
-[SHSHeadphoneHearingProtectionController deviceTypeString];
-[SHSHeadphoneHearingProtectionController getHeadphoneLevelLimitEnabled];
-[SHSHeadphoneHearingProtectionController getHeadphoneLevelLimitSetting];
-[SHSHeadphoneHearingProtectionController getHeadphoneNotificationsEnabled];
-[SHSHeadphoneHearingProtectionController headphoneAudioDevicesSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneLevelLimitDescriptionSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneLevelLimitGroupSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneLevelLimitLockedByRestrictions];
-[SHSHeadphoneHearingProtectionController headphoneLevelLimitSliderSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneLevelLimitSwitchSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneNotificationsGroupSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneNotificationsSwitchSpecifier];
-[SHSHeadphoneHearingProtectionController headphoneWeeklyNotificationDescriptionSpecifier];
-[SHSHeadphoneHearingProtectionController isDeviceInRetailKioskMode];
-[SHSHeadphoneHearingProtectionController isDeviceiPod];
-[SHSHeadphoneHearingProtectionController levelLimitThreshold];
-[SHSHeadphoneHearingProtectionController openHealthArticleSafeListening];
-[SHSHeadphoneHearingProtectionController openHealthPrivacySettings];
-[SHSHeadphoneHearingProtectionController queryNotificationCountsFromDate:toDate:];
-[SHSHeadphoneHearingProtectionController setAudioSettingsManager:];
-[SHSHeadphoneHearingProtectionController setDeviceInRetailKioskMode:];
-[SHSHeadphoneHearingProtectionController setDeviceiPad:];
-[SHSHeadphoneHearingProtectionController setDeviceiPod:];
-[SHSHeadphoneHearingProtectionController setHeadphoneLevelLimitEnabled:forSpecifier:];
-[SHSHeadphoneHearingProtectionController setHeadphoneLevelLimitValue:forSpecifier:];
-[SHSHeadphoneHearingProtectionController setHeadphoneNotificationsEnabled:forSpecifier:];
-[SHSHeadphoneHearingProtectionController setLevelLimitThreshold:];
-[SHSHeadphoneHearingProtectionController setWeeklyNotificationCount:];
-[SHSHeadphoneHearingProtectionController setWeeklyNotificationData:];
-[SHSHeadphoneHearingProtectionController shouldShowHeadphoneNotificationsSection];
-[SHSHeadphoneHearingProtectionController shouldShowHealthFeatures];
-[SHSHeadphoneHearingProtectionController updateHeadphoneLevelLimitDescriptionText];
-[SHSHeadphoneHearingProtectionController updateHeadphoneLevelLimitText];
-[SHSHeadphoneHearingProtectionController updateMonthlyNotificationCounts:withNames:forDates:];
-[SHSHeadphoneHearingProtectionController weeklyNotificationCount];
-[SHSHeadphoneHearingProtectionController weeklyNotificationCount:];
-[SHSHeadphoneHearingProtectionController weeklyNotificationData];
```
