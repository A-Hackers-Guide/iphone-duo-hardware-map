# `UIMainMenuSystem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMenuSystem`
- 7 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"_UIMenuBuilder" _automaticallyRebuildingBuilder;
@"UIMainMenuSystemConfiguration" _configuration;
@? _buildHandler;
@"UIMainMenuSystemConfiguration" _overrideConfiguration;
@? _overrideBuildHandler;
@"UIResponder" _initialBuildingResponderOverride;
@"NSString" _overrideApplicationName;
```

## Properties

```
@property (T@"NSArray",R,N) _keyCommands;
@property (T@"UIMenu",R,N) _rootMenu;
```

## Class methods

```
+[UIMainMenuSystem sharedSystem];
```

## Instance methods

```
-[UIMainMenuSystem _overrideApplicationName];
-[UIMainMenuSystem setBuildConfiguration:buildHandler:];
-[UIMainMenuSystem dealloc];
-[UIMainMenuSystem _defaultRootMenuChildren];
-[UIMainMenuSystem _campoAvailabilityDidChange:];
-[UIMainMenuSystem _setOverrideApplicationName:];
-[UIMainMenuSystem _init];
-[UIMainMenuSystem _additionalKeyCommands];
-[UIMainMenuSystem setNeedsRebuild];
-[UIMainMenuSystem _automaticallyRebuildIfNeeded];
-[UIMainMenuSystem _buildMenuWithBuilder:fromResponderChain:atLocation:inCoordinateSpace:];
-[UIMainMenuSystem _rootMenu];
-[UIMainMenuSystem _setOverrideBuildConfiguration:overrideBuildHandler:];
-[UIMainMenuSystem _effectiveBuildHandler];
-[UIMainMenuSystem _effectiveConfiguration];
-[UIMainMenuSystem _keyCommands];
-[UIMainMenuSystem _setInitialBuildingResponder:];
```
