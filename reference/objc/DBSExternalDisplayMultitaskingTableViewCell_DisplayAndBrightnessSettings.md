# `DBSExternalDisplayMultitaskingTableViewCell`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSTableCell`
- Protocols: `DBSExternalDisplayManagerObserver`, `DBSExternalDisplayMultitaskingOptionViewDelegate`
- 5 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<DBSExternalDisplayMultitaskingTableViewCellDelegate>" _delegate;
@"DBSExternalDisplayMultitaskingOptionView" _screenMirroringOptionView;
@"DBSExternalDisplayMultitaskingOptionView" _extendedDisplayOptionView;
@"NSLayoutConstraint" _screenMirroringOptionOneThirdConstraint;
@"NSLayoutConstraint" _multitaskingOptionEqualWidthConstraint;
```

## Properties

```
@property (T@"DBSExternalDisplayMultitaskingOptionView",&,N,V_screenMirroringOptionView) screenMirroringOptionView;
@property (T@"DBSExternalDisplayMultitaskingOptionView",&,N,V_extendedDisplayOptionView) extendedDisplayOptionView;
@property (T@"NSLayoutConstraint",&,N,V_screenMirroringOptionOneThirdConstraint) screenMirroringOptionOneThirdConstraint;
@property (T@"NSLayoutConstraint",&,N,V_multitaskingOptionEqualWidthConstraint) multitaskingOptionEqualWidthConstraint;
@property (T@"<DBSExternalDisplayMultitaskingTableViewCellDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DBSExternalDisplayMultitaskingTableViewCell cellStyle];
```

## Instance methods

```
-[DBSExternalDisplayMultitaskingTableViewCell dealloc];
-[DBSExternalDisplayMultitaskingTableViewCell layoutSubviews];
-[DBSExternalDisplayMultitaskingTableViewCell setDelegate:];
-[DBSExternalDisplayMultitaskingTableViewCell prepareForReuse];
-[DBSExternalDisplayMultitaskingTableViewCell delegate];
-[DBSExternalDisplayMultitaskingTableViewCell initWithStyle:reuseIdentifier:];
-[DBSExternalDisplayMultitaskingTableViewCell refreshCellContentsWithSpecifier:];
-[DBSExternalDisplayMultitaskingTableViewCell _configureView];
-[DBSExternalDisplayMultitaskingTableViewCell _updateSelectedMultitaskingOptionView:];
-[DBSExternalDisplayMultitaskingTableViewCell extendedDisplayOptionView];
-[DBSExternalDisplayMultitaskingTableViewCell externalDisplayManager:didUpdateMirroringEnabledState:];
-[DBSExternalDisplayMultitaskingTableViewCell multitaskingOptionEqualWidthConstraint];
-[DBSExternalDisplayMultitaskingTableViewCell screenMirroringOptionOneThirdConstraint];
-[DBSExternalDisplayMultitaskingTableViewCell screenMirroringOptionView];
-[DBSExternalDisplayMultitaskingTableViewCell setExtendedDisplayOptionView:];
-[DBSExternalDisplayMultitaskingTableViewCell setMultitaskingOptionEqualWidthConstraint:];
-[DBSExternalDisplayMultitaskingTableViewCell setScreenMirroringOptionOneThirdConstraint:];
-[DBSExternalDisplayMultitaskingTableViewCell setScreenMirroringOptionView:];
-[DBSExternalDisplayMultitaskingTableViewCell userDidTapOnMultitaskingOptionView:];
```
