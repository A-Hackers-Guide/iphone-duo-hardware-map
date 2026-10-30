# `CTQuickSwitchClientData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
{QuickSwitchClientData="fDeviceId"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"fVersion"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"fPayload"{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}}"fSelfDevice"B"fUpdateTimestamp"Q} _internalInfo;
```

## Properties

```
@property (T@"NSString",R,N) deviceId;
@property (T@"NSString",R,N) version;
@property (T@"NSData",R,N) payload;
@property (TB,R,N) isSelfDevice;
@property (TQ,R,N) updateTimestamp;
```

## Class methods

```
+[CTQuickSwitchClientData supportsSecureCoding];
+[CTQuickSwitchClientData clientDataWithInternalInfo:];
```

## Instance methods

```
-[CTQuickSwitchClientData deviceId];
-[CTQuickSwitchClientData payload];
-[CTQuickSwitchClientData version];
-[CTQuickSwitchClientData encodeWithCoder:];
-[CTQuickSwitchClientData description];
-[CTQuickSwitchClientData initWithInternalInfo:];
-[CTQuickSwitchClientData initWithCoder:];
-[CTQuickSwitchClientData copyWithZone:];
-[CTQuickSwitchClientData updateTimestamp];
-[CTQuickSwitchClientData internalInfo];
-[CTQuickSwitchClientData isSelfDevice];
```
