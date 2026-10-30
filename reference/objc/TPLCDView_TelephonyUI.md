# `TPLCDView`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPLCDBar`
- 6 instance variables, 1 properties, 31 instance methods, 2 class methods

## Instance variables

```
@"UIView" _contentView;
@"TPLCDTextView" _textView;
@"TPLCDTextView" _labelView;
@"TPLCDSubImageView" _imageView;
b1 _layoutAsLabelled;
B _verticallyCenterTextViewIfLabelless;
```

## Properties

```
@property (TB,V_verticallyCenterTextViewIfLabelless) verticallyCenterTextViewIfLabelless;
```

## Class methods

```
+[TPLCDView defaultLabelFontSize];
+[TPLCDView defaultTextFontSize];
```

## Instance methods

```
-[TPLCDView didMoveToWindow];
-[TPLCDView text];
-[TPLCDView label];
-[TPLCDView setLabel:];
-[TPLCDView layoutSubviews];
-[TPLCDView setText:];
-[TPLCDView setShadowColor:];
-[TPLCDView _labelFrame];
-[TPLCDView _imageViewFrame];
-[TPLCDView _labelVInset];
-[TPLCDView _resetContentViewFrame];
-[TPLCDView _text1Frame];
-[TPLCDView _textVInset];
-[TPLCDView blinkLabel];
-[TPLCDView didFinishAnimatingLCDLabelFadeOut:finished:context:];
-[TPLCDView fullSizedContentViewFrame];
-[TPLCDView initWithDefaultSizeForOrientation:];
-[TPLCDView secondLineText];
-[TPLCDView setContentsAlpha:];
-[TPLCDView setLabel:animate:];
-[TPLCDView setLabelFontSize:];
-[TPLCDView setLayoutAsLabelled:];
-[TPLCDView setSecondLineText:];
-[TPLCDView setSubImage:];
-[TPLCDView setTextFontSize:];
-[TPLCDView setVerticallyCenterTextViewIfLabelless:];
-[TPLCDView shouldCenterContentView];
-[TPLCDView shouldCenterText];
-[TPLCDView subImage];
-[TPLCDView textFrame];
-[TPLCDView verticallyCenterTextViewIfLabelless];
```
