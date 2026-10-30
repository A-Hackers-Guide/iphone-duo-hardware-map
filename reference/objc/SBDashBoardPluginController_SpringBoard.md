# `SBDashBoardPluginController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalAppearanceProviding`, `CSExternalBehaviorProviding`, `CSExternalEventHandling`, `SBLockScreenPluginManagerDelegate`, `SBLockScreenPluginPresenting`
- 4 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBDashBoardPluginViewController" _pluginViewController;
q _pluginViewControllerPresentationStyle;
@"SBLockScreenPluginManager" _pluginManager;
```

## Properties

```
@property (T@"<SBFLockScreenActionProvider>",R,N) lockScreenActionProvider;
@property (T@"NSString",R,C,N) appearanceIdentifier;
@property (T@"NSSet",R,C,N) components;
@property (T@"_UILegibilitySettings",R,N) legibilitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
```

## Instance methods

```
-[SBDashBoardPluginController handleEvent:];
-[SBDashBoardPluginController _activate];
-[SBDashBoardPluginController wouldHandleButtonEvent:];
-[SBDashBoardPluginController conformsToCSBehaviorProviding];
-[SBDashBoardPluginController _deactivate];
-[SBDashBoardPluginController conformsToCSAppearanceProviding];
-[SBDashBoardPluginController appearanceIdentifier];
-[SBDashBoardPluginController dealloc];
-[SBDashBoardPluginController proximityDetectionMode];
-[SBDashBoardPluginController components];
-[SBDashBoardPluginController scrollingStrategy];
-[SBDashBoardPluginController notificationBehavior];
-[SBDashBoardPluginController disableLockScreenPluginWithContext:];
-[SBDashBoardPluginController enableLockScreenPluginWithContext:];
-[SBDashBoardPluginController legibilitySettings];
-[SBDashBoardPluginController conformsToCSExternalBehaviorProviding];
-[SBDashBoardPluginController conformsToCSEventHandling];
-[SBDashBoardPluginController coverSheetIdentifier];
-[SBDashBoardPluginController participantState];
-[SBDashBoardPluginController restrictedCapabilities];
-[SBDashBoardPluginController pluginManager:willUnloadPlugin:];
-[SBDashBoardPluginController _dismissPluginViewController:withStyle:animated:completion:];
-[SBDashBoardPluginController _presentPluginViewController:withStyle:animated:completion:];
-[SBDashBoardPluginController _setPluginViewController:];
-[SBDashBoardPluginController initWithCoverSheetViewController:];
-[SBDashBoardPluginController lockScreenActionProvider];
-[SBDashBoardPluginController pluginManager:activePluginDidChange:];
-[SBDashBoardPluginController pluginManager:didLoadPlugin:];
-[SBDashBoardPluginController pluginManager:displayedPluginDidChangeFromPlugin:toPlugin:];
-[SBDashBoardPluginController pluginManager:displayedPluginDidUpdateAppearance:];
-[SBDashBoardPluginController pluginManager:plugin:handleAction:];
```
