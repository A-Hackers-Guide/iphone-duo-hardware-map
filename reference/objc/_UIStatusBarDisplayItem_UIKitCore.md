# `_UIStatusBarDisplayItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarPrioritized`, `_UIStatusBarActionable`
- 32 instance variables, 42 properties, 76 instance methods, 0 class methods

## Instance variables

```
B _wasPreviouslyDisabledWithToken;
B _enabled;
B _background;
B _dynamicallyHidden;
B _floating;
B _needsAddingToLayout;
@"UIView<_UIStatusBarDisplayable>" _view;
@"_UIStatusBarAction" _action;
@"_UIStatusBarAction" _hoverAction;
@"_UIStatusBarIdentifier" _identifier;
@"_UIStatusBarItem" _item;
@"<UILayoutItem>" _layoutItem;
@"UIView" _highlightView;
d _alpha;
d _viewAlpha;
d _baselineOffset;
d _centerOffset;
@"_UIStatusBarStyleAttributes" _overriddenStyleAttributes;
q _overriddenVerticalAlignment;
@"_UIStatusBarRegion" _region;
@"UIView" _containerView;
d _dynamicHidingAlpha;
@"NSMutableIndexSet" _disablingTokens;
@"NSTimer" _floatingTimer;
@"_UIStatusBarDisplayItemPlacement" _placement;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _actionInsets;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _extendedHoverInsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _absolutePresentationFrame;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _viewTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _dynamicHidingTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _dynamicScaleTransform;
```

## Properties

