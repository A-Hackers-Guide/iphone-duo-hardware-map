# `UIBarButtonItemGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 13 instance variables, 36 properties, 73 instance methods, 6 class methods

## Instance variables

```
@"NSMutableArray" _barButtonItems;
@"NSString" _customizationIdentifier;
{?="locked"b1"sendActionsBeforeDismiss"b1"showInOverflow"b1"customizationDisposition"b2"requiresOwnSection"b1"isInSidebarSection"b1"wantsHighPriority"b1} _groupFlags;
B _shouldAlwaysCollapse;
q _visibilityPriority;
@"UIBarButtonItem" _representativeItem;
@"UIMenuElement" _menuRepresentation;
q __calculationVisibility;
@"<_UIBarButtonItemGroupOwner>" _owner;
@? __notifyPrepareForLayout;
@? __notifyWillRequestMenuRepresentation;
@"_UITypedStorage" __typedStorage;
Q _expandStyle;
```

## Properties

```
@property (TB,N) __hidden;
@property (T@"NSArray",R,N,G_items) items;
@property (TB,N,G_isLocked,S_setLocked:) locked;
@property (TB,N,G_sendActionsBeforeDismiss,S_setSendActionsBeforeDismiss:) sendActionsBeforeDismiss;
@property (T@"UIMenuElement",R,C,N) _effectiveMenuRepresentation;
@property (T@"UIMenu",R,C,N) _representativeItemMenu;
@property (TB,R,N) _canCollapse;
@property (T@"NSString",R,C,N) _customizationIdentifier;
@property (TB,R,N,G_isDefaultItem) _isDefaultItem;
@property (TB,R,N,G_isRemovableItem) _removableItem;
@property (TB,R,N,G_isMovableItem) _movableItem;
@property (TB,R,N,G_showInOverflow) _showInOverflow;
@property (Tq,N,S_setCalculationVisibility:,V__calculationVisibility) _calculationVisibility;
@property (TB,R,N,G_isHiddenForCalculation) _hiddenForCalculation;
@property (TB,R,N) _disabledExpansion;
@property (Td,R,N) _contextualExpandedPadding;
@property (T@"<_UIBarButtonItemGroupOwner>",W,N,G_owner,S_setOwner:,V_owner) owner;
@property (TB,R,N) _viewNeedsWrapper;
@property (T@?,C,N,V__notifyPrepareForLayout) _notifyPrepareForLayout;
@property (T@?,C,N,V__notifyWillRequestMenuRepresentation) _notifyWillRequestMenuRepresentation;
@property (TB,R,N,G_isCritical) _critical;
@property (TB,N,S_setRequiresOwnSection:) _requiresOwnSection;
@property (TB,R,N,G_isSystemGroup) systemGroup;
@property (TQ,N,G_expandStyle,S_setExpandStyle:,V_expandStyle) expandStyle;
@property (TB,N,G_shouldAlwaysCollapse,S_setShouldAlwaysCollapse:,V_shouldAlwaysCollapse) shouldAlwaysCollapse;
@property (TB,N,G_dci_isAvailableWithoutCustomization,S_dci_setAvailableWithoutCustomization:) _dci_availableWithoutCustomization;
@property (TB,N,G_isHidden,S_setHidden:) _hidden;
@property (Td,N,G_minimumLeadingSpace,S_setMinimumLeadingSpace:) minimumLeadingSpace;
@property (Td,N,G_minimumTrailingSpace,S_setMinimumTrailingSpace:) minimumTrailingSpace;
@property (Tq,N,S_setVisibilityPriority:,V_visibilityPriority) _visibilityPriority;
@property (T@"NSArray",C,N) barButtonItems;
@property (T@"UIBarButtonItem",&,N,V_representativeItem) representativeItem;
@property (TB,R,N,GisDisplayingRepresentativeItem) displayingRepresentativeItem;
@property (TB,N) alwaysAvailable;
@property (T@"UIMenuElement",C,N,V_menuRepresentation) menuRepresentation;
@property (TB,N,GisHidden) hidden;
```

## Class methods

```
+[UIBarButtonItemGroup _effectiveMenuRepresentationWithBarButtonItems:representativeItem:];
+[UIBarButtonItemGroup _synthesizedMenuElementsWithBarButtonItems:];
+[UIBarButtonItemGroup fixedGroupWithRepresentativeItem:items:];
+[UIBarButtonItemGroup groupWithFixedSpace];
+[UIBarButtonItemGroup movableGroupWithCustomizationIdentifier:representativeItem:items:];
+[UIBarButtonItemGroup optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:];
```

## Instance methods

