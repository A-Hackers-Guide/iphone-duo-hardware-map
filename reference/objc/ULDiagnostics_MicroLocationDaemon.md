# `ULDiagnostics`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 25 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _providersLock;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSHashTable" _providers;
@"NSString" _label;
Q _stateHandle;
^v _cppProviders;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T{os_unfair_lock_s=I},N,V_providersLock) providersLock;
@property (T@"NSHashTable",&,N,V_providers) providers;
@property (T@"NSString",&,N,V_label) label;
@property (TQ,N,V_stateHandle) stateHandle;
@property (T^v,N,V_cppProviders) cppProviders;
```

## Instance methods

```
-[ULDiagnostics stateHandle];
-[ULDiagnostics initWithLabel:];
-[ULDiagnostics providers];
-[ULDiagnostics setProviders:];
-[ULDiagnostics _withLock:];
-[ULDiagnostics init];
-[ULDiagnostics label];
-[ULDiagnostics setLabel:];
-[ULDiagnostics dealloc];
-[ULDiagnostics queue];
-[ULDiagnostics removeProvider:];
-[ULDiagnostics addProvider:];
-[ULDiagnostics _registerStateHandler];
-[ULDiagnostics setStateHandle:];
-[ULDiagnostics setQueue:];
-[ULDiagnostics addCppProvider:];
-[ULDiagnostics getCppProviders];
-[ULDiagnostics _diagnosticsInfo];
-[ULDiagnostics _stateDataForInfo:];
-[ULDiagnostics cppProviders];
-[ULDiagnostics getCppProviderCount];
-[ULDiagnostics providersLock];
-[ULDiagnostics removeCppProvider:];
-[ULDiagnostics setCppProviders:];
-[ULDiagnostics setProvidersLock:];
```
