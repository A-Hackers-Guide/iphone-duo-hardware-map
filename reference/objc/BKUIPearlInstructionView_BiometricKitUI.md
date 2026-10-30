# `BKUIPearlInstructionView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _darkMode;
@"NSString" _instruction;
@"NSString" _detail;
@"UILabel" _instructionLabel;
@"UILabel" _detailLabel;
@"NSLayoutConstraint" _labelsWidthConstraint;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _labelsHorizontalMargin;
```

## Properties

```
@property (T@"UILabel",W,N,V_instructionLabel) instructionLabel;
@property (T@"UILabel",W,N,V_detailLabel) detailLabel;
@property (T{UIEdgeInsets=dddd},N,V_labelsHorizontalMargin) labelsHorizontalMargin;
@property (T@"NSLayoutConstraint",&,N,V_labelsWidthConstraint) labelsWidthConstraint;
@property (T@"NSString",&,N,V_instruction) instruction;
@property (T@"NSString",&,N,V_detail) detail;
@property (TB,N,V_darkMode) darkMode;
@property (T@"NSLayoutYAxisAnchor",R,N) instructionTextTopAnchor;
```

## Instance methods

```
-[BKUIPearlInstructionView setDetailLabel:];
-[BKUIPearlInstructionView intrinsicContentSize];
-[BKUIPearlInstructionView init];
-[BKUIPearlInstructionView detailLabel];
-[BKUIPearlInstructionView detail];
-[BKUIPearlInstructionView viewForLastBaselineLayout];
-[BKUIPearlInstructionView setDarkMode:];
-[BKUIPearlInstructionView viewForFirstBaselineLayout];
-[BKUIPearlInstructionView setDetail:];
-[BKUIPearlInstructionView darkMode];
-[BKUIPearlInstructionView instructionLabel];
-[BKUIPearlInstructionView setInstructionLabel:];
-[BKUIPearlInstructionView setInstruction:];
-[BKUIPearlInstructionView instruction];
-[BKUIPearlInstructionView _configureConstraints];
-[BKUIPearlInstructionView instructionTextTopAnchor];
-[BKUIPearlInstructionView labelsHorizontalMargin];
-[BKUIPearlInstructionView labelsWidthConstraint];
-[BKUIPearlInstructionView setLabelsHorizontalMargin:];
-[BKUIPearlInstructionView setLabelsWidthConstraint:];
```