```
@property (T@"NSMutableIndexSet",&,N,V_disablingTokens) disablingTokens;
@property (T@"NSTimer",&,N,V_floatingTimer) floatingTimer;
@property (T@"<UILayoutItem>",&,N,V_layoutItem) layoutItem;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_placement) placement;
@property (TB,N,V_needsAddingToLayout) needsAddingToLayout;
@property (T@"_UIStatusBarIdentifier",R,C,N,V_identifier) identifier;
@property (T@"_UIStatusBarItem",R,W,N,V_item) item;
@property (T@"<_UIStatusBarDisplayable>",R,N) displayable;
@property (T@"UIView<_UIStatusBarDisplayable>",R,N,V_view) view;
@property (T@"UIView",&,N,V_highlightView) highlightView;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,R,N) visible;
@property (TB,N,GisBackground,V_background) background;
@property (Td,N,V_alpha) alpha;
@property (Td,N,V_viewAlpha) viewAlpha;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (T{CGAffineTransform=dddddd},N,V_viewTransform) viewTransform;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) absoluteFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_absolutePresentationFrame) absolutePresentationFrame;
@property (Td,N,V_baselineOffset) baselineOffset;
@property (Td,N,V_centerOffset) centerOffset;
@property (T@"_UIStatusBarStyleAttributes",&,N,V_overriddenStyleAttributes) overriddenStyleAttributes;
@property (Tq,N,V_overriddenVerticalAlignment) overriddenVerticalAlignment;
@property (T@"_UIStatusBarRegion",W,N,V_region) region;
@property (T@"UIView",W,N,V_containerView) containerView;
@property (TB,N,V_dynamicallyHidden) dynamicallyHidden;
@property (Td,N,V_dynamicHidingAlpha) dynamicHidingAlpha;
@property (T{CGAffineTransform=dddddd},N,V_dynamicHidingTransform) dynamicHidingTransform;
@property (T{CGAffineTransform=dddddd},N,V_dynamicScaleTransform) dynamicScaleTransform;
@property (TB,N,V_floating) floating;
@property (Tq,R,N) priority;
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
-[_UIStatusBarDisplayItem setRegion:];
-[_UIStatusBarDisplayItem setBaselineOffset:];
-[_UIStatusBarDisplayItem baselineOffset];
-[_UIStatusBarDisplayItem priority];
-[_UIStatusBarDisplayItem dynamicHidingAlpha];
-[_UIStatusBarDisplayItem setNeedsAddingToLayout:];
-[_UIStatusBarDisplayItem setContainerView:];
-[_UIStatusBarDisplayItem setFloating:];
-[_UIStatusBarDisplayItem region];
-[_UIStatusBarDisplayItem visible];
-[_UIStatusBarDisplayItem actionInsets];
-[_UIStatusBarDisplayItem setHighlightView:];
-[_UIStatusBarDisplayItem setFloatingTimer:];
-[_UIStatusBarDisplayItem setActionInsets:];
-[_UIStatusBarDisplayItem applyStyleAttributes:];
-[_UIStatusBarDisplayItem floatingTimer];
-[_UIStatusBarDisplayItem hoverAction];
-[_UIStatusBarDisplayItem displayable];
-[_UIStatusBarDisplayItem dynamicHidingTransform];
-[_UIStatusBarDisplayItem setPlacement:];
-[_UIStatusBarDisplayItem placement];
-[_UIStatusBarDisplayItem setOverriddenVerticalAlignment:];
-[_UIStatusBarDisplayItem setHoverAction:];
-[_UIStatusBarDisplayItem enableWithToken:];
-[_UIStatusBarDisplayItem clearPreviousTokenDisablementIfNecessary];
-[_UIStatusBarDisplayItem identifier];
-[_UIStatusBarDisplayItem setOverriddenStyleAttributes:];
-[_UIStatusBarDisplayItem setBackground:];
-[_UIStatusBarDisplayItem setDynamicHidingTransform:];
-[_UIStatusBarDisplayItem disableWithToken:];
-[_UIStatusBarDisplayItem floating];
-[_UIStatusBarDisplayItem setDynamicallyHidden:];
-[_UIStatusBarDisplayItem _updateComputedAlpha];
-[_UIStatusBarDisplayItem needsAddingToLayout];
-[_UIStatusBarDisplayItem _detectedErrorInFloatingState];
-[_UIStatusBarDisplayItem setAction:];
-[_UIStatusBarDisplayItem action];
-[_UIStatusBarDisplayItem setTransform:];
-[_UIStatusBarDisplayItem hoverView];
-[_UIStatusBarDisplayItem extendedHoverInsets];
-[_UIStatusBarDisplayItem item];
-[_UIStatusBarDisplayItem transform];
-[_UIStatusBarDisplayItem viewAlpha];
-[_UIStatusBarDisplayItem overriddenVerticalAlignment];
-[_UIStatusBarDisplayItem disablingTokens];
-[_UIStatusBarDisplayItem isEnabled];
-[_UIStatusBarDisplayItem containerView];
-[_UIStatusBarDisplayItem isBackground];
-[_UIStatusBarDisplayItem dynamicallyHidden];
-[_UIStatusBarDisplayItem view];
-[_UIStatusBarDisplayItem setAlpha:];
-[_UIStatusBarDisplayItem setAbsoluteFrame:];
-[_UIStatusBarDisplayItem hoverHighlightsAsRegion];
-[_UIStatusBarDisplayItem centerOffset];
-[_UIStatusBarDisplayItem setEnabled:];
-[_UIStatusBarDisplayItem setExtendedHoverInsets:];
-[_UIStatusBarDisplayItem setViewAlpha:];
-[_UIStatusBarDisplayItem absolutePresentationFrame];
-[_UIStatusBarDisplayItem description];
-[_UIStatusBarDisplayItem initWithIdentifier:item:];
-[_UIStatusBarDisplayItem alpha];
-[_UIStatusBarDisplayItem setDynamicHidingAlpha:];
-[_UIStatusBarDisplayItem layoutItem];
-[_UIStatusBarDisplayItem overriddenStyleAttributes];
-[_UIStatusBarDisplayItem _updateComputedTransform];
-[_UIStatusBarDisplayItem absoluteFrame];
-[_UIStatusBarDisplayItem setLayoutItem:];
-[_UIStatusBarDisplayItem dynamicScaleTransform];
-[_UIStatusBarDisplayItem setCenterOffset:];
-[_UIStatusBarDisplayItem highlightView];
-[_UIStatusBarDisplayItem setViewTransform:];
-[_UIStatusBarDisplayItem viewTransform];
-[_UIStatusBarDisplayItem absoluteHoverFrame];
-[_UIStatusBarDisplayItem setDisablingTokens:];
-[_UIStatusBarDisplayItem setDynamicScaleTransform:];
-[_UIStatusBarDisplayItem presentationAbsoluteFrame];
```
