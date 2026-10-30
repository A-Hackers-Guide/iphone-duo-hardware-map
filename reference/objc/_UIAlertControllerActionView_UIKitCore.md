# `_UIAlertControllerActionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `_UIAlertActionViewRepresentation`
- 33 instance variables, 13 properties, 64 instance methods, 0 class methods

## Instance variables

```
B _highlighted;
@"UIView" _labelContainerView;
@"UILabel" _label;
@"NSLayoutConstraint" _axLabelContainerWidthConstraint;
@"NSLayoutConstraint" _labelContainerLeadingConstraint;
@"NSLayoutConstraint" _labelContainerTrailingConstraint;
@"NSLayoutConstraint" _labelContainerCenterXConstraint;
@"NSLayoutConstraint" _labelContainerLeadingPinConstraint;
@"NSLayoutConstraint" _labelContainerTrailingPinConstraint;
@"NSLayoutConstraint" _labelWidthConstraint;
@"NSLayoutConstraint" _labelCenterLeadingConstraint;
@"UIView" _contentViewControllerContainerView;
@"NSArray" _contentViewControllerConstraints;
@"UILabel" _descriptiveLabel;
@"NSArray" _havingDescriptiveLabelConstraints;
@"NSArray" _notHavingDescriptiveLabelConstraints;
@"NSLayoutConstraint" _descriptiveLabelWidthConstraint;
@"NSLayoutConstraint" _descriptiveLabelTrailingToLabelLeadingLabelConstraint;
@"NSLayoutConstraint" _descriptiveLabelTrailingToContainerCenterConstraint;
@"UIImageView" _checkView;
@"NSLayoutConstraint" _checkToMarginConstraint;
@"UIImageView" _imageView;
@"NSLayoutConstraint" _marginToImageConstraint;
@"NSLayoutConstraint" _imageViewBaselineOrCenterYConstraint;
@"NSLayoutConstraint" _imageViewTopConstraint;
@"NSLayoutConstraint" _imageViewBottomConstraint;
@"NSLayoutConstraint" _minimumHeightConstraint;
@"UIAlertAction" _action;
@"UIAlertControllerVisualStyle" _visualStyle;
@"_UIAlertControllerActionViewMetrics" _metrics;
B _hasDescriptiveText;
d _axEnforcedWidth;
@"UIAlertController" _alertController;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,V_labelContainerCenterXConstraint) labelContainerCenterXConstraint;
@property (T@"NSLayoutConstraint",&,V_labelContainerLeadingPinConstraint) labelContainerLeadingPinConstraint;
@property (T@"NSLayoutConstraint",&,V_labelContainerTrailingPinConstraint) labelContainerTrailingPinConstraint;
@property (T@"UIAlertAction",C,N) action;
@property (T@"UIAlertController",W,N,V_alertController) alertController;
@property (T@"UIAlertControllerVisualStyle",W,N,V_visualStyle) visualStyle;
@property (TB,N,GisHighlighted) highlighted;
@property (Td,R) currentDescriptiveLabelTextWidth;
@property (Td,R) currentLabelTextWidth;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIAlertControllerActionView _updateImageView];
-[_UIAlertControllerActionView applyMetrics:];
-[_UIAlertControllerActionView setVisualStyle:];
-[_UIAlertControllerActionView visualStyle];
-[_UIAlertControllerActionView isHighlighted];
-[_UIAlertControllerActionView alertController];
-[_UIAlertControllerActionView dealloc];
-[_UIAlertControllerActionView _action:changedToChecked:];
-[_UIAlertControllerActionView _action:changedToBePreferred:];
-[_UIAlertControllerActionView setAction:];
-[_UIAlertControllerActionView action];
-[_UIAlertControllerActionView _updateStyle];
-[_UIAlertControllerActionView tintColorDidChange];
-[_UIAlertControllerActionView setHighlighted:];
-[_UIAlertControllerActionView focusItemDeferralMode];
-[_UIAlertControllerActionView _action:changedToTitle:];
-[_UIAlertControllerActionView description];
-[_UIAlertControllerActionView initWithCoder:];
-[_UIAlertControllerActionView _action:changedToTitleTextAlignment:];
-[_UIAlertControllerActionView _action:updatedTitleTextColor:];
-[_UIAlertControllerActionView setAlertController:];
-[_UIAlertControllerActionView _action:updatedImageTintColor:];
-[_UIAlertControllerActionView initWithFrame:];
-[_UIAlertControllerActionView _action:changedToEnabled:];
-[_UIAlertControllerActionView hasLayoutHeightConstraintsIdenticalToInterfaceActionCustomView:];
-[_UIAlertControllerActionView labelContainerCenterXConstraint];
-[_UIAlertControllerActionView updateSizeUsingAXEnforcedWidth:];
-[_UIAlertControllerActionView _buildCheckViewConstraints];
-[_UIAlertControllerActionView _buildConstraints];
-[_UIAlertControllerActionView _buildContentViewControllerContainerConstraints];
-[_UIAlertControllerActionView _buildHavingDescriptiveLabelConstraints];
-[_UIAlertControllerActionView _buildImageViewConstraints];
-[_UIAlertControllerActionView _buildNotHavingDescriptiveLabelConstraints];
-[_UIAlertControllerActionView _contentSizeChanged];
-[_UIAlertControllerActionView _effectiveTitleTextAlignment];
-[_UIAlertControllerActionView _interfaceActionViewState];
-[_UIAlertControllerActionView _loadCheckView];
-[_UIAlertControllerActionView _loadContentViewControllerContainerViewIfNecessary];
-[_UIAlertControllerActionView _loadContentViewControllerView];
-[_UIAlertControllerActionView _loadDescriptiveLabel];
-[_UIAlertControllerActionView _loadImageView];
-[_UIAlertControllerActionView _prepareConstraintsForHavingDescriptiveText:];
-[_UIAlertControllerActionView _prepareConstraintsForImage:];
-[_UIAlertControllerActionView _recomputeColors];
-[_UIAlertControllerActionView _removeContentViewControllerContainerViewSubviews];
-[_UIAlertControllerActionView _updateCheckImageView];
-[_UIAlertControllerActionView _updateContentViewControllerContainerViewConstraints];
-[_UIAlertControllerActionView _updateDescriptiveText];
-[_UIAlertControllerActionView _updateHavingDescriptiveLabelConstraints];
-[_UIAlertControllerActionView _updateImageMargins];
-[_UIAlertControllerActionView _updateImageViewAttributes];
-[_UIAlertControllerActionView _updateLabelAttributes];
-[_UIAlertControllerActionView _updateLabelContainerConstraints];
-[_UIAlertControllerActionView _updateMinimumHeightAndDesiredWidthConstraints];
-[_UIAlertControllerActionView _updateTextAlignmentForHavingDescriptiveText:titleTextAlignment:];
-[_UIAlertControllerActionView currentDescriptiveLabelTextWidth];
-[_UIAlertControllerActionView currentLabelTextWidth];
-[_UIAlertControllerActionView hasActiveMinimumSizeConstraintsWithSize:];
-[_UIAlertControllerActionView labelContainerLeadingPinConstraint];
-[_UIAlertControllerActionView labelContainerTrailingPinConstraint];
-[_UIAlertControllerActionView setLabelContainerCenterXConstraint:];
-[_UIAlertControllerActionView setLabelContainerLeadingPinConstraint:];
-[_UIAlertControllerActionView setLabelContainerTrailingPinConstraint:];
-[_UIAlertControllerActionView underlyingInterfaceActionRepresentationDidChange];
```
