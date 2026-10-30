# `CBUUID`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 11 instance methods, 4 class methods

## Instance variables

```
[16C] _bytes;
c _type;
```

## Properties

```
@property (T@"NSData",R,N) data;
@property (T@"NSString",R,N) UUIDString;
```

## Class methods

```
+[CBUUID UUIDWithString:];
+[CBUUID UUIDWithNSUUID:];
+[CBUUID UUIDWithCFUUID:];
+[CBUUID UUIDWithData:];
```

## Instance methods

```
-[CBUUID initWithString:];
-[CBUUID UUIDString];
-[CBUUID data];
-[CBUUID initWithNSUUID:];
-[CBUUID initWithCFUUID:];
-[CBUUID hash];
-[CBUUID description];
-[CBUUID initWithString:safe:];
-[CBUUID initWithData:];
-[CBUUID copyWithZone:];
-[CBUUID isEqual:];
```