```
-[UIBarButtonItemGroup _owner];
-[UIBarButtonItemGroup _customizationIdentifier];
-[UIBarButtonItemGroup _validateAllItems];
-[UIBarButtonItemGroup _setOwner:];
-[UIBarButtonItemGroup barButtonItems];
-[UIBarButtonItemGroup _sendPrepareForLayout];
-[UIBarButtonItemGroup _setLocked:];
-[UIBarButtonItemGroup setHidden:];
-[UIBarButtonItemGroup _setShouldAlwaysCollapse:];
-[UIBarButtonItemGroup _removeBarButtonItem:];
-[UIBarButtonItemGroup _isRemovableItem];
-[UIBarButtonItemGroup isDisplayingRepresentativeItem];
-[UIBarButtonItemGroup init];
-[UIBarButtonItemGroup reverseEnumerateVisibleItems:];
-[UIBarButtonItemGroup _setExpandStyle:];
-[UIBarButtonItemGroup _notifyWillRequestMenuRepresentation];
-[UIBarButtonItemGroup setRepresentativeItem:];
-[UIBarButtonItemGroup _setSendActionsBeforeDismiss:];
-[UIBarButtonItemGroup _setMinimumLeadingSpace:];
-[UIBarButtonItemGroup _effectiveVisibilityPriority];
-[UIBarButtonItemGroup _shouldAlwaysCollapse];
-[UIBarButtonItemGroup _expandStyle];
-[UIBarButtonItemGroup _isLocked];
-[UIBarButtonItemGroup menuRepresentation];
-[UIBarButtonItemGroup alwaysAvailable];
-[UIBarButtonItemGroup _setCalculationVisibility:];
-[UIBarButtonItemGroup _isMovableItem];
-[UIBarButtonItemGroup isHidden];
-[UIBarButtonItemGroup _setBarButtonItems:allowsSearchBarPlacementItem:];
-[UIBarButtonItemGroup setAlwaysAvailable:];
-[UIBarButtonItemGroup _isDefaultItem];
-[UIBarButtonItemGroup _isHiddenForCalculation];
-[UIBarButtonItemGroup _isHidden];
-[UIBarButtonItemGroup set_notifyPrepareForLayout:];
-[UIBarButtonItemGroup _removeRepresentative:];
-[UIBarButtonItemGroup setMenuRepresentation:];
-[UIBarButtonItemGroup _contextualExpandedPadding];
-[UIBarButtonItemGroup set_notifyWillRequestMenuRepresentation:];
-[UIBarButtonItemGroup _ib_setCustomizationIdentifier:];
-[UIBarButtonItemGroup encodeWithCoder:];
-[UIBarButtonItemGroup _minimumLeadingSpace];
-[UIBarButtonItemGroup _sendActionsBeforeDismiss];
-[UIBarButtonItemGroup _setHidden:];
-[UIBarButtonItemGroup _items];
-[UIBarButtonItemGroup _effectiveMenuRepresentation];
-[UIBarButtonItemGroup _calculationVisibility];
-[UIBarButtonItemGroup _visibilityPriority];
-[UIBarButtonItemGroup _setMinimumTrailingSpace:];
-[UIBarButtonItemGroup description];
-[UIBarButtonItemGroup _canCollapse];
-[UIBarButtonItemGroup representativeItem];
-[UIBarButtonItemGroup _dci_isAvailableWithoutCustomization];
-[UIBarButtonItemGroup _sendNeedsToolbarUpdate];
-[UIBarButtonItemGroup initWithCoder:];
-[UIBarButtonItemGroup _dci_setAvailableWithoutCustomization:];
-[UIBarButtonItemGroup _isSystemGroup];
-[UIBarButtonItemGroup setBarButtonItems:];
-[UIBarButtonItemGroup __hidden];
-[UIBarButtonItemGroup _requiresOwnSection];
-[UIBarButtonItemGroup _setRequiresOwnSection:];
-[UIBarButtonItemGroup _representativeItemMenu];
-[UIBarButtonItemGroup initWithBarButtonItems:representativeItem:];
-[UIBarButtonItemGroup _showInOverflow];
-[UIBarButtonItemGroup enumerateVisibleItems:];
-[UIBarButtonItemGroup _minimumTrailingSpace];
-[UIBarButtonItemGroup _viewNeedsWrapper];
-[UIBarButtonItemGroup _disabledExpansion];
-[UIBarButtonItemGroup _notifyPrepareForLayout];
-[UIBarButtonItemGroup _ib_setCustomizationDisposition:];
-[UIBarButtonItemGroup _isCritical];
-[UIBarButtonItemGroup set__hidden:];
-[UIBarButtonItemGroup _setVisibilityPriority:];
-[UIBarButtonItemGroup _relinquishOwnership:];
```
