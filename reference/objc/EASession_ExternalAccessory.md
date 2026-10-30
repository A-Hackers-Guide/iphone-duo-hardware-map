# `EASession`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"EAAccessory" _accessory;
I _sessionID;
@"NSString" _protocolString;
@"NSInputStream" _inputStream;
@"NSOutputStream" _outputStream;
B _openCompleted;
i _sock;
B _useSocketInterfaceForEASession;
@"NSString" _eaSessionUUIDFromCoreAccessories;
```

## Properties

```
@property (T@"EAAccessory",R,N,V_accessory) accessory;
@property (T@"NSString",R,N,V_protocolString) protocolString;
@property (T@"NSInputStream",R,N,V_inputStream) inputStream;
@property (T@"NSOutputStream",R,N,V_outputStream) outputStream;
```

## Instance methods

```
-[EASession _shortDescription];
-[EASession outputStream];
-[EASession init];
-[EASession dealloc];
-[EASession inputStream];
-[EASession description];
-[EASession accessory];
-[EASession _sessionID];
-[EASession protocolString];
-[EASession EASessionUUID];
-[EASession isOpenCompleted];
-[EASession _endStreams];
-[EASession _handleIncomingEAData:];
-[EASession _streamClosed];
-[EASession initWithAccessory:forProtocol:];
-[EASession setOpenCompleted:];
```
