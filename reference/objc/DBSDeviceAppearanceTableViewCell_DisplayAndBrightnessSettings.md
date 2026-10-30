# `DBSDeviceAppearanceTableViewCell`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSTableCell`
- Protocols: `DBSDeviceAppearanceOptionViewDelegate`
- 6 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"<DBSDeviceAppearanceTableViewCellDelegate>" _delegate;
@"DBSDeviceAppearanceOptionView" __lightOptionView;
@"DBSDeviceAppearanceOptionView" __darkOptionView;
@"UILayoutGuide" __leadingGuide;
@"UILayoutGuide" __middleGuide;
@"UILayoutGuide" __trailingGuide;
```

## Properties

```
@property (T@"DBSDeviceAppearanceOptionView",&,N,V__lightOptionView) _lightOptionView;
@property (T@"DBSDeviceAppearanceOptionView",&,N,V__darkOptionView) _darkOptionView;
@property (T@"UILayoutGuide",&,N,V__leadingGuide) _leadingGuide;
@property (T@"UILayoutGuide",&,N,V__middleGuide) _middleGuide;
@property (T@"UILayoutGuide",&,N,V__trailingGuide) _trailingGuide;
@property (T@"<DBSDeviceAppearanceTableViewCellDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DBSDeviceAppearanceTableViewCell cellStyle];
```

## Instance methods

```
-[DBSDeviceAppearanceTableViewCell init];
-[DBSDeviceAppearanceTableViewCell setDelegate:];
-[DBSDeviceAppearanceTableViewCell delegate];
-[DBSDeviceAppearanceTableViewCell initWithCoder:];
-[DBSDeviceAppearanceTableViewCell initWithStyle:reuseIdentifier:];
-[DBSDeviceAppearanceTableViewCell initWithFrame:];
-[DBSDeviceAppearanceTableViewCell _configureView];
-[DBSDeviceAppearanceTableViewCell _darkOptionView];
-[DBSDeviceAppearanceTableViewCell _leadingGuide];
-[DBSDeviceAppearanceTableViewCell _lightOptionView];
-[DBSDeviceAppearanceTableViewCell _middleGuide];
-[DBSDeviceAppearanceTableViewCell _trailingGuide];
-[DBSDeviceAppearanceTableViewCell set_darkOptionView:];
-[DBSDeviceAppearanceTableViewCell set_leadingGuide:];
-[DBSDeviceAppearanceTableViewCell set_lightOptionView:];
-[DBSDeviceAppearanceTableViewCell set_middleGuide:];
-[DBSDeviceAppearanceTableViewCell set_trailingGuide:];
-[DBSDeviceAppearanceTableViewCell userDidTapOnAppearanceOptionView:];
```
