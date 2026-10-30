# `DSDTOBannerView`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextViewDelegate`
- 4 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _presentingViewController;
@"UILabel" _titleLabel;
@"UITextView" _descriptionView;
@"NSLayoutConstraint" _cellHeightConstraint;
```

## Properties

```
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UITextView",&,N,V_descriptionView) descriptionView;
@property (T@"NSLayoutConstraint",&,N,V_cellHeightConstraint) cellHeightConstraint;
@property (T@"UIViewController",W,N,V_presentingViewController) presentingViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSDTOBannerView setTitleLabel:];
-[DSDTOBannerView init];
-[DSDTOBannerView setPresentingViewController:];
-[DSDTOBannerView titleLabel];
-[DSDTOBannerView presentingViewController];
-[DSDTOBannerView textView:primaryActionForTextItem:defaultAction:];
-[DSDTOBannerView descriptionView];
-[DSDTOBannerView setDescriptionView:];
-[DSDTOBannerView _setupView];
-[DSDTOBannerView preferredHeightForWidth:];
-[DSDTOBannerView _createTitleLabel];
-[DSDTOBannerView _createDescriptionTextViewWithLink];
-[DSDTOBannerView cellHeightConstraint];
-[DSDTOBannerView configureForWelcomeController:];
-[DSDTOBannerView setCellHeightConstraint:];
```
