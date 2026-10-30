# `SBHomeScreenDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 1 instance variables, 43 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" _iconUserInterfaceStyle;
```

## Properties

```
@property (T@"NSData",C,D,N) iconTintColorData;
@property (TB,D,N,GisSidebarPinned) sidebarPinned;
@property (TB,D,N) shouldUseLargeDefaultSizedIcons;
@property (TB,D,N) shouldUseLargeIcons;
@property (TB,D,N) shouldFudgeShortcutsToCauseMaximumPain;
@property (TB,D,N) shouldHideReportWidgetStackRotationQuickAction;
@property (TB,D,N) shouldPrepareDefaultTodayList;
@property (TB,D,N) shouldPrepareStackForDefaultTodayList;
@property (TB,D,N) shouldUpgradeEnableWidgetSuggestions;
@property (TB,D,N) shouldAddDefaultWidgetsToHomeScreen;
@property (TB,D,N) enableModalWidgetDiscoverabilityForTesting;
@property (T@"NSString",C,D,N) overriddenScreenType;
@property (TB,D,N) automaticallyAddsNewApplications;
@property (TB,D,N) showsBadgesInAppLibrary;
@property (TB,D,N) showsHomeScreenSearchAffordance;
@property (TB,D,N) pagesHaveEverBeenHidden;
@property (TB,D,N) shouldShowLibraryEducationView;
@property (TB,D,N) shouldShowWidgetIntroductionPopover;
@property (TB,D,N) userHasDeletedSuggestedWidget;
@property (TB,D,N) userDidUndoSuggestedWidget;
@property (TB,D,N) didMigrateHomeScreenDefaultsTintToPosterBoard;
@property (T@"NSArray",C,D,N) focusModesRequiringIntroduction;
@property (T@"NSString",C,D,N) leftOfHomeAppBundleIdentifier;
@property (TB,D,N) shouldIgnoreMinimumRequiredSDKVersionForWidgets;
@property (TB,D,N) shouldInsertDownloadFileStackIconToFloatingDock;
@property (T@"NSString",C,N,V_iconUserInterfaceStyle) iconUserInterfaceStyle;
@property (Td,D,N) iconUserInterfaceStyleVariation;
@property (Td,D,N) iconUserInterfaceStyleLuminance;
@property (Td,D,N) iconUserInterfaceStyleSaturation;
@property (TB,D,N) shouldUseFlatIconsEverywhere;
@property (TB,D,N) shouldDisableSpecularEverywhere;
@property (TB,D,N) shouldDisableSpecularEverywhereUsingLSSAssertion;
@property (TB,D,N) shouldDisableWidgetSpecular;
@property (TB,D,N) shouldDisableDockSpecular;
@property (TB,D,N) shouldDisableFolderSpecular;
@property (TB,D,N) shouldDisableGlassDock;
@property (TB,D,N) shouldExcludeDockShadow;
@property (TB,D,N) shouldExcludeSearchShadow;
@property (TB,D,N) shouldExcludeAllClearGlassShadows;
@property (TB,D,N) shouldDisableParallax;
@property (TB,D,N) shouldDisableParallaxOnPageControl;
@property (TB,D,N,GisVerboseLoggingEnabled) verboseLoggingEnabled;
@property (TB,D,N) enableHomeScreenWallpaperDimming;
```

## Instance methods

```
-[SBHomeScreenDefaults _bindAndRegisterDefaults];
-[SBHomeScreenDefaults iconTintColor];
-[SBHomeScreenDefaults setIconTintColor:];
-[SBHomeScreenDefaults _isV68Device];
-[SBHomeScreenDefaults automaticallyAddsNewApplicationsExists];
-[SBHomeScreenDefaults iconUserInterfaceStyle];
-[SBHomeScreenDefaults observeIconTintColorOnQueue:withBlock:];
-[SBHomeScreenDefaults setIconUserInterfaceStyle:];
```
