# `_MTLCommandBufferDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLCommandBufferDescriptor`
- 7 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _retainedReferences;
B _captureProgramAddressTable;
B _cloneIntersectionFunctionTablesPerDispatch;
B _disableFineGrainedComputePreemption;
Q _errorOptions;
@"<MTLLogState>" _logState;
@"<MTLDeadlineProfile>" _deadlineProfile;
```

## Properties

```
@property (TB,N,V_captureProgramAddressTable) captureProgramAddressTable;
@property (TB,N,V_cloneIntersectionFunctionTablesPerDispatch) cloneIntersectionFunctionTablesPerDispatch;
@property (T@"<MTLDeadlineProfile>",N,V_deadlineProfile) deadlineProfile;
@property (TB,N,V_disableFineGrainedComputePreemption) disableFineGrainedComputePreemption;
```

## Instance methods

```
-[_MTLCommandBufferDescriptor setErrorOptions:];
-[_MTLCommandBufferDescriptor errorOptions];
-[_MTLCommandBufferDescriptor deadlineProfile];
-[_MTLCommandBufferDescriptor retainedReferences];
-[_MTLCommandBufferDescriptor setDisableFineGrainedComputePreemption:];
-[_MTLCommandBufferDescriptor init];
-[_MTLCommandBufferDescriptor dealloc];
-[_MTLCommandBufferDescriptor setRetainedReferences:];
-[_MTLCommandBufferDescriptor setDeadlineProfile:];
-[_MTLCommandBufferDescriptor disableFineGrainedComputePreemption];
-[_MTLCommandBufferDescriptor captureProgramAddressTable];
-[_MTLCommandBufferDescriptor cloneIntersectionFunctionTablesPerDispatch];
-[_MTLCommandBufferDescriptor copyWithZone:];
-[_MTLCommandBufferDescriptor setLogState:];
-[_MTLCommandBufferDescriptor setCaptureProgramAddressTable:];
-[_MTLCommandBufferDescriptor logState];
-[_MTLCommandBufferDescriptor setCloneIntersectionFunctionTablesPerDispatch:];
```
