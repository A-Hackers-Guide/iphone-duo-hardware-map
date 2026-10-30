# `SBWindowingSwitcherPersonality`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- Protocols: `SBChainableModifierDelegate`, `SBSwitcherPersonality`
- 16 instance variables, 7 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"SBRootWindowingModifier" _rootModifier;
@"SBAppLayout" _currentAppLayout;
q _currentEnvironmentMode;
@"SBWindowingStrip" _strip;
@"SBAppsRegionModel" _appsRegionModel;
@"SBDeckRegionModel" _deckRegionModel;
@"NSArray" _spacesBeforeAppsRegion;
@"NSArray" _spacesAfterAppsRegion;
@"SBAppLayout" _arcSwipeInitialAppLayout;
@"SBDisplayItem" _arcSwipeNextDisplayItem;
@"SBDisplayItem" _arcSwipePreviousDisplayItem;
@"SBSceneHandleSizesCache" _sceneHandleSizeCache;
@"NSUUID" _transitionIDForPreviousStateModel;
@"SBAppsRegionModel" _previousAppsRegionModel;
@"SBDeckRegionModel" _previousDeckRegionModel;
@"<SBSwitcherPersonalityView>" _view;
```

## Properties

```
@property (T@"SBSwitcherModifier",R,N) switcherModifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBSwitcherPersonalityView>",W,N,V_view) view;
@property (T@"<SBChainableModifierDelegate>",W,N) switcherContextDelegate;
```

## Instance methods

```
-[SBWindowingSwitcherPersonality handleEvent:];
-[SBWindowingSwitcherPersonality preferredSceneSizeThatFits:displayItem:];
-[SBWindowingSwitcherPersonality activities];
-[SBWindowingSwitcherPersonality setSwitcherContextDelegate:];
-[SBWindowingSwitcherPersonality performWithFinalPresentationValue:];
-[SBWindowingSwitcherPersonality appLayout];
-[SBWindowingSwitcherPersonality recentAppLayouts];
-[SBWindowingSwitcherPersonality setView:];
-[SBWindowingSwitcherPersonality identifiersInStrip];
-[SBWindowingSwitcherPersonality viewWillLayout];
-[SBWindowingSwitcherPersonality handleEvent:responseHandler:];
-[SBWindowingSwitcherPersonality view];
-[SBWindowingSwitcherPersonality switcherContextDelegate];
-[SBWindowingSwitcherPersonality windowingStrip];
-[SBWindowingSwitcherPersonality windowingViewModelForAppLayout:];
-[SBWindowingSwitcherPersonality performWithInterfaceOrientation:block:];
-[SBWindowingSwitcherPersonality bounds];
-[SBWindowingSwitcherPersonality setTimelineAuditor:];
-[SBWindowingSwitcherPersonality performWithUpdateMode:block:];
-[SBWindowingSwitcherPersonality strip];
-[SBWindowingSwitcherPersonality deckRegionModel];
-[SBWindowingSwitcherPersonality environmentMode];
-[SBWindowingSwitcherPersonality appsRegionModel];
-[SBWindowingSwitcherPersonality _minimumSizeForDisplayItem:];
-[SBWindowingSwitcherPersonality _sceneFittingSize:minimumSize:];
-[SBWindowingSwitcherPersonality _shouldResetCacheForEvent:];
-[SBWindowingSwitcherPersonality _updateCurrentAppLayout:];
-[SBWindowingSwitcherPersonality arcSwipeInitialAppLayout];
-[SBWindowingSwitcherPersonality arcSwipeNextDisplayItem];
-[SBWindowingSwitcherPersonality arcSwipePreviousDisplayItem];
-[SBWindowingSwitcherPersonality initWithSwitcherModifier:];
-[SBWindowingSwitcherPersonality spacesAfterAppsRegion];
-[SBWindowingSwitcherPersonality spacesBeforeAppsRegion];
-[SBWindowingSwitcherPersonality switcherModifier];
```
