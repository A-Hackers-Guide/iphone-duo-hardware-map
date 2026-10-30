# `BTBannerUISession`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 22 properties, 55 instance methods, 0 class methods

## Instance variables

```
B _bannerRunning;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSObject<OS_xpc_object>" _xpcConnection;
i _backgroundColor;
I _bannerType;
I _leadingAccessoryImagePID;
@? _actionHandler;
@"NSString" _bannerAppID;
@"NSString" _centerContentText;
@"NSString" _centerContentItemsIcon;
@"NSString" _centerContentItemsText;
@"NSString" _identifier;
@"NSString" _label;
@"NSString" _leadingAccessoryImageName;
@"NSString" _leadingAccessoryImagePath;
d _timeoutSeconds;
@"NSString" _trailingAccessoryImageName;
@"NSString" _trailingAccessoryImagePath;
@"NSString" _trailingAccessoryText;
d _lowBatteryLevel;
d _batteryLevelInfo;
@"NSString" _feedbackDeviceContext;
@"NSString" _feedbackFormIdentifier;
@"NSString" _subformType;
```

## Properties

```
@property (T@?,C,N,V_actionHandler) actionHandler;
@property (Ti,N,V_backgroundColor) backgroundColor;
@property (T@"NSString",C,N,V_bannerAppID) bannerAppID;
@property (TI,N,V_bannerType) bannerType;
@property (T@"NSString",C,N,V_centerContentText) centerContentText;
@property (T@"NSString",C,N,V_centerContentItemsIcon) centerContentItemsIcon;
@property (T@"NSString",C,N,V_centerContentItemsText) centerContentItemsText;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_label) label;
@property (T@"NSString",C,N,V_leadingAccessoryImageName) leadingAccessoryImageName;
@property (T@"NSString",C,N,V_leadingAccessoryImagePath) leadingAccessoryImagePath;
@property (TI,N,V_leadingAccessoryImagePID) leadingAccessoryImagePID;
@property (Td,N,V_timeoutSeconds) timeoutSeconds;
@property (T@"NSString",C,N,V_trailingAccessoryImageName) trailingAccessoryImageName;
@property (T@"NSString",C,N,V_trailingAccessoryImagePath) trailingAccessoryImagePath;
@property (T@"NSString",C,N,V_trailingAccessoryText) trailingAccessoryText;
@property (Td,N,V_lowBatteryLevel) lowBatteryLevel;
@property (Td,N,V_batteryLevelInfo) batteryLevelInfo;
@property (T@"NSString",C,N,V_feedbackDeviceContext) feedbackDeviceContext;
@property (T@"NSString",C,N,V_feedbackFormIdentifier) feedbackFormIdentifier;
@property (T@"NSString",C,N,V_subformType) subformType;
```

## Instance methods

```
-[BTBannerUISession encodeWithXPCObject:];
-[BTBannerUISession dispatchQueue];
-[BTBannerUISession _activate];
-[BTBannerUISession identifier];
-[BTBannerUISession init];
-[BTBannerUISession label];
-[BTBannerUISession setLabel:];
-[BTBannerUISession setActionHandler:];
-[BTBannerUISession setDispatchQueue:];
-[BTBannerUISession setBackgroundColor:];
-[BTBannerUISession actionHandler];
-[BTBannerUISession invalidate];
-[BTBannerUISession setIdentifier:];
-[BTBannerUISession activate];
-[BTBannerUISession backgroundColor];
-[BTBannerUISession _xpcSendReplyError:request:];
-[BTBannerUISession timeoutSeconds];
-[BTBannerUISession setTimeoutSeconds:];
-[BTBannerUISession lowBatteryLevel];
-[BTBannerUISession bannerType];
-[BTBannerUISession setBannerType:];
-[BTBannerUISession setTrailingAccessoryText:];
-[BTBannerUISession trailingAccessoryText];
-[BTBannerUISession _xpcSendMessage];
-[BTBannerUISession setBannerAppID:];
-[BTBannerUISession setSubformType:];
-[BTBannerUISession _xpcCompleted:];
-[BTBannerUISession _xpcConnectionMessage:];
-[BTBannerUISession _xpcEvent:];
-[BTBannerUISession _xpcStart];
-[BTBannerUISession bannerAppID];
-[BTBannerUISession batteryLevelInfo];
-[BTBannerUISession centerContentItemsIcon];
-[BTBannerUISession centerContentItemsText];
-[BTBannerUISession centerContentText];
-[BTBannerUISession feedbackDeviceContext];
-[BTBannerUISession feedbackFormIdentifier];
-[BTBannerUISession leadingAccessoryImageName];
-[BTBannerUISession leadingAccessoryImagePID];
-[BTBannerUISession leadingAccessoryImagePath];
-[BTBannerUISession setBatteryLevelInfo:];
-[BTBannerUISession setCenterContentItemsIcon:];
-[BTBannerUISession setCenterContentItemsText:];
-[BTBannerUISession setCenterContentText:];
-[BTBannerUISession setFeedbackDeviceContext:];
-[BTBannerUISession setFeedbackFormIdentifier:];
-[BTBannerUISession setLeadingAccessoryImageName:];
-[BTBannerUISession setLeadingAccessoryImagePID:];
-[BTBannerUISession setLeadingAccessoryImagePath:];
-[BTBannerUISession setLowBatteryLevel:];
-[BTBannerUISession setTrailingAccessoryImageName:];
-[BTBannerUISession setTrailingAccessoryImagePath:];
-[BTBannerUISession subformType];
-[BTBannerUISession trailingAccessoryImageName];
-[BTBannerUISession trailingAccessoryImagePath];
```
