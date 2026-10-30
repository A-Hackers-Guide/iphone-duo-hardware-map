# `CAMFocalLengthLabel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
q _focalLength;
@"UILabel" __unitLabel;
@"UILabel" __numeralLabel;
@"UIFont" __numeralFont;
@"UIFont" __unitFont;
{CGSize="width"d"height"d} __numeralSize;
{CGSize="width"d"height"d} __unitSize;
```

## Properties

```
@property (T@"UILabel",R,N,V__unitLabel) _unitLabel;
@property (T@"UILabel",R,N,V__numeralLabel) _numeralLabel;
@property (T@"UIFont",&,N,V__numeralFont) _numeralFont;
@property (T@"UIFont",&,N,V__unitFont) _unitFont;
@property (T{CGSize=dd},N,V__numeralSize) _numeralSize;
@property (T{CGSize=dd},N,V__unitSize) _unitSize;
@property (Tq,N,V_focalLength) focalLength;
```

## Instance methods

```
-[CAMFocalLengthLabel focalLength];
-[CAMFocalLengthLabel intrinsicContentSize];
-[CAMFocalLengthLabel setFocalLength:];
-[CAMFocalLengthLabel layoutSubviews];
-[CAMFocalLengthLabel tintColorDidChange];
-[CAMFocalLengthLabel setFocalLength:animated:];
-[CAMFocalLengthLabel _preferredContentSizeCategoryChanged];
-[CAMFocalLengthLabel initWithFrame:];
-[CAMFocalLengthLabel _updateUnitText];
-[CAMFocalLengthLabel _numeralFont];
-[CAMFocalLengthLabel _numeralLabel];
-[CAMFocalLengthLabel _numeralSize];
-[CAMFocalLengthLabel _unitFont];
-[CAMFocalLengthLabel _unitLabel];
-[CAMFocalLengthLabel _unitSize];
-[CAMFocalLengthLabel _updateFontsAndTextAnimated:];
-[CAMFocalLengthLabel _updateNumeralTextAnimated:];
-[CAMFocalLengthLabel set_numeralFont:];
-[CAMFocalLengthLabel set_numeralSize:];
-[CAMFocalLengthLabel set_unitFont:];
-[CAMFocalLengthLabel set_unitSize:];
```
