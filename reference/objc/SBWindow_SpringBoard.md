# `SBWindow`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFWindow`
- Protocols: `SBFRecycledViewsContainerProviding`, `SBWindowLayoutStrategyObserving`
- 6 instance variables, 7 properties, 31 instance methods, 3 class methods

## Instance variables

```
@"SBUICoronaAnimationController" _coronaAnimationController;
@"SBRecycledViewsContainer" _recycledViewsContainerView;
B _requestedHiddenValue;
@"NSMutableSet" _additionalHiddenReasons;
@"TRAParticipant" _traitsParticipant;
@"<SBWindowLayoutStrategy>" _layoutStrategy;
```

## Properties

```
@property (T@"<SBWindowLayoutStrategy>",R,N,V_layoutStrategy) layoutStrategy;
@property (T@"TRAParticipant",R,N,V_traitsParticipant) traitsParticipant;
@property (T@"UIView",R,N) recycledViewsContainer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWindow sb_autorotates];
+[SBWindow defaultLayoutStrategy];
+[SBWindow sb_disableStatusBarHeightChanges];
```

## Instance methods

```
-[SBWindow _willEnableSecureRendering:];
-[SBWindow layoutStrategy];
-[SBWindow setHidden:];
-[SBWindow handleStatusBarChangeFromHeight:toHeight:];
-[SBWindow dealloc];
-[SBWindow recycledViewsContainer];
-[SBWindow makeKeyAndVisible];
-[SBWindow initWithWindowScene:];
-[SBWindow description];
-[SBWindow traitCollectionDidChange:];
-[SBWindow _didDisableSecureRendering:];
-[SBWindow traitsParticipant];
-[SBWindow initWithFrame:];
-[SBWindow initWithWindowScene:rootViewController:layoutStrategy:role:debugName:];
-[SBWindow _shouldResizeWithScene];
-[SBWindow setAutorotates:forceUpdateInterfaceOrientation:];
-[SBWindow initWithWindowScene:role:debugName:];
-[SBWindow sb_coronaAnimationController];
-[SBWindow _addHiddenReason:];
-[SBWindow _removeHiddenReason:];
-[SBWindow _sb_updateAutorotatesFlagAndForceInterfaceOrientationUpdate:];
-[SBWindow _setTraitsParticipant:];
-[SBWindow _traitsParticipant];
-[SBWindow _updateHidingForSecureRendering:];
-[SBWindow _updateRealIsHidden];
-[SBWindow initWithWindowScene:layoutStrategy:role:debugName:];
-[SBWindow initWithWindowScene:rootViewController:role:debugName:];
-[SBWindow layoutStrategyFrameOnScreenDidChange:];
-[SBWindow moveToWindowSceneIfNeeded:];
-[SBWindow sb_updateAutorotatesFlag];
-[SBWindow setAlphaAndObeyBecauseIAmTheWindowManager:];
```
