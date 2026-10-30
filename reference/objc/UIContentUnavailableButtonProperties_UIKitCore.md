# `UIContentUnavailableButtonProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedEnabled"b1"hasCustomizedRole"b1"hasCustomizedMinimumSize"b1} _buttonFlags;
B _enabled;
@"UIButtonConfiguration" _configuration;
@"UIAction" _primaryAction;
@"UIMenu" _menu;
q _role;
@"UIButtonConfiguration" _defaultConfiguration;
{CGSize="width"d"height"d} _minimumSize;
```

## Properties

```
@property (T@"UIButtonConfiguration",&,N) configuration;
@property (T{CGSize=dd},N) minimumSize;
@property (T@"UIAction",C,N) primaryAction;
@property (T@"UIMenu",C,N) menu;
@property (TB,N,GisEnabled) enabled;
@property (Tq,N) role;
```

## Class methods

```
+[UIContentUnavailableButtonProperties supportsSecureCoding];
```

## Instance methods

```
-[UIContentUnavailableButtonProperties menu];
-[UIContentUnavailableButtonProperties primaryAction];
-[UIContentUnavailableButtonProperties setMinimumSize:];
-[UIContentUnavailableButtonProperties minimumSize];
-[UIContentUnavailableButtonProperties init];
-[UIContentUnavailableButtonProperties setConfiguration:];
-[UIContentUnavailableButtonProperties isEnabled];
-[UIContentUnavailableButtonProperties configuration];
-[UIContentUnavailableButtonProperties setEnabled:];
-[UIContentUnavailableButtonProperties setPrimaryAction:];
-[UIContentUnavailableButtonProperties encodeWithCoder:];
-[UIContentUnavailableButtonProperties role];
-[UIContentUnavailableButtonProperties hash];
-[UIContentUnavailableButtonProperties setRole:];
-[UIContentUnavailableButtonProperties description];
-[UIContentUnavailableButtonProperties initWithCoder:];
-[UIContentUnavailableButtonProperties copyWithZone:];
-[UIContentUnavailableButtonProperties isEqual:];
-[UIContentUnavailableButtonProperties setMenu:];
```
