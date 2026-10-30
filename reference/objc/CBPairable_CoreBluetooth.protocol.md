# `CBPairable` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N) dispatchQueue;
@property (T@?,C,N) pairingCompletedHandler;
@property (T@?,C,N) pairingPromptHandler;
```

## Instance methods

```
-[CBPairable dispatchQueue];
-[CBPairable setDispatchQueue:];
-[CBPairable pairingPromptHandler];
-[CBPairable setPairingPromptHandler:];
-[CBPairable pairingCompletedHandler];
-[CBPairable pairingPerformAction:completionHandler:];
-[CBPairable pairingPerformAction:withOptions:completionHandler:];
-[CBPairable setPairingCompletedHandler:];
```
