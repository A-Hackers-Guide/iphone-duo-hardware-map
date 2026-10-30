# `BKAccessoryGroup`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
I _type;
@"NSUUID" _uuid;
@"NSString" _name;
@"BKDevice" _device;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"BKDevice",R,N,V_device) device;
```

## Instance methods

```
-[BKAccessoryGroup device];
-[BKAccessoryGroup hash];
-[BKAccessoryGroup isEqual:];
-[BKAccessoryGroup name];
-[BKAccessoryGroup accessoriesWithError:];
-[BKAccessoryGroup connectedAccessoriesWithError:];
-[BKAccessoryGroup initWithServerAccessoryGroup:device:];
-[BKAccessoryGroup isEqualToAccessoryGroup:];
-[BKAccessoryGroup isEqualToServerAccessoryGroup:];
-[BKAccessoryGroup serverAccessoryGroup];
```
