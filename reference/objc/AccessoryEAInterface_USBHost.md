# `AccessoryEAInterface`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `iAP2EASession`
- 26 instance variables, 5 properties, 36 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _writeBufferArray;
@"NSMutableArray" _readBufferArray;
@"NSMutableArray" _dataForAppArray;
@"NSMutableArray" _allReadBuffers;
@"NSMutableArray" _allWriteBuffers;
^{__CFSocket=} _listenSockRef;
^{__CFRunLoopSource=} _listenSockRls;
^{__CFSocket=} _sockRef;
^{__CFRunLoopSource=} _sockRls;
B _sockReadDisabled;
Q _deviceID;
@"NSString" _protocolName;
^^{IOUSBInterfaceStruct942} _usbInterface;
^{__CFRunLoopSource=} _usbRls;
C _inPipe;
C _outPipe;
S _maxInSize;
S _maxOutSize;
I _interfaceSpeed;
@"NSThread" _runLoopThread;
@"NSRunLoop" _runLoop;
S _vid;
S _pid;
I _vidpid;
Q _registryEntryID;
@? _dataInHandler;
```

## Properties

```
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (T@?,C,N,V_dataInHandler) dataInHandler;
@property (TS,R,N,V_vid) vid;
@property (TS,R,N,V_pid) pid;
@property (TI,R,N,V_vidpid) vidpid;
```

## Class methods

```
+[AccessoryEAInterface findNativeEAInterfacesForRegistryID:];
+[AccessoryEAInterface initializeSessionClose];
```

## Instance methods

```
-[AccessoryEAInterface _run];
-[AccessoryEAInterface dealloc];
-[AccessoryEAInterface pid];
-[AccessoryEAInterface writeData:];
-[AccessoryEAInterface _writeData:];
-[AccessoryEAInterface vid];
-[AccessoryEAInterface registryEntryID];
-[AccessoryEAInterface _writeSocketCB:];
-[AccessoryEAInterface _acceptSocketCB:acceptedSock:];
-[AccessoryEAInterface _cancelThread];
-[AccessoryEAInterface _clearPipeStall:];
-[AccessoryEAInterface _createInterfaceFromUSBID:];
-[AccessoryEAInterface _dequeueReadBuffer];
-[AccessoryEAInterface _dequeueWriteBuffer];
-[AccessoryEAInterface _enqueueReadBuffer:];
-[AccessoryEAInterface _enqueueWriteBuffer:];
-[AccessoryEAInterface _openPipeFromApp];
-[AccessoryEAInterface _openPipeFromAppOnThread];
-[AccessoryEAInterface _openPipeToApp];
-[AccessoryEAInterface _openPipeToAppOnThread];
-[AccessoryEAInterface _readComplete:readLength:];
-[AccessoryEAInterface _readSessionDataFromApp];
-[AccessoryEAInterface _readSessionDataFromUSB];
-[AccessoryEAInterface _readSocketCB:];
-[AccessoryEAInterface _registerListenSocket];
-[AccessoryEAInterface _sendSessionCloseNotification];
-[AccessoryEAInterface _sendSessionOpenNotification];
-[AccessoryEAInterface _writeComplete:writeLength:];
-[AccessoryEAInterface _writeSessionDataToApp];
-[AccessoryEAInterface _writeUSBData:];
-[AccessoryEAInterface closeDataPipes];
-[AccessoryEAInterface dataInHandler];
-[AccessoryEAInterface initWithProtocol:endpointUUID:vid:pid:eaSessionUUID:USBDeviceID:];
-[AccessoryEAInterface setDataInHandler:];
-[AccessoryEAInterface shuttingDownSession];
-[AccessoryEAInterface vidpid];
```
