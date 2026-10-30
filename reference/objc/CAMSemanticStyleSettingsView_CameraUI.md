# `CAMSemanticStyleSettingsView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMSemanticStylePickerDelegate`, `CEKBadgeViewDelegate`
- 12 instance variables, 16 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _showsTitle;
@"<CAMSemanticStyleSettingsViewDelegate>" _delegate;
@"UIScrollView" __scrollView;
@"UILabel" __titleLabel;
@"UILabel" __descriptionLabel;
@"UIButton" __selectButton;
@"CAMSemanticStylePicker" __semanticStylePicker;
@"CAMSemanticStyleDetailView" __semanticStyleDetailView;
@"NSArray" __semanticStyles;
@"NSArray" __semanticStyleBadges;
@"NSArray" __semanticStyleImageViews;
@"NSLayoutConstraint" __descriptionLabelTopConstraint;
```

## Properties

```
@property (T@"UIScrollView",R,N,V__scrollView) _scrollView;
@property (T@"UILabel",R,N,V__titleLabel) _titleLabel;
@property (T@"UILabel",R,N,V__descriptionLabel) _descriptionLabel;
@property (T@"UIButton",R,N,V__selectButton) _selectButton;
@property (T@"CAMSemanticStylePicker",R,N,V__semanticStylePicker) _semanticStylePicker;
@property (T@"CAMSemanticStyleDetailView",R,N,V__semanticStyleDetailView) _semanticStyleDetailView;
@property (T@"NSArray",R,N,V__semanticStyles) _semanticStyles;
@property (T@"NSArray",R,N,V__semanticStyleBadges) _semanticStyleBadges;
@property (T@"NSArray",R,N,V__semanticStyleImageViews) _semanticStyleImageViews;
@property (T@"NSLayoutConstraint",&,N,S_setDescriptionLabelTopConstraint:,V__descriptionLabelTopConstraint) _descriptionLabelTopConstraint;
@property (TB,N,V_showsTitle) showsTitle;
@property (T@"<CAMSemanticStyleSettingsViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSemanticStyleSettingsView _scrollView];
-[CAMSemanticStyleSettingsView _semanticStyles];
-[CAMSemanticStyleSettingsView init];
-[CAMSemanticStyleSettingsView badgeViewDidChangeIntrinsicContentSize:];
-[CAMSemanticStyleSettingsView layoutSubviews];
-[CAMSemanticStyleSettingsView setDelegate:];
-[CAMSemanticStyleSettingsView _semanticStyleBadges];
-[CAMSemanticStyleSettingsView delegate];
-[CAMSemanticStyleSettingsView setShowsTitle:];
-[CAMSemanticStyleSettingsView semanticStylePickerDidChangeSelectedStyle:];
-[CAMSemanticStyleSettingsView semanticStylePickerDidScroll:];
-[CAMSemanticStyleSettingsView showsTitle];
-[CAMSemanticStyleSettingsView _titleLabel];
-[CAMSemanticStyleSettingsView _descriptionLabel];
-[CAMSemanticStyleSettingsView _descriptionLabelTopConstraint];
-[CAMSemanticStyleSettingsView _handleUseStyleButtonReleased:];
-[CAMSemanticStyleSettingsView _layoutSemanticStyleMaskedBadgesForContentFrame:];
-[CAMSemanticStyleSettingsView _previewImageNameForSemanticStylePreset:];
-[CAMSemanticStyleSettingsView _selectButton];
-[CAMSemanticStyleSettingsView _semanticStyleDetailView];
-[CAMSemanticStyleSettingsView _semanticStyleImageViews];
-[CAMSemanticStyleSettingsView _semanticStylePicker];
-[CAMSemanticStyleSettingsView _setDescriptionLabelTopConstraint:];
-[CAMSemanticStyleSettingsView _updateUIForShowsTitle];
-[CAMSemanticStyleSettingsView _updateUIForStyle:];
```
