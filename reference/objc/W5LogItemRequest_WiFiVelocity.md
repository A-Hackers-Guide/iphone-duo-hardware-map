# `W5LogItemRequest`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" _uuid;
q _itemID;
@"NSDictionary" _configuration;
```

## Properties

```
@property (T@"NSUUID",C,N,V_uuid) uuid;
@property (Tq,N,V_itemID) itemID;
@property (T@"NSDictionary",C,N,V_configuration) configuration;
```

## Class methods

```
+[W5LogItemRequest supportsSecureCoding];
+[W5LogItemRequest requestWithItemID:configuration:];
```

## Instance methods

```
-[W5LogItemRequest setItemID:];
-[W5LogItemRequest uuid];
-[W5LogItemRequest init];
-[W5LogItemRequest dealloc];
-[W5LogItemRequest setUuid:];
-[W5LogItemRequest setConfiguration:];
-[W5LogItemRequest configuration];
-[W5LogItemRequest encodeWithCoder:];
-[W5LogItemRequest conformsToProtocol:];
-[W5LogItemRequest hash];
-[W5LogItemRequest description];
-[W5LogItemRequest initWithCoder:];
-[W5LogItemRequest copyWithZone:];
-[W5LogItemRequest isEqual:];
-[W5LogItemRequest itemID];
-[W5LogItemRequest isEqualToLogItemRequest:];
```
