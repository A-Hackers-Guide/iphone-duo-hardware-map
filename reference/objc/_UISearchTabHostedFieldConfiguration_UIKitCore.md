# `_UISearchTabHostedFieldConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _showsCancelAction;
B _automaticallyActivatesSearch;
@"UIView" _searchBarView;
@"UIAction" _cancelAction;
@"<_UIAssertion>" __borrowedAssertion;
@"<_UISearchTabHostedFieldHost>" __searchFieldHost;
d _intrinsicSearchTextFieldHeight;
@"NSString" _searchIconMatchedViewIdentifier;
```

## Properties

```
@property (T@"<_UIAssertion>",&,N,V__borrowedAssertion) _borrowedAssertion;
@property (T@"<_UISearchTabHostedFieldHost>",W,N,S_setSearchFieldHost:,V__searchFieldHost) _searchFieldHost;
@property (Td,N,V_intrinsicSearchTextFieldHeight) intrinsicSearchTextFieldHeight;
@property (TB,N,V_automaticallyActivatesSearch) automaticallyActivatesSearch;
@property (T@"NSString",C,N,V_searchIconMatchedViewIdentifier) searchIconMatchedViewIdentifier;
@property (TB,N,V_showsCancelAction) showsCancelAction;
@property (T@"UIView",R,N,V_searchBarView) searchBarView;
@property (T@"UIAction",R,N,V_cancelAction) cancelAction;
```

## Instance methods

```
-[_UISearchTabHostedFieldConfiguration automaticallyActivatesSearch];
-[_UISearchTabHostedFieldConfiguration setAutomaticallyActivatesSearch:];
-[_UISearchTabHostedFieldConfiguration showsCancelAction];
-[_UISearchTabHostedFieldConfiguration cancelAction];
-[_UISearchTabHostedFieldConfiguration searchIconMatchedViewIdentifier];
-[_UISearchTabHostedFieldConfiguration _borrowedAssertion];
-[_UISearchTabHostedFieldConfiguration _searchFieldHost];
-[_UISearchTabHostedFieldConfiguration _setSearchFieldHost:];
-[_UISearchTabHostedFieldConfiguration initWithSearchBarView:cancelAction:];
-[_UISearchTabHostedFieldConfiguration intrinsicSearchTextFieldHeight];
-[_UISearchTabHostedFieldConfiguration searchBarView];
-[_UISearchTabHostedFieldConfiguration searchTextFieldDidMoveToSuperview];
-[_UISearchTabHostedFieldConfiguration setIntrinsicSearchTextFieldHeight:];
-[_UISearchTabHostedFieldConfiguration setSearchIconMatchedViewIdentifier:];
-[_UISearchTabHostedFieldConfiguration setShowsCancelAction:];
-[_UISearchTabHostedFieldConfiguration set_borrowedAssertion:];
```
