# `UISegmentedControlStyleProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 28 properties, 47 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) useGeneratedImages;
@property (TB,R,N) useSelectionIndicatorStyling;
@property (TB,R,N) animateSlidingSelectionByDefault;
@property (TB,R,N) useTVStyleFocusSelection;
@property (Td,R,N) defaultContentPaddingWidth;
@property (Td,R,N) defaultTextContentPaddingWidth;
@property (Td,R,N) segmentSelectionScaleFactor;
@property (Td,R,N) segmentHidingFinalScaleFactor;
@property (TB,R,N) limitInternalLayoutAndInteractionToDefaultHeight;
@property (TB,R,N) hasTransparentBackgroundByDefault;
@property (T@"UIColor",R,N) defaultBackgroundTintColor;
@property (TB,R,N) supportsDynamicTypeByDefault;
@property (TB,R,N) supportsAXPopover;
@property (Td,R,N) defaultInterSegmentSpacing;
@property (T@"UIVibrancyEffect",R,N) selectedSegmentDefaultVibrancyEffect;
@property (T@"UIBlurEffect",R,N) selectedSegmentDefaultBlurEffect;
@property (T@"UIVibrancyEffect",R,N) selectedSegmentContentDefaultVibrancyEffect;
@property (T@"UIVibrancyEffect",R,N) unselectedSegmentContentDefaultVibrancyEffect;
@property (TB,R,N) hasShadowWithSelectedSegmentEffect;
@property (Td,R,N) mostlyInsideMargin;
@property (TB,R,N) usesContinuousCurveCorners;
@property (TB,?,R,N) wantsFocusWithoutSelection;
@property (TB,?,R,N) shouldHideSelectionOnFocusUpdate;
@property (TB,?,R,N) animateHighlightingSelectionByDefault;
@property (T@"UIVibrancyEffect",?,R,N) highlightedSegmentDefaultVibrancyEffect;
@property (TB,?,R,N) apportionsSegmentWidthsByContentByDefault;
@property (T@"UIBlurEffect",?,R,N) backgroundBlurEffect;
@property (TB,?,R,N) disablePointerEffects;
```

## Instance methods

```
-[UISegmentedControlStyleProvider segmentSelectionScaleFactor];
-[UISegmentedControlStyleProvider fontForControlSize:selected:];
-[UISegmentedControlStyleProvider fontColorForSegment:enabled:selected:state:];
-[UISegmentedControlStyleProvider usesContinuousCurveCorners];
-[UISegmentedControlStyleProvider selectionIndicatorInsetForControlSize:];
-[UISegmentedControlStyleProvider defaultHeightForControlSize:traitCollection:];
-[UISegmentedControlStyleProvider dividerWidthForControlSize:];
-[UISegmentedControlStyleProvider createBackdropView];
-[UISegmentedControlStyleProvider alignmentInsetsForControlSize:bounds:traitCollection:];
-[UISegmentedControlStyleProvider animateSlidingSelectionByDefault];
-[UISegmentedControlStyleProvider contentInsetsForControlSize:position:bounds:traitCollection:];
-[UISegmentedControlStyleProvider cornerRadiusForControlSize:];
-[UISegmentedControlStyleProvider createSegmentBezelView];
-[UISegmentedControlStyleProvider createSelectedSegmentEffectShadowView];
-[UISegmentedControlStyleProvider defaultBackgroundTintColor];
-[UISegmentedControlStyleProvider defaultContentPaddingWidth];
-[UISegmentedControlStyleProvider defaultInterSegmentSpacing];
-[UISegmentedControlStyleProvider defaultTextContentPaddingWidth];
-[UISegmentedControlStyleProvider hasShadowWithSelectedSegmentEffect];
-[UISegmentedControlStyleProvider hasTransparentBackgroundByDefault];
-[UISegmentedControlStyleProvider limitInternalLayoutAndInteractionToDefaultHeight];
-[UISegmentedControlStyleProvider mostlyInsideMargin];
-[UISegmentedControlStyleProvider segmentHidingFinalScaleFactor];
-[UISegmentedControlStyleProvider selectedSegmentContentDefaultVibrancyEffect];
-[UISegmentedControlStyleProvider selectedSegmentDefaultBlurEffect];
-[UISegmentedControlStyleProvider selectedSegmentDefaultVibrancyEffect];
-[UISegmentedControlStyleProvider supportsAXPopover];
-[UISegmentedControlStyleProvider supportsDynamicTypeByDefault];
-[UISegmentedControlStyleProvider unselectedSegmentContentDefaultVibrancyEffect];
-[UISegmentedControlStyleProvider useGeneratedImages];
-[UISegmentedControlStyleProvider useSelectionIndicatorStyling];
-[UISegmentedControlStyleProvider useTVStyleFocusSelection];
-[UISegmentedControlStyleProvider wantsFocusWithoutSelection];
-[UISegmentedControlStyleProvider highlightColorForSegmentSelected:highlighted:traitCollection:tintColor:];
-[UISegmentedControlStyleProvider touchesBegan];
-[UISegmentedControlStyleProvider touchesEnded];
-[UISegmentedControlStyleProvider animateHighlightingSelectionByDefault];
-[UISegmentedControlStyleProvider apportionsSegmentWidthsByContentByDefault];
-[UISegmentedControlStyleProvider backgroundBlurEffect];
-[UISegmentedControlStyleProvider disablePointerEffects];
-[UISegmentedControlStyleProvider feedbackGeneratorForSegmentedControl:];
-[UISegmentedControlStyleProvider highlightedSegmentDefaultVibrancyEffect];
-[UISegmentedControlStyleProvider pointerEffectClassForSegment:selected:];
-[UISegmentedControlStyleProvider selectedSegmentCompositingModeForTraitCollection:];
-[UISegmentedControlStyleProvider setActiveSegmentControl:];
-[UISegmentedControlStyleProvider shouldHideSelectionOnFocusUpdate];
-[UISegmentedControlStyleProvider updateSegmentedControl:fromTraitCollection:];
```
