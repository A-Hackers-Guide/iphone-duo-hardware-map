# `SBAnalyticsEventsControllerForIconController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHAnalyticsProviding`
- 4 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _shouldUseLargeHomeScreenIcons;
@"SBIconModel" _iconModel;
@"SBSHomeScreenIconStyleConfiguration" _iconStyleConfiguration;
@"SBHAnalyticsEventsController" _analyticsEventsController;
```

## Properties

```
@property (T@"SBIconModel",R,C,N,V_iconModel) iconModel;
@property (T@"SBSHomeScreenIconStyleConfiguration",R,C,N,V_iconStyleConfiguration) iconStyleConfiguration;
@property (TB,R,N,V_shouldUseLargeHomeScreenIcons) shouldUseLargeHomeScreenIcons;
@property (T@"SBHAnalyticsEventsController",&,N,V_analyticsEventsController) analyticsEventsController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAnalyticsEventsControllerForIconController analyticsEventsController];
-[SBAnalyticsEventsControllerForIconController setAnalyticsEventsController:];
-[SBAnalyticsEventsControllerForIconController shouldUseLargeHomeScreenIcons];
-[SBAnalyticsEventsControllerForIconController significantTimeChanged];
-[SBAnalyticsEventsControllerForIconController rootFolder];
-[SBAnalyticsEventsControllerForIconController iconModel];
-[SBAnalyticsEventsControllerForIconController iconStyleConfiguration];
-[SBAnalyticsEventsControllerForIconController initWithIconModel:];
-[SBAnalyticsEventsControllerForIconController _analyticsLoggingForDisplayZoomMode];
-[SBAnalyticsEventsControllerForIconController _analyticsLoggingForFixedIconLocation];
-[SBAnalyticsEventsControllerForIconController _analyticsLoggingForHomeScreenComposition];
-[SBAnalyticsEventsControllerForIconController _analyticsLoggingForIconVisibility];
-[SBAnalyticsEventsControllerForIconController _analyticsLoggingForOptimizedHomeScreen];
-[SBAnalyticsEventsControllerForIconController _homeScreenInfoForIconVisibilityAnalytics];
-[SBAnalyticsEventsControllerForIconController _homeScreenStyleTypeFromConfigurationType:variant:];
-[SBAnalyticsEventsControllerForIconController _iconAttributesForIconVisibilityAnalytics:];
-[SBAnalyticsEventsControllerForIconController _selectIconForIconVisibilityAnalytics:];
-[SBAnalyticsEventsControllerForIconController _shortVersionStringForBundleIdentifier:];
-[SBAnalyticsEventsControllerForIconController updateIconModel:];
-[SBAnalyticsEventsControllerForIconController updateIconStyleConfiguration:];
-[SBAnalyticsEventsControllerForIconController updateShouldUseLargeHomeScreenIcons:];
```
