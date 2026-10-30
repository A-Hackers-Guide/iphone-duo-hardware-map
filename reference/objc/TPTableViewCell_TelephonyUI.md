# `TPTableViewCell`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 8 instance variables, 10 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _accessiblityConstraintsEnabled;
B _constraintsLoaded;
B _foregroundViewLoaded;
@"UIView" _foregroundView;
@"NSLayoutConstraint" _foregroundViewLeadingAnchorLayoutConstraint;
@"NSLayoutConstraint" _foregroundViewTrailingAnchorLayoutConstraint;
@"NSLayoutConstraint" _foregroundViewTopAnchorLayoutConstraint;
@"NSLayoutConstraint" _foregroundViewBottomAnchorLayoutConstraint;
```

## Properties

```
@property (TB,N,GisAccessiblityConstraintsEnabled,V_accessiblityConstraintsEnabled) accessiblityConstraintsEnabled;
@property (TB,N,GisConstraintsLoaded,V_constraintsLoaded) constraintsLoaded;
@property (TB,N,GisForegroundViewLoaded,V_foregroundViewLoaded) foregroundViewLoaded;
@property (T@"UIView",&,N,V_foregroundView) foregroundView;
@property (T@"NSLayoutConstraint",R,N,V_foregroundViewLeadingAnchorLayoutConstraint) foregroundViewLeadingAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",R,N,V_foregroundViewTrailingAnchorLayoutConstraint) foregroundViewTrailingAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",R,N,V_foregroundViewTopAnchorLayoutConstraint) foregroundViewTopAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",R,N,V_foregroundViewBottomAnchorLayoutConstraint) foregroundViewBottomAnchorLayoutConstraint;
@property (T@"UIColor",&,N) foregroundColor;
@property (T{UIEdgeInsets=dddd},R,N) intrinsicSeparatorInset;
```

## Class methods

```
+[TPTableViewCell requiresConstraintBasedLayout];
+[TPTableViewCell separatorInsetForContentSizeCategory:];
```

## Instance methods

```
-[TPTableViewCell commonInit];
-[TPTableViewCell setForegroundColor:];
-[TPTableViewCell updateConstraintsConstants];
-[TPTableViewCell foregroundView];
-[TPTableViewCell init];
-[TPTableViewCell layoutSubviews];
-[TPTableViewCell loadConstraints];
-[TPTableViewCell setForegroundView:];
-[TPTableViewCell updateFonts];
-[TPTableViewCell updateConstraints];
-[TPTableViewCell initWithCoder:];
-[TPTableViewCell traitCollectionDidChange:];
-[TPTableViewCell foregroundColor];
-[TPTableViewCell initWithStyle:reuseIdentifier:];
-[TPTableViewCell initWithFrame:];
-[TPTableViewCell unloadConstraints];
-[TPTableViewCell loadContentView];
-[TPTableViewCell foregroundViewBottomAnchorLayoutConstraint];
-[TPTableViewCell foregroundViewLeadingAnchorLayoutConstraint];
-[TPTableViewCell foregroundViewTopAnchorLayoutConstraint];
-[TPTableViewCell foregroundViewTrailingAnchorLayoutConstraint];
-[TPTableViewCell intrinsicSeparatorInset];
-[TPTableViewCell isAccessiblityConstraintsEnabled];
-[TPTableViewCell isConstraintsLoaded];
-[TPTableViewCell isForegroundViewLoaded];
-[TPTableViewCell setAccessiblityConstraintsEnabled:];
-[TPTableViewCell setConstraintsLoaded:];
-[TPTableViewCell setForegroundViewLoaded:];
```
