# `BKAccessory`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
I _type;
@"NSUUID" _uuid;
I _flags;
@"NSString" _name;
@"BKAccessoryGroup" _accessoryGroup;
@"BKDevice" _device;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (TB,R,N) isRemovable;
@property (T@"NSData",R,C,N) uid;
@property (T@"BKAccessoryGroup",R,N,V_accessoryGroup) accessoryGroup;
@property (T@"BKDevice",R,N,V_device) device;
```

## Instance methods

```
-[BKAccessory device];
-[BKAccessory hash];
-[BKAccessory uid];
-[BKAccessory isEqual:];
-[BKAccessory name];
-[BKAccessory isRemovable];
-[BKAccessory serverAccessory];
-[BKAccessory initWithServerAccessory:device:];
-[BKAccessory accessoryGroup];
-[BKAccessory isAuthorized:error:];
-[BKAccessory isConnected:error:];
-[BKAccessory isEqualToAccessory:];
-[BKAccessory isEqualToServerAccessory:];
```
