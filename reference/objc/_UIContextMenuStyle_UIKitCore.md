# `_UIContextMenuStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 31 instance variables, 35 properties, 70 instance methods, 1 class methods

## Instance variables

```
B _hasInteractivePreview;
B _preventPreviewRasterization;
B _previewOverlapsMenu;
B _ignoresContainerSizeChange;
B _keepsInputViewsVisible;
B _ignoresDefaultSizingRules;
B _shouldMenuOverlapSourcePreview;
B __allowsImmediateSelection;
B __shouldAvoidInputViews;
B __orderMenuBasedOnPriority;
B _prefersStackedHierarchy;
B _showsAccessoriesForCompactMenu;
@"UIView" _containerView;
Q _preferredLayout;
q _inputViewVisibility;
@"UITraitCollection" _preferredTraitCollection;
@"NSArray" _preferredBackgroundEffects;
@"UIColor" _preferredBackgroundColor;
@"<_UIViewMaterial>" _preferredMenuMaterial;
q _itemSelectionHighlightStyle;
q __backgroundInteractionStyle;
@"<_UITraitEnvironmentInternal>" __parentTraitEnvironmentForUserInterfaceStyle;
d __internalPreferredMenuWidth;
Q _preferredAttachmentEdge;
d _preferredMenuWidth;
d _preferredMaximumMenuHeight;
q _preferredImageVisibility;
{CGPoint="x"d"y"d} __preferredMenuAttachmentPoint;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _preferredEdgeInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _preferredBackgroundInsets;
{?="attachment"Q"alignment"Q"attachmentOffset"d"alignmentOffset"d"gravity"q} __preferredAnchor;
```

## Properties

```
@property (T{?=QQddq},N,V__preferredAnchor) _preferredAnchor;
@property (T{CGPoint=dd},N,V__preferredMenuAttachmentPoint) _preferredMenuAttachmentPoint;
@property (TB,N,V__allowsImmediateSelection) _allowsImmediateSelection;
@property (TB,N,V__shouldAvoidInputViews) _shouldAvoidInputViews;
@property (TB,N,V__orderMenuBasedOnPriority) _orderMenuBasedOnPriority;
@property (Tq,N,V__backgroundInteractionStyle) _backgroundInteractionStyle;
@property (T@"<_UITraitEnvironmentInternal>",W,N,V__parentTraitEnvironmentForUserInterfaceStyle) _parentTraitEnvironmentForUserInterfaceStyle;
@property (Td,N,V__internalPreferredMenuWidth) _internalPreferredMenuWidth;
@property (TB,R,N) _layoutAllowsPreview;
@property (TB,R,N) _layoutAllowsMenu;
@property (TB,N,V_prefersStackedHierarchy) prefersStackedHierarchy;
@property (TQ,N,V_preferredAttachmentEdge) preferredAttachmentEdge;
@property (TB,N,V_showsAccessoriesForCompactMenu) showsAccessoriesForCompactMenu;
@property (Td,N,V_preferredMenuWidth) preferredMenuWidth;
@property (Td,N,V_preferredMaximumMenuHeight) preferredMaximumMenuHeight;
@property (Tq,N,V_preferredImageVisibility) preferredImageVisibility;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (TQ,N,V_preferredLayout) preferredLayout;
@property (T{UIEdgeInsets=dddd},N,V_preferredEdgeInsets) preferredEdgeInsets;
@property (TB,N,V_hasInteractivePreview) hasInteractivePreview;
@property (TB,N,V_preventPreviewRasterization) preventPreviewRasterization;
@property (TB,N) reversesActionOrderWhenAttachedToTop;
@property (TB,N,V_previewOverlapsMenu) previewOverlapsMenu;
@property (TB,N,V_ignoresContainerSizeChange) ignoresContainerSizeChange;
@property (TB,N) prefersCenteredPreviewWhenActionsAreAbsent;
@property (TB,N,V_keepsInputViewsVisible) keepsInputViewsVisible;
@property (Tq,N,V_inputViewVisibility) inputViewVisibility;
@property (TB,N,V_ignoresDefaultSizingRules) ignoresDefaultSizingRules;
@property (T@"UITraitCollection",&,N,V_preferredTraitCollection) preferredTraitCollection;
@property (T@"NSArray",&,N,V_preferredBackgroundEffects) preferredBackgroundEffects;
@property (T@"UIColor",&,N,V_preferredBackgroundColor) preferredBackgroundColor;
@property (T{UIEdgeInsets=dddd},N,V_preferredBackgroundInsets) preferredBackgroundInsets;
@property (TB,N,V_shouldMenuOverlapSourcePreview) shouldMenuOverlapSourcePreview;
@property (T@"<_UIViewMaterial>",C,N,V_preferredMenuMaterial) preferredMenuMaterial;
@property (Tq,N,V_itemSelectionHighlightStyle) itemSelectionHighlightStyle;
```

## Class methods

```
+[_UIContextMenuStyle defaultStyle];
```

