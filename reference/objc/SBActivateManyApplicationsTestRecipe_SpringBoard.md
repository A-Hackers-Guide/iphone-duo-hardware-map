# `SBActivateManyApplicationsTestRecipe`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTestRecipe`
- 2 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _launchedAppsCount;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBActivateManyApplicationsTestRecipe _bundleIdentifiers];
```

## Instance methods

```
-[SBActivateManyApplicationsTestRecipe init];
-[SBActivateManyApplicationsTestRecipe title];
-[SBActivateManyApplicationsTestRecipe _addAppToStageWithBundleIdentifier:];
-[SBActivateManyApplicationsTestRecipe _addNewNotesSceneToStage];
-[SBActivateManyApplicationsTestRecipe _destroyApplicationSceneHandles:];
-[SBActivateManyApplicationsTestRecipe _removeFrontmostScene];
-[SBActivateManyApplicationsTestRecipe _removeNotesScenes];
-[SBActivateManyApplicationsTestRecipe _removeScenesForAppWithBundleIdentifier:];
-[SBActivateManyApplicationsTestRecipe handleVolumeDecrease];
-[SBActivateManyApplicationsTestRecipe handleVolumeIncrease];
-[SBActivateManyApplicationsTestRecipe windowSceneDidUpdate:];
```
