# `ACCUserNotification`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _allowLockScreenDismissal;
B _isModal;
B _dismissOnUnlock;
B _ignoreQuietMode;
B _presentViaSystemAperture;
i _type;
@"NSString" _uuid;
@"NSString" _title;
@"NSString" _message;
@"NSString" _lockScreenTitle;
@"NSString" _lockScreenMessage;
@"NSString" _defaultButtonName;
@"NSString" _alternateButtonName;
@"NSString" _otherButtonName;
@"NSDictionary" _iconConfiguration;
@"NSURL" _iconURL;
@"NSNumber" _systemSoundID;
d _timeout;
@"NSString" _identifier;
@"NSString" _groupIdentifier;
@"NSDictionary" _userNotificationCFDict;
^{__CFUserNotification=} _userNotificationCF;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_userNotificationCFDict) userNotificationCFDict;
@property (T^{__CFUserNotification=},N,V_userNotificationCF) userNotificationCF;
@property (T@"NSString",R,N,V_uuid) uuid;
@property (Ti,N,V_type) type;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_message) message;
@property (T@"NSString",C,N,V_lockScreenTitle) lockScreenTitle;
@property (T@"NSString",C,N,V_lockScreenMessage) lockScreenMessage;
@property (T@"NSString",C,N,V_defaultButtonName) defaultButtonName;
@property (T@"NSString",C,N,V_alternateButtonName) alternateButtonName;
@property (T@"NSString",C,N,V_otherButtonName) otherButtonName;
@property (T@"NSDictionary",C,N,V_iconConfiguration) iconConfiguration;
@property (T@"NSURL",C,N,V_iconURL) iconURL;
@property (TB,N,V_allowLockScreenDismissal) allowLockScreenDismissal;
@property (TB,N,V_isModal) isModal;
@property (TB,N,V_dismissOnUnlock) dismissOnUnlock;
@property (TB,N,V_ignoreQuietMode) ignoreQuietMode;
@property (TB,N,V_presentViaSystemAperture) presentViaSystemAperture;
@property (T@"NSNumber",&,N,V_systemSoundID) systemSoundID;
@property (Td,N,V_timeout) timeout;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_groupIdentifier) groupIdentifier;
```

## Instance methods

```
-[ACCUserNotification isModal];
-[ACCUserNotification setSystemSoundID:];
-[ACCUserNotification systemSoundID];
-[ACCUserNotification setMessage:];
-[ACCUserNotification groupIdentifier];
-[ACCUserNotification uuid];
-[ACCUserNotification identifier];
-[ACCUserNotification init];
-[ACCUserNotification message];
-[ACCUserNotification timeout];
-[ACCUserNotification setIconURL:];
-[ACCUserNotification setIdentifier:];
-[ACCUserNotification setType:];
-[ACCUserNotification setTimeout:];
-[ACCUserNotification type];
-[ACCUserNotification title];
-[ACCUserNotification iconURL];
-[ACCUserNotification allowLockScreenDismissal];
-[ACCUserNotification setTitle:];
-[ACCUserNotification setGroupIdentifier:];
-[ACCUserNotification setIsModal:];
-[ACCUserNotification setAllowLockScreenDismissal:];
-[ACCUserNotification dismissOnUnlock];
-[ACCUserNotification ignoreQuietMode];
-[ACCUserNotification otherButtonName];
-[ACCUserNotification lockScreenTitle];
-[ACCUserNotification alternateButtonName];
-[ACCUserNotification createBackingUserNotification];
-[ACCUserNotification defaultButtonName];
-[ACCUserNotification iconConfiguration];
-[ACCUserNotification lockScreenMessage];
-[ACCUserNotification presentViaSystemAperture];
-[ACCUserNotification setAlternateButtonName:];
-[ACCUserNotification setDefaultButtonName:];
-[ACCUserNotification setDismissOnUnlock:];
-[ACCUserNotification setIconConfiguration:];
-[ACCUserNotification setIgnoreQuietMode:];
-[ACCUserNotification setLockScreenMessage:];
-[ACCUserNotification setLockScreenTitle:];
-[ACCUserNotification setOtherButtonName:];
-[ACCUserNotification setPresentViaSystemAperture:];
-[ACCUserNotification setUserNotificationCF:];
-[ACCUserNotification setUserNotificationCFDict:];
-[ACCUserNotification updateBackingUserNotification];
-[ACCUserNotification userNotificationCF];
-[ACCUserNotification userNotificationCFDict];
```
