# `_UIStatusBarVisualProvider_CarPlay`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarCellularItemTypeStringProvider`, `_UIStatusBarVisualProvider`, `_UIStatusBarPillRegionVisualProvider`
- 6 instance variables, 14 properties, 33 instance methods, 4 class methods

## Instance variables

```
B _showingSensorActivityIndicator;
B _showingPill;
@"_UIStatusBar" _statusBar;
@"_UIStatusBarVisualProvider_PillRegionCoordinator" _pillRegionCoordinator;
@"_UIStatusBarRegion" _timeRegion;
@"_UIStatusBarRegion" _radarRegion;
```

## Properties

```
@property (T@"_UIStatusBarVisualProvider_PillRegionCoordinator",&,N,V_pillRegionCoordinator) pillRegionCoordinator;
@property (T@"_UIStatusBarRegion",&,N,V_timeRegion) timeRegion;
@property (T@"_UIStatusBarRegion",&,N,V_radarRegion) radarRegion;
@property (TB,N,V_showingSensorActivityIndicator) showingSensorActivityIndicator;
@property (TB,N,V_showingPill) showingPill;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIStatusBar",W,N,V_statusBar) statusBar;
@property (TB,R,N) supportsIndirectPointerTouchActions;
@property (T@"UIFont",R,N) clockFont;
@property (TB,?,R,N) canFixupDisplayItemAttributes;
@property (TB,N) expanded;
```

## Class methods

```
+[_UIStatusBarVisualProvider_CarPlay requiresIterativeOverflowLayout];
+[_UIStatusBarVisualProvider_CarPlay intrinsicContentSizeForOrientation:];
+[_UIStatusBarVisualProvider_CarPlay scalesWithScreenNativeScale];
+[_UIStatusBarVisualProvider_CarPlay visualProviderSubclassForScreen:visualProviderInfo:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_CarPlay statusBar];
-[_UIStatusBarVisualProvider_CarPlay setExpanded:];
-[_UIStatusBarVisualProvider_CarPlay setStatusBar:];
-[_UIStatusBarVisualProvider_CarPlay init];
-[_UIStatusBarVisualProvider_CarPlay styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_CarPlay clockFont];
-[_UIStatusBarVisualProvider_CarPlay expanded];
-[_UIStatusBarVisualProvider_CarPlay setRadarRegion:];
-[_UIStatusBarVisualProvider_CarPlay setShowingPill:];
-[_UIStatusBarVisualProvider_CarPlay _animationForPillTime];
-[_UIStatusBarVisualProvider_CarPlay _animationForSensorIndicator];
-[_UIStatusBarVisualProvider_CarPlay _defaultScaleAnimationWithIdentifier:];
-[_UIStatusBarVisualProvider_CarPlay actionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider_CarPlay additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_CarPlay animatedTypeDisplayItemSpacingFactorForCellularType:];
-[_UIStatusBarVisualProvider_CarPlay condensedFontForCellularType:defaultFont:baselineOffset:];
-[_UIStatusBarVisualProvider_CarPlay itemCreated:];
-[_UIStatusBarVisualProvider_CarPlay orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_CarPlay overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_CarPlay pillRegionCoordinator];
-[_UIStatusBarVisualProvider_CarPlay radarRegion];
-[_UIStatusBarVisualProvider_CarPlay removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_CarPlay setPillRegionCoordinator:];
-[_UIStatusBarVisualProvider_CarPlay setShowingSensorActivityIndicator:];
-[_UIStatusBarVisualProvider_CarPlay setTimeRegion:];
-[_UIStatusBarVisualProvider_CarPlay setupInContainerView:];
-[_UIStatusBarVisualProvider_CarPlay showSensorActivityIndicatorWithoutPortalView];
-[_UIStatusBarVisualProvider_CarPlay showingPill];
-[_UIStatusBarVisualProvider_CarPlay showingSensorActivityIndicator];
-[_UIStatusBarVisualProvider_CarPlay stringForCellularType:condensed:];
-[_UIStatusBarVisualProvider_CarPlay supportsIndirectPointerTouchActions];
-[_UIStatusBarVisualProvider_CarPlay timeRegion];
-[_UIStatusBarVisualProvider_CarPlay willUpdateWithData:];
```
