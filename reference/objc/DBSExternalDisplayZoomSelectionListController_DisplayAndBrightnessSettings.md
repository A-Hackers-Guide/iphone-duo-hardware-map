# `DBSExternalDisplayZoomSelectionListController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DBSDisplayZoomSelectionListController`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBSConnectedDisplayInfo" _externalDisplayInfo;
@"SBSExternalDisplayService" _displayService;
@"SBSDisplayModeSettings" _selectedDisplayModeSettings;
```

## Properties

```
@property (T@"SBSDisplayModeSettings",&,N,V_selectedDisplayModeSettings) selectedDisplayModeSettings;
@property (T@"SBSConnectedDisplayInfo",&,N,V_externalDisplayInfo) externalDisplayInfo;
@property (T@"SBSExternalDisplayService",&,N,V_displayService) displayService;
```

## Instance methods

```
-[DBSExternalDisplayZoomSelectionListController tableView:cellForRowAtIndexPath:];
-[DBSExternalDisplayZoomSelectionListController setDisplayService:];
-[DBSExternalDisplayZoomSelectionListController setSelectedDisplayModeSettings:];
-[DBSExternalDisplayZoomSelectionListController userDidTapDone:];
-[DBSExternalDisplayZoomSelectionListController _updateNavigationButtonStateWithNewDisplayModeSettings:];
-[DBSExternalDisplayZoomSelectionListController displayService];
-[DBSExternalDisplayZoomSelectionListController displayZoomTableViewCell:userDidTapOnDisplayZoomOption:];
-[DBSExternalDisplayZoomSelectionListController displayZoomTableViewCellCurrentlySelectedDisplayZoomOption:];
-[DBSExternalDisplayZoomSelectionListController externalDisplayInfo];
-[DBSExternalDisplayZoomSelectionListController selectedDisplayModeSettings];
-[DBSExternalDisplayZoomSelectionListController setExternalDisplayInfo:];
-[DBSExternalDisplayZoomSelectionListController supportedDisplayZoomOptions];
-[DBSExternalDisplayZoomSelectionListController updateNavigationButtonStateWithCurrentState];
```
