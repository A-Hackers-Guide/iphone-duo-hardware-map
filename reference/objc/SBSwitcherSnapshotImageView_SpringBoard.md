# `SBSwitcherSnapshotImageView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBReusableView`
- 12 instance variables, 15 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _imageView;
@"UIView" _scalingView;
d _cornerRadius;
Q _maskedCorners;
B _allowStatusBarToOverlap;
B _usesNonuniformScaling;
B _hasOpaqueContents;
B _stretchToFillBounds;
B _allowsEdgeAntialiasing;
q _contentMode;
q _orientationForClassicLayout;
{CACornerRadii="minXMaxY"{CGSize="width"d"height"d}"maxXMaxY"{CGSize="width"d"height"d}"maxXMinY"{CGSize="width"d"height"d}"minXMinY"{CGSize="width"d"height"d}} _cornerRadii;
```

## Properties

```
@property (T@"UIImage",&,N) image;
@property (Tq,N,V_contentMode) contentMode;
@property (Td,N) cornerRadius;
@property (TQ,N) maskedCorners;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N,V_cornerRadii) cornerRadii;
@property (TB,N,V_usesNonuniformScaling) usesNonuniformScaling;
@property (TB,N,V_hasOpaqueContents) hasOpaqueContents;
@property (TB,N,V_stretchToFillBounds) stretchToFillBounds;
@property (TB,N,V_allowsEdgeAntialiasing) allowsEdgeAntialiasing;
@property (TB,N,V_allowStatusBarToOverlap) allowStatusBarToOverlap;
@property (Tq,N,V_orientationForClassicLayout) orientationForClassicLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherSnapshotImageView cornerRadii];
-[SBSwitcherSnapshotImageView setHasOpaqueContents:];
-[SBSwitcherSnapshotImageView _updateCornerRadius];
-[SBSwitcherSnapshotImageView initWithImage:];
-[SBSwitcherSnapshotImageView setStretchToFillBounds:];
-[SBSwitcherSnapshotImageView contentMode];
-[SBSwitcherSnapshotImageView setContentMode:];
-[SBSwitcherSnapshotImageView _transformVerticalScale];
-[SBSwitcherSnapshotImageView hasOpaqueContents];
-[SBSwitcherSnapshotImageView setCornerRadii:];
-[SBSwitcherSnapshotImageView layoutSubviews];
-[SBSwitcherSnapshotImageView allowsEdgeAntialiasing];
-[SBSwitcherSnapshotImageView maskedCorners];
-[SBSwitcherSnapshotImageView setCornerRadius:];
-[SBSwitcherSnapshotImageView _isUsingExternalClassicLayout];
-[SBSwitcherSnapshotImageView stretchToFillBounds];
-[SBSwitcherSnapshotImageView setMaskedCorners:];
-[SBSwitcherSnapshotImageView setAllowStatusBarToOverlap:];
-[SBSwitcherSnapshotImageView setAllowsEdgeAntialiasing:];
-[SBSwitcherSnapshotImageView _transformScale];
-[SBSwitcherSnapshotImageView allowStatusBarToOverlap];
-[SBSwitcherSnapshotImageView prepareForReuse];
-[SBSwitcherSnapshotImageView cornerRadius];
-[SBSwitcherSnapshotImageView setOrientationForClassicLayout:];
-[SBSwitcherSnapshotImageView orientationForClassicLayout];
-[SBSwitcherSnapshotImageView usesNonuniformScaling];
-[SBSwitcherSnapshotImageView setUsesNonuniformScaling:];
-[SBSwitcherSnapshotImageView scalingTransform];
-[SBSwitcherSnapshotImageView image];
-[SBSwitcherSnapshotImageView _transformHorizontalScale];
-[SBSwitcherSnapshotImageView setImage:];
```
