# `SBElasticSliderView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CCUIContinuousSliderView`
- 13 instance variables, 10 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"MTMaterialView" _captureOnlyMaterialView;
@"MTMaterialView" _baseMaterialView;
@"UIView" _shadowView;
@"UIView" _maskView;
d _cornerRadiusMinorAxisFraction;
d _regularMinorAxisDimension;
d _compactMinorAxisDimension;
d _additiveGlyphScaleFactor;
Q _shadowMode;
@"UIView" _leadingAccessoryView;
@"UIView" _trailingAccessoryView;
Q _accessoryLayoutEdge;
d _accessoryViewPadding;
```

## Properties

```
@property (Td,N,V_cornerRadiusMinorAxisFraction) cornerRadiusMinorAxisFraction;
@property (Td,N,V_regularMinorAxisDimension) regularMinorAxisDimension;
@property (Td,N,V_compactMinorAxisDimension) compactMinorAxisDimension;
@property (Td,N,V_additiveGlyphScaleFactor) additiveGlyphScaleFactor;
@property (TQ,N,V_shadowMode) shadowMode;
@property (T{UIEdgeInsets=dddd},R,N) shadowOutsets;
@property (T@"UIView",&,N,V_leadingAccessoryView) leadingAccessoryView;
@property (T@"UIView",&,N,V_trailingAccessoryView) trailingAccessoryView;
@property (TQ,N,V_accessoryLayoutEdge) accessoryLayoutEdge;
@property (Td,N,V_accessoryViewPadding) accessoryViewPadding;
```

## Instance methods

```
-[SBElasticSliderView _updateCornerRadius];
-[SBElasticSliderView applyContinuousSliderCornerRadius:];
-[SBElasticSliderView _minorAxisElasticLength];
-[SBElasticSliderView setAxis:];
-[SBElasticSliderView _layoutAccessoryViews];
-[SBElasticSliderView _fractionToRegularMetrics];
-[SBElasticSliderView createBackgroundView];
-[SBElasticSliderView compactMinorAxisDimension];
-[SBElasticSliderView setAdditiveGlyphScaleFactor:];
-[SBElasticSliderView setLeadingAccessoryView:];
-[SBElasticSliderView setTrailingAccessoryView:];
-[SBElasticSliderView glyphCenter];
-[SBElasticSliderView leadingAccessoryView];
-[SBElasticSliderView layoutElasticContentViews];
-[SBElasticSliderView _updateShadowMode];
-[SBElasticSliderView shadowOutsets];
-[SBElasticSliderView accessoryLayoutEdge];
-[SBElasticSliderView setShadowMode:];
-[SBElasticSliderView trailingAccessoryView];
-[SBElasticSliderView setRegularMinorAxisDimension:];
-[SBElasticSliderView accessoryViewPadding];
-[SBElasticSliderView _createElasticBackgroundView];
-[SBElasticSliderView shadowMode];
-[SBElasticSliderView additiveGlyphScaleFactor];
-[SBElasticSliderView setCornerRadiusMinorAxisFraction:];
-[SBElasticSliderView _elasticGlyphCenterForDefaultGlyphCenter:];
-[SBElasticSliderView _usesSolariumBackground];
-[SBElasticSliderView setCompactMinorAxisDimension:];
-[SBElasticSliderView setAccessoryLayoutEdge:];
-[SBElasticSliderView regularMinorAxisDimension];
-[SBElasticSliderView _updateGlyphScaleForAdditiveScaleOrAxisUpdate];
-[SBElasticSliderView setAccessoryViewPadding:];
-[SBElasticSliderView initWithFrame:];
-[SBElasticSliderView setContinuousSliderCornerRadius:];
-[SBElasticSliderView cornerRadiusMinorAxisFraction];
```
