# `ASMPolarisResourceProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessorySensorManagerDarwin_Private.framework/AccessorySensorManagerDarwin_Private`](../userland/System__Library__PrivateFrameworks__AccessorySensorManagerDarwin_Private.framework__AccessorySensorManagerDarwin_Private.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _activateCalled;
@"NSMutableSet" _currentResourceKeys;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _resourceStartHandler;
@? _resourceStopHandler;
```

## Properties

```
@property (T@?,C,N,V_resourceStartHandler) resourceStartHandler;
@property (T@?,C,N,V_resourceStopHandler) resourceStopHandler;
```

## Instance methods

```
-[ASMPolarisResourceProvider init];
-[ASMPolarisResourceProvider invalidate];
-[ASMPolarisResourceProvider _activateWithExecutionSession:];
-[ASMPolarisResourceProvider activateWithExecutionSession:];
-[ASMPolarisResourceProvider resourceStartHandler];
-[ASMPolarisResourceProvider resourceStopHandler];
-[ASMPolarisResourceProvider setResourceStartHandler:];
-[ASMPolarisResourceProvider setResourceStopHandler:];
```
