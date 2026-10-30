# `CBCoordinatedSetInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
C _setSize;
@"NSString" _setName;
@"NSMutableArray" _connectedIdentifiers;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_connectedIdentifiers) connectedIdentifiers;
@property (T@"NSString",&,N,V_setName) setName;
@property (TC,N,V_setSize) setSize;
```

## Instance methods

```
-[CBCoordinatedSetInfo copyWithZone:];
-[CBCoordinatedSetInfo connectedIdentifiers];
-[CBCoordinatedSetInfo setName];
-[CBCoordinatedSetInfo setSize];
-[CBCoordinatedSetInfo initWithInfo:withSize:];
-[CBCoordinatedSetInfo setConnectedIdentifiers:];
-[CBCoordinatedSetInfo setSetName:];
-[CBCoordinatedSetInfo setSetSize:];
```
