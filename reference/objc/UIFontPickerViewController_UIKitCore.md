# `UIFontPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIFontPickerViewControllerHost`, `BSDescriptionProviding`
- 5 instance variables, 9 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _presentingViewController;
@"UIFontPickerViewControllerConfiguration" _configuration;
@"<_UIFontPickerViewHostingImpl>" _hostingImpl;
@"<UIFontPickerViewControllerDelegate>" _delegate;
@"NSArray" __selectedFontDescriptors;
```

## Properties

```
@property (T@"NSArray",&,N,S_setSelectedFontDescriptors:,V__selectedFontDescriptors) _selectedFontDescriptors;
@property (TB,R,N,V_presentingViewController) _presentingViewController;
@property (T@"UIFontPickerViewControllerConfiguration",R,C,N,V_configuration) configuration;
@property (T@"<UIFontPickerViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIFontDescriptor",&,N) selectedFontDescriptor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIFontPickerViewController dismissViewControllerWithTransition:completion:];
-[UIFontPickerViewController debugDescription];
-[UIFontPickerViewController succinctDescriptionBuilder];
-[UIFontPickerViewController viewIsAppearing:];
-[UIFontPickerViewController init];
-[UIFontPickerViewController _pickerDidCancel];
-[UIFontPickerViewController _presentingViewController];
-[UIFontPickerViewController initWithConfiguration:];
-[UIFontPickerViewController descriptionWithMultilinePrefix:];
-[UIFontPickerViewController succinctDescription];
-[UIFontPickerViewController viewWillAppear:];
-[UIFontPickerViewController _canShowWhileLocked];
-[UIFontPickerViewController setDelegate:];
-[UIFontPickerViewController configuration];
-[UIFontPickerViewController debugDescriptionWithMultilinePrefix:];
-[UIFontPickerViewController _initWithConfiguration:];
-[UIFontPickerViewController encodeWithCoder:];
-[UIFontPickerViewController delegate];
-[UIFontPickerViewController description];
-[UIFontPickerViewController initWithCoder:];
-[UIFontPickerViewController descriptionBuilderWithMultilinePrefix:];
-[UIFontPickerViewController _commonFontPickerViewControllerInit];
-[UIFontPickerViewController _isContainedInRemoteSheet];
-[UIFontPickerViewController _parentIsInPopoverPresentation];
-[UIFontPickerViewController _pickerDidSelectFont:];
-[UIFontPickerViewController _selectedFontDescriptors];
-[UIFontPickerViewController _setSelectedFontDescriptors:];
-[UIFontPickerViewController _shouldShowNavigationBarForCurrentParentVC];
-[UIFontPickerViewController _viewControllerPresentationDidInitiate];
-[UIFontPickerViewController _viewShouldHaveGlassBackground];
-[UIFontPickerViewController selectedFontDescriptor];
-[UIFontPickerViewController setSelectedFontDescriptor:];
```
