# `UIKBAutoFillTestArchive`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSCopying`
- 9 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _tableViewTagToDataSource;
B _requiresNavigationControllerNesting;
@"UIKBAutoFillTestExpectedResult" _expectedResult;
@"UIView" _snapshotView;
@"NSString" _viewControllerClassName;
@"NSString" _viewControllerTitle;
@"NSString" _navigationControllerClassName;
@"NSString" _presentingViewControllerClassName;
@"UINavigationItem" _viewControllerNavigationItem;
```

## Properties

```
@property (T@"UIView",&,N,V_snapshotView) snapshotView;
@property (T@"NSString",C,N,V_viewControllerClassName) viewControllerClassName;
@property (T@"NSString",C,N,V_viewControllerTitle) viewControllerTitle;
@property (TB,N,V_requiresNavigationControllerNesting) requiresNavigationControllerNesting;
@property (T@"NSString",C,N,V_navigationControllerClassName) navigationControllerClassName;
@property (T@"NSString",C,N,V_presentingViewControllerClassName) presentingViewControllerClassName;
@property (T@"UINavigationItem",&,N,V_viewControllerNavigationItem) viewControllerNavigationItem;
@property (T@"UIKBAutoFillTestExpectedResult",&,N,V_expectedResult) expectedResult;
```

## Class methods

```
+[UIKBAutoFillTestArchive autoFillTestArchiveWithData:];
```

## Instance methods

```
-[UIKBAutoFillTestArchive snapshotView];
-[UIKBAutoFillTestArchive viewControllerClassName];
-[UIKBAutoFillTestArchive init];
-[UIKBAutoFillTestArchive setSnapshotView:];
-[UIKBAutoFillTestArchive encodeWithCoder:];
-[UIKBAutoFillTestArchive initWithCoder:];
-[UIKBAutoFillTestArchive copyWithZone:];
-[UIKBAutoFillTestArchive autoFillTestArchiveData];
-[UIKBAutoFillTestArchive expectedResult];
-[UIKBAutoFillTestArchive navigationControllerClassName];
-[UIKBAutoFillTestArchive presentingViewControllerClassName];
-[UIKBAutoFillTestArchive requiresNavigationControllerNesting];
-[UIKBAutoFillTestArchive setExpectedResult:];
-[UIKBAutoFillTestArchive setNavigationControllerClassName:];
-[UIKBAutoFillTestArchive setPresentingViewControllerClassName:];
-[UIKBAutoFillTestArchive setRequiresNavigationControllerNesting:];
-[UIKBAutoFillTestArchive setTableViewDataSource:forTableViewWithTag:];
-[UIKBAutoFillTestArchive setViewControllerClassName:];
-[UIKBAutoFillTestArchive setViewControllerNavigationItem:];
-[UIKBAutoFillTestArchive setViewControllerTitle:];
-[UIKBAutoFillTestArchive tableViewDataSourceWithTag:];
-[UIKBAutoFillTestArchive viewControllerNavigationItem];
-[UIKBAutoFillTestArchive viewControllerTitle];
```
