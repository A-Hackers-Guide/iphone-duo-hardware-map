# `IOUSBHostCIPortStateMachine`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _powered;
B _connected;
B _overcurrent;
i _portState;
I _portStatus;
i _linkState;
i _speed;
Q _portNumber;
@"IOUSBHostControllerInterface" _controllerInterface;
```

## Properties

```
@property (TQ,N,V_portNumber) portNumber;
@property (Ti,N,V_portState) portState;
@property (TI,N,V_portStatus) portStatus;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (TB,N,V_powered) powered;
@property (TB,N,V_connected) connected;
@property (TB,N,V_overcurrent) overcurrent;
@property (Ti,R,N,V_linkState) linkState;
@property (Ti,R,N,V_speed) speed;
```

## Instance methods

```
-[IOUSBHostCIPortStateMachine connected];
-[IOUSBHostCIPortStateMachine setPortNumber:];
-[IOUSBHostCIPortStateMachine powered];
-[IOUSBHostCIPortStateMachine setConnected:];
-[IOUSBHostCIPortStateMachine setPowered:];
-[IOUSBHostCIPortStateMachine portNumber];
-[IOUSBHostCIPortStateMachine speed];
-[IOUSBHostCIPortStateMachine description];
-[IOUSBHostCIPortStateMachine linkState];
-[IOUSBHostCIPortStateMachine setOvercurrent:];
-[IOUSBHostCIPortStateMachine controllerInterface];
-[IOUSBHostCIPortStateMachine initWithInterface:portNumber:error:];
-[IOUSBHostCIPortStateMachine inspectCommand:error:];
-[IOUSBHostCIPortStateMachine overcurrent];
-[IOUSBHostCIPortStateMachine portState];
-[IOUSBHostCIPortStateMachine portStatus];
-[IOUSBHostCIPortStateMachine processCommand:readonly:commandResult:error:];
-[IOUSBHostCIPortStateMachine respondToCommand:status:error:];
-[IOUSBHostCIPortStateMachine setControllerInterface:];
-[IOUSBHostCIPortStateMachine setPortState:];
-[IOUSBHostCIPortStateMachine setPortStatus:];
-[IOUSBHostCIPortStateMachine updateLinkState:speed:inhibitLinkStateChange:error:];
```
