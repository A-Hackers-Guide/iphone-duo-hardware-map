# `_UINavigationBarVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 43 properties, 57 instance methods, 1 class methods

## Instance variables

```
q _idiom;
q _metrics;
B _inPopover;
```

## Properties

```
@property (Tq,N,V_metrics) metrics;
@property (TB,R,N) metricsIsMini;
@property (TB,R,N) metricsHasPrompt;
@property (TB,N,V_inPopover) inPopover;
@property (Tq,R,N,V_idiom) idiom;
@property (Td,R,N) backButtonIndicatorSpacing;
@property (Td,R,N) buttonHeight;
@property (Td,R,N) barHeight;
@property (Td,R,N) barPromptHeight;
@property (Td,R,N) topMargin;
@property (Td,R,N) horizontalMarginAdjustment;
@property (Td,R,N) topTitleMargin;
@property (Td,R,N) topBackMargin;
@property (Td,R,N) headingFontSize;
@property (Td,R,N) buttonFontSize;
@property (Td,R,N) leftTitleMargin;
@property (Td,R,N) leftBackTitleMargin;
@property (Td,R,N) leftBackImageMargin;
@property (Td,R,N) rightTitleMargin;
@property (Td,R,N) rightImageMargin;
@property (Td,R,N) leftTextMargin;
@property (Td,R,N) topImageMargin;
@property (Td,R,N) bottomImageMargin;
@property (Td,R,N) bottomButtonMargin;
@property (Td,R,N) promptInset;
@property (Td,R,N) interItemSpace;
@property (Td,R,N) interBlockSpace;
@property (Td,R,N) maxBackButtonProportion;
@property (Td,R,N) minBackTextWidth;
@property (Td,R,N) minBackImageWidth;
@property (Td,R,N) minButtonWidth;
@property (Td,R,N) minTitleWidth;
@property (Td,R,N) buttonImagePadding;
@property (Td,R,N) promptFontSize;
@property (T@"UIFont",R,C,N) promptFont;
@property (Td,R,N) promptTextOffset;
@property (Td,R,N) navigationItemBaselineOffset;
@property (Td,R,N) backIndicatorBottomMargin;
@property (T{UIEdgeInsets=dddd},R,N) buttonContentEdgeInsets;
@property (Td,R,N) _legacyLeftTitleMargin;
@property (Td,R,N) _legacyRightTitleMargin;
@property (Td,R,N) _legacyButtonFontSize;
@property (Td,R,N) _legacyButtonImagePadding;
```

## Class methods

```
+[_UINavigationBarVisualStyle visualStyleForIdiom:];
```

## Instance methods

```
-[_UINavigationBarVisualStyle setMetrics:];
-[_UINavigationBarVisualStyle initWithIdiom:];
-[_UINavigationBarVisualStyle buttonHeight];
-[_UINavigationBarVisualStyle topMargin];
-[_UINavigationBarVisualStyle horizontalMarginAdjustment];
-[_UINavigationBarVisualStyle metrics];
-[_UINavigationBarVisualStyle idiom];
-[_UINavigationBarVisualStyle barPromptHeight];
-[_UINavigationBarVisualStyle headingFontSize];
-[_UINavigationBarVisualStyle interBlockSpace];
-[_UINavigationBarVisualStyle leftTitleMargin];
-[_UINavigationBarVisualStyle _legacyButtonFontForStyle:];
-[_UINavigationBarVisualStyle _legacyButtonFontSize];
-[_UINavigationBarVisualStyle _legacyButtonImagePadding];
-[_UINavigationBarVisualStyle _legacyLeftTitleMargin];
-[_UINavigationBarVisualStyle _legacyRightTitleMargin];
-[_UINavigationBarVisualStyle backButtonAnimationClippingPadding];
-[_UINavigationBarVisualStyle backButtonIndicatorSpacing];
-[_UINavigationBarVisualStyle backIndicatorBottomMargin];
-[_UINavigationBarVisualStyle barHeight];
-[_UINavigationBarVisualStyle barHeightForMetrics:];
-[_UINavigationBarVisualStyle bottomButtonMargin];
-[_UINavigationBarVisualStyle bottomImageMargin];
-[_UINavigationBarVisualStyle buttonContentEdgeInsets];
-[_UINavigationBarVisualStyle buttonFontForStyle:];
-[_UINavigationBarVisualStyle buttonFontSize];
-[_UINavigationBarVisualStyle buttonImagePadding];
-[_UINavigationBarVisualStyle defaultTitleColorForUserInterfaceStyle:barStyle:];
-[_UINavigationBarVisualStyle imageButtonMarginInNavigationBar:];
-[_UINavigationBarVisualStyle inPopover];
-[_UINavigationBarVisualStyle interItemSpace];
-[_UINavigationBarVisualStyle leftBackImageMargin];
-[_UINavigationBarVisualStyle leftBackTitleMargin];
-[_UINavigationBarVisualStyle leftBackTitleMarginForCustomBackButtonBackground:];
-[_UINavigationBarVisualStyle leftTextMargin];
-[_UINavigationBarVisualStyle maxBackButtonProportion];
-[_UINavigationBarVisualStyle metricsHasPrompt];
-[_UINavigationBarVisualStyle metricsIsMini];
-[_UINavigationBarVisualStyle minBackImageWidth];
-[_UINavigationBarVisualStyle minBackTextWidth];
-[_UINavigationBarVisualStyle minButtonWidth];
-[_UINavigationBarVisualStyle minTitleWidth];
-[_UINavigationBarVisualStyle navigationBar:metricsForOrientation:hasPrompt:];
-[_UINavigationBarVisualStyle navigationItemBaselineOffset];
-[_UINavigationBarVisualStyle promptFont];
-[_UINavigationBarVisualStyle promptFontSize];
-[_UINavigationBarVisualStyle promptInset];
-[_UINavigationBarVisualStyle promptTextOffset];
-[_UINavigationBarVisualStyle rightImageMargin];
-[_UINavigationBarVisualStyle rightTitleMargin];
-[_UINavigationBarVisualStyle setInPopover:];
-[_UINavigationBarVisualStyle shouldForceLegacyLeftBackTitleMarginForCustomBackButtonBackground:];
-[_UINavigationBarVisualStyle textButtonMarginInNavigationBar:];
-[_UINavigationBarVisualStyle timingFunctionForAnimationInView:withKeyPath:isInteractive:];
-[_UINavigationBarVisualStyle topBackMargin];
-[_UINavigationBarVisualStyle topImageMargin];
-[_UINavigationBarVisualStyle topTitleMargin];
```
