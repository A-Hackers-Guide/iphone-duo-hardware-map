# `SBAppSwitcherDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 24 properties, 3 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",&,D,N) recentsPlistRepresentation;
@property (TB,D,N) chamoisWindowingEnabled;
@property (TB,D,N) chamoisHideStrips;
@property (TB,D,N) chamoisHideDock;
@property (TB,D,N) flexibleWindowingAutomaticStageCreationEnabledExternal;
@property (TB,D,N) flexibleWindowingPreviouslyEnabledAutomaticStageCreation;
@property (TB,D,N) chamoisHideStripsExternal;
@property (TB,D,N) chamoisHideDockExternal;
@property (TB,D,N) medusaMultitaskingEnabled;
@property (TB,D,N) flexibleWindowingManualStageCreationShouldRestorePreviousOpenWindows;
@property (TB,D,N) flexibleWindowingDoubleTapTopOfWindowToZoomEnabled;
@property (TB,D,N) backgroundNethermostWindows;
@property (TB,D,N) wantsManyForegroundWindows;
@property (TQ,D,N) bottomEdgeGestureSwipeCount;
@property (TB,R,D,N,GisSpringBoardKillable) springBoardKillable;
@property (TB,R,D,N,GareTrackpadSwitcherGesturesEnabled) trackpadSwitcherGesturesEnabled;
@property (TB,D,N) shouldShowSplitPeekEducation;
@property (TB,D,N) shouldShowSlideOverPeekEducation;
@property (TB,D,N) shouldUpdateExternalDisplayMirroringWhenWindowManagementStyleUpdates;
@property (TB,D,N) hasEverUsedMultiAppConfiguration;
@property (T@"NSDate",D,N) lastMultitaskingModeSwitchDate;
@property (T@"NSArray",R,D,N) legacyRecentApplications;
@property (T@"NSArray",R,D,N) legacyRecentDisplayItems;
@property (T@"NSArray",R,D,N) legacyRecentDisplayItemRoles;
```

## Instance methods

```
-[SBAppSwitcherDefaults _bindAndRegisterDefaults];
-[SBAppSwitcherDefaults _shouldMedusaMultitaskingBeEnabledByDefault];
-[SBAppSwitcherDefaults clearLegacyDefaults];
```
