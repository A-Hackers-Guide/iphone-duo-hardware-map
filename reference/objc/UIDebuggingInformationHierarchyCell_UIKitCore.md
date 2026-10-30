# `UIDebuggingInformationHierarchyCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 10 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIButton" _disclosureButton;
@"UILabel" _mainLabel;
@"UIButton" _infoButton;
@"NSIndexPath" _indexPath;
B _collapsedBeneath;
@"NSLayoutConstraint" _disclosureButtonAvailableConstraint;
@"NSLayoutConstraint" _disclosureButtonUnavailableConstraint;
B _disclosureIndicatorHidden;
@"NSString" _name;
@"<UIDebuggingInformationHierarchyCellDelegate>" _delegate;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"UIButton",R,N) infoButton;
@property (T@"<UIDebuggingInformationHierarchyCellDelegate>",W,N,V_delegate) delegate;
@property (T@"NSIndexPath",R,N) indexPath;
@property (TB,N,V_disclosureIndicatorHidden) disclosureIndicatorHidden;
```

## Instance methods

```
-[UIDebuggingInformationHierarchyCell indexPath];
-[UIDebuggingInformationHierarchyCell applyLayoutAttributes:];
-[UIDebuggingInformationHierarchyCell layoutSubviews];
-[UIDebuggingInformationHierarchyCell setDelegate:];
-[UIDebuggingInformationHierarchyCell prepareForReuse];
-[UIDebuggingInformationHierarchyCell delegate];
-[UIDebuggingInformationHierarchyCell setName:];
-[UIDebuggingInformationHierarchyCell name];
-[UIDebuggingInformationHierarchyCell deliverToggle];
-[UIDebuggingInformationHierarchyCell disclosureIndicatorHidden];
-[UIDebuggingInformationHierarchyCell displayDetailsForCell];
-[UIDebuggingInformationHierarchyCell infoButton];
-[UIDebuggingInformationHierarchyCell setDisclosureIndicatorHidden:];
```
