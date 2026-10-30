# `SBFocusModesHomeScreenSettingsManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFocusModesHomeScreenSettingsServerDelegate`, `SBIconListLayoutDelegate`
- 1 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBFocusModesHomeScreenSettingsServer" _settingsServer;
```

## Properties

```
@property (T@"SBFocusModesHomeScreenSettingsServer",&,N,V_settingsServer) settingsServer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFocusModesHomeScreenSettingsManager iconController];
-[SBFocusModesHomeScreenSettingsManager init];
-[SBFocusModesHomeScreenSettingsManager iconListView:didConfigureIconView:forIcon:];
-[SBFocusModesHomeScreenSettingsManager _snapshotRemainingListViews:snapshotDelay:snapshotScale:excludeWallpaper:forFocusModeIdentifier:iconManager:rootFolderView:accumulatedSnapshots:completion:];
-[SBFocusModesHomeScreenSettingsManager _snapshotRootFolderView:snapshotDelay:snapshotScale:excludeWallpaper:focusModeIdentifier:iconManager:isSuggestedPage:completion:];
-[SBFocusModesHomeScreenSettingsManager setSettingsServer:];
-[SBFocusModesHomeScreenSettingsManager settingsServer];
-[SBFocusModesHomeScreenSettingsManager settingsServer:addSuggestedHomeScreenPageWithRequest:];
-[SBFocusModesHomeScreenSettingsManager settingsServer:homeScreenSnapshotsForSuggestedPagesWithRequest:completion:];
-[SBFocusModesHomeScreenSettingsManager settingsServer:homeScreenSnapshotsWithRequest:completion:];
-[SBFocusModesHomeScreenSettingsManager settingsServer:updateFocusModeHomeScreenSettingsWithRequest:];
```
