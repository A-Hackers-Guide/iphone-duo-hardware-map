# `_UIStatusBarRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarActionable`
- 27 instance variables, 43 properties, 73 instance methods, 0 class methods

## Instance variables

```
B _offsetable;
B _needsReLayout;
B _disableItemFrameBasedOverflow;
@"_UIStatusBarAction" _action;
@"_UIStatusBarAction" _hoverAction;
@"NSString" _identifier;
@"_UIStatusBar" _statusBar;
@"<_UIStatusBarRegionLayout>" _layout;
@"NSSet" _dependentRegionIdentifiers;
@"_UIStatusBarRegion" _enabilityRegion;
d _alpha;
q _style;
q _overriddenStyle;
@"_UIStatusBarStyleAttributes" _overriddenStyleAttributes;
@"UIView" _contentView;
@"UIView" _backgroundView;
@"UIView" _highlightView;
@"NSOrderedSet" _displayItems;
@"NSMutableIndexSet" _disablingTokens;
@"UILayoutGuide" _layoutGuide;
@"NSLayoutConstraint" _centerXConstraint;
@"NSLayoutConstraint" _centerYConstraint;
@"UIView" _containerView;
@"UIView" _frozenView;
{UIOffset="horizontal"d"vertical"d} _offset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _actionInsets;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _extendedHoverInsets;
```

## Properties

