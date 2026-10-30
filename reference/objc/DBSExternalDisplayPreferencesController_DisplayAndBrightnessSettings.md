# `DBSExternalDisplayPreferencesController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `DBSZoomAndProSpecifiersDelegate`, `DBSDisplayZoomSelectionControllerDelegate`
- 2 instance variables, 7 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"DBSZoomAndProSpecifiers" __zoomAndProSpecifierVendor;
@"UISlider" _externalBrightnessSlider;
```

## Properties

```
@property (T@"DBSZoomAndProSpecifiers",&,N,V__zoomAndProSpecifierVendor) _zoomAndProSpecifierVendor;
@property (T@"SBSConnectedDisplayInfo",R,N) externalDisplayInfo;
@property (T@"UISlider",W,N,V_externalBrightnessSlider) externalBrightnessSlider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DBSExternalDisplayPreferencesController tableView:shouldHighlightRowAtIndexPath:];
-[DBSExternalDisplayPreferencesController init];
-[DBSExternalDisplayPreferencesController dealloc];
-[DBSExternalDisplayPreferencesController viewDidLoad];
-[DBSExternalDisplayPreferencesController tableView:didSelectRowAtIndexPath:];
-[DBSExternalDisplayPreferencesController specifiers];
-[DBSExternalDisplayPreferencesController valueForSpecifier:];
-[DBSExternalDisplayPreferencesController _zoomAndProSpecifierVendor];
-[DBSExternalDisplayPreferencesController connectedDisplayDidUpdate:];
-[DBSExternalDisplayPreferencesController connectedDisplayName];
-[DBSExternalDisplayPreferencesController currentHDRMode];
-[DBSExternalDisplayPreferencesController displayModeSpecifiers];
-[DBSExternalDisplayPreferencesController displayZoomDidUpdate];
-[DBSExternalDisplayPreferencesController externalAutoBrightnessValueForSpecifier:];
-[DBSExternalDisplayPreferencesController externalBrightnessDidUpdate:];
-[DBSExternalDisplayPreferencesController externalBrightnessSlider];
-[DBSExternalDisplayPreferencesController externalBrightnessSliderTouchEnded:];
-[DBSExternalDisplayPreferencesController externalBrightnessSpecifiers];
-[DBSExternalDisplayPreferencesController externalBrightnessValueForSpecifier:];
-[DBSExternalDisplayPreferencesController externalDisplayInfo];
-[DBSExternalDisplayPreferencesController getProModeEnabled];
-[DBSExternalDisplayPreferencesController handleDBSExternalDBSDisplayPreferencesControllerExternalDisplayManagerExternalAutoBrightnessAvailablityDidChangeNotification:];
-[DBSExternalDisplayPreferencesController handleDBSExternalDBSDisplayPreferencesControllerExternalDisplayManagerExternalAutoBrightnessValueDidChangeNotification:];
-[DBSExternalDisplayPreferencesController handleDBSExternalDisplayManagerExternalBrightnessAvailablityDidChangeNotification:];
-[DBSExternalDisplayPreferencesController insertExternalBrightnessSpecifiers];
-[DBSExternalDisplayPreferencesController localizedMagnifyModeName];
-[DBSExternalDisplayPreferencesController matchContentEnabled:];
-[DBSExternalDisplayPreferencesController presentModalFineTuneController];
-[DBSExternalDisplayPreferencesController presentModalMagnifyController];
-[DBSExternalDisplayPreferencesController proModeSupported];
-[DBSExternalDisplayPreferencesController removeExternalBrightnessSpecifiers];
-[DBSExternalDisplayPreferencesController setCurrentHDRMode:];
-[DBSExternalDisplayPreferencesController setExternalAutoBrightnessValue:specifier:];
-[DBSExternalDisplayPreferencesController setExternalBrightnessSlider:];
-[DBSExternalDisplayPreferencesController setExternalBrightnessValue:specifier:];
-[DBSExternalDisplayPreferencesController setMatchContentEnabled:specifier:];
-[DBSExternalDisplayPreferencesController setProModeEnabled:];
-[DBSExternalDisplayPreferencesController set_zoomAndProSpecifierVendor:];
-[DBSExternalDisplayPreferencesController supportedZoomModesCount];
```
