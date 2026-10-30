# `ASPickerDisplaySettings`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
d _discoveryTimeout;
Q _options;
```

## Properties

```
@property (Td,N,V_discoveryTimeout) discoveryTimeout;
@property (TQ,N,V_options) options;
```

## Class methods

```
+[ASPickerDisplaySettings supportsSecureCoding];
+[ASPickerDisplaySettings defaultSettings];
```

## Instance methods

```
-[ASPickerDisplaySettings encodeWithXPCObject:];
-[ASPickerDisplaySettings initWithXPCObject:error:];
-[ASPickerDisplaySettings descriptionWithLevel:];
-[ASPickerDisplaySettings setOptions:];
-[ASPickerDisplaySettings encodeWithCoder:];
-[ASPickerDisplaySettings description];
-[ASPickerDisplaySettings initWithCoder:];
-[ASPickerDisplaySettings options];
-[ASPickerDisplaySettings copyWithZone:];
-[ASPickerDisplaySettings isEqual:];
-[ASPickerDisplaySettings discoveryTimeout];
-[ASPickerDisplaySettings setDiscoveryTimeout:];
```
