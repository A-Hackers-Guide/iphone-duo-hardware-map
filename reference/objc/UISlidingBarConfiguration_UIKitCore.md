# `UISlidingBarConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 14 instance variables, 24 properties, 59 instance methods, 0 class methods

## Instance variables

```
(?="value"I"flags"{?="leadingMayBeHidden"b1"trailingMayBeHidden"b1"supplementaryMayBeHidden"b1"allowMixedSideBySideAndOverlay"b1"allowTotalWidthGreaterThanParent"b1"forceOverlay"b1"leadingBorderWidthIsInPixels"b1"trailingBorderWidthIsInPixels"b1"shouldFadeStaticNavBarButton"b1"supplementaryAdoptsPrimaryBackgroundStyle"b1"borderAbuttingMainRendersAsShadow"b1"reserved"b19}) _configurationFlags;
q _supplementaryEdge;
d _minimumMainWidthFraction;
d _minimumMainWidthFractionForSecondColumn;
d _maximumMainWidth;
d _rubberBandExtension;
@"NSArray" _leadingWidths;
@"NSArray" _trailingWidths;
@"NSArray" _supplementaryWidths;
@"UIColor" _borderColor;
d __rawLeadingBorderWidth;
d __rawTrailingBorderWidth;
q __leadingBackgroundStyle;
q __trailingBackgroundStyle;
```

## Properties

```
@property (TB,N) borderAbuttingMainRendersAsShadow;
@property (Td,N,S_setRawLeadingBorderWidth:,V__rawLeadingBorderWidth) _rawLeadingBorderWidth;
@property (TB,N,S_setLeadingBorderWidthIsInPixels:) _leadingBorderWidthIsInPixels;
@property (Td,N,S_setRawTrailingBorderWidth:,V__rawTrailingBorderWidth) _rawTrailingBorderWidth;
@property (TB,N,S_setTrailingBorderWidthIsInPixels:) _trailingBorderWidthIsInPixels;
@property (Tq,N,S_setLeadingBackgroundStyle:,V__leadingBackgroundStyle) _leadingBackgroundStyle;
@property (Tq,N,S_setTrailingBackgroundStyle:,V__trailingBackgroundStyle) _trailingBackgroundStyle;
@property (TB,N,S_setSupplementaryAdoptsPrimaryBackgroundStyle:) _supplementaryAdoptsPrimaryBackgroundStyle;
@property (Td,N,V_minimumMainWidthFraction) minimumMainWidthFraction;
@property (Td,N,V_minimumMainWidthFractionForSecondColumn) minimumMainWidthFractionForSecondColumn;
@property (Td,N,V_maximumMainWidth) maximumMainWidth;
@property (Tq,N,V_supplementaryEdge) supplementaryEdge;
@property (TB,N) leadingMayBeHidden;
@property (TB,N) trailingMayBeHidden;
@property (TB,N) supplementaryMayBeHidden;
@property (Td,N,V_rubberBandExtension) rubberBandExtension;
@property (T@"NSArray",C,N,V_leadingWidths) leadingWidths;
@property (T@"NSArray",C,N,V_trailingWidths) trailingWidths;
@property (T@"NSArray",C,N,V_supplementaryWidths) supplementaryWidths;
@property (T@"UIColor",&,N,V_borderColor) borderColor;
@property (TB,N) allowMixedSideBySideAndOverlay;
@property (TB,N) allowTotalWidthGreaterThanParent;
@property (TB,N) forceOverlay;
@property (TB,N) shouldFadeStaticNavBarButton;
```

## Instance methods

