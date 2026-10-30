# `CEKApertureButton`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 17 instance variables, 18 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _shouldShowApertureValue;
B _wantsBackground;
B __rightToLeftFormatting;
@"<CEKApertureButtonDelegate>" _delegate;
d _apertureValue;
q _expansionDirection;
q _orientation;
@"UIImageView" __circleOutlineView;
@"UILabel" __symbolLabel;
@"UILabel" __valueLabel;
@"UIImageView" __circleBackgroundView;
@"NSNumberFormatter" __decimalFormatter;
@"NSNumberFormatter" __wholeNumberFormatter;
d __cachedSpaceWidth;
d __cachedSymbolLabelWidth;
d __cachedValueLabelWidth;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _tappableEdgeInsets;
```

## Properties

```
@property (T@"UIImageView",R,N,V__circleOutlineView) _circleOutlineView;
@property (T@"UILabel",R,N,V__symbolLabel) _symbolLabel;
@property (T@"UILabel",R,N,V__valueLabel) _valueLabel;
@property (T@"UIImageView",&,N,V__circleBackgroundView) _circleBackgroundView;
@property (T@"NSNumberFormatter",R,N,V__decimalFormatter) _decimalFormatter;
@property (T@"NSNumberFormatter",R,N,V__wholeNumberFormatter) _wholeNumberFormatter;
@property (TB,R,N,G_isRightToLeftFormatting,V__rightToLeftFormatting) _rightToLeftFormatting;
@property (Td,R,N,V__cachedSpaceWidth) _cachedSpaceWidth;
@property (Td,R,N,V__cachedSymbolLabelWidth) _cachedSymbolLabelWidth;
@property (Td,N,S_setCachedValueLabelWidth:,V__cachedValueLabelWidth) _cachedValueLabelWidth;
@property (T@"<CEKApertureButtonDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_apertureValue) apertureValue;
@property (TB,N,V_shouldShowApertureValue) shouldShowApertureValue;
@property (Tq,N,V_expansionDirection) expansionDirection;
@property (TB,N,GisActive) active;
@property (TB,N,V_wantsBackground) wantsBackground;
@property (T{UIEdgeInsets=dddd},N,V_tappableEdgeInsets) tappableEdgeInsets;
@property (Tq,N,V_orientation) orientation;
```

## Instance methods

```
-[CEKApertureButton setOrientation:animated:];
-[CEKApertureButton setOrientation:];
-[CEKApertureButton intrinsicContentSize];
-[CEKApertureButton alignmentRectInsets];
-[CEKApertureButton wantsBackground];
-[CEKApertureButton orientation];
-[CEKApertureButton _updateBackgroundView];
-[CEKApertureButton layoutSubviews];
-[CEKApertureButton setActive:];
-[CEKApertureButton setDelegate:];
-[CEKApertureButton tintColorDidChange];
-[CEKApertureButton setApertureValue:];
-[CEKApertureButton setHighlighted:];
-[CEKApertureButton setTappableEdgeInsets:];
-[CEKApertureButton delegate];
-[CEKApertureButton isActive];
-[CEKApertureButton tappableEdgeInsets];
-[CEKApertureButton initWithFrame:];
-[CEKApertureButton _updateColorsAnimated:];
-[CEKApertureButton setActive:animated:];
-[CEKApertureButton apertureValue];
-[CEKApertureButton setExpansionDirection:];
-[CEKApertureButton setShouldShowApertureValue:animated:];
-[CEKApertureButton setWantsBackground:];
-[CEKApertureButton _setLayer:highlighted:animated:];
-[CEKApertureButton _cachedSpaceWidth];
-[CEKApertureButton _cachedSymbolLabelWidth];
-[CEKApertureButton _cachedValueLabelWidth];
-[CEKApertureButton _circleBackgroundView];
-[CEKApertureButton _circleImageWithColor:];
-[CEKApertureButton _circleOutlineView];
-[CEKApertureButton _decimalFormatter];
-[CEKApertureButton _expansionInsets];
-[CEKApertureButton _isRightToLeftFormatting];
-[CEKApertureButton _rotateView:withInterfaceOrientation:animated:];
-[CEKApertureButton _setCachedValueLabelWidth:];
-[CEKApertureButton _setCenterAndBoundsForView:frame:];
-[CEKApertureButton _symbolLabel];
-[CEKApertureButton _updateSymbolLabelOrientationAnimated:];
-[CEKApertureButton _updateValueLabel];
-[CEKApertureButton _valueLabel];
-[CEKApertureButton _wholeNumberFormatter];
-[CEKApertureButton expansionDirection];
-[CEKApertureButton setShouldShowApertureValue:];
-[CEKApertureButton set_circleBackgroundView:];
-[CEKApertureButton shouldShowApertureValue];
```
