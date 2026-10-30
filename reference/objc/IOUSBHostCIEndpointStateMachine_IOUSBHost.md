# `IOUSBHostCIEndpointStateMachine`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
i _endpointState;
i _endpointType;
Q _deviceAddress;
Q _endpointAddress;
r^{IOUSBHostCIMessage=IIQ} _currentTransferMessage;
@"IOUSBHostControllerInterface" _controllerInterface;
```

## Properties

```
@property (Ti,N,V_endpointState) endpointState;
@property (TQ,N,V_deviceAddress) deviceAddress;
@property (TQ,N,V_endpointAddress) endpointAddress;
@property (Tr^{IOUSBHostCIMessage=IIQ},N,V_currentTransferMessage) currentTransferMessage;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (Ti,N,V_endpointType) endpointType;
```

## Instance methods

```
-[IOUSBHostCIEndpointStateMachine endpointType];
-[IOUSBHostCIEndpointStateMachine setEndpointState:];
-[IOUSBHostCIEndpointStateMachine endpointState];
-[IOUSBHostCIEndpointStateMachine setEndpointType:];
-[IOUSBHostCIEndpointStateMachine description];
-[IOUSBHostCIEndpointStateMachine deviceAddress];
-[IOUSBHostCIEndpointStateMachine setDeviceAddress:];
-[IOUSBHostCIEndpointStateMachine endpointAddress];
-[IOUSBHostCIEndpointStateMachine controllerInterface];
-[IOUSBHostCIEndpointStateMachine currentTransferMessage];
-[IOUSBHostCIEndpointStateMachine enqueueTransferCompletionForMessage:status:transferLength:error:];
-[IOUSBHostCIEndpointStateMachine initWithInterface:command:error:];
-[IOUSBHostCIEndpointStateMachine inspectCommand:error:];
-[IOUSBHostCIEndpointStateMachine processCommand:readonly:error:];
-[IOUSBHostCIEndpointStateMachine processDoorbell:error:];
-[IOUSBHostCIEndpointStateMachine respondToCommand:status:error:];
-[IOUSBHostCIEndpointStateMachine setControllerInterface:];
-[IOUSBHostCIEndpointStateMachine setCurrentTransferMessage:];
-[IOUSBHostCIEndpointStateMachine setEndpointAddress:];
```
