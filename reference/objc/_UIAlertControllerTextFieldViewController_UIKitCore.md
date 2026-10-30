# `_UIAlertControllerTextFieldViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewController`
- 7 instance variables, 5 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" textFieldViews;
@"NSMutableArray" textFields;
B _textFieldsCanBecomeFirstResponder;
@"UIAlertControllerVisualStyle" _visualStyle;
@"UICollectionViewFlowLayout" _collectionViewLayout;
B _hidden;
@"<_UIAlertControllerTextFieldViewControllerContaining>" _container;
```

## Properties

```
@property (T@"<_UIAlertControllerTextFieldViewControllerContaining>",W,N,V_container) container;
@property (TB,N) textFieldsCanBecomeFirstResponder;
@property (T@"UIAlertControllerVisualStyle",N) visualStyle;
@property (T@"NSArray",R,VtextFields) textFields;
@property (TB,N,GisHidden,V_hidden) hidden;
```

## Instance methods

```
-[_UIAlertControllerTextFieldViewController collectionView:canFocusItemAtIndexPath:];
-[_UIAlertControllerTextFieldViewController setTextFieldsCanBecomeFirstResponder:];
-[_UIAlertControllerTextFieldViewController setVisualStyle:];
-[_UIAlertControllerTextFieldViewController textFieldAtIndex:];
-[_UIAlertControllerTextFieldViewController collectionView:numberOfItemsInSection:];
-[_UIAlertControllerTextFieldViewController setHidden:];
-[_UIAlertControllerTextFieldViewController _updatePreferredContentSize];
-[_UIAlertControllerTextFieldViewController _returnKeyPressedInTextField:];
-[_UIAlertControllerTextFieldViewController init];
-[_UIAlertControllerTextFieldViewController visualStyle];
-[_UIAlertControllerTextFieldViewController collectionView:cellForItemAtIndexPath:];
-[_UIAlertControllerTextFieldViewController numberOfSectionsInCollectionView:];
-[_UIAlertControllerTextFieldViewController addTextFieldWithPlaceholder:];
-[_UIAlertControllerTextFieldViewController textFieldContainerViews];
-[_UIAlertControllerTextFieldViewController setContainer:];
-[_UIAlertControllerTextFieldViewController viewDidLoad];
-[_UIAlertControllerTextFieldViewController textFieldsCanBecomeFirstResponder];
-[_UIAlertControllerTextFieldViewController resignFirstResponder];
-[_UIAlertControllerTextFieldViewController textFields];
-[_UIAlertControllerTextFieldViewController numberOfTextFields];
-[_UIAlertControllerTextFieldViewController viewWillAppear:];
-[_UIAlertControllerTextFieldViewController _canShowWhileLocked];
-[_UIAlertControllerTextFieldViewController isHidden];
-[_UIAlertControllerTextFieldViewController removeAllTextFields];
-[_UIAlertControllerTextFieldViewController _bottomMarginForTextFields];
-[_UIAlertControllerTextFieldViewController viewWillLayoutSubviews];
-[_UIAlertControllerTextFieldViewController updateTextFieldStyle];
-[_UIAlertControllerTextFieldViewController container];
```
