# `SBSAElementContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SAElementIdentifying`, `SBSABlockMutating`, `SBSAElementContextProviding`, `SBSATouchTransparency`
- 26 instance variables, 30 properties, 60 instance methods, 3 class methods

## Instance variables

```
B _fixedInPortraitOrientation;
B _requestingMenuPresentation;
B _limitedSizeSupported;
B _alerting;
B _transparentToTouches;
B _displayedWithLimitedSize;
B _inhibitsIndicatorMitosis;
i _viewControllerAppearState;
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
q _layoutMode;
q _systemApertureCustomLayout;
q _systemApertureCustomLayoutCustomAnimationStyle;
q _systemApertureLayoutCustomizingOptions;
q _activeDynamicAnimation;
@"UIColor" _keyColor;
d _preferredLeadingPadding;
d _preferredTrailingPadding;
d _preferredMinimalPadding;
d _preferredAvoidanceCornerRadius;
d _preferredSystemClipPadding;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _preferredEdgeOutsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _preferredLeadingBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _preferredTrailingBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _preferredMinimalBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _preferredAvoidanceRect;
```

## Properties

```
@property (T@"NSString",C,N,S_setClientIdentifier:,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",C,N,S_setElementIdentifier:,V_elementIdentifier) elementIdentifier;
@property (Tq,N,S_setLayoutMode:,V_layoutMode) layoutMode;
@property (T{NSDirectionalEdgeInsets=dddd},N,S_setPreferredEdgeOutsets:,V_preferredEdgeOutsets) preferredEdgeOutsets;
@property (TB,N,GisFixedInPortraitOrientation,S_setFixedInPortraitOrientation:,V_fixedInPortraitOrientation) fixedInPortraitOrientation;
@property (Tq,N,S_setSystemApertureCustomLayout:,V_systemApertureCustomLayout) systemApertureCustomLayout;
@property (Tq,N,S_setSystemApertureCustomLayoutCustomAnimationStyle:,V_systemApertureCustomLayoutCustomAnimationStyle) systemApertureCustomLayoutCustomAnimationStyle;
@property (Tq,N,S_setSystemApertureLayoutCustomizingOptions:,V_systemApertureLayoutCustomizingOptions) systemApertureLayoutCustomizingOptions;
@property (Tq,N,S_setActiveDynamicAnimation:,V_activeDynamicAnimation) activeDynamicAnimation;
@property (T@"UIColor",C,N,S_setKeyColor:,V_keyColor) keyColor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setPreferredLeadingBounds:,V_preferredLeadingBounds) preferredLeadingBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setPreferredTrailingBounds:,V_preferredTrailingBounds) preferredTrailingBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setPreferredMinimalBounds:,V_preferredMinimalBounds) preferredMinimalBounds;
@property (Td,N,S_setPreferredLeadingPadding:,V_preferredLeadingPadding) preferredLeadingPadding;
@property (Td,N,S_setPreferredTrailingPadding:,V_preferredTrailingPadding) preferredTrailingPadding;
@property (Td,N,S_setPreferredMinimalPadding:,V_preferredMinimalPadding) preferredMinimalPadding;
@property (Ti,N,S_setViewControllerAppearState:,V_viewControllerAppearState) viewControllerAppearState;
@property (TB,N,GisRequestingMenuPresentation,S_setRequestingMenuPresentation:,V_requestingMenuPresentation) requestingMenuPresentation;
@property (TB,N,GisLimitedSizeSupported,S_setLimitedSizeSupported:,V_limitedSizeSupported) limitedSizeSupported;
@property (TB,N,GisAlerting,S_setAlerting:,V_alerting) alerting;
@property (TB,N,GisTransparentToTouches,S_setTransparentToTouches:,V_transparentToTouches) transparentToTouches;
@property (TB,N,GisDisplayedWithLimitedSize,S_setDisplayedWithLimitedSize:,V_displayedWithLimitedSize) displayedWithLimitedSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setPreferredAvoidanceRect:,V_preferredAvoidanceRect) preferredAvoidanceRect;
@property (Td,N,S_setPreferredAvoidanceCornerRadius:,V_preferredAvoidanceCornerRadius) preferredAvoidanceCornerRadius;
@property (TB,N,S_setInhibitsIndicatorMitosis:,V_inhibitsIndicatorMitosis) inhibitsIndicatorMitosis;
@property (Td,N,S_setPreferredSystemClipPadding:,V_preferredSystemClipPadding) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAElementContext initialize];
+[SBSAElementContext instanceWithBlock:];
+[SBSAElementContext mutatorClass];
```

