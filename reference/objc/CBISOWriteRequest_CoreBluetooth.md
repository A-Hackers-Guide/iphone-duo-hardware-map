# `CBISOWriteRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
S _packetSequenceNumber;
@? _completionHandler;
@"NSData" _data;
@"NSError" _error;
@"<CBStackISOStream>" _stream;
```

## Properties

```
@property (T@"NSError",C,N,V_error) error;
@property (T@"<CBStackISOStream>",&,N,V_stream) stream;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"NSData",&,N,V_data) data;
@property (TS,N,V_packetSequenceNumber) packetSequenceNumber;
```

## Instance methods

```
-[CBISOWriteRequest stream];
-[CBISOWriteRequest setError:];
-[CBISOWriteRequest setCompletionHandler:];
-[CBISOWriteRequest completionHandler];
-[CBISOWriteRequest data];
-[CBISOWriteRequest setStream:];
-[CBISOWriteRequest error];
-[CBISOWriteRequest setData:];
-[CBISOWriteRequest packetSequenceNumber];
-[CBISOWriteRequest setPacketSequenceNumber:];
```