```
-[UISlidingBarConfiguration setBorderColor:];
-[UISlidingBarConfiguration setShouldFadeStaticNavBarButton:];
-[UISlidingBarConfiguration init];
-[UISlidingBarConfiguration shouldFadeStaticNavBarButton];
-[UISlidingBarConfiguration hash];
-[UISlidingBarConfiguration description];
-[UISlidingBarConfiguration copyWithZone:];
-[UISlidingBarConfiguration isEqual:];
-[UISlidingBarConfiguration borderColor];
-[UISlidingBarConfiguration setTrailingBorderWidthInPoints:];
-[UISlidingBarConfiguration setTrailingBorderWidthInPixels:];
-[UISlidingBarConfiguration _leadingBackgroundStyle];
-[UISlidingBarConfiguration _leadingBorderWidthIsInPixels];
-[UISlidingBarConfiguration _rawLeadingBorderWidth];
-[UISlidingBarConfiguration _rawTrailingBorderWidth];
-[UISlidingBarConfiguration _setLeadingBackgroundStyle:];
-[UISlidingBarConfiguration _setLeadingBorderWidthIsInPixels:];
-[UISlidingBarConfiguration _setRawLeadingBorderWidth:];
-[UISlidingBarConfiguration _setRawTrailingBorderWidth:];
-[UISlidingBarConfiguration _setSupplementaryAdoptsPrimaryBackgroundStyle:];
-[UISlidingBarConfiguration _setTrailingBackgroundStyle:];
-[UISlidingBarConfiguration _setTrailingBorderWidthIsInPixels:];
-[UISlidingBarConfiguration _supplementaryAdoptsPrimaryBackgroundStyle];
-[UISlidingBarConfiguration _trailingBackgroundStyle];
-[UISlidingBarConfiguration _trailingBorderWidthIsInPixels];
-[UISlidingBarConfiguration allowMixedSideBySideAndOverlay];
-[UISlidingBarConfiguration allowTotalWidthGreaterThanParent];
-[UISlidingBarConfiguration borderAbuttingMainRendersAsShadow];
-[UISlidingBarConfiguration forceOverlay];
-[UISlidingBarConfiguration leadingBorderWidthForScale:];
-[UISlidingBarConfiguration leadingMayBeHidden];
-[UISlidingBarConfiguration leadingWidths];
-[UISlidingBarConfiguration maximumMainWidth];
-[UISlidingBarConfiguration minimumMainWidthFraction];
-[UISlidingBarConfiguration minimumMainWidthFractionForSecondColumn];
-[UISlidingBarConfiguration rubberBandExtension];
-[UISlidingBarConfiguration setAllowMixedSideBySideAndOverlay:];
-[UISlidingBarConfiguration setAllowTotalWidthGreaterThanParent:];
-[UISlidingBarConfiguration setBorderAbuttingMainRendersAsShadow:];
-[UISlidingBarConfiguration setForceOverlay:];
-[UISlidingBarConfiguration setLeadingBorderWidthInPixels:];
-[UISlidingBarConfiguration setLeadingBorderWidthInPoints:];
-[UISlidingBarConfiguration setLeadingMayBeHidden:];
-[UISlidingBarConfiguration setLeadingWidths:];
-[UISlidingBarConfiguration setMaximumMainWidth:];
-[UISlidingBarConfiguration setMinimumMainWidthFraction:];
-[UISlidingBarConfiguration setMinimumMainWidthFractionForSecondColumn:];
-[UISlidingBarConfiguration setRubberBandExtension:];
-[UISlidingBarConfiguration setSupplementaryEdge:];
-[UISlidingBarConfiguration setSupplementaryMayBeHidden:];
-[UISlidingBarConfiguration setSupplementaryWidths:];
-[UISlidingBarConfiguration setTrailingMayBeHidden:];
-[UISlidingBarConfiguration setTrailingWidths:];
-[UISlidingBarConfiguration supplementaryEdge];
-[UISlidingBarConfiguration supplementaryMayBeHidden];
-[UISlidingBarConfiguration supplementaryWidths];
-[UISlidingBarConfiguration trailingBorderWidthForScale:];
-[UISlidingBarConfiguration trailingMayBeHidden];
-[UISlidingBarConfiguration trailingWidths];
```
