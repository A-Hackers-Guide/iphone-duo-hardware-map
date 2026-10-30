# `SBWindowSceneStatusBarLayoutManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 8 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableOrderedSet" _windowLevelOverrideReasons;
@"NSMutableDictionary" _windowLevelOverrideMap;
@"NSMutableDictionary" _edgeInsetsDictionary;
@"NSMutableSet" _activeLayoutLayers;
@"NSMutableDictionary" _orientationWindowDictionary;
d _defaultWindowLevel;
@"SBWindowScene" _windowScene;
@"<BSInvalidatable>" _stateCaptureAssertion;
```

## Properties

```
@property (TQ,R,N) topmostActiveLayoutLayer;
@property (T{UIEdgeInsets=dddd},R,N) statusBarEdgeInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowSceneStatusBarLayoutManager succinctDescriptionBuilder];
-[SBWindowSceneStatusBarLayoutManager descriptionWithMultilinePrefix:];
-[SBWindowSceneStatusBarLayoutManager initWithWindowScene:];
-[SBWindowSceneStatusBarLayoutManager succinctDescription];
-[SBWindowSceneStatusBarLayoutManager description];
-[SBWindowSceneStatusBarLayoutManager descriptionBuilderWithMultilinePrefix:];
-[SBWindowSceneStatusBarLayoutManager setDefaultWindowLevel:];
-[SBWindowSceneStatusBarLayoutManager _applyEdgeInsetsToStatusBar];
-[SBWindowSceneStatusBarLayoutManager _updateStatusBarOrientationForTopMostActiveLayer];
-[SBWindowSceneStatusBarLayoutManager _updateWindowLevel];
-[SBWindowSceneStatusBarLayoutManager addActiveLayoutLayer:];
-[SBWindowSceneStatusBarLayoutManager orientationWindowForLayoutLayer:];
-[SBWindowSceneStatusBarLayoutManager removeActiveLayoutLayer:];
-[SBWindowSceneStatusBarLayoutManager removeWindowLevelOverrideReason:];
-[SBWindowSceneStatusBarLayoutManager setOrientationWindow:forStatusBarLayoutLayer:];
-[SBWindowSceneStatusBarLayoutManager setStatusBarEdgeInsets:forLayoutLayer:];
-[SBWindowSceneStatusBarLayoutManager setWindowLevel:forOverrideReason:];
-[SBWindowSceneStatusBarLayoutManager statusBarEdgeInsets];
-[SBWindowSceneStatusBarLayoutManager statusBarOrientationShouldFollowWindow:];
-[SBWindowSceneStatusBarLayoutManager topmostActiveLayoutLayer];
```