## Instance methods

```
-[_UIContextMenuStyle shouldMenuOverlapSourcePreview];
-[_UIContextMenuStyle setContainerView:];
-[_UIContextMenuStyle setShouldMenuOverlapSourcePreview:];
-[_UIContextMenuStyle set_internalPreferredMenuWidth:];
-[_UIContextMenuStyle preferredBackgroundInsets];
-[_UIContextMenuStyle set_shouldAvoidInputViews:];
-[_UIContextMenuStyle setPreferredMaximumMenuHeight:];
-[_UIContextMenuStyle setPreferredMenuMaterial:];
-[_UIContextMenuStyle _preferredAnchor];
-[_UIContextMenuStyle setShowsAccessoriesForCompactMenu:];
-[_UIContextMenuStyle prefersStackedHierarchy];
-[_UIContextMenuStyle preferredLayout];
-[_UIContextMenuStyle preferredMaximumMenuHeight];
-[_UIContextMenuStyle set_orderMenuBasedOnPriority:];
-[_UIContextMenuStyle preferredMenuWidth];
-[_UIContextMenuStyle set_preferredAnchor:];
-[_UIContextMenuStyle set_parentTraitEnvironmentForUserInterfaceStyle:];
-[_UIContextMenuStyle inputViewVisibility];
-[_UIContextMenuStyle _orderMenuBasedOnPriority];
-[_UIContextMenuStyle setPreferredAttachmentEdge:];
-[_UIContextMenuStyle setIgnoresDefaultSizingRules:];
-[_UIContextMenuStyle setAllowsBackgroundInteractionAcrossProccesses:];
-[_UIContextMenuStyle _backgroundInteractionStyle];
-[_UIContextMenuStyle setIgnoresContainerSizeChange:];
-[_UIContextMenuStyle containerView];
-[_UIContextMenuStyle setItemSelectionHighlightStyle:];
-[_UIContextMenuStyle previewOverlapsMenu];
-[_UIContextMenuStyle setPreferredBackgroundColor:];
-[_UIContextMenuStyle setPreferredBackgroundEffects:];
-[_UIContextMenuStyle ignoresContainerSizeChange];
-[_UIContextMenuStyle preferredTraitCollection];
-[_UIContextMenuStyle set_allowsImmediateSelection:];
-[_UIContextMenuStyle set_backgroundInteractionStyle:];
-[_UIContextMenuStyle preferredAttachmentEdge];
-[_UIContextMenuStyle hasInteractivePreview];
-[_UIContextMenuStyle preferredEdgeInsets];
-[_UIContextMenuStyle setKeepsInputViewsVisible:];
-[_UIContextMenuStyle _layoutAllowsMenu];
-[_UIContextMenuStyle setPreferredMenuWidth:];
-[_UIContextMenuStyle _internalPreferredMenuWidth];
-[_UIContextMenuStyle preferredBackgroundEffects];
-[_UIContextMenuStyle ignoresDefaultSizingRules];
-[_UIContextMenuStyle _layoutAllowsPreview];
-[_UIContextMenuStyle setReversesActionOrderWhenAttachedToTop:];
-[_UIContextMenuStyle setPreventPreviewRasterization:];
-[_UIContextMenuStyle setPrefersStackedHierarchy:];
-[_UIContextMenuStyle setPreferredTraitCollection:];
-[_UIContextMenuStyle set_preferredMenuAttachmentPoint:];
-[_UIContextMenuStyle setPreferredEdgeInsets:];
-[_UIContextMenuStyle preferredMenuMaterial];
-[_UIContextMenuStyle setPreviewOverlapsMenu:];
-[_UIContextMenuStyle setHasInteractivePreview:];
-[_UIContextMenuStyle showsAccessoriesForCompactMenu];
-[_UIContextMenuStyle copyWithZone:];
-[_UIContextMenuStyle _shouldAvoidInputViews];
-[_UIContextMenuStyle setPreferredLayout:];
-[_UIContextMenuStyle setPreferredBackgroundInsets:];
-[_UIContextMenuStyle preferredImageVisibility];
-[_UIContextMenuStyle _allowsImmediateSelection];
-[_UIContextMenuStyle setInputViewVisibility:];
-[_UIContextMenuStyle setPrefersCenteredPreviewWhenActionsAreAbsent:];
-[_UIContextMenuStyle _preferredMenuAttachmentPoint];
-[_UIContextMenuStyle setPreferredImageVisibility:];
-[_UIContextMenuStyle keepsInputViewsVisible];
-[_UIContextMenuStyle reversesActionOrderWhenAttachedToTop];
-[_UIContextMenuStyle itemSelectionHighlightStyle];
-[_UIContextMenuStyle preferredBackgroundColor];
-[_UIContextMenuStyle _parentTraitEnvironmentForUserInterfaceStyle];
-[_UIContextMenuStyle preventPreviewRasterization];
-[_UIContextMenuStyle prefersCenteredPreviewWhenActionsAreAbsent];
```
