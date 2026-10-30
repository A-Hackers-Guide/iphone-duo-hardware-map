# `IOUSBHostCIControllerStateMachine`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
i _controllerState;
@"IOUSBHostControllerInterface" _controllerInterface;
Q _lastFrameNumber;
Q _lastFrameTimestamp;
```

## Properties

```
@property (Ti,N,V_controllerState) controllerState;
@property (T@"IOUSBHostControllerInterface",&,N,V_controllerInterface) controllerInterface;
@property (TQ,N,V_lastFrameNumber) lastFrameNumber;
@property (TQ,N,V_lastFrameTimestamp) lastFrameTimestamp;
```

## Instance methods

```
-[IOUSBHostCIControllerStateMachine description];
-[IOUSBHostCIControllerStateMachine setControllerState:];
-[IOUSBHostCIControllerStateMachine controllerState];
-[IOUSBHostCIControllerStateMachine lastFrameNumber];
-[IOUSBHostCIControllerStateMachine controllerInterface];
-[IOUSBHostCIControllerStateMachine enqueueUpdatedFrame:timestamp:error:];
-[IOUSBHostCIControllerStateMachine initWithInterface:error:];
-[IOUSBHostCIControllerStateMachine inspectCommand:error:];
-[IOUSBHostCIControllerStateMachine lastFrameTimestamp];
-[IOUSBHostCIControllerStateMachine processCommand:readonly:error:];
-[IOUSBHostCIControllerStateMachine respondToCommand:status:error:];
-[IOUSBHostCIControllerStateMachine respondToCommand:status:frame:timestamp:error:];
-[IOUSBHostCIControllerStateMachine setControllerInterface:];
-[IOUSBHostCIControllerStateMachine setLastFrameNumber:];
-[IOUSBHostCIControllerStateMachine setLastFrameTimestamp:];
```
