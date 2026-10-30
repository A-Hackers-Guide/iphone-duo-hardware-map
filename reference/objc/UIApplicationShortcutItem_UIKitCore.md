# `UIApplicationShortcutItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSMutableCopying`
- 7 instance variables, 13 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"NSString" _type;
@"NSString" _localizedTitle;
@"NSString" _localizedSubtitle;
@"UIApplicationShortcutIcon" _icon;
@ _targetContentIdentifier;
@"NSData" _userInfoData;
Q _activationMode;
```

## Properties

```
@property (T@"SBSApplicationShortcutItem",R,C,N) sbsShortcutItem;
@property (T@"NSString",C,N,V_type) type;
@property (T@"NSString",C,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",C,N,V_localizedSubtitle) localizedSubtitle;
@property (T@"UIApplicationShortcutIcon",C,N,V_icon) icon;
@property (T@"NSDictionary",C,N) userInfo;
@property (T@"NSData",C,N,V_userInfoData) userInfoData;
@property (T@,C,N,V_targetContentIdentifier) targetContentIdentifier;
@property (TQ,R,N,V_activationMode) activationMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIApplicationShortcutItem _sbsActivationModeFromUIActivationMode:];
+[UIApplicationShortcutItem _uiActivationModeFromSBSActivationMode:];
```

## Instance methods

```
-[UIApplicationShortcutItem localizedTitle];
-[UIApplicationShortcutItem targetContentIdentifier];
-[UIApplicationShortcutItem setTargetContentIdentifier:];
-[UIApplicationShortcutItem mutableCopyWithZone:];
-[UIApplicationShortcutItem init];
-[UIApplicationShortcutItem initWithXPCDictionary:];
-[UIApplicationShortcutItem userInfo];
-[UIApplicationShortcutItem setIcon:];
-[UIApplicationShortcutItem setUserInfo:];
-[UIApplicationShortcutItem userInfoData];
-[UIApplicationShortcutItem setType:];
-[UIApplicationShortcutItem setUserInfoData:];
-[UIApplicationShortcutItem type];
-[UIApplicationShortcutItem encodeWithXPCDictionary:];
-[UIApplicationShortcutItem activationMode];
-[UIApplicationShortcutItem hash];
-[UIApplicationShortcutItem setLocalizedTitle:];
-[UIApplicationShortcutItem description];
-[UIApplicationShortcutItem copyWithZone:];
-[UIApplicationShortcutItem setLocalizedSubtitle:];
-[UIApplicationShortcutItem isEqual:];
-[UIApplicationShortcutItem localizedSubtitle];
-[UIApplicationShortcutItem icon];
-[UIApplicationShortcutItem sbsShortcutItem];
-[UIApplicationShortcutItem _initWithType:localizedTitle:localizedSubtitle:icon:userInfoData:activationMode:targetContentIdentifier:];
-[UIApplicationShortcutItem initWithSBSApplicationShortcutItem:];
-[UIApplicationShortcutItem initWithType:localizedTitle:];
-[UIApplicationShortcutItem initWithType:localizedTitle:localizedSubtitle:icon:userInfo:];
```
