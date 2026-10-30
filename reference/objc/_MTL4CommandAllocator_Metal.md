# `_MTL4CommandAllocator`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4CommandAllocatorGGDSPI`
- 4 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
Q _globalTraceObjectID;
@"MTLPrivateDataTable" _privateDataTable;
{vector<void (^)(), std::allocator<void (^)()>>="__begin_"^@?"__end_"^@?""{?="__cap_"^@?}} _resetHandlers;
```

## Properties

```
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",R) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4CommandAllocator initWithDevice:];
-[_MTL4CommandAllocator initWithDevice:descriptor:];
-[_MTL4CommandAllocator setPrivateData:privateDataOffset:logState:];
-[_MTL4CommandAllocator getPrivateDataAndOffset:privateDataOffset:];
-[_MTL4CommandAllocator device];
-[_MTL4CommandAllocator globalTraceObjectID];
-[_MTL4CommandAllocator allocatedSize];
-[_MTL4CommandAllocator dealloc];
-[_MTL4CommandAllocator reset];
-[_MTL4CommandAllocator addResetHandler:];
-[_MTL4CommandAllocator _executeResetHandlers];
```
