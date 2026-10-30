# `SBFlashlightElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemApertureProvidedContentElement`
- Protocols: `SAElementIdentifying`, `SBSystemApertureContextProviding`, `SBSystemApertureLayoutCustomizing`
- 7 instance variables, 24 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"SBUISystemApertureCAPackageContentProvider" _leadingPackageViewProvider;
@"SBUISystemApertureTextContentProvider" _trailingTextProvider;
@"SBUISystemApertureCAPackageButton" _expandedLeadingPackageButton;
@"UILabel" _expandedTitleLabel;
@"UILabel" _expandedTrailingLabel;
Q _style;
Q _state;
```

## Properties

```
@property (T@"SBUISystemApertureCAPackageContentProvider",R,N,V_leadingPackageViewProvider) leadingPackageViewProvider;
@property (T@"SBUISystemApertureTextContentProvider",R,N,V_trailingTextProvider) trailingTextProvider;
@property (T@"SBUISystemApertureCAPackageButton",R,N,V_expandedLeadingPackageButton) expandedLeadingPackageButton;
@property (T@"UILabel",R,N,V_expandedTitleLabel) expandedTitleLabel;
@property (T@"UILabel",R,N,V_expandedTrailingLabel) expandedTrailingLabel;
@property (TQ,R,N,V_style) style;
@property (TQ,N,V_state) state;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
```

## Instance methods

```
-[SBFlashlightElement keyColor];
-[SBFlashlightElement overridesConcentricPaddingForView:inLayoutMode:];
-[SBFlashlightElement concentricPaddingOverrideForView:inLayoutMode:];
-[SBFlashlightElement clientIdentifier];
-[SBFlashlightElement isProvidedViewConcentric:inLayoutMode:];
-[SBFlashlightElement setState:];
-[SBFlashlightElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBFlashlightElement elementIdentifier];
-[SBFlashlightElement style];
-[SBFlashlightElement isMinimalPresentationPossible];
-[SBFlashlightElement layoutHostContainerViewDidLayoutSubviews:];
-[SBFlashlightElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBFlashlightElement state];
-[SBFlashlightElement trailingTextProvider];
-[SBFlashlightElement _configureCustomViewsIfNecessary];
-[SBFlashlightElement _handleExpandedLeadingButtonAction];
-[SBFlashlightElement _layoutHuggingObstructionForLabel:x:width:maxLabelHeight:];
-[SBFlashlightElement _sensorObstructionHeightForView:];
-[SBFlashlightElement _textColorForState:];
-[SBFlashlightElement _titleColorForStyle:];
-[SBFlashlightElement _titleTextForStyle:];
-[SBFlashlightElement _trailingTextForState:];
-[SBFlashlightElement expandedLeadingPackageButton];
-[SBFlashlightElement expandedTitleLabel];
-[SBFlashlightElement expandedTrailingLabel];
-[SBFlashlightElement initWithStyle:state:];
-[SBFlashlightElement leadingPackageViewProvider];
```
