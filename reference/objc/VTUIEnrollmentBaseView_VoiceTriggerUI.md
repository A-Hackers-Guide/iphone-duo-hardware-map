# `VTUIEnrollmentBaseView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextViewDelegate`
- 12 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _iconImageView;
@"UIView" _scrollContainerView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
@"UILabel" _instructionLabel;
@"UIView" _contentView;
@"UITextView" _privacyTextView;
@"UIScrollView" _scrollView;
@"_UIBackdropView" _backdropView;
@"NSLayoutConstraint" _readableLeftAnchorConstraint;
@"NSLayoutConstraint" _readableRightAnchorConstraint;
@"<VTUIEnrollmentDelegate>" _enrollmentDelegate;
```

## Properties

```
@property (T@"<VTUIEnrollmentDelegate>",W,N,V_enrollmentDelegate) enrollmentDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUIEnrollmentBaseView backdropView];
-[VTUIEnrollmentBaseView setContentView:];
-[VTUIEnrollmentBaseView footerView];
-[VTUIEnrollmentBaseView layoutSubviews];
-[VTUIEnrollmentBaseView setSubtitle:];
-[VTUIEnrollmentBaseView safeAreaInsetsDidChange];
-[VTUIEnrollmentBaseView updateConstraints];
-[VTUIEnrollmentBaseView traitCollectionDidChange:];
-[VTUIEnrollmentBaseView setTitle:];
-[VTUIEnrollmentBaseView initWithFrame:];
-[VTUIEnrollmentBaseView _backdropStyle];
-[VTUIEnrollmentBaseView setShowsVerticalScrollIndicator:];
-[VTUIEnrollmentBaseView textView:shouldInteractWithURL:inRange:interaction:];
-[VTUIEnrollmentBaseView _setupUI];
-[VTUIEnrollmentBaseView _createPrivacyTextView];
-[VTUIEnrollmentBaseView enrollmentDelegate];
-[VTUIEnrollmentBaseView fadeInSubviews];
-[VTUIEnrollmentBaseView imageOffsetFromTop];
-[VTUIEnrollmentBaseView setEnrollmentDelegate:];
-[VTUIEnrollmentBaseView setInstructionText:];
-[VTUIEnrollmentBaseView showPrivacyTextView];
```
