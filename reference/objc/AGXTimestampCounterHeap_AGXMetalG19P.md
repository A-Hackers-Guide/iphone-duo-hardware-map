# `AGXTimestampCounterHeap`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTL4CounterHeapGGDSPI`
- 4 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"AGXBuffer" heap_backing;
@"IOGPUMetalDevice" _device;
Q count;
q type;
```

## Properties

```
@property (T@"NSString",C) label;
@property (TQ,R,Vcount) count;
@property (Tq,R,Vtype) type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXTimestampCounterHeap label];
-[AGXTimestampCounterHeap setLabel:];
-[AGXTimestampCounterHeap dealloc];
-[AGXTimestampCounterHeap count];
-[AGXTimestampCounterHeap type];
-[AGXTimestampCounterHeap initWithDevice:descriptor:error:];
-[AGXTimestampCounterHeap fillWithByte:];
-[AGXTimestampCounterHeap invalidateCounterRange:];
-[AGXTimestampCounterHeap resolveCounterRange:];
```
