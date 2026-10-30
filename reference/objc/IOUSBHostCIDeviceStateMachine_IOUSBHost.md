# `IOUSBHostCIDeviceStateMachine`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _deviceState;
Q _completeRoute;
Q _deviceAddress;
@"IOUSBHostControllerInterface" _controllerInterface;
```

## Properties

```
@property (Ti,N,V_deviceState) deviceState;
@property (TQ,N,V_completeRoute) completeRoute;
@property (TQ,N,V_deviceAddress) deviceAddress;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
```

## Instance methods

```
-[IOUSBHostCIDeviceStateMachine deviceState];
-[IOUSBHostCIDeviceStateMachine setDeviceState:];
-[IOUSBHostCIDeviceStateMachine description];
-[IOUSBHostCIDeviceStateMachine deviceAddress];
-[IOUSBHostCIDeviceStateMachine setDeviceAddress:];
-[IOUSBHostCIDeviceStateMachine completeRoute];
-[IOUSBHostCIDeviceStateMachine controllerInterface];
-[IOUSBHostCIDeviceStateMachine initWithInterface:command:error:];
-[IOUSBHostCIDeviceStateMachine inspectCommand:error:];
-[IOUSBHostCIDeviceStateMachine processCommand:readonly:error:];
-[IOUSBHostCIDeviceStateMachine respondToCommand:status:deviceAddress:error:];
-[IOUSBHostCIDeviceStateMachine respondToCommand:status:error:];
-[IOUSBHostCIDeviceStateMachine setCompleteRoute:];
-[IOUSBHostCIDeviceStateMachine setControllerInterface:];
```
