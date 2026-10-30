# `CKKSCurrentItemQuery`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _accessGroup;
@"NSString" _zoneID;
```

## Properties

```
@property (T@"NSString",&,V_identifier) identifier;
@property (T@"NSString",&,V_accessGroup) accessGroup;
@property (T@"NSString",&,V_zoneID) zoneID;
```

## Class methods

```
+[CKKSCurrentItemQuery supportsSecureCoding];
```

## Instance methods

```
-[CKKSCurrentItemQuery setZoneID:];
-[CKKSCurrentItemQuery setAccessGroup:];
-[CKKSCurrentItemQuery identifier];
-[CKKSCurrentItemQuery accessGroup];
-[CKKSCurrentItemQuery zoneID];
-[CKKSCurrentItemQuery setIdentifier:];
-[CKKSCurrentItemQuery encodeWithCoder:];
-[CKKSCurrentItemQuery description];
-[CKKSCurrentItemQuery initWithCoder:];
-[CKKSCurrentItemQuery initWithIdentifier:accessGroup:zoneID:];
```
