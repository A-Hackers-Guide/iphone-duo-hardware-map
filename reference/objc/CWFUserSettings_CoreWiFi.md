# `CWFUserSettings`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 9 properties, 22 instance methods, 1 class methods

## Instance variables

```
q _syncMode;
q _askToJoinMode;
q _autoHotspotMode;
q _compatibilityMode;
@"NSDictionary" _OSSpecificAttributes;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N,V_syncMode) syncMode;
@property (Tq,N,V_askToJoinMode) askToJoinMode;
@property (Tq,N,V_autoHotspotMode) autoHotspotMode;
@property (Tq,N,V_compatibilityMode) compatibilityMode;
@property (T@"NSDictionary",C,N,V_OSSpecificAttributes) OSSpecificAttributes;
```

## Class methods

```
+[CWFUserSettings supportsSecureCoding];
```

## Instance methods

```
-[CWFUserSettings setAutoHotspotMode:];
-[CWFUserSettings askToJoinMode];
-[CWFUserSettings autoHotspotMode];
-[CWFUserSettings JSONCompatibleKeyValueMap];
-[CWFUserSettings setCompatibilityMode:];
-[CWFUserSettings setAskToJoinMode:];
-[CWFUserSettings descriptionForCompatibilityMode];
-[CWFUserSettings descriptionForAskToJoinMode];
-[CWFUserSettings setSyncMode:];
-[CWFUserSettings isEqualToUserSettings:];
-[CWFUserSettings compatibilityMode];
-[CWFUserSettings syncMode];
-[CWFUserSettings setOSSpecificAttributes:];
-[CWFUserSettings encodeWithCoder:];
-[CWFUserSettings hash];
-[CWFUserSettings descriptionForSyncMode];
-[CWFUserSettings description];
-[CWFUserSettings initWithCoder:];
-[CWFUserSettings OSSpecificAttributes];
-[CWFUserSettings descriptionForAutoHotspotMode];
-[CWFUserSettings copyWithZone:];
-[CWFUserSettings isEqual:];
```