## Instance methods

```
-[SBSAElementContext systemApertureLayoutCustomizingOptions];
-[SBSAElementContext keyColor];
-[SBSAElementContext layoutMode];
-[SBSAElementContext systemApertureCustomLayout];
-[SBSAElementContext isRequestingMenuPresentation];
-[SBSAElementContext inhibitsIndicatorMitosis];
-[SBSAElementContext preferredAvoidanceCornerRadius];
-[SBSAElementContext isAlerting];
-[SBSAElementContext clientIdentifier];
-[SBSAElementContext preferredEdgeOutsets];
-[SBSAElementContext preferredSystemClipPadding];
-[SBSAElementContext isDisplayedWithLimitedSize];
-[SBSAElementContext elementIdentifier];
-[SBSAElementContext init];
-[SBSAElementContext preferredTrailingPadding];
-[SBSAElementContext preferredAvoidanceRect];
-[SBSAElementContext isTransparentToTouches];
-[SBSAElementContext preferredTrailingBounds];
-[SBSAElementContext activeDynamicAnimation];
-[SBSAElementContext preferredMinimalBounds];
-[SBSAElementContext hash];
-[SBSAElementContext preferredMinimalPadding];
-[SBSAElementContext systemApertureCustomLayoutCustomAnimationStyle];
-[SBSAElementContext description];
-[SBSAElementContext preferredLeadingPadding];
-[SBSAElementContext initWithSystemApertureElementContext:];
-[SBSAElementContext copyWithZone:];
-[SBSAElementContext isFixedInPortraitOrientation];
-[SBSAElementContext isEqual:];
-[SBSAElementContext preferredLeadingBounds];
-[SBSAElementContext isLimitedSizeSupported];
-[SBSAElementContext viewControllerAppearState];
-[SBSAElementContext copyWithBlock:];
-[SBSAElementContext membersForCoder];
-[SBSAElementContext _setLayoutMode:];
-[SBSAElementContext _setPreferredSystemClipPadding:];
-[SBSAElementContext _setFixedInPortraitOrientation:];
-[SBSAElementContext _setRequestingMenuPresentation:];
-[SBSAElementContext _setSystemApertureCustomLayout:];
-[SBSAElementContext _setActiveDynamicAnimation:];
-[SBSAElementContext _setAlerting:];
-[SBSAElementContext _setClientIdentifier:];
-[SBSAElementContext _setDisplayedWithLimitedSize:];
-[SBSAElementContext _setElementIdentifier:];
-[SBSAElementContext _setInhibitsIndicatorMitosis:];
-[SBSAElementContext _setKeyColor:];
-[SBSAElementContext _setLimitedSizeSupported:];
-[SBSAElementContext _setPreferredAvoidanceCornerRadius:];
-[SBSAElementContext _setPreferredAvoidanceRect:];
-[SBSAElementContext _setPreferredEdgeOutsets:];
-[SBSAElementContext _setPreferredLeadingBounds:];
-[SBSAElementContext _setPreferredLeadingPadding:];
-[SBSAElementContext _setPreferredMinimalBounds:];
-[SBSAElementContext _setPreferredMinimalPadding:];
-[SBSAElementContext _setPreferredTrailingBounds:];
-[SBSAElementContext _setPreferredTrailingPadding:];
-[SBSAElementContext _setSystemApertureCustomLayoutCustomAnimationStyle:];
-[SBSAElementContext _setSystemApertureLayoutCustomizingOptions:];
-[SBSAElementContext _setTransparentToTouches:];
-[SBSAElementContext _setViewControllerAppearState:];
```
