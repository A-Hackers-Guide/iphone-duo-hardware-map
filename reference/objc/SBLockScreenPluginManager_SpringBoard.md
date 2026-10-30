# `SBLockScreenPluginManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLockScreenPluginAgent`, `PTSettingsKeyObserver`, `SBFLockScreenActionProvider`
- 6 instance variables, 8 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _plugins;
@"SBLockScreenPlugin" _activePlugin;
@"SBLockScreenPlugin" _displayedPlugin;
@"<SBLockScreenPluginManagerDelegate>" _delegate;
@"CSLockScreenTestPluginSettings" _testSettings;
B _enabled;
```

## Properties

```
@property (T@"SBLockScreenPlugin",R,N,V_activePlugin) activePlugin;
@property (T@"SBLockScreenPlugin",R,N,V_displayedPlugin) displayedPlugin;
@property (T@"<SBLockScreenPluginManagerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenPluginManager handleEvent:];
-[SBLockScreenPluginManager succinctDescriptionBuilder];
-[SBLockScreenPluginManager init];
-[SBLockScreenPluginManager dealloc];
-[SBLockScreenPluginManager descriptionWithMultilinePrefix:];
-[SBLockScreenPluginManager settings:changedValueForKey:];
-[SBLockScreenPluginManager isEnabled];
-[SBLockScreenPluginManager succinctDescription];
-[SBLockScreenPluginManager setDelegate:];
-[SBLockScreenPluginManager disableLockScreenPluginWithContext:];
-[SBLockScreenPluginManager setEnabled:];
-[SBLockScreenPluginManager enableLockScreenPluginWithContext:];
-[SBLockScreenPluginManager delegate];
-[SBLockScreenPluginManager description];
-[SBLockScreenPluginManager descriptionBuilderWithMultilinePrefix:];
-[SBLockScreenPluginManager lockScreenActionContext];
-[SBLockScreenPluginManager _handleUIRelock];
-[SBLockScreenPluginManager displayedPlugin];
-[SBLockScreenPluginManager _handlePluginDisabled:withContext:];
-[SBLockScreenPluginManager _highestPriorityPluginIgnoringViewDisplay:];
-[SBLockScreenPluginManager _loadLockScreenPluginWithContext:];
-[SBLockScreenPluginManager _pluginForPluginController:];
-[SBLockScreenPluginManager _refreshLockScreenPlugin];
-[SBLockScreenPluginManager _sendEventToPlugin:];
-[SBLockScreenPluginManager _setActivePlugin:displayedPlugin:];
-[SBLockScreenPluginManager activatePluginController:];
-[SBLockScreenPluginManager activePlugin];
-[SBLockScreenPluginManager deactivatePluginController:];
-[SBLockScreenPluginManager pluginController:sendAction:];
-[SBLockScreenPluginManager pluginController:updateAppearance:];
```
