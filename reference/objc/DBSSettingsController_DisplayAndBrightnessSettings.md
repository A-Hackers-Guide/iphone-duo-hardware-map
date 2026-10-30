# `DBSSettingsController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `UISUserInterfaceStyleModeDelegate`, `DBSDeviceAppearanceTableViewCellDelegate`, `DBSExternalDisplayMultitaskingTableViewCellDelegate`, `DBSZoomAndProSpecifiersDelegate`, `DBSArrangementViewControllerDelegate`, `PSListControllerTestableSpecifiers`
- 10 instance variables, 10 properties, 76 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _autoLockValues;
@"NSDictionary" _autoLockTitleDictionary;
@"NSMutableDictionary" _localizedAutoLockTitleDictionary;
@"NSDateFormatter" _timeFormatter;
@"SBSExternalDisplayService" _displayService;
@"SBSConnectedDisplayInfo" _externalDisplayInfo;
@"UISUserInterfaceStyleMode" __styleMode;
@"CBClient" __brightnessClient;
@"DBSZoomAndProSpecifiers" __zoomAndProSpecifierVendor;
@"PSSetupController" _arrangementViewController;
```

## Properties

```
@property (T@"UISUserInterfaceStyleMode",&,N,V__styleMode) _styleMode;
@property (T@"CBClient",&,N,V__brightnessClient) _brightnessClient;
@property (T@"DBSZoomAndProSpecifiers",&,N,V__zoomAndProSpecifierVendor) _zoomAndProSpecifierVendor;
@property (T@"SBSExternalDisplayService",&,N,V_displayService) displayService;
@property (T@"SBSConnectedDisplayInfo",&,N,V_externalDisplayInfo) externalDisplayInfo;
@property (T@"PSSetupController",&,N,V_arrangementViewController) arrangementViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DBSSettingsController booleanCapabilitiesToTest];
```

## Instance methods

```
-[DBSSettingsController observeValueForKeyPath:ofObject:change:context:];
-[DBSSettingsController init];
-[DBSSettingsController dealloc];
-[DBSSettingsController viewDidLoad];
-[DBSSettingsController tableView:willDisplayCell:forRowAtIndexPath:];
-[DBSSettingsController initWithNibName:bundle:];
-[DBSSettingsController viewWillAppear:];
-[DBSSettingsController viewDidAppear:];
-[DBSSettingsController traitCollectionDidChange:];
-[DBSSettingsController arrangementViewController];
-[DBSSettingsController userInterfaceStyleModeDidChange:];
-[DBSSettingsController specifiers];
-[DBSSettingsController setBoldTextEnabled:specifier:];
-[DBSSettingsController profileNotification:];
-[DBSSettingsController setDisplayService:];
-[DBSSettingsController insertExternalDisplaySpecifiers];
-[DBSSettingsController removeExternalDisplaySpecifiers];
-[DBSSettingsController _deviceAppearanceScheduleString];
-[DBSSettingsController autoLockValues:];
-[DBSSettingsController getAppearanceValueForSpecifier:];
-[DBSSettingsController _brightnessClient];
-[DBSSettingsController _darkAppearanceTimeString];
-[DBSSettingsController _deviceAppearanceScheduleSpecifier];
-[DBSSettingsController _initialAutoLock];
-[DBSSettingsController _lightAppearanceTimeString];
-[DBSSettingsController _localizeAutoLockTitles];
-[DBSSettingsController _localizeAutoLockTitlesWithSpecifiers:];
-[DBSSettingsController _reloadBlueLightSpecifiers:reloadUI:];
-[DBSSettingsController _styleMode];
-[DBSSettingsController _updateAutoLockSpecifiers:];
-[DBSSettingsController _updateDeviceAppearanceToNewInterfaceStyle:];
-[DBSSettingsController _zoomAndProSpecifierVendor];
-[DBSSettingsController arrangementViewControllerDidDismiss:];
-[DBSSettingsController autoLock:];
-[DBSSettingsController autoLockTitles];
-[DBSSettingsController blueLightSchedule:];
-[DBSSettingsController boldTextEnabledForSpecifier:];
-[DBSSettingsController connectedDisplayName];
-[DBSSettingsController connectedDisplaySpecifiers];
-[DBSSettingsController deviceAppearanceTableViewCellUserDidTapOnDarkAppearance:];
-[DBSSettingsController deviceAppearanceTableViewCellUserDidTapOnLightAppearance:];
-[DBSSettingsController displayService];
-[DBSSettingsController externalDisplayInfo];
-[DBSSettingsController externalDisplayMultitaskingTableViewCellUserDidSelectedExtendedDisplay:];
-[DBSSettingsController externalDisplayMultitaskingTableViewCellUserDidSelectedScreenMirroring:];
-[DBSSettingsController getAutomaticAppearanceEnabledForSpecifier:];
-[DBSSettingsController handleBlueLightStatusChanged:];
-[DBSSettingsController handleDBSExternalDisplayManagerCurrentModeDidChangeNotification:];
-[DBSSettingsController handleDisplayServiceInfoUpdate];
-[DBSSettingsController insertArrangementSpecifier];
-[DBSSettingsController jumpToAccessibilitySettings:];
-[DBSSettingsController localizedTimeForTime:];
-[DBSSettingsController lockGroupFooterText];
-[DBSSettingsController locksAndUnlocksWithCase:];
-[DBSSettingsController makeArrangementSpecifier];
-[DBSSettingsController presentArrangementController];
-[DBSSettingsController presentModalMagnifyController];
-[DBSSettingsController proModeSupported];
-[DBSSettingsController setAppearanceValue:forSpecifier:];
-[DBSSettingsController setArrangementViewController:];
-[DBSSettingsController setAutoLock:specifier:];
-[DBSSettingsController setAutomaticAppearanceEnabled:forSpecifier:];
-[DBSSettingsController setExternalDisplayInfo:];
-[DBSSettingsController setLockGroupFooter:];
-[DBSSettingsController setLocksAndUnlocksWithCase:specifier:];
-[DBSSettingsController set_brightnessClient:];
-[DBSSettingsController set_styleMode:];
-[DBSSettingsController set_zoomAndProSpecifierVendor:];
-[DBSSettingsController shouldShowAlwaysOn];
-[DBSSettingsController shouldShowAutoLock];
-[DBSSettingsController shouldShowCaseLock];
-[DBSSettingsController shouldShowLockGroup];
-[DBSSettingsController updateAutoLockSpecifier];
-[DBSSettingsController updateExternalDisplayInfoWithCompletionHandler:];
-[DBSSettingsController updateForExternalMonitorAvailability:];
-[DBSSettingsController updateReferenceDependentUIElements];
```
