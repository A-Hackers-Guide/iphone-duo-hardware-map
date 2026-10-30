# `CTQuickSwitchInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 5 instance methods, 2 class methods

## Instance variables

```
{QuickSwitchInfo="fMode"C"fLastTransitionTimestamp"Q"previousTransitionTimestamp"Q"fLastSuccessfulActiveIccidTimestampsMs"{map<std::string, unsigned long long, std::less<std::string>, std::allocator<std::pair<const std::string, unsigned long long>>>="__tree_"{__tree<std::__value_type<std::string, unsigned long long>, std::__map_value_compare<std::string, std::pair<const std::string, unsigned long long>, std::less<std::string>>, std::allocator<std::pair<const std::string, unsigned long long>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}}} _internalInfo;
```

## Properties

```
@property (Tq,R) mode;
```

## Class methods

```
+[CTQuickSwitchInfo supportsSecureCoding];
+[CTQuickSwitchInfo quickSwitchInfoWithInternalInfo:];
```

## Instance methods

```
-[CTQuickSwitchInfo encodeWithCoder:];
-[CTQuickSwitchInfo mode];
-[CTQuickSwitchInfo description];
-[CTQuickSwitchInfo initWithInternalInfo:];
-[CTQuickSwitchInfo initWithCoder:];
```
