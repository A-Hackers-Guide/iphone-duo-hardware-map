# `SHSDualSIMListCell`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSTableCell`
- 6 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"SHSBadgeView" _badgeView;
@"UILabel" _nameLabel;
@"UILabel" _numberLabel;
@"UILabel" _detailToneTextLabel;
@"SHSBadgeView" _centeredBadgeView;
@"UILabel" _centeredNameLabel;
```

## Properties

```
@property (T@"SHSBadgeView",&,N,V_badgeView) badgeView;
@property (T@"UILabel",&,N,V_nameLabel) nameLabel;
@property (T@"UILabel",&,N,V_numberLabel) numberLabel;
@property (T@"UILabel",&,N,V_detailToneTextLabel) detailToneTextLabel;
@property (T@"SHSBadgeView",&,N,V_centeredBadgeView) centeredBadgeView;
@property (T@"UILabel",&,N,V_centeredNameLabel) centeredNameLabel;
```

## Class methods

```
+[SHSDualSIMListCell cellStyle];
```

## Instance methods

```
-[SHSDualSIMListCell badgeView];
-[SHSDualSIMListCell textLabel];
-[SHSDualSIMListCell nameLabel];
-[SHSDualSIMListCell setBadgeView:];
-[SHSDualSIMListCell initWithStyle:reuseIdentifier:];
-[SHSDualSIMListCell refreshCellContentsWithSpecifier:];
-[SHSDualSIMListCell canReload];
-[SHSDualSIMListCell detailTextLabel];
-[SHSDualSIMListCell setNameLabel:];
-[SHSDualSIMListCell centeredBadgeView];
-[SHSDualSIMListCell centeredNameLabel];
-[SHSDualSIMListCell setCenteredBadgeView:];
-[SHSDualSIMListCell setCenteredNameLabel:];
-[SHSDualSIMListCell canBeChecked];
-[SHSDualSIMListCell setNumberLabel:];
-[SHSDualSIMListCell numberLabel];
-[SHSDualSIMListCell _setBadge:andLabel:andPhoneNumber:];
-[SHSDualSIMListCell _setCenteredBadge:andLabel:];
-[SHSDualSIMListCell detailToneTextLabel];
-[SHSDualSIMListCell setDetailToneTextLabel:];
```
