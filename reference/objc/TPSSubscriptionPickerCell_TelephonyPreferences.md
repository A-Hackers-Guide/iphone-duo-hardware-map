# `TPSSubscriptionPickerCell`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSTableCell`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"TPBadgeView" _badgeView;
@"UILabel" _nameLabel;
@"UILabel" _numberLabel;
@"TPBadgeView" _centeredBadgeView;
@"UILabel" _centeredNameLabel;
```

## Properties

```
@property (T@"TPBadgeView",&,N,V_badgeView) badgeView;
@property (T@"UILabel",&,N,V_nameLabel) nameLabel;
@property (T@"UILabel",&,N,V_numberLabel) numberLabel;
@property (T@"TPBadgeView",&,N,V_centeredBadgeView) centeredBadgeView;
@property (T@"UILabel",&,N,V_centeredNameLabel) centeredNameLabel;
```

## Class methods

```
+[TPSSubscriptionPickerCell cellStyle];
```

## Instance methods

```
-[TPSSubscriptionPickerCell badgeView];
-[TPSSubscriptionPickerCell nameLabel];
-[TPSSubscriptionPickerCell setBadgeView:];
-[TPSSubscriptionPickerCell initWithStyle:reuseIdentifier:];
-[TPSSubscriptionPickerCell refreshCellContentsWithSpecifier:];
-[TPSSubscriptionPickerCell setNameLabel:];
-[TPSSubscriptionPickerCell centeredBadgeView];
-[TPSSubscriptionPickerCell centeredNameLabel];
-[TPSSubscriptionPickerCell setCenteredBadgeView:];
-[TPSSubscriptionPickerCell setCenteredNameLabel:];
-[TPSSubscriptionPickerCell setNumberLabel:];
-[TPSSubscriptionPickerCell numberLabel];
-[TPSSubscriptionPickerCell _setBadge:andLabel:andPhoneNumber:];
-[TPSSubscriptionPickerCell _setCenteredBadge:andLabel:];
```
