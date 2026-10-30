# `UITextFormattingViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIColorPickerViewControllerDelegate`, `UIFontPickerViewControllerDelegate`, `__TFTypographySettingsContentViewControllerDelegate`, `_UITextFormattingRemoteViewControllerHost`, `UIPopoverPresentationControllerDelegate`
- 21 instance variables, 11 properties, 89 instance methods, 0 class methods

## Instance variables

```
@"UIView" _containerView;
@"UIView" _contentView;
@"UIStackView" _contentStackView;
@"UINavigationBar" _navBar;
@"_UIKBVisualEffectViewForTextFormatting" _backdropView;
d _keyboardSpace;
@"UIViewController" _preferredFontPickerPresentationViewController;
@"UIViewController" _preferredColorPickerPresentationViewController;
B _shouldSkipStoppingKeyboardSuppressionOnDidDisappear;
d _selectedFontSize;
@"UIColorPickerViewController" _colorPicker;
@"UIFontPickerViewController" _fontPicker;
@"<_UITextFormattingViewHostingImpl>" _hostingImpl;
@"_TFTextFormattingContentViewController" _contentViewController;
@"UITextFormattingViewControllerConfiguration" _configuration;
@"UITextFormattingViewControllerFormattingDescriptor" _formattingDescriptor;
@"<UITextFormattingViewControllerDelegate>" _delegate;
@"UIViewController" _remoteViewController;
@"<_UITextFormattingViewControllerInternalDelegate>" _internalDelegate;
@? __conversionHandler;
@"<UIResponderStandardEditActions>" __editResponder;
```

## Properties

