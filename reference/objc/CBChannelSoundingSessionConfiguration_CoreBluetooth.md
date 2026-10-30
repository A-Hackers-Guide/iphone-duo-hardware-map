# `CBChannelSoundingSessionConfiguration`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
C _configId;
B _returnTonesData;
S _procedureOptions;
q _role;
```

## Properties

```
@property (TS,N,V_procedureOptions) procedureOptions;
@property (TC,N,V_configId) configId;
@property (TB,R,N,V_returnTonesData) returnTonesData;
@property (Tq,R,N,V_role) role;
```

## Instance methods

```
-[CBChannelSoundingSessionConfiguration role];
-[CBChannelSoundingSessionConfiguration initWithRole:];
-[CBChannelSoundingSessionConfiguration returnTonesData];
-[CBChannelSoundingSessionConfiguration configId];
-[CBChannelSoundingSessionConfiguration initWithReturnTonesData:];
-[CBChannelSoundingSessionConfiguration procedureOptions];
-[CBChannelSoundingSessionConfiguration setConfigId:];
-[CBChannelSoundingSessionConfiguration setProcedureOptions:];
```
