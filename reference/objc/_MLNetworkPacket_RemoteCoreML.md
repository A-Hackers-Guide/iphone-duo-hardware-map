# `_MLNetworkPacket`

- Image: [`/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`](../userland/System__Library__PrivateFrameworks__RemoteCoreML.framework__RemoteCoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableData" _buffer;
@"NSMutableData" _doubleBuffer;
Q _sizeOfPacket;
Q _command;
```

## Properties

```
@property (T@"NSMutableData",&,N,V_buffer) buffer;
@property (T@"NSMutableData",&,N,V_doubleBuffer) doubleBuffer;
@property (TQ,N,V_sizeOfPacket) sizeOfPacket;
@property (TQ,N,V_command) command;
```

## Instance methods

```
-[_MLNetworkPacket buffer];
-[_MLNetworkPacket setBuffer:];
-[_MLNetworkPacket init];
-[_MLNetworkPacket command];
-[_MLNetworkPacket reset];
-[_MLNetworkPacket setCommand:];
-[_MLNetworkPacket resetMetadata];
-[_MLNetworkPacket setSizeOfPacket:];
-[_MLNetworkPacket sizeOfPacket];
-[_MLNetworkPacket cleanupDoubleBuffer];
-[_MLNetworkPacket doubleBuffer];
-[_MLNetworkPacket resetDoubleBuffer];
-[_MLNetworkPacket setDoubleBuffer:];
```
