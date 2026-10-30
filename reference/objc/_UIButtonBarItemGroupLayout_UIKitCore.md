# `_UIButtonBarItemGroupLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIButtonBarLayout`
- 18 instance variables, 13 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _itemLayoutMap;
@"NSMutableArray" _itemLayouts;
@"NSMutableArray" _configuredItemLayouts;
@"_UIButtonBarLayout" _representativeLayout;
@"_UIButtonBarSpacerLayout" _leadingSpacerLayout;
B _critical;
B _fixed;
B _compact;
B _spilled;
B _useGroupSizing;
B _suppressSpacing;
B _suppressCustomSpacing;
@"UIBarButtonItemGroup" _group;
@"UILayoutGuide" _groupSizeGuide;
q _leadingSpacerType;
@? _itemViewGenerator;
d _compactWidth;
d _expandedWidth;
```

## Properties

```
@property (T@"UIBarButtonItemGroup",R,N,V_group) group;
@property (T@"UILayoutGuide",R,N,V_groupSizeGuide) groupSizeGuide;
@property (TB,N,V_critical) critical;
@property (TB,N,V_fixed) fixed;
@property (TB,N,V_compact) compact;
@property (TB,N,V_spilled) spilled;
@property (TB,N,V_useGroupSizing) useGroupSizing;
@property (TB,N,V_suppressSpacing) suppressSpacing;
@property (TB,N,V_suppressCustomSpacing) suppressCustomSpacing;
@property (Tq,N,V_leadingSpacerType) leadingSpacerType;
@property (T@?,C,N,V_itemViewGenerator) itemViewGenerator;
@property (Td,R,N,V_compactWidth) compactWidth;
@property (Td,R,N,V_expandedWidth) expandedWidth;
```

## Instance methods

```
-[_UIButtonBarItemGroupLayout setCompact:];
-[_UIButtonBarItemGroupLayout _configure];
-[_UIButtonBarItemGroupLayout setCritical:];
-[_UIButtonBarItemGroupLayout group];
-[_UIButtonBarItemGroupLayout description];
-[_UIButtonBarItemGroupLayout compact];
-[_UIButtonBarItemGroupLayout critical];
-[_UIButtonBarItemGroupLayout spilled];
-[_UIButtonBarItemGroupLayout suppressSpacing];
-[_UIButtonBarItemGroupLayout _addConstraintsToActivate:toDeactivate:];
-[_UIButtonBarItemGroupLayout _addLayoutGuides:];
-[_UIButtonBarItemGroupLayout _addLayoutViews:];
-[_UIButtonBarItemGroupLayout _itemLayouts];
-[_UIButtonBarItemGroupLayout _iterateConfiguredLayouts:];
-[_UIButtonBarItemGroupLayout _newLayoutForBarButtonItem:useGroupSizing:];
-[_UIButtonBarItemGroupLayout _representativeLayout];
-[_UIButtonBarItemGroupLayout compactWidth];
-[_UIButtonBarItemGroupLayout dirtyLayoutForPlainAppearanceChange:doneAppearanceChanged:];
-[_UIButtonBarItemGroupLayout expandedWidth];
-[_UIButtonBarItemGroupLayout fixed];
-[_UIButtonBarItemGroupLayout groupSizeGuide];
-[_UIButtonBarItemGroupLayout initWithLayoutMetrics:];
-[_UIButtonBarItemGroupLayout initWithLayoutMetrics:barButtonItemGroup:];
-[_UIButtonBarItemGroupLayout isGroupLayout];
-[_UIButtonBarItemGroupLayout isSpaceLayout];
-[_UIButtonBarItemGroupLayout itemViewGenerator];
-[_UIButtonBarItemGroupLayout layoutForBarButtonItem:];
-[_UIButtonBarItemGroupLayout layoutsForSpacerItem:];
-[_UIButtonBarItemGroupLayout leadingSpacerType];
-[_UIButtonBarItemGroupLayout minimumLayoutWidthGivenMinimumSpaceWidth:];
-[_UIButtonBarItemGroupLayout recalculateLayoutWidthsGivenItemSpaceWidth:];
-[_UIButtonBarItemGroupLayout setFixed:];
-[_UIButtonBarItemGroupLayout setItemViewGenerator:];
-[_UIButtonBarItemGroupLayout setLeadingSpacerType:];
-[_UIButtonBarItemGroupLayout setSpilled:];
-[_UIButtonBarItemGroupLayout setSuppressCustomSpacing:];
-[_UIButtonBarItemGroupLayout setSuppressSpacing:];
-[_UIButtonBarItemGroupLayout setUseGroupSizing:];
-[_UIButtonBarItemGroupLayout shouldHorizontallyCenterView:];
-[_UIButtonBarItemGroupLayout subLayouts];
-[_UIButtonBarItemGroupLayout suppressCustomSpacing];
-[_UIButtonBarItemGroupLayout useGroupSizing];
```
