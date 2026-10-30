# `_TtC5UIKit27_UISliderFluidVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UISliderFluidStyleVisualElement`, `UIGestureRecognizerDelegate`, `_UIFluidSliderDirectDrivingDelegate`
- 27 instance variables, 6 properties, 76 instance methods, 0 class methods

## Instance variables

```
_$sSo8UISliderCSgXw slider;
_$sSo17UISliderDataModelCSg data;
_$sSo6UIViewC clipView;
_$sSo6UIViewC barView;
_$sSo6UIViewC trackView;
_$sSaySo6UIViewCG tickViews;
_$sSo6UIViewCSg tickView;
_$sSo18UIVisualEffectViewCSg barEffectView;
_$sSo18UIVisualEffectViewCSg leftTrackEffectView;
_$sSo18UIVisualEffectViewCSg rightTrackEffectView;
_$sSo6UIViewCSg minimumView;
_$sSo6UIViewCSg maximumView;
Swift.Bool usingSliderStyling;
_$sSo31_UIFluidSliderInteractionUpdateCSg lastUpdate;
Swift.Bool hasPlayedBounceForCurrentValue;
Swift.Bool changeWithVolumeButtons;
_$sSo25_UIFluidSliderInteractionCSg fluidInteraction;
_$sSo28UILongPressGestureRecognizerCSg expansionGesture;
__C.TouchType touchType;
Swift.Bool isInteractivelyChanging;
UIKit._UISliderFluidVisualElement.InteractiveChangeState interactiveChangeState;
_$sSd paddingAroundImage;
CoreGraphics.CGFloat defaultExpansionFactor;
CoreGraphics.CGFloat defaultHorizontalExpansionFactor;
_$sSd disabledAlpha;
_$sSd acceleratedThumbFillRange;
__C._UISliderFluidUpdateSource fluidUpdateSource;
```

## Properties

```
@property (T@"UISlider",N,W,Vslider) slider;
@property (T@"UISliderDataModel",N,&,Vdata) data;
@property (TB,N,VchangeWithVolumeButtons) changeWithVolumeButtons;
@property (TQ,N,VfluidUpdateSource) fluidUpdateSource;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) bounds;
```

## Instance methods

```
-[_TtC5UIKit27_UISliderFluidVisualElement cancelTouchTracking];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetThumbTintColor];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMaximumTrackImageForState:];
-[_TtC5UIKit27_UISliderFluidVisualElement setValue:animated:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetSelected];
-[_TtC5UIKit27_UISliderFluidVisualElement thumbView];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetValues];
-[_TtC5UIKit27_UISliderFluidVisualElement setFluidUpdateSource:];
-[_TtC5UIKit27_UISliderFluidVisualElement minimumValueImageRectForBounds:];
-[_TtC5UIKit27_UISliderFluidVisualElement gestureRecognizer:shouldReceiveTouch:];
-[_TtC5UIKit27_UISliderFluidVisualElement handleExpansionGesture:];
-[_TtC5UIKit27_UISliderFluidVisualElement valueTextRectForBounds:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetEnabled];
-[_TtC5UIKit27_UISliderFluidVisualElement _intrinsicSizeWithinSize:];
-[_TtC5UIKit27_UISliderFluidVisualElement maxTrackView];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetHighlighted];
-[_TtC5UIKit27_UISliderFluidVisualElement didUpdateConfiguration];
-[_TtC5UIKit27_UISliderFluidVisualElement thumbHitEdgeInsets];
-[_TtC5UIKit27_UISliderFluidVisualElement createThumbView];
-[_TtC5UIKit27_UISliderFluidVisualElement endTrackingWithTouch:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement currentMaximumTrackImage];
-[_TtC5UIKit27_UISliderFluidVisualElement continueTrackingWithTouch:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement data];
-[_TtC5UIKit27_UISliderFluidVisualElement didPerformLayout];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMinimumValueImage];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetUserInteractionEnabled];
-[_TtC5UIKit27_UISliderFluidVisualElement isAnimatingValueChange];
-[_TtC5UIKit27_UISliderFluidVisualElement setSlider:];
-[_TtC5UIKit27_UISliderFluidVisualElement currentMinimumTrackImage];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetFluidTrackHidden];
-[_TtC5UIKit27_UISliderFluidVisualElement hitTest:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement currentThumbImage];
-[_TtC5UIKit27_UISliderFluidVisualElement beginTrackingWithTouch:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMinimumTrackTintColor];
-[_TtC5UIKit27_UISliderFluidVisualElement changeWithVolumeButtons];
-[_TtC5UIKit27_UISliderFluidVisualElement setBounds:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMaximumTrackImageForStates];
-[_TtC5UIKit27_UISliderFluidVisualElement sizeThatFits:];
-[_TtC5UIKit27_UISliderFluidVisualElement gestureRecognizerShouldBegin:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetThumbImageForStates];
-[_TtC5UIKit27_UISliderFluidVisualElement driver:shouldBeginAtPoint:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMaximumTrackTintColor];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetThumbImageForState:];
-[_TtC5UIKit27_UISliderFluidVisualElement didUpdateSliderStyle];
-[_TtC5UIKit27_UISliderFluidVisualElement setData:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetShowValue];
-[_TtC5UIKit27_UISliderFluidVisualElement maximumValueImageRectForBounds:];
-[_TtC5UIKit27_UISliderFluidVisualElement didChangeMinimumTrackVisibleWithDuration:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetSpeedMultiplier];
-[_TtC5UIKit27_UISliderFluidVisualElement slider];
-[_TtC5UIKit27_UISliderFluidVisualElement gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_TtC5UIKit27_UISliderFluidVisualElement thumbViewNeue];
-[_TtC5UIKit27_UISliderFluidVisualElement setFrame:];
-[_TtC5UIKit27_UISliderFluidVisualElement setChangeWithVolumeButtons:];
-[_TtC5UIKit27_UISliderFluidVisualElement driver:shouldAdjustValueForProposedValue:adjustedValue:startValue:endValue:];
-[_TtC5UIKit27_UISliderFluidVisualElement bounds];
-[_TtC5UIKit27_UISliderFluidVisualElement minTrackView];
-[_TtC5UIKit27_UISliderFluidVisualElement _controlTouchBegan:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement fluidUpdateSource];
-[_TtC5UIKit27_UISliderFluidVisualElement thumbRectForBounds:trackRect:value:];
-[_TtC5UIKit27_UISliderFluidVisualElement didUpdateTraitCollection];
-[_TtC5UIKit27_UISliderFluidVisualElement initWithCoder:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMinimumTrackImageForState:];
-[_TtC5UIKit27_UISliderFluidVisualElement trackRectForBounds:];
-[_TtC5UIKit27_UISliderFluidVisualElement minValueImageView];
-[_TtC5UIKit27_UISliderFluidVisualElement _controlTouchMoved:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetThumbEnabled];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMinimumTrackImageForStates];
-[_TtC5UIKit27_UISliderFluidVisualElement initWithFrame:];
-[_TtC5UIKit27_UISliderFluidVisualElement cancelMouseTracking];
-[_TtC5UIKit27_UISliderFluidVisualElement overrideTrackingState:];
-[_TtC5UIKit27_UISliderFluidVisualElement maxValueImageView];
-[_TtC5UIKit27_UISliderFluidVisualElement _controlTouchEnded:withEvent:];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetContinuous];
-[_TtC5UIKit27_UISliderFluidVisualElement frame];
-[_TtC5UIKit27_UISliderFluidVisualElement didSetMaximumValueImage];
```
