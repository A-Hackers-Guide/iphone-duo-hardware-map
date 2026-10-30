# `CWFHotspotFamilyMember`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
q _sharingMode;
@"NSString" _displayName;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",C,N,V_displayName) displayName;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Tq,N,V_sharingMode) sharingMode;
```

## Class methods

```
+[CWFHotspotFamilyMember supportsSecureCoding];
```

## Instance methods

```
-[CWFHotspotFamilyMember identifier];
-[CWFHotspotFamilyMember displayName];
-[CWFHotspotFamilyMember setDisplayName:];
-[CWFHotspotFamilyMember setIdentifier:];
-[CWFHotspotFamilyMember encodeWithCoder:];
-[CWFHotspotFamilyMember description];
-[CWFHotspotFamilyMember initWithCoder:];
-[CWFHotspotFamilyMember copyWithZone:];
-[CWFHotspotFamilyMember setSharingMode:];
-[CWFHotspotFamilyMember initWithDisplayName:identifier:sharingMode:];
-[CWFHotspotFamilyMember sharingMode];
```
