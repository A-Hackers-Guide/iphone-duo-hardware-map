# `_TtC5UIKit19NavigationButtonBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIButtonBarAppearanceDelegate`, `_UIButtonBarGroupOrderOwner`
- 38 instance variables, 10 properties, 30 instance methods, 0 class methods

## Instance variables

```
_$syXlXp buttonVisualProviderClass;
__C._UINavigationButtonBarPosition position;
_$sSa -> UIKit.NavigationButtonBar.SectionLayout sectionLayouts;
_$sSa -> UIKit.NavigationButtonBar.SectionLayout effectiveLayout;
_$sSDySo15_UIBarItemGroupC UIKit.NavigationButtonBar.GroupLayout groupLayoutMap;
_$sSo33_UIBarButtonItemAppearanceStorageCSg appearanceStorage;
Swift.Bool isCompact;
_$sSo30_UIPointerInteractionAssistantCSgXw assistant;
Swift.Bool supportsAlwaysOverflowGroups;
_$sSo30_UIBarButtonItemSearchBarGroupCSg searchBarGroup;
_$sSo15_UIBarItemGroupCSg scopeBarGroup;
Swift.Bool searchTakesOverContentView;
Swift.Bool searchPrefersIconItem;
_$sSo15UIBarButtonItemCSg $__lazy_storage_$_searchCancelItem;
Swift.Bool isInLayoutReentrancyGuard;
Swift.Bool effectiveLayoutHasCriticalGroup;
Swift.Bool needsAppearanceUpdate;
Swift.Bool plainAppearanceChanged;
Swift.Bool doneAppearanceChanged;
Swift.Bool denyPointerInteractions;
UIKit.NavigationButtonBarDelegate ? delegate;
Swift.Bool plainItemAppearanceNeedsUpdate;
_$sSo20_UIBarButtonItemDataCSg plainItemAppearance;
Swift.Bool prominentItemAppearanceNeedsUpdate;
_$sSo20_UIBarButtonItemDataCSg prominentItemAppearance;
UIKit.NavigationButtonBar.Layout.Metrics layoutMetrics;
_$sSo24_UIButtonBarGroupOrdererCSg groupOrderer;
_$sSaySo15_UIBarItemGroupCG fixedLeadingGroups;
_$sSaySo15_UIBarItemGroupCG fixedTrailingGroups;
Swift.Bool forceFixedSpacing;
Swift.Bool supportsOverflow;
_$sSaySo13_UIBarSectionCG barSections;
Swift.Bool hideGroupsPreferringVerticalBar;
_$sSo20UIBarButtonItemGroupCSg pinnedTrailingGroupPreferringVerticalBar;
_$sSa -> UIKit.NavigationButtonBar.IdentifiedSection ? resolvedSections;
_$sSa -> UIKit.ExternalGroup ? _groupsPreferringVerticalBar;
Foundation.UUID ? _externalOverflowSectionID;
_$sSa -> UIKit.NavigationButtonBar.IdentifiedSection sectionedBarButtonGroups;
```

## Properties

```
@property (Tq,N,R) barType;
@property (TB,N,R) compactMetrics;
@property (T@"UIColor",N,R) tintColor;
@property (TB,N,R) centerTextButtons;
@property (Td,N,R) defaultEdgeSpacing;
@property (Td,N,R) defaultTextPadding;
@property (Td,N,R) backButtonMargin;
@property (Td,N,R) backButtonMaximumWidth;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) bounds;
@property (T@"_UIBarButtonItemAppearanceStorage",N,&,VappearanceStorage) appearanceStorage;
```

## Instance methods

```
-[_TtC5UIKit19NavigationButtonBar edgesPaddingBarButtonItem:];
-[_TtC5UIKit19NavigationButtonBar _layoutMarginsForButtonBarButton:compact:];
-[_TtC5UIKit19NavigationButtonBar traitCollectionForResolvingButtonBarButtonBackgroundColor:];
-[_TtC5UIKit19NavigationButtonBar defaultHeightForButtonBarButton:representingBarButtonItem:];
-[_TtC5UIKit19NavigationButtonBar backIndicatorMaskImage];
-[_TtC5UIKit19NavigationButtonBar tintColorForButtonBarButton:];
-[_TtC5UIKit19NavigationButtonBar init];
-[_TtC5UIKit19NavigationButtonBar convertPoint:fromCoordinateSpace:];
-[_TtC5UIKit19NavigationButtonBar appearanceStorage];
-[_TtC5UIKit19NavigationButtonBar convertRect:toCoordinateSpace:];
-[_TtC5UIKit19NavigationButtonBar absorptionForItem:];
-[_TtC5UIKit19NavigationButtonBar additionalEdgeSpacingForButtonBarButton:representingBarButtonItem:];
-[_TtC5UIKit19NavigationButtonBar backButtonMargin];
-[_TtC5UIKit19NavigationButtonBar convertPoint:toCoordinateSpace:];
-[_TtC5UIKit19NavigationButtonBar itemAtPoint:inView:];
-[_TtC5UIKit19NavigationButtonBar _groupOrdererGroups:];
-[_TtC5UIKit19NavigationButtonBar convertRect:fromCoordinateSpace:];
-[_TtC5UIKit19NavigationButtonBar centerTextButtons];
-[_TtC5UIKit19NavigationButtonBar bounds];
-[_TtC5UIKit19NavigationButtonBar tintColor];
-[_TtC5UIKit19NavigationButtonBar configurationDependenciesChangedForButtonBarButton:representingBarButtonItem:];
-[_TtC5UIKit19NavigationButtonBar defaultEdgeSpacing];
-[_TtC5UIKit19NavigationButtonBar defaultTextPadding];
-[_TtC5UIKit19NavigationButtonBar backIndicatorImage];
-[_TtC5UIKit19NavigationButtonBar setAppearanceStorage:];
-[_TtC5UIKit19NavigationButtonBar barType];
-[_TtC5UIKit19NavigationButtonBar compactMetrics];
-[_TtC5UIKit19NavigationButtonBar invalidateAssistant:];
-[_TtC5UIKit19NavigationButtonBar backButtonMaximumWidth];
-[_TtC5UIKit19NavigationButtonBar _groupOrdererDidUpdate:];
```
