# `UISegmentedControlDefaultStyleProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISegmentedControlStyleProvider`
- 0 instance variables, 32 properties, 36 instance methods, 0 class methods

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISegmentedControlDefaultStyleProvider wantsFocusWithoutSelection];
-[UISegmentedControlDefaultStyleProvider segmentSelectionScaleFactor];
-[UISegmentedControlDefaultStyleProvider fontForControlSize:selected:];
-[UISegmentedControlDefaultStyleProvider fontColorForSegment:enabled:selected:state:];
-[UISegmentedControlDefaultStyleProvider usesContinuousCurveCorners];
-[UISegmentedControlDefaultStyleProvider selectionIndicatorInsetForControlSize:];
-[UISegmentedControlDefaultStyleProvider defaultHeightForControlSize:traitCollection:];
-[UISegmentedControlDefaultStyleProvider dividerWidthForControlSize:];
-[UISegmentedControlDefaultStyleProvider createBackdropView];
-[UISegmentedControlDefaultStyleProvider alignmentInsetsForControlSize:bounds:];
-[UISegmentedControlDefaultStyleProvider alignmentInsetsForControlSize:bounds:traitCollection:];
-[UISegmentedControlDefaultStyleProvider animateSlidingSelectionByDefault];
-[UISegmentedControlDefaultStyleProvider contentInsetsForControlSize:position:bounds:traitCollection:];
-[UISegmentedControlDefaultStyleProvider cornerRadiusForControlSize:];
-[UISegmentedControlDefaultStyleProvider createSegmentBezelView];
-[UISegmentedControlDefaultStyleProvider createSelectedSegmentEffectShadowView];
-[UISegmentedControlDefaultStyleProvider defaultBackgroundTintColor];
-[UISegmentedControlDefaultStyleProvider defaultContentPaddingWidth];
-[UISegmentedControlDefaultStyleProvider defaultInterSegmentSpacing];
-[UISegmentedControlDefaultStyleProvider defaultTextContentPaddingWidth];
-[UISegmentedControlDefaultStyleProvider disablePointerEffects];
-[UISegmentedControlDefaultStyleProvider hasShadowWithSelectedSegmentEffect];
-[UISegmentedControlDefaultStyleProvider hasTransparentBackgroundByDefault];
-[UISegmentedControlDefaultStyleProvider limitInternalLayoutAndInteractionToDefaultHeight];
-[UISegmentedControlDefaultStyleProvider maskToCornerRadius];
-[UISegmentedControlDefaultStyleProvider mostlyInsideMargin];
-[UISegmentedControlDefaultStyleProvider segmentHidingFinalScaleFactor];
-[UISegmentedControlDefaultStyleProvider selectedSegmentContentDefaultVibrancyEffect];
-[UISegmentedControlDefaultStyleProvider selectedSegmentDefaultBlurEffect];
-[UISegmentedControlDefaultStyleProvider selectedSegmentDefaultVibrancyEffect];
-[UISegmentedControlDefaultStyleProvider supportsAXPopover];
-[UISegmentedControlDefaultStyleProvider supportsDynamicTypeByDefault];
-[UISegmentedControlDefaultStyleProvider unselectedSegmentContentDefaultVibrancyEffect];
-[UISegmentedControlDefaultStyleProvider useGeneratedImages];
-[UISegmentedControlDefaultStyleProvider useSelectionIndicatorStyling];
-[UISegmentedControlDefaultStyleProvider useTVStyleFocusSelection];
```
