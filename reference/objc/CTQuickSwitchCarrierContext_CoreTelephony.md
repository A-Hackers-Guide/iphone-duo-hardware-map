# `CTQuickSwitchCarrierContext`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 6 properties, 10 instance methods, 2 class methods

## Instance variables

```
{QuickSwitchCarrierContext="role"C"carrierLifecycleState"C"slot"i"smsForkingMechanism"C"companionInfos"{map<std::string, QuickSwitchCompanionInfo, std::less<std::string>, std::allocator<std::pair<const std::string, QuickSwitchCompanionInfo>>>="__tree_"{__tree<std::__value_type<std::string, QuickSwitchCompanionInfo>, std::__map_value_compare<std::string, std::pair<const std::string, QuickSwitchCompanionInfo>, std::less<std::string>>, std::allocator<std::pair<const std::string, QuickSwitchCompanionInfo>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}}"supportType"C"mdn"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"formattedMdn"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"carrierName"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"enrollmentTimestamp"{optional<double>=""(?="__null_state_"c"__val_"d)"__engaged_"B}} _internalContext;
```

## Properties

```
@property (TQ,R) role;
@property (TQ,R) lifecycleState;
@property (TQ,R) smsForkingMechanism;
@property (TQ,R) supportType;
@property (T@"NSString",R) formattedMdn;
@property (T@"NSString",R) carrierName;
```

## Class methods

```
+[CTQuickSwitchCarrierContext supportsSecureCoding];
+[CTQuickSwitchCarrierContext quickSwitchCarrierContextWithInternalContext:];
```

## Instance methods

```
-[CTQuickSwitchCarrierContext lifecycleState];
-[CTQuickSwitchCarrierContext carrierName];
-[CTQuickSwitchCarrierContext encodeWithCoder:];
-[CTQuickSwitchCarrierContext role];
-[CTQuickSwitchCarrierContext description];
-[CTQuickSwitchCarrierContext initWithCoder:];
-[CTQuickSwitchCarrierContext formattedMdn];
-[CTQuickSwitchCarrierContext initWithInternalContext:];
-[CTQuickSwitchCarrierContext smsForkingMechanism];
-[CTQuickSwitchCarrierContext supportType];
```
