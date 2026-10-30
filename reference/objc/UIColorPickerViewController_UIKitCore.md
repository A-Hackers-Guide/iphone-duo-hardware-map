# `UIColorPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIColorPickerColorQueueDelegate`, `_UIColorPickerViewProvidingDelegate`
- 9 instance variables, 21 properties, 62 instance methods, 0 class methods

## Instance variables

```
@"UIPresentationController" _presentationController;
{?="delegateImplementsDidSelectColorContinuous"b1"delegateImplementsDidSelectColor"b1"delegateImplementsDidDeselectColorSPI"b1"disableReshowingColorPickerOnEyedropperDismiss"b1} _flags;
@"<_UIColorPickerViewHostingImpl>" _hostingImpl;
@"<UIColorPickerViewControllerDelegate>" _delegate;
@"_UIColorPickerViewControllerConfiguration" _configuration;
@"UIColor" _selectedColor;
@"UIViewController" _childViewController;
@"_UIColorPickerColorQueue" _colorQueue;
@"_UIColorPickerViewControllerConfiguration" __remoteConfiguration;
```

## Properties

```
@property (T@"_UIColorPickerColorQueue",&,N,V_colorQueue) colorQueue;
@property (T@"UIViewController",&,N,S_setChildViewController:,V_childViewController) _childViewController;
@property (T@"_UIColorPickerViewControllerConfiguration",R,C,N,V_configuration) configuration;
@property (T@"_UIColorPickerViewControllerConfiguration",C,N,S_setRemoteConfiguration:,V__remoteConfiguration) _remoteConfiguration;
@property (TB,N,S_setShouldUseDarkGridInDarkMode:) _shouldUseDarkGridInDarkMode;
@property (Tq,N,S_setUserInterfaceStyleForGrid:) _userInterfaceStyleForGrid;
@property (T@"NSArray",C,N,S_setSuggestedColors:) _suggestedColors;
@property (T@"UIColor",&,N,S_setSelectedColor:,V_selectedColor) _selectedColor;
@property (TB,N,S_setAllowsNoColor:) _allowsNoColor;
@property (TB,N,S_setSupportsEyedropper:) _supportsEyedropper;
@property (TB,N,S_setShowsGridOnly:) _showsGridOnly;
@property (Td,N) maxGain;
@property (T@"<UIColorPickerViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIColor",&,N) selectedColor;
@property (TB,N) supportsAlpha;
@property (TB,N) supportsEyedropper;
@property (Td,N) maximumLinearExposure;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIColorPickerViewController preferredContentSizeDidChangeForChildContentContainer:];
-[UIColorPickerViewController setMaxGain:];
-[UIColorPickerViewController init];
-[UIColorPickerViewController willMoveToParentViewController:];
-[UIColorPickerViewController viewWillAppear:];
-[UIColorPickerViewController _canShowWhileLocked];
-[UIColorPickerViewController setDelegate:];
-[UIColorPickerViewController configuration];
-[UIColorPickerViewController loadView];
-[UIColorPickerViewController _defaultColor];
-[UIColorPickerViewController encodeWithCoder:];
-[UIColorPickerViewController _updateConfiguration];
-[UIColorPickerViewController delegate];
-[UIColorPickerViewController viewWillLayoutSubviews];
-[UIColorPickerViewController _remoteSheet];
-[UIColorPickerViewController maxGain];
-[UIColorPickerViewController initWithCoder:];
-[UIColorPickerViewController setTitle:];
-[UIColorPickerViewController didMoveToParentViewController:];
-[UIColorPickerViewController __setSelectedColor:notifyingViewService:];
-[UIColorPickerViewController _allowsNoColor];
-[UIColorPickerViewController _childViewController];
-[UIColorPickerViewController _commonUIColorPickerViewControllerInit];
-[UIColorPickerViewController _dequeue_pickerDidSelectColor:colorSpace:isVolatile:];
-[UIColorPickerViewController _formSheetSizeForWindowWithSize:screenSize:metrics:];
-[UIColorPickerViewController _pickerDidDismissEyedropper];
-[UIColorPickerViewController _pickerDidFinish];
-[UIColorPickerViewController _pickerDidFloatEyedropper];
-[UIColorPickerViewController _pickerDidSelectColor:colorSpace:isVolatile:];
-[UIColorPickerViewController _pickerDidShowEyedropper];
-[UIColorPickerViewController _presentationController:prepareAdaptivePresentationController:];
-[UIColorPickerViewController _remoteConfiguration];
-[UIColorPickerViewController _selectDefaultColorIfNecessary];
-[UIColorPickerViewController _selectedColor];
-[UIColorPickerViewController _setAllowsNoColor:];
-[UIColorPickerViewController _setChildViewController:];
-[UIColorPickerViewController _setRemoteConfiguration:];
-[UIColorPickerViewController _setSelectedColor:];
-[UIColorPickerViewController _setShouldUseDarkGridInDarkMode:];
-[UIColorPickerViewController _setShowsGridOnly:];
-[UIColorPickerViewController _setSuggestedColors:];
-[UIColorPickerViewController _setSupportsEyedropper:];
-[UIColorPickerViewController _setUserInterfaceStyleForGrid:];
-[UIColorPickerViewController _setupColorQueueIfNecessary];
-[UIColorPickerViewController _shouldUseDarkGridInDarkMode];
-[UIColorPickerViewController _showsGridOnly];
-[UIColorPickerViewController _suggestedColors];
-[UIColorPickerViewController _supportsEyedropper];
-[UIColorPickerViewController _updateConfigurationIfNeeded];
-[UIColorPickerViewController _userInterfaceStyleForGrid];
-[UIColorPickerViewController beginAppearanceTransition:animated:];
-[UIColorPickerViewController colorQueue];
-[UIColorPickerViewController dismissEyedropper:];
-[UIColorPickerViewController maximumLinearExposure];
-[UIColorPickerViewController selectedColor];
-[UIColorPickerViewController setColorQueue:];
-[UIColorPickerViewController setMaximumLinearExposure:];
-[UIColorPickerViewController setSelectedColor:];
-[UIColorPickerViewController setSupportsAlpha:];
-[UIColorPickerViewController setSupportsEyedropper:];
-[UIColorPickerViewController supportsAlpha];
-[UIColorPickerViewController supportsEyedropper];
```
