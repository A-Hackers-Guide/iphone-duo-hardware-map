# `CUIMeshBuffer`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MDLMeshBuffer`
- 4 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableData" _data;
Q _type;
@"<MDLMeshBufferZone>" _zone;
@"<MDLMeshBufferAllocator>" _allocator;
```

## Properties

```
@property (TQ,R,N) length;
@property (T@"<MDLMeshBufferAllocator>",R,&,N,V_allocator) allocator;
@property (T@"<MDLMeshBufferZone>",R,&,N,V_zone) zone;
@property (TQ,R,N,V_type) type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CUIMeshBuffer allocator];
-[CUIMeshBuffer zone];
-[CUIMeshBuffer init];
-[CUIMeshBuffer dealloc];
-[CUIMeshBuffer length];
-[CUIMeshBuffer type];
-[CUIMeshBuffer map];
-[CUIMeshBuffer copyWithZone:];
-[CUIMeshBuffer initWithBytes:andLength:ofType:];
-[CUIMeshBuffer fillData:offset:];
```
