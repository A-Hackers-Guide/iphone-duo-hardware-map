# `SBCoverSheetBlurView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PBUIWallpaperObserver`
- 8 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
d _blurRadius;
d _weighting;
@"UIColor" _dimmingColor;
@? _scaleAdjustment;
@? _alphaAdjustment;
@"UIView" _reduceTransparencyView;
q _variantToTrack;
@"SBWallpaperController" _wallpaperController;
```

## Properties

```
@property (Td,N,V_blurRadius) blurRadius;
@property (Td,N,V_weighting) weighting;
@property (T@"UIColor",&,N,V_dimmingColor) dimmingColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCoverSheetBlurView layerClass];
```

## Instance methods

```
-[SBCoverSheetBlurView wallpaperDidChangeForVariant:];
-[SBCoverSheetBlurView dimmingColor];
-[SBCoverSheetBlurView backdropLayer];
-[SBCoverSheetBlurView dealloc];
-[SBCoverSheetBlurView layoutSubviews];
-[SBCoverSheetBlurView _reduceTransparencyEnabledStateDidChange:];
-[SBCoverSheetBlurView blurRadius];
-[SBCoverSheetBlurView weighting];
-[SBCoverSheetBlurView setWeighting:];
-[SBCoverSheetBlurView setBlurRadius:];
-[SBCoverSheetBlurView setDimmingColor:];
-[SBCoverSheetBlurView _averageWallpaperColor];
-[SBCoverSheetBlurView _configureForCurrentReduceTransparencySetting];
-[SBCoverSheetBlurView _createFilters];
-[SBCoverSheetBlurView _createReduceTransparencyView];
-[SBCoverSheetBlurView _removeFilters];
-[SBCoverSheetBlurView _removeReduceTransparencyView];
-[SBCoverSheetBlurView _updateForBlurRadius:weighting:forPresentationValue:];
-[SBCoverSheetBlurView initWithFrame:wallpaperController:scaleAdjustment:alphaAdjustment:];
-[SBCoverSheetBlurView setWeighting:forPresentationValue:];
```
