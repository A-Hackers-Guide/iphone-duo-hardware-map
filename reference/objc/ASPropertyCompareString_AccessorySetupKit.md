# `ASPropertyCompareString`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _string;
Q _compareOptions;
```

## Properties

```
@property (T@"NSString",R,C,N,V_string) string;
@property (TQ,R,N,V_compareOptions) compareOptions;
```

## Class methods

```
+[ASPropertyCompareString supportsSecureCoding];
```

## Instance methods

```
-[ASPropertyCompareString encodeWithXPCObject:];
-[ASPropertyCompareString initWithXPCObject:error:];
-[ASPropertyCompareString descriptionWithLevel:];
-[ASPropertyCompareString string];
-[ASPropertyCompareString encodeWithCoder:];
-[ASPropertyCompareString hash];
-[ASPropertyCompareString description];
-[ASPropertyCompareString initWithCoder:];
-[ASPropertyCompareString copyWithZone:];
-[ASPropertyCompareString isEqual:];
-[ASPropertyCompareString initWithString:compareOptions:];
-[ASPropertyCompareString compareOptions];
```
