# `UIRecentsInputViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- 13 instance variables, 13 properties, 46 instance methods, 3 class methods

## Instance variables

```
B _canManageList;
@"<UIRecentsInputViewControllerDelegate>" _recentInputDelegate;
@"UILexicon" _recentInputs;
q _containingEffectStyle;
@"UIView" _customHeaderView;
@"NSLayoutConstraint" _widthConstraint;
@"NSLayoutConstraint" _heightConstraint;
@"NSString" _previouslyUsedString;
@"NSString" _clearAllString;
@"NSString" _enterNewString;
@"UIView" _headerView;
@"UIView" _headerContainerView;
@"UIViewController" _headerContainerViewController;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_widthConstraint) widthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_heightConstraint) heightConstraint;
@property (T@"NSString",&,N,V_previouslyUsedString) previouslyUsedString;
@property (T@"NSString",&,N,V_clearAllString) clearAllString;
@property (T@"NSString",&,N,V_enterNewString) enterNewString;
@property (T@"UIView",&,N,V_headerView) headerView;
@property (T@"UIView",&,N,V_headerContainerView) headerContainerView;
@property (T@"UIViewController",&,N,V_headerContainerViewController) headerContainerViewController;
@property (T@"<UIRecentsInputViewControllerDelegate>",W,N,V_recentInputDelegate) recentInputDelegate;
@property (T@"UILexicon",&,N,V_recentInputs) recentInputs;
@property (Tq,N,V_containingEffectStyle) containingEffectStyle;
@property (TB,N,V_canManageList) canManageList;
@property (T@"UIView",&,N,V_customHeaderView) customHeaderView;
```

## Class methods

```
+[UIRecentsInputViewController labelStringsForCanManageList:];
+[UIRecentsInputViewController preferredContentWidthForStrings:font:layoutMargins:];
+[UIRecentsInputViewController preferredContentWidthwithManageListEnabled:];
```

## Instance methods

```
-[UIRecentsInputViewController setHeightConstraint:];
-[UIRecentsInputViewController heightConstraint];
-[UIRecentsInputViewController tableView:canMoveRowAtIndexPath:];
-[UIRecentsInputViewController tableView:numberOfRowsInSection:];
-[UIRecentsInputViewController numberOfSectionsInTableView:];
-[UIRecentsInputViewController tableView:cellForRowAtIndexPath:];
-[UIRecentsInputViewController tableView:canFocusRowAtIndexPath:];
-[UIRecentsInputViewController headerView];
-[UIRecentsInputViewController tableView:titleForHeaderInSection:];
-[UIRecentsInputViewController viewDidLoad];
-[UIRecentsInputViewController viewWillAppear:];
-[UIRecentsInputViewController viewDidAppear:];
-[UIRecentsInputViewController tableView:didSelectRowAtIndexPath:];
-[UIRecentsInputViewController widthConstraint];
-[UIRecentsInputViewController setWidthConstraint:];
-[UIRecentsInputViewController preferredFocusedView];
-[UIRecentsInputViewController setHeaderView:];
-[UIRecentsInputViewController tableView:heightForHeaderInSection:];
-[UIRecentsInputViewController scrollViewDidChangeContentSize:];
-[UIRecentsInputViewController _delete:];
-[UIRecentsInputViewController _overrideTraitCollectionForHeaderViewController];
-[UIRecentsInputViewController canManageList];
-[UIRecentsInputViewController clearAllString];
-[UIRecentsInputViewController containingEffectStyle];
-[UIRecentsInputViewController customHeaderView];
-[UIRecentsInputViewController didSelectButtonAtIndexPath:];
-[UIRecentsInputViewController ensureConstraints];
-[UIRecentsInputViewController enterNewString];
-[UIRecentsInputViewController headerContainerView];
-[UIRecentsInputViewController headerContainerViewController];
-[UIRecentsInputViewController indexPathForPreferredFocusedViewInTableView:];
-[UIRecentsInputViewController previouslyUsedString];
-[UIRecentsInputViewController recentInputDelegate];
-[UIRecentsInputViewController recentInputs];
-[UIRecentsInputViewController setCanManageList:];
-[UIRecentsInputViewController setClearAllString:];
-[UIRecentsInputViewController setContainingEffectStyle:];
-[UIRecentsInputViewController setCustomHeaderView:];
-[UIRecentsInputViewController setEnterNewString:];
-[UIRecentsInputViewController setHeaderContainerView:];
-[UIRecentsInputViewController setHeaderContainerViewController:];
-[UIRecentsInputViewController setPreviouslyUsedString:];
-[UIRecentsInputViewController setRecentInputDelegate:];
-[UIRecentsInputViewController setRecentInputs:];
-[UIRecentsInputViewController tableView:canEditRowAtIndexPath:];
-[UIRecentsInputViewController updateTableViewWidth];
```
