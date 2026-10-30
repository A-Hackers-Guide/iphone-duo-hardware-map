# `SBLiveActivitySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 7 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _allowAlertsOnHostApp;
B _hideActivitiesInLockScreen;
B _hideActivitiesInDynamicIsland;
B _hideActivitiesInAmbient;
B _disableActivityAlertsAsBanners;
B _allowPortraitActivitiesInAmbient;
@"SBAmbientLiveActivitiesSettings" _ambientSettings;
```

## Properties

```
@property (TB,N,V_allowAlertsOnHostApp) allowAlertsOnHostApp;
@property (TB,N,V_hideActivitiesInLockScreen) hideActivitiesInLockScreen;
@property (TB,N,V_hideActivitiesInDynamicIsland) hideActivitiesInDynamicIsland;
@property (TB,N,V_hideActivitiesInAmbient) hideActivitiesInAmbient;
@property (TB,N,V_disableActivityAlertsAsBanners) disableActivityAlertsAsBanners;
@property (TB,N,V_allowPortraitActivitiesInAmbient) allowPortraitActivitiesInAmbient;
@property (T@"SBAmbientLiveActivitiesSettings",&,N,V_ambientSettings) ambientSettings;
```

## Class methods

```
+[SBLiveActivitySettings settingsControllerModule];
```

## Instance methods

```
-[SBLiveActivitySettings setDefaultValues];
-[SBLiveActivitySettings ambientSettings];
-[SBLiveActivitySettings allowAlertsOnHostApp];
-[SBLiveActivitySettings allowPortraitActivitiesInAmbient];
-[SBLiveActivitySettings disableActivityAlertsAsBanners];
-[SBLiveActivitySettings hideActivitiesInAmbient];
-[SBLiveActivitySettings hideActivitiesInDynamicIsland];
-[SBLiveActivitySettings hideActivitiesInLockScreen];
-[SBLiveActivitySettings setAllowAlertsOnHostApp:];
-[SBLiveActivitySettings setAllowPortraitActivitiesInAmbient:];
-[SBLiveActivitySettings setAmbientSettings:];
-[SBLiveActivitySettings setDisableActivityAlertsAsBanners:];
-[SBLiveActivitySettings setHideActivitiesInAmbient:];
-[SBLiveActivitySettings setHideActivitiesInDynamicIsland:];
-[SBLiveActivitySettings setHideActivitiesInLockScreen:];
```
