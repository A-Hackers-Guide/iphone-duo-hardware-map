# `CAMInstructionLabel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 14 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _wantsLargerText;
@"NSString" _text;
@"<CAMInstructionLabelDelegate>" _delegate;
q _style;
@"UILabel" __label;
@"NSAttributedString" __attributedText;
@"UIActivityIndicatorView" __activityIndicatorView;
@"NSString" __symbolSuffixName;
```

## Properties

```
@property (T@"UILabel",R,N,V__label) _label;
@property (T@"NSAttributedString",C,N,V__attributedText) _attributedText;
@property (T@"UIActivityIndicatorView",&,N,V__activityIndicatorView) _activityIndicatorView;
@property (T{UIEdgeInsets=dddd},R,N) _textInsets;
@property (T@"UIColor",R,N) _textColor;
@property (Td,R,N) _backgroundAlpha;
@property (Td,R,N) _backgroundColorWhiteValue;
@property (T@"NSString",R,N) _symbolPrefixName;
@property (T@"NSString",R,N,V__symbolSuffixName) _symbolSuffixName;
@property (TB,R,N) _wantsMonospacedNumerals;
@property (T@"NSString",C,N,V_text) text;
@property (T@"<CAMInstructionLabelDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_style) style;
@property (TB,N,V_wantsLargerText) wantsLargerText;
```

## Instance methods

```
-[CAMInstructionLabel _label];
-[CAMInstructionLabel _backgroundAlpha];
-[CAMInstructionLabel intrinsicContentSize];
-[CAMInstructionLabel _textColor];
-[CAMInstructionLabel text];
-[CAMInstructionLabel layoutSubviews];
-[CAMInstructionLabel _updateLabel];
-[CAMInstructionLabel style];
-[CAMInstructionLabel _preferredContentSizeCategoryDidChange];
-[CAMInstructionLabel setStyle:];
-[CAMInstructionLabel sizeThatFits:];
-[CAMInstructionLabel setDelegate:];
-[CAMInstructionLabel _textInsets];
-[CAMInstructionLabel delegate];
-[CAMInstructionLabel _activityIndicatorView];
-[CAMInstructionLabel setText:];
-[CAMInstructionLabel _symbolSuffixName];
-[CAMInstructionLabel initWithFrame:];
-[CAMInstructionLabel _updateLayerCornerRadius];
-[CAMInstructionLabel _attributedText];
-[CAMInstructionLabel _updateAttributedText];
-[CAMInstructionLabel _textAttributes];
-[CAMInstructionLabel _fontSize];
-[CAMInstructionLabel wantsLargerText];
-[CAMInstructionLabel _applyMonospacedNumeralsToText:];
-[CAMInstructionLabel _backgroundColorWhiteValue];
-[CAMInstructionLabel _defaultCornerRadius];
-[CAMInstructionLabel _symbolPrefixName];
-[CAMInstructionLabel _wantsMonospacedNumerals];
-[CAMInstructionLabel _wantsPrefixActivityIndicatorView];
-[CAMInstructionLabel setWantsLargerText:];
-[CAMInstructionLabel set_activityIndicatorView:];
-[CAMInstructionLabel set_attributedText:];
```
