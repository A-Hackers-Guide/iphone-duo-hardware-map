# `CWFEventID`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
q _type;
@"NSString" _interfaceName;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
```

## Class methods

```
+[CWFEventID supportsSecureCoding];
+[CWFEventID eventIDWithType:interfaceName:];
```

## Instance methods

```
-[CWFEventID isEqualToEventID:];
-[CWFEventID setInterfaceName:];
-[CWFEventID interfaceName];
-[CWFEventID setType:];
-[CWFEventID type];
-[CWFEventID encodeWithCoder:];
-[CWFEventID hash];
-[CWFEventID description];
-[CWFEventID initWithCoder:];
-[CWFEventID copyWithZone:];
-[CWFEventID isEqual:];
```
