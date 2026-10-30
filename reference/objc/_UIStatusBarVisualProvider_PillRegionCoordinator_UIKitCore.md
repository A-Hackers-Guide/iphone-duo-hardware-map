# `_UIStatusBarVisualProvider_PillRegionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _visualProviderImplementsBackgroundActivityPillAnimation;
@"<_UIStatusBarPillRegionVisualProvider>" _visualProvider;
@"_UIStatusBarDisplayItemPlacement" _backgroundActivityDetailPlacement;
@"_UIStatusBarDisplayItemPlacement" _pillIconPlacement;
@"_UIStatusBarRegion" _pillRegion;
@"NSTimer" _backgroundActivityDetailTimer;
```

## Properties

```
@property (T@"NSTimer",&,N,V_backgroundActivityDetailTimer) backgroundActivityDetailTimer;
@property (T@"<_UIStatusBarPillRegionVisualProvider>",W,N,V_visualProvider) visualProvider;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_backgroundActivityDetailPlacement) backgroundActivityDetailPlacement;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_pillIconPlacement) pillIconPlacement;
@property (T@"_UIStatusBarRegion",&,N,V_pillRegion) pillRegion;
```

## Instance methods

```
-[_UIStatusBarVisualProvider_PillRegionCoordinator visualProvider];
-[_UIStatusBarVisualProvider_PillRegionCoordinator setVisualProvider:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator _hideActivityDetailAndUpdate:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator _updateBackgroundActivityWithEntry:timeEntry:needsUpdate:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator animationForBackgroundActivityIcon];
-[_UIStatusBarVisualProvider_PillRegionCoordinator animationForBackgroundActivityPill];
-[_UIStatusBarVisualProvider_PillRegionCoordinator animationForBackgroundActivityPillWithDuration:scale:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator backgroundActivityDetailPlacement];
-[_UIStatusBarVisualProvider_PillRegionCoordinator backgroundActivityDetailTimer];
-[_UIStatusBarVisualProvider_PillRegionCoordinator handledUpdateOfActionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator pillIconPlacement];
-[_UIStatusBarVisualProvider_PillRegionCoordinator pillRegion];
-[_UIStatusBarVisualProvider_PillRegionCoordinator setBackgroundActivityDetailPlacement:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator setBackgroundActivityDetailTimer:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator setPillIconPlacement:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator setPillRegion:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator updateDataForBackgroundActivity:];
-[_UIStatusBarVisualProvider_PillRegionCoordinator updatePill];
-[_UIStatusBarVisualProvider_PillRegionCoordinator updateRegion:highlighted:initialPress:cornerRadius:];
```
