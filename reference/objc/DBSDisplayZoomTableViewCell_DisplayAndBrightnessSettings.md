# `DBSDisplayZoomTableViewCell`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- Protocols: `DBSDisplayZoomOptionViewDelegate`
- 7 instance variables, 11 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"<DBSDisplayZoomTableViewCellDelegate>" _delegate;
@"NSString" _resolutionWarning;
@"DBSDisplayZoomOptionView" _standardOptionView;
@"DBSDisplayZoomOptionView" _zoomedOptionView;
@"DBSDisplayZoomOptionView" _denseOptionView;
@"DBSDisplayZoomOptionView" _denserOptionView;
@"UILabel" _warningLabel;
```

## Properties

```
@property (T@"DBSDisplayZoomOptionView",&,N,V_standardOptionView) standardOptionView;
@property (T@"DBSDisplayZoomOptionView",&,N,V_zoomedOptionView) zoomedOptionView;
@property (T@"DBSDisplayZoomOptionView",&,N,V_denseOptionView) denseOptionView;
@property (T@"DBSDisplayZoomOptionView",&,N,V_denserOptionView) denserOptionView;
@property (T@"UILabel",&,N,V_warningLabel) warningLabel;
@property (T@"<DBSDisplayZoomTableViewCellDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_resolutionWarning) resolutionWarning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DBSDisplayZoomTableViewCell cellStyle];
```

## Instance methods

```
-[DBSDisplayZoomTableViewCell startAnimation];
-[DBSDisplayZoomTableViewCell setDelegate:];
-[DBSDisplayZoomTableViewCell delegate];
-[DBSDisplayZoomTableViewCell stopAnimation];
-[DBSDisplayZoomTableViewCell setWarningLabel:];
-[DBSDisplayZoomTableViewCell warningLabel];
-[DBSDisplayZoomTableViewCell denseOptionView];
-[DBSDisplayZoomTableViewCell _configureForLegacy];
-[DBSDisplayZoomTableViewCell _configureForThreeDisplayOptionsWithLeadingView:middleView:trailingView:];
-[DBSDisplayZoomTableViewCell _configureForTwoDisplayOptionsWithLeadingView:trailingView:];
-[DBSDisplayZoomTableViewCell _optionViewsByDensity];
-[DBSDisplayZoomTableViewCell configureView];
-[DBSDisplayZoomTableViewCell denserOptionView];
-[DBSDisplayZoomTableViewCell resolutionWarning];
-[DBSDisplayZoomTableViewCell setDenseOptionView:];
-[DBSDisplayZoomTableViewCell setDenserOptionView:];
-[DBSDisplayZoomTableViewCell setResolutionWarning:];
-[DBSDisplayZoomTableViewCell setStandardOptionView:];
-[DBSDisplayZoomTableViewCell setZoomedOptionView:];
-[DBSDisplayZoomTableViewCell standardOptionView];
-[DBSDisplayZoomTableViewCell updateSelectedViewWithOption:];
-[DBSDisplayZoomTableViewCell userDidTapOnDisplayZoomOptionView:];
-[DBSDisplayZoomTableViewCell zoomedOptionView];
```