```
@property (T@"<_UITextFormattingViewControllerInternalDelegate>",W,N,S_setInternalDelegate:,V_internalDelegate) _internalDelegate;
@property (T@?,R,C,N,V__conversionHandler) _conversionHandler;
@property (T@"UIViewController",&,N,S_setChildViewController:,V_remoteViewController) _remoteViewController;
@property (T@"<UIResponderStandardEditActions>",W,N,S_setEditResponder:,V__editResponder) _editResponder;
@property (T@"UITextFormattingViewControllerConfiguration",R,C,N,V_configuration) configuration;
@property (T@"UITextFormattingViewControllerFormattingDescriptor",C,N,V_formattingDescriptor) formattingDescriptor;
@property (T@"<UITextFormattingViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextFormattingViewController _commonInit];
-[UITextFormattingViewController adaptivePresentationStyleForPresentationController:traitCollection:];
-[UITextFormattingViewController _scrollView];
-[UITextFormattingViewController preferredContentSizeDidChangeForChildContentContainer:];
-[UITextFormattingViewController viewIsAppearing:];
-[UITextFormattingViewController init];
-[UITextFormattingViewController viewWillDisappear:];
-[UITextFormattingViewController dealloc];
-[UITextFormattingViewController setConfiguration:];
-[UITextFormattingViewController fontPickerViewControllerDidPickFont:];
-[UITextFormattingViewController willMoveToParentViewController:];
-[UITextFormattingViewController initWithConfiguration:];
-[UITextFormattingViewController viewWillAppear:];
-[UITextFormattingViewController _useLandscapeLayout];
-[UITextFormattingViewController _canShowWhileLocked];
-[UITextFormattingViewController setDelegate:];
-[UITextFormattingViewController viewDidAppear:];
-[UITextFormattingViewController configuration];
-[UITextFormattingViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[UITextFormattingViewController loadView];
-[UITextFormattingViewController encodeWithCoder:];
-[UITextFormattingViewController delegate];
-[UITextFormattingViewController _textView];
-[UITextFormattingViewController viewWillLayoutSubviews];
-[UITextFormattingViewController _remoteSheet];
-[UITextFormattingViewController viewDidDisappear:];
-[UITextFormattingViewController initWithCoder:];
-[UITextFormattingViewController didMoveToParentViewController:];
-[UITextFormattingViewController _internalDelegate];
-[UITextFormattingViewController _modifyKeyboardTrackingIfNeededForType:fromFrame:toFrame:start:];
-[UITextFormattingViewController _adjustAttributesInTextStorage:atRange:forChangeValue:];
-[UITextFormattingViewController _applyTextViewHighlightWithChangeValue:];
-[UITextFormattingViewController _backdropViewStyle];
-[UITextFormattingViewController _cleanupForEditResponder];
-[UITextFormattingViewController _computeContentSize];
-[UITextFormattingViewController _conversionHandler];
-[UITextFormattingViewController _didCloseRemotePickerForTextFormatting];
-[UITextFormattingViewController _editResponder];
-[UITextFormattingViewController _formSheetSizeForWindowWithSize:screenSize:metrics:];
-[UITextFormattingViewController _invokeEditResponderAction:];
-[UITextFormattingViewController _invokeEditResponderAction:withArgument:];
-[UITextFormattingViewController _modifyKeyboardTrackingIfNeededForKeyboardSuppression];
-[UITextFormattingViewController _modifyKeyboardTrackingIfNeededForType:start:];
-[UITextFormattingViewController _onUserInterfaceStyleChange];
-[UITextFormattingViewController _preferredCornerRadiusForAnimationOptionsSheet];
-[UITextFormattingViewController _presentColorPicker:selectedColor:];
-[UITextFormattingViewController _presentFontPickerWithConfiguration:selectedFonts:];
-[UITextFormattingViewController _presentTypographySettingsForFont:];
-[UITextFormattingViewController _presentationController:prepareAdaptivePresentationController:];
-[UITextFormattingViewController _reconfigureViewHierarchyForParentController:];
-[UITextFormattingViewController _remoteViewController];
-[UITextFormattingViewController _resetDetentsForSheetController:invalidate:];
-[UITextFormattingViewController _resumeKeyboardSuppressionIfNeeded];
-[UITextFormattingViewController _sendUpdatesToEditResponder:];
-[UITextFormattingViewController _setChildViewController:];
-[UITextFormattingViewController _setEditResponder:];
-[UITextFormattingViewController _setInternalDelegate:];
-[UITextFormattingViewController _setShouldDeferColorPickerPresentationToViewController:];
-[UITextFormattingViewController _setShouldDeferFontPickerPresentationToViewController:];
-[UITextFormattingViewController _setupForEditResponder];
-[UITextFormattingViewController _startSuppressingKeyboardForTextFormatting];
-[UITextFormattingViewController _stopSuppressingKeyboardForTextFormatting];
-[UITextFormattingViewController _textFormattingDidChangeValue:textAttributes:];
-[UITextFormattingViewController _textFormattingDidChangeValue:textAttributesData:];
-[UITextFormattingViewController _textFormattingDidFinish];
-[UITextFormattingViewController _textFormattingRequestsFirstResponderResignation];
-[UITextFormattingViewController _textFormattingRequestsFirstResponderRestoration];
-[UITextFormattingViewController _textViewFormattingDidBegin];
-[UITextFormattingViewController _textViewFormattingDidEnd];
-[UITextFormattingViewController _textViewFormattingWillBegin];
-[UITextFormattingViewController _textViewFormattingWillEnd];
-[UITextFormattingViewController _typographySettingsViewControllerDidUpdateFont:];
-[UITextFormattingViewController _updateBackdropView];
-[UITextFormattingViewController _updateChildControllersConfiguration];
-[UITextFormattingViewController _updateContentSizeForAppearance:];
-[UITextFormattingViewController _updateDisabledComponents];
-[UITextFormattingViewController _updateFormattingDescriptor:];
-[UITextFormattingViewController _updateInternalConfigurationProperties];
-[UITextFormattingViewController _updateNavBarVisibility];
-[UITextFormattingViewController _updateScrollViewContentSizeIfNeeded];
-[UITextFormattingViewController _useChildViewWidthForContentSize];
-[UITextFormattingViewController _useLandscapeLayoutForSize:];
-[UITextFormattingViewController colorPickerViewController:didSelectColor:continuously:];
-[UITextFormattingViewController colorPickerViewControllerDidFinish:];
-[UITextFormattingViewController fontPickerViewControllerDidCancel:];
-[UITextFormattingViewController formattingDescriptor];
-[UITextFormattingViewController modifyKeyboardTrackingIfNeededForType:start:force:immediate:];
-[UITextFormattingViewController preferredVerticalBarBehavior];
-[UITextFormattingViewController setFormattingDescriptor:];
```
