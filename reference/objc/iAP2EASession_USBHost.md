# `iAP2EASession`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _endpointUUID;
@"NSString" _eaSessionUUID;
i _listenSock;
i _sock;
B _openPipeToAppAfterAccept;
B _openPipeFromAppAfterAccept;
B _isWirelessSession;
```

## Instance methods

```
-[iAP2EASession init];
-[iAP2EASession dealloc];
-[iAP2EASession description];
-[iAP2EASession openPipeFromApp];
-[iAP2EASession _createListenSocket];
-[iAP2EASession _openPipeFromApp];
-[iAP2EASession _openPipeToApp];
-[iAP2EASession closeDataPipes];
-[iAP2EASession initWithProtocol:endpointUUID:eaSessionUUID:];
-[iAP2EASession openPipeToApp];
-[iAP2EASession shuttingDownSession];
```
