# `_UISearchTextFieldContentSizeCategoryLimitManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _originalShowsLargeContentViewer;
@"NSString" _originalMaximumContentSizeCategory;
B _shouldMaintainExistingCategoryLimit;
@"<UITraitChangeRegistration>" _contentSizeCategoryTraitChangeRegistration;
@"UIView" _limitView;
@"UISearchTextField" _searchTextField;
```

## Properties

```
@property (T@"UIView",R,W,N,V_limitView) limitView;
@property (T@"UISearchTextField",R,W,N,V_searchTextField) searchTextField;
```

## Instance methods

```
-[_UISearchTextFieldContentSizeCategoryLimitManager dealloc];
-[_UISearchTextFieldContentSizeCategoryLimitManager searchTextField];
-[_UISearchTextFieldContentSizeCategoryLimitManager initWithSearchTextField:limitView:];
-[_UISearchTextFieldContentSizeCategoryLimitManager limitView];
-[_UISearchTextFieldContentSizeCategoryLimitManager updateContentSizeCategoryLimitsAsFirstResponder:];
```
