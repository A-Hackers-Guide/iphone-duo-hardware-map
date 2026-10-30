# `EAUSBBuffer`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
* _bufPtr;
Q _bufferLength;
i _usbError;
@"AccessoryEAInterface" _eaInterface;
* _readPtr;
* _writePtr;
Q _writeAttempts;
```

## Properties

```
@property (T@"AccessoryEAInterface",W,N,V_eaInterface) eaInterface;
@property (Ti,V_usbError) usbError;
@property (T*,R,N,V_readPtr) readPtr;
@property (T*,R,N,V_writePtr) writePtr;
@property (TQ,R,N,V_writeAttempts) writeAttempts;
@property (TQ,R,N) dataLength;
@property (TQ,R,N) writeSpaceRemaining;
```

## Instance methods

```
-[EAUSBBuffer dealloc];
-[EAUSBBuffer reset];
-[EAUSBBuffer dataLength];
-[EAUSBBuffer setEaInterface:];
-[EAUSBBuffer readPtr];
-[EAUSBBuffer attemptWrite];
-[EAUSBBuffer eaInterface];
-[EAUSBBuffer initWithSession:bufferSize:];
-[EAUSBBuffer moveReadPtr:];
-[EAUSBBuffer moveWritePtr:];
-[EAUSBBuffer setUsbError:];
-[EAUSBBuffer usbError];
-[EAUSBBuffer writeAttempts];
-[EAUSBBuffer writePtr];
-[EAUSBBuffer writeSpaceRemaining];
```
