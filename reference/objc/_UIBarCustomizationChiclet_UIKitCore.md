# `_UIBarCustomizationChiclet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`
- 12 instance variables, 17 properties, 43 instance methods, 0 class methods

## Instance variables

```
B _platterVisible;
B _labelVisible;
B _minimized;
q _chicletSize;
@"_UIBarCustomizationChicletAnchorView" _anchorView;
@"_UIBarCustomizationItem" _representedItem;
@"UIView" _contentWrapperView;
@"UIView" _rootItemView;
@"NSArray" _subitemViews;
@"UIView" _platterView;
@"UILabel" _label;
@"UIPointerInteraction" _pointerInteraction;
```

## Properties

```
@property (T@"UIView",&,N,V_contentWrapperView) contentWrapperView;
@property (T@"UIView",&,N,V_rootItemView) rootItemView;
@property (T@"NSArray",&,N,V_subitemViews) subitemViews;
@property (T@"UIView",&,N,V_platterView) platterView;
@property (T@"UILabel",&,N,V_label) label;
@property (T@"UIPointerInteraction",&,N,V_pointerInteraction) pointerInteraction;
@property (TB,N,V_platterVisible) platterVisible;
@property (TB,N,V_labelVisible) labelVisible;
@property (TB,N,V_minimized) minimized;
@property (TB,R,N) fixed;
@property (Tq,N,V_chicletSize) chicletSize;
@property (T@"_UIBarCustomizationChicletAnchorView",W,N,V_anchorView) anchorView;
@property (T@"_UIBarCustomizationItem",R,W,N,V_representedItem) representedItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIBarCustomizationChiclet platterView];
-[_UIBarCustomizationChiclet setPointerInteraction:];
-[_UIBarCustomizationChiclet setPlatterView:];
-[_UIBarCustomizationChiclet sizeToFit];
-[_UIBarCustomizationChiclet pointerInteraction:styleForRegion:];
-[_UIBarCustomizationChiclet minimized];
-[_UIBarCustomizationChiclet label];
-[_UIBarCustomizationChiclet setAnchorView:];
-[_UIBarCustomizationChiclet setLabel:];
-[_UIBarCustomizationChiclet layoutSubviews];
-[_UIBarCustomizationChiclet _addContentView:];
-[_UIBarCustomizationChiclet hitTest:withEvent:];
-[_UIBarCustomizationChiclet initWithItem:];
-[_UIBarCustomizationChiclet sizeThatFits:];
-[_UIBarCustomizationChiclet pointerInteraction];
-[_UIBarCustomizationChiclet pointerInteraction:regionForRequest:defaultRegion:];
-[_UIBarCustomizationChiclet _currentContentSize];
-[_UIBarCustomizationChiclet pointInside:withEvent:];
-[_UIBarCustomizationChiclet setMinimized:];
-[_UIBarCustomizationChiclet anchorView];
-[_UIBarCustomizationChiclet representedItem];
-[_UIBarCustomizationChiclet setChicletSize:];
-[_UIBarCustomizationChiclet _contentSizeWithInterItemSpacing:];
-[_UIBarCustomizationChiclet _currentInterItemSpacing];
-[_UIBarCustomizationChiclet _interItemSpacingForChicletSize:];
-[_UIBarCustomizationChiclet _isDisplayingRootItem];
-[_UIBarCustomizationChiclet _platterMinHeight];
-[_UIBarCustomizationChiclet _traitCollectionDidChangeOnSubtreeInternal:];
-[_UIBarCustomizationChiclet _updatePlatterShadow];
-[_UIBarCustomizationChiclet chicletSize];
-[_UIBarCustomizationChiclet contentWrapperView];
-[_UIBarCustomizationChiclet fittingSizeWithChicletSize:];
-[_UIBarCustomizationChiclet fixed];
-[_UIBarCustomizationChiclet labelVisible];
-[_UIBarCustomizationChiclet platterVisible];
-[_UIBarCustomizationChiclet rootItemView];
-[_UIBarCustomizationChiclet setContentWrapperView:];
-[_UIBarCustomizationChiclet setLabelVisible:];
-[_UIBarCustomizationChiclet setPlatterVisible:];
-[_UIBarCustomizationChiclet setRootItemView:];
-[_UIBarCustomizationChiclet setSubitemViews:];
-[_UIBarCustomizationChiclet subitemViews];
-[_UIBarCustomizationChiclet updateItemCenterPoints];
```
