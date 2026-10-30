# `SBAppSwitcherPageShadowView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFView`
- Protocols: `PTSettingsKeyObserver`
- 20 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"SBAppSwitcherSettings" _switcherSettings;
@"SBMedusaSettings" _medusaSettings;
@"SBFView" _diffuseShadowView;
@"SBFView" _rimShadowView;
d _rimShadowRadius;
d _rimShadowOpacity;
d _diffuseShadowRadius;
d _diffuseShadowOpacity;
{CGSize="width"d"height"d} _diffuseShadowOffset;
d _diffuseShadowRadiusWhileTouched;
d _diffuseShadowOpacityWhileTouched;
{CGSize="width"d"height"d} _diffuseShadowOffsetWhileTouched;
d _diffuseShadowRadiusWhileCursorHovered;
d _diffuseShadowOpacityWhileCursorHovered;
{CGSize="width"d"height"d} _diffuseShadowOffsetWhileCursorHovered;
d _switcherCardScale;
q _style;
Q _highlightType;
@"UIBezierPath" _shadowPath;
d _shadowOffset;
```

## Properties

```
@property (T@"UIView",R,N) _diffuseShadowView;
@property (T@"UIView",R,N) _rimShadowView;
@property (Td,N,V_switcherCardScale) switcherCardScale;
@property (Tq,N,V_style) style;
@property (TQ,N,V_highlightType) highlightType;
@property (T@"UIBezierPath",&,N,V_shadowPath) shadowPath;
@property (Td,N,V_shadowOffset) shadowOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppSwitcherPageShadowView setShadowPath:];
-[SBAppSwitcherPageShadowView _diffuseShadowView];
-[SBAppSwitcherPageShadowView highlightType];
-[SBAppSwitcherPageShadowView _updateShadowViews];
-[SBAppSwitcherPageShadowView setShadowOffset:];
-[SBAppSwitcherPageShadowView setSwitcherCardScale:];
-[SBAppSwitcherPageShadowView switcherCardScale];
-[SBAppSwitcherPageShadowView initWithFrame:style:];
-[SBAppSwitcherPageShadowView style];
-[SBAppSwitcherPageShadowView settings:changedValueForKey:];
-[SBAppSwitcherPageShadowView setStyle:];
-[SBAppSwitcherPageShadowView shadowPath];
-[SBAppSwitcherPageShadowView _setContinuousCornerRadius:];
-[SBAppSwitcherPageShadowView _rimShadowView];
-[SBAppSwitcherPageShadowView traitCollectionDidChange:];
-[SBAppSwitcherPageShadowView _applyPrototypeSettingsToConstants];
-[SBAppSwitcherPageShadowView setHighlightType:];
-[SBAppSwitcherPageShadowView shadowOffset];
-[SBAppSwitcherPageShadowView _updateShadowParameters];
```
