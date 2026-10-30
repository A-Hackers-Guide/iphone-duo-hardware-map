# `_UINavigationBarNSToolbarLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 23 instance variables, 23 properties, 49 instance methods, 0 class methods

## Instance variables

```
B _isTitleSectionHidden;
B _showSidebarToggle;
B _isFullyOccluded;
q _style;
q _location;
@"NSString" _customizationIdentifier;
@"NSString" _title;
@"NSString" _subtitle;
@"NSURL" _representedURL;
@? _representedDragItemsProvider;
@"_UINavigationBarPalette" _bottomPalette;
@"NSArray" _staticLeadingItemGroups;
@"NSArray" _leadingGroups;
@"NSArray" _centerGroupsCustomized;
@"NSArray" _centerGroupsFull;
@"NSArray" _trailingGroups;
@"UIBarButtonItemGroup" _pinnedTrailingGroup;
@"NSArray" _staticTrailingItemGroups;
@"NSString" _backButtonTitle;
@"UIImage" _backButtonImage;
@? _backButtonHandler;
@"UISearchTextField" _trailingInlineSearchTextField;
@"UISearchTextField" _centeredInlineSearchTextField;
```

## Properties

```
@property (Tq,N,V_style) style;
@property (Tq,N,V_location) location;
@property (T@"NSString",C,N,V_customizationIdentifier) customizationIdentifier;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_subtitle) subtitle;
@property (TB,N,V_isTitleSectionHidden) isTitleSectionHidden;
@property (T@"NSURL",C,N,V_representedURL) representedURL;
@property (T@?,C,N,V_representedDragItemsProvider) representedDragItemsProvider;
@property (T@"_UINavigationBarPalette",&,N,V_bottomPalette) bottomPalette;
@property (T@"NSArray",C,N,V_staticLeadingItemGroups) staticLeadingItemGroups;
@property (T@"NSArray",C,N,V_leadingGroups) leadingGroups;
@property (T@"NSArray",C,N,V_centerGroupsCustomized) centerGroupsCustomized;
@property (T@"NSArray",C,N,V_centerGroupsFull) centerGroupsFull;
@property (T@"NSArray",C,N,V_trailingGroups) trailingGroups;
@property (T@"UIBarButtonItemGroup",&,N,V_pinnedTrailingGroup) pinnedTrailingGroup;
@property (T@"NSArray",C,N,V_staticTrailingItemGroups) staticTrailingItemGroups;
@property (TB,N,V_showSidebarToggle) showSidebarToggle;
@property (T@"NSString",C,N,V_backButtonTitle) backButtonTitle;
@property (T@"UIImage",&,N,V_backButtonImage) backButtonImage;
@property (T@?,C,N,V_backButtonHandler) backButtonHandler;
@property (T@"UISearchTextField",&,N,V_trailingInlineSearchTextField) trailingInlineSearchTextField;
@property (T@"UISearchTextField",&,N,V_centeredInlineSearchTextField) centeredInlineSearchTextField;
@property (TB,N,V_isFullyOccluded) isFullyOccluded;
```

## Instance methods

```
-[_UINavigationBarNSToolbarLayout subtitle];
-[_UINavigationBarNSToolbarLayout location];
-[_UINavigationBarNSToolbarLayout backButtonHandler];
-[_UINavigationBarNSToolbarLayout setSubtitle:];
-[_UINavigationBarNSToolbarLayout style];
-[_UINavigationBarNSToolbarLayout bottomPalette];
-[_UINavigationBarNSToolbarLayout setStyle:];
-[_UINavigationBarNSToolbarLayout setBackButtonHandler:];
-[_UINavigationBarNSToolbarLayout setLeadingGroups:];
-[_UINavigationBarNSToolbarLayout leadingGroups];
-[_UINavigationBarNSToolbarLayout setBottomPalette:];
-[_UINavigationBarNSToolbarLayout setCustomizationIdentifier:];
-[_UINavigationBarNSToolbarLayout setLocation:];
-[_UINavigationBarNSToolbarLayout title];
-[_UINavigationBarNSToolbarLayout trailingGroups];
-[_UINavigationBarNSToolbarLayout description];
-[_UINavigationBarNSToolbarLayout setTitle:];
-[_UINavigationBarNSToolbarLayout setTrailingGroups:];
-[_UINavigationBarNSToolbarLayout copyWithZone:];
-[_UINavigationBarNSToolbarLayout customizationIdentifier];
-[_UINavigationBarNSToolbarLayout backButtonTitle];
-[_UINavigationBarNSToolbarLayout backButtonImage];
-[_UINavigationBarNSToolbarLayout isFullyOccluded];
-[_UINavigationBarNSToolbarLayout _initWithLayout:];
-[_UINavigationBarNSToolbarLayout centerGroupsCustomized];
-[_UINavigationBarNSToolbarLayout centerGroupsFull];
-[_UINavigationBarNSToolbarLayout centeredInlineSearchTextField];
-[_UINavigationBarNSToolbarLayout isTitleSectionHidden];
-[_UINavigationBarNSToolbarLayout pinnedTrailingGroup];
-[_UINavigationBarNSToolbarLayout representedDragItemsProvider];
-[_UINavigationBarNSToolbarLayout representedURL];
-[_UINavigationBarNSToolbarLayout setBackButtonImage:];
-[_UINavigationBarNSToolbarLayout setBackButtonTitle:];
-[_UINavigationBarNSToolbarLayout setCenterGroupsCustomized:];
-[_UINavigationBarNSToolbarLayout setCenterGroupsFull:];
-[_UINavigationBarNSToolbarLayout setCenteredInlineSearchTextField:];
-[_UINavigationBarNSToolbarLayout setIsFullyOccluded:];
-[_UINavigationBarNSToolbarLayout setIsTitleSectionHidden:];
-[_UINavigationBarNSToolbarLayout setPinnedTrailingGroup:];
-[_UINavigationBarNSToolbarLayout setRepresentedDragItemsProvider:];
-[_UINavigationBarNSToolbarLayout setRepresentedURL:];
-[_UINavigationBarNSToolbarLayout setShowSidebarToggle:];
-[_UINavigationBarNSToolbarLayout setStaticLeadingItemGroups:];
-[_UINavigationBarNSToolbarLayout setStaticTrailingItemGroups:];
-[_UINavigationBarNSToolbarLayout setTrailingInlineSearchTextField:];
-[_UINavigationBarNSToolbarLayout showSidebarToggle];
-[_UINavigationBarNSToolbarLayout staticLeadingItemGroups];
-[_UINavigationBarNSToolbarLayout staticTrailingItemGroups];
-[_UINavigationBarNSToolbarLayout trailingInlineSearchTextField];
```