```
@property (T@"NSMutableIndexSet",&,N,V_disablingTokens) disablingTokens;
@property (T@"UILayoutGuide",&,N,V_layoutGuide) layoutGuide;
@property (T@"NSLayoutConstraint",&,N,V_centerXConstraint) centerXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_centerYConstraint) centerYConstraint;
@property (T@"UIView",R,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_frozenView) frozenView;
@property (T@"NSArray",R,N) enabledDisplayItems;
@property (T@"NSArray",R,N) currentEnabledDisplayItems;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"_UIStatusBar",W,N,V_statusBar) statusBar;
@property (T@"<UILayoutItem>",R,N) layoutItem;
@property (T@"<UILayoutItem>",R,N) containerItem;
@property (T@"<_UIStatusBarRegionLayout>",&,N,V_layout) layout;
@property (T@"NSSet",&,N,V_dependentRegionIdentifiers) dependentRegionIdentifiers;
@property (TB,R,N,GisEnabled) enabled;
@property (T@"_UIStatusBarRegion",W,N,V_enabilityRegion) enabilityRegion;
@property (TB,N,V_offsetable) offsetable;
@property (T{UIOffset=dd},N,V_offset) offset;
@property (TB,N,GisFrozen) frozen;
@property (Td,N,V_alpha) alpha;
@property (Tq,R,N) effectiveStyle;
@property (Tq,N,V_style) style;
@property (Tq,N,V_overriddenStyle) overriddenStyle;
@property (T@"_UIStatusBarStyleAttributes",&,N,V_overriddenStyleAttributes) overriddenStyleAttributes;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (T@"UIView",&,N,V_highlightView) highlightView;
@property (T@"NSOrderedSet",&,N,V_displayItems) displayItems;
@property (T@"_UIStatusBarDisplayItem",R,N) overflowedDisplayItem;
@property (T@"NSDictionary",R,C,N) displayItemAbsoluteFrames;
@property (TB,N,V_needsReLayout) needsReLayout;
@property (TB,N,V_disableItemFrameBasedOverflow) disableItemFrameBasedOverflow;
@property (T@"_UIStatusBarAction",&,N,V_action) action;
@property (T@"_UIStatusBarAction",&,N,V_hoverAction) hoverAction;
@property (T@"UIView",R,N) hoverView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) absoluteHoverFrame;
@property (TB,R,N) hoverHighlightsAsRegion;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_extendedHoverInsets) extendedHoverInsets;
@property (T{UIEdgeInsets=dddd},N,V_actionInsets) actionInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarRegion isFrozen];
-[_UIStatusBarRegion effectiveStyle];
-[_UIStatusBarRegion statusBar];
-[_UIStatusBarRegion setLayoutGuide:];
-[_UIStatusBarRegion setContentView:];
-[_UIStatusBarRegion setFrozen:];
-[_UIStatusBarRegion actionInsets];
-[_UIStatusBarRegion setHighlightView:];
-[_UIStatusBarRegion setActionInsets:];
-[_UIStatusBarRegion hoverAction];
-[_UIStatusBarRegion displayItems];
-[_UIStatusBarRegion setStatusBar:];
-[_UIStatusBarRegion setHoverAction:];
-[_UIStatusBarRegion setNeedsReLayout:];
-[_UIStatusBarRegion enableWithToken:];
-[_UIStatusBarRegion layoutGuide];
-[_UIStatusBarRegion identifier];
-[_UIStatusBarRegion setOverriddenStyleAttributes:];
-[_UIStatusBarRegion disableWithToken:];
-[_UIStatusBarRegion centerXConstraint];
-[_UIStatusBarRegion containerItem];
-[_UIStatusBarRegion needsReLayout];
-[_UIStatusBarRegion setDependentRegionIdentifiers:];
-[_UIStatusBarRegion setFrozenView:];
-[_UIStatusBarRegion setAction:];
-[_UIStatusBarRegion action];
-[_UIStatusBarRegion hoverView];
-[_UIStatusBarRegion extendedHoverInsets];
-[_UIStatusBarRegion centerYConstraint];
-[_UIStatusBarRegion enabledDisplayItems];
-[_UIStatusBarRegion style];
-[_UIStatusBarRegion setEnabilityRegion:];
-[_UIStatusBarRegion setStyle:];
-[_UIStatusBarRegion disablingTokens];
-[_UIStatusBarRegion isEnabled];
-[_UIStatusBarRegion containerView];
-[_UIStatusBarRegion setIdentifier:];
-[_UIStatusBarRegion _overriddenStyleAttributesChanged];
-[_UIStatusBarRegion enabilityRegion];
-[_UIStatusBarRegion overflowedDisplayItem];
-[_UIStatusBarRegion setCenterXConstraint:];
-[_UIStatusBarRegion setAlpha:];
-[_UIStatusBarRegion hoverHighlightsAsRegion];
-[_UIStatusBarRegion setOffsetable:];
-[_UIStatusBarRegion _addSubview:atBack:];
-[_UIStatusBarRegion dependentRegionIdentifiers];
-[_UIStatusBarRegion disableItemFrameBasedOverflow];
-[_UIStatusBarRegion setExtendedHoverInsets:];
-[_UIStatusBarRegion setDisplayItems:];
-[_UIStatusBarRegion contentView];
-[_UIStatusBarRegion setOverriddenStyle:];
-[_UIStatusBarRegion backgroundView];
-[_UIStatusBarRegion description];
-[_UIStatusBarRegion layout];
-[_UIStatusBarRegion setCenterYConstraint:];
-[_UIStatusBarRegion alpha];
-[_UIStatusBarRegion setOffset:];
-[_UIStatusBarRegion layoutItem];
-[_UIStatusBarRegion overriddenStyleAttributes];
-[_UIStatusBarRegion offsetable];
-[_UIStatusBarRegion setBackgroundView:];
-[_UIStatusBarRegion initWithIdentifier:];
-[_UIStatusBarRegion highlightView];
-[_UIStatusBarRegion setLayout:];
-[_UIStatusBarRegion absoluteHoverFrame];
-[_UIStatusBarRegion offset];
-[_UIStatusBarRegion currentEnabledDisplayItems];
-[_UIStatusBarRegion displayItemAbsoluteFrames];
-[_UIStatusBarRegion setDisablingTokens:];
-[_UIStatusBarRegion frozenView];
-[_UIStatusBarRegion overriddenStyle];
-[_UIStatusBarRegion setDisableItemFrameBasedOverflow:];
-[_UIStatusBarRegion displayItemForHUDAtLocation:];
```
